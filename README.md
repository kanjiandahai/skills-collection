# skills-collection

[![GitHub stars](https://img.shields.io/github/stars/kanjiandahai/skills-collection?style=social)](https://github.com/kanjiandahai/skills-collection/stargazers)
[![License: MIT](https://img.shields.io/github/license/kanjiandahai/skills-collection)](LICENSE)
[![Skills](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fkanjiandahai%2Fskills-collection%2Fmain%2Fcatalog.json&query=%24.skill_count&label=skills)](catalog.json)
[![Catalog CI](https://github.com/kanjiandahai/skills-collection/actions/workflows/catalog.yml/badge.svg)](https://github.com/kanjiandahai/skills-collection/actions/workflows/catalog.yml)
[![Install](https://img.shields.io/badge/install-npx%20skills%20add-black)](#安装)

持续增长的公开 **Skills 索引仓**：**聚合 + 分类 + 可滚动更新**。

Growing public index of reusable agent skills — aggregate, categorize, and keep updating (not a frozen Top-N list).

目标不是钉死一份 Top N 榜单，而是维护一份**只增不减**（除非主动删除）的能力索引：从 [skills.sh](https://www.skills.sh/) 等公开信号发现候选，用分类消化同质簇，并保留可运行的 `SKILL.md` 摘要或正文。

## 安装

```bash
npx skills add kanjiandahai/skills-collection
```

机器可读索引：[`catalog.json`](catalog.json) · [`llms.txt`](llms.txt)

## 增长模型

1. **Bootstrap**：用 skills.sh All-Time 去重热度灌入一批种子（本仓曾在 2026-11-01 做过 Top100-unique 灌入）。
2. **持续收录**：定期跑刷新脚本，把榜单上尚未入库的高信号名称做成 stub 卡片；也欢迎手工 PR 补充文档向 / 私域向 skill。
3. **元数据刷新**：对已有 skill，用新快照更新 `rank` / `installs`（以及缺失的 `source`），**不覆盖**更丰富的 description 与正文。
4. **单调增长**：已入库 skill 默认保留；刷新脚本**不会**为了「对齐 Top N」而删卡。

当前收录 <!-- BEGIN_SKILL_COUNT -->169<!-- END_SKILL_COUNT --> 个 skill（计数由 `scripts/build-catalog.py` 维护）。

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
| [`finance`](#category-finance) | **12** | 金融 |
| [`engineering`](#category-engineering) | **30** | 工程实现 |

合计：**169** 个 skill。完整机器索引见 [`catalog.json`](catalog.json)。

## 按分类浏览

<a id="category-discovery"></a>
### `discovery` · 发现与安装（4）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 1 | [`find-skills`](skills/find-skills/SKILL.md) | `vercel-labs/skills` | 4,143,610 | 发现、筛选并安装合适的 Agent Skill。用户说找不到 skill、有没有某某能力、帮我搜 skill、skills.sh / npx skills、或不知道该装哪个 skill 时使用。 |
| 13 | [`setup-matt-pocock-skills`](skills/setup-matt-pocock-skills/SKILL.md) | `mattpocock/skills` | 1,090,554 | 安装/配置 Matt Pocock 技能包。用户要启用该套 skills 时使用。 |
| 117 | [`setup-pre-commit`](skills/setup-pre-commit/SKILL.md) | `mattpocock/skills` | 511,903 | 来自 skills.sh 的 discovery 向 skill「setup-pre-commit」。安装量信号约 511,903；详情见上游 mattpocock/skills。 |
| 187 | [`skill-creator`](skills/skill-creator/SKILL.md) | `anthropics/skills` | 420,614 | 从零编写、改写并打磨 Agent Skill（SKILL.md）。用户要创建 skill、优化 description 触发、给 skill 加评测、或把一段工作流沉淀成 skill 时使用。 |

<a id="category-planning"></a>
### `planning` · 规划 / 澄清 / 工程决策（32）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 2 | [`grill-me`](skills/grill-me/SKILL.md) | `mattpocock/skills` | 1,472,219 | 对计划或设计做高压追问，直到决策树走通、双方理解一致。用户说 grill me、拷问一下方案、帮我抠需求、压力测试设计、把计划问清楚时使用。 |
| 6 | [`grill-with-docs`](skills/grill-with-docs/SKILL.md) | `mattpocock/skills` | 1,260,788 | 结合文档资料做高压方案追问。用户要边读文档边拷问设计时使用。 |
| 8 | [`improve-codebase-architecture`](skills/improve-codebase-architecture/SKILL.md) | `mattpocock/skills` | 1,204,860 | 诊断并改进代码库架构：边界、模块化、依赖方向与可测性。用户说架构混乱、拆模块、减耦合、理清分层、改进 codebase architecture 时使用。 |
| 10 | [`tdd`](skills/tdd/SKILL.md) | `mattpocock/skills` | 1,178,984 | 用测试驱动实现功能：先写失败测试，再写最小实现，再重构。用户要求 TDD、先写测试、红绿重构、或实现前先定行为规格时使用。 |
| 14 | [`handoff`](skills/handoff/SKILL.md) | `mattpocock/skills` | 1,077,247 | 把上下文整理成可交接的 handoff 文档。用户换人/换会话继续做时使用。 |
| 16 | [`grilling`](skills/grilling/SKILL.md) | `mattpocock/skills` | 1,028,898 | 持续追问以澄清模糊需求（grilling 流程）。用户要被系统化拷问时使用。 |
| 17 | [`triage`](skills/triage/SKILL.md) | `mattpocock/skills` | 1,022,814 | 对问题/任务做分流定级。用户一堆 issue/bug 不知先做哪个时使用。 |
| 18 | [`prototype`](skills/prototype/SKILL.md) | `mattpocock/skills` | 1,021,735 | 快速做出可验证原型。用户要先跑通 demo 再谈完美实现时使用。 |
| 26 | [`domain-modeling`](skills/domain-modeling/SKILL.md) | `mattpocock/skills` | 915,974 | 梳理领域模型与边界上下文。用户要 DDD/领域语言/模型图时使用。 |
| 27 | [`teach`](skills/teach/SKILL.md) | `mattpocock/skills` | 896,162 | 把复杂主题教给用户或写成教程。用户说「教我」「讲清楚」时使用。 |
| 28 | [`codebase-design`](skills/codebase-design/SKILL.md) | `mattpocock/skills` | 891,203 | 从零或重构时设计代码库结构。用户要定目录/模块边界时使用。 |
| 30 | [`diagnosing-bugs`](skills/diagnosing-bugs/SKILL.md) | `mattpocock/skills` | 872,766 | 系统化定位缺陷根因。用户卡在诡异 bug 时使用。 |
| 54 | [`code-review`](skills/code-review/SKILL.md) | `mattpocock/skills` | 829,992 | 结构化代码审查。用户要 review PR/改动时使用。 |
| 58 | [`implement`](skills/implement/SKILL.md) | `mattpocock/skills` | 808,925 | 把已澄清的规格落地为实现。用户说「按方案实现」时使用。 |
| 63 | [`ask-matt`](skills/ask-matt/SKILL.md) | `mattpocock/skills` | 799,120 | 以 Matt 风格答疑或给工程建议。用户要该系列方法论建议时使用。 |
| 66 | [`wayfinder`](skills/wayfinder/SKILL.md) | `mattpocock/skills` | 754,357 | 在未知代码库里找路：定位模块与改动点。用户「从哪改」时使用。 |
| 67 | [`to-spec`](skills/to-spec/SKILL.md) | `mattpocock/skills` | 749,744 | 把讨论收敛成规格说明。用户要写 spec 时使用。 |
| 68 | [`research`](skills/research/SKILL.md) | `mattpocock/skills` | 747,235 | 针对技术/产品问题做有出处的调研。用户要调研对比时使用。 |
| 70 | [`to-tickets`](skills/to-tickets/SKILL.md) | `mattpocock/skills` | 746,330 | 把规格拆成可执行工单。用户要拆任务/issue 时使用。 |
| 82 | [`wizard`](skills/wizard/SKILL.md) | `mattpocock/skills` | 584,449 | 用向导式步骤带用户做完复杂配置。用户要一步步引导时使用。 |
| 97 | [`resolving-merge-conflicts`](skills/resolving-merge-conflicts/SKILL.md) | `mattpocock/skills` | 551,138 | 解决 Git 合并冲突。用户遇到 conflict 时使用。 |
| 111 | [`to-questionnaire`](skills/to-questionnaire/SKILL.md) | `mattpocock/skills` | 528,458 | 把模糊需求变成问卷/检查表。用户要收集决策信息时使用。 |
| 113 | [`git-guardrails-claude-code`](skills/git-guardrails-claude-code/SKILL.md) | `mattpocock/skills` | 522,531 | 来自 skills.sh 的 planning 向 skill「git-guardrails-claude-code」。安装量信号约 522,531；详情见上游 mattpocock/skills。 |
| 118 | [`writing-beats`](skills/writing-beats/SKILL.md) | `mattpocock/skills` | 505,261 | 来自 skills.sh 的 planning 向 skill「writing-beats」。安装量信号约 505,261；详情见上游 mattpocock/skills。 |
| 119 | [`writing-shape`](skills/writing-shape/SKILL.md) | `mattpocock/skills` | 504,850 | 来自 skills.sh 的 planning 向 skill「writing-shape」。安装量信号约 504,850；详情见上游 mattpocock/skills。 |
| 120 | [`writing-fragments`](skills/writing-fragments/SKILL.md) | `mattpocock/skills` | 504,164 | 来自 skills.sh 的 planning 向 skill「writing-fragments」。安装量信号约 504,164；详情见上游 mattpocock/skills。 |
| 121 | [`scaffold-exercises`](skills/scaffold-exercises/SKILL.md) | `mattpocock/skills` | 502,451 | 来自 skills.sh 的 planning 向 skill「scaffold-exercises」。安装量信号约 502,451；详情见上游 mattpocock/skills。 |
| 122 | [`writing-for-agents`](skills/writing-for-agents/SKILL.md) | `mattpocock/skills` | 500,813 | 来自 skills.sh 的 planning 向 skill「writing-for-agents」。安装量信号约 500,813；详情见上游 mattpocock/skills。 |
| 123 | [`migrate-to-shoehorn`](skills/migrate-to-shoehorn/SKILL.md) | `mattpocock/skills` | 498,439 | 来自 skills.sh 的 planning 向 skill「migrate-to-shoehorn」。安装量信号约 498,439；详情见上游 mattpocock/skills。 |
| 131 | [`wait-what`](skills/wait-what/SKILL.md) | `mattpocock/skills` | 479,572 | 来自 skills.sh 的 planning 向 skill「wait-what」。安装量信号约 479,572；详情见上游 mattpocock/skills。 |
| 151 | [`loop-me`](skills/loop-me/SKILL.md) | `mattpocock/skills` | 462,645 | 来自 skills.sh 的 planning 向 skill「loop-me」。安装量信号约 462,645；详情见上游 mattpocock/skills。 |
| 164 | [`claude-handoff`](skills/claude-handoff/SKILL.md) | `mattpocock/skills` | 444,437 | 来自 skills.sh 的 planning 向 skill「claude-handoff」。安装量信号约 444,437；详情见上游 mattpocock/skills。 |

<a id="category-browser"></a>
### `browser` · 浏览器与社交自动化（3）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 4 | [`agent-browser`](skills/agent-browser/SKILL.md) | `vercel-labs/agent-browser` | 1,324,536 | 指导助手用浏览器完成页面操作、抓取与验证（打开、点击、填写、截图、断言）。用户要自动化网页流程、检查线上 UI、登录后操作站点、或用无头/有头浏览器跑任务时使用。 |
| 9 | [`reddit-automation`](skills/reddit-automation/SKILL.md) | `flowkit-labs/skills` | 1,186,465 | 自动化 Reddit 浏览、发帖或互动流程（需遵守平台规则）。用户要 Reddit 代理操作时使用。 |
| 23 | [`twitter-automation`](skills/twitter-automation/SKILL.md) | `101-skills/superpowers` | 917,570 | 自动化 X/Twitter 浏览与操作（遵守平台规则）。用户要推特代理流程时使用。 |

<a id="category-design"></a>
### `design` · 设计与前端体验（9）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 11 | [`design-mobile-apps`](skills/design-mobile-apps/SKILL.md) | `designed-by-ai/skills` | 1,152,654 | 移动端 App UI/交互设计指导。用户做 iOS/Android/跨端界面时使用。 |
| 15 | [`frontend-design`](skills/frontend-design/SKILL.md) | `anthropics/skills` | 1,058,803 | 做有辨识度的前端视觉与界面，避免千篇一律的 AI 默认审美。新建页面、改版 UI、落地页、仪表盘皮肤，或用户抱怨「看起来像模板」时使用。 |
| 29 | [`ui-taste`](skills/ui-taste/SKILL.md) | `uizze.sh` | 874,987 | 提升 UI 品味与细节一致性。用户觉得界面「土/乱/廉价」时使用。 |
| 31 | [`vercel-react-best-practices`](skills/vercel-react-best-practices/SKILL.md) | `vercel-labs/agent-skills` | 858,669 | 按 Vercel 倡导的 React/Next 最佳实践检查与改写。用户做 React/Next 优化时使用。 |
| 57 | [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | `vercel-labs/agent-skills` | 809,234 | 对照现代 Web 设计准则检查页面。用户要可用性/无障碍/视觉规范时使用。 |
| 72 | [`design-taste-frontend`](skills/design-taste-frontend/SKILL.md) | `leonxlnx/taste-skill` | 711,387 | 设计与前端体验相关技能 `design-taste-frontend`。当任务匹配该上游 skill 名称与场景时使用。 |
| 152 | [`high-end-visual-design`](skills/high-end-visual-design/SKILL.md) | `leonxlnx/taste-skill` | 458,850 | 来自 skills.sh 的 design 向 skill「high-end-visual-design」。安装量信号约 458,850；详情见上游 leonxlnx/taste-skill。 |
| 153 | [`redesign-existing-projects`](skills/redesign-existing-projects/SKILL.md) | `leonxlnx/taste-skill` | 458,719 | 来自 skills.sh 的 design 向 skill「redesign-existing-projects」。安装量信号约 458,719；详情见上游 leonxlnx/taste-skill。 |
| 191 | [`ios-design`](skills/ios-design/SKILL.md) | `uizze.sh` | 417,203 | 来自 skills.sh 的 design 向 skill「ios-design」。安装量信号约 417,203；详情见上游 uizze.sh。 |

<a id="category-media"></a>
### `media` · 媒体与视频（25）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 3 | [`hyperframes-cli`](skills/hyperframes-cli/SKILL.md) | `heygen-com/hyperframes` | 1,357,195 | 通过 Hyperframes CLI 创建/渲染视频相关工作流。用户提到 Hyperframes 命令行时使用。 |
| 5 | [`hyperframes`](skills/hyperframes/SKILL.md) | `heygen-com/hyperframes` | 1,319,943 | Hyperframes 视频创作总技能。用户要做 AI 视频/成片流水线且提到 Hyperframes 时使用。 |
| 7 | [`media-use`](skills/media-use/SKILL.md) | `heygen-com/hyperframes` | 1,228,258 | 选择与运用媒体资源（图/音/视频）完成创作任务。用户纠结媒体素材用法时使用。 |
| 12 | [`hyperframes-registry`](skills/hyperframes-registry/SKILL.md) | `heygen-com/hyperframes` | 1,116,775 | 查找与复用 Hyperframes 注册表中的模板/组件。用户要选 Hyperframes 资源时使用。 |
| 19 | [`hyperframes-animation`](skills/hyperframes-animation/SKILL.md) | `heygen-com/hyperframes` | 1,005,059 | Hyperframes 动画时间线与动效相关工作。用户要调动画时使用。 |
| 20 | [`hyperframes-core`](skills/hyperframes-core/SKILL.md) | `heygen-com/hyperframes` | 930,744 | Hyperframes 核心概念与基础构图。用户入门或排查基础能力时使用。 |
| 21 | [`ai-video-generation`](skills/ai-video-generation/SKILL.md) | `101-skills/superpowers` | 919,308 | 用 AI 生成视频成片或片段。用户要文生视频/脚本转视频时使用。 |
| 22 | [`ai-image-generation`](skills/ai-image-generation/SKILL.md) | `101-skills/superpowers` | 917,955 | 用 AI 生成或迭代图像。用户要文生图、改图、出视觉稿时使用。 |
| 24 | [`ai-avatar-video`](skills/ai-avatar-video/SKILL.md) | `101-skills/superpowers` | 917,307 | 生成数字人/口播类 Avatar 视频。用户要数字人讲解视频时使用。 |
| 25 | [`hyperframes-creative`](skills/hyperframes-creative/SKILL.md) | `heygen-com/hyperframes` | 916,794 | Hyperframes 创意方向与叙事包装。用户要定视频创意时使用。 |
| 65 | [`hyperframes-keyframes`](skills/hyperframes-keyframes/SKILL.md) | `heygen-com/hyperframes` | 754,477 | Hyperframes 体系技能 `hyperframes-keyframes`。用户在 Hyperframes 视频工作流中需要该能力时使用。 |
| 71 | [`remotion-best-practices`](skills/remotion-best-practices/SKILL.md) | `remotion-dev/skills` | 722,049 | 音视频与媒体生成相关技能 `remotion-best-practices`。当任务匹配该上游 skill 名称与场景时使用。 |
| 73 | [`hyperframes-audio`](skills/hyperframes-audio/SKILL.md) | `heygen-com/hyperframes` | 663,547 | Hyperframes 体系技能 `hyperframes-audio`。用户在 Hyperframes 视频工作流中需要该能力时使用。 |
| 74 | [`general-video`](skills/general-video/SKILL.md) | `heygen-com/hyperframes` | 661,428 | 音视频与媒体生成相关技能 `general-video`。当任务匹配该上游 skill 名称与场景时使用。 |
| 98 | [`remotion-to-hyperframes`](skills/remotion-to-hyperframes/SKILL.md) | `heygen-com/hyperframes` | 548,464 | 音视频与媒体生成相关技能 `remotion-to-hyperframes`。当任务匹配该上游 skill 名称与场景时使用。 |
| 103 | [`product-launch-video`](skills/product-launch-video/SKILL.md) | `heygen-com/hyperframes` | 538,990 | 音视频与媒体生成相关技能 `product-launch-video`。当任务匹配该上游 skill 名称与场景时使用。 |
| 114 | [`faceless-explainer`](skills/faceless-explainer/SKILL.md) | `heygen-com/hyperframes` | 521,688 | 来自 skills.sh 的 media 向 skill「faceless-explainer」。安装量信号约 521,688；详情见上游 heygen-com/hyperframes。 |
| 116 | [`motion-graphics`](skills/motion-graphics/SKILL.md) | `heygen-com/hyperframes` | 514,007 | 来自 skills.sh 的 media 向 skill「motion-graphics」。安装量信号约 514,007；详情见上游 heygen-com/hyperframes。 |
| 154 | [`slideshow`](skills/slideshow/SKILL.md) | `heygen-com/hyperframes` | 455,786 | 来自 skills.sh 的 media 向 skill「slideshow」。安装量信号约 455,786；详情见上游 heygen-com/hyperframes。 |
| 155 | [`embedded-captions`](skills/embedded-captions/SKILL.md) | `heygen-com/hyperframes` | 453,600 | 来自 skills.sh 的 media 向 skill「embedded-captions」。安装量信号约 453,600；详情见上游 heygen-com/hyperframes。 |
| 156 | [`hyperframes-studio`](skills/hyperframes-studio/SKILL.md) | `heygen-com/hyperframes` | 451,321 | 来自 skills.sh 的 media 向 skill「hyperframes-studio」。安装量信号约 451,321；详情见上游 heygen-com/hyperframes。 |
| 161 | [`pr-to-video`](skills/pr-to-video/SKILL.md) | `heygen-com/hyperframes` | 448,935 | 来自 skills.sh 的 media 向 skill「pr-to-video」。安装量信号约 448,935；详情见上游 heygen-com/hyperframes。 |
| 165 | [`video-edit`](skills/video-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 442,344 | 来自 skills.sh 的 media 向 skill「video-edit」。安装量信号约 442,344；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 167 | [`image-to-video`](skills/image-to-video/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 440,560 | 来自 skills.sh 的 media 向 skill「image-to-video」。安装量信号约 440,560；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 188 | [`music-to-video`](skills/music-to-video/SKILL.md) | `heygen-com/hyperframes` | 418,974 | 来自 skills.sh 的 media 向 skill「music-to-video」。安装量信号约 418,974；详情见上游 heygen-com/hyperframes。 |

<a id="category-collaboration"></a>
### `collaboration` · 协作套件（飞书 / Lark）（27）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 32 | [`lark-doc`](skills/lark-doc/SKILL.md) | `open.feishu.cn` | 838,580 | 飞书/Lark OpenAPI 场景：doc。用户要在飞书生态完成相关自动化或集成时使用。 |
| 33 | [`lark-base`](skills/lark-base/SKILL.md) | `open.feishu.cn` | 837,904 | 飞书/Lark OpenAPI 场景：base。用户要在飞书生态完成相关自动化或集成时使用。 |
| 34 | [`lark-drive`](skills/lark-drive/SKILL.md) | `open.feishu.cn` | 837,894 | 飞书/Lark OpenAPI 场景：drive。用户要在飞书生态完成相关自动化或集成时使用。 |
| 35 | [`lark-shared`](skills/lark-shared/SKILL.md) | `open.feishu.cn` | 837,674 | 飞书/Lark OpenAPI 场景：shared。用户要在飞书生态完成相关自动化或集成时使用。 |
| 36 | [`lark-im`](skills/lark-im/SKILL.md) | `open.feishu.cn` | 836,933 | 飞书/Lark OpenAPI 场景：im。用户要在飞书生态完成相关自动化或集成时使用。 |
| 37 | [`lark-calendar`](skills/lark-calendar/SKILL.md) | `open.feishu.cn` | 836,540 | 飞书/Lark OpenAPI 场景：calendar。用户要在飞书生态完成相关自动化或集成时使用。 |
| 38 | [`lark-sheets`](skills/lark-sheets/SKILL.md) | `open.feishu.cn` | 836,441 | 飞书/Lark OpenAPI 场景：sheets。用户要在飞书生态完成相关自动化或集成时使用。 |
| 39 | [`lark-approval`](skills/lark-approval/SKILL.md) | `open.feishu.cn` | 836,415 | 飞书/Lark OpenAPI 场景：approval。用户要在飞书生态完成相关自动化或集成时使用。 |
| 40 | [`lark-wiki`](skills/lark-wiki/SKILL.md) | `open.feishu.cn` | 836,338 | 飞书/Lark OpenAPI 场景：wiki。用户要在飞书生态完成相关自动化或集成时使用。 |
| 41 | [`lark-contact`](skills/lark-contact/SKILL.md) | `open.feishu.cn` | 835,567 | 飞书/Lark OpenAPI 场景：contact。用户要在飞书生态完成相关自动化或集成时使用。 |
| 42 | [`lark-task`](skills/lark-task/SKILL.md) | `open.feishu.cn` | 835,460 | 飞书/Lark OpenAPI 场景：task。用户要在飞书生态完成相关自动化或集成时使用。 |
| 43 | [`lark-slides`](skills/lark-slides/SKILL.md) | `open.feishu.cn` | 835,323 | 飞书/Lark OpenAPI 场景：slides。用户要在飞书生态完成相关自动化或集成时使用。 |
| 44 | [`lark-mail`](skills/lark-mail/SKILL.md) | `open.feishu.cn` | 835,281 | 飞书/Lark OpenAPI 场景：mail。用户要在飞书生态完成相关自动化或集成时使用。 |
| 45 | [`lark-whiteboard`](skills/lark-whiteboard/SKILL.md) | `open.feishu.cn` | 835,125 | 飞书/Lark OpenAPI 场景：whiteboard。用户要在飞书生态完成相关自动化或集成时使用。 |
| 46 | [`lark-event`](skills/lark-event/SKILL.md) | `open.feishu.cn` | 835,035 | 飞书/Lark OpenAPI 场景：event。用户要在飞书生态完成相关自动化或集成时使用。 |
| 47 | [`lark-openapi-explorer`](skills/lark-openapi-explorer/SKILL.md) | `open.feishu.cn` | 834,796 | 飞书/Lark OpenAPI 场景：openapi explorer。用户要在飞书生态完成相关自动化或集成时使用。 |
| 48 | [`lark-attendance`](skills/lark-attendance/SKILL.md) | `open.feishu.cn` | 834,696 | 飞书/Lark OpenAPI 场景：attendance。用户要在飞书生态完成相关自动化或集成时使用。 |
| 49 | [`lark-skill-maker`](skills/lark-skill-maker/SKILL.md) | `open.feishu.cn` | 834,326 | 飞书/Lark OpenAPI 场景：skill maker。用户要在飞书生态完成相关自动化或集成时使用。 |
| 50 | [`lark-workflow-meeting-summary`](skills/lark-workflow-meeting-summary/SKILL.md) | `open.feishu.cn` | 834,184 | 飞书/Lark OpenAPI 场景：workflow meeting summary。用户要在飞书生态完成相关自动化或集成时使用。 |
| 51 | [`lark-minutes`](skills/lark-minutes/SKILL.md) | `open.feishu.cn` | 833,986 | 飞书/Lark OpenAPI 场景：minutes。用户要在飞书生态完成相关自动化或集成时使用。 |
| 52 | [`lark-workflow-standup-report`](skills/lark-workflow-standup-report/SKILL.md) | `open.feishu.cn` | 833,899 | 飞书/Lark OpenAPI 场景：workflow standup report。用户要在飞书生态完成相关自动化或集成时使用。 |
| 53 | [`lark-vc`](skills/lark-vc/SKILL.md) | `open.feishu.cn` | 833,251 | 飞书/Lark OpenAPI 场景：vc。用户要在飞书生态完成相关自动化或集成时使用。 |
| 55 | [`lark-okr`](skills/lark-okr/SKILL.md) | `open.feishu.cn` | 815,656 | 飞书/Lark OpenAPI 场景：okr。用户要在飞书生态完成相关自动化或集成时使用。 |
| 62 | [`lark-markdown`](skills/lark-markdown/SKILL.md) | `open.feishu.cn` | 801,529 | 飞书/Lark OpenAPI 场景：markdown。用户要在飞书生态完成相关自动化或集成时使用。 |
| 64 | [`lark-vc-agent`](skills/lark-vc-agent/SKILL.md) | `open.feishu.cn` | 777,869 | 飞书/Lark OpenAPI 场景：vc agent。用户要在飞书生态完成相关自动化或集成时使用。 |
| 69 | [`lark-apps`](skills/lark-apps/SKILL.md) | `open.feishu.cn` | 746,736 | 飞书/Lark OpenAPI 场景：apps。用户要在飞书生态完成相关自动化或集成时使用。 |
| 75 | [`lark-note`](skills/lark-note/SKILL.md) | `open.feishu.cn` | 618,126 | 飞书/Lark OpenAPI 场景：note。用户要在飞书生态完成相关自动化或集成时使用。 |

<a id="category-cloud"></a>
### `cloud` · 云平台（Azure / Foundry 等）（21）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 81 | [`microsoft-foundry`](skills/microsoft-foundry/SKILL.md) | `microsoft/azure-skills` | 585,309 | Microsoft Foundry / Azure AI 相关项目引导。用户提到 Foundry 时使用。 |
| 83 | [`azure-diagnostics`](skills/azure-diagnostics/SKILL.md) | `microsoft/azure-skills` | 576,049 | Azure 云场景：diagnostics。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 84 | [`azure-prepare`](skills/azure-prepare/SKILL.md) | `microsoft/azure-skills` | 575,222 | Azure 云场景：prepare。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 85 | [`azure-ai`](skills/azure-ai/SKILL.md) | `microsoft/azure-skills` | 574,510 | Azure 云场景：ai。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 86 | [`azure-deploy`](skills/azure-deploy/SKILL.md) | `microsoft/azure-skills` | 574,261 | Azure 云场景：deploy。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 87 | [`azure-validate`](skills/azure-validate/SKILL.md) | `microsoft/azure-skills` | 573,818 | Azure 云场景：validate。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 88 | [`azure-storage`](skills/azure-storage/SKILL.md) | `microsoft/azure-skills` | 573,090 | Azure 云场景：storage。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 89 | [`azure-compliance`](skills/azure-compliance/SKILL.md) | `microsoft/azure-skills` | 572,695 | Azure 云场景：compliance。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 90 | [`appinsights-instrumentation`](skills/appinsights-instrumentation/SKILL.md) | `microsoft/azure-skills` | 572,490 | 云平台与基础设施相关技能 `appinsights-instrumentation`。当任务匹配该上游 skill 名称与场景时使用。 |
| 91 | [`azure-resource-lookup`](skills/azure-resource-lookup/SKILL.md) | `microsoft/azure-skills` | 572,439 | Azure 云场景：resource lookup。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 92 | [`azure-resource-visualizer`](skills/azure-resource-visualizer/SKILL.md) | `microsoft/azure-skills` | 572,399 | Azure 云场景：resource visualizer。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 93 | [`entra-app-registration`](skills/entra-app-registration/SKILL.md) | `microsoft/azure-skills` | 572,356 | 云平台与基础设施相关技能 `entra-app-registration`。当任务匹配该上游 skill 名称与场景时使用。 |
| 94 | [`azure-kusto`](skills/azure-kusto/SKILL.md) | `microsoft/azure-skills` | 572,108 | Azure 云场景：kusto。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 95 | [`azure-aigateway`](skills/azure-aigateway/SKILL.md) | `microsoft/azure-skills` | 571,711 | Azure 云场景：aigateway。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 96 | [`azure-messaging`](skills/azure-messaging/SKILL.md) | `microsoft/azure-skills` | 563,365 | Azure 云场景：messaging。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 112 | [`azure-compute`](skills/azure-compute/SKILL.md) | `microsoft/azure-skills` | 528,193 | Azure 云场景：compute。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 115 | [`azure-cloud-migrate`](skills/azure-cloud-migrate/SKILL.md) | `microsoft/azure-skills` | 520,963 | 来自 skills.sh 的 cloud 向 skill「azure-cloud-migrate」。安装量信号约 520,963；详情见上游 microsoft/azure-skills。 |
| 135 | [`azure-quotas`](skills/azure-quotas/SKILL.md) | `microsoft/azure-skills` | 476,733 | 来自 skills.sh 的 cloud 向 skill「azure-quotas」。安装量信号约 476,733；详情见上游 microsoft/azure-skills。 |
| 146 | [`azure-upgrade`](skills/azure-upgrade/SKILL.md) | `microsoft/azure-skills` | 469,874 | 来自 skills.sh 的 cloud 向 skill「azure-upgrade」。安装量信号约 469,874；详情见上游 microsoft/azure-skills。 |
| 162 | [`azure-enterprise-infra-planner`](skills/azure-enterprise-infra-planner/SKILL.md) | `microsoft/azure-skills` | 446,495 | 来自 skills.sh 的 cloud 向 skill「azure-enterprise-infra-planner」。安装量信号约 446,495；详情见上游 microsoft/azure-skills。 |
| 166 | [`azure-kubernetes`](skills/azure-kubernetes/SKILL.md) | `microsoft/azure-skills` | 440,788 | 来自 skills.sh 的 cloud 向 skill「azure-kubernetes」。安装量信号约 440,788；详情见上游 microsoft/azure-skills。 |

<a id="category-documents"></a>
### `documents` · 文档与办公格式（6）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| — | [`docx-documents`](skills/docx-documents/SKILL.md) | — | — | 创建或编辑 Word 文档（.docx）：正文样式、标题层级、目录、表格、页眉页脚、批注与修订。用户提到 Word、docx、写公文/方案文档时使用。 |
| — | [`flowchart-mermaid`](skills/flowchart-mermaid/SKILL.md) | — | — | 用 Mermaid 画清晰、可渲染的流程图与相关示意图。用户提到画流程图、流程、决策树、工作流、架构示意、时序图、状态机、ER/类图，或要把过程可视化成 diagram-as-code 时使用。 |
| — | [`pdf-documents`](skills/pdf-documents/SKILL.md) | — | — | 创建、阅读、拆合或填写 PDF。用户提到 PDF、导出说明书、合并拆分页面、提取表格/文字、加水印、填表时使用。 |
| — | [`poster-design`](skills/poster-design/SKILL.md) | — | — | 设计海报、静态视觉稿、活动宣传图或单页艺术构图。用户提到做海报、宣传图、视觉设计、静态画面、PNG/PDF 海报时使用；输出以画面为主，文案极少。 |
| — | [`pptx-deck`](skills/pptx-deck/SKILL.md) | — | — | 制作或改写 PowerPoint / .pptx 幻灯片（路演、汇报、培训、方案）。用户提到做 PPT、幻灯片、presentation、deck、pitch，或要生成/修改 .pptx 时使用。 |
| — | [`spreadsheet-xlsx`](skills/spreadsheet-xlsx/SKILL.md) | — | — | 创建、编辑、分析或美化电子表格（.xlsx / .csv / .tsv）。用户提到做表、改 Excel、透视、公式、清洗脏表、从数据出报表或图表时使用。 |

<a id="category-finance"></a>
### `finance` · 金融（12）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| — | [`company-tearsheet`](skills/company-tearsheet/SKILL.md) | — | — | 做公司一页纸：业务、财务快照、竞争要点、近期催化与开放问题。用户要快速熟悉标的时使用。 |
| — | [`crypto-market-watch`](skills/crypto-market-watch/SKILL.md) | — | — | 加密市场观察笔记：价格区间、主导叙事、链上/衍生品公开指标与风险事件。用户要加密周报骨架时使用。 |
| — | [`earnings-digest`](skills/earnings-digest/SKILL.md) | — | — | 提炼财报/业绩发布要点：收入利润、指引、分部与管理层口径。用户要看季报、听会纪要摘要时使用。 |
| — | [`fund-flow-notes`](skills/fund-flow-notes/SKILL.md) | — | — | 整理资金流向笔记：北向/ETF/期货持仓等公开流向的记录模板。用户要跟踪资金面变化时使用。 |
| — | [`investment-memo`](skills/investment-memo/SKILL.md) | — | — | 起草投资备忘录骨架：论点、证据、反方、催化剂与监控指标。用户要写内部 memo 时使用。 |
| — | [`macro-calendar`](skills/macro-calendar/SKILL.md) | — | — | 解读宏观数据与央行日历：为何重要、市场常关注什么、如何记录预期差。用户看非农、CPI、利率决议时使用。 |
| — | [`market-brief`](skills/market-brief/SKILL.md) | — | — | 整理当日/当周行情简报：指数、板块、重要个股与事件一览。用户要晨报、收盘总结、市场速览时使用。 |
| — | [`portfolio-review`](skills/portfolio-review/SKILL.md) | — | — | 按用户提供的持仓做结构化回顾：权重、盈亏、集中度与待办。用户要复盘组合、月度检视时使用。 |
| — | [`quant-research-notes`](skills/quant-research-notes/SKILL.md) | — | — | 整理量化研究笔记：假设、数据、特征、回测设置与失效条件。用户要沉淀实验或读论文时使用。 |
| — | [`risk-checklist`](skills/risk-checklist/SKILL.md) | — | — | 交易/投资决策前的风险检查清单：流动性、杠杆、事件、操作与合规。用户要下单前自检或复盘失误时使用。 |
| — | [`sec-filing-skim`](skills/sec-filing-skim/SKILL.md) | — | — | 速读监管公告与长篇披露（如 10-K/10-Q/年报）：风险因素、MD&A、重大合同。用户要啃文件时使用。 |
| — | [`valuation-sanity`](skills/valuation-sanity/SKILL.md) | — | — | 对估值假设做 sanity check：倍数、增长与情景是否自洽。用户要检查模型或街头倍数时使用。 |

<a id="category-engineering"></a>
### `engineering` · 工程实现（30）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 76 | [`caveman`](skills/caveman/SKILL.md) | `juliusbrussee/caveman` | 603,221 | Caveman：极简/直给的工程沟通与实现风格。用户要该技能工作流时使用。 |
| 104 | [`google-agents-cli-adk-code`](skills/google-agents-cli-adk-code/SKILL.md) | `google/agents-cli` | 532,028 | 用 Google Agents CLI / ADK 编写 Agent 代码。用户做 ADK 开发时使用。 |
| 105 | [`google-agents-cli-deploy`](skills/google-agents-cli-deploy/SKILL.md) | `google/agents-cli` | 531,355 | 部署 Google Agents CLI 相关 Agent。用户要发布到运行环境时使用。 |
| 106 | [`google-agents-cli-publish`](skills/google-agents-cli-publish/SKILL.md) | `google/agents-cli` | 531,146 | 发布 Agent 包或制品。用户要 publish 时使用。 |
| 107 | [`google-agents-cli-workflow`](skills/google-agents-cli-workflow/SKILL.md) | `google/agents-cli` | 530,523 | 编排 Agents CLI 工作流。用户要多步 Agent 流水线时使用。 |
| 108 | [`google-agents-cli-eval`](skills/google-agents-cli-eval/SKILL.md) | `google/agents-cli` | 530,507 | 评估 Agent 质量。用户要 eval/打分时使用。 |
| 109 | [`google-agents-cli-scaffold`](skills/google-agents-cli-scaffold/SKILL.md) | `google/agents-cli` | 530,391 | 脚手架生成 Agent 项目。用户要快速起项目时使用。 |
| 110 | [`google-agents-cli-observability`](skills/google-agents-cli-observability/SKILL.md) | `google/agents-cli` | 530,360 | 为 Agent 加观测（日志/追踪/指标）。用户要可观测性时使用。 |
| 124 | [`paper-context-resolver`](skills/paper-context-resolver/SKILL.md) | `lllllllama/rigorpilot-skills` | 483,766 | 来自 skills.sh 的 engineering 向 skill「paper-context-resolver」。安装量信号约 483,766；详情见上游 lllllllama/rigorpilot-skills。 |
| 126 | [`repo-intake-and-plan`](skills/repo-intake-and-plan/SKILL.md) | `lllllllama/rigorpilot-skills` | 482,959 | 来自 skills.sh 的 engineering 向 skill「repo-intake-and-plan」。安装量信号约 482,959；详情见上游 lllllllama/rigorpilot-skills。 |
| 127 | [`minimal-run-and-audit`](skills/minimal-run-and-audit/SKILL.md) | `lllllllama/rigorpilot-skills` | 482,882 | 来自 skills.sh 的 engineering 向 skill「minimal-run-and-audit」。安装量信号约 482,882；详情见上游 lllllllama/rigorpilot-skills。 |
| 128 | [`env-and-assets-bootstrap`](skills/env-and-assets-bootstrap/SKILL.md) | `lllllllama/rigorpilot-skills` | 482,769 | 来自 skills.sh 的 engineering 向 skill「env-and-assets-bootstrap」。安装量信号约 482,769；详情见上游 lllllllama/rigorpilot-skills。 |
| 150 | [`supabase-postgres-best-practices`](skills/supabase-postgres-best-practices/SKILL.md) | `supabase/agent-skills` | 468,744 | 来自 skills.sh 的 engineering 向 skill「supabase-postgres-best-practices」。安装量信号约 468,744；详情见上游 supabase/agent-skills。 |
| 168 | [`nano-banana-2`](skills/nano-banana-2/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 440,246 | 来自 skills.sh 的 engineering 向 skill「nano-banana-2」。安装量信号约 440,246；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 169 | [`image-edit`](skills/image-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 439,802 | 来自 skills.sh 的 engineering 向 skill「image-edit」。安装量信号约 439,802；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 170 | [`nano-banana-edit`](skills/nano-banana-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 439,642 | 来自 skills.sh 的 engineering 向 skill「nano-banana-edit」。安装量信号约 439,642；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 171 | [`flux-kontext`](skills/flux-kontext/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 439,432 | 来自 skills.sh 的 engineering 向 skill「flux-kontext」。安装量信号约 439,432；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 172 | [`wan-2-7`](skills/wan-2-7/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,872 | 来自 skills.sh 的 engineering 向 skill「wan-2-7」。安装量信号约 438,872；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 173 | [`seedance-v2`](skills/seedance-v2/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,719 | 来自 skills.sh 的 engineering 向 skill「seedance-v2」。安装量信号约 438,719；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 174 | [`gpt-image-edit`](skills/gpt-image-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,712 | 来自 skills.sh 的 engineering 向 skill「gpt-image-edit」。安装量信号约 438,712；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 175 | [`happyhorse-1-0`](skills/happyhorse-1-0/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,632 | 来自 skills.sh 的 engineering 向 skill「happyhorse-1-0」。安装量信号约 438,632；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 176 | [`flux-2-klein`](skills/flux-2-klein/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 438,466 | 来自 skills.sh 的 engineering 向 skill「flux-2-klein」。安装量信号约 438,466；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 181 | [`vercel-composition-patterns`](skills/vercel-composition-patterns/SKILL.md) | `vercel-labs/agent-skills` | 430,333 | 来自 skills.sh 的 engineering 向 skill「vercel-composition-patterns」。安装量信号约 430,333；详情见上游 vercel-labs/agent-skills。 |
| 182 | [`ui-ux-pro-max`](skills/ui-ux-pro-max/SKILL.md) | `nextlevelbuilder/ui-ux-pro-max-skill` | 427,165 | 来自 skills.sh 的 engineering 向 skill「ui-ux-pro-max」。安装量信号约 427,165；详情见上游 nextlevelbuilder/ui-ux-pro-max-skill。 |
| 184 | [`minimalist-ui`](skills/minimalist-ui/SKILL.md) | `leonxlnx/taste-skill` | 425,120 | 来自 skills.sh 的 engineering 向 skill「minimalist-ui」。安装量信号约 425,120；详情见上游 leonxlnx/taste-skill。 |
| 185 | [`caveman-commit`](skills/caveman-commit/SKILL.md) | `juliusbrussee/caveman` | 422,405 | 来自 skills.sh 的 engineering 向 skill「caveman-commit」。安装量信号约 422,405；详情见上游 juliusbrussee/caveman。 |
| 189 | [`caveman-compress`](skills/caveman-compress/SKILL.md) | `juliusbrussee/caveman` | 418,533 | 来自 skills.sh 的 engineering 向 skill「caveman-compress」。安装量信号约 418,533；详情见上游 juliusbrussee/caveman。 |
| 190 | [`caveman-review`](skills/caveman-review/SKILL.md) | `juliusbrussee/caveman` | 418,371 | 来自 skills.sh 的 engineering 向 skill「caveman-review」。安装量信号约 418,371；详情见上游 juliusbrussee/caveman。 |
| 192 | [`kling-3-0`](skills/kling-3-0/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 415,690 | 来自 skills.sh 的 engineering 向 skill「kling-3-0」。安装量信号约 415,690；详情见上游 prime-skills/runcomfy-agent-skills。 |
| — | [`webapp-testing`](skills/webapp-testing/SKILL.md) | — | — | 为 Web 应用设计并运行可靠的 UI/端到端测试与冒烟检查。用户要测页面、写 Playwright/Cypress 测试、加回归、验证修复是否生效时使用。 |
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
  build-catalog.py           # catalog.json + README 分类表 + llms.txt
  check-catalog.py           # CI：目录 / catalog / README 一致性
  refresh-from-skills-sh.py  # 榜单发现 / 热度刷新
.github/workflows/catalog.yml
catalog.json
llms.txt
CONTRIBUTING.md
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

分类取值：`discovery` / `planning` / `browser` / `design` / `media` / `collaboration` / `cloud` / `documents` / `finance` / `engineering` / `meta`。

## 贡献

完整约定见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。简要步骤：

1. 在 `skills/` 下新增目录与 `SKILL.md`（务必带 `category`）
2. 运行 `python3 scripts/build-catalog.py` 与 `python3 scripts/check-catalog.py`
3. 开 PR 说明用途；若来自榜单请附 `source`（`rank` / `installs` 可留给刷新脚本）

也可用刷新脚本批量补洞，再开 PR 审 stub 质量。新手任务见 Issues 标签 `good first issue`。

## License

[MIT](LICENSE)
