#!/usr/bin/env python3
"""Scan skills/*/SKILL.md and write catalog.json at the repo root."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
OUT = ROOT / "catalog.json"
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


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


def main() -> None:
    entries = []
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skill_id = skill_md.parent.name
        meta = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        entries.append(
            {
                "id": skill_id,
                "name": meta.get("name", skill_id),
                "description": meta.get("description", ""),
                "tags": meta.get("tags", []),
                "path": str(skill_md.relative_to(ROOT).as_posix()),
            }
        )

    catalog = {
        "name": "skills-collection",
        "description": "Public index of reusable agent skills",
        "skills": entries,
    }
    OUT.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(entries)} skills)")


if __name__ == "__main__":
    main()
