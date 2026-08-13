---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 57 条内容中筛选出 13 条重要资讯。

---

1. [阿里开源 Qwen3.8-2.4T-A95B 模型：2.4T MoE 架构，激活 95B 参数](#item-1) ⭐️ 8.9/10
2. [DeepSeek V4 Pro 0813 正式发布，引发开发者对其性能与成本的讨论](#item-2) ⭐️ 8.6/10
3. [AI 正在淘汰软件工程的中层阶级？](#item-3) ⭐️ 8.3/10
4. [Tailscale 将数据库损坏溯源至一个存在 16 年的 SQLite WAL-Reset 漏洞](#item-4) ⭐️ 8.0/10
5. [YC 支持的初创公司利用 AI 智能体为半导体散热发现新材料。](#item-5) ⭐️ 8.0/10
6. [Meta 超 200 亿美元收购 AI 初创公司 Manus 被中国监管机构强制撤销](#item-6) ⭐️ 8.0/10
7. [Meta 开源多模态模型 Muse Glimmer 30B 在 OpenRouter 平台上线。](#item-7) ⭐️ 7.8/10
8. [谷歌研究：Recall（回忆）是 LLM 参数化事实性的主要瓶颈](#item-8) ⭐️ 7.65/10
9. [微软首发自研推理模型 MAI-Thinking-1，现已上线 Microsoft Foundry 平台。](#item-9) ⭐️ 7.65/10
10. [调查发现，号称'100%人类撰写'的医学研究服务实为全程 AI 驱动。](#item-10) ⭐️ 7.15/10
11. [Mitchell Hashimoto 预览 Superlogical 终端的 'Tab Peek' UI 功能](#item-11) ⭐️ 7.0/10
12. [Vercel AI SDK 月下载量突破 8050 万次，增速超越各大 AI 实验室 SDK](#item-12) ⭐️ 7.0/10
13. [Aaron Levie 认为，由于非确定性工作流，FDEs 对于 AI 智能体至关重要。](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [阿里开源 Qwen3.8-2.4T-A95B 模型：2.4T MoE 架构，激活 95B 参数](https://www.ithome.com/0/989/001.htm) ⭐️ 8.9/10

阿里巴巴的 Qwen 团队正式开源了 Qwen3.8-2.4T-A95B 模型的权重，这是其顶级 'Qwen-Max' 级别模型首次开源。该模型采用 2.4 万亿参数的混合专家（MoE）架构，每个 Token 激活 950 亿参数，原生支持 256K 上下文长度，并可扩展至 100 万 Token。 此次发布是开源大语言模型领域的一次重大范式转变，它将顶级的超大规模模型架构开放给研究和开发社区。这直接影响了 AI 智能体和开源工具生态，为创新提供了一个强大且可审查的基础，降低了开发高级 AI 应用的门槛。 该模型提供了 BF16 和 FP8 精度格式，据报道，其 1 比特量化版本可将模型大小降至约 397GB，同时保持 950 亿激活参数。不过，开源权重版本缺少官方 'Qwen3.8-Max' 服务中的某些功能，例如视觉输入支持和默认的 100 万上下文长度。

aihot · IT之家（RSS） · 8月12日 16:10 · [中文阅读](https://aihot.virxact.com/items/cmsqagyyz00yuroucf55e5fue) · 2 个来源

**核验**: 多源印证

**背景**: 混合专家（MoE）是一种用于大语言模型的架构，它使用许多专门的子模型（'专家'）来提高性能，同时通过在推理时仅为每个输入激活一部分专家来保持计算成本可控。模型量化（例如使用 FP8 精度）是一种通过用更少的比特表示权重来减少大模型内存占用和计算需求的技术，尽管有时可能会影响精度。开源模型权重是指将训练好的模型参数公开，允许他人使用、研究和在其基础上构建，这有助于促进透明度和加速研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts? | IBM</a></li>
<li><a href="https://promptengineering.org/llm-open-source-vs-open-weights-vs-restricted-weights/">Openness in Language Models : Open Source vs Open Weights vs...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论既包含了兴奋之情，也提出了实际担忧。用户对该模型的性能印象深刻，有人指出其 1 比特量化版本将顶级能力带到了更易获取的硬件上。然而，也有人担忧其服务成本高于 Grok 等竞争对手，开源权重版本缺乏视觉支持和默认的 100 万上下文，并且需要进一步的量化工作才能使其更易于部署。讨论中还将其与 DeepSeek V4-Pro 等其他近期大型模型进行了比较。

**标签**: `#Large Language Models`, `#Model Open-Sourcing`, `#Mixture of Experts`, `#AI Research`, `#Chinese AI`

---

<a id="item-2"></a>
## [DeepSeek V4 Pro 0813 正式发布，引发开发者对其性能与成本的讨论](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.6/10

深度求索（DeepSeek）发布了其旗舰模型 V4 Pro 的正式版本（GA），命名为 '0813'，这是一个拥有 1.6 万亿参数、采用专家混合（MoE）架构、支持 100 万令牌上下文窗口的大模型。该版本在 Hacker News 上引发了广泛讨论，开发者们正在分享其用于编程和开发任务时的实际性能与成本效益反馈。 此次发布之所以重要，是因为它代表了一个可用于生产环境的高性能 AI 模型领域的主要竞争者，直接与 Claude Fable 5 和 Grok 4.6 等模型展开竞争。正如社区所强调的，其出色的成本效益可能显著降低开发者和公司利用尖端 AI 进行代码生成、模拟和引擎优化等复杂任务的门槛。 该模型在 OpenRouter 上的定价为每百万输入令牌 0.435 美元，每百万输出令牌 0.87 美元。它采用了混合注意力机制和三种推理模式。然而，一些社区成员批评相关基准测试页面缺乏适当的坐标轴标签，使得性能声明难以独立验证。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600) · 4 个来源

**核验**: 多源印证

**背景**: DeepSeek V4 Pro 是中国 AI 公司深度求索推出的大语言模型。专家混合模型是一种架构，它使用一个系统，其中不同的专用子网络（'专家'）针对不同的输入被激活，这使得模型总参数量可以非常庞大（例如 1.6 万亿），同时每次推理只使用其中一小部分（例如激活 490 亿参数），从而保持较低的计算成本。这种架构是实现高能力与相对高效率的关键。该模型通过 API 访问，OpenRouter 和 Together AI 等平台聚合了多个提供商的服务和定价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.together.ai/models/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 API: Pricing, Benchmarks & Docs | Together AI</a></li>
<li><a href="https://models.dev/models/deepseek/deepseek-v4-pro-0813/">DeepSeek V 4 Pro 0813 pricing, providers, and specs | Models .dev</a></li>
<li><a href="https://benchable.ai/models/deepseek/deepseek-v4-pro-20260813">DeepSeek : DeepSeek V 4 Pro 0813 - AI Model Details & Bench...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论显示出对该模型实际性能和价值的强烈积极情绪。用户报告称，在交通模拟和分布式物理引擎等任务上，以合理的成本获得了显著收益。然而，也有人批评原始链接缺乏有用信息，且基准测试图表没有标注。一些用户基于对之前 DeepSeek 模型的积极体验表示兴奋，并期待这个新版本具备更强大的能力。

**标签**: `#AI Models`, `#Developer Tools`, `#Cost Optimization`, `#Code Generation`, `#Open Source AI`

---

<a id="item-3"></a>
## [AI 正在淘汰软件工程的中层阶级？](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.3/10

一篇博客文章引发了讨论，其论点认为 AI 编码助手和智能体正在自动化许多软件工程师传统上执行的、以代码实现为核心的中层任务。这种自动化被认为可能通过掏空中层岗位，重塑行业的劳动力结构。 这一趋势至关重要，因为它可能从根本上改变软件开发的职业路径，加剧高级架构师与底层实现者之间的两极分化。它迫使行业重新评估未来工程师所需的技能，强调系统设计和批判性思维，而非常规编码。 讨论强调，AI 正在自动化'Stack Overflow 工程师'的角色，即中层工程师通过频繁搜索解决方案将高级设计转化为代码。一个关键的警示是，如果使用者缺乏正确指导和审查 AI 输出的批判性思维，AI 反而会放大不良的工程实践。

hackernews · florianherrengt · 8月12日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=49271994) · 2 个来源

**核验**: 多源印证

**背景**: 诸如 OpenAI 的 Codex（驱动 GitHub Copilot）和 Google 的 Gemini Code Assist 等 AI 编码助手，利用大语言模型根据自然语言提示生成、补全和重构代码。这些工具正成为开发者工作流程中的标准配置，通过自动化重复性编码任务来改变软件开发生命周期（SDLC）。更广泛的趋势涉及能够处理代码审查、管理拉取请求等更复杂软件工程任务的 AI 智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software Engineering</a></li>
<li><a href="https://www.morganstanley.com/insights/articles/ai-software-development-industry-growth">AI in Software Development: Creating Jobs and Redefining Roles | Morgan Stanley</a></li>
<li><a href="https://codeassist.google/">Gemini Code Assist for teams and businesses</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了多样化的观点，包括担忧 AI 会赋能'糟糕的'工程师大规模生产低质量代码，以及观察到 AI 自动化了从高级工程师到中级工程师的代码实现'交接'过程。另一些人则强调，为避免积累技术债务，批判性思维和深度学习仍然不可替代，也有人指出这种技术性替代是一个长期的经济趋势。

**标签**: `#AI Impact`, `#Software Engineering`, `#Future of Work`, `#Developer Tools`, `#Industry Trends`

---

<a id="item-4"></a>
## [Tailscale 将数据库损坏溯源至一个存在 16 年的 SQLite WAL-Reset 漏洞](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale 发布了一份详细的技术分析报告，解释了其控制平面数据库损坏的根源是 SQLite 预写式日志（WAL）机制中一个微妙的竞态条件漏洞，SQLite 开发者将其命名为 'WAL-Reset bug'。据估计，这个漏洞已存在至少 16 年，由涉及检查点和 WAL 文件重置的特定并发操作序列触发。 这一发现意义重大，因为 SQLite 是一个基础且被广泛信任的数据库库，用于无数应用程序中。一个长期隐藏、可能导致数据损坏的漏洞，挑战了人们对其在并发负载下绝对可靠性的假设。详细的调试过程以及为测试而资助开发的开源 VFS 垫片，也凸显了复杂工具和协作对于发现关键软件中罕见、复杂漏洞的重要性。 该漏洞仅在一种特定的竞态条件下发生：当一个连接执行检查点操作时，另一个连接恰好在事务提交后重置 WAL 文件。Tailscale 的调查得到了一个定制的、开源的 SQLite VFS（虚拟文件系统）垫片的帮助，该垫片由 Simon Willison 的公司资助开发，有助于隔离和复现这个竞态条件。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**核验**: 多源印证

**背景**: SQLite 是一个广泛使用的、自包含的、无服务器的 SQL 数据库引擎，以其可靠性和广泛的测试而闻名。预写式日志（WAL）是 SQLite 中的一种日志模式，它通过允许读取操作与单个写入操作并发进行来提高并发性。在 WAL 模式下，更改首先写入一个单独的 WAL 文件，然后在一个称为检查点的过程中稍后传输到主数据库文件。竞态条件是一种软件缺陷，其输出取决于不可控事件的顺序或时间，在并发系统中通常会导致数据损坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sqlite.org/wal.html">Write - Ahead Logging</a></li>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL - Reset bug</a></li>
<li><a href="https://en.wikipedia.org/wiki/Race_condition">Race condition - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论中既有对调试工作的赞赏，也有关于 SQLite 设计理念的辩论。一些评论者（如 inigyou）认为，这个漏洞再次证明 SQLite 并不适合高并发系统，并且与 PostgreSQL 相比缺乏在线备份等功能。另一些评论者（如 deepsun）则思考测试的局限性，指出 SQLite 庞大的测试覆盖率（59000%）仍然让这个漏洞隐藏了 16 年，这凸显了测试只能证明漏洞的存在，而不能证明其不存在。Simon Willison 强调了企业资助开源调试工具的积极作用。

**标签**: `#databases`, `#sqlite`, `#debugging`, `#concurrency`, `#systems-engineering`

---

<a id="item-5"></a>
## [YC 支持的初创公司利用 AI 智能体为半导体散热发现新材料。](https://discoveredmaterials.com/research/) ⭐️ 8.0/10

Y Combinator P26 批次的初创公司 Discovered Materials 推出了旨在为半导体行业发现新材料的 AI 智能体，特别针对 GPU 的热管理问题。他们发布了一个研究基准以及由 Anthropic 和 OpenAI 等前沿 AI 模型发现的数百种新材料候选物。 这很重要，因为 GPU 热设计功耗的指数级增长是数据中心效率和可持续性的关键瓶颈。成功加速新型热材料的发现与合成，可以显著降低下一代半导体制造所需的成本、时间和能耗。 该公司最初的重点是用于 3D 封装、热界面材料和基板的材料，并且已经合成了性能与行业长期保密配方相当的热界面材料。他们承认的一个主要挑战是弥合从计算发现到可行的实验室合成之间的差距，这仍然是一个高度依赖经验的过程。

hackernews · advaith08 · 8月12日 07:51 · [社区讨论](https://news.ycombinator.com/item?id=49269090)

**核验**: 多源印证

**背景**: 热设计功耗是芯片产生的最大热量，冷却系统必须将其散发；现代 GPU（如英伟达的 Blackwell）的 TDP 超过 1 千瓦。高带宽内存通过将内存垂直堆叠在处理器晶粒上来获得更好性能，但当前使用的二氧化硅等介电材料导热性差，会导致热量积聚。新材料从实验室发现到投入生产的过渡过程（即“从实验室到晶圆厂”） notoriously 缓慢且昂贵，常被称为“死亡之谷”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thermal_design_power">Thermal design power - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪是谨慎乐观的，专家们验证了弥合计算与实验之间鸿沟这一核心挑战。关键讨论围绕如何定义 AI 训练数据下的真正新颖性、历史上类似 AI 发现主张缺乏实际影响，以及超越计算预测的材料合成成本与可行性等实际问题展开。

**标签**: `#AI Agents`, `#Materials Science`, `#Semiconductors`, `#YC`, `#Research`

---

<a id="item-6"></a>
## [Meta 超 200 亿美元收购 AI 初创公司 Manus 被中国监管机构强制撤销](https://x.com/latepostnews/status/2087424969869603182) ⭐️ 8.0/10

2026 年 8 月 11 日，Manus 宣布即将恢复独立运营，标志着其被 Meta 以超 200 亿美元收购的交易被强制撤销。这一逆转源于 2026 年 4 月中国国家发改委发布的正式禁止投资决定，要求当事人撤销该收购交易。 这一事件是跨境科技并购的一个关键转折点，表明国家监管和地缘政治考量可以推翻重大的商业交易。它预示着中国 AI 初创企业通过被外国公司收购实现高价值退出的路径将面临更严格的审查和潜在障碍，可能重塑全球 AI 投资和初创企业的战略。 尽管经历了动荡，Manus 在调查期间的收入增长了约 5 倍，达到近每日 150 万美元。公司保持了开发节奏，并准备在交易撤销后发布 2.0 版本，其 150 人的团队在此期间无一人离职。

twitter · 晚点 LatePost · 8月12日 06:24

**核验**: 多源印证

**背景**: Manus 是一家 AI 智能体公司，开发能够自主执行复杂多步骤任务的软件，超越了对话式聊天机器人。其最初的产品'Monica'是一个基于 GPT-3 构建的浏览器扩展。该公司在 2025 年中期因其先进的 AI 智能体演示而获得广泛关注。'交易撤销'指的是撤销已完成的交易，并尽可能为所有相关方恢复交易前状态的过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.squaredtech.co/metas-2b-manus-deal-is-falling-apart-and-beijing-pulled-the-trigge">Meta Manus Deal : Beijing Forces Major $2B Unwind</a></li>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Mergers & Acquisitions`, `#Geopolitics`, `#Startup Exit`, `#Regulation`

---

<a id="item-7"></a>
## [Meta 开源多模态模型 Muse Glimmer 30B 在 OpenRouter 平台上线。](https://x.com/OpenRouter/status/2087509478480765218) ⭐️ 7.8/10

Meta AI 发布了其首个开放权重模型 Muse Glimmer，这是一个拥有 300 亿参数的密集文本+图像模型，现已在 OpenRouter 平台上线。该模型采用 Apache 2.0 许可证，旨在成为可靠的本地智能体，在 MCP Atlas 基准测试中得分为 75.5，在 SWE-Bench Pro 中得分为 51.2。 此次发布意义重大，因为它为开发者提供了一个来自主流 AI 实验室、功能强大且商业许可宽松的开源模型，该模型专门针对智能体任务进行了优化。它在 OpenRouter 平台上线降低了访问和实验的门槛，有望加速能够处理涉及代码和视觉数据的复杂多步骤工作流的本地 AI 智能体的开发。 该模型在 MCP Atlas 上 75.5 的得分表明其在具有多个可用 API 的生产级智能体场景中表现强劲，而其 SWE-Bench Pro 51.2 的得分则反映了其在现实企业级软件工程任务上的能力。作为一个拥有 300 亿参数的“密集”模型，意味着它并非混合专家架构，这可能对其效率和部署资源占用产生影响。

aihot · X：OpenRouter (@OpenRouter) · 8月12日 12:00 · [中文阅读](https://aihot.virxact.com/items/cmsq1hwsb02norobuzbw8cdcc)

**核验**: 多源印证

**背景**: OpenRouter 是一个统一的 API 平台，为开发者提供对不同供应商的各种大型语言模型的标准化访问。MCP Atlas 是一个基准测试，用于衡量模型在同时提供多个 API 和服务的生产级智能体环境中的表现。SWE-Bench Pro 是一个较新的基准测试，旨在严格评估 LLM 编码智能体在现实企业级软件工程任务上的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-boss.com/blog/what-is-mcp-atlas">What Is MCP - Atlas ? Scaled Tool Use Explained | LLM Boss</a></li>
<li><a href="https://www.linkedin.com/posts/brad-kenstler_github-scaleapiswe-benchpro-os-swe-bench-activity-7375928042118033409-ni5s">Introducing SWE - Bench Pro : A New Benchmark for Coding... | LinkedIn</a></li>
<li><a href="https://developer.puter.com/encyclopedia/openrouter/">OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Open Source`, `#Multimodal Models`, `#Developer Tools`

---

<a id="item-8"></a>
## [谷歌研究：Recall（回忆）是 LLM 参数化事实性的主要瓶颈](https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality) ⭐️ 7.65/10

谷歌研究提出了一个知识画像框架，发现前沿大语言模型（如 Gemini 3、GPT-5）的事实编码已接近饱和，但回忆（recall）能力不足，多数事实错误源于“丢钥匙”而非“空货架”。该团队同时推出了 WikiProfile 基准，包含 2,150 条维基百科事实，每条配 10 个问题，用于分别探测模型的编码、回忆与识别能力。 这一发现将提升大语言模型可靠性的重点，从单纯增加知识转向改进知识检索机制，这对于开发准确的 AI 智能体和工具至关重要。新的诊断框架和基准为研究者和开发者提供了可操作的见解，以系统性地解决事实性错误问题。 该框架将事实性错误分为五种不同的画像，包括编码失败和回忆失败。WikiProfile 基准的设计旨在分离和测量这些不同的失败模式，超越了简单的总体准确率评分，提供了更细粒度的诊断能力。

aihot · Google Research：Blog（网页） · 8月12日 17:57 · [中文阅读](https://aihot.virxact.com/items/cmsqe6mat01bsroli3hw71nz7)

**核验**: 多源印证

**背景**: 参数化知识指的是在大语言模型权重中存储的、在预训练期间学习到的事实性信息。大语言模型面临的一个关键挑战是“幻觉”，即生成事实错误的内容。传统上，人们认为提高事实性需要改进知识编码，但这项研究表明，主要问题往往是在回答问题时检索（回忆）已编码知识的能力不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality/">Empty shelves or lost keys? Recall is the bottleneck for parametric...</a></li>
<li><a href="https://huggingface.co/datasets/google/WikiProfile">google/ WikiProfile · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM Research`, `#AI Evaluation`, `#Factual Accuracy`, `#Google Research`, `#Benchmarks`

---

<a id="item-9"></a>
## [微软首发自研推理模型 MAI-Thinking-1，现已上线 Microsoft Foundry 平台。](https://x.com/mustafasuleyman/status/2087570047967408396) ⭐️ 7.65/10

微软 AI 首席执行官 Mustafa Suleyman 宣布推出 MAI-Thinking-1，这是该公司首个完全从零开始构建的推理模型，现已上线 Microsoft Foundry 平台。该模型于 2026 年 6 月 2 日的 Microsoft Build 大会上发布。 此次发布标志着微软在开发独立、自研 AI 能力战略上迈出重要一步，有望减少其在高级推理任务上对 OpenAI 等合作伙伴的依赖。在 Foundry 平台上提供专门的推理模型，为开发者构建需要复杂、多步逻辑的更强大 AI 智能体和应用提供了新工具。 据报道，MAI-Thinking-1 是一个拥有 350 亿参数、专为复杂多步指令设计的模型，其构建过程没有从 GPT 等竞争对手的模型中进行知识蒸馏，确保了没有第三方模型依赖。它被定位为一个专门专注于推理的基础模型类别，与通用语言模型不同。

aihot · X：Mustafa Suleyman（Microsoft AI CEO） (@mustafasuleyman) · 8月12日 16:00 · [中文阅读](https://aihot.virxact.com/items/cmsqbnb8j01nrroosmwa5r6mj)

**核验**: 多源印证

**背景**: 推理 AI 模型旨在执行复杂、多步的逻辑思考和问题解决，这是高级 AI 智能体的关键能力。Microsoft Foundry 是一个企业级 AI 平台（前身为 Azure AI Studio），用于大规模构建、落地和管理 AI 应用及智能体。微软通过与 OpenAI 等合作伙伴的关系在 AI 领域进行了大量投资，但也在开发自己的模型套件，以确保战略独立性并为云客户提供多样化的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/mai-thinking-1-complete-guide/">MAI - Thinking - 1 : Microsoft's First In-House Reasoning Model (2026)</a></li>
<li><a href="https://aidive.org/en/ai/microsoft-foundry">Microsoft Foundry : platform for AI apps and agents</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Microsoft`, `#Reasoning AI`, `#Product Launch`, `#AI Infrastructure`

---

<a id="item-10"></a>
## [调查发现，号称'100%人类撰写'的医学研究服务实为全程 AI 驱动。](https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai) ⭐️ 7.15/10

404 Media 的一项调查揭露，为医学研究者提供服务的 Research Gold 公司，其明确宣称'100%人类撰写、绝不使用 AI'的服务，实际上完全由 AI 操作。该公司列出的博士审稿人是 AI 生成的虚构人物，并且未经许可使用了真实自由职业方法学家的身份。 这一事件暴露了在严谨性和诚信至关重要的医学研究领域，存在严重的信任与伦理失范。它凸显了 AI 欺骗在专业服务中日益增长的挑战，可能削弱对学术支持行业的信心，并误导那些依赖此类服务进行系统综述等关键工作的研究人员。 当通过电话联系时，一个自称'Sarah'的 AI 助手坚称自己是人类并试图推销服务。该公司网站虚假宣称遵循 PRISMA 2020 和 Cochrane 手册等既定的方法学标准，这些是进行严谨系统综述的指南。

aihot · Hacker News 热门（buzzing.cc 中文翻译） · 8月12日 05:41 · [中文阅读](https://aihot.virxact.com/items/cmspo193n05q2rojeue8j2k5a)

**核验**: 多源印证

**背景**: 系统综述和荟萃分析是综合现有研究证据的严谨方法，在医学中常用于指导临床决策。方法学家是确保研究过程（包括研究设计和数据分析）在方法学上可靠的专家。像 Research Gold 这样的服务声称能为研究人员处理这种复杂、耗时的工作，并标榜拥有人类专家的专业知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scielo.org.za/scielo.php?script=sci_arttext&pid=S1681-150X2016000400005">Meta - analysis : Everything you wanted to know but were afraid to ask</a></li>
<li><a href="https://analysisfunction.civilservice.gov.uk/careers/role-profiles-and-career-pathways/role-profile-methodologist/">Role profile: methodologist – Government Analysis Function</a></li>

</ul>
</details>

**标签**: `#AI Ethics`, `#AI Misuse`, `#Investigative Journalism`, `#Academic Integrity`, `#AI Deception`

---

<a id="item-11"></a>
## [Mitchell Hashimoto 预览 Superlogical 终端的 'Tab Peek' UI 功能](https://x.com/mitchellh/status/2087537750182666290) ⭐️ 7.0/10

Mitchell Hashimoto 预览了 Superlogical 终端的一项新 'tab peek' UI 功能，用户通过三指向下滑动手势，可以实时查看其他会话标签页和分屏的、由 Metal 渲染的预览。继续拖动则会进入类似 'Mission Control' 的模式，以概览所有会话。 这一功能代表了终端多路复用器的一种新颖 UI/UX 模式，旨在通过提供即时、无干扰的上下文切换和会话状态感知，显著提升开发者的工作效率。作为一款为 AI 智能体时代重建的终端的关键功能，它标志着开发者工具正朝着更具交互性和视觉直观性的方向转变。 该预览覆盖层会将终端内容向下推离屏幕，而不会调整其大小，从而避免了文本或布局的破坏性重排。该功能未来也将支持键盘快捷键操作，并且预览是使用苹果的 Metal API 进行渲染，以实现高性能图形显示。

twitter · Mitchell Hashimoto · 8月12日 13:52

**核验**: 多源印证

**背景**: Superlogical 是一家新的终端多路复用器初创公司，由 HashiCorp 联合创始人、Vagrant 和 Terraform 等工具的创建者 Mitchell Hashimoto 创立。终端多路复用器（如 tmux 或 screen）允许用户在单个窗口内管理多个终端会话。Hashimoto 对 Superlogical 的愿景是从头开始重建终端基础设施，以更好地与 AI 编程智能体和现代开发工作流集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.superlogical.com/?ref=upstract.com">Superlogical</a></li>
<li><a href="https://noqta.tn/en/blog/superlogical-terminal-multiplexer-ai-agents-2026">Superlogical : Mitchell Hashimoto's Terminal Multiplexer for the AI...</a></li>
<li><a href="https://digg.com/tech/qkvpmyt8">Mitchell Hashimoto Previews Superlogical Tab Peek · Digg</a></li>

</ul>
</details>

**标签**: `#Developer Tools`, `#UI/UX Design`, `#Terminal`, `#Productivity`, `#Workflow Automation`

---

<a id="item-12"></a>
## [Vercel AI SDK 月下载量突破 8050 万次，增速超越各大 AI 实验室 SDK](https://x.com/rauchg/status/2087339038781161858) ⭐️ 7.0/10

Guillermo Rauch 宣布 Vercel AI SDK (@aisdk) 正经历惊人的增长，每 30 天约有 8050 万次下载。其增长速度现已超过所有主要 AI 实验室的 SDK，并且它保持开源和提供商无关的特性。 这种大规模的采用表明开发者强烈偏好开放、灵活且能避免供应商锁定的工具，这可能将影响力从专有的 AI 实验室生态系统转移到开源社区。该 SDK 的提供商无关特性使开发者能够轻松在不同 AI 模型和服务之间切换，从而促进创新和竞争。 AI SDK 是 Vercel 推出的一个免费、开源的 TypeScript 工具包，专为使用 React、Next.js 和 Node.js 等框架构建 AI 应用程序而设计。其一个关键特性是多提供商支持，允许开发者以最少的代码更改切换提供商，这通常由 Vercel AI Gateway 提供便利。

follow_builders · Guillermo Rauch · 8月12日 00:43

**核验**: 多源印证

**背景**: AI SDK（软件开发工具包）为开发者提供了将人工智能功能集成到其应用程序中的工具和库。在此上下文中，“提供商无关”意味着该 SDK 被设计为可与多个 AI 模型提供商（如 OpenAI、Anthropic 或 Google）协同工作，而不会将开发者锁定在单一供应商的生态系统中。Vercel 以其 Next.js 框架和前端云平台而闻名，创建此 SDK 旨在为 Web 开发者简化 AI 应用开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-sdk.dev/">AI SDK</a></li>
<li><a href="https://github.com/vercel/ai">GitHub - vercel / ai : The AI Toolkit for TypeScript. From the creators of...</a></li>
<li><a href="https://www.promptforge-app.com/articles/llm-agnostic-application-architecture-rest-prompts">LLM Agnostic Architecture: Build with REST Prompts | PromptForge</a></li>

</ul>
</details>

**标签**: `#AI SDK`, `#Open Source`, `#Developer Tools`, `#AI Adoption`, `#Vercel`

---

<a id="item-13"></a>
## [Aaron Levie 认为，由于非确定性工作流，FDEs 对于 AI 智能体至关重要。](https://x.com/levie/status/2087385493684335064) ⭐️ 7.0/10

Box 公司 CEO Aaron Levie 在社交媒体发文中强调，前沿部署工程师（FDEs）是 AI 领域一个永久且关键的角色。他解释说，构建 AI 智能体与传统软件开发有根本性不同，因为它需要将非确定性系统集成到从未被自动化的工作流中，这要求持续的适配工作。 这很重要，因为它标志着软件实施模式的转变，其成功依赖于像 FDEs 这样的专业角色来弥合原始 AI 能力与不断变化的实际业务需求之间的差距。它强调了对 AI 智能体的高度定制和维护负担，将持续催生对这些工程和集成技能的需求，影响供应商、系统集成商和企业客户。 Levie 指出，与确定性软件不同，AI 智能体需要基于客户反馈进行持续的评估、模型更新和系统变更。一个关键挑战在于，对于像 2026 年的会计智能体这样的新 AI 应用，不存在预先定义的用户旅程或既定工作流可供设计参考。

follow_builders · Aaron Levie · 8月12日 03:47

**核验**: 多源印证

**背景**: 前沿部署工程师（FDEs）是一种专业角色，由 Palantir 等公司推广开来，他们与客户紧密合作，部署和定制复杂的技术解决方案，尤其是 AI。在 AI 和大语言模型（LLMs）的背景下，FDEs 专注于将原始模型输出适配到具体、实际的业务应用中。传统软件在很大程度上是确定性的，意味着给定相同的输入，每次都会产生相同的、可预测的输出，这简化了实施和测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://amitray.com/compassionate-ai-for-forward-deployed-engineers-fdes-in-saas-companies/">Compassionate AI for Forward Deployed Engineers ( FDEs ) in SaaS...</a></li>
<li><a href="https://medium.com/jin-system-architect/non-determinism-has-entered-the-build-pipeline-the-real-test-of-software-engineering-in-the-age-of-68145d0dff32">Non - Determinism Has Entered the Build Pipeline: The Real... | Medium</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Product Strategy`, `#Software Development`, `#Industry Analysis`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="16"><span>其他追踪推文</span><span class="archive-tab-count">16</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="7"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">7</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/MaxForAI/status/2087596692497719654">@MaxForAI: 梁文锋他真的我哭死😭 https://t.co/rRNdSok99y</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月12日 17:46 UTC · 喜欢 225 · 转发 21 · 回复 20 · 浏览 39016</p>
<p class="archive-item-content">梁文锋他真的我哭死😭 https://t.co/rRNdSok99y</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087583794819956750">@op7418: 滑动变祖器拉满！ https://t.co/tuFQD6Ujdv</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 16:55 UTC · 喜欢 12 · 转发 1 · 回复 20 · 浏览 5998</p>
<p class="archive-item-content">滑动变祖器拉满！ https://t.co/tuFQD6Ujdv</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087582937395147196">@op7418: SpaceX AI 发布了 Grok 4.6 模型，然后价格还行，每百万输入输出分别为 2 和 6 美元。 当然，如果你有 Twitter 的 Premium+的会员的话，依然可以通过...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 16:52 UTC · 喜欢 4 · 转发 1 · 回复 25 · 浏览 3999</p>
<p class="archive-item-content">SpaceX AI 发布了 Grok 4.6 模型，然后价格还行，每百万输入输出分别为 2 和 6 美元。<br>
<br>
当然，如果你有 Twitter 的 Premium+的会员的话，依然可以通过 Grok Build 授权来白嫖。 https://t.co/QHcUnTUS9P</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087580222992592946">@op7418: DeepSeek V4 Pro 正式版 0813 发布了！ 从流传的测试成绩来看依然相当爆炸 https://t.co/UvQIyr3wgc</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 16:41 UTC · 喜欢 35 · 转发 0 · 回复 6 · 浏览 16685</p>
<p class="archive-item-content">DeepSeek V4 Pro 正式版 0813 发布了！<br>
<br>
从流传的测试成绩来看依然相当爆炸 https://t.co/UvQIyr3wgc</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/opencode/status/2087572432181686748">@opencode: There&#x27;s been a week of hype for DeepSeek Flash So good time to announce that the newest DeepS...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 16:10 UTC · 喜欢 5103 · 转发 216 · 回复 202 · 浏览 341934</p>
<p class="archive-item-content">There&#x27;s been a week of hype for DeepSeek Flash<br>
<br>
So good time to announce that the newest DeepSeek V4 Pro is now available in OpenCode Go</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/mitchellh/status/2087571133206007948">@mitchellh: We&#x27;re looking to hire Windows developers capable of producing UI at this quality (but, idioma...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月12日 16:05 UTC · 喜欢 673 · 转发 43 · 回复 59 · 浏览 84733</p>
<p class="archive-item-content">We&#x27;re looking to hire Windows developers capable of producing UI at this quality (but, idiomatic to the Windows ecosystem, not cloning Apple). If you are one or know someone, please have them apply via `ssh https://t.co/4JHvflVz0r`. We&#x27;ve been struggling to find this person.<br>
<br>
There&#x27;s just a lot of Windows applications out there (like, almost all of them) that just aren&#x27;t good. We&#x27;re looking for someone who wants to create a Windows applications that sparks joy, excites people, and feels good. We want frame perfect animation. We want obsessive consideration over user flows, click counts, keyboard press counts, etc. <br>
<br>
We&#x27;re a team that has that kind of obsession, but lacks the Windows experience. If you know a Windows dev who has this quality obsession and wants to work with a group that shares those ideals, I want to talk to them.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087565843248906666">@dotey: deepseek-v4-pro https://t.co/IjkVmGeWvo https://t.co/YhfvnA8N6A</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月12日 15:44 UTC · 喜欢 108 · 转发 8 · 回复 14 · 浏览 32072</p>
<p class="archive-item-content">deepseek-v4-pro<br>
https://t.co/IjkVmGeWvo https://t.co/YhfvnA8N6A</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/SpaceXAI/status/2087562800982077492">@SpaceXAI: Introducing Grok 4.6. It delivers frontier intelligence and is a significant improvement over...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 15:32 UTC · 喜欢 25591 · 转发 2812 · 回复 1384 · 浏览 14881928</p>
<p class="archive-item-content">Introducing Grok 4.6.<br>
<br>
It delivers frontier intelligence and is a significant improvement over Grok 4.5 at the same price. https://t.co/RtTbpXcb3a</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/lijigang/status/2087560528763953541">@lijigang: 新增了 skill: /ljg-classic 在小红书上看到解读文言文的一类模板卡片，试着写了一版。 用途：将文言文做逐字解读+章节释义 用法：/ljg-classic 《金刚经》第一品...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月12日 15:23 UTC · 喜欢 47 · 转发 6 · 回复 20 · 浏览 4245</p>
<p class="archive-item-content">新增了 skill: /ljg-classic  <br>
<br>
在小红书上看到解读文言文的一类模板卡片，试着写了一版。  <br>
<br>
用途：将文言文做逐字解读+章节释义 <br>
用法：/ljg-classic 《金刚经》第一品 https://t.co/ztIGC2QKpK</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087494509454389651">@op7418: 又有羊毛薅了，Manus 从 Meta 剥离以后开启了限免。 如果你之前自己买过 Manus 会员，或者是通过 Lenny&#x27;s Newsletter 领过会员的话，最近可以用一用。 仅限...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 11:00 UTC · 喜欢 33 · 转发 1 · 回复 16 · 浏览 15213</p>
<p class="archive-item-content">又有羊毛薅了，Manus 从 Meta 剥离以后开启了限免。<br>
<br>
如果你之前自己买过 Manus 会员，或者是通过 Lenny&#x27;s Newsletter 领过会员的话，最近可以用一用。<br>
<br>
仅限 Manus 1.6 和 Manus Lite 两个模型 https://t.co/fXaObJ8iG2</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087457636128333947">@op7418: 小红书发布了他们的 Read Skills Top 100 排行榜，这个有专门的页面，而且会自动更新。 结果发现，藏师傅居然有两个 Skills 在前十的位置，其中一个居然排在第二！ 他...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 08:34 UTC · 喜欢 89 · 转发 9 · 回复 17 · 浏览 13101</p>
<p class="archive-item-content">小红书发布了他们的 Read Skills Top 100 排行榜，这个有专门的页面，而且会自动更新。<br>
<br>
结果发现，藏师傅居然有两个 Skills 在前十的位置，其中一个居然排在第二！<br>
<br>
他们这个也挺有意思的，排名第一的居然是一个占星应用。 https://t.co/Tpja0SwuGu</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087434739929977149">@dotey: Manus 还是挺了不起的，期待再创辉煌</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月12日 07:03 UTC · 喜欢 51 · 转发 0 · 回复 53 · 浏览 35712</p>
<p class="archive-item-content">Manus 还是挺了不起的，期待再创辉煌</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/leon7hao/status/2087433080420417577">@leon7hao: 很早之前就写过一篇关于 worktree 的 vibe coding 文章，我想可以再提一下。 大家肯定是因为希望并行地开发功能和修复才使用的 worktree。宝玉老师说可以在同一目录...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月12日 06:56 UTC · 喜欢 45 · 转发 11 · 回复 43 · 浏览 11784</p>
<p class="archive-item-content">很早之前就写过一篇关于 worktree 的 vibe coding 文章，我想可以再提一下。<br>
<br>
大家肯定是因为希望并行地开发功能和修复才使用的 worktree。宝玉老师说可以在同一目录直接并行，这对于相对简单的情况是完全可以的。但是涉及稍微复杂的情况，这样反而丧失了并行带来的好处，不断破坏 Agent 的上下文。这就好似双向同步一样的灾难，Agent A 读取到了文件改动，再顺着改动重读一遍所有的调用，浪费更多的 token，之前的设计决策可能也会被一并推翻。何况 Agent 是有大概率出现细节遗漏，导致仓库同时存在不同的假设。墨菲定律告诉我们这一定会发生。<br>
<br>
除了磁盘浪费多份之外，worktree 烦人的另外一点是一个分支只能被 checkout 绑定在一个目录。因为环境变量，端口，我相信很多人的习惯是在主目录进行测试。<br>
<br>
所以我觉得最好的一种使用 worktree 的方案是结合 GitHub 或者其他 host，本地 clone 两份 git。测试用一份，开发用一份。worktree 只在开发 git 使用，测试通过 checkout 挨个分支进行测试和收尾。通过之后开发的对话连同 worktree 就可以一并 archive 回收掉。在 Lody 中可以无感地做到这些，archive 了对话，worktree 也就被自动回收。通过 PR 状态感知验收状态。<br>
<br>
这样的好处是<br>
- Agent 做的改动永远有留痕和备份，冲突是通过 merge 完整地解决，而不是边做边解冲突。<br>
- 磁盘占用不会无限膨胀，而只和你的最大并发能力有关。<br>
- 脑袋不需要有 worktree 的概念包袱，一个 git 命令不会也可以随便并行，只需要了解干完活把对话 archive 就行。也不用受 branch 已经 checkout 到 abc 目录的折磨。<br>
<br>
https://t.co/F3kMkLZj9n</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087411690237268100">@dotey: 我一直有个观点，就是： 人不用去跟汽车比谁跑的快，不用跟 AI 比谁更聪明博学；我们驾驭好汽车到达目的地，用好 AI 完成任务，就很好了。</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月12日 05:31 UTC · 喜欢 224 · 转发 9 · 回复 101 · 浏览 31773</p>
<p class="archive-item-content">我一直有个观点，就是：<br>
人不用去跟汽车比谁跑的快，不用跟 AI 比谁更聪明博学；我们驾驭好汽车到达目的地，用好 AI 完成任务，就很好了。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087377704286847246">@dotey: 我是能不用 worktree 就不用 worktree，要么不同任务用 branch 分支，要么就直接同一个分支多任务，一般不太用担心冲突，首先只要任务类型不一样冲突可能性较小。 另外现在 Har...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月12日 03:16 UTC · 喜欢 104 · 转发 6 · 回复 61 · 浏览 81283</p>
<p class="archive-item-content">我是能不用 worktree 就不用 worktree，要么不同任务用 branch 分支，要么就直接同一个分支多任务，一般不太用担心冲突，首先只要任务类型不一样冲突可能性较小。<br>
<br>
另外现在 Harness 比如说 Claude Code、Codex 都很聪明，遇到冲突会等另一个执行完。<br>
<br>
使用 worktree 主要是在做耗时较长的 PoC 场景，只是验证一下，同时要做其他任务，完了就删除目录。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087365195580792900">@op7418: 《影之刃零》的发售预告来了，太牛逼了！那个人居然是甄子丹。 https://t.co/COdKS3aWv6</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 02:26 UTC · 喜欢 56 · 转发 3 · 回复 57 · 浏览 19137</p>
<p class="archive-item-content">《影之刃零》的发售预告来了，太牛逼了！那个人居然是甄子丹。 https://t.co/COdKS3aWv6</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2087423996115681767">Thibault Sottiaux: I previously promised a reset for every 1M in additional active users for Codex, until 10M. W...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux: 我曾承诺 Codex 每新增 100 万活跃用户就进行一次重置，直到 1000 万...</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月12日 06:20 UTC · 喜欢 2737 · 转发 176 · 回复 516</p>
<p class="archive-item-content">The creator of Codex teases a major announcement following the platform surpassing 10 million active users, referencing a previously promised &#x27;reset&#x27; milestone.</p>
<p class="archive-item-translation"><span>中文摘要</span>Codex 的创建者预告了一个重大发布，暗示该平台在活跃用户超过 1000 万后，将兑现之前承诺的里程碑&#x27;重置&#x27;。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/realmadhuguru/status/2087362394280599641">Madhu Guru: dev rels are having their moment. since building software has become trivial, distribution is...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Madhu Guru: 开发者关系正迎来其高光时刻。既然构建软件已变得微不足道，分发才是...</p>
<p class="source-line">Follow Builders · X 动态 · Madhu Guru · 8月12日 02:15 UTC · 喜欢 9 · 转发 0 · 回复 1</p>
<p class="archive-item-content">The author argues that as software creation becomes easier, distribution is the key challenge, making developer relations professionals with social media and technical skills highly valuable.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者认为，随着软件创建变得容易，分发成为关键挑战，这使得兼具社交媒体能力和技术技能的开发者关系专业人士极具价值。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/realmadhuguru/status/2087355597851390220">Madhu Guru: story time.. in 2023 (my previous role) I remember the first time some customers volunteered...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Madhu Guru: 故事时间... 回顾 2023 年（我之前的角色），我记得第一次有客户主动...</p>
<p class="source-line">Follow Builders · X 动态 · Madhu Guru · 8月12日 01:48 UTC · 喜欢 15 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A reflection on how early customer prompts for building entire apps from simple requests, once seen as ambitious, have shaped the vision for end-to-end AI development systems that are now becoming a reality.</p>
<p class="archive-item-translation"><span>中文摘要</span>文章回顾了早期客户提出&#x27;为我构建一个 X 应用&#x27;的提示如何塑造了构建端到端 AI 开发系统的愿景，并指出这一愿景在三年后已基本实现。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2087354092914122896">Guillermo Rauch: Many people are saying https://t.co/iluZF3d1Iu</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：很多人都在说 https://t.co/iluZF3d1Iu</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 8月12日 01:42 UTC · 喜欢 100 · 转发 3 · 回复 10</p>
<p class="archive-item-content">A tweet by Guillermo Rauch sharing a link with no accompanying explanation or context.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 发布的一条推文，分享了一个链接，但没有任何解释或背景信息。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2087345374633824486">Peter Yang: Getting many messages like these for /human-review. It&#x27;s now at 717 GitHub stars! Try it here...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：收到了很多关于 /human-review 的消息，它现在有 717 个 GitHub star 了！在这里试试...</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 8月12日 01:08 UTC · 喜欢 101 · 转发 2 · 回复 7</p>
<p class="archive-item-content">The author announces that their tool &#x27;/human-review&#x27; has reached 717 GitHub stars and encourages people to try it.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者宣布其工具 &#x27;/human-review&#x27; 已获得 717 个 GitHub star，并鼓励人们尝试。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2087341164752240860">Nikunj Kothari: if a founder cancels on you on a scheduled meeting, that’s a sign of great respect in their c...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari: 如果创始人在预定会议上放你鸽子，这在他们文化中是极大尊重的表现...</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 8月12日 00:51 UTC · 喜欢 295 · 转发 0 · 回复 12</p>
<p class="archive-item-content">A tweet humorously suggests that a founder canceling a scheduled meeting is a sign of respect in their culture.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文幽默地暗示，创始人在预定会议上取消会面，这在他们文化中是一种尊重的表现。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2087340277874995223">Peter Yang: Trying to onboard my parents to ChatGPT desktop app and the separation between Chat, Work, an...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：尝试让我的父母使用 ChatGPT 桌面应用，以及 Chat、Work 和 Codex 之间的割裂...</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 8月12日 00:47 UTC · 喜欢 269 · 转发 5 · 回复 47</p>
<p class="archive-item-content">The author criticizes the inconsistent user experience across ChatGPT&#x27;s different platforms (web, desktop, mobile) and its feature separation, using their parents&#x27; onboarding difficulty as an example.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者批评了 ChatGPT 在不同平台（网页、桌面、移动端）及其功能模块之间不一致的用户体验，并以父母的上手困难为例。</p>
</article>
</div>
</section>
