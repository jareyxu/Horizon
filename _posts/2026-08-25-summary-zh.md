---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 40 条内容中筛选出 11 条重要资讯。

---

1. [让可执行文件同时成为 SQLite 数据库](#item-1) ⭐️ 8.3/10
2. [seL4 在 AArch64 上完成安全证明](#item-2) ⭐️ 8.0/10
3. [依赖 AI 编程或致编码专业能力崩塌，引发开发者热议](#item-3) ⭐️ 8.0/10
4. [Grok Bot 0.18.0 源码映射泄露，原始代码被完整还原](#item-4) ⭐️ 8.0/10
5. [AI Agent 让布鲁克斯的“外科手术团队”模式重新可行](#item-5) ⭐️ 8.0/10
6. [MetaRoCE：为 AI 规模以太网打造的全新 RDMA 传输协议](#item-6) ⭐️ 7.55/10
7. [GPT-5.6 登陆 Kiro，开发成本降低约 82%](#item-7) ⭐️ 7.47/10
8. [MS Paint 与 Photos 为本地生成的 AI 图片静默嵌入 GUID 水印](#item-8) ⭐️ 7.0/10
9. [Pi 贡献者澄清：网传「官方方案」实为社区 PR 误传](#item-9) ⭐️ 7.0/10
10. [评估构建的金发姑娘原则：衡量中间阶段](#item-10) ⭐️ 7.0/10
11. [Garry Tan 预测：记录系统须成为 AI 控制层，否则将被智能体取代](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [让可执行文件同时成为 SQLite 数据库](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database) ⭐️ 8.3/10

fzakaria.com 上的一篇技术文章提出了一个概念：让 ELF 可执行文件同时充当 SQLite 数据库，利用 SQLite 的虚拟表机制和 ELF 格式灵活的节（section）布局来实现。 这一想法可能催生出自描述的可执行文件，开发者可以用 SQL 查询其内部结构，从而简化调试、检查和打包流程。有评论者认为，它甚至可能以更高效的格式取代 AppImage。 ELF 格式非常紧凑且没有自描述模式，修改时通常需要将原有节清零并添加新节。SQLite 的虚拟表机制是关键使能技术，它让 SQLite 能够访问数据库文件之外的资源。

hackernews · setheron · 8月24日 04:48 · [社区讨论](https://news.ycombinator.com/item?id=49415271) · 2 个来源

**核验**: 多源印证

**背景**: ELF（Executable and Linkable Format，可执行与可链接格式）是 Linux 及其他类 Unix 系统上可执行文件和共享库的标准二进制格式，其设计具有灵活、可扩展和跨平台的特点。SQLite 虚拟表是注册到打开的数据库连接上的对象，在 SQL 语句看来与普通表或视图无异，从而让 SQL 可以查询文件系统等外部资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sqlite.org/vtab.html">The Virtual Table Mechanism Of SQLite</a></li>
<li><a href="https://en.wikipedia.org/wiki/ELF_file_format">ELF file format</a></li>
<li><a href="https://www.chiark.greenend.org.uk/doc/sqlite3/vtablist.html">List Of Virtual Tables</a></li>

</ul>
</details>

**社区讨论**: 评论整体非常热情：有读者称虚拟表机制“令人震撼”且极其有用，还有人认为这种方法可以取代大多数 AppImage 的使用场景。作者提到，这个想法在学术圈得到的反馈并不那么友好。也有评论者指出，从广义上讲 ELF 本身就已经是一种数据库。

**标签**: `#SQLite`, `#ELF`, `#executable`, `#virtual tables`, `#developer tools`

---

<a id="item-2"></a>
## [seL4 在 AArch64 上完成安全证明](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

Proofcraft 于 2026 年 8 月 21 日宣布，seL4 在 AArch64 上的机密性（confidentiality）证明现已完成，此前已完成功能正确性和完整性证明。在 NCSC 的持续支持下，这完成了 seL4 实现在 AArch64 上强制安全隔离的正式数学证明。 这是 seL4 的一个重要形式化验证里程碑：seL4 是少数拥有机器检查安全证明的操作系统内核之一，而这一成果将此类保证扩展到了广泛使用的 64 位 ARM 架构。它增强了 seL4 在安全关键和任务关键系统中使用的理由，因为应用之间的隔离可以防止攻击扩散。 该证明目前覆盖非 MCS（非混合关键性）配置和单核（unicore）系统，并在 Proofcraft 所列假设下有效。机密性结果的完成，使 AArch64 上的功能正确性、完整性和机密性三类证明全部就绪。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**核验**: 多源印证

**背景**: seL4 是由 NICTA 和新南威尔士大学开发的第三代 L4 微内核，专为高可信、安全系统而设计，是首个拥有机器检查的功能正确性证明的操作系统内核。形式化验证利用数学方法证明系统满足机密性、完整性和可用性等性质。AArch64 是 ARM 架构的 64 位执行状态，广泛应用于现代智能手机、嵌入式设备和许多服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SeL4">seL4 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://en.wikipedia.org/wiki/L4_microkernel_family">L4 microkernel family - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了证明仅适用于非 MCS 和单核配置等限制，也有人警告侧信道时序攻击可能削弱该结果。其他人讨论了 seL4 的实际使用者，包括 GenodeOS、LionsOS 以及一家中国汽车制造商将其用作 hypervisor，并认为仅靠嵌入式/军用市场资助可能不够，还需要原生 seL4/Linux 路线。

**标签**: `#seL4`, `#formal verification`, `#microkernel`, `#security`, `#AArch64`

---

<a id="item-3"></a>
## [依赖 AI 编程或致编码专业能力崩塌，引发开发者热议](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 8.0/10

Lars Faye 发表观点文章，认为对 AI 编程工具的依赖将导致编码专业能力崩塌，该文在 Hacker News 上引发 398 条评论的热议。讨论聚焦于引导式编码（guided coding）与 vibe coding 的对比，以及企业层面要求尽量使用 AI 生成代码的压力。 这件事很重要，因为 AI 编程助手正迅速成为软件工程中的标配，而文章质疑它们是否会侵蚀构建和维护复杂系统所需的深层专业能力。这场讨论影响开发者、工程管理者和教育工作者，他们需要决定如何在引入 AI 工具的同时不牺牲技能的养成。 文章的核心论点是：消除编码中的摩擦会削弱长期技能养成，因为专业能力是在攻克难题的过程中发展起来的。评论者指出，企业层面的强制要求，例如“如果你还在手写代码，你就做错了”，正推动工程师以超过人工审查速度的节奏产出代码。

hackernews · larsfaye · 8月24日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=49421554)

**核验**: 多源印证

**背景**: Cursor、Zencoder 等 AI 编程工具利用大语言模型在开发者的编辑器中生成、补全和修改代码。“Vibe coding”通常指让 AI 在极少人工监督下编写大部分代码，而“引导式编码”（guided coding）则指开发者照常编写代码，但使用集成的 LLM 来消除繁琐部分并辅助规划。文章认为后者能保留理解力和技能，而前者可能导致无人能完全理解的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/">AI Coding Agent for Building Ambitious Software | Cursor</a></li>
<li><a href="https://zencoder.ai/">Zencoder | The AI Coding Agent</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论大多认同文章的担忧，多位开发者提到企业把手工编码视为错误做法的强制要求。一些评论者强烈主张引导式编码是比 vibe coding 更高效、质量更高的替代方案，另一些人则认为主动寻求摩擦的开发者仍能培养专业能力，并警告当前的发展轨迹不可持续。

**标签**: `#AI coding`, `#software engineering`, `#developer expertise`, `#AI agents`, `#industry analysis`

---

<a id="item-4"></a>
## [Grok Bot 0.18.0 源码映射泄露，原始代码被完整还原](https://x.com/LinearUncle/status/2091771520339325356) ⭐️ 8.0/10

Grok Bot 0.18.0 在发布时未关闭运行时 source maps，开发者 Bennett 据此完整还原了原始源代码。还原出的代码（含系统提示词、工具定义和模型路由逻辑）已发布到 GitHub。 这是一次罕见的、非计划性的专有 AI 智能体内部实现曝光，揭示了通常被保密的系统提示词与路由逻辑等细节。同时也警示了严重的安全风险：在生产环境发布 source maps 会让任何人都能还原原始源代码。 Bennett 将还原后的源码发布在 github.com/b-nnett/grok-b…，发帖人实测最新版本已不再包含 source maps。此次泄露使系统提示词、工具定义和模型路由逻辑全部可读。

twitter · LinearUncle · 8月24日 06:16

**核验**: 多源印证

**背景**: Source map 是一种 JSON 文件，用于将压缩或转换后的 JavaScript 映射回原始源文件，通常用于调试。如果生产构建未关闭 source maps，任何人都能据此还原原始代码。Grok Bot 是 xAI 推出的 AI 智能体，拥有自己的云端计算机，可以像人类用户一样操作应用和网站。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Source_map">Source map - Glossary - MDN Web Docs</a></li>
<li><a href="https://x.ai/bot">Grok Bot : A new kind of colleague</a></li>
<li><a href="https://www.indiatoday.in/technology/news/story/elon-musk-launches-grok-bot-ai-agent-with-its-own-computer-that-does-things-for-you-2969267-2026-08-12">Elon Musk launches Grok Bot , AI agent with its own... - India Today</a></li>

</ul>
</details>

**社区讨论**: 评论区反应以调侃和好奇为主：有网友笑称 source maps 没关导致全部代码被还原，还有人说自己在上厕所间隙用 Codex 帮忙查看泄露内容。也有人向 Grok 提问：source map 是什么、开发者怎么会忘记关闭它。

**标签**: `#Grok Bot`, `#source maps`, `#reverse engineering`, `#AI agents`, `#security`

---

<a id="item-5"></a>
## [AI Agent 让布鲁克斯的“外科手术团队”模式重新可行](https://x.com/dotey/status/2091662478425899254) ⭐️ 8.0/10

一篇被广泛转发的帖子认为，Claude Code、Codex 等 AI 编程 Agent 让布鲁克斯的“外科手术团队”模式重新变得可行：一个具备技术判断力的人可以带领一群 Agent，构成一个完整的交付单元。 这一观点重新定义了 AI 时代软件团队的组织方式，认为“一个人 + AI”可以接近甚至达到传统团队的产出。它也指出，人类大脑的工作记忆容量仍是驾驭系统复杂度的最终瓶颈。 帖子将康威定律与《人月神话》中布鲁克斯的讨论联系起来：n 个人会产生 n(n-1)/2 条沟通路径。它认为 AI Agent 可以充当单一“外科医生”周围的支持团队，由后者掌握全部设计决策；而在超大规模系统上，仍需要多个“外科医生”各自带领 Agent 团队按接口契约分工。

twitter · 宝玉 · 8月23日 23:02

**核验**: 多源印证

**背景**: 康威定律由梅尔文·康威于 1967 年提出，指组织设计出的系统会复制其沟通结构。弗雷德·布鲁克斯在《人月神话》中提出“外科手术团队”模式，把设计决策集中到一位架构师身上以降低沟通成本。Claude Code 和 Codex 是 AI 编程 Agent，可以在开发者的指导下编辑代码、执行命令并完成开发任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lafosse.com/insights/the-mythical-man-month-best-practice-for-building-development-teams/">The Mythical Man-Month - Best practice for building development teams</a></li>
<li><a href="https://www.trevorlasn.com/blog/conways-law">Conway ' s Law : The Hidden Force Shaping Your Software Arch...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent , Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 评论者大多结合亲身经历表示认同：一个人加 AI 就能完成以前需要多人配合的系统，但最耗时的是前期的需求讨论和后期的测试验证。也有人提出反向观点：在 Agent 时代，康威定律可能变成系统架构反映的是单个人的提示词历史与思维方式。

**标签**: `#AI agents`, `#Conway's Law`, `#Claude Code`, `#AI developer tools`, `#software engineering`

---

<a id="item-6"></a>
## [MetaRoCE：为 AI 规模以太网打造的全新 RDMA 传输协议](https://engineering.fb.com/2026/08/24/networking-traffic/metaroce-rdma-transport-ai-ethernet) ⭐️ 7.55/10

Meta 于 2026 年 8 月 24 日宣布并开源了 MetaRoCE，这是一个专为以太网上的 AI 工作负载设计的新型 RDMA 传输协议。该协议通过开放计算项目（OCP）发布了规范、参考软件实现和合规测试套件。 MetaRoCE 解决了 AI 规模以太网的关键网络挑战，例如对 PFC 的依赖、多路径支持和乱序交付，同时兼容现有 RDMA Verbs API 和软件栈。这可以让 GPU 集群运营方在不修改应用程序的情况下，构建具备高吞吐和低尾延迟的百万 GPU 规模网络。 该协议将智能移至端点，原生支持乱序交付、多路径、无损容忍和双向拥塞控制，从而无需使用优先级流控（PFC）。Meta 通过 OCP 发布了规范、参考实现和合规测试，以推动广泛采用。

aihot · Meta Engineering Blog（RSS） · 8月24日 18:02 · [中文阅读](https://aihot.virxact.com/items/cmt7nq1d02bs1ro7373u88po4)

**核验**: 多源印证

**背景**: RDMA（远程直接内存访问）允许一台服务器通过网络直接读写另一台服务器的内存，而无需主机 CPU 或操作系统内核参与，这对高性能 AI 和 HPC 工作负载非常重要。PFC 由 IEEE 802.1Qbb 标准定义，是一种用于以太网架构中防止丢包的链路级流控机制，但在超大规模下会变得运维复杂。MetaRoCE 旨在让通用以太网也能获得 RDMA 的优势，同时避开 PFC 的扩展性问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://engineering.fb.com/2026/08/24/networking-traffic/metaroce-rdma-transport-ai-ethernet/">MetaRoCE : A New RDMA Transport Built for AI-Scale Ethernet</a></li>
<li><a href="https://www.leviathansystems.co/glossary/priority-flow-control">What Is Priority Flow Control ? | Leviathan Systems</a></li>
<li><a href="https://www.ionos.com/digitalguide/server/know-how/what-is-remote-direct-memory-access-rdma/">What is Remote Direct Memory Access ( RDMA )? - IONOS</a></li>

</ul>
</details>

**标签**: `#RDMA`, `#AI infrastructure`, `#Ethernet networking`, `#Meta`, `#Open Compute Project`

---

<a id="item-7"></a>
## [GPT-5.6 登陆 Kiro，开发成本降低约 82%](https://openai.com/index/gpt-5-6-in-kiro) ⭐️ 7.47/10

OpenAI 的 GPT-5.6 模型家族（Sol、Terra、Luna）现已登陆软件开发智能体 Kiro。在 Terminal-Bench 2.1 测试中，GPT-5.6 Terra 在 Kiro 内完成任务的成本降低了约 82%。 这一更新让先进的 AI 编程智能体更具性价比，直接回应了开发者对更低成本、更高质量代码生成的需求。同时，它也巩固了 OpenAI 与 AWS 合作在竞争激烈的 AI 开发者工具市场中的地位。 GPT-5.6 家族包含 Sol、Terra 和 Luna 三款模型，并与 AWS 合作优化，以更少的迭代和更高的 token 价值帮助开发者。根据 Artificial Analysis 排行榜，GPT-5.6 Sol（xhigh）在 Terminal-Bench v2.1 上取得 89.5% 的最高分。

aihot · OpenAI：官网动态（RSS · 排除企业/客户案例） · 8月24日 12:00 · [中文阅读](https://aihot.virxact.com/items/cmt7nzq6i2c27ro73tqxagz44)

**核验**: 多源印证

**背景**: Kiro 是一款基于 Code OSS 平台的智能体 AI IDE，可将提示词转化为可执行的规格说明、验证代码正确性，并通过并行智能体在大型代码库中工作。Terminal-Bench 是一套基准测试，用于衡量智能体在容器环境中完成复杂且有价值任务的能力，例如调试异步代码和解决安全问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kiro.dev/">Kiro: Move beyond AI coding to agentic engineering</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/terminalbench-v2-1">Terminal-Bench v2.1 Benchmark Leaderboard | Artificial Analysis</a></li>
<li><a href="https://github.com/harbor-framework/terminal-bench-2-1">GitHub - harbor-framework/terminal-bench-2-1: Terminal-Bench 2.1 · GitHub</a></li>

</ul>
</details>

**标签**: `#GPT-5.6`, `#Kiro`, `#AI agents`, `#developer tools`, `#cost efficiency`

---

<a id="item-8"></a>
## [MS Paint 与 Photos 为本地生成的 AI 图片静默嵌入 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 7.0/10

一项逆向工程分析发现，微软画图（MS Paint）和照片（Photos）应用会在使用 AI 功能编辑的图片中嵌入不可见的 GUID 水印，即使图片是在本地设备上生成的也是如此。该水印由服务器签发且无法关闭，而可见水印则可以手动关闭。 这一发现很重要，因为不可见 GUID 相当于唯一标识符，可能将图片关联到具体的微软账户，从而削弱用户在本地创建或编辑图片时的匿名性。它还对广泛使用的消费级 AI 工具中静默嵌入水印的做法提出信任质疑，并可能带来版权纠纷方面的法律影响。 分析指出，在 Copilot+ PC 上，图像生成在本地完成，但提示词审核仍由远程服务器执行，服务器签发的 GUID 会以不可见水印的形式嵌入本地生成的图片中。目前尚不清楚该水印是否也适用于 AI 增强的背景删除等操作，且据报道这个不可见水印无法关闭。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**核验**: 多源印证

**背景**: 不可见水印是一种将隐藏信息嵌入数字图片的技术，用于在不明显改变图像外观的情况下追踪来源或版权。内容来源与真实性联盟（C2PA）等行业组织正在推广开放标准，用于记录数字内容的来源和编辑历史，其中通常包含与 AI 相关的元数据。微软在画图和照片应用中提供的 AI 图像功能，是生成式 AI 工具进入消费级软件这一大趋势的一部分，而 Copilot+ PC 支持部分本地处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs ... :: Xusheng Li</a></li>
<li><a href="https://c2pa.org/">C 2 PA | Verifying Media Content Sources</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content_Authenticity_Initiative">Content Authenticity Initiative - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论区有人对 MS Paint 现在包含 AI 功能感到震惊，并担心不可见 GUID 作为唯一标识符，可能被用来将图片追溯到用户的微软账户，甚至引发版权传票。有评论者认为 AI 方面是障眼法，真正的问题在于秘密添加唯一标识符；还有人提到微软此前在 Azure DevOps 中错误添加 Copilot 水印的草率做法，并建议避免使用这类应用。另有评论者表示，该水印曾在他/她的使用场景中被错误触发。

**标签**: `#watermarking`, `#privacy`, `#AI tools`, `#Microsoft`, `#digital provenance`

---

<a id="item-9"></a>
## [Pi 贡献者澄清：网传「官方方案」实为社区 PR 误传](https://x.com/yaogangqiang/status/2091751515686096935) ⭐️ 7.0/10

一位基于 Pi 开发业务产品并参与贡献的开发者公开纠正了一篇广泛传播的分享：该分享把一个自动关闭、未经人工审核的社区 PR 包装成「Pi 官方方案」，并把 PR 自行报告的 benchmark 写成 Pi 的官方结论。他还指出，文中关于 Session Tree、Lane 和 Operation Log 的架构描述源自 Harness v2 的旧设计，并非当前 dev 的最新方案。 这次澄清很重要，因为关于 Pi「官方方案」和 benchmark 的病毒式传播内容可能误导正在评估 AI 编程助手的开发者。它有助于避免 AI 开发者工具社区得出错误结论，也提醒人们：当信息搭上 Coding Agent、Pi、DeepSeek、Claude Code 等热点时，未经核实的内容很容易被放大传播。 该社区 PR 是自动关闭的，没有经过人工审核，其自行报告的 benchmark 却被当作 Pi 的官方结论。作者还澄清，「DSH 会永久丢失原始结果」是社区 PR 对 DSH pruner 的评价，并非「Pi 官方表示」。

twitter · Gangqiang Yao · 8月24日 04:56

**核验**: 多源印证

**背景**: Pi 是一个开源 AI agent 工具包，提供统一的 LLM API、agent 循环、TUI 和 coding agent CLI，并以极简 system prompt 实现高 token 效率。Harness v2 是一份关于「持久化 agent harness」的设计文档，描述了 append-only conversation tree、可平行 lane、每条 lane 的 operation log 以及 latest-wins global facts 等概念；网传文章据称引用的是该设计的旧版本，而非当前 dev 的最新方案。DSH（DeepSeek Harness）是围绕基于 DeepSeek 的 agent harness 构建的插件与基础设施生态，包含会话同步和上下文剪枝等工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/earendil-works/pi">GitHub - earendil-works/pi: AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI · GitHub</a></li>
<li><a href="https://tenten.co/learning/coding-agent-harness-crash-recovery/">Agent Harness 長跑崩潰還原</a></li>
<li><a href="https://github.com/0xsline/awesome-deepseek-harness">GitHub - 0xsline/awesome-deepseek-harness: DeepSeek Harness (DSH) ecosystem: curated plugins, tools, and infrastructure from dsh-external/hub and the public dsh-plugin topic. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 作者指出，这篇内容传播很广，部分原因是它同时踩中了 Coding Agent、Pi、DeepSeek、Claude Code 等热点；他也观察到评论区几乎没有人去核查原始来源和这些结论。68 条回复说明讨论热度不低，但整体缺乏事实核查，而非出现有实质内容的反驳。

**标签**: `#AI agents`, `#Pi`, `#open source`, `#fact-checking`, `#developer tools`

---

<a id="item-10"></a>
## [评估构建的金发姑娘原则：衡量中间阶段](https://x.com/realmadhuguru/status/2091684812012875981) ⭐️ 7.0/10

Madhu Guru 关于构建评估的第七篇文章提出了“金发姑娘原则”：评估应衡量 AI 代理的各个中间工作阶段，而不仅仅是最终答案。他以金融分析代理为例，将工作流程拆分为客户理解、证据收集、数据分析和推荐建议，并为每个阶段设置独立评估。 这一点很重要，因为许多团队只构建最终答案的黄金数据集，导致难以诊断代理在哪个环节失败。分阶段评估能提供可操作的诊断信息，帮助开发者提升代理可靠性并减少调试时间。 文章主张评估应“不过细、不过粗、恰到好处”——粒度要足以定位问题并采取行动。一个设计良好的评估集可能会给出类似客户理解 92%、证据提取 92%、数据分析 70%、推荐建议 75% 的分数，从而指出薄弱环节。

follow_builders · Madhu Guru · 8月24日 00:31

**核验**: 多源印证

**背景**: LLM 评估（evals）用于验证基于大语言模型的系统是否足够可靠，因为 LLM 具有非确定性，其失败更多是行为层面的问题，而不是代码层面的缺陷。黄金数据集（golden set）是一组经过人工整理的参考答案，用来检查模型输出是否正确。对于 AI 代理，完整的评估通常需要结合生产环境监控、用户反馈和系统性评估，而分阶段评估有助于定位具体哪个子任务出了问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents">Demystifying evals for AI agents \ Anthropic</a></li>
<li><a href="https://www.langchain.com/resources/llm-evals">LLM Evals: The Feedback Loop Behind Reliable AI Agents</a></li>
<li><a href="https://newsletter.pragmaticengineer.com/p/evals">A pragmatic guide to LLM evals for devs</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#evals`, `#LLM evaluation`, `#agent development`, `#financial analysis`

---

<a id="item-11"></a>
## [Garry Tan 预测：记录系统须成为 AI 控制层，否则将被智能体取代](https://x.com/garrytan/status/2091742825042030681) ⭐️ 7.0/10

Y Combinator 总裁 Garry Tan 在 X 上预测，记录系统（systems of record）必须演变为 AI 控制层（harness），否则可能被 AI 智能体取代。这条帖子是一则简短、宏观的行业预测，而非深入的技术分析。 这一预测来自创业投资领域最具影响力的人物之一，因此它预示着企业软件的资金流向和产品战略可能转向何方。随着 AI 智能体成为主要用户界面，它也给 CRM、ERP 等记录类软件厂商带来重新定位的压力。 “记录系统”是企业运营的权威数据存储，例如 CRM 或 ERP 系统。“AI 控制层（harness）”则是管理智能体身份、访问权限和用户意图的层级，决定产品在何时以及以何种方式发挥作用。

follow_builders · Garry Tan · 8月24日 04:22

**核验**: 多源印证

**背景**: 传统企业软件通过中央平台连接各部门、自动化工作流，并将数据存储在共享系统中。随着 AI 智能体能够直接根据用户意图采取行动，一些分析师认为智能体将取代仪表盘甚至 SaaS 工具，另一些人则建议保留记录系统并在其上构建智能体层。Garry Tan 的预测与这种观点一致，即记录系统必须吸收智能体能力，否则将失去其核心地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/harness-problem-enterprise-ai-jody-boelkes-svklc">The Harness Problem in Enterprise AI</a></li>
<li><a href="https://orbilontech.com/ai-agents-replacing-saas-tools-2026/">AI Agents Replacing SaaS Tools: What It Means for 2026</a></li>
<li><a href="https://www.sencha.com/blog/the-ultimate-guide-to-enterprise-software-application/">Enterprise Software Application: Everything You Need to Know in 2025</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#systems of record`, `#enterprise software`, `#industry prediction`, `#AI tools`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="9"><span>其他追踪推文</span><span class="archive-tab-count">9</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="3"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">3</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2092014354946257338">@dotey: https://t.co/TxWy1XGBrY</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月24日 22:21 UTC · 喜欢 2 · 转发 0 · 回复 1 · 浏览 439</p>
<p class="archive-item-content">https://t.co/TxWy1XGBrY</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2091996016631300366">@dotey: 这种技术选型，我年轻的时候会选 DeepSeek Harness，现在会选 Pi。 年轻的时候追求技术上的新和酷，喜欢学新的东西，总觉得什么都要用用什么都要学学，喜欢折腾，较少的考虑项目...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月24日 21:08 UTC · 喜欢 18 · 转发 0 · 回复 10 · 浏览 4967</p>
<p class="archive-item-content">这种技术选型，我年轻的时候会选 DeepSeek Harness，现在会选 Pi。<br>
<br>
年轻的时候追求技术上的新和酷，喜欢学新的东西，总觉得什么都要用用什么都要学学，喜欢折腾，较少的考虑项目和团队。<br>
<br>
现在更追求项目需要的、稳定的、简单的，先做出来才是最重要的，能稳定运行更好。Pi 就简单稳定，DSH 还是新东西，稳定下来还要一段时间，何苦来哉。<br>
<br>
再说了，现在有 AI，测试覆盖好一点，以后要换底层其实没那么难。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2091968767848837330">@dotey: 如果对 DeepSeek Harness 有兴趣的，可以看看，写的很好👍</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月24日 19:19 UTC · 喜欢 69 · 转发 6 · 回复 15 · 浏览 13309</p>
<p class="archive-item-content">如果对 DeepSeek Harness 有兴趣的，可以看看，写的很好👍</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/XDustinWei/status/2091863994915266670">@XDustinWei: 写公众号真的能改变人的命运！ 我是那种比较内向，甚至有点社恐的人，很怕在公开场合表达，刚开始的时候我都不敢把自己写的小破文章发出来。 后面有认识的大佬的鼓励，下定决心跨出第一步，跨出第一...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月24日 12:23 UTC · 喜欢 113 · 转发 16 · 回复 25 · 浏览 14822</p>
<p class="archive-item-content">写公众号真的能改变人的命运！<br>
<br>
我是那种比较内向，甚至有点社恐的人，很怕在公开场合表达，刚开始的时候我都不敢把自己写的小破文章发出来。<br>
<br>
后面有认识的大佬的鼓励，下定决心跨出第一步，跨出第一步后好像也没那么难。<br>
<br>
从去年 12 月，我开始定期更新公众号，也不频繁，就下班写一写，赶上热度也有文章冲上了 10W+<br>
<br>
然后就有商单找我，而且写着写着竟然也有出版社联系到我出书。<br>
<br>
这些是我之前想都不敢想的！<br>
<br>
而最近，这件当时觉得有点不可思议的事，真的落地了，我写的《Codex 提效手册》正式上架了。<br>
<br>
也特别感谢人民邮电出版社图灵的编辑老师，最初邀请我写这本书。<br>
来 X 上，我还特别想感谢一下宝玉老师 @dotey  和花叔 @AlchainHust   ，第一次写书多少有点不自信，但把书稿给到大佬后，收到了他们的推荐，这给了我很大的信心。<br>
<br>
半年前的我，连发篇文章都不敢，现在我居然有了自己写的书。<br>
我觉得，写作真的在一点点改变我的命运轨迹。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/LotusDecoder/status/2091798706135966009">@LotusDecoder: 好了， 硬件的选择告一段落， 开始新的软件栈纠结， 是继续用 pi agent 做开发呢？ 还是用 deepseek harness？ pi 是真的简洁易懂，改改代码就上手。 deeps...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月24日 08:04 UTC · 喜欢 26 · 转发 0 · 回复 26 · 浏览 8575</p>
<p class="archive-item-content">好了，<br>
硬件的选择告一段落，<br>
开始新的软件栈纠结，<br>
是继续用 pi agent 做开发呢？<br>
还是用 deepseek harness？<br>
<br>
pi 是真的简洁易懂，改改代码就上手。<br>
deepseek harness 是一切皆插件，以后给到 agent 本体的自由度会更大吧。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2091780906965242131">@op7418: 小米发了一个 AI 的本地的主机，搭载他们新发布的三个芯片，O3、O100 和 D100，支持 120B 和 3B 双模型，支持快慢系统的切换。 https://t.co/gYIleXbByp</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月24日 06:53 UTC · 喜欢 866 · 转发 83 · 回复 98 · 浏览 268775</p>
<p class="archive-item-content">小米发了一个 AI 的本地的主机，搭载他们新发布的三个芯片，O3、O100 和 D100，支持 120B 和 3B 双模型，支持快慢系统的切换。 https://t.co/gYIleXbByp</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2091738749734666258">@op7418: 我实在搞不懂那些用 AI 回复的人是什么心理和心态。 这样只会加大你被别人拉黑的概率，而且你的内容一眼就能看出来是 AI 生成的，AI 圈所有人都能看懂。 你转发，我不管，再强调一遍：所...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月24日 04:05 UTC · 喜欢 192 · 转发 5 · 回复 156 · 浏览 45620</p>
<p class="archive-item-content">我实在搞不懂那些用 AI 回复的人是什么心理和心态。<br>
<br>
这样只会加大你被别人拉黑的概率，而且你的内容一眼就能看出来是 AI 生成的，AI 圈所有人都能看懂。<br>
<br>
你转发，我不管，再强调一遍：所有用 AI 回复我的内容的人，我都会拉黑<br>
<br>
这是一个非常吃力不讨好、闲得没事干、浪费 token 的行为，怎么还有人锲而不舍地这么干？</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2091691189531750722">@op7418: Codex 重置了，提到的 Token 过度消耗问题也得到了修复</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月24日 00:56 UTC · 喜欢 14 · 转发 0 · 回复 54 · 浏览 19505</p>
<p class="archive-item-content">Codex 重置了，提到的 Token 过度消耗问题也得到了修复</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2091688655828246890">@thsottiaux: Good Sunday. Reset has been propagated to accounts and we landed some fixes to usage for thin...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月24日 00:46 UTC · 喜欢 9858 · 转发 366 · 回复 1524 · 浏览 1178859</p>
<p class="archive-item-content">Good Sunday. Reset has been propagated to accounts and we landed some fixes to usage for things mentioned yesterday as issues we found. You should feel a positive difference. More to come tomorrow and will keep communicating.</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2091696412744700268">Nikunj Kothari: Mother in law is visiting from India.. Wants to do serendipitous date night with her grand da...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari：岳母从印度来访.. 想和孙女来一场随性的约会之夜</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 8月24日 01:17 UTC · 喜欢 170 · 转发 0 · 回复 12</p>
<p class="archive-item-content">A developer shares a quick personal story about getting a data eSIM for his visiting mother-in-law in minutes.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位开发者分享了一个快速为来访的岳母办理数据 eSIM 的个人小故事，感叹现在几分钟就能搞定通信。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2091688655828246890">Thibault Sottiaux: Good Sunday. Reset has been propagated to accounts and we landed some fixes to usage for thin...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.3 out of 10">6.3</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：周日愉快。重置已传播到账户，我们修复了一些使用问题...</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月24日 00:46 UTC · 喜欢 7425 · 转发 316 · 回复 1055 · 浏览 1178859</p>
<p class="archive-item-content">Thibault Sottiaux announces that the usage reset has been propagated to accounts and fixes for usage issues have been deployed, with more updates to come.</p>
<p class="archive-item-translation"><span>中文摘要</span>Thibault Sottiaux 宣布使用量重置已同步到账户，并部署了针对使用问题的修复，更多更新将于明天发布。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2091671326897713424">Guillermo Rauch: Intelligence is getting cheaper. @OpenAI Sol&#x27;s price reductions &amp; discounts on Vercel AI Gate...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：智能正在变得更便宜。@OpenAI Sol 的价格下调及 Vercel AI Gateway 折扣……</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 8月23日 23:38 UTC · 喜欢 325 · 转发 17 · 回复 33</p>
<p class="archive-item-content">Guillermo Rauch argues that falling inference costs are driving elastic demand for frontier models, and AI gateways are becoming essential for capturing price volatility and reducing operating costs.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 认为推理成本下降正推动前沿模型需求弹性增长，而 AI 网关对于利用价格波动、降低运营成本正变得不可或缺。</p>
</article>
</div>
</section>
