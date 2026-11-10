# Matt 原版技能如何写，以及如何用于本团队的修订

Matt 把三个判断写在不同位置。用户或 Agent 从描述判断该选哪个技能，执行者从正文判断眼下该做哪一步，接手者从产物判断工作到了哪里。例如 `grill-with-docs` 的正文只有一条指令，分别加载访谈和领域建模两个技能。访谈何时问、词条何时写、哪种决定值得单独记录，都由真正执行该工作的技能定义。对团队最有价值的借鉴，是把每个判断放在会用到它的地方。[原版澄清入口](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/grill-with-docs/SKILL.md) · [原版写作说明](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL.md)

## 本次查了什么

本库的来源记录已给出上游提交 `5beb35b040e3de97e54fa9e386d7e42d15c295c2` 和目录映射。2026-11-07 按该映射逐项核对 19 个上游目录的文件集合，重新计算本地 60 个文件的 Git blob 标识和 SHA-256，分别与留存的上游文件树和导入清单比对，全部一致。下文引用 Matt 原文时均链接到该提交，团队现行规则则链接到本库，便于逐项修订后继续比较。[来源记录](../SOURCES.md) · [逐文件清单](source-baseline.json) · [上游固定版本](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2)

另核对了同一提交的上游调用约定，以及团队设计说明提到的 `to-spec`、`to-tickets` 两份原文。这两个技能是 `to-notion` 与 `to-pm` 的设计来源，安装清单仍为 19 项 Matt 技能加 5 项自建技能。本文的实证范围是源码及其引用关系，客户端运行效果另见项目的试用记录。[上游调用约定](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/.agents/invocation.md) · [团队设计依据](custom-skill-design.md) · [项目验证记录](validation.md)

## 描述怎样影响调用

| 固定版本中的选择 | 描述写给谁 | 文件里怎样实现 |
| --- | --- | --- |
| 10 项由用户显式选择 | 给浏览技能的人一句话，说明会得到什么。如 `implement` 接收方案或任务，完成相应实现。 | `SKILL.md` 的 `disable-model-invocation: true` 与 `agents/openai.yaml` 的 `policy.allow_implicit_invocation: false` 配对。界面另用 `display_name` 和 `short_description` 展示。[入口](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement/SKILL.md) · [界面配置](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement/agents/openai.yaml) |
| 9 项允许 Agent 或用户选择 | 说明哪种任务适用。例如 `prototype` 把「验证状态或逻辑」和「探索界面形态」写入描述，正文对这两类问题给出不同产物。 | 匹配到的 9 项均省略上述禁用字段，在同一份界面配置中保留人能读懂的简介。[入口](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/SKILL.md) · [界面配置](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/agents/openai.yaml) |

