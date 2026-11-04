# Agent Workflow Skills

24 项研发工作流技能，覆盖需求澄清、方案简化、执行与验收。可安装到团队项目，也可作为中文定制技能库的起点。

## 主流程

**澄清需求 → 建立项目 → 形成方案 → 简化 → 组织执行 → 实施与验收 → 反馈更新**

| 步骤 | 技能 | 完成什么 |
| --- | --- | --- |
| 澄清需求 | `grill-with-docs`；复杂探索用 `wayfinder` | 确定目标、约束和关键取舍 |
| 建立项目 | `init-notion-project` | 首次建立或复用 Notion 项目主页 |
| 形成方案 | `to-notion` | 把共识写成包含范围、依据和完成条件的方案 |
| 简化 | `simplify` | 判断哪些工作应保留、删除、复用或延后，修订原方案 |
| 组织执行 | `to-pm` | 按成果安排里程碑、Issues、执行步骤和依赖 |
| 实施与验收 | `implement`、`research`、`project-docs` | 按任务完成软件实现、调查研究或材料交付，并核对证据 |

执行结果由 `to-pm` 回写原 Issue，达到完成条件后验收；影响路线的结论由 `to-notion` 更新原方案，再调整后续工作。人负责目标、关键取舍和验收，Agent 在明确范围内推进。

## 本项目的 Notion 约定

**Notion 是本团队选定的存档与材料对接平台。** 上述流程按这一选择实现：项目主页汇集方案、里程碑、Issues 和成果链接，便于团队查阅与交接。代码、数据和实验原始记录保留在项目文件或原系统中，由 Notion 引用。

通过 `init-notion-project`、`to-notion`、`to-pm` 写入 Notion 前，需要在 Agent 工具中配置可操作页面和数据库的 Notion 连接，并授权访问目标项目。安装技能本身不会完成这项连接与授权。

其他团队可复用主流程，并自行选择存档平台。更换平台时，需要适配上述三项技能及[共享记录规则](skills/_shared/record-writing.md)，同时衔接 `simplify` 等技能的回写步骤。需求澄清、研究和实现等技能可独立使用。

## 安装

**交给 Agent 安装**。在业务项目中打开 Codex、WorkBuddy 等工具，发送下面的请求。

> 请将 https://github.com/LloydS827/agent-workflow-skills 中的整套技能安装到当前项目。先读 README，按当前工具选择安装目录，运行安装脚本及 --check 校验。保留已有的不同内容，完成后告诉我如何调用。

**自行安装**。需要 Git 和 Python 3，在终端运行以下命令。将 `/path/to/project` 换成业务项目根目录，并按下表选择技能目录。

```sh
git clone https://github.com/LloydS827/agent-workflow-skills.git
cd agent-workflow-skills
python3 scripts/install.py "/path/to/project/.agents/skills"
python3 scripts/install.py "/path/to/project/.agents/skills" --check
```

| 工具 | 项目内的技能目录 |
| --- | --- |
| Codex | `.agents/skills/` |
| WorkBuddy | `.codebuddy/skills/` |
| DeepSeek Harness | `.dsh/skills/`，也可共用 `.agents/skills/` |
| 其他 Agent | 使用其规定的技能目录，或放入 `team-skills/` 后按路径读取 |

Windows 可将 `python3` 换成 `py -3`。也可从 GitHub 下载 ZIP，按[手动安装说明](docs/getting-started.md#手动复制安装)操作。安装包含共享参考和许可；遇到同名文件的不同内容时会列出冲突。

## 开始使用

以下以本项目的 Notion 工作流为例。完成技能安装与 Notion 连接后，在业务项目中新开会话，准备项目目标、已有材料和 Notion 父页或项目主页，从需求澄清开始。

> 请用本项目安装的技能推进 [项目名称]。目标是 [目标]，已有材料是 [材料]，Notion 入口是 [链接]。先用 grill-with-docs 澄清需求，再用 init-notion-project 建立或复用项目，用 to-notion 形成方案、simplify 简化、to-pm 组织执行任务。影响目标与范围的取舍由我确认，最后给出近期可开始的任务及验收条件。

任务安排明确后，选择一项开展实施与验证，并把结果交回原记录。

> 请执行 [Issue 或其中的步骤]，按任务选择实现、研究或材料技能，依据约定条件验证成果。完成后用 to-pm 回写证据与进展；影响原方案的发现先提出调整建议。

已有项目可从当前进度进入，研究可穿插各步。需要分步推进时直接点名相应技能；暂未连接 Notion 时，可先完成澄清和方案草案。[完整示例](examples/meeting-actions.md)

## 进一步使用与定制

- [技能目录](docs/skills.md) · [工作流设计](docs/workflow.md) · [使用与更新](docs/getting-started.md)
- [修改技能](CONTRIBUTING.md) · [来源与许可](SOURCES.md) · [验证记录](docs/validation.md)

以本库继续定制时，在 `skills/` 中修改，运行 `python3 scripts/check.py`，再安装到试用项目验证。
