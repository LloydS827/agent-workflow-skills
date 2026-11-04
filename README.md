# Agent Workflow Skills

24 项研发工作流技能，覆盖需求澄清、方案简化、执行与验收。可安装到团队项目，也可作为中文定制技能库的起点。

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

在业务项目中新开会话，点名 `to-notion` 或直接读取 `<技能目录>/to-notion/SKILL.md`，尝试下面的请求。

> 请用 to-notion 把以下决定整理成方案草案，直接在对话中给出范围和验收条件。第一版由主持人录入会议待办、负责人和完成条件，成员查看自己的事项，日历同步留到以后。

这个练习无需连接 Notion。正式写入时提供目标项目和连接器权限。团队可将安装后的技能目录纳入业务仓库，供成员共用。

## 进一步使用与定制

- [技能目录](docs/skills.md) · [工作流设计](docs/workflow.md) · [使用与更新](docs/getting-started.md)
- [修改技能](CONTRIBUTING.md) · [来源与许可](SOURCES.md) · [验证记录](docs/validation.md)

以本库继续定制时，在 `skills/` 中修改，运行 `python3 scripts/check.py`，再安装到试用项目验证。