描述还承担检索成本。Matt 建议把真正改变处理方式的情形各写一次，让执行步骤留在加载后的正文中。中文修订时，可先问「使用者想拿到什么」，再看技能是否需要由 Agent 自主发现。本团队五项技能都保留显式入口，因此可以分别用一句中文写清结果，同步修订选择器文字。技术名称继续用于安装和调用。这个建议沿用的是本库既有调用策略。[写作原理](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL.md#context-pointers) · [技能机制](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL-MECHANICS.md) · [本库技能目录](skills.md)

上游把「现在加载一个配套技能」写成对技能工具的调用，把「下一步可以选哪个显式入口」写成给人的指引。几个显式入口共用一份规则时，可让它们分别引用普通文件。本库的 Notion 布局和写入约定适合沿用这种方式，主流程的箭头表示交接次序，调用范围由用户交办的环节决定。[上游依赖约定](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/.agents/invocation.md#dependencies-between-them) · [团队流程](workflow.md)

翻译描述时还要核对正文。例如同一提交的 README 用 `red-green-refactor` 概括 TDD，技能描述也收录了这个检索词。正文明确把每一轮写成「一个失败测试→最少实现使之通过」，把重构安排到审查阶段。若按 README 的文字直接翻译执行步骤，就会改变重构发生的时机。[上游 README](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/README.md) · [TDD 的执行规则](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md#rules-of-the-loop)

## 从需求讨论到实施，原版怎样交接

| 工作发生在哪里 | 原版怎样约束下一步 | 接手时能看到什么 |
| --- | --- | --- |
| 澄清需求 | `grill-with-docs` 分别调用 `grilling`、`domain-modeling`。前者一轮只问前提已确定的问题，给出建议答案。后者在术语达成共识时更新词条，仅在决定难逆转、脱离上下文难理解且确有取舍时提议写 ADR。 | 已解决的决定和领域定义。尚依赖其他答案的问题留给下一轮。[澄清](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/grill-with-docs/SKILL.md) · [提问](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md) · [术语与决策](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/SKILL.md) |
| 跨会话探索 | `wayfinder` 先确定这次要解决的决定，再建一张地图。可以说清的问题才建子 Issue，有些子 Issue 虽能写清问题，仍需等依赖解决后才能领取。先建记录取得真实标识，再连阻塞关系。 | 主 Issue 索引结论，子 Issue 的评论保存答案。下一会话从未关闭、未被阻塞、未被领取的决定中选择。[地图与决策子 Issue](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wayfinder/SKILL.md) |
| 将讨论形成软件规格 | `to-spec` 从已有讨论、实现、领域术语和 ADR 综合规格。它特别要求与用户核对测试接口，优先复用能观察完整行为的已有接口。 | 发布到配置的 issue tracker，标为 `ready-for-agent`。正文保存用户行为、实施决定、测试和范围。能更准确表达已定结构的原型片段可以保留。[固定版本 to-spec](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-spec/SKILL.md) |
| 从规格拆出可执行工作 | `to-tickets` 读取来源全文及评论，将软件拆成能独立演示或验证的完整行为。大范围机械迁移另有分支，先使新旧形式并存，分批迁移后再移除旧形式。让用户核对粒度和真正阻止开工的依赖，再发布。 | 本地跟踪器每项工作一个文件，在线跟踪器每项一条记录，按前置顺序建立，凭真实标识连接。每项写明交付行为、验收条件和阻塞因素。[固定版本 to-tickets](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-tickets/SKILL.md) |
| 实施和验收 | `implement` 先核实传入任务的标题，在已约定的测试接口使用 `tdd`，完成后调用 `code-review`。后者先固定比较起点，再分别按仓库规范和来源规格审查。 | 实现、测试和提交可追溯到同一项任务。两类审查保留各自结论。整份规格的并行实现由独立入口 `implement-spec` 读取任务依赖，在集成分支合并并复核。[单项实现](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement/SKILL.md) · [测试](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md) · [审查](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/code-review/SKILL.md) · [整份规格](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement-spec/SKILL.md) |

这里有一个容易影响团队设计的区别。Matt 的决策子 Issue 用问题及答案标记完成，可执行的 ticket 用可验证的交付行为标记完成。本团队又把可单独跟踪的成果叫作 Issue，把 Issue 内的执行步骤叫作 ticket。按流程修订时，需要逐处写对完成对象，才能处理「测量做完了，但假设被否定」或「脚本跑过了，但整项还待现场验收」这样的反馈。[原版地图](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wayfinder/SKILL.md) · [团队术语](../GLOSSARY.md) · [团队工作流](workflow.md)

## 正文、参考文件和工具各写什么

- **共用判断留在入口，分支细节放在要用的地方。** `prototype` 的入口先判定要试逻辑还是界面，再分别指向两份制作说明。逻辑分支交付可单独打开的 HTML，界面分支交付能切换备选设计的路由。正文保留两者都要遵守的条件，如展示相关状态、留下问题与结论。读者知道何时点开哪个文件，也知道两种结果怎样比较。[入口与分支](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/SKILL.md) · [逻辑原型](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/LOGIC.md) · [界面原型](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/UI.md)
- **给步骤一个能重新观察到的结束条件。** `diagnosing-bugs` 先要求实际运行能触发用户所报故障的命令并展示脱敏输出，再缩小复现场景。需要人操作时才读取 shell 模板，模板把操作提示和结果采集分开。由此可推得，写入类技能适合用「回读到哪条记录、哪些字段或正文」界定完成，使用者才知道上次超时后该从哪里继续。[诊断步骤](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/SKILL.md) · [人工复现模板](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh)
- **初始化先查现状，再选择需要的分支。** `setup-matt-pocock-skills` 检查仓库里的跟踪器、领域文档与已有配置。是否安装 `triage` 决定是否讨论分诊标签，已有配置块则原位更新。上游让用户审阅配置草案后写入。本团队可以借鉴的部分是依据现状补缺，而首次创建和确认权限的规则由团队自己的项目约定决定。[仓库初始化](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/SKILL.md) · [本项目写入约定](../skills/_shared/record-writing.md)
- **判断能否删减，要说明删后谁承担工作。** `codebase-design` 在模块层面做删除测试，检查原有复杂度会消失还是分摊给多个调用方。`improve-codebase-architecture` 在有实际变更和维护负担的地方寻找候选，为每项呈现改前改后的差异，等待人选定一项深入讨论。将这一问法用于需求、实验和协作成本，属于团队对原方法的扩展。[模块删除测试](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md#principles) · [候选方案如何呈现](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/improve-codebase-architecture/SKILL.md)
- **把证据交给下一位执行者。** `research` 要求后台调查一手来源，按主张引用，将结果写入仓库内一份 Markdown。`handoff` 则把下一会话需要的上下文写入临时目录，对已有规格、提交和 Issue 直接给出路径或链接。两者的存放位置由下一个使用者和材料寿命决定。[研究记录](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/research/SKILL.md) · [会话交接](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/handoff/SKILL.md)

同一版本还有三种值得查阅的持久化做法。`triage` 恢复已有条目时先读上轮问题及新答复，再依据验证结果更新状态。`teach` 把学习目标、资料、课程和学习记录分别落到有明确用途的文件，跨会话可续接。`retro` 用实际会话记录定位出错点，先查已有检查，再判断适合改自动检查、导航指引还是需要人判断的审查规则。三者分别适用于反复维护同一记录、长期维护多类材料、事后修订方法。[分诊](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/triage/SKILL.md) · [教学](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/SKILL.md) · [复盘](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/retro/SKILL.md)

## 五项自建技能的修订议题

下表按团队主流程排列，列出**待讨论的建议**。本团队选择 Notion 作为存档与材料对接平台，启用位置、主页布局、任务编号和正式文件验收都以团队约定为准。表中的情境可在后续修订时作为前后对照输入。[团队工作流](workflow.md) · [原设计及验收场景](custom-skill-design.md)

| 自建技能 | 推荐讨论的具体改法 | 用什么输入检验 |
| --- | --- | --- |
| `init-notion-project` | 借鉴仓库初始化的「查现状→补缺」。中文描述写明建立或复用一个 Notion 项目主页。正文依照新项目、已有主页选择动作，只在相应步骤引用共享布局和写入规则。 | 已有主页含任务库和人工说明，里程碑区域缺失。观察是否能沿用原主页和原库，只补缺失区域并回读。再次执行应引用同一入口。[现行入口](../skills/init-notion-project/SKILL.md) · [团队主页布局](../skills/_shared/notion-project.md) |
| `to-notion` | 沿用 `to-spec` 综合已有决定的动作，按团队实际产物区分软件方案、研究计划和结果记录。把写草案、更新指定原页的完成条件分别写清。 | 用户要求把仿真结果补进指定页面。检查正文是否保留实验条件和实机验证缺口，能否提供原页更新的证据。[现行入口](../skills/to-notion/SKILL.md) |
| `simplify` | 用上游删除测试追问每项关键删减的代价落在何处。保留团队允许「方案已足够简单」的出口，以及改变目标或证据强度时由人取舍的步骤。 | 提议删除对照组以缩短实验。观察是否说明删前、删后分别还能回答什么问题，再请人决定取舍。[现行入口](../skills/simplify/SKILL.md) |
| `to-pm` | 沿用 `to-tickets` 的可验收成果与阻塞判据。入口先选首次拆解、方案调整、进展回写或阶段复盘，各分支只读取完成本次动作需要的页面、关联与证据。 | 设备未到，但分析工作可开工。再提供「某个 ticket 已完成」的反馈，检验 Agent 是否记录局部等待和已完成步骤，仍能指出整个 Issue 缺的验收证据。[现行入口](../skills/to-pm/SKILL.md) |
| `project-docs` | 这项来自团队的正式材料方法。可借鉴 `prototype` 的条件式引用，用交付格式选择制作能力，以读者实际拿到的文件判断完成，并沿用已有文件检查说明。 | 用户同时要技术方案与预算，最后修改一项设备数量。检查两份文件口径、总额、渲染结果，交付可打开的路径并说明未核验的部分。[现行入口](../skills/project-docs/SKILL.md) · [交付检查](../skills/project-docs/references/delivery-check.md) |

## 第一项讨论稿 · 建立或补齐 Notion 项目主页

建议给使用者的描述是「为新项目建立 Notion 主页，或补齐已有主页的缺项，返回项目主页链接。」新项目里，Issues 和里程碑先各留一个位置，团队开始安排执行时由 `to-pm` 建库。已有项目里，如果四个区域齐备、只是在主页上的排列与示例不同，回读并返回原主页就满足初始化的完成条件。可以用这一场景检验修订后的技能能否尊重团队已有的人工布局。[初始化原设计](custom-skill-design.md#init-notion-project建立项目框架) · [现行主页约定](../skills/_shared/notion-project.md)

**2026-11-07 已确定父页选择顺序。** 用户指定父页时直接使用。用户未指定时读取当前业务项目的约定，两者都没有再询问。本团队采用「项目总览」作为自己的父页名称。[修订后的定位规则](../skills/init-notion-project/SKILL.md#1-定位项目)
