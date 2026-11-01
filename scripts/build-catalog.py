#!/usr/bin/env python3
"""Scan skills/*/SKILL.md, write catalog.json, refresh README browse tables."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
OUT = ROOT / "catalog.json"
README = ROOT / "README.md"
LLMS = ROOT / "llms.txt"
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)

REPO_SLUG = "kanjiandahai/skills-collection"
REPO_WEB = f"https://github.com/{REPO_SLUG}"
REPO_RAW = f"https://raw.githubusercontent.com/{REPO_SLUG}/main"
SCHEMA_VERSION = 1

CATEGORY_ORDER = [
    "discovery",
    "planning",
    "browser",
    "design",
    "media",
    "collaboration",
    "cloud",
    "documents",
    "finance",
    "engineering",
    "meta",
]

CATEGORY_LABELS = {
    "discovery": "发现与安装",
    "planning": "规划 / 澄清 / 工程决策",
    "browser": "浏览器与社交自动化",
    "design": "设计与前端体验",
    "media": "媒体与视频",
    "collaboration": "协作套件（飞书 / Lark）",
    "cloud": "云平台（Azure / Foundry 等）",
    "documents": "文档与办公格式",
    "finance": "金融",
    "engineering": "工程实现",
    "meta": "元 / 其它",
}

BEGIN = "<!-- BEGIN_CATALOG_BROWSE -->"
END = "<!-- END_CATALOG_BROWSE -->"
COUNT_BEGIN = "<!-- BEGIN_SKILL_COUNT -->"
COUNT_END = "<!-- END_SKILL_COUNT -->"

# Keep README 说明 cells short; soft target ~100, hard cut ~120.
DESC_SOFT = 100
DESC_HARD = 120


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = FRONTMATTER.match(text)
    if not match:
        return {}, text
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
    body = text[match.end() :]
    return data, body


def first_useful_body_line(body: str) -> str:
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            # Prefer prose over a heading that just repeats the name.
            continue
        if line.startswith("```") or line.startswith("|"):
            continue
        if line.startswith("- ") or line.startswith("* ") or line.startswith(">"):
            line = line.lstrip("-*> ").strip()
        if line:
            return line
    return ""


def shorten_description(text: str, soft: int = DESC_SOFT, hard: int = DESC_HARD) -> str:
    text = re.sub(r"\s+", " ", (text or "").strip())
    if not text:
        return ""
    if len(text) <= hard:
        return text
    cut = text[:soft].rstrip()
    # Prefer breaking at punctuation / space near the soft limit.
    for sep in ("。", "；", ";", "，", ",", "、", " ", "·"):
        idx = cut.rfind(sep)
        if idx >= soft // 2:
            cut = cut[: idx + (1 if sep in "。；;" else 0)].rstrip()
            break
    if not cut.endswith(("…", "...", "。")):
        cut = cut.rstrip("，,;；、 ") + "…"
    return cut


def md_cell(text: str) -> str:
    """Escape pipe/newlines so a value is safe inside a markdown table cell."""
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def load_entries() -> list[dict]:
    entries = []
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skill_id = skill_md.parent.name
        raw = skill_md.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        description = (meta.get("description") or "").strip()
        if not description:
            description = first_useful_body_line(body)
        rel = str(skill_md.relative_to(ROOT).as_posix())
        entry = {
            "id": skill_id,
            "name": meta.get("name", skill_id),
            "description": description,
            "tags": meta.get("tags", []),
            "category": meta.get("category", "meta"),
            "path": rel,
            "url": f"{REPO_WEB}/blob/main/{rel}",
            "raw_url": f"{REPO_RAW}/{rel}",
        }
        if "source" in meta:
            entry["source"] = meta["source"]
        for key in ("rank", "installs"):
            if key in meta:
                try:
                    entry[key] = int(meta[key])
                except (TypeError, ValueError):
                    entry[key] = meta[key]
        entries.append(entry)
    return entries


def fmt_int(n) -> str:
    if isinstance(n, int):
        return f"{n:,}"
    return "—"


def render_browse(entries: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_cat[e.get("category") or "meta"].append(e)

    lines: list[str] = []
    lines.append("## 分类一览")
    lines.append("")
    lines.append("| 分类 | 数量 | 说明 |")
    lines.append("|------|------|------|")
    for cat in CATEGORY_ORDER:
        items = by_cat.get(cat, [])
        if not items and cat == "meta":
            continue
        label = CATEGORY_LABELS.get(cat, cat)
        if items:
            lines.append(
                f"| [`{cat}`](#category-{cat}) | **{len(items)}** | {label} |"
            )
        else:
            lines.append(f"| `{cat}` | 0 | {label} |")
    for cat in sorted(by_cat.keys()):
        if cat not in CATEGORY_ORDER:
            items = by_cat[cat]
            lines.append(
                f"| [`{cat}`](#category-{cat}) | **{len(items)}** | {cat} |"
            )
    lines.append("")
    lines.append(
        f"合计：**{len(entries)}** 个 skill。完整机器索引见 [`catalog.json`](catalog.json)。"
    )
    lines.append("")
    lines.append("## 按分类浏览")
    lines.append("")

    cats = [c for c in CATEGORY_ORDER if by_cat.get(c)]
    cats += sorted(c for c in by_cat if c not in CATEGORY_ORDER)
    for cat in cats:
        items = by_cat[cat]
        items.sort(
            key=lambda e: (
                e["rank"] if isinstance(e.get("rank"), int) else 10**9,
                -(e["installs"] if isinstance(e.get("installs"), int) else -1),
                e["id"],
            )
        )
        label = CATEGORY_LABELS.get(cat, cat)
        lines.append(f'<a id="category-{cat}"></a>')
        lines.append(f"### `{cat}` · {label}（{len(items)}）")
        lines.append("")
        lines.append("| Rank | Skill | Source | Installs | 说明 |")
        lines.append("|-----:|-------|--------|---------:|------|")
        for e in items:
            rank = e["rank"] if isinstance(e.get("rank"), int) else "—"
            source = f"`{e['source']}`" if e.get("source") else "—"
            installs = fmt_int(e.get("installs"))
            blurb = md_cell(shorten_description(e.get("description", ""))) or "—"
            lines.append(
                f"| {rank} | [`{e['id']}`]({e['path']}) | {source} | {installs} | {blurb} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def update_readme(entries: list[dict]) -> None:
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    browse = render_browse(entries)

    if BEGIN in text and END in text:
        pre, rest = text.split(BEGIN, 1)
        _, post = rest.split(END, 1)
        text = pre + BEGIN + "\n" + browse + END + post
    else:
        text = text.rstrip() + "\n\n" + BEGIN + "\n" + browse + END + "\n"

    count_bit = str(len(entries))
    if COUNT_BEGIN in text and COUNT_END in text:
        pre, rest = text.split(COUNT_BEGIN, 1)
        _, post = rest.split(COUNT_END, 1)
        text = pre + COUNT_BEGIN + count_bit + COUNT_END + post

    README.write_text(text, encoding="utf-8")


def render_llms(entries: list[dict], updated_at: str) -> str:
    """Write an llms.txt index (https://llmstxt.org/) for agents/crawlers."""
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_cat[e.get("category") or "meta"].append(e)

    lines: list[str] = []
    lines.append("# skills-collection")
    lines.append("")
    lines.append(
        "> 持续增长的公开 Agent Skills 索引仓（聚合 + 分类 + 可滚动更新）。"
        " Growing public index of reusable agent skills."
    )
    lines.append("")
    lines.append(f"- Repo: {REPO_WEB}")
    lines.append(f"- Catalog: {REPO_RAW}/catalog.json")
    lines.append(f"- Install: `npx skills add {REPO_SLUG}`")
    lines.append(f"- Updated: {updated_at}")
    lines.append(f"- Skills: {len(entries)}")
    lines.append("")
    lines.append("## Categories")
    lines.append("")
    cats = [c for c in CATEGORY_ORDER if by_cat.get(c)]
    cats += sorted(c for c in by_cat if c not in CATEGORY_ORDER)
    for cat in cats:
        label = CATEGORY_LABELS.get(cat, cat)
        lines.append(f"- `{cat}` — {label} ({len(by_cat[cat])})")
    lines.append("")

    for cat in cats:
        items = sorted(
            by_cat[cat],
            key=lambda e: (
                e["rank"] if isinstance(e.get("rank"), int) else 10**9,
                e["id"],
            ),
        )
        label = CATEGORY_LABELS.get(cat, cat)
        lines.append(f"## {cat} · {label}")
        lines.append("")
        for e in items:
            url = e.get("url") or f"{REPO_WEB}/blob/main/{e['path']}"
            desc = shorten_description(e.get("description", ""), soft=140, hard=180)
            desc = desc.replace("\n", " ").strip() or "(no description)"
            lines.append(f"- [{e['id']}]({url}): {desc}")
        lines.append("")
    lines.append("## Optional")
    lines.append("")
    lines.append(f"- [README]({REPO_WEB}/blob/main/README.md): 人类可读索引与安装说明")
    lines.append(f"- [CONTRIBUTING]({REPO_WEB}/blob/main/CONTRIBUTING.md): 如何贡献新 skill")
    lines.append(f"- [UPDATE]({REPO_WEB}/blob/main/UPDATE.md): 刷新与维护流程")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    entries = load_entries()
    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    catalog = {
        "schema_version": SCHEMA_VERSION,
        "name": "skills-collection",
        "description": (
            "Growing public index of reusable agent skills "
            "(aggregated from skills.sh signals + manual contrib; categories)"
        ),
        "description_zh": (
            "持续增长的公开 Agent Skills 索引仓：聚合 + 分类 + 可滚动更新"
        ),
        "homepage": REPO_WEB,
        "install": f"npx skills add {REPO_SLUG}",
        "updated_at": updated_at,
        "skill_count": len(entries),
        "skills": entries,
    }
    OUT.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    update_readme(entries)
    LLMS.write_text(render_llms(entries, updated_at), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(entries)} skills)")
    print(f"Updated {README.relative_to(ROOT)} browse tables")
    print(f"Wrote {LLMS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
