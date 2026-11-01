---
name: find-skills
description: 发现、筛选并安装合适的 Agent Skill。用户说找不到 skill、有没有某某能力、帮我搜 skill、skills.sh / npx skills、或不知道该装哪个 skill 时使用。
tags: [skills, discovery, catalog, install]
---

# find-skills

帮助用户在公开生态里 **找到并对上号** 的 skill，而不是从零臆造一套流程。

## 何时用

- 「有没有做 X 的 skill」「推荐几个 skill」
- 提到 skills.sh、`npx skills`、ClawHub、某厂商 skill 市场
- 本仓库 `catalog.json` 不够用、需要外站补充时

## 工作流

1. **澄清任务**：要解决什么、运行在哪个助手/环境（Claude Code、Cursor、其他）。
2. **先查本地索引**：读本仓 `catalog.json` 与 `skills/*/SKILL.md` 的 description，能命中就直接推荐路径。
3. **再查公开榜单**：打开 [skills.sh](https://www.skills.sh/) 或对应 registry，用任务关键词与安装量/热度交叉验证；注明数据日期与来源。
4. **对比 2–5 个候选**：触发场景、是否绑死某一产品 CLI、许可证、维护活跃度。
5. **给出安装方式**：优先官方文档命令（如 `npx skills add owner/repo --skill name`）；不要编造不存在的包名。
6. **落地**：用户确认后，按目标环境写入 skill 目录或说明如何启用。

## 推荐原则

- 通用流程 skill 优于单一 SaaS 的整包 CLI（除非用户就要那个产品）
- description 写清「何时触发」的 skill 通常比只有工具名的更有用
- 安装量高 ≠ 适合：核对是否与用户栈匹配

## 成功标准

- 至少给出 1 个可安装、与任务对齐的 skill，并写明来源链接
- 说清为何选它、有何替代；用户能直接复制安装命令
