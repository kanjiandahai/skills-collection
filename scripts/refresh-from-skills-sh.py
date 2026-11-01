#!/usr/bin/env python3
"""Ingest skills.sh ranking CSV as a discovery signal; grow the local catalog.

Never removes existing skills. Updates rank/installs/source on matches,
creates stub SKILL.md for new candidates among the top-N unique names.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SNAPSHOTS_DIR = ROOT / "data" / "snapshots"
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)

LATEST_URL = (
    "https://raw.githubusercontent.com/LinklyAI/best-skills/main/"
    "data/latest/raw/skills-sh.csv"
)
DATED_URL = (
    "https://raw.githubusercontent.com/LinklyAI/best-skills/main/"
    "data/{day}/raw/skills-sh.csv"
)
FALLBACK_DAY = "2026-11-01"

CATEGORY_LABELS = {
    "discovery": "发现与安装",
    "planning": "规划 / 澄清 / 工程决策",
    "browser": "浏览器与社交自动化",
    "design": "设计与前端体验",
    "media": "媒体与视频",
    "collaboration": "协作套件（飞书 / Lark）",
    "cloud": "云平台（Azure / Foundry 等）",
    "documents": "文档与办公格式",
    "engineering": "工程实现",
    "meta": "元 / 其它",
}


def fetch_csv_text(prefer_day: str | None = None) -> tuple[str, str]:
    """Return (csv_text, source_label). Prefer latest, then dated walk-back."""
    attempts: list[tuple[str, str]] = [("latest", LATEST_URL)]
    start = date.fromisoformat(prefer_day) if prefer_day else date.today()
    for i in range(0, 15):
        day = (start - timedelta(days=i)).isoformat()
        attempts.append((day, DATED_URL.format(day=day)))
    attempts.append((FALLBACK_DAY, DATED_URL.format(day=FALLBACK_DAY)))

    seen: set[str] = set()
    last_err: Exception | None = None
    for label, url in attempts:
        if url in seen:
            continue
        seen.add(url)
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                text = resp.read().decode("utf-8")
            if "view,rank" in text.splitlines()[0]:
                return text, label
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            last_err = exc
            continue
    raise RuntimeError(f"Could not download skills-sh.csv; last error: {last_err}")


def parse_all_time(csv_text: str) -> list[dict]:
    reader = csv.DictReader(io.StringIO(csv_text))
    rows: list[dict] = []
    for row in reader:
        if (row.get("view") or "").strip() != "all-time":
            continue
        try:
            rank = int(row["rank"])
            installs = int(row["installs"] or 0)
        except (KeyError, ValueError, TypeError):
            continue
        name = (row.get("name") or "").strip()
        source = (row.get("source") or "").strip()
        if not name:
            continue
        rows.append(
            {
                "rank": rank,
                "name": name,
                "source": source,
                "installs": installs,
                "id": name,
            }
        )
    rows.sort(key=lambda r: r["rank"])
    return rows


def dedupe_best_rank(rows: list[dict]) -> list[dict]:
    best: dict[str, dict] = {}
    for row in rows:
        key = row["name"]
        if key not in best or row["rank"] < best[key]["rank"]:
            best[key] = row
    return sorted(best.values(), key=lambda r: r["rank"])


def guess_category(name: str, source: str) -> str:
    n = name.lower()
    s = (source or "").lower()

    if n in {"find-skills", "skill-creator"} or n.startswith("setup-") or "find-skill" in n:
        return "discovery"
    if n.startswith("lark-") or "feishu" in s or "open.feishu" in s:
        return "collaboration"
    if (
        n.startswith("azure-")
        or n.startswith("entra-")
        or "appinsights" in n
        or "foundry" in n
        or "microsoft/azure" in s
        or "azure-skills" in s
    ):
        return "cloud"
    if (
        "hyperframes" in n
        or "remotion" in n
        or "video" in n
        or "avatar" in n
        or n in {"media-use", "ai-image-generation", "general-video"}
        or "heygen" in s
    ):
        return "media"
    if any(
        k in n
        for k in (
            "design",
            "frontend",
            "ui-taste",
            "web-design",
            "react-best",
        )
    ):
        return "design"
    if (
        "browser" in n
        or n.endswith("-automation")
        or n in {"reddit-automation", "twitter-automation", "agent-browser"}
    ):
        return "browser"
    if any(
        k in n
        for k in (
            "docx",
            "pdf",
            "pptx",
            "xlsx",
            "spreadsheet",
            "mermaid",
            "poster",
            "flowchart",
            "document",
        )
    ):
        return "documents"
    planning_keys = (
        "grill",
        "tdd",
        "handoff",
        "triage",
        "prototype",
        "domain-model",
        "teach",
        "codebase",
        "diagnos",
        "code-review",
        "implement",
        "ask-matt",
        "wayfinder",
        "to-spec",
        "research",
        "to-tickets",
        "wizard",
        "resolving-merge",
        "to-questionnaire",
        "planning",
        "architecture",
    )
    if any(k in n for k in planning_keys) or "mattpocock" in s:
        # mattpocock pack is mostly planning/process; keep google/azure out already
        if not n.startswith("google-"):
            return "planning"
    return "engineering"


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    data: dict = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [
                item.strip().strip("'\"")
                for item in inner.split(",")
                if item.strip()
            ]
        else:
            data[key] = value.strip("'\"")
    return data


def set_frontmatter_fields(text: str, updates: dict) -> str:
    """Update or insert scalar frontmatter keys; leave body untouched."""
    match = FRONTMATTER.match(text)
    if not match:
        # prepend new frontmatter
        lines = ["---"]
        for k, v in updates.items():
            lines.append(f"{k}: {v}")
        lines.append("---")
        lines.append("")
        return "\n".join(lines) + text.lstrip()

    block = match.group(1)
    lines = block.splitlines()
    keys_done: set[str] = set()
    new_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and ":" in stripped:
            key = stripped.split(":", 1)[0].strip()
            if key in updates:
                new_lines.append(f"{key}: {updates[key]}")
                keys_done.add(key)
                continue
        new_lines.append(line)
    for key, value in updates.items():
        if key not in keys_done:
            new_lines.append(f"{key}: {value}")
    new_block = "\n".join(new_lines)
    return text[: match.start(1)] + new_block + text[match.end(1) :]


def stub_body(name: str, category: str, source: str) -> str:
    label = CATEGORY_LABELS.get(category, category)
    src = source or "（未知上游）"
    return f"""# {name}

