# 开始使用

## 打开业务项目

按 [README 的安装说明](../README.md#安装)把技能装进目标项目，再在 Agent 中打开这个项目。试用修订版本时，确认选中的入口来自刚安装的目录。对于按路径读取的工具，用「读取 `team-skills/<技能名>/SKILL.md`」启动，相互调用的技能也从同一目录读取。下文给出的是技能名。

只做需求澄清时可以直接使用 [grill-with-docs](../skills/grill-with-docs/SKILL.md)。需要跨会话推进多个相互依赖的决定时选 [wayfinder](../skills/wayfinder/SKILL.md)，提前明确目标工程的 tracker。要访问 Notion，先在 Agent 中启用 Notion 插件或配置 Notion MCP，并完成工作区授权。告诉 Agent 页面名称即可开始查找，有现成链接也可直接用。新项目优先使用你指定的父页，其次沿用当前业务项目的位置约定。

## 手动复制安装

从 GitHub 下载并解压整个技能库。在业务项目中创建 README 对应的技能目录，把本库 `skills/` 里面的所有文件夹复制进去，包括 `_shared/`。再将 [Matt 的许可文件](../licenses/mattpocock-skills-MIT.txt) 放到目标 `_shared/` 下。安装后应能直接找到 `目标技能目录/to-notion/SKILL.md`。已有同名内容先比较，保留团队的修改。

## 工具与调用

| 工具 | 调用方法与目录依据 |
| --- | --- |
| Codex | 在 CLI 输入 `$` 选择技能；同名时选择来自业务项目的版本。[官方说明](https://learn.chatgpt.com/docs/build-skills) |
| WorkBuddy | 在本地项目会话中点名技能。自动发现仍需在桌面端验证，找不到时直接要求读取 `.codebuddy/skills/to-notion/SKILL.md`。[项目配置说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project) |
| DeepSeek Harness | 输入 `/to-notion`。Git 项目安装到仓库根目录，支持 `.dsh/skills/` 与 `.agents/skills/`。[目录规则](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md) · [调用方式](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/tool-skill/README.md) |
| 其他文件型 Agent | 要求读取 `team-skills/to-notion/SKILL.md` 并依照说明执行，配套技能与共享参考也从同一目录读取。 |

## 从讨论走到执行安排

可使用[会议待办练习](../examples/meeting-actions.md)的输入，或换成真实项目的讨论结论。把下面方括号中的内容换成你的项目与需求。

> 请使用安装在这个业务项目里的技能。先用 grill-with-docs 确认第一版的目标与验收条件，再依次用 init-notion-project、to-notion、simplify、to-pm，将方案和执行安排写入 [目标父页或已有主页]，项目名为 [名称]。已有共识和材料如下：[内容]。重大取舍交给我决定。最后返回实际入口、最终保留的范围和仍待验证的事项。

已有项目复用原主页。已明确需求可跳过澄清，已有候选方案从 simplify 开始；能核实该版本经 simplify 定稿时，直接用 to-pm 拆票。初始化仅预留区域，to-pm 在需要时建立或复用里程碑与 Issues 数据库。详情见[工作流设计](workflow.md)。

## 推进一个已领取的任务

- **软件**　读取 [implement](../skills/implement/SKILL.md)，例如「请用 implement 领取 QUEUE-017 的第一步，把提交、验证结果和剩余条件交给 to-pm」。Agent 会按业务项目约定查原票与执行版，按指定范围审查交付。需同步回写时可在同一请求中交办。
- **整份软件方案**　需要协调多张原票时，用 [implement-all](../skills/implement-all/SKILL.md)。例如「请执行这份已定稿的方案。先告诉我哪些成果已有证据、哪些 Issue 可并行、哪些还缺输入，然后按顺序实施并集成验收。」只需梳理顺序时可明确说「这轮只给执行安排」。
- **调查**　读取 [research](../skills/research/SKILL.md)，给出问题和要支撑的决定，保留一手来源与研究记录。
- **正式材料**　读取 [project-docs](../skills/project-docs/SKILL.md)，给出读者、用途、已有依据和格式要求。

完成后可这样交回结果：

> 请用本项目安装的 to-pm，根据 [证据与反馈] 更新 [项目及 Issue 编号] 中的原记录。保留人工备注和其他未完成步骤。说明哪些完成条件已有证据，哪些仍待验证。

## 团队如何更新

从新版技能库的根目录运行原安装命令，加上 `--check`。例如 Codex 项目可执行 `python3 scripts/install.py "../我的项目/.agents/skills" --check`。检查只读取文件。若只是缺失文件，重跑安装命令就会补齐。若有同名文件内容不同，脚本会在写入前列出冲突。

有冲突时，先把新版安装到一个临时空目录，将差异与业务项目的已安装版本比较。保留团队定制，合并希望采用的改动，确认上游已删除的文件是否也应在项目中移除。用原来的试用请求复验后，在业务仓库中记录此次更新。安装器只补文件，其他组件和旧文件由项目维护者决定是否保留。

V0.21 起，整份软件方案改用 `$implement-all`，单张 Issue 或票内步骤继续用 `$implement`。从 V0.2 升级时，先核对新入口已安装，再将旧版 `implement-spec/` 移到技能目录之外备份，并更新团队提示中的调用名。

正式文档技能统一叫 `project-docs`。曾单独安装 `formal-project-docs` 的成员，在核对新版后把旧目录移到技能目录之外备份，并将个人调用改为 `$project-docs`。

只支持单技能上传的客户端需要每个包自带它使用的参考文件。部分技能会读取兄弟目录 `_shared/`，逐个上传原始文件夹会丢失这些引用。可读本地项目时，优先采用 README 中的整套安装方式。

## 运行环境

Notion 写入需要页面、数据库、关系和视图的相应权限。缺少写入能力时交付标明状态的草案。研究、审查与并行实现按各自方法使用子 Agent；实现还需代码执行、测试和版本管理工具。生成 Word、演示文稿、表格或 PDF 时，需要相应的制作与渲染工具。本机安装、云端安装和按路径读取是三种不同的使用条件，分别验证。
