# skills-collection

持续增长的公开 **Skills 索引仓**：**聚合 + 分类 + 可滚动更新**。

目标不是钉死一份 Top N 榜单，而是维护一份**只增不减**（除非主动删除）的能力索引：从 [skills.sh](https://www.skills.sh/) 等公开信号发现候选，用分类消化同质簇，并保留可运行的 `SKILL.md` 摘要或正文。

## 增长模型

1. **Bootstrap**：用 skills.sh All-Time 去重热度灌入一批种子（本仓曾在 2026-11-01 做过 Top100-unique 灌入）。
2. **持续收录**：定期跑刷新脚本，把榜单上尚未入库的高信号名称做成 stub 卡片；也欢迎手工 PR 补充文档向 / 私域向 skill。
3. **元数据刷新**：对已有 skill，用新快照更新 `rank` / `installs`（以及缺失的 `source`），**不覆盖**更丰富的 description 与正文。
4. **单调增长**：已入库 skill 默认保留；刷新脚本**不会**为了「对齐 Top N」而删卡。

当前收录 <!-- BEGIN_SKILL_COUNT -->157<!-- END_SKILL_COUNT --> 个 skill（计数由 `scripts/build-catalog.py` 维护）。

<!-- BEGIN_CATALOG_BROWSE -->
## 分类一览

| 分类 | 数量 | 说明 |
|------|------|------|
| [`discovery`](#category-discovery) | **4** | 发现与安装 |
| [`planning`](#category-planning) | **32** | 规划 / 澄清 / 工程决策 |
| [`browser`](#category-browser) | **3** | 浏览器与社交自动化 |
| [`design`](#category-design) | **9** | 设计与前端体验 |
| [`media`](#category-media) | **25** | 媒体与视频 |
| [`collaboration`](#category-collaboration) | **27** | 协作套件（飞书 / Lark） |
| [`cloud`](#category-cloud) | **21** | 云平台（Azure / Foundry 等） |
| [`documents`](#category-documents) | **6** | 文档与办公格式 |
| [`engineering`](#category-engineering) | **30** | 工程实现 |

合计：**157** 个 skill。完整机器索引见 [`catalog.json`](catalog.json)。

## 按分类浏览

<a id="category-discovery"></a>
### `discovery` · 发现与安装（4）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 1 | [`find-skills`](skills/find-skills/SKILL.md) | `vercel-labs/skills` | 4,143,610 |
| 13 | [`setup-matt-pocock-skills`](skills/setup-matt-pocock-skills/SKILL.md) | `mattpocock/skills` | 1,090,554 |
| 117 | [`setup-pre-commit`](skills/setup-pre-commit/SKILL.md) | `mattpocock/skills` | 511,903 |
| 187 | [`skill-creator`](skills/skill-creator/SKILL.md) | `anthropics/skills` | 420,614 |

<a id="category-planning"></a>
### `planning` · 规划 / 澄清 / 工程决策（32）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 2 | [`grill-me`](skills/grill-me/SKILL.md) | `mattpocock/skills` | 1,472,219 |
| 6 | [`grill-with-docs`](skills/grill-with-docs/SKILL.md) | `mattpocock/skills` | 1,260,788 |
| 8 | [`improve-codebase-architecture`](skills/improve-codebase-architecture/SKILL.md) | `mattpocock/skills` | 1,204,860 |
| 10 | [`tdd`](skills/tdd/SKILL.md) | `mattpocock/skills` | 1,178,984 |
| 14 | [`handoff`](skills/handoff/SKILL.md) | `mattpocock/skills` | 1,077,247 |
| 16 | [`grilling`](skills/grilling/SKILL.md) | `mattpocock/skills` | 1,028,898 |
| 17 | [`triage`](skills/triage/SKILL.md) | `mattpocock/skills` | 1,022,814 |
| 18 | [`prototype`](skills/prototype/SKILL.md) | `mattpocock/skills` | 1,021,735 |
| 26 | [`domain-modeling`](skills/domain-modeling/SKILL.md) | `mattpocock/skills` | 915,974 |
| 27 | [`teach`](skills/teach/SKILL.md) | `mattpocock/skills` | 896,162 |
| 28 | [`codebase-design`](skills/codebase-design/SKILL.md) | `mattpocock/skills` | 891,203 |
| 30 | [`diagnosing-bugs`](skills/diagnosing-bugs/SKILL.md) | `mattpocock/skills` | 872,766 |
| 54 | [`code-review`](skills/code-review/SKILL.md) | `mattpocock/skills` | 829,992 |
| 58 | [`implement`](skills/implement/SKILL.md) | `mattpocock/skills` | 808,925 |
| 63 | [`ask-matt`](skills/ask-matt/SKILL.md) | `mattpocock/skills` | 799,120 |
| 66 | [`wayfinder`](skills/wayfinder/SKILL.md) | `mattpocock/skills` | 754,357 |
| 67 | [`to-spec`](skills/to-spec/SKILL.md) | `mattpocock/skills` | 749,744 |
| 68 | [`research`](skills/research/SKILL.md) | `mattpocock/skills` | 747,235 |
| 70 | [`to-tickets`](skills/to-tickets/SKILL.md) | `mattpocock/skills` | 746,330 |
| 82 | [`wizard`](skills/wizard/SKILL.md) | `mattpocock/skills` | 584,449 |
| 97 | [`resolving-merge-conflicts`](skills/resolving-merge-conflicts/SKILL.md) | `mattpocock/skills` | 551,138 |
| 111 | [`to-questionnaire`](skills/to-questionnaire/SKILL.md) | `mattpocock/skills` | 528,458 |
| 113 | [`git-guardrails-claude-code`](skills/git-guardrails-claude-code/SKILL.md) | `mattpocock/skills` | 522,531 |
| 118 | [`writing-beats`](skills/writing-beats/SKILL.md) | `mattpocock/skills` | 505,261 |
| 119 | [`writing-shape`](skills/writing-shape/SKILL.md) | `mattpocock/skills` | 504,850 |
| 120 | [`writing-fragments`](skills/writing-fragments/SKILL.md) | `mattpocock/skills` | 504,164 |
| 121 | [`scaffold-exercises`](skills/scaffold-exercises/SKILL.md) | `mattpocock/skills` | 502,451 |
| 122 | [`writing-for-agents`](skills/writing-for-agents/SKILL.md) | `mattpocock/skills` | 500,813 |
| 123 | [`migrate-to-shoehorn`](skills/migrate-to-shoehorn/SKILL.md) | `mattpocock/skills` | 498,439 |
| 131 | [`wait-what`](skills/wait-what/SKILL.md) | `mattpocock/skills` | 479,572 |
| 151 | [`loop-me`](skills/loop-me/SKILL.md) | `mattpocock/skills` | 462,645 |
| 164 | [`claude-handoff`](skills/claude-handoff/SKILL.md) | `mattpocock/skills` | 444,437 |

<a id="category-browser"></a>
### `browser` · 浏览器与社交自动化（3）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 4 | [`agent-browser`](skills/agent-browser/SKILL.md) | `vercel-labs/agent-browser` | 1,324,536 |
| 9 | [`reddit-automation`](skills/reddit-automation/SKILL.md) | `flowkit-labs/skills` | 1,186,465 |
| 23 | [`twitter-automation`](skills/twitter-automation/SKILL.md) | `101-skills/superpowers` | 917,570 |

<a id="category-design"></a>
### `design` · 设计与前端体验（9）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 11 | [`design-mobile-apps`](skills/design-mobile-apps/SKILL.md) | `designed-by-ai/skills` | 1,152,654 |
| 15 | [`frontend-design`](skills/frontend-design/SKILL.md) | `anthropics/skills` | 1,058,803 |
| 29 | [`ui-taste`](skills/ui-taste/SKILL.md) | `uizze.sh` | 874,987 |
| 31 | [`vercel-react-best-practices`](skills/vercel-react-best-practices/SKILL.md) | `vercel-labs/agent-skills` | 858,669 |
| 57 | [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | `vercel-labs/agent-skills` | 809,234 |
| 72 | [`design-taste-frontend`](skills/design-taste-frontend/SKILL.md) | `leonxlnx/taste-skill` | 711,387 |
| 152 | [`high-end-visual-design`](skills/high-end-visual-design/SKILL.md) | `leonxlnx/taste-skill` | 458,850 |
| 153 | [`redesign-existing-projects`](skills/redesign-existing-projects/SKILL.md) | `leonxlnx/taste-skill` | 458,719 |
| 191 | [`ios-design`](skills/ios-design/SKILL.md) | `uizze.sh` | 417,203 |

<a id="category-media"></a>
### `media` · 媒体与视频（25）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 3 | [`hyperframes-cli`](skills/hyperframes-cli/SKILL.md) | `heygen-com/hyperframes` | 1,357,195 |
| 5 | [`hyperframes`](skills/hyperframes/SKILL.md) | `heygen-com/hyperframes` | 1,319,943 |
| 7 | [`media-use`](skills/media-use/SKILL.md) | `heygen-com/hyperframes` | 1,228,258 |
| 12 | [`hyperframes-registry`](skills/hyperframes-registry/SKILL.md) | `heygen-com/hyperframes` | 1,116,775 |
| 19 | [`hyperframes-animation`](skills/hyperframes-animation/SKILL.md) | `heygen-com/hyperframes` | 1,005,059 |
| 20 | [`hyperframes-core`](skills/hyperframes-core/SKILL.md) | `heygen-com/hyperframes` | 930,744 |
| 21 | [`ai-video-generation`](skills/ai-video-generation/SKILL.md) | `101-skills/superpowers` | 919,308 |
| 22 | [`ai-image-generation`](skills/ai-image-generation/SKILL.md) | `101-skills/superpowers` | 917,955 |
| 24 | [`ai-avatar-video`](skills/ai-avatar-video/SKILL.md) | `101-skills/superpowers` | 917,307 |
| 25 | [`hyperframes-creative`](skills/hyperframes-creative/SKILL.md) | `heygen-com/hyperframes` | 916,794 |
| 65 | [`hyperframes-keyframes`](skills/hyperframes-keyframes/SKILL.md) | `heygen-com/hyperframes` | 754,477 |
| 71 | [`remotion-best-practices`](skills/remotion-best-practices/SKILL.md) | `remotion-dev/skills` | 722,049 |
| 73 | [`hyperframes-audio`](skills/hyperframes-audio/SKILL.md) | `heygen-com/hyperframes` | 663,547 |
| 74 | [`general-video`](skills/general-video/SKILL.md) | `heygen-com/hyperframes` | 661,428 |
| 98 | [`remotion-to-hyperframes`](skills/remotion-to-hyperframes/SKILL.md) | `heygen-com/hyperframes` | 548,464 |
| 103 | [`product-launch-video`](skills/product-launch-video/SKILL.md) | `heygen-com/hyperframes` | 538,990 |
| 114 | [`faceless-explainer`](skills/faceless-explainer/SKILL.md) | `heygen-com/hyperframes` | 521,688 |
| 116 | [`motion-graphics`](skills/motion-graphics/SKILL.md) | `heygen-com/hyperframes` | 514,007 |
| 154 | [`slideshow`](skills/slideshow/SKILL.md) | `heygen-com/hyperframes` | 455,786 |
| 155 | [`embedded-captions`](skills/embedded-captions/SKILL.md) | `heygen-com/hyperframes` | 453,600 |
| 156 | [`hyperframes-studio`](skills/hyperframes-studio/SKILL.md) | `heygen-com/hyperframes` | 451,321 |
| 161 | [`pr-to-video`](skills/pr-to-video/SKILL.md) | `heygen-com/hyperframes` | 448,935 |
| 165 | [`video-edit`](skills/video-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 442,344 |
| 167 | [`image-to-video`](skills/image-to-video/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 440,560 |
| 188 | [`music-to-video`](skills/music-to-video/SKILL.md) | `heygen-com/hyperframes` | 418,974 |

<a id="category-collaboration"></a>
### `collaboration` · 协作套件（飞书 / Lark）（27）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 32 | [`lark-doc`](skills/lark-doc/SKILL.md) | `open.feishu.cn` | 838,580 |
| 33 | [`lark-base`](skills/lark-base/SKILL.md) | `open.feishu.cn` | 837,904 |
| 34 | [`lark-drive`](skills/lark-drive/SKILL.md) | `open.feishu.cn` | 837,894 |
| 35 | [`lark-shared`](skills/lark-shared/SKILL.md) | `open.feishu.cn` | 837,674 |
| 36 | [`lark-im`](skills/lark-im/SKILL.md) | `open.feishu.cn` | 836,933 |
| 37 | [`lark-calendar`](skills/lark-calendar/SKILL.md) | `open.feishu.cn` | 836,540 |
| 38 | [`lark-sheets`](skills/lark-sheets/SKILL.md) | `open.feishu.cn` | 836,441 |
| 39 | [`lark-approval`](skills/lark-approval/SKILL.md) | `open.feishu.cn` | 836,415 |
| 40 | [`lark-wiki`](skills/lark-wiki/SKILL.md) | `open.feishu.cn` | 836,338 |
| 41 | [`lark-contact`](skills/lark-contact/SKILL.md) | `open.feishu.cn` | 835,567 |
| 42 | [`lark-task`](skills/lark-task/SKILL.md) | `open.feishu.cn` | 835,460 |
| 43 | [`lark-slides`](skills/lark-slides/SKILL.md) | `open.feishu.cn` | 835,323 |
| 44 | [`lark-mail`](skills/lark-mail/SKILL.md) | `open.feishu.cn` | 835,281 |
| 45 | [`lark-whiteboard`](skills/lark-whiteboard/SKILL.md) | `open.feishu.cn` | 835,125 |
| 46 | [`lark-event`](skills/lark-event/SKILL.md) | `open.feishu.cn` | 835,035 |
| 47 | [`lark-openapi-explorer`](skills/lark-openapi-explorer/SKILL.md) | `open.feishu.cn` | 834,796 |
| 48 | [`lark-attendance`](skills/lark-attendance/SKILL.md) | `open.feishu.cn` | 834,696 |
| 49 | [`lark-skill-maker`](skills/lark-skill-maker/SKILL.md) | `open.feishu.cn` | 834,326 |
| 50 | [`lark-workflow-meeting-summary`](skills/lark-workflow-meeting-summary/SKILL.md) | `open.feishu.cn` | 834,184 |
| 51 | [`lark-minutes`](skills/lark-minutes/SKILL.md) | `open.feishu.cn` | 833,986 |
| 52 | [`lark-workflow-standup-report`](skills/lark-workflow-standup-report/SKILL.md) | `open.feishu.cn` | 833,899 |
| 53 | [`lark-vc`](skills/lark-vc/SKILL.md) | `open.feishu.cn` | 833,251 |
| 55 | [`lark-okr`](skills/lark-okr/SKILL.md) | `open.feishu.cn` | 815,656 |
| 62 | [`lark-markdown`](skills/lark-markdown/SKILL.md) | `open.feishu.cn` | 801,529 |
| 64 | [`lark-vc-agent`](skills/lark-vc-agent/SKILL.md) | `open.feishu.cn` | 777,869 |
| 69 | [`lark-apps`](skills/lark-apps/SKILL.md) | `open.feishu.cn` | 746,736 |
| 75 | [`lark-note`](skills/lark-note/SKILL.md) | `open.feishu.cn` | 618,126 |

<a id="category-cloud"></a>
### `cloud` · 云平台（Azure / Foundry 等）（21）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 81 | [`microsoft-foundry`](skills/microsoft-foundry/SKILL.md) | `microsoft/azure-skills` | 585,309 |
| 83 | [`azure-diagnostics`](skills/azure-diagnostics/SKILL.md) | `microsoft/azure-skills` | 576,049 |
| 84 | [`azure-prepare`](skills/azure-prepare/SKILL.md) | `microsoft/azure-skills` | 575,222 |
| 85 | [`azure-ai`](skills/azure-ai/SKILL.md) | `microsoft/azure-skills` | 574,510 |
| 86 | [`azure-deploy`](skills/azure-deploy/SKILL.md) | `microsoft/azure-skills` | 574,261 |
| 87 | [`azure-validate`](skills/azure-validate/SKILL.md) | `microsoft/azure-skills` | 573,818 |
| 88 | [`azure-storage`](skills/azure-storage/SKILL.md) | `microsoft/azure-skills` | 573,090 |
| 89 | [`azure-compliance`](skills/azure-compliance/SKILL.md) | `microsoft/azure-skills` | 572,695 |
| 90 | [`appinsights-instrumentation`](skills/appinsights-instrumentation/SKILL.md) | `microsoft/azure-skills` | 572,490 |
| 91 | [`azure-resource-lookup`](skills/azure-resource-lookup/SKILL.md) | `microsoft/azure-skills` | 572,439 |
| 92 | [`azure-resource-visualizer`](skills/azure-resource-visualizer/SKILL.md) | `microsoft/azure-skills` | 572,399 |
| 93 | [`entra-app-registration`](skills/entra-app-registration/SKILL.md) | `microsoft/azure-skills` | 572,356 |
| 94 | [`azure-kusto`](skills/azure-kusto/SKILL.md) | `microsoft/azure-skills` | 572,108 |
| 95 | [`azure-aigateway`](skills/azure-aigateway/SKILL.md) | `microsoft/azure-skills` | 571,711 |
| 96 | [`azure-messaging`](skills/azure-messaging/SKILL.md) | `microsoft/azure-skills` | 563,365 |
| 112 | [`azure-compute`](skills/azure-compute/SKILL.md) | `microsoft/azure-skills` | 528,193 |
| 115 | [`azure-cloud-migrate`](skills/azure-cloud-migrate/SKILL.md) | `microsoft/azure-skills` | 520,963 |
| 135 | [`azure-quotas`](skills/azure-quotas/SKILL.md) | `microsoft/azure-skills` | 476,733 |
| 146 | [`azure-upgrade`](skills/azure-upgrade/SKILL.md) | `microsoft/azure-skills` | 469,874 |
| 162 | [`azure-enterprise-infra-planner`](skills/azure-enterprise-infra-planner/SKILL.md) | `microsoft/azure-skills` | 446,495 |
| 166 | [`azure-kubernetes`](skills/azure-kubernetes/SKILL.md) | `microsoft/azure-skills` | 440,788 |

<a id="category-documents"></a>
### `documents` · 文档与办公格式（6）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| — | [`docx-documents`](skills/docx-documents/SKILL.md) | — | — |
| — | [`flowchart-mermaid`](skills/flowchart-mermaid/SKILL.md) | — | — |
| — | [`pdf-documents`](skills/pdf-documents/SKILL.md) | — | — |
| — | [`poster-design`](skills/poster-design/SKILL.md) | — | — |
| — | [`pptx-deck`](skills/pptx-deck/SKILL.md) | — | — |
| — | [`spreadsheet-xlsx`](skills/spreadsheet-xlsx/SKILL.md) | — | — |

<a id="category-engineering"></a>
### `engineering` · 工程实现（30）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 76 | [`caveman`](skills/caveman/SKILL.md) | `juliusbrussee/caveman` | 603,221 |
| 104 | [`google-agents-cli-adk-code`](skills/google-agents-cli-adk-code/SKILL.md) | `google/agents-cli` | 532,028 |
| 105 | [`google-agents-cli-deploy`](skills/google-agents-cli-deploy/SKILL.md) | `google/agents-cli` | 531,355 |
| 106 | [`google-agents-cli-publish`](skills/google-agents-cli-publish/SKILL.md) | `google/agents-cli` | 531,146 |
| 107 | [`google-agents-cli-workflow`](skills/google-agents-cli-workflow/SKILL.md) | `google/agents-cli` | 530,523 |
| 108 | [`google-agents-cli-eval`](skills/google-agents-cli-eval/SKILL.md) | `google/agents-cli` | 530,507 |
| 109 | [`google-agents-cli-scaffold`](skills/google-agents-cli-scaffold/SKILL.md) | `google/agents-cli` | 530,391 |
| 110 | [`google-agents-cli-observability`](skills/google-agents-cli-observability/SKILL.md) | `google/agents-cli` | 530,360 |
| 124 | [`paper-context-resolver`](skills/paper-context-resolver/SKILL.md) | `lllllllama/rigorpilot-skills` | 483,766 |
| 126 | [`repo-intake-and-plan`](skills/repo-intake-and-plan/SKILL.md) | `lllllllama/rigorpilot-skills` | 482,959 |
| 127 | [`minimal-run-and-audit`](skills/minimal-run-and-audit/SKILL.md) | `lllllllama/rigorpilot-skills` | 482,882 |
| 128 | [`env-and-assets-bootstrap`](skills/env-and-assets-bootstrap/SKILL.md) | `lllllllama/rigorpilot-skills` | 482,769 |
| 150 | [`supabase-postgres-best-practices`](skills/supabase-postgres-best-practices/SKILL.md) | `supabase/agent-skills` | 468,744 |
| 168 | [`nano-banana-2`](skills/nano-banana-2/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 440,246 |
| 169 | [`image-edit`](skills/image-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 439,802 |
| 170 | [`nano-banana-edit`](skills/nano-banana-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 439,642 |
| 171 | [`flux-kontext`](skills/flux-kontext/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 439,432 |
| 172 | [`wan-2-7`](skills/wan-2-7/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,872 |
| 173 | [`seedance-v2`](skills/seedance-v2/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,719 |
| 174 | [`gpt-image-edit`](skills/gpt-image-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,712 |
| 175 | [`happyhorse-1-0`](skills/happyhorse-1-0/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,632 |
| 176 | [`flux-2-klein`](skills/flux-2-klein/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,466 |
| 181 | [`vercel-composition-patterns`](skills/vercel-composition-patterns/SKILL.md) | `vercel-labs/agent-skills` | 430,333 |
| 182 | [`ui-ux-pro-max`](skills/ui-ux-pro-max/SKILL.md) | `nextlevelbuilder/ui-ux-pro-max-skill` | 427,165 |
| 184 | [`minimalist-ui`](skills/minimalist-ui/SKILL.md) | `leonxlnx/taste-skill` | 425,120 |
| 185 | [`caveman-commit`](skills/caveman-commit/SKILL.md) | `juliusbrussee/caveman` | 422,405 |
| 189 | [`caveman-compress`](skills/caveman-compress/SKILL.md) | `juliusbrussee/caveman` | 418,533 |
| 190 | [`caveman-review`](skills/caveman-review/SKILL.md) | `juliusbrussee/caveman` | 418,371 |
| 192 | [`kling-3-0`](skills/kling-3-0/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 415,690 |
| — | [`webapp-testing`](skills/webapp-testing/SKILL.md) | — | — |
<!-- END_CATALOG_BROWSE -->

## 数据来源 / 更新方式

| 来源 | 用途 |
|------|------|
| [skills.sh](https://www.skills.sh/) 导出（经 [LinklyAI/best-skills](https://github.com/LinklyAI/best-skills) 日快照 / `data/latest`） | **发现信号** + 热度元数据，不是目录上限 |
| 手工 PR / 早期沉淀 | 文档类等榜单未覆盖能力 |
| [`data/snapshots/`](data/snapshots/) | 历史灌入快照（输入），不是索引本身 |

种子说明：[`data/snapshots/skills-sh-top100-2026-11-01.json`](data/snapshots/skills-sh-top100-2026-11-01.json) 是 2026-11-01 的 bootstrap 记录；之后刷新会写入 `data/snapshots/skills-sh-YYYY-MM-DD.json`。

```bash
# 从最新榜单发现候选并更新热度（默认 Top 150 unique all-time）
python3 scripts/refresh-from-skills-sh.py

# 只重建机器索引 + README 分类表
python3 scripts/build-catalog.py
```

可选参数：`--top 200`、`--min-installs 100000`、`--day 2026-11-01`、`--dry-run`。  
Bot / CI 也可按同一命令周期性推送刷新（见 [`UPDATE.md`](UPDATE.md)）。

## 目录结构

```text
data/
  README.md
  snapshots/                 # 榜单输入快照（非索引）
skills/
  <skill-id>/
    SKILL.md                 # YAML frontmatter + Markdown
scripts/
  build-catalog.py           # catalog.json + README 分类表
  refresh-from-skills-sh.py  # 榜单发现 / 热度刷新
catalog.json
UPDATE.md
```

## Skill 约定

每个技能一个文件夹，文件夹名即 `id`（kebab-case）。`SKILL.md` frontmatter 示例：

```yaml
---
name: find-skills
description: 一句话说明何时使用该技能
tags: [discovery, catalog]
category: discovery
source: vercel-labs/skills   # 可选，来自榜单时填写
rank: 1                      # 可选，随快照刷新
installs: 4143610            # 可选，随快照刷新
---
```

正文写清：何时用、工作流、成功标准。保持通用；上游细节以 `source` 仓库为准。自动灌入的 stub 可后续人工加厚。

分类取值：`discovery` / `planning` / `browser` / `design` / `media` / `collaboration` / `cloud` / `documents` / `engineering` / `meta`。

## 贡献

1. 在 `skills/` 下新增目录与 `SKILL.md`（务必带 `category`）
2. 运行 `python3 scripts/build-catalog.py`
3. 开 PR 说明用途；若来自榜单请附 `source`（`rank` / `installs` 可留给刷新脚本）

也可用刷新脚本批量补洞，再开 PR 审 stub 质量。

## License

[MIT](LICENSE)
