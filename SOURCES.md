# 来源与版本

## 本次导入

2026-11-02 以 P00CodingAgent 个人工作流在 2026-10-30 确认的 **24 项在用技能**为起点。首次迁入的五项自建技能和两份共享参考共 13 个文件。本次补入 19 项 Matt 技能共 60 个文件。两批共 73 个技能文件，均保留导入时的内容与目录内布局。[SHA-256 清单与上游目录对照](docs/source-baseline.json)

| 来源 | 包含的技能 |
| --- | --- |
| 维护者工作流 | init-notion-project、to-notion、simplify、to-pm、project-docs，另含 `_shared/` 的项目布局与写入约定 |
| Matt Pocock · engineering | code-review、codebase-design、diagnosing-bugs、domain-modeling、grill-with-docs、implement、implement-spec、improve-codebase-architecture、prototype、research、retro、setup-matt-pocock-skills、tdd、triage、wayfinder |
| Matt Pocock · productivity | grilling、handoff、teach、writing-for-agents |

19 项技能按个人工作流采用的版本迁入。导入时将每项的全部相对路径和 Git blob 哈希与上游提交 `5beb35b040e3de97e54fa9e386d7e42d15c295c2` 的文件树核对，60 个文件全部一致。上游按用途分组，本项目在 `skills/` 下按技能名平铺。Matt Pocock 的版权声明和 MIT 许可全文随这些文件保留。[固定版本源码](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2) · [上游许可副本](licenses/mattpocock-skills-MIT.txt)

## 工作流和设计依据

[工作流设计](docs/workflow.md)、[术语表](GLOSSARY.md)和[自建技能设计与验收](docs/custom-skill-design.md)来自个人工作流定稿的 README、术语表及项目设计记录。迁入的内容涵盖工作方法、工具分工、交接与验收，案例采用合成输入。初版 README 的组织参考了 Matt 项目的使用入口与贡献说明。

2026-10-30 建立项目目录时参考的上游 README 和 CONTRIBUTING.md 的 Git blob 分别为 `f7038f139299985eea6c3e18398dbafb379a0010` 和 `5895f1e8ac654a9c477243b187cbe901cd614d72`。技能源码采用上表所列的固定版本。

to-notion 借鉴 to-spec 综合已有讨论的做法，to-pm 沿用 to-tickets 按成果拆分任务的思路。simplify 检查删除一项工作后复杂度去了哪里，project-docs 合并了维护者原有 formal-project-docs 的工作方法和审校清单，涵盖正式行文、预算口径、跨文件一致性、外部读者独立阅读与最终呈现检查。项目内统一从 project-docs 调用。to-spec 和 to-tickets 在这里是设计出处；当前主流程通过 to-notion 和 to-pm 运行。原型、测试、审查与研究等实际调用的支撑技能已随项目收录。

旧入口 to-linear 在个人工作流中已退役，历史设计由 to-pm 的设计说明承接。文档、演示文稿、表格和 PDF 制作能力，以及 Notion 连接器等，由目标运行环境提供。

## 后续修订

每项导入技能都在本项目内继续维护。中文化时保留作者与许可，记录翻译之外的行为变化；可用文件清单或上游固定版本回看修订前内容。项目自有内容的发行许可和公开发布方式另行确定。

首次跨工具适配在五项自建技能的 `SKILL.md` 中补齐了 `disable-model-invocation: true`，使读取该字段的客户端也能沿用项目的显式调用约定。原始 SHA-256 清单保留作对照。安装脚本把上游许可随技能复制到目标的 `_shared/`。
