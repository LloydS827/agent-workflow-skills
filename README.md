# Agent Workflow Skills · V0.21

一套从需求讨论走到交付验收的研发工作流，可直接安装到团队项目。仓库收录 5 项团队自建技能和 19 项来自 Matt Pocock 的技能，共 24 项。

## 主流程

| 步骤 | 怎么做 | 交给下一步什么 |
| --- | --- | --- |
| 1. 澄清需求 | 用 `grill-with-docs` 追问目标、约束和关键取舍，由需求方决定 | 本轮要解决的问题，以及怎样算做成 |
| 2. 建立项目 | 用 `init-notion-project` 建立或复用项目主页 | 一个团队入口，预留 Issues 和里程碑区域 |
| 3. 记录候选方案 | 用 `to-notion` 整理讨论、依据与待验证项 | 一份待简化的候选方案 |
| 4. 简化并定稿 | 用 `simplify` 检查哪些工作可以取消、复用或延后 | 同一方案页上的执行版本、保留范围和验收条件 |
| 5. 拆解与领取 | 用 `to-pm` 从定稿拆出 Issue，在票内列出具体步骤（ticket） | 可先领取的编号、前置依赖、交付物与验收条件 |
| 6. 实施与验收 | 单项软件工作用 `implement`，跨多张 Issue 的整份方案用 `implement-all`，正式材料用 `project-docs` | 成果、验证证据和仍待完成的条件 |
| 7. 反馈更新 | 用 `to-pm` 回写原票，勾选已验证的步骤，整项达标后结项 | 若结果改变范围或路线，用 `to-notion` 记回原方案，经 `simplify` 定稿后再调票 |

需要核实技术事实时，可在相应步骤调用 `research`，将一手来源和结论交回当前任务。

### 本团队的 Notion 约定

团队用 Notion 对接方案、里程碑和 Issues。代码、数据与实验日志保留在原位置，由项目页引用。实际读写需要在 Agent 中接入并授权 Notion MCP。新建项目优先使用用户指定的父页，其次沿用业务项目的约定，两者都没有时再询问。本团队约定的父页叫「项目总览」。其他团队可替换存档平台，按相同的交付物衔接各步。[Notion 接入说明](https://developers.notion.com/guides/mcp/get-started-with-mcp) · [共享写入约定](skills/_shared/record-writing.md)

## 安装

**交给 Agent 安装**时，在 Codex、WorkBuddy、DeepSeek Harness 等工具中打开业务项目，发送以下请求。

> 请从 https://github.com/LloydS827/agent-workflow-skills 安装 v0.21 的全部技能到当前项目。按 README 选择本工具的目录，运行安装脚本，再用 --check 核对。保留已有的不同内容，完成后告诉我怎样调用。

**自行安装**需要 Git 和 Python 3。下面是 Codex 的安装命令，请将路径换成自己的业务项目。其他工具按表替换技能目录。

```sh
git clone --branch v0.21 https://github.com/LloydS827/agent-workflow-skills.git
cd agent-workflow-skills
python3 scripts/install.py "/path/to/project/.agents/skills"
python3 scripts/install.py "/path/to/project/.agents/skills" --check
```

| 工具 | 业务项目内的技能目录 |
| --- | --- |
| Codex | `.agents/skills/` |
| WorkBuddy | `.codebuddy/skills/` |
| DeepSeek Harness | `.dsh/skills/` 或 `.agents/skills/` |
| 其他 Agent | 使用工具指定的目录，或安装到 `team-skills/` 后点名读取其中的 `<技能名>/SKILL.md` |

Windows 可用 `py -3`。安装脚本会复制共享参考和上游许可，遇到同名文件内容不同会列出冲突。从 V0.2 升级时，把旧调用名 `implement-spec` 换成 `implement-all`。[手动复制](docs/getting-started.md#手动复制安装) · [升级已有安装](docs/getting-started.md#团队如何更新)

## 开始使用

新项目可以从这条请求开始。

> 请用本项目的工作流推进 [项目名]。目标是 [目标]，已有材料是 [材料]。先用 grill-with-docs 和我澄清关键取舍，再依次用 init-notion-project、to-notion、simplify、to-pm 建立项目、定稿和拆票。最后给出当前可领取的 Issue 编号、输入和验收条件。

已有可领取的任务时，直接指定要做的范围。

> 请领取 [Issue 编号及链接] 的 [整项或指定步骤]，按票内条件实施和验证。用 to-pm 将成果和证据回写原票，说明还剩哪些验收条件。

[会议待办收集示例](examples/meeting-actions.md) · [完整工作流设计](docs/workflow.md)

## 全部 24 项技能

| 用途 | 技能与作用 |
| --- | --- |
| 需求与决策 | [grill-with-docs](skills/grill-with-docs/SKILL.md) 澄清需求并记录共识 · [grilling](skills/grilling/SKILL.md) 追问关键取舍 · [domain-modeling](skills/domain-modeling/SKILL.md) 维护术语和决策记录 · [wayfinder](skills/wayfinder/SKILL.md) 梳理跨会话的决策依赖 |
| 项目与交付 | [init-notion-project](skills/init-notion-project/SKILL.md) 建项目主页 · [to-notion](skills/to-notion/SKILL.md) 写方案与结论 · [simplify](skills/simplify/SKILL.md) 删减范围并定稿 · [to-pm](skills/to-pm/SKILL.md) 拆票与回写 · [project-docs](skills/project-docs/SKILL.md) 制作和检查正式材料 |
| 实现与验证 | [implement](skills/implement/SKILL.md) 按交办范围实现软件 · [implement-all](skills/implement-all/SKILL.md) 按依赖组织整份规格的多任务实现 · [tdd](skills/tdd/SKILL.md) 用行为测试驱动实现 · [code-review](skills/code-review/SKILL.md) 按规范和需求审查变更 · [diagnosing-bugs](skills/diagnosing-bugs/SKILL.md) 诊断故障与性能退化 |
| 调研与设计 | [research](skills/research/SKILL.md) 查一手来源，留下带引用的研究笔记 · [prototype](skills/prototype/SKILL.md) 用原型检验设计 · [codebase-design](skills/codebase-design/SKILL.md) 推敲模块边界 · [improve-codebase-architecture](skills/improve-codebase-architecture/SKILL.md) 寻找架构改进点 |
| 协作与学习 | [triage](skills/triage/SKILL.md) 分类和核实待办请求 · [handoff](skills/handoff/SKILL.md) 交接会话 · [retro](skills/retro/SKILL.md) 复盘编码过程 · [teach](skills/teach/SKILL.md) 组织学习 |
| 配置与维护 | [setup-matt-pocock-skills](skills/setup-matt-pocock-skills/SKILL.md) 配置工程任务跟踪与领域文档 · [writing-for-agents](skills/writing-for-agents/SKILL.md) 编写技能与 Agent 指令 |

[技能目录与产出](docs/skills.md) · [定制与贡献](CONTRIBUTING.md) · [来源与许可](SOURCES.md) · [验证记录](docs/validation.md)
