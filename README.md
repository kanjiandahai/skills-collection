# skills-collection

公开的 **Skills 索引仓**：用统一的 `SKILL.md` 格式收集、整理可复用的助手技能说明，方便人和各类 agent 直接浏览、复制或二次分发。

## 常用 Top 10（本仓口径）

综合 [skills.sh](https://www.skills.sh/) All-Time 安装量与 Anthropic 官方技能库热度，**剔除** Hyperframes / 飞书等强产品绑定套件与 `setup-*` 元安装包后，收录如下 10 个通用能力（2026-11 快照）：

| # | Skill | 为何进榜 |
|---|-------|----------|
| 1 | [`find-skills`](skills/find-skills/SKILL.md) | skills.sh 全站安装量第一：发现/安装 skill |
| 2 | [`grill-me`](skills/grill-me/SKILL.md) | 需求/方案高压追问（Matt Pocock 系热门） |
| 3 | [`agent-browser`](skills/agent-browser/SKILL.md) | 浏览器自动化操作与验证 |
| 4 | [`frontend-design`](skills/frontend-design/SKILL.md) | Anthropic 库安装量最高档：有辨识度的 UI |
| 5 | [`tdd`](skills/tdd/SKILL.md) | 测试驱动开发工作流 |
| 6 | [`improve-codebase-architecture`](skills/improve-codebase-architecture/SKILL.md) | 架构梳理与分步重构 |
| 7 | [`skill-creator`](skills/skill-creator/SKILL.md) | 编写与打磨 SKILL.md |
| 8 | [`pdf-documents`](skills/pdf-documents/SKILL.md) | PDF 读写与拆合（文档技能刚需） |
| 9 | [`docx-documents`](skills/docx-documents/SKILL.md) | Word / docx 结构化写作 |
| 10 | [`webapp-testing`](skills/webapp-testing/SKILL.md) | Web 应用 E2E / 冒烟测试 |

## 其他已收录

| Skill | 用途 |
|-------|------|
| [`pptx-deck`](skills/pptx-deck/SKILL.md) | PowerPoint 演示文稿 |
| [`spreadsheet-xlsx`](skills/spreadsheet-xlsx/SKILL.md) | Excel / CSV |
| [`poster-design`](skills/poster-design/SKILL.md) | 海报 / 静态视觉 |
| [`flowchart-mermaid`](skills/flowchart-mermaid/SKILL.md) | Mermaid 流程图 |
| [`hello-world`](skills/hello-world/SKILL.md) | 格式示例 |

完整机器索引见 [`catalog.json`](catalog.json)。


## 目录结构

```text
skills/
  <skill-id>/
    SKILL.md          # 技能正文（YAML frontmatter + Markdown）
scripts/
  build-catalog.py    # 从 skills/*/SKILL.md 生成 catalog.json
catalog.json          # 机器可读索引（可由脚本重新生成）
```

## Skill 约定

每个技能一个文件夹，文件夹名即 `id`（建议 kebab-case）。`SKILL.md` 开头使用 YAML frontmatter：

```yaml
---
name: hello-world
description: 一句话说明何时使用该技能
tags: [example, starter]
---
```

正文写清：什么时候用、要做什么、成功标准与注意事项。保持通用、可复用，不要写死某个私人账号或本地路径。

## 生成本地索引

```bash
python3 scripts/build-catalog.py
```

会扫描 `skills/*/SKILL.md`，写出根目录 `catalog.json`。

## 贡献

1. 在 `skills/` 下新增目录与 `SKILL.md`
2. 运行 `python3 scripts/build-catalog.py` 更新索引
3. 开 PR 说明技能用途与适用范围

## License

[MIT](LICENSE)
