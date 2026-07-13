---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 44 条内容中筛选出 9 条重要资讯。

---

1. [Grok CLI 被曝静默上传整个代码库及 API 密钥至 xAI 云存储](#item-1) ⭐️ 9.05/10
2. [George Hotz：LLM 有价值，但前沿实验室的估值被高估了](#item-2) ⭐️ 8.0/10
3. [Anthropic 负责人分享 Agent 基础设施演进洞察](#item-3) ⭐️ 8.0/10
4. [纳德拉提出](#item-4) ⭐️ 7.88/10
5. [Ploy 将生产级 AI Agent 迁移至 GPT-5.6：速度提升 2.2 倍，成本降低 27%](#item-5) ⭐️ 7.3/10
6. [腾讯混元发布 Hy3 模型：295B 参数 MoE 架构，面向 Agent 的 LLM 定位，已集成微信服务超 10 亿用户](#item-6) ⭐️ 7.12/10
7. [Mindwalk：在代码库 3D 地图上回放编码代理会话](#item-7) ⭐️ 7.1/10
8. [Claude Code 在读取提示前发送 33k tokens，OpenCode 仅 7k](#item-8) ⭐️ 7.0/10
9. [JetBrains 实测：号称省 65% Token 的 Caveman 技能在真实智能体场景仅省 8.5%](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Grok CLI 被曝静默上传整个代码库及 API 密钥至 xAI 云存储](https://x.com/Khazix0918/status/2076504273282908170) ⭐️ 9.05/10

安全研究者发现 xAI 官方 Grok CLI（npm 包 @xai-official/grok v0.2.93）会通过旁路通道 POST /v1/storage 将整个项目目录打包为 tar.gz 静默上传至 xAI 的 Google Cloud Storage 存储桶（grok-code-session-traces），即使模型仅回复一个单词且未调用任何文件工具，上传仍然发生。该工具还跨项目扫描并上传包含 API 密钥的 Claude Code 配置文件（~/.claude.json、settings.local.json），并以明文传输 .env 文件；7 月 13 日 xAI 通过服务端远程开关关闭了上传功能，但代码管线仍保留。 这是一起重大安全事件：一家头部 AI 公司的开发者工具在未经同意的情况下窃取整个代码库和凭证，对任何安装了 Grok CLI 的开发者构成直接威胁。xAI 通过远程开关而非代码更新来关闭该功能，同时保留上传管线的做法，暗示数据收集是有意为之且随时可能被重新启用，从根本上动摇了开发者对 AI 编程工具的信任。 网络流量分析显示，在 12 GB 仓库测试中，/v1/storage 端点传输了 5.10 GiB 数据，而模型对话通道仅传输 192 KB，比例约为 27,800:1。关闭

aihot · X：卡兹克 (@Khazix0918) · 7月13日 03:09 · [中文阅读](https://aihot.virxact.com/items/cmrinwb3900yebilkxv3esdnc) · 3 个来源

**核验**: 多源印证

**背景**: Grok CLI 是 xAI 的官方命令行编程代理（npm 包 @xai-official/grok），目前由 Grok 4.5 驱动，旨在与 Anthropic 的 Claude Code 等 AI 辅助编程工具竞争。Claude Code 将配置和凭证存储在 ~/.claude.json 和 settings.local.json 等文件中，这些文件可能包含 Anthropic 服务的 API 密钥。Grok CLI 上传时使用的 git bundle 格式是 Git 的标准机制，可将引用和 Git 对象打包到单个文件中，实际上捕获了整个仓库的完整历史。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://git-scm.com/docs/bundle-format">Git - bundle-format Documentation</a></li>

</ul>
</details>

**社区讨论**: 安全研究者 @Khazix0918 的原始帖子引发了广泛关注，社区将其与此前 Anthropic 在 Claude Code 中植入隐形代码识别中国用户的事件相提并论。社区情绪普遍为震惊和被背叛感，用户呼吁立即卸载 Grok CLI，并担忧主流 AI 厂商的编程工具无法被信任来处理敏感代码库和凭证。

**标签**: `#AI安全`, `#Grok CLI`, `#API密钥泄露`, `#AI开发者工具`, `#数据隐私`

---

<a id="item-2"></a>
## [George Hotz：LLM 有价值，但前沿实验室的估值被高估了](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.0/10

George Hotz 发布了一篇博客文章，认为虽然 LLM 确实创造了巨大价值，但前沿 AI 实验室（如 OpenAI、Anthropic 等）无法按比例捕获这些价值，因此它们的高估值从根本上存在偏差。他的核心论点是价值创造不等于价值捕获——这一区别解释了为什么实验室在技术真正有用的同时仍在积极推动按 token 计费的订阅模式。 这一观点挑战了前沿实验室估值由 AI 变革性潜力所支撑的主流叙事，暗示经济收益将广泛扩散而非集中于模型提供商。这一讨论对 AI 投资者、开源可持续性以及理解 LLM 生产力提升究竟在哪里体现具有重要意义。 Hotz 的论点基于价值创造（做大经济收益的蛋糕）与价值捕获（为自己切取最大一块）之间的经济学区别，指出历史上创造巨大价值的先驱者往往无法捕获太多价值。社区评论者强调，生产力提升主要表现为针对高度特定个人用例构建的私有一次性软件，而非公开发布的产品，并担忧随着随意 fork 项目成为常态，开源的可持续性面临挑战。

hackernews · therepanic · 7月12日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48883343)

**核验**: 多源印证

**背景**: 价值创造与价值捕获是经济学中的基础概念：价值创造指产品或服务提供的总感知收益，而价值捕获是提供者能够变现的那部分收益。前沿 AI 实验室如 OpenAI、Anthropic、Meta 和 Google DeepMind 是开发最先进 AI 模型的主要组织，它们基于 AI 将带来变革性影响的预期获得了巨额估值。George Hotz 是 comma.ai 的创始人，也是知名黑客和工程师，以其独立且常常反主流的技术观点而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://intelligence.org/2025/06/11/so-you-want-to-work-at-a-frontier-ai-lab/">So You Want to Work at a Frontier AI Lab - Machine Intelligence Research Institute</a></li>
<li><a href="https://farrellymitchell.com/value-creation-implementation/value-creation-vs-value-capture/">Value creation vs value capture | Farrelly Mitchell</a></li>
<li><a href="https://www.linkedin.com/pulse/20121112204533-16553-value-creation-vs-value-capture-musings-on-the-new-economy">Value Creation vs . Value Capture : Musings on the New Economy</a></li>

</ul>
</details>

**社区讨论**: 讨论中强烈认同 Hotz 关于价值创造与价值捕获的框架，评论者指出在当前订阅价格下前沿模型物超所值，但仍无法支撑万亿级估值。多位评论者观察到生产力提升是真实的，但主要体现在私人层面——用户为个人用例构建一次性软件而非发布公开项目——这引发了对 fork 变得轻而易举的时代开源可持续性的担忧。也有评论者持不同意见，认为 Sonnet 4 和 Opus 4.5 等近期模型发布代表了真正的阶跃式进步，正在加速时间线，可能会让怀疑者感到意外。

**标签**: `#LLM`, `#AI行业判断`, `#开源AI`, `#AI生产力`, `#frontier labs`

---

<a id="item-3"></a>
## [Anthropic 负责人分享 Agent 基础设施演进洞察](https://x.com/dotey/status/2076174130135674907) ⭐️ 8.0/10

7 月 10 日，Anthropic 发布了一场对谈，Claude 平台工程负责人 Katelyn Lesse、产品负责人 Angela Jiang 和产品经理 Jess Yann 分享了来自一线的 Agent 基础设施观察。核心洞察包括编排层（harness）正在变薄、多 Agent 协作模式兴起，以及从个人生产力出发务实衡量 ROI 的方法。 这些洞察直接来自构建最广泛使用的 Agent 平台之一的 Anthropic 领导层，使其成为 Agent 基础设施发展方向的可信风向标。从逐步控制转向多 Agent 协作设计，加上自下而上的企业采纳策略，为开发者和企业推进 AI 转型提供了可操作的指导。 讨论强调，随着模型推理和工具调用能力增强，开发者不再需要规定每一步，只需给出目标和边界，让模型自行决定执行路径。Angela Jiang 特别提醒，虽然 Agent 能放大个人能力，但不会自动解决团队的协调、取舍和决策问题——当每个人都能快速做出原型并独立上线时，容易出现产品无序扩张的风险。

twitter · 宝玉 · 7月12日 05:17

**核验**: 多源印证

**背景**: Agent harness 是围绕大语言模型的控制层，负责指导模型执行任务，包括管理工具调用、反馈循环和项目完成决策。随着 LLM 在推理和工具使用方面的能力提升，这些编排层过去需要大量流程控制代码来处理分支、条件判断和错误恢复。多 Agent 编排是一种较新的范式，多个 Agent 之间相互协作——提方案、挑错或升级求助——而非遵循单一刚性流水线。讨论中提到的 Shopify River 系统是一个端到端 Agent 工作流的典型案例，将需求文档、开发环境、代码实现和 QA 测试串联成统一流水线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>
<li><a href="https://shopify.engineering/under-the-river">Under the River (2026) - Shopify</a></li>

</ul>
</details>

**社区讨论**: 该帖子获得了 357 个点赞和 39 条回复，显示出社区对 Agent 基础设施趋势的强烈关注。讨论引起了正在经历从刚性编排向灵活多 Agent 协作模式转变的开发者和从业者的共鸣，也吸引了寻求务实 AI 采纳策略的企业关注。

**标签**: `#AI Agents`, `#Anthropic`, `#Agent Infrastructure`, `#AI Developer Tools`, `#Enterprise AI`

---

<a id="item-4"></a>
## [纳德拉提出](https://x.com/satyanadella/status/2076323181154230284) ⭐️ 7.88/10

微软 CEO 萨提亚·纳德拉提出了 这一概念为企业 AI 采用提出了一个根本性的战略挑战：使用 AI 工具的行为本身可能通过向模型提供商泄露专有知识来削弱企业的竞争优势。随着 AI 深入核心业务流程，保护组织学习循环和维持数据主权的能力将决定企业是从 AI 中获益，还是在无意中交出自己的智力资本。 纳德拉明确指出企业需要对私有评估、组织记忆所有权和适配权重拥有控制权，未经同意数据不得外泄至信任边界之外。他还主张企业应有权使用模型输出来微调或训练自有模型，实质上是要求企业掌控自身的学习循环，而非将其反馈给提供商的模型。

aihot · X：Satya Nadella (@satyanadella) · 7月12日 15:09 · [中文阅读](https://aihot.virxact.com/items/cmrhyer8a01q3biidlr8xr6rm)

**核验**: 多源印证

**背景**: 诺贝尔经济学奖得主肯尼斯·阿罗曾描述了经典的

<details><summary>参考链接</summary>
<ul>
<li><a href="https://snscratchpad.com/posts/reverse-information-paradox/">The Reverse Information Paradox | sn scratchpad</a></li>
<li><a href="https://digg.com/tech/u4a9rpdr">Microsoft CEO Satya Nadella describes AI reverse information ...</a></li>
<li><a href="https://www.startuphub.ai/ai-news/technology/2026/the-ai-reverse-information-paradox">The AI ' Reverse Information Paradox ' | StartupHub.ai</a></li>

</ul>
</details>

**标签**: `#AI治理`, `#数据隐私`, `#企业AI策略`, `#反向信息悖论`, `#行业判断`

---

<a id="item-5"></a>
## [Ploy 将生产级 AI Agent 迁移至 GPT-5.6：速度提升 2.2 倍，成本降低 27%](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6) ⭐️ 7.3/10

Ploy 是一家用 AI Agent 构建和编辑营销网站的公司，他们将其生产级 Agent 从 Anthropic 的 Opus（4.7/4.8）迁移至 GPT-5.6 Sol 作为默认模型，报告构建速度提升 2.2 倍、成本降低 27%，且完成质量达到或超过原有模型。Opus 此前占据默认位置达四个月之久。 这为 GPT-5.6 在涉及规划、代码生成、图像生成和自我评估的复杂 Agent 工作流中的表现提供了具体的真实生产数据，对评估前沿模型迁移的开发者具有直接参考价值。结果表明 GPT-5.6 可能在速度、成本和质量方面提供了极具竞争力的组合，可能改变生产级 AI Agent 的竞争格局。 该 Agent 的工作负载要求极高：它需要规划页面、阅读代码库、编写组件、生成图像、截取自己的工作截图，并自行判断何时完成。社区成员 thiagoperes 独立验证了类似结果——从 GPT-5.4 nano/mini 迁移到 5.6 后，在多种简单工作流中均观察到类似幅度的改善，并指出对许多公司而言，模型升级本质上只是一行代码的改动，即使已拥有复杂的模型路由架构也是如此。

hackernews · brryant · 7月12日 17:13 · [社区讨论](https://news.ycombinator.com/item?id=48882716) · [中文阅读](https://aihot.virxact.com/items/cmrig9mkx0024bijp9pr04hss) · 2 个来源

**核验**: 已核对原文

**背景**: 执行复杂多步骤任务的生产级 AI Agent 需要能够在单一工作流中处理规划、代码生成、视觉生成和自我评估的模型。像 Ploy 这样的公司会持续将前沿模型发布版本与生产工作负载进行基准测试，以找到速度、成本和输出质量的最佳平衡。模型路由架构可以将不同子任务分配给不同的专用模型，但正如本次迁移所示，一个强大的单一模型有时能在简化运营的同时仍提供更优的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6">Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper</a></li>
<li><a href="https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6">Ploy 将 AI 智能体默认模型从 Claude Opus 4.8 切换至 GPT-5.6 Sol</a></li>

</ul>
</details>

**社区讨论**: thiagoperes 独立验证了性能改善，报告从 GPT-5.4 nano/mini 迁移到 5.6 后在多种工作流中获得了类似提升，并认为模型升级通常只是简单的一行代码改动，即使拥有复杂的路由架构也是如此。kristianp 批评了文章的 LLM 生成写作风格，希望指导 LLM 的人能重写最糟糕的部分。bob1029 建议采用混合方案——用 Luna 处理涉及工具的工作负载，用 Sol 负责人机交互和编排，而 arikrahman 则指出在非补贴的美国提供商上，Deepseek 配合缓存命中可以让请求几乎免费。

**标签**: `#AI agents`, `#GPT-5.6`, `#model migration`, `#production AI`, `#cost optimization`

---

<a id="item-6"></a>
## [腾讯混元发布 Hy3 模型：295B 参数 MoE 架构，面向 Agent 的 LLM 定位，已集成微信服务超 10 亿用户](https://x.com/AYi_AInotes/status/2076341952023310580) ⭐️ 7.12/10

腾讯混元团队发布了拥有 295B 参数的 MoE 模型 Hy3，该模型定位为面向 Agent 的大语言模型。目前它已集成至服务超 10 亿用户的微信服务中，在任务成功率和推理效率上均有显著提升。

aihot · X：阿易 AI Notes (@AYi_AInotes) · 7月12日 16:24 · [中文阅读](https://aihot.virxact.com/items/cmri0lo1e00irbixecx7cj2f5)

**核验**: 已核对原文

**标签**: `#AI Agents`, `#MoE架构`, `#腾讯混元`, `#LLM`, `#AI产品发布`

---

<a id="item-7"></a>
## [Mindwalk：在代码库 3D 地图上回放编码代理会话](https://github.com/cosmtrek/mindwalk) ⭐️ 7.1/10

Mindwalk 是一款新发布的开源 Go 工具，可在代码库的 3D 地图上回放 Claude Code 和 Codex 代理会话，用颜色标记代理搜索、读取或编辑过的文件。它以单个 Go 二进制文件运行，所有会话数据完全在本地处理，并包含显示错误率、文件修改量等摩擦信号面板，以及上下文压缩和子代理启动等时间轴标记。 随着 Claude Code 和 Codex 等 AI 编码代理成为主流，开发者需要审计和理解这些代理如何导航复杂代码库的方法——这正是 Mindwalk 直接解决的盲点。通过让代理行为可视化透明，它帮助开发者发现低效环节、调试失败会话，并建立对 AI 辅助开发工作流的信任。 该工具提供树状图和地形图两种视图模式，文件触达状态分为未访问、已查看、已读取、已编辑四种颜色标记。播放控制包含键盘快捷键，可调节速度并跳转到编辑点或错误点，摩擦信号面板则展示错误率和文件修改量等指标，同时时间轴上标记了上下文压缩事件和子代理激活等节点。

aihot · Hacker News 热门（buzzing.cc 中文翻译） · 7月12日 13:51 · [中文阅读](https://aihot.virxact.com/items/cmrhvwe6k00y7biidjabepmem)

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 的代理式编码工具，通过 CLI 或桌面应用运行，能够理解代码库、编辑文件并执行命令。Codex 是 OpenAI 的竞争性 AI 编码代理，集成在 ChatGPT 中，用于处理拉取请求、代码重构和代码审查等并行工作流。两类代理都会自主导航大型代码库，进行搜索、读取和编辑文件，但其决策过程往往不透明——上下文压缩机制使这一问题更加复杂，代理会摘要或丢弃早期对话上下文以保持在 token 限制内，可能丢失重要信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software Engineering | OpenAI</a></li>
<li><a href="https://www.anthropic.com/research/claude-code-expertise">How Claude Code is used in practice \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Claude Code`, `#Codex`, `#可视化工具`, `#开源 AI 工具`

---

<a id="item-8"></a>
## [Claude Code 在读取提示前发送 33k tokens，OpenCode 仅 7k](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 7.0/10

Systima.ai 的一项对比研究发现，Claude Code 在处理用户提示前会发送约 33,000 个 tokens，而 OpenCode 仅发送 7,000 个 tokens。该研究通过在编程代理工具与 Anthropic API 端点之间添加日志记录来捕获所有请求，明确显示 Claude Code 在缓存策略和框架 token 使用方面远不如 OpenCode 高效。 这一 token 开销直接影响开发者成本，尤其是对按 token 付费的 API 用户而言，同时也引发了关于 AI 编程代理厂商是否有动机增加 token 使用量的疑问。随着代理式编程工具成为主流开发基础设施，效率已成为工具选择中的关键因素。 研究人员在编程代理工具与 Anthropic 端点之间添加了日志记录，以捕获所有请求和返回的使用量数据。在社区反馈质疑 token 开销是否是正确的衡量指标后，作者承诺将更新研究，加入更深入的任务分析、定性结果对比以及可复现的输入输出。

hackernews · systima · 7月12日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**背景**: Claude Code 是 Anthropic 的代理式编程工具，运行在终端中，帮助开发者编辑文件、运行命令并加速代码交付。OpenCode 是一个基于 Go 语言的开源 CLI 替代方案，提供终端用户界面以与各种 AI 模型交互，常被定位为 Claude Code 的免费替代品。Token 开销是指每次 API 请求中在处理实际用户提示之前发送的系统提示、工具定义和其他元数据所消耗的 tokens，这些 tokens 需要用户付费。两种工具都充当

**标签**: `#Claude Code`, `#token efficiency`, `#AI coding agents`, `#developer tools`, `#cost optimization`

---

<a id="item-9"></a>
## [JetBrains 实测：号称省 65% Token 的 Caveman 技能在真实智能体场景仅省 8.5%](https://x.com/dotey/status/2076371173244588135) ⭐️ 7.0/10

JetBrains 使用 Claude Code 在 SkillsBench 上跑了 86 个真实编程任务，分别测试装与不装 Caveman 技能，共进行约 240 次计费实验，花费 106 美元。结果显示，Caveman 在智能体场景中仅省了 8.5% 的输出 Token，远低于其宣称的 65%，因为工具调用、系统提示词和 MCP 等才是 Token 消耗的大头，而非聊天输出。 这暴露了 AI 开发者社区对智能体工作流中 Token 成本来源的一个根本性误解——优化输出冗余度对总账单几乎只是杯水车薪。真正想省钱的开发者应关注上下文管理、减少不必要的 MCP 和 Skills 加载，以及用更聪明的模型减少返工，而不是压缩输出语言。 65% 的数字来自聊天场景，AI 会生成大段文字，但在智能体工作流中，输出 Token 仅占总消耗的一小部分。Caveman 技能本身每轮还会增加约 1–1.5k 输入 Token，而且过于简短的输出会导致开发者追问，触发额外的工具调用，把省下的 Token 又吃回去。即便是 8.5% 这个数字也是天花板，因为测试中强制每次回复都生效，日常使用中触发频率只会更低。

twitter · 宝玉 · 7月12日 18:20

**核验**: 多源印证

**背景**: Caveman 项目由荷兰莱顿大学 19 岁的大一新生 Julius Brussee 创建，它在 Claude Code、Codex 等 AI 编程工具的提示词中加入一段指令，让 AI 像原始人一样说话——删除冠词、客套和连接词，只保留技术要素。SkillsBench 是一个基准测试平台，通过在装与不装相关技能的情况下分别运行模型来评估编程智能体在独立编程任务上的表现。MCP（Model Context Protocol）是 Anthropic 于 2024 年 11 月推出的开放标准，用于连接 AI 系统与外部工具和数据源，是智能体工作流中 Token 消耗的主要来源之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/JuliusBrussee/caveman/blob/main/README.md">caveman /README.md at main · JuliusBrussee/ caveman · GitHub</a></li>
<li><a href="https://www.skillsbench.ai/">SkillsBench — Benchmarking How Well Agent Skills Work</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 该帖子产生了约 20 条回复，说明有一定讨论度。整体 sentiment 与作者的分析一致——认为 Caveman 这类省 Token 技巧是过渡期产物，随着模型单价下降和提示词缓存将重复上下文成本降低约九成，这类优化的意义会越来越小。评论者普遍认同，啰嗦的输出本质上是通信协议中自带的纠错码，而且编程智能体与开发者之间的共享背景远不如人际电报场景可靠。

**标签**: `#AI智能体`, `#Token优化`, `#Claude Code`, `#实证测试`, `#AI开发工具`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="13"><span>其他追踪推文</span><span class="archive-tab-count">13</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="4"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">4</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2076478706462367832">@op7418: 在 Anthropic 重置和延长 Fable5 使用时间之后 OpenAI 直接取消了 Codex 的五小时使用限制，同时进行了新一次的重置</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月13日 01:27 UTC · 喜欢 14 · 转发 0 · 回复 11 · 浏览 10132</p>
<p class="archive-item-content">在 Anthropic 重置和延长 Fable5 使用时间之后<br>
<br>
OpenAI 直接取消了 Codex 的五小时使用限制，同时进行了新一次的重置</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2076372677577576864">@dotey: 给 Codex 点赞👍 暂时移除 5 小时使用限制，GPT 5.6 Sol 更省 token，下一小时内进行使用量重置</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月12日 18:26 UTC · 喜欢 174 · 转发 3 · 回复 40 · 浏览 42865</p>
<p class="archive-item-content">给 Codex 点赞👍<br>
暂时移除 5 小时使用限制，GPT 5.6 Sol 更省 token，下一小时内进行使用量重置</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2076365965915467978">@thsottiaux: Morning. The last 48 hours of Codex and ChatGPT Work have been intense! Three important updat...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.3 out of 10">6.3</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月12日 17:59 UTC · 喜欢 21829 · 转发 1723 · 回复 2545 · 浏览 2708372</p>
<p class="archive-item-content">Morning. The last 48 hours of Codex and ChatGPT Work have been intense! Three important updates:<br>
<br>
- Temporarily removing the 5 hour usage limit restriction for all Plus, Business and Pro plans<br>
- Rolling out changes that will make GPT 5.6 Sol more efficient across the board and that will be reflected in less usage being used so that it can take you further. Exact impact to be quantified and shared<br>
- We hit 6M active users, and are landing a usage reset in the next hour<br>
<br>
Go do things<br>
<br>
--- From aihot ---<br>
早上好。过去 48 小时里，Codex 和 ChatGPT Work 非常忙碌！三项重要更新：<br>
<br>
- 暂时取消所有 Plus、Business 和 Pro 计划的 5 小时使用限制<br>
- 正在推出变更，使 GPT 5.6 Sol 整体更高效，这将体现在使用量减少上，从而让你能走得更远。具体影响待量化后公布<br>
- 我们已达到 600 万活跃用户，并将在接下来一小时内进行使用量重置<br>
<br>
去创造吧。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2076365965915467978">@thsottiaux: Morning. The last 48 hours of Codex and ChatGPT Work have been intense! Three important updat...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月12日 17:59 UTC · 喜欢 21824 · 转发 1722 · 回复 2545 · 浏览 2708372</p>
<p class="archive-item-content">Morning. The last 48 hours of Codex and ChatGPT Work have been intense! Three important updates:<br>
<br>
- Temporarily removing the 5 hour usage limit restriction for all Plus, Business and Pro plans<br>
- Rolling out changes that will make GPT 5.6 Sol more efficient across the board and that will be reflected in less usage being used so that it can take you further. Exact impact to be quantified and shared<br>
- We hit 6M active users, and are landing a usage reset in the next hour<br>
<br>
Go do things</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2076355165645361559">@dotey: Claude 延长了 Claude Fable 5 的访问到 7/19！ 从来没见过这么傻逼的公司，跟儿戏一样！</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月12日 17:17 UTC · 喜欢 472 · 转发 7 · 回复 101 · 浏览 99677</p>
<p class="archive-item-content">Claude 延长了 Claude Fable 5 的访问到 7/19！<br>
<br>
从来没见过这么傻逼的公司，跟儿戏一样！</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2076352559263207806">@op7418: 哈哈 果然延长了，Fable 5 的计划延长一周到 7 月 19 号 https://t.co/pzdlnWHJGw</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月12日 17:06 UTC · 喜欢 17 · 转发 1 · 回复 11 · 浏览 11313</p>
<p class="archive-item-content">哈哈 果然延长了，Fable 5 的计划延长一周到 7 月 19 号 https://t.co/pzdlnWHJGw</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/claudeai/status/2076351399999557669">@claudeai: We&#x27;re extending Claude Fable 5 access on all paid plans, as well as keeping Claude Code’s wee...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月12日 17:02 UTC · 喜欢 62670 · 转发 6390 · 回复 5594 · 浏览 13764507</p>
<p class="archive-item-content">We&#x27;re extending Claude Fable 5 access on all paid plans, as well as keeping Claude Code’s weekly rate limits 50% higher, through July 19.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2076335432321929585">@op7418: 今天是 Fable 5 在 Claude 套餐的最后一天了，还没用完的使劲蹬啊</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月12日 15:58 UTC · 喜欢 33 · 转发 0 · 回复 44 · 浏览 33009</p>
<p class="archive-item-content">今天是 Fable 5 在 Claude 套餐的最后一天了，还没用完的使劲蹬啊</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2076326449955602659">@op7418: 哈哈 这个 GPT 的模型选择器交互可以的，比现在 OpenAI 官方的直观</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月12日 15:22 UTC · 喜欢 20 · 转发 1 · 回复 10 · 浏览 12185</p>
<p class="archive-item-content">哈哈 这个 GPT 的模型选择器交互可以的，比现在 OpenAI 官方的直观</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/Tz_2022/status/2076301177994559794">@Tz_2022: 我这里再放一个暴论： 当前所有以节约 token 为目标的各种 skill / harness，都是阶段性产物，很快就会扫入历史的垃圾堆。。。 这就是短消息按字数收费的那个时代，在钻研怎...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月12日 13:42 UTC · 喜欢 396 · 转发 13 · 回复 46 · 浏览 58490</p>
<p class="archive-item-content">我这里再放一个暴论：<br>
<br>
当前所有以节约 token 为目标的各种 skill / harness，都是阶段性产物，很快就会扫入历史的垃圾堆。。。<br>
<br>
这就是短消息按字数收费的那个时代，在钻研怎么发尽可能少字数的短信把事说清楚的那些奇技淫巧。。。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/maria_rcks/status/2076176709221552447">@maria_rcks: I solved the model picker problem, no need to thank me Tibo https://t.co/e7youjMILD</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月12日 05:27 UTC · 喜欢 9529 · 转发 313 · 回复 365 · 浏览 1251113</p>
<p class="archive-item-content">I solved the model picker problem, no need to thank me Tibo https://t.co/e7youjMILD</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/Arcadia_Bao/status/2076158266145669517">@Arcadia_Bao: 有人可能会说。我不管这种文字是不是套路，我只要保证外在形式不犯错就行。我就是借一下 AI 文案的壳，里面装上高价值的信息和内容，不就够了吗？ 道理是这个道理没错。但你权衡利弊时还需要考虑 2 个...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月12日 04:14 UTC · 喜欢 16 · 转发 2 · 回复 3 · 浏览 6494</p>
<p class="archive-item-content">有人可能会说。我不管这种文字是不是套路，我只要保证外在形式不犯错就行。我就是借一下 AI 文案的壳，里面装上高价值的信息和内容，不就够了吗？<br>
道理是这个道理没错。但你权衡利弊时还需要考虑 2 个巨大的盲点<br>
1、你的内容真的有高价值吗？写真正过硬的内容其实比单纯写好文案要难得多。<br>
2、在你的内容真的很好的时候，放弃个性化的表达，你未来失去的好处，可能远远重于眼前的一点便利。<br>
这就还是我说的老问题。当你有好东西的时候，装在平庸、可能随时过时的 AI 文壳子里，是一种暴殄天物，是一种自毁。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/Arcadia_Bao/status/2076153508689248425">@Arcadia_Bao: 文字这种东西，当 LLM 能够稳定产出「看似没有 AI 味道」的作品的的时候，说明你选取的那个写作赛道，本身就具有非常严重的模版化倾向。 比方说营销号自媒体，比如口播稿。 一个模版框架里，正好塞...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月12日 03:55 UTC · 喜欢 8 · 转发 1 · 回复 1 · 浏览 7258</p>
<p class="archive-item-content">文字这种东西，当 LLM 能够稳定产出「看似没有 AI 味道」的作品的的时候，说明你选取的那个写作赛道，本身就具有非常严重的模版化倾向。<br>
比方说营销号自媒体，比如口播稿。<br>
一个模版框架里，正好塞进了严丝合缝的新模板。因为本身对高度八股文就有容忍度。所以看似也问题不大。仅此而已。<br>
但要明确一点，对模板有容忍度不代表容忍度是无限。赛道容忍八股文模板，也不代表你发八股文模板就是好。更不代表这种趋同的写作方式，能给你带来任何额外的好处。<br>
因为，你说到底就只是做到了「和大部分人差不多」而已。<br>
而且，这种现在看上去 OK 的「无 AI 味写作」，也都逃不脱最终沦为「AI 味道」的宿命。<br>
好比说前一段时间 GPT 和 Claude 的某些调教的比较过头的版本严重偏好短句。出现这种情况的原因，我推测，有一部分是针对前两年的老模型喜欢写固定套路的长句、容易出现 AI 八股文的矫枉过正。<br>
因为以短句替代长句作为段落，超短句写诗一样排列，就能够很容易去掉所有易被识别的短语搭配和长句模版。<br>
从训练的结果上，这显然是更加讨喜的。<br>
废话，句子都被打散成原子了。 ABCDEFG 被打散成 A B D G K 一个一个单字母蹦了，还能找出什么固定模式？<br>
但是阅读体验也彻底拉完了。<br>
因为彻底去模版化本身也是一种最严重的模版。这种狗屎短句很快就就把所有人整疯了。<br>
现在的所谓 GPT-5.6 写作自然也是如此。说白了都是为了某种场景某种特定姿态，凹姿势凹出来的，一旦要做变化，一旦脱离具体的模版情境，比如进行风格化改写，推广到更多的场景，一样会原形毕露。</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2076155833428431012">Swyx: if you only learned about jevons paradox primarily wrt software demand in the age of agentic...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Swyx · 7月12日 04:04 UTC · 喜欢 143 · 转发 9 · 回复 28</p>
<p class="archive-item-content">Swyx argues that as coding agents make knowledge work more efficient, demand for work will increase rather than decrease, and what&#x27;s happening in coding is just the beginning of a broader trend across all knowledge work.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2076151956440261008">Guillermo Rauch: Easy money (Swiss francs)</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 7月12日 03:49 UTC · 喜欢 298 · 转发 6 · 回复 26</p>
<p class="archive-item-content">Guillermo Rauch posts a cryptic tweet about &#x27;easy money (Swiss francs)&#x27; with no technical context or substance.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2076151105080447404">Peter Yang: The score is 3 vs 1 but imo this was a very mixed performance from Argentina. Not sure how th...</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月12日 03:46 UTC · 喜欢 31 · 转发 0 · 回复 17</p>
<p class="archive-item-content">A tweet commenting on Argentina&#x27;s mixed performance in a sports match despite a 3-1 scoreline.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2076150076087611433">Nikunj Kothari: Argentina has the mandate of heaven.. what a strike by Alvarez. England vs. Argentina France...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 7月12日 03:42 UTC · 喜欢 23 · 转发 1 · 回复 6</p>
<p class="archive-item-content">A social media post commenting on football matches involving Argentina, England, France, and Spain.</p>
</article>
</div>
</section>
