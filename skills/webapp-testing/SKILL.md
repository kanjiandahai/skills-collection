---
name: webapp-testing
description: 为 Web 应用设计并运行可靠的 UI/端到端测试与冒烟检查。用户要测页面、写 Playwright/Cypress 测试、加回归、验证修复是否生效时使用。
tags: [testing, e2e, playwright, webapp]
category: engineering
---

# webapp-testing

让 Web 测试 **稳定、表达意图、可在 CI 跑**：少睡轮询，多等条件；少耦合实现细节。

## 何时用

- 新功能要回归网
- 「帮我确认这个 bug 修好了」
- 补 Playwright / Cypress / 同类 E2E

## 工作流

1. 定范围：冒烟（关键路径）还是深测；环境 URL 与测试账号策略。
2. 用用户可见的方式定位：role、label、文案、`data-testid`。
3. 每个用例一条用户路径；准备 → 动作 → 断言清晰。
4. 等待用「元素/响应满足条件」，避免固定 `sleep`。
5. 失败保留 trace/截图/视频（若框架支持）；先修片状再加测。

## 原则

- 测用户可感知行为，不测内部私有类名（除非约定测试钩子）
- 数据隔离：不依赖脏库顺序；可构造夹具
- 保持套件快：E2E 少而精，细节下沉单元测

## 成功标准

- 本地与 CI 同命令可绿
- 失败时有足够附件定位；用例名能当规格读
