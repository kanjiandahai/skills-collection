---
name: azure-quotas
description: 来自 skills.sh 的 cloud 向 skill「azure-quotas」。安装量信号约 476,733；详情见上游 microsoft/azure-skills。
tags: [cloud, skills-sh, stub]
category: cloud
source: microsoft/azure-skills
rank: 135
installs: 476733
---
# azure-quotas

索引摘要（由 skills.sh 榜单自动灌入）。上游细节以 `microsoft/azure-skills` 为准；本卡只保留触发场景与通用工作流。

## 何时用

- 任务落在「云平台（Azure / Foundry 等）」且与 `azure-quotas` 能力名对齐时
- 用户点名该 skill，或本仓 `catalog.json` 检索命中时

## 工作流

1. **确认触发**：核对任务是否真需要该 skill，避免和同类能力重复调用。
2. **查上游**：打开 `source` 仓库或 registry，阅读官方 SKILL / README。
3. **落地执行**：按上游步骤完成；缺凭据/环境时先说明依赖。
4. **回写索引**（可选）：若发现更好的 description 或分类，开 PR 更新本卡。

## 成功标准

- 行为与上游 skill 一致，未凭空编造专有 API
- 用户能复现安装或启用方式（来自上游文档）