索引摘要（由 skills.sh 榜单自动灌入）。上游细节以 `{src}` 为准；本卡只保留触发场景与通用工作流。

## 何时用

- 任务落在「{label}」且与 `{name}` 能力名对齐时
- 用户点名该 skill，或本仓 `catalog.json` 检索命中时

## 工作流

1. **确认触发**：核对任务是否真需要该 skill，避免和同类能力重复调用。
2. **查上游**：打开 `source` 仓库或 registry，阅读官方 SKILL / README。
3. **落地执行**：按上游步骤完成；缺凭据/环境时先说明依赖。
4. **回写索引**（可选）：若发现更好的 description 或分类，开 PR 更新本卡。

## 成功标准

- 行为与上游 skill 一致，未凭空编造专有 API
- 用户能复现安装或启用方式（来自上游文档）
"""


def make_stub(row: dict, category: str) -> str:
    name = row["name"]
    tags = [category, "skills-sh", "stub"]
    tags_s = "[" + ", ".join(tags) + "]"
    desc = (
        f"来自 skills.sh 的 {category} 向 skill「{name}」。"
        f"安装量信号约 {row['installs']:,}；详情见上游 {row['source'] or 'registry'}。"
    )
    fm = "\n".join(
        [
            "---",
            f"name: {name}",
            f"description: {desc}",
            f"tags: {tags_s}",
            f"category: {category}",
            f"source: {row['source']}",
            f"rank: {row['rank']}",
            f"installs: {row['installs']}",
            "---",
            "",
        ]
    )
    return fm + stub_body(name, category, row["source"])


def index_existing() -> dict[str, Path]:
    """Map frontmatter name and folder id -> SKILL.md path."""
    by_key: dict[str, Path] = {}
    for path in SKILLS_DIR.glob("*/SKILL.md"):
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        folder = path.parent.name
        by_key[folder] = path
        name = meta.get("name")
        if isinstance(name, str) and name:
            by_key[name] = path
    return by_key


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--top",
        type=int,
        default=150,
        help="Max unique all-time names to consider for add/update (default 150)",
    )
    parser.add_argument(
        "--min-installs",
        type=int,
        default=0,
        help="Skip candidates below this all-time installs (default 0)",
    )
    parser.add_argument(
        "--day",
        type=str,
        default=None,
        help="Prefer this YYYY-MM-DD snapshot (still tries latest first)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing files",
    )
    args = parser.parse_args()

    csv_text, source_label = fetch_csv_text(prefer_day=args.day)
    all_time = parse_all_time(csv_text)
    unique = dedupe_best_rank(all_time)
    candidates = [
        r
        for r in unique
        if r["installs"] >= args.min_installs
    ][: args.top]

    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    # Use calendar day of source_label when dated; else UTC today
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", source_label):
        snap_day = source_label
    else:
        snap_day = datetime.now(timezone.utc).date().isoformat()
    snapshot_path = SNAPSHOTS_DIR / f"skills-sh-{snap_day}.json"
    snapshot_payload = {
        "fetched_from": source_label,
        "view": "all-time",
        "deduped_by": "name",
        "top": args.top,
        "min_installs": args.min_installs,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "candidates": candidates,
    }

    existing = index_existing()
    added = updated = unchanged = 0
    actions: list[str] = []

    for row in candidates:
        category = guess_category(row["name"], row["source"])
        row["category"] = category

        path = existing.get(row["name"]) or existing.get(row["id"])
        if path is None:
            skill_dir = SKILLS_DIR / row["id"]
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                path = skill_md
            else:
                content = make_stub(row, category)
                actions.append(f"ADD  {row['name']} -> {skill_md.relative_to(ROOT)}")
                if not args.dry_run:
                    skill_dir.mkdir(parents=True, exist_ok=True)
                    skill_md.write_text(content, encoding="utf-8")
                added += 1
                existing[row["name"]] = skill_md
                existing[row["id"]] = skill_md
                continue

        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        new_vals = {
            "rank": str(row["rank"]),
            "installs": str(row["installs"]),
        }
        if row["source"]:
            # only fill source if missing; do not clobber a richer/different source
            if not meta.get("source"):
                new_vals["source"] = row["source"]
            elif meta.get("source") == row["source"]:
                pass
            else:
                # keep local source; still refresh rank/installs
                pass

        changed = False
        for k, v in new_vals.items():
            cur = meta.get(k)
            if cur is None or str(cur) != str(v):
                changed = True
                break
        if not changed:
            unchanged += 1
            continue

        actions.append(
            f"UPD  {row['name']} rank={row['rank']} installs={row['installs']}"
        )
        if not args.dry_run:
            new_text = set_frontmatter_fields(text, new_vals)
            path.write_text(new_text, encoding="utf-8")
        updated += 1

    if not args.dry_run:
        snapshot_path.write_text(
            json.dumps(snapshot_payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build-catalog.py")],
            check=True,
            cwd=ROOT,
        )

    print(f"Source: {source_label}")
    print(f"Candidates considered: {len(candidates)} (top={args.top})")
    print(f"Added: {added}")
    print(f"Updated: {updated}")
    print(f"Unchanged: {unchanged}")
    if not args.dry_run:
        print(f"Snapshot: {snapshot_path.relative_to(ROOT)}")
    else:
        print("Dry-run: no files written")
    for line in actions[:40]:
        print(line)
    if len(actions) > 40:
        print(f"... ({len(actions) - 40} more)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
