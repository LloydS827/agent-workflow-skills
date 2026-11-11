# 参与与维护

本项目以完整导入的工作流为起点，逐项按实际用途校订和定制。优先在原技能目录中修改，让调用者始终有一个明确入口。需要协助新建或修订技能时，可点名调用 [skill-builder](skills/skill-builder/SKILL.md)。当前使用方法见 [README](README.md)，原始版本见[来源说明](SOURCES.md)。

## 修订一项技能

修订自建技能时，可从[Matt 原版技能调研](docs/matt-skill-design.md)查到相应的上游实例，以及团队在 Notion 和材料交付上的设计取舍。

编写或修订 `SKILL.md` 时，写法见 [skill-builder 的执行流程](skills/skill-builder/SKILL.md#执行流程)第 3 步。

1. 从[技能目录](docs/skills.md)确定它承接的任务，阅读其 `SKILL.md`、配套参考、脚本和 `agents/openai.yaml`。涉及上下游交接时查阅[工作流设计](docs/workflow.md)；涉及五项自建技能时对照[原设计与验收场景](docs/custom-skill-design.md)。
2. 按使用者需要中文化入口、说明或示例，已有内容能满足用途时可保留原文。保留安装名、命令、路径、元数据键和外部系统字段。明确区分措辞调整与有意改变的行为，尤其是调用时机、输出位置和完成条件。
3. 用同一份具体输入对照修订前后行为。记录触发方式、实际产出、是否满足完成条件、仍需人工处理的步骤。涉及记录写入时检查重复调用和部分成功后的恢复；涉及交付文件时检查最终呈现。
4. 如果输入、产出、依赖或步骤变化，同步修订使用说明及相关示例。保留上游归属与许可，导入清单作为历史对照保存。

## 检查改动

运行 `python3 scripts/check.py` 检查技能目录、调用配置和项目内引用。Codex 的 `interface.display_name` 与英文调用名保持一致。新增或移除入口时，同步 README、技能目录文档和检查脚本的清单。仅由人启动的技能同时在 `SKILL.md` 中设置 `disable-model-invocation: true`，在 `agents/openai.yaml` 中设置 `policy.allow_implicit_invocation: false`。

用 README 的安装命令把当前工作副本装进临时业务项目，加 `--check` 核对文件，再从该项目实际调用受影响的技能。需要对照原始导入快照时运行 `python3 scripts/check.py --baseline`；这会列出从导入至今的差异，包括已记录的跨工具适配。

工作区源码、本机安装和云端安装各自核验。发布安排及试用证据见[验证计划](docs/validation.md)。
