# 贡献指南 · Contributing

感谢关注 [skills-collection](https://github.com/kanjiandahai/skills-collection)。本仓是**可持续增长的 Agent Skills 索引**：聚合公开信号、按能力分类、保留可浏览的 `SKILL.md`。欢迎补洞、加厚 stub、修正分类。

English summary: add or thicken a skill under `skills/<id>/SKILL.md`, run `python3 scripts/build-catalog.py`, open a PR. Prefer Chinese or bilingual descriptions; keep `category` accurate.

## 快速开始

1. Fork 本仓并创建分支。
2. 在 `skills/<kebab-case-id>/` 新增（或编辑）`SKILL.md`。
3. 本地运行：

```bash
python3 scripts/build-catalog.py
python3 scripts/check-catalog.py
```

4. 提交改动（通常包含 `SKILL.md`、`catalog.json`、`README.md`、`llms.txt`）。
5. 开 PR，说明用途与来源。

安装整仓试用：

```bash
npx skills add kanjiandahai/skills-collection
```

## Skill 约定

```yaml
---
name: example-skill
description: 一句话说明何时使用；触发词越好越容易被 agent 选中
tags: [finance, research]
category: finance
source: owner/repo   # 可选；来自 skills.sh / 上游仓时填写
rank: 42             # 可选；刷新脚本维护
installs: 123456     # 可选；刷新脚本维护
---
```

正文建议包含：何时用、步骤/工作流、成功标准。自动灌入的 stub 可以很短，欢迎 PR 加厚。

**分类**（`category`）：`discovery` / `planning` / `browser` / `design` / `media` / `collaboration` / `cloud` / `documents` / `finance` / `engineering` / `meta`。

## Good first issues（适合新手）

- 给 stub 补一句更准的 `description` 与正文小节
- 修正明显分错的 `category`
- 新增一个文档 / 金融 / 工程向、榜单未覆盖的 skill
- 帮某个 skill 补上可靠的 `source`（上游仓路径）

请先在 Issues 里认领，避免重复劳动。标签：`good first issue`。

## 刷新脚本（维护者）

从 skills.sh 信号发现新名称、刷新热度（**不会删卡**）：

```bash
python3 scripts/refresh-from-skills-sh.py
# 或预览：
python3 scripts/refresh-from-skills-sh.py --dry-run
```

详见 [`UPDATE.md`](UPDATE.md)。

## CI

PR 会跑 [`.github/workflows/catalog.yml`](.github/workflows/catalog.yml)：校验 `catalog.json` 与 `skills/*/SKILL.md`、README 计数、`llms.txt` 一致。本地先跑 `python3 scripts/check-catalog.py` 可避免红灯。

## License

贡献默认按仓库 [MIT](LICENSE) 许可。
