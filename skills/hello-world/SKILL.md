---
name: hello-world
description: 示例技能：演示 skills-collection 的目录与 frontmatter 约定；新技能可复制此模板改写。
tags: [example, starter]
category: meta
---

# hello-world

这是一个占位示例，用来展示本仓库的 skill 格式。真正有用的技能请替换或另建目录。

## 何时使用

- 你在熟悉本仓库结构，或准备复制模板写新 skill 时

## 要做什么

1. 复制 `skills/hello-world/` 为新的 `skills/<id>/`
2. 改写 frontmatter 里的 `name`、`description`、`tags`
3. 在正文写清触发场景、步骤与成功标准
4. 运行 `python3 scripts/build-catalog.py` 更新 `catalog.json`

## 成功标准

- 新 skill 有独立目录与合法 frontmatter
- `catalog.json` 中能看到对应条目
