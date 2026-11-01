---
name: skill-creator
description: 从零编写、改写并打磨 Agent Skill（SKILL.md）。用户要创建 skill、优化 description 触发、给 skill 加评测、或把一段工作流沉淀成 skill 时使用。
tags: [skills, authoring, eval]
---

# skill-creator

把可重复工作流打成 **可触发的 Skill**：写清楚何时用，正文给步骤与边界，再小规模试跑改进。

## 何时用

- 「把刚才的流程做成 skill」
- 改现有 SKILL.md、加强触发描述
- 为 skill 设计简单评测用例

## 工作流

1. **抓意图**：技能让助手多会什么？什么话术应触发？输出长什么样？
2. **写草稿**：
   - `name`：短 id
   - `description`：做什么 + **何时用**（写稍积极一点，减少欠触发）
   - 正文：步骤、检查清单、反模式；保持通用，不写死私人账号
3. **结构**：`SKILL.md` 为主；脚本进 `scripts/`，长参考进 `references/`，按需再读。
4. **试跑**：准备 2–3 条真实用户口吻的提示；有/无 skill 对比观感（环境允许时）。
5. **根据反馈改**：泛化，勿过拟合到那两条例子；能复用的脚本收进 skill。
6. **可选**：为 description 准备「该触发 / 不该触发」查询，迭代措辞。

## 写作要点

- description 是主触发器；「何时用」不要只藏在正文
- 解释 **为什么**，少用空洞的 ALWAYS/NEVER 堆砌
- 理想正文 < 500 行；更长就拆 reference 并写明何时打开

## 成功标准

- 新人只看 description 就知道该不该加载
- 按正文能独立完成一类任务；示例不绑死单一仓库隐私路径
