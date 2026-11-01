---
name: gpt-image-edit
description: 来自 skills.sh 的 engineering 向 skill「gpt-image-edit」。安装量信号约 438,712；详情见上游 prime-skills/runcomfy-agent-skills。
tags: [engineering, skills-sh, stub]
category: engineering
source: prime-skills/runcomfy-agent-skills
rank: 174
installs: 438712
---
# gpt-image-edit

索引摘要（由 skills.sh 榜单自动灌入）。上游细节以 `prime-skills/runcomfy-agent-skills` 为准；本卡只保留触发场景与通用工作流。

## 何时用

- 任务落在「工程实现」且与 `gpt-image-edit` 能力名对齐时
- 用户点名该 skill，或本仓 `catalog.json` 检索命中时

## 工作流

1. **确认触发**：核对任务是否真需要该 skill，避免和同类能力重复调用。
2. **查上游**：打开 `source` 仓库或 registry，阅读官方 SKILL / README。
3. **落地执行**：按上游步骤完成；缺凭据/环境时先说明依赖。
4. **回写索引**（可选）：若发现更好的 description 或分类，开 PR 更新本卡。

## 成功标准

- 行为与上游 skill 一致，未凭空编造专有 API
- 用户能复现安装或启用方式（来自上游文档）
