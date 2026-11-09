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

相关演示：[visual-agents-workflow](https://github.com/kanjiandahai/visual-agents-workflow)（可点击多 Agent 工作流沙盘 / [Live demo](https://kanjiandahai.github.io/visual-agents-workflow/)）。

## 增长模型

1. **Bootstrap**：用 skills.sh All-Time 去重热度灌入一批种子（本仓曾在 2026-11-01 做过 Top100-unique 灌入）。
2. **持续收录**：定期跑刷新脚本，把榜单上尚未入库的高信号名称做成 stub 卡片；也欢迎手工 PR 补充文档向 / 私域向 skill。
3. **元数据刷新**：对已有 skill，用新快照更新 `rank` / `installs`（以及缺失的 `source`），**不覆盖**更丰富的 description 与正文。
4. **单调增长**：已入库 skill 默认保留；刷新脚本**不会**为了「对齐 Top N」而删卡。

当前收录 <!-- BEGIN_SKILL_COUNT -->172<!-- END_SKILL_COUNT --> 个 skill（计数由 `scripts/build-catalog.py` 维护）。

<!-- BEGIN_CATALOG_BROWSE -->
## 分类一览

| 分类 | 数量 | 说明 |
|------|------|------|
| [`discovery`](#category-discovery) | **4** | 发现与安装 |
| [`planning`](#category-planning) | **32** | 规划 / 澄清 / 工程决策 |
| [`browser`](#category-browser) | **3** | 浏览器与社交自动化 |
| [`design`](#category-design) | **10** | 设计与前端体验 |
| [`media`](#category-media) | **25** | 媒体与视频 |
| [`collaboration`](#category-collaboration) | **27** | 协作套件（飞书 / Lark） |
| [`cloud`](#category-cloud) | **22** | 云平台（Azure / Foundry 等） |
| [`documents`](#category-documents) | **6** | 文档与办公格式 |
| [`finance`](#category-finance) | **12** | 金融 |
| [`engineering`](#category-engineering) | **31** | 工程实现 |

合计：**172** 个 skill。完整机器索引见 [`catalog.json`](catalog.json)。

## 按分类浏览

<a id="category-discovery"></a>
### `discovery` · 发现与安装（4）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 1 | [`find-skills`](skills/find-skills/SKILL.md) | `vercel-labs/skills` | 4,267,611 | 发现、筛选并安装合适的 Agent Skill。用户说找不到 skill、有没有某某能力、帮我搜 skill、skills.sh / npx skills、或不知道该装哪个 skill 时使用。 |
| 13 | [`setup-matt-pocock-skills`](skills/setup-matt-pocock-skills/SKILL.md) | `mattpocock/skills` | 1,124,745 | 安装/配置 Matt Pocock 技能包。用户要启用该套 skills 时使用。 |
| 118 | [`setup-pre-commit`](skills/setup-pre-commit/SKILL.md) | `mattpocock/skills` | 534,672 | 来自 skills.sh 的 discovery 向 skill「setup-pre-commit」。安装量信号约 511,903；详情见上游 mattpocock/skills。 |
| 194 | [`skill-creator`](skills/skill-creator/SKILL.md) | `anthropics/skills` | 427,265 | 从零编写、改写并打磨 Agent Skill（SKILL.md）。用户要创建 skill、优化 description 触发、给 skill 加评测、或把一段工作流沉淀成 skill 时使用。 |

<a id="category-planning"></a>
### `planning` · 规划 / 澄清 / 工程决策（32）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 2 | [`grill-me`](skills/grill-me/SKILL.md) | `mattpocock/skills` | 1,517,927 | 对计划或设计做高压追问，直到决策树走通、双方理解一致。用户说 grill me、拷问一下方案、帮我抠需求、压力测试设计、把计划问清楚时使用。 |
| 9 | [`grill-with-docs`](skills/grill-with-docs/SKILL.md) | `mattpocock/skills` | 1,300,218 | 结合文档资料做高压方案追问。用户要边读文档边拷问设计时使用。 |
| 10 | [`improve-codebase-architecture`](skills/improve-codebase-architecture/SKILL.md) | `mattpocock/skills` | 1,242,646 | 诊断并改进代码库架构：边界、模块化、依赖方向与可测性。用户说架构混乱、拆模块、减耦合、理清分层、改进 codebase architecture 时使用。 |
| 12 | [`tdd`](skills/tdd/SKILL.md) | `mattpocock/skills` | 1,215,700 | 用测试驱动实现功能：先写失败测试，再写最小实现，再重构。用户要求 TDD、先写测试、红绿重构、或实现前先定行为规格时使用。 |
| 14 | [`handoff`](skills/handoff/SKILL.md) | `mattpocock/skills` | 1,113,371 | 把上下文整理成可交接的 handoff 文档。用户换人/换会话继续做时使用。 |
| 16 | [`grilling`](skills/grilling/SKILL.md) | `mattpocock/skills` | 1,074,638 | 持续追问以澄清模糊需求（grilling 流程）。用户要被系统化拷问时使用。 |
| 18 | [`prototype`](skills/prototype/SKILL.md) | `mattpocock/skills` | 1,055,928 | 快速做出可验证原型。用户要先跑通 demo 再谈完美实现时使用。 |
| 19 | [`triage`](skills/triage/SKILL.md) | `mattpocock/skills` | 1,054,145 | 对问题/任务做分流定级。用户一堆 issue/bug 不知先做哪个时使用。 |
| 25 | [`domain-modeling`](skills/domain-modeling/SKILL.md) | `mattpocock/skills` | 953,493 | 梳理领域模型与边界上下文。用户要 DDD/领域语言/模型图时使用。 |
| 27 | [`codebase-design`](skills/codebase-design/SKILL.md) | `mattpocock/skills` | 929,365 | 从零或重构时设计代码库结构。用户要定目录/模块边界时使用。 |
| 28 | [`teach`](skills/teach/SKILL.md) | `mattpocock/skills` | 929,060 | 把复杂主题教给用户或写成教程。用户说「教我」「讲清楚」时使用。 |
| 30 | [`diagnosing-bugs`](skills/diagnosing-bugs/SKILL.md) | `mattpocock/skills` | 908,441 | 系统化定位缺陷根因。用户卡在诡异 bug 时使用。 |
| 58 | [`code-review`](skills/code-review/SKILL.md) | `mattpocock/skills` | 867,964 | 结构化代码审查。用户要 review PR/改动时使用。 |
| 60 | [`implement`](skills/implement/SKILL.md) | `mattpocock/skills` | 842,831 | 把已澄清的规格落地为实现。用户说「按方案实现」时使用。 |
| 63 | [`ask-matt`](skills/ask-matt/SKILL.md) | `mattpocock/skills` | 830,049 | 以 Matt 风格答疑或给工程建议。用户要该系列方法论建议时使用。 |
| 65 | [`wayfinder`](skills/wayfinder/SKILL.md) | `mattpocock/skills` | 788,171 | 在未知代码库里找路：定位模块与改动点。用户「从哪改」时使用。 |
| 66 | [`to-spec`](skills/to-spec/SKILL.md) | `mattpocock/skills` | 784,632 | 把讨论收敛成规格说明。用户要写 spec 时使用。 |
| 68 | [`research`](skills/research/SKILL.md) | `mattpocock/skills` | 782,015 | 针对技术/产品问题做有出处的调研。用户要调研对比时使用。 |
| 69 | [`to-tickets`](skills/to-tickets/SKILL.md) | `mattpocock/skills` | 781,025 | 把规格拆成可执行工单。用户要拆任务/issue 时使用。 |
| 100 | [`wizard`](skills/wizard/SKILL.md) | `mattpocock/skills` | 614,487 | 用向导式步骤带用户做完复杂配置。用户要一步步引导时使用。 |
| 104 | [`to-questionnaire`](skills/to-questionnaire/SKILL.md) | `mattpocock/skills` | 559,050 | 把模糊需求变成问卷/检查表。用户要收集决策信息时使用。 |
| 113 | [`resolving-merge-conflicts`](skills/resolving-merge-conflicts/SKILL.md) | `mattpocock/skills` | 551,197 | 解决 Git 合并冲突。用户遇到 conflict 时使用。 |
| 115 | [`git-guardrails-claude-code`](skills/git-guardrails-claude-code/SKILL.md) | `mattpocock/skills` | 545,398 | 来自 skills.sh 的 planning 向 skill「git-guardrails-claude-code」。安装量信号约 522,531；详情见上游 mattpocock/skills。 |
| 117 | [`writing-for-agents`](skills/writing-for-agents/SKILL.md) | `mattpocock/skills` | 534,765 | 来自 skills.sh 的 planning 向 skill「writing-for-agents」。安装量信号约 500,813；详情见上游 mattpocock/skills。 |
| 119 | [`writing-beats`](skills/writing-beats/SKILL.md) | `mattpocock/skills` | 527,978 | 来自 skills.sh 的 planning 向 skill「writing-beats」。安装量信号约 505,261；详情见上游 mattpocock/skills。 |
| 120 | [`writing-shape`](skills/writing-shape/SKILL.md) | `mattpocock/skills` | 527,600 | 来自 skills.sh 的 planning 向 skill「writing-shape」。安装量信号约 504,850；详情见上游 mattpocock/skills。 |
| 121 | [`writing-fragments`](skills/writing-fragments/SKILL.md) | `mattpocock/skills` | 526,833 | 来自 skills.sh 的 planning 向 skill「writing-fragments」。安装量信号约 504,164；详情见上游 mattpocock/skills。 |
| 126 | [`scaffold-exercises`](skills/scaffold-exercises/SKILL.md) | `mattpocock/skills` | 524,928 | 来自 skills.sh 的 planning 向 skill「scaffold-exercises」。安装量信号约 502,451；详情见上游 mattpocock/skills。 |
| 129 | [`migrate-to-shoehorn`](skills/migrate-to-shoehorn/SKILL.md) | `mattpocock/skills` | 520,856 | 来自 skills.sh 的 planning 向 skill「migrate-to-shoehorn」。安装量信号约 498,439；详情见上游 mattpocock/skills。 |
| 136 | [`wait-what`](skills/wait-what/SKILL.md) | `mattpocock/skills` | 510,059 | 来自 skills.sh 的 planning 向 skill「wait-what」。安装量信号约 479,572；详情见上游 mattpocock/skills。 |
| 145 | [`loop-me`](skills/loop-me/SKILL.md) | `mattpocock/skills` | 485,522 | 来自 skills.sh 的 planning 向 skill「loop-me」。安装量信号约 462,645；详情见上游 mattpocock/skills。 |
| 168 | [`claude-handoff`](skills/claude-handoff/SKILL.md) | `mattpocock/skills` | 467,322 | 来自 skills.sh 的 planning 向 skill「claude-handoff」。安装量信号约 444,437；详情见上游 mattpocock/skills。 |

<a id="category-browser"></a>
### `browser` · 浏览器与社交自动化（3）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 5 | [`agent-browser`](skills/agent-browser/SKILL.md) | `vercel-labs/agent-browser` | 1,435,926 | 指导助手用浏览器完成页面操作、抓取与验证（打开、点击、填写、截图、断言）。用户要自动化网页流程、检查线上 UI、登录后操作站点、或用无头/有头浏览器跑任务时使用。 |
| 8 | [`reddit-automation`](skills/reddit-automation/SKILL.md) | `flowkit-labs/skills` | 1,300,419 | 自动化 Reddit 浏览、发帖或互动流程（需遵守平台规则）。用户要 Reddit 代理操作时使用。 |
| 23 | [`twitter-automation`](skills/twitter-automation/SKILL.md) | `101-skills/superpowers` | 994,971 | 自动化 X/Twitter 浏览与操作（遵守平台规则）。用户要推特代理流程时使用。 |

<a id="category-design"></a>
### `design` · 设计与前端体验（10）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 7 | [`design-mobile-apps`](skills/design-mobile-apps/SKILL.md) | `designed-by-ai/skills` | 1,308,072 | 移动端 App UI/交互设计指导。用户做 iOS/Android/跨端界面时使用。 |
| 15 | [`frontend-design`](skills/frontend-design/SKILL.md) | `anthropics/skills` | 1,093,510 | 做有辨识度的前端视觉与界面，避免千篇一律的 AI 默认审美。新建页面、改版 UI、落地页、仪表盘皮肤，或用户抱怨「看起来像模板」时使用。 |
| 17 | [`ui-taste`](skills/ui-taste/SKILL.md) | `uizze.sh` | 1,063,609 | 提升 UI 品味与细节一致性。用户觉得界面「土/乱/廉价」时使用。 |
| 35 | [`vercel-react-best-practices`](skills/vercel-react-best-practices/SKILL.md) | `vercel-labs/agent-skills` | 881,836 | 按 Vercel 倡导的 React/Next 最佳实践检查与改写。用户做 React/Next 优化时使用。 |
| 61 | [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | `vercel-labs/agent-skills` | 839,663 | 对照现代 Web 设计准则检查页面。用户要可用性/无障碍/视觉规范时使用。 |
| 76 | [`design-taste-frontend`](skills/design-taste-frontend/SKILL.md) | `leonxlnx/taste-skill` | 750,235 | 设计与前端体验相关技能 `design-taste-frontend`。当任务匹配该上游 skill 名称与场景时使用。 |
| 169 | [`high-end-visual-design`](skills/high-end-visual-design/SKILL.md) | `leonxlnx/taste-skill` | 458,878 | 来自 skills.sh 的 design 向 skill「high-end-visual-design」。安装量信号约 458,850；详情见上游 leonxlnx/taste-skill。 |
| 170 | [`redesign-existing-projects`](skills/redesign-existing-projects/SKILL.md) | `leonxlnx/taste-skill` | 458,756 | 来自 skills.sh 的 design 向 skill「redesign-existing-projects」。安装量信号约 458,719；详情见上游 leonxlnx/taste-skill。 |
| 191 | [`emil-design-eng`](skills/emil-design-eng/SKILL.md) | `emilkowalski/skills` | 429,310 | 来自 skills.sh 的 design 向 skill「emil-design-eng」。安装量信号约 429,310；详情见上游 emilkowalski/skills。 |
| 191 | [`ios-design`](skills/ios-design/SKILL.md) | `uizze.sh` | 417,203 | 来自 skills.sh 的 design 向 skill「ios-design」。安装量信号约 417,203；详情见上游 uizze.sh。 |

<a id="category-media"></a>
### `media` · 媒体与视频（25）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 3 | [`hyperframes-cli`](skills/hyperframes-cli/SKILL.md) | `heygen-com/hyperframes` | 1,474,944 | 通过 Hyperframes CLI 创建/渲染视频相关工作流。用户提到 Hyperframes 命令行时使用。 |
| 4 | [`hyperframes`](skills/hyperframes/SKILL.md) | `heygen-com/hyperframes` | 1,436,657 | Hyperframes 视频创作总技能。用户要做 AI 视频/成片流水线且提到 Hyperframes 时使用。 |
| 6 | [`media-use`](skills/media-use/SKILL.md) | `heygen-com/hyperframes` | 1,347,181 | 选择与运用媒体资源（图/音/视频）完成创作任务。用户纠结媒体素材用法时使用。 |
| 11 | [`hyperframes-registry`](skills/hyperframes-registry/SKILL.md) | `heygen-com/hyperframes` | 1,228,300 | 查找与复用 Hyperframes 注册表中的模板/组件。用户要选 Hyperframes 资源时使用。 |
| 20 | [`hyperframes-animation`](skills/hyperframes-animation/SKILL.md) | `heygen-com/hyperframes` | 1,005,325 | Hyperframes 动画时间线与动效相关工作。用户要调动画时使用。 |
| 21 | [`ai-video-generation`](skills/ai-video-generation/SKILL.md) | `101-skills/superpowers` | 997,110 | 用 AI 生成视频成片或片段。用户要文生视频/脚本转视频时使用。 |
| 22 | [`ai-image-generation`](skills/ai-image-generation/SKILL.md) | `101-skills/superpowers` | 995,417 | 用 AI 生成或迭代图像。用户要文生图、改图、出视觉稿时使用。 |
| 24 | [`ai-avatar-video`](skills/ai-avatar-video/SKILL.md) | `101-skills/superpowers` | 994,722 | 生成数字人/口播类 Avatar 视频。用户要数字人讲解视频时使用。 |
| 26 | [`hyperframes-core`](skills/hyperframes-core/SKILL.md) | `heygen-com/hyperframes` | 931,005 | Hyperframes 核心概念与基础构图。用户入门或排查基础能力时使用。 |
| 29 | [`hyperframes-creative`](skills/hyperframes-creative/SKILL.md) | `heygen-com/hyperframes` | 917,055 | Hyperframes 创意方向与叙事包装。用户要定视频创意时使用。 |
| 70 | [`remotion-best-practices`](skills/remotion-best-practices/SKILL.md) | `remotion-dev/skills` | 775,546 | 音视频与媒体生成相关技能 `remotion-best-practices`。当任务匹配该上游 skill 名称与场景时使用。 |
| 75 | [`hyperframes-keyframes`](skills/hyperframes-keyframes/SKILL.md) | `heygen-com/hyperframes` | 754,736 | Hyperframes 体系技能 `hyperframes-keyframes`。用户在 Hyperframes 视频工作流中需要该能力时使用。 |
| 81 | [`hyperframes-audio`](skills/hyperframes-audio/SKILL.md) | `heygen-com/hyperframes` | 663,806 | Hyperframes 体系技能 `hyperframes-audio`。用户在 Hyperframes 视频工作流中需要该能力时使用。 |
| 82 | [`general-video`](skills/general-video/SKILL.md) | `heygen-com/hyperframes` | 661,691 | 音视频与媒体生成相关技能 `general-video`。当任务匹配该上游 skill 名称与场景时使用。 |
| 103 | [`remotion-to-hyperframes`](skills/remotion-to-hyperframes/SKILL.md) | `heygen-com/hyperframes` | 585,527 | 音视频与媒体生成相关技能 `remotion-to-hyperframes`。当任务匹配该上游 skill 名称与场景时使用。 |
| 116 | [`product-launch-video`](skills/product-launch-video/SKILL.md) | `heygen-com/hyperframes` | 539,257 | 音视频与媒体生成相关技能 `product-launch-video`。当任务匹配该上游 skill 名称与场景时使用。 |
| 128 | [`faceless-explainer`](skills/faceless-explainer/SKILL.md) | `heygen-com/hyperframes` | 521,959 | 来自 skills.sh 的 media 向 skill「faceless-explainer」。安装量信号约 521,688；详情见上游 heygen-com/hyperframes。 |
| 131 | [`motion-graphics`](skills/motion-graphics/SKILL.md) | `heygen-com/hyperframes` | 514,270 | 来自 skills.sh 的 media 向 skill「motion-graphics」。安装量信号约 514,007；详情见上游 heygen-com/hyperframes。 |
| 141 | [`slideshow`](skills/slideshow/SKILL.md) | `heygen-com/hyperframes` | 491,284 | 来自 skills.sh 的 media 向 skill「slideshow」。安装量信号约 455,786；详情见上游 heygen-com/hyperframes。 |
| 154 | [`video-edit`](skills/video-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 478,622 | 来自 skills.sh 的 media 向 skill「video-edit」。安装量信号约 442,344；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 160 | [`image-to-video`](skills/image-to-video/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 477,717 | 来自 skills.sh 的 media 向 skill「image-to-video」。安装量信号约 440,560；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 171 | [`embedded-captions`](skills/embedded-captions/SKILL.md) | `heygen-com/hyperframes` | 453,862 | 来自 skills.sh 的 media 向 skill「embedded-captions」。安装量信号约 453,600；详情见上游 heygen-com/hyperframes。 |
| 172 | [`hyperframes-studio`](skills/hyperframes-studio/SKILL.md) | `heygen-com/hyperframes` | 451,579 | 来自 skills.sh 的 media 向 skill「hyperframes-studio」。安装量信号约 451,321；详情见上游 heygen-com/hyperframes。 |
| 174 | [`pr-to-video`](skills/pr-to-video/SKILL.md) | `heygen-com/hyperframes` | 449,193 | 来自 skills.sh 的 media 向 skill「pr-to-video」。安装量信号约 448,935；详情见上游 heygen-com/hyperframes。 |
| 188 | [`music-to-video`](skills/music-to-video/SKILL.md) | `heygen-com/hyperframes` | 418,974 | 来自 skills.sh 的 media 向 skill「music-to-video」。安装量信号约 418,974；详情见上游 heygen-com/hyperframes。 |

<a id="category-collaboration"></a>
### `collaboration` · 协作套件（飞书 / Lark）（27）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 36 | [`lark-doc`](skills/lark-doc/SKILL.md) | `open.feishu.cn` | 874,789 | 飞书/Lark OpenAPI 场景：doc。用户要在飞书生态完成相关自动化或集成时使用。 |
| 37 | [`lark-drive`](skills/lark-drive/SKILL.md) | `open.feishu.cn` | 874,041 | 飞书/Lark OpenAPI 场景：drive。用户要在飞书生态完成相关自动化或集成时使用。 |
| 38 | [`lark-base`](skills/lark-base/SKILL.md) | `open.feishu.cn` | 874,007 | 飞书/Lark OpenAPI 场景：base。用户要在飞书生态完成相关自动化或集成时使用。 |
| 39 | [`lark-shared`](skills/lark-shared/SKILL.md) | `open.feishu.cn` | 873,899 | 飞书/Lark OpenAPI 场景：shared。用户要在飞书生态完成相关自动化或集成时使用。 |
| 40 | [`lark-im`](skills/lark-im/SKILL.md) | `open.feishu.cn` | 873,006 | 飞书/Lark OpenAPI 场景：im。用户要在飞书生态完成相关自动化或集成时使用。 |
| 41 | [`lark-calendar`](skills/lark-calendar/SKILL.md) | `open.feishu.cn` | 872,595 | 飞书/Lark OpenAPI 场景：calendar。用户要在飞书生态完成相关自动化或集成时使用。 |
| 42 | [`lark-sheets`](skills/lark-sheets/SKILL.md) | `open.feishu.cn` | 872,502 | 飞书/Lark OpenAPI 场景：sheets。用户要在飞书生态完成相关自动化或集成时使用。 |
| 43 | [`lark-approval`](skills/lark-approval/SKILL.md) | `open.feishu.cn` | 872,452 | 飞书/Lark OpenAPI 场景：approval。用户要在飞书生态完成相关自动化或集成时使用。 |
| 44 | [`lark-wiki`](skills/lark-wiki/SKILL.md) | `open.feishu.cn` | 872,450 | 飞书/Lark OpenAPI 场景：wiki。用户要在飞书生态完成相关自动化或集成时使用。 |
| 45 | [`lark-contact`](skills/lark-contact/SKILL.md) | `open.feishu.cn` | 871,614 | 飞书/Lark OpenAPI 场景：contact。用户要在飞书生态完成相关自动化或集成时使用。 |
| 46 | [`lark-task`](skills/lark-task/SKILL.md) | `open.feishu.cn` | 871,496 | 飞书/Lark OpenAPI 场景：task。用户要在飞书生态完成相关自动化或集成时使用。 |
| 47 | [`lark-slides`](skills/lark-slides/SKILL.md) | `open.feishu.cn` | 871,340 | 飞书/Lark OpenAPI 场景：slides。用户要在飞书生态完成相关自动化或集成时使用。 |
| 48 | [`lark-mail`](skills/lark-mail/SKILL.md) | `open.feishu.cn` | 871,305 | 飞书/Lark OpenAPI 场景：mail。用户要在飞书生态完成相关自动化或集成时使用。 |
| 49 | [`lark-whiteboard`](skills/lark-whiteboard/SKILL.md) | `open.feishu.cn` | 871,140 | 飞书/Lark OpenAPI 场景：whiteboard。用户要在飞书生态完成相关自动化或集成时使用。 |
| 50 | [`lark-event`](skills/lark-event/SKILL.md) | `open.feishu.cn` | 871,070 | 飞书/Lark OpenAPI 场景：event。用户要在飞书生态完成相关自动化或集成时使用。 |
| 51 | [`lark-openapi-explorer`](skills/lark-openapi-explorer/SKILL.md) | `open.feishu.cn` | 870,819 | 飞书/Lark OpenAPI 场景：openapi explorer。用户要在飞书生态完成相关自动化或集成时使用。 |
| 52 | [`lark-attendance`](skills/lark-attendance/SKILL.md) | `open.feishu.cn` | 870,714 | 飞书/Lark OpenAPI 场景：attendance。用户要在飞书生态完成相关自动化或集成时使用。 |
| 53 | [`lark-skill-maker`](skills/lark-skill-maker/SKILL.md) | `open.feishu.cn` | 870,328 | 飞书/Lark OpenAPI 场景：skill maker。用户要在飞书生态完成相关自动化或集成时使用。 |
| 54 | [`lark-workflow-meeting-summary`](skills/lark-workflow-meeting-summary/SKILL.md) | `open.feishu.cn` | 870,185 | 飞书/Lark OpenAPI 场景：workflow meeting summary。用户要在飞书生态完成相关自动化或集成时使用。 |
| 55 | [`lark-workflow-standup-report`](skills/lark-workflow-standup-report/SKILL.md) | `open.feishu.cn` | 869,889 | 飞书/Lark OpenAPI 场景：workflow standup report。用户要在飞书生态完成相关自动化或集成时使用。 |
| 56 | [`lark-minutes`](skills/lark-minutes/SKILL.md) | `open.feishu.cn` | 869,167 | 飞书/Lark OpenAPI 场景：minutes。用户要在飞书生态完成相关自动化或集成时使用。 |
| 57 | [`lark-vc`](skills/lark-vc/SKILL.md) | `open.feishu.cn` | 868,412 | 飞书/Lark OpenAPI 场景：vc。用户要在飞书生态完成相关自动化或集成时使用。 |
| 59 | [`lark-okr`](skills/lark-okr/SKILL.md) | `open.feishu.cn` | 851,670 | 飞书/Lark OpenAPI 场景：okr。用户要在飞书生态完成相关自动化或集成时使用。 |
| 62 | [`lark-markdown`](skills/lark-markdown/SKILL.md) | `open.feishu.cn` | 837,574 | 飞书/Lark OpenAPI 场景：markdown。用户要在飞书生态完成相关自动化或集成时使用。 |
| 64 | [`lark-vc-agent`](skills/lark-vc-agent/SKILL.md) | `open.feishu.cn` | 813,022 | 飞书/Lark OpenAPI 场景：vc agent。用户要在飞书生态完成相关自动化或集成时使用。 |
| 67 | [`lark-apps`](skills/lark-apps/SKILL.md) | `open.feishu.cn` | 782,806 | 飞书/Lark OpenAPI 场景：apps。用户要在飞书生态完成相关自动化或集成时使用。 |
| 84 | [`lark-note`](skills/lark-note/SKILL.md) | `open.feishu.cn` | 653,291 | 飞书/Lark OpenAPI 场景：note。用户要在飞书生态完成相关自动化或集成时使用。 |

<a id="category-cloud"></a>
### `cloud` · 云平台（Azure / Foundry 等）（22）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 83 | [`microsoft-foundry`](skills/microsoft-foundry/SKILL.md) | `microsoft/azure-skills` | 661,244 | Microsoft Foundry / Azure AI 相关项目引导。用户提到 Foundry 时使用。 |
| 85 | [`azure-diagnostics`](skills/azure-diagnostics/SKILL.md) | `microsoft/azure-skills` | 651,977 | Azure 云场景：diagnostics。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 86 | [`azure-prepare`](skills/azure-prepare/SKILL.md) | `microsoft/azure-skills` | 651,077 | Azure 云场景：prepare。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 87 | [`azure-ai`](skills/azure-ai/SKILL.md) | `microsoft/azure-skills` | 650,343 | Azure 云场景：ai。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 88 | [`azure-deploy`](skills/azure-deploy/SKILL.md) | `microsoft/azure-skills` | 650,047 | Azure 云场景：deploy。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 89 | [`azure-validate`](skills/azure-validate/SKILL.md) | `microsoft/azure-skills` | 649,729 | Azure 云场景：validate。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 90 | [`azure-storage`](skills/azure-storage/SKILL.md) | `microsoft/azure-skills` | 648,873 | Azure 云场景：storage。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 91 | [`azure-compliance`](skills/azure-compliance/SKILL.md) | `microsoft/azure-skills` | 648,478 | Azure 云场景：compliance。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 92 | [`appinsights-instrumentation`](skills/appinsights-instrumentation/SKILL.md) | `microsoft/azure-skills` | 648,263 | 云平台与基础设施相关技能 `appinsights-instrumentation`。当任务匹配该上游 skill 名称与场景时使用。 |
| 93 | [`azure-resource-lookup`](skills/azure-resource-lookup/SKILL.md) | `microsoft/azure-skills` | 648,214 | Azure 云场景：resource lookup。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 94 | [`azure-resource-visualizer`](skills/azure-resource-visualizer/SKILL.md) | `microsoft/azure-skills` | 648,172 | Azure 云场景：resource visualizer。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 95 | [`entra-app-registration`](skills/entra-app-registration/SKILL.md) | `microsoft/azure-skills` | 648,140 | 云平台与基础设施相关技能 `entra-app-registration`。当任务匹配该上游 skill 名称与场景时使用。 |
| 96 | [`azure-kusto`](skills/azure-kusto/SKILL.md) | `microsoft/azure-skills` | 647,875 | Azure 云场景：kusto。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 97 | [`azure-aigateway`](skills/azure-aigateway/SKILL.md) | `microsoft/azure-skills` | 647,476 | Azure 云场景：aigateway。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 98 | [`azure-messaging`](skills/azure-messaging/SKILL.md) | `microsoft/azure-skills` | 639,128 | Azure 云场景：messaging。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 101 | [`azure-compute`](skills/azure-compute/SKILL.md) | `microsoft/azure-skills` | 603,962 | Azure 云场景：compute。用户要在 Azure 上完成相关配置、部署或排查时使用。 |
| 102 | [`azure-cloud-migrate`](skills/azure-cloud-migrate/SKILL.md) | `microsoft/azure-skills` | 596,726 | 来自 skills.sh 的 cloud 向 skill「azure-cloud-migrate」。安装量信号约 520,963；详情见上游 microsoft/azure-skills。 |
| 112 | [`azure-quotas`](skills/azure-quotas/SKILL.md) | `microsoft/azure-skills` | 552,503 | 来自 skills.sh 的 cloud 向 skill「azure-quotas」。安装量信号约 476,733；详情见上游 microsoft/azure-skills。 |
| 114 | [`azure-upgrade`](skills/azure-upgrade/SKILL.md) | `microsoft/azure-skills` | 545,650 | 来自 skills.sh 的 cloud 向 skill「azure-upgrade」。安装量信号约 469,874；详情见上游 microsoft/azure-skills。 |
| 127 | [`azure-enterprise-infra-planner`](skills/azure-enterprise-infra-planner/SKILL.md) | `microsoft/azure-skills` | 522,276 | 来自 skills.sh 的 cloud 向 skill「azure-enterprise-infra-planner」。安装量信号约 446,495；详情见上游 microsoft/azure-skills。 |
| 130 | [`azure-kubernetes`](skills/azure-kubernetes/SKILL.md) | `microsoft/azure-skills` | 516,631 | 来自 skills.sh 的 cloud 向 skill「azure-kubernetes」。安装量信号约 440,788；详情见上游 microsoft/azure-skills。 |
| 187 | [`airunway-aks-setup`](skills/airunway-aks-setup/SKILL.md) | `microsoft/azure-skills` | 441,817 | 来自 skills.sh 的 cloud 向 skill「airunway-aks-setup」。安装量信号约 441,817；详情见上游 microsoft/azure-skills。 |

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
### `engineering` · 工程实现（31）

| Rank | Skill | Source | Installs | 说明 |
|-----:|-------|--------|---------:|------|
| 99 | [`caveman`](skills/caveman/SKILL.md) | `juliusbrussee/caveman` | 616,628 | Caveman：极简/直给的工程沟通与实现风格。用户要该技能工作流时使用。 |
| 105 | [`google-agents-cli-adk-code`](skills/google-agents-cli-adk-code/SKILL.md) | `google/agents-cli` | 557,858 | 用 Google Agents CLI / ADK 编写 Agent 代码。用户做 ADK 开发时使用。 |
| 106 | [`google-agents-cli-deploy`](skills/google-agents-cli-deploy/SKILL.md) | `google/agents-cli` | 557,106 | 部署 Google Agents CLI 相关 Agent。用户要发布到运行环境时使用。 |
| 107 | [`google-agents-cli-publish`](skills/google-agents-cli-publish/SKILL.md) | `google/agents-cli` | 556,904 | 发布 Agent 包或制品。用户要 publish 时使用。 |
| 108 | [`google-agents-cli-workflow`](skills/google-agents-cli-workflow/SKILL.md) | `google/agents-cli` | 556,060 | 编排 Agents CLI 工作流。用户要多步 Agent 流水线时使用。 |
| 109 | [`google-agents-cli-eval`](skills/google-agents-cli-eval/SKILL.md) | `google/agents-cli` | 556,052 | 评估 Agent 质量。用户要 eval/打分时使用。 |
| 110 | [`google-agents-cli-scaffold`](skills/google-agents-cli-scaffold/SKILL.md) | `google/agents-cli` | 555,929 | 脚手架生成 Agent 项目。用户要快速起项目时使用。 |
| 111 | [`google-agents-cli-observability`](skills/google-agents-cli-observability/SKILL.md) | `google/agents-cli` | 555,896 | 为 Agent 加观测（日志/追踪/指标）。用户要可观测性时使用。 |
| 137 | [`paper-context-resolver`](skills/paper-context-resolver/SKILL.md) | `lllllllama/rigorpilot-skills` | 492,530 | 来自 skills.sh 的 engineering 向 skill「paper-context-resolver」。安装量信号约 483,766；详情见上游 lllllllama/rigorpilot-skills。 |
| 138 | [`repo-intake-and-plan`](skills/repo-intake-and-plan/SKILL.md) | `lllllllama/rigorpilot-skills` | 491,712 | 来自 skills.sh 的 engineering 向 skill「repo-intake-and-plan」。安装量信号约 482,959；详情见上游 lllllllama/rigorpilot-skills。 |
| 139 | [`minimal-run-and-audit`](skills/minimal-run-and-audit/SKILL.md) | `lllllllama/rigorpilot-skills` | 491,641 | 来自 skills.sh 的 engineering 向 skill「minimal-run-and-audit」。安装量信号约 482,882；详情见上游 lllllllama/rigorpilot-skills。 |
| 140 | [`env-and-assets-bootstrap`](skills/env-and-assets-bootstrap/SKILL.md) | `lllllllama/rigorpilot-skills` | 491,516 | 来自 skills.sh 的 engineering 向 skill「env-and-assets-bootstrap」。安装量信号约 482,769；详情见上游 lllllllama/rigorpilot-skills。 |
| 153 | [`ai-music`](skills/ai-music/SKILL.md) | `gencraft-labs/skills` | 479,098 | 来自 skills.sh 的 engineering 向 skill「ai-music」。安装量信号约 479,098；详情见上游 gencraft-labs/skills。 |
| 156 | [`supabase-postgres-best-practices`](skills/supabase-postgres-best-practices/SKILL.md) | `supabase/agent-skills` | 478,483 | 来自 skills.sh 的 engineering 向 skill「supabase-postgres-best-practices」。安装量信号约 468,744；详情见上游 supabase/agent-skills。 |
| 176 | [`vercel-composition-patterns`](skills/vercel-composition-patterns/SKILL.md) | `vercel-labs/agent-skills` | 444,409 | 来自 skills.sh 的 engineering 向 skill「vercel-composition-patterns」。安装量信号约 430,333；详情见上游 vercel-labs/agent-skills。 |
| 178 | [`nano-banana-2`](skills/nano-banana-2/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 443,784 | 来自 skills.sh 的 engineering 向 skill「nano-banana-2」。安装量信号约 440,246；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 179 | [`image-edit`](skills/image-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 443,327 | 来自 skills.sh 的 engineering 向 skill「image-edit」。安装量信号约 439,802；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 180 | [`nano-banana-edit`](skills/nano-banana-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 443,147 | 来自 skills.sh 的 engineering 向 skill「nano-banana-edit」。安装量信号约 439,642；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 181 | [`flux-kontext`](skills/flux-kontext/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 442,938 | 来自 skills.sh 的 engineering 向 skill「flux-kontext」。安装量信号约 439,432；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 182 | [`wan-2-7`](skills/wan-2-7/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 442,371 | 来自 skills.sh 的 engineering 向 skill「wan-2-7」。安装量信号约 438,872；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 183 | [`gpt-image-edit`](skills/gpt-image-edit/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 442,226 | 来自 skills.sh 的 engineering 向 skill「gpt-image-edit」。安装量信号约 438,712；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 184 | [`seedance-v2`](skills/seedance-v2/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 442,223 | 来自 skills.sh 的 engineering 向 skill「seedance-v2」。安装量信号约 438,719；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 185 | [`happyhorse-1-0`](skills/happyhorse-1-0/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 442,132 | 来自 skills.sh 的 engineering 向 skill「happyhorse-1-0」。安装量信号约 438,632；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 186 | [`flux-2-klein`](skills/flux-2-klein/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 441,966 | 来自 skills.sh 的 engineering 向 skill「flux-2-klein」。安装量信号约 438,466；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 188 | [`ui-ux-pro-max`](skills/ui-ux-pro-max/SKILL.md) | `nextlevelbuilder/ui-ux-pro-max-skill` | 441,566 | 来自 skills.sh 的 engineering 向 skill「ui-ux-pro-max」。安装量信号约 427,165；详情见上游 nextlevelbuilder/ui-ux-pro-max-skill。 |
| 190 | [`caveman-commit`](skills/caveman-commit/SKILL.md) | `juliusbrussee/caveman` | 430,499 | 来自 skills.sh 的 engineering 向 skill「caveman-commit」。安装量信号约 422,405；详情见上游 juliusbrussee/caveman。 |
| 192 | [`kling-3-0`](skills/kling-3-0/SKILL.md) | `prime-skills/runcomfy-agent-skills` | 415,690 | 来自 skills.sh 的 engineering 向 skill「kling-3-0」。安装量信号约 415,690；详情见上游 prime-skills/runcomfy-agent-skills。 |
| 193 | [`caveman-compress`](skills/caveman-compress/SKILL.md) | `juliusbrussee/caveman` | 427,844 | 来自 skills.sh 的 engineering 向 skill「caveman-compress」。安装量信号约 418,533；详情见上游 juliusbrussee/caveman。 |
| 195 | [`caveman-review`](skills/caveman-review/SKILL.md) | `juliusbrussee/caveman` | 426,460 | 来自 skills.sh 的 engineering 向 skill「caveman-review」。安装量信号约 418,371；详情见上游 juliusbrussee/caveman。 |
| 196 | [`minimalist-ui`](skills/minimalist-ui/SKILL.md) | `leonxlnx/taste-skill` | 425,147 | 来自 skills.sh 的 engineering 向 skill「minimalist-ui」。安装量信号约 425,120；详情见上游 leonxlnx/taste-skill。 |
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
