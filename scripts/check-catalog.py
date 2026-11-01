#!/usr/bin/env python3
"""Validate catalog.json, skills/ dirs, and README count markers stay in sync."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CATALOG = ROOT / "catalog.json"
README = ROOT / "README.md"
LLMS = ROOT / "llms.txt"
COUNT_BEGIN = "<!-- BEGIN_SKILL_COUNT -->"
COUNT_END = "<!-- END_SKILL_COUNT -->"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    skill_mds = [p for p in skill_dirs if (p / "SKILL.md").is_file()]
    missing_md = [p.name for p in skill_dirs if not (p / "SKILL.md").is_file()]
    if missing_md:
        fail(f"skill dirs without SKILL.md: {missing_md}")

    disk_ids = {p.name for p in skill_mds}
    disk_count = len(disk_ids)

    if not CATALOG.is_file():
        fail("catalog.json missing")
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))

    for key in ("schema_version", "updated_at", "skill_count", "skills"):
        if key not in catalog:
            fail(f"catalog.json missing top-level key: {key}")

    if not isinstance(catalog["schema_version"], int) or catalog["schema_version"] < 1:
        fail(f"invalid schema_version: {catalog['schema_version']!r}")

    if not isinstance(catalog["updated_at"], str) or not catalog["updated_at"]:
        fail("updated_at must be a non-empty string")

    skills = catalog["skills"]
    if not isinstance(skills, list):
        fail("catalog.skills must be a list")

    catalog_ids = []
    for i, entry in enumerate(skills):
        if not isinstance(entry, dict):
            fail(f"skills[{i}] is not an object")
        for req in ("id", "path", "url", "category"):
            if req not in entry:
                fail(f"skills[{i}] missing {req}")
        sid = entry["id"]
        catalog_ids.append(sid)
        expected_path = f"skills/{sid}/SKILL.md"
        if entry["path"] != expected_path:
            fail(f"{sid}: path {entry['path']!r} != {expected_path!r}")
        if not (ROOT / entry["path"]).is_file():
            fail(f"{sid}: path does not exist on disk: {entry['path']}")
        if "/blob/" not in entry["url"] and "/raw.githubusercontent.com/" not in entry["url"]:
            fail(f"{sid}: url should point at github blob or raw: {entry['url']!r}")

    if len(catalog_ids) != len(set(catalog_ids)):
        dupes = sorted({x for x in catalog_ids if catalog_ids.count(x) > 1})
        fail(f"duplicate ids in catalog: {dupes}")

    catalog_id_set = set(catalog_ids)
    if catalog_id_set != disk_ids:
        only_catalog = sorted(catalog_id_set - disk_ids)
        only_disk = sorted(disk_ids - catalog_id_set)
        fail(
            "catalog ids != skills/*/SKILL.md: "
            f"only_in_catalog={only_catalog} only_on_disk={only_disk}"
        )

    if catalog["skill_count"] != disk_count:
        fail(
            f"catalog.skill_count={catalog['skill_count']} "
            f"!= disk skill count={disk_count}"
        )
    if len(skills) != disk_count:
        fail(f"len(catalog.skills)={len(skills)} != disk skill count={disk_count}")

    if not README.is_file():
        fail("README.md missing")
    readme = README.read_text(encoding="utf-8")
    if COUNT_BEGIN not in readme or COUNT_END not in readme:
        fail("README.md missing BEGIN_SKILL_COUNT / END_SKILL_COUNT markers")
    _, rest = readme.split(COUNT_BEGIN, 1)
    count_str, _ = rest.split(COUNT_END, 1)
    try:
        readme_count = int(count_str.strip())
    except ValueError:
        fail(f"README skill count marker is not an int: {count_str!r}")
    if readme_count != disk_count:
        fail(f"README skill count={readme_count} != disk skill count={disk_count}")

    # Soft checks: browse section and badges present
    if "<!-- BEGIN_CATALOG_BROWSE -->" not in readme:
        fail("README missing BEGIN_CATALOG_BROWSE marker")
    if "npx skills add kanjiandahai/skills-collection" not in readme:
        fail("README missing install command")

    if not LLMS.is_file():
        fail("llms.txt missing")
    llms = LLMS.read_text(encoding="utf-8")
    if "# skills-collection" not in llms:
        fail("llms.txt missing title")
    if str(disk_count) not in llms:
        # Allow if written as "Skills: N"
        if f"Skills: {disk_count}" not in llms:
            fail(f"llms.txt does not mention skill count {disk_count}")

    print(
        f"OK: {disk_count} skills; catalog schema_version="
        f"{catalog['schema_version']} updated_at={catalog['updated_at']}"
    )


if __name__ == "__main__":
    main()
