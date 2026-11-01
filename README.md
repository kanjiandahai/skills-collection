# skills-collection

公开的 **Skills 索引仓**：按 [skills.sh](https://www.skills.sh/) **All-Time** 热度收录去重后的 **Top 100** 技能卡片，并加上分类，方便浏览与二次分发。

## Top 100 口径

- 数据文件：[`data/skills-sh-top100-2026-11-01.json`](data/skills-sh-top100-2026-11-01.json)
- 原始榜单：`skills.sh` 导出（[LinklyAI/best-skills](https://github.com/LinklyAI/best-skills) `2026-11-01` 快照，`view=all-time`，按 `rank` 升序）
- **按 skill `name` 去重**，保留首次（最好）名次，取前 **100** 个唯一名称
- **不去掉** 飞书 Lark、Hyperframes、Azure 等产品向条目——一律收录，再用下方分类消化
- 每张卡是索引摘要（何时用 / 短工作流 / 成功标准），并标注上游 `source`；**不复制**上游专有长文

## 有没有必要分类？——有

Top 100 里协作套件、媒体管线、云技能扎堆，扁平列表很难扫。本仓给每个 skill 恰好一个 `category`：

| 分类 | 数量 | 说明 |
|------|------|------|
| [`discovery`](#category-discovery) | **2** | 发现与安装 |
| [`planning`](#category-planning) | **22** | 规划 / 澄清 / 工程决策 |
| [`browser`](#category-browser) | **3** | 浏览器与社交自动化 |
| [`design`](#category-design) | **6** | 设计与前端体验 |
| [`media`](#category-media) | **16** | 媒体与视频 |
| [`collaboration`](#category-collaboration) | **27** | 协作套件（飞书 / Lark） |
| [`cloud`](#category-cloud) | **16** | 云平台（Azure / Foundry 等） |
| `documents` | 0 | 文档与办公格式（Top100 未命中；本仓额外文档类见下） |
| [`engineering`](#category-engineering) | **8** | 工程实现（其余技术向） |
| `meta` | 0 | 元 / 其它（Top100 未命中；本仓额外文档类见下） |

Top100 合计：**100**。另有本仓额外技能 **9** 个（见文末）。

## 按分类浏览（Top 100）

<a id="category-discovery"></a>
### `discovery` · 发现与安装（2）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 1 | [`find-skills`](skills/find-skills/SKILL.md) | `vercel-labs/skills` | 4,143,610 |
| 13 | [`setup-matt-pocock-skills`](skills/setup-matt-pocock-skills/SKILL.md) | `mattpocock/skills` | 1,090,554 |

<a id="category-planning"></a>
### `planning` · 规划 / 澄清 / 工程决策（22）

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

<a id="category-browser"></a>
### `browser` · 浏览器与社交自动化（3）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 4 | [`agent-browser`](skills/agent-browser/SKILL.md) | `vercel-labs/agent-browser` | 1,324,536 |
| 9 | [`reddit-automation`](skills/reddit-automation/SKILL.md) | `flowkit-labs/skills` | 1,186,465 |
| 23 | [`twitter-automation`](skills/twitter-automation/SKILL.md) | `101-skills/superpowers` | 917,570 |

<a id="category-design"></a>
### `design` · 设计与前端体验（6）

| Rank | Skill | Source | Installs |
|-----:|-------|--------|---------:|
| 11 | [`design-mobile-apps`](skills/design-mobile-apps/SKILL.md) | `designed-by-ai/skills` | 1,152,654 |
| 15 | [`frontend-design`](skills/frontend-design/SKILL.md) | `anthropics/skills` | 1,058,803 |
| 29 | [`ui-taste`](skills/ui-taste/SKILL.md) | `uizze.sh` | 874,987 |
| 31 | [`vercel-react-best-practices`](skills/vercel-react-best-practices/SKILL.md) | `vercel-labs/agent-skills` | 858,669 |
| 57 | [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | `vercel-labs/agent-skills` | 809,234 |
| 72 | [`design-taste-frontend`](skills/design-taste-frontend/SKILL.md) | `leonxlnx/taste-skill` | 711,387 |

<a id="category-media"></a>
### `media` · 媒体与视频（16）

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
### `cloud` · 云平台（Azure / Foundry 等）（16）

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

<a id="category-engineering"></a>
### `engineering` · 工程实现（其余技术向）（8）

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

## 本仓额外（不在 Top100 唯一名列表内）

这些是仓库早期沉淀或文档向补充，保留完整正文：

| Skill | Category | 用途 |
|-------|----------|------|
| [`docx-documents`](skills/docx-documents/SKILL.md) | `documents` | 创建或编辑 Word 文档（.docx）：正文样式、标题层级、目录、表格、页眉页脚、批注与修订 |
| [`flowchart-mermaid`](skills/flowchart-mermaid/SKILL.md) | `documents` | 用 Mermaid 画清晰、可渲染的流程图与相关示意图 |
| [`hello-world`](skills/hello-world/SKILL.md) | `meta` | 示例技能：演示 skills-collection 的目录与 frontmatter 约定；新技能可复制此模板改写 |
| [`pdf-documents`](skills/pdf-documents/SKILL.md) | `documents` | 创建、阅读、拆合或填写 PDF |
| [`poster-design`](skills/poster-design/SKILL.md) | `documents` | 设计海报、静态视觉稿、活动宣传图或单页艺术构图 |
| [`pptx-deck`](skills/pptx-deck/SKILL.md) | `documents` | 制作或改写 PowerPoint / .pptx 幻灯片（路演、汇报、培训、方案） |
| [`skill-creator`](skills/skill-creator/SKILL.md) | `discovery` | 从零编写、改写并打磨 Agent Skill（SKILL.md） |
| [`spreadsheet-xlsx`](skills/spreadsheet-xlsx/SKILL.md) | `documents` | 创建、编辑、分析或美化电子表格（.xlsx / .csv / .tsv） |
| [`webapp-testing`](skills/webapp-testing/SKILL.md) | `engineering` | 为 Web 应用设计并运行可靠的 UI/端到端测试与冒烟检查 |

完整机器索引见 [`catalog.json`](catalog.json)。

## 目录结构

```text
data/
  skills-sh-top100-2026-11-01.json   # Top100 快照
skills/
  <skill-id>/
    SKILL.md                         # YAML frontmatter + Markdown
scripts/
  build-catalog.py                   # 生成 catalog.json
catalog.json
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
rank: 1                      # 可选
installs: 4143610            # 可选
---
```

正文写清：何时用、工作流、成功标准。保持通用；上游细节以 `source` 仓库为准。

## 生成本地索引

```bash
python3 scripts/build-catalog.py
```

## 贡献

1. 在 `skills/` 下新增目录与 `SKILL.md`（带 `category`）
2. 运行 `python3 scripts/build-catalog.py`
3. 开 PR 说明用途；若来自榜单请附 `source` / `rank`

## License

[MIT](LICENSE)
