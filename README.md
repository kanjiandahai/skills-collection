# skills-collection

公开的 **Skills 索引仓**：用统一的 `SKILL.md` 格式收集、整理可复用的助手技能说明，方便人和各类 agent 直接浏览、复制或二次分发。

## 已收录（精选）

| Skill | 用途 |
|-------|------|
| [`flowchart-mermaid`](skills/flowchart-mermaid/SKILL.md) | Mermaid 流程图 / 时序 / 状态等 diagram-as-code |
| [`pptx-deck`](skills/pptx-deck/SKILL.md) | 做或改 PowerPoint（`.pptx`）演示文稿 |
| [`poster-design`](skills/poster-design/SKILL.md) | 海报 / 静态视觉稿（PNG、单页 PDF） |
| [`spreadsheet-xlsx`](skills/spreadsheet-xlsx/SKILL.md) | Excel / CSV 表格创建、编辑与分析 |

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
