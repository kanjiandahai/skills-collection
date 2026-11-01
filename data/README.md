# data/

本目录存放 **灌入用快照**，不是 skill 索引本身。

- 真正的索引在仓库根目录的 `skills/*/SKILL.md` 与 `catalog.json`。
- `snapshots/` 下的 JSON 记录某次从 skills.sh（经 LinklyAI/best-skills）读取并考虑入库的候选名单，便于审计与回放。
- `skills-sh-top100-2026-11-01.json`：bootstrap 种子（All-Time 去重 Top100）。
- 之后由 `scripts/refresh-from-skills-sh.py` 写入 `skills-sh-YYYY-MM-DD.json`。

刷新脚本默认 **只增不减**：快照变小或榜单换血，不会删除已有 skill。
