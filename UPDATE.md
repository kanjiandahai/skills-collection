# 如何更新本索引仓

## 从 skills.sh 刷新（推荐）

```bash
python3 scripts/refresh-from-skills-sh.py
```

行为概要：

1. 下载最新 CSV（优先 `data/latest`，否则按日期回退约 14 天）
2. 取 `view=all-time`，按 `name` 去重保留最好名次
3. 对默认 Top 150 候选：已存在则更新 `rank` / `installs`（缺失才补 `source`）；不存在则建 stub `SKILL.md`
4. 写入 `data/snapshots/skills-sh-YYYY-MM-DD.json`
5. 调用 `build-catalog.py` 重建 `catalog.json` 与 README 分类表

常用选项：

```bash
python3 scripts/refresh-from-skills-sh.py --dry-run
python3 scripts/refresh-from-skills-sh.py --top 200 --min-installs 100000
python3 scripts/refresh-from-skills-sh.py --day 2026-11-01
```

**不会删除**已有 skill。周期性 Bot/CI 可直接跑同一命令后 `git commit` / `git push`。

## 只重建目录

```bash
python3 scripts/build-catalog.py
```

## 手工新增一个 skill

1. 新建 `skills/<id>/SKILL.md`，填写 frontmatter（含 `category`）与正文
2. `python3 scripts/build-catalog.py`
3. 提交 PR

## 分类

常用 `category`：`discovery` / `planning` / `browser` / `design` / `media` / `collaboration` / `cloud` / `documents` / `finance` / `engineering` / `meta`。展示名由 `scripts/build-catalog.py` 的 `CATEGORY_LABELS` 维护（`finance` → 金融）。
