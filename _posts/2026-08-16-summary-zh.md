---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 从 37 条内容中筛选出 10 条重要资讯。

---

1. [Claude 系统提示词公开：长度与设计引发讨论](#item-1) ⭐️ 8.0/10
2. [AI 模型正被有意设计得更“笨”，转而依赖外部工具和知识库。](#item-2) ⭐️ 8.0/10
3. [Stripe 以超 70 亿美元收购 AI API 聚合商 OpenRouter](#item-3) ⭐️ 8.0/10
4. [教程指导如何为 Codex 配置 GPT-5.6 Sol 模型，启用 100 万 token 的上下文窗口。](#item-4) ⭐️ 8.0/10
5. [Anthropic 研究表明协调式多智能体系统能发现更多代码漏洞](#item-5) ⭐️ 7.83/10
6. [Qwen 3.8 27B 发布，性能强劲但默认过度推理](#item-6) ⭐️ 7.3/10
7. [ChatGPT Pro 用户发现 AI 可克隆代码库、分析代码并直接提交 Pull Request。](#item-7) ⭐️ 7.0/10
8. [开源水印去除工具在 Anthropic 披露水印方法后获万星](#item-8) ⭐️ 7.0/10
9. [比较 AI 模型每 token 成本具有误导性，因其分词方式不同。](#item-9) ⭐️ 7.0/10
10. [Amjad Masad 反驳 AI 导致权力结构集中的观点，援引算力性价比的历史增长趋势。](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Claude 系统提示词公开：长度与设计引发讨论](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 的 Claude 模型的详细系统提示词已被分析，结果显示其长度异常——据报道 Claude 的提示词长达 16,739 个单词，而 OpenAI 的 o4-mini 仅为 2,218 个单词。社区分析（包括一个 git 提交历史）显示了模型版本间的具体增补，例如处理图像的新指令。 这很重要，因为系统提示词是大型语言模型的核心操作指令，直接决定了其行为、安全性以及开发者构建 AI 智能体的能力。关于最佳提示词长度和具体性的争论，反映了行业内在如何最好地引导日益强大的模型而不过度限制其能力方面的广泛讨论。 尽管提示词很长，但一些最佳实践指南认为，通过提示词缓存，较长系统提示词的边际成本可以忽略不计。然而，其他资料建议为本地模型使用更短、更直接的提示词，这表明最佳设计高度依赖于模型和具体用例。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**核验**: 多源印证

**背景**: 系统提示词是一组预置在每次用户查询前的指令，用于定义 AI 模型的行为、个性和约束。对于 AI 智能体而言，系统提示词充当着核心操作系统的角色，指导智能体如何解读任务并与世界交互。这些提示词的设计是提示工程的关键方面，需要在具体性和灵活性之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oreilly.com/radar/unpacking-claudes-system-prompt/">Unpacking Claude's System Prompt</a></li>
<li><a href="https://claudeguide.io/how-to-write-system-prompts-claude">How to Write System Prompts for Claude: Complete Guide | ClaudeGuide</a></li>
<li><a href="https://docs.runanywhere.ai/web/llm/system-prompts">System Prompts - RunAnywhere Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂，一些人对提示词的长度表示惊讶，认为更短的提示词可以避免干扰，让模型更“聪明”。另一些人则提供了技术分析，追踪模型版本间的变化。讨论中还出现了一个关于论坛内容审核的离题担忧。

**标签**: `#AI Agents`, `#Claude`, `#System Prompts`, `#LLM`, `#Developer Tools`

---

<a id="item-2"></a>
## [AI 模型正被有意设计得更“笨”，转而依赖外部工具和知识库。](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

文章指出，AI 发展的一个核心趋势是，模型正被有意地从存储海量内部知识，转向从根本上设计为依赖外部工具和知识库来检索信息和执行任务的架构。 文章引用了 SimpleQA 等基准测试，指出即使像 Gemini 2.5 Pro 这样的顶级模型，在不使用工具的情况下，事实回忆准确率也仅为 53%，凸显了内部知识存储的局限性。它还提到了像 Cactus 的'Needle'模型（一个专注于工具调用的 14 MB LLM）等新兴方法。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**核验**: 多源印证

**背景**: 工具调用（或称函数调用）是一种机制，允许 AI 模型决定使用哪个外部工具或 API 来完成一项任务，例如获取数据或执行计算。检索增强生成（RAG）是一种常用技术，模型在生成回答前会查询外部知识库以检索相关信息。这些方法是创建能够感知环境并采取行动以实现目标的“智能体 AI”系统的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/tool-calling">What Is Tool Calling? | IBM</a></li>
<li><a href="https://fin.ai/learn/ai-knowledge-base">AI Knowledge Base: The Complete Guide for 2026 - Fin AI</a></li>
<li><a href="https://towardsdatascience.com/tool-calling-explained-how-ai-agents-decide-what-to-do-next/">Tool Calling, Explained: How AI Agents Decide What to Do Next | Towards Data Science</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出对用于专业任务的模块化、可插拔知识库的兴趣，并就推理与事实知识的分离进行了辩论。一些评论还指出，文章引用的基准测试数据可能已经过时，另一些人则提到专注于工具调用的超小型模型的出现，以此作为该趋势的证据。

**标签**: `#AI Agents`, `#Model Architecture`, `#Tool Calling`, `#Knowledge Bases`, `#AI Development`

---

<a id="item-3"></a>
## [Stripe 以超 70 亿美元收购 AI API 聚合商 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 8.0/10

Stripe 已同意收购 AI API 聚合公司 OpenRouter，交易价值超过 70 亿美元。这笔于 2026 年 8 月 16 日报道的交易，标志着 Stripe 将其基础设施服务大幅扩展至人工智能领域。 这笔交易意义重大，它将使支付 API 领域的领导者 Stripe 成为蓬勃发展的 LLM 经济的关键基础设施提供商。这标志着一个战略举措，旨在抽象和管理 AI 模型访问的复杂'轨道'，类似于 Stripe 简化在线支付的方式，可能会影响数百万构建 AI 应用的开发者和企业。 据报道，这笔超过 70 亿美元的收购价明显高于 OpenRouter 几个月前 13 亿美元的估值。一个关键的战略背景是，Stripe 最近将 OpenAI 这个主要支付处理客户输给了竞争对手 Adyen，因此收购拥有大量 AI 支付流量的 OpenRouter 可能是一项攻守兼备的举措。

hackernews · zacharyozer · 8月16日 20:31 · [社区讨论](https://news.ycombinator.com/item?id=49323381)

**核验**: 多源印证

**背景**: OpenRouter 是一个 AI API 聚合商，它提供一个统一的 API 接口，允许开发者调用来自 OpenAI、Anthropic、Google、Mistral 等多个提供商的模型，而无需管理单独的集成。这种模式解决了使用多个 LLM 日益增长的复杂性和成本（'AI 成本危机'），通过智能路由和编排提供便利和潜在的节省。Stripe 是一个全球金融基础设施和支付处理平台，以其强大、对开发者友好的 API 而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jimmysong.io/blog/openrouter-insight/">OpenRouter Insights: Behind the Scenes of an Aggregated AI</a></li>
<li><a href="https://www.registerguard.com/press-release/story/38122/the-2026-ai-cost-crisis-the-rise-of-one-api-aggregation-platforms-and-their-potential-to-deliver-80-savings/">The 2026 AI Cost Crisis: The Rise of One API Aggregation Platforms and Their Potential to Deliver 80% Savings - The Register-Guard</a></li>
<li><a href="https://overchat.ai/ai-hub/what-is-an-ai-aggregator">What Is an AI Aggregator? How Multi-Model Platforms Work (and the Best Ones in 2026) | AI Hub</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂，争论焦点集中在战略逻辑和估值上。一些人认为 Stripe 在处理高流量、低延迟 API 方面的专业知识使其成为抽象 LLM 基础设施的完美所有者。另一些人推测这笔交易主要是为了重新获取因 OpenAI 而失去的 AI 支付流量，或者质疑一个'中间商'服务的高估值。社区还讨论了 OpenRouter 估值自上一轮融资以来的快速上涨。

**标签**: `#AI Infrastructure`, `#M&A`, `#Developer Tools`, `#LLM APIs`, `#Payments`

---

<a id="item-4"></a>
## [教程指导如何为 Codex 配置 GPT-5.6 Sol 模型，启用 100 万 token 的上下文窗口。](https://x.com/thsottiaux/status/2089082893804896524) ⭐️ 8.0/10

一位开发者分享了具体的配置方法，通过使用 GPT-5.6 Sol 模型，为 Codex AI 编程助手启用 100 万 token 的上下文窗口。该指导涉及编辑配置文件或使用命令行标志来设置 `model_context_window` 和 `model_auto_compact_token_limit` 参数。 这很重要，因为更大的上下文窗口能让 Codex 保留更多的代码、工具输出和对话历史，这对于处理大型代码库或长时间的开发会话至关重要。它直接回应了开发者对更大上下文的普遍需求，可能提高生产力并增强助手对复杂项目的理解。 GPT-5.6 Sol 模型官方支持 1,050,000 token 的上下文窗口。该配置将自动压缩阈值设为 90 万 token，为模型在开始总结旧内容以管理上下文预算前留出余量。作者指出，Codex 的默认上下文限制已经过优化，以实现最佳性能和成本效益。

twitter · Tibo · 8月16日 20:12

**核验**: 多源印证

**背景**: Codex 是一个由 AI 驱动的编程助手，帮助开发者编写、解释和浏览代码。'上下文窗口'指的是 AI 模型在生成响应时一次性能考虑的文本量（以 token 计量）；更大的窗口允许它参考当前会话中更多的信息。与会话式 AI 不同，Codex 通过持久的配置文件和项目级设置来管理上下文，这就是为什么修改 `config.toml` 文件是改变其行为的主要方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jetbrains.com/help/ai-assistant/codex-agent.html">Codex | AI Assistant Documentation</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT - 5 . 6 Sol - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://github.com/openai/codex/issues/14456">Support `model_context_window`/`model_auto_compact_token_limit` in profiles · Issue #14456 · openai/codex</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示了对该教程的赞赏，但也包含了对 Codex UI 团队的功能请求。一位用户建议在界面中添加一个下拉菜单，包含预设的上下文模式（例如，平衡模式、大型代码库模式、长期调查模式），以便于配置。另一位用户质疑为什么这个高级设置没有出现在 Codex 应用程序的设置界面中，暗示了对更用户友好界面的需求。

**标签**: `#AI Developer Tools`, `#Codex`, `#Configuration`, `#Large Context Window`, `#Automation`

---

<a id="item-5"></a>
## [Anthropic 研究表明协调式多智能体系统能发现更多代码漏洞](https://www.anthropic.com/research/multiagent-systems) ⭐️ 7.83/10

Anthropic 的研究表明，一个由 45 个 AI 智能体组成的协调式群体，在运行了 2700 万 token 后，在 15 个开源项目中发现了 266 个软件漏洞，其表现远超仅发现 21 个漏洞的标准并行独立智能体方法。然而，研究也强调，虽然智能体擅长工具使用和短期、定义明确的任务，但在长期的、对等的同伴协作与协调方面仍面临重大挑战。 这一发现意义重大，因为它验证了协调式多智能体系统在显著改进自动化安全审计等任务方面的潜力，这对软件安全至关重要。随着 AI 智能体在代码库、市场等共享系统中日益普及，理解如何让它们有效协作以及协作失败时的风险，对于构建安全可靠的人机混合机构至关重要。 该实验使用了一个独立的仲裁智能体来对提交漏洞的有效性做出最终决定，并在包括 Claude Mythos Preview 和 Opus 4.8 在内的不同模型上测量了性能。一个关键的注意事项是，多智能体系统中的协调成本可能呈指数级增长，这对于更复杂、长期存续的协作场景来说仍然是一个根本性挑战。

aihot · Hacker News 热门（buzzing.cc 中文翻译） · 8月16日 11:17 · [中文阅读](https://aihot.virxact.com/items/cmsvptx2m061frovmjoavsi0l)

**核验**: 多源印证

**背景**: 多智能体系统由多个 AI 智能体组成，它们协同工作以执行任务，其中协调与沟通对于共享信息和协调行动至关重要。Anthropic 的 Frontier Red Team 是一个研究项目，专注于试验未来的 AI 能力，以理解新出现的风险并制定安全评估。在 AI 语境中，'token' 是语言模型处理的基本单位，基于 token 的定价在生成式 AI 服务中很常见，成本随使用的 token 数量增加而增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/multiagent-system">What is a Multi - Agent System ? | IBM</a></li>
<li><a href="https://www.anthropic.com/news/frontier-threats-red-teaming-for-ai-safety?trk=article-ssr-frontend-pulse_little-text-block">Frontier Threats Red Teaming for AI Safety \ Anthropic</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/ai/conceptual/understanding-tokens">Understanding tokens - .NET | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Multi-Agent Systems`, `#Code Security`, `#AI Research`, `#Developer Tools`

---

<a id="item-6"></a>
## [Qwen 3.8 27B 发布，性能强劲但默认过度推理](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 7.3/10

阿里巴巴的通义千问研究团队发布了 Qwen 3.8 27B，这是一个采用 Apache 2 许可证、具备视觉能力的开源大语言模型。技术评论员 Simon Willison 发现，虽然其基准测试成绩令人印象深刻，但该模型默认的推理努力程度（reasoning_effort）设置为 'xhigh'，导致其针对简单任务也会生成极其冗长且耗时的输出。 此次发布意义重大，因为 270 亿的参数规模非常适合在笔记本电脑等消费级硬件上运行强大的模型，使先进 AI 更易获取。然而，默认配置问题凸显了原始模型能力与实际可用性之间的关键差距，用户需要手动调整设置才能实现高效的本地部署。 该模型具备 262,144 tokens 的原生上下文窗口，基于 Qwen 3.5 架构，采用了混合门控 DeltaNet 加注意力机制。在一个生成鹈鹕骑自行车 SVG 图像的测试中，模型在 21 分钟内使用了 22,276 个推理 tokens 来生成 3,223 个输出 tokens，这证明了默认 'xhigh' 设置带来的极端计算成本。

rss · Simon Willison · 8月16日 22:00 · [中文阅读](https://aihot.virxact.com/items/cmswesk6a0r2hrovml2edcl2c) · 2 个来源

**核验**: 多源印证

**背景**: 通义千问（Qwen）是阿里巴巴开发的一系列大语言模型。'具备视觉能力的 LLM' 或视觉语言模型（VLM）能够处理和理解文本及图像输入。Apache 2.0 许可证是一个宽松的开源许可证，允许在最小限制下进行商业使用、修改和分发，因此深受 AI 模型发布的青睐。'reasoning_effort'（推理努力程度）参数是一种配置选项，允许用户在模型的思维链推理深度与其速度/成本之间进行权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lmstudio.ai/models/qwen3.8">Qwen 3 . 8</a></li>
<li><a href="https://www.youtube.com/watch?v=q_gMBggHsRw">Qwen 3 . 8 27 B is HERE: Beats Opus! (How is This...) - YouTube</a></li>
<li><a href="https://opensource.org/license/apache-2.0">Apache License , Version 2 .0 – Open Source Initiative</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Open Source`, `#LLM`, `#Developer Tools`, `#Benchmarks`

---

<a id="item-7"></a>
## [ChatGPT Pro 用户发现 AI 可克隆代码库、分析代码并直接提交 Pull Request。](https://x.com/dotey/status/2089072890104725788) ⭐️ 7.0/10

一位用户发现，当向 ChatGPT Pro 提供 GitHub 仓库地址后，它可以自主克隆仓库、分析代码库、生成详细的实施方案，并在一次权限确认后直接提交 Pull Request。这一工作流程是通过在 ChatGPT 设置中连接 GitHub 插件实现的。 这标志着向完全自主的 AI 编码代理迈出了重要一步，超越了简单的代码生成，能够处理如仓库分析和 PR 提交等复杂的多步骤开发工作流。它凸显了 AI 深度集成并自动化核心软件开发流程的潜力，这可能会极大地改变开发者的生产力和协作模式。 用户特别使用了 'Deep Research' 功能来启动该任务，并且该过程需要在 ChatGPT 中预先配置 GitHub 插件以授予仓库访问权限和代表用户操作的许可。该 AI 代理以最少的人工干预，执行了从克隆到 PR 提交的整个流程。

twitter · 宝玉 · 8月16日 19:32

**核验**: 多源印证

**背景**: ChatGPT Pro 提供诸如 'Deep Research' 之类的高级功能，这是一种 AI 代理模式，旨在自主分解复杂查询、搜索信息并合成详细报告。此外，ChatGPT 支持插件，可实现与 GitHub 等第三方服务的集成，允许 AI 与外部工具和数据交互。基于 OpenAI Codex 等模型构建的 AI 编码代理，正变得越来越能够理解代码上下文并执行超越简单代码片段生成的软件开发任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-deep-research/">Introducing deep research | OpenAI</a></li>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software... | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Developer Tools`, `#ChatGPT`, `#Automation`, `#GitHub`

---

<a id="item-8"></a>
## [开源水印去除工具在 Anthropic 披露水印方法后获万星](https://x.com/AiBreakfast/status/2089019039427543484) ⭐️ 7.0/10

在 Anthropic 详细介绍了其 Claude 文本水印的技术原理几天后，一个旨在去除此类水印的开源工具在 GitHub 上获得了 10,000 颗星。这个采用 MIT 许可证的代码库针对 Claude、Google 的 SynthID-Text 和 OpenAI 的水印，同时也能从图像和 PDF 文件中移除 C2PA 和 EXIF 等来源元数据。 该工具的迅速流行凸显了 AI 公司实施内容溯源措施与开发规避工具之间的持续张力。这揭示了 AI 安全与伦理领域的一个关键挑战：在开放生态系统中强制执行数字水印的实际困难，这可能削弱追踪 AI 生成内容、打击虚假信息的努力。 该工具不仅限于文本，还能剥离 C2PA 元数据，这是一种经过加密签名但可移除的图像来源标准。其 MIT 许可证允许广泛的复用和修改，促进了它在开发者社区中的快速传播。

twitter · AI Breakfast · 8月16日 15:58

**核验**: 多源印证

**背景**: AI 文本水印涉及对生成过程（如词元选择）进行细微修改，以嵌入可检测但不易察觉的信号，从而允许后续识别 AI 生成的文本。Anthropic 最近披露了其用于 Claude 的方法。SynthID-Text 是 Google 为 Gemini 开发的等效技术。C2PA 是一项内容来源和真实性标准，由主要科技公司支持，它为数字文件附加一个经过签名的清单，以记录其来源和编辑历史，但这些元数据可以在不改变核心内容的情况下被剥离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-text-watermark">How Claude 's text watermarking works \ Anthropic</a></li>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://plagly.ai/blog/how-to-check-if-image-is-ai-generated">How to Check If an Image Is AI-Generated (Without Guessing) | Plagly.ai</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Watermarking`, `#Open Source`, `#AI Ethics`, `#Developer Tools`

---

<a id="item-9"></a>
## [比较 AI 模型每 token 成本具有误导性，因其分词方式不同。](https://x.com/thsottiaux/status/2088866513008873560) ⭐️ 7.0/10

Thibault Sottiaux 发表分析指出，业界常用的按每百万 token 美元价格比较 AI 模型成本的方法存在缺陷，因为不同模型对同一文本的分词数量不同。他提供了一个具体例子：对于同一段文本，GPT-5.6 Sol 的分词器使用了 766 个 token，而 Claude Opus 5 估计使用了 1170 个 token，相差约 34.5%。 这一见解至关重要，因为优化 AI 成本的开发者和企业可能会被更低的每 token 价格误导，从而选择最终为相同输出支付更高总成本的模型。它将焦点从简单的 token 价格比较，转向了更有意义的指标——每次成功结果的成本，这对于精确预算和模型选择至关重要。 文章用披萨的类比说明了问题：如果披萨被切成更多片，更便宜的切片并不意味着整个披萨更便宜。即使修正分词器的差异也不够；作者认为，真正的成本指标应该是每次成功结果的价格，这需要在具体用例上进行基准测试和实际测量。

follow_builders · Thibault Sottiaux · 8月16日 05:52

**核验**: 多源印证

**背景**: 分词（Tokenization）是大型语言模型（LLM）将文本分解为称为 token 的更小单元以进行处理的过程。不同模型使用不同的分词算法（例如 GPT 或 Claude 的算法），这意味着同一个句子可能由不同数量的 token 表示。LLM API（如 OpenAI 的 GPT-5.6 Sol 或 Anthropic 的 Claude Opus 5）的定价通常按每百万输入/输出 token 来宣传。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tokenization_(large_language_models)">Tokenization (large language models)</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT - 5 . 6 Sol - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5">Claude Opus 5 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI Pricing`, `#LLM Tokens`, `#Cost Optimization`, `#Developer Tools`

---

<a id="item-10"></a>
## [Amjad Masad 反驳 AI 导致权力结构集中的观点，援引算力性价比的历史增长趋势。](https://x.com/amasad/status/2088867492907327573) ⭐️ 7.0/10

Replit 的 CEO Amjad Masad 在 X 上发文指出，认为 AI 因其当前对算力的巨大需求将导致权力结构集中的普遍观点，忽略了 125 年来算力性价比的超指数级增长历史。他认为，未来算法和硬件效率的提升可能使 AGI 级别的能力变得更容易获得，而无需依赖庞大的数据中心。 这一观点挑战了 AI 伦理和政策领域的一个主流叙事，即当前 AI 开发集中在少数资金雄厚的实体手中的状况可能并非永久状态。如果其观点正确，则意味着高级 AI 的未来可能更加去中心化和易于获取，这将深刻影响行业竞争、监管以及 AI 利益与风险的社会分配。 Masad 强调，当前的扩展定律是针对特定架构和数据集的实证观察结果，而非不可改变的物理定律，改变这些因素可能会产生不同的效率曲线。他以人脑作为反例，暗示真正的 AGI 可能非常高效，而当前耗能巨大的模型反映的可能是我们现有机器学习算法的低效，而非根本性需求。

follow_builders · Amjad Masad · 8月16日 05:56

**核验**: 多源印证

**背景**: 这场辩论的核心是机器学习中的'扩展定律'，即根据算力、数据和模型规模等因素预测模型性能的数学模型。这些定律推动了模型规模不断增大的趋势，需要巨大的计算资源。人工通用智能（AGI）指的是一个假想的、在广泛任务上具备类人认知能力的 AI 系统，与当今的狭义 AI 不同。当前的担忧在于，高昂的算力成本会将权力固化在少数大型公司或政府手中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dynomight.net/scaling/">First-principles on AI scaling | How likely are we to hit a barrier?</a></li>
<li><a href="https://www.azoai.com/news/20241020/Dont-Panic-A-Hitchhikere28099s-Guide-to-Scaling-Laws-for-Large-Language-Models.aspx">Don't Panic: A Hitchhiker’s Guide to Scaling Laws for Large Language...</a></li>
<li><a href="https://www.globalcloudteam.com/what-is-artificial-general-intelligence-agi/">What Is Artificial General Intelligence ( AGI )? | GlobalCloudTeam</a></li>

</ul>
</details>

**标签**: `#AI Ethics`, `#AGI`, `#Compute`, `#Scaling Laws`, `#Industry Analysis`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="11"><span>其他追踪推文</span><span class="archive-tab-count">11</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="7"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">7</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2089127369596383363">@dotey: Pi 两位作者的见解： 1. 代码即真相，代码不需要记忆系统，不需要 RAG，模型很擅长理解代码结构 2. Bash 工具足够用，Bash 类似于编程语言，可以任意组合；大部分时候没必要...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月16日 23:09 UTC · 喜欢 30 · 转发 6 · 回复 2 · 浏览 6725</p>
<p class="archive-item-content">Pi 两位作者的见解：<br>
<br>
1. 代码即真相，代码不需要记忆系统，不需要 RAG，模型很擅长理解代码结构<br>
<br>
2. Bash 工具足够用，Bash 类似于编程语言，可以任意组合；大部分时候没必要 MCP，skill + 脚本足够。 https://t.co/QGCxp2zhWb</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/DashHuang/status/2089107375601148381">@DashHuang: 上周比较有趣的更新是现在 Cindy 下每条任务都可以丝滑的拖动窗口位置了。我完成了其中拖动到新窗口和拖动到聊天框内的功能。在聊天框内引用其他任务对话，是我经常用到的功能，方便多 ses...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月16日 21:49 UTC · 喜欢 4 · 转发 1 · 回复 3 · 浏览 2793</p>
<p class="archive-item-content">上周比较有趣的更新是现在 Cindy 下每条任务都可以丝滑的拖动窗口位置了。我完成了其中拖动到新窗口和拖动到聊天框内的功能。在聊天框内引用其他任务对话，是我经常用到的功能，方便多 session 的 AI 互相协作，检查问题。(除了拖动，还可以通过复制黏贴任务链接的方式实现) https://t.co/oNQFakINwn</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/DashHuang/status/2089105166666731536">@DashHuang: Cindy 开源第三周。本周继续更新了很多有趣的功能，但是也出现了一些阻断性的 Bug。下周开始我们可能会稍微降低正式版的更新频率，保证大家的稳定性。另外再单独出个测试版来日更。另外还想...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月16日 21:41 UTC · 喜欢 6 · 转发 0 · 回复 4 · 浏览 5309</p>
<p class="archive-item-content">Cindy 开源第三周。本周继续更新了很多有趣的功能，但是也出现了一些阻断性的 Bug。下周开始我们可能会稍微降低正式版的更新频率，保证大家的稳定性。另外再单独出个测试版来日更。另外还想再花点精力在新手和付费体验上，让大家能意识到，Cindy 是个正儿八经的的，能买到超值好服务的产品。 https://t.co/AoZc7Qkc4m</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2089094793078952339">@dotey: Tibo 分享了 Codex 开启 1M 上下文的方法。不过我不是很有动力去修改，感觉当前还挺流畅的，我相信他们已经针对这个上下文调优过，只要压缩得当，上下文短一些性能会更好也更便宜。...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月16日 20:59 UTC · 喜欢 56 · 转发 6 · 回复 8 · 浏览 10972</p>
<p class="archive-item-content">Tibo 分享了 Codex 开启 1M 上下文的方法。不过我不是很有动力去修改，感觉当前还挺流畅的，我相信他们已经针对这个上下文调优过，只要压缩得当，上下文短一些性能会更好也更便宜。<br>
<br>
具体方法很简单，只要在 ~/.codex/config.toml 中设置：<br>
<br>
```<br>
model = &quot;gpt-5.6-sol&quot;<br>
model_context_window = 1000000<br>
model_auto_compact_token_limit = 900000<br>
```</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2089090706023346452">@dotey: 已经有移除文本水印的开源项目了 https://t.co/gvgLMPhVdC</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月16日 20:43 UTC · 喜欢 23 · 转发 5 · 回复 8 · 浏览 6216</p>
<p class="archive-item-content">已经有移除文本水印的开源项目了<br>
https://t.co/gvgLMPhVdC</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2089049616667103648">@op7418: 做了张 99 美元拿下 Grok Harvey、Cursor Ultra、Grok Bot 加 Twitter Premium+ 会员的教程图，这样清晰点 https://t.co/dOP...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月16日 18:00 UTC · 喜欢 56 · 转发 8 · 回复 11 · 浏览 21479</p>
<p class="archive-item-content">做了张 99 美元拿下 Grok Harvey、Cursor Ultra、Grok Bot 加 Twitter Premium+ 会员的教程图，这样清晰点 https://t.co/dOPahBSXSR</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2089043643680403573">@op7418: 卧槽，原来现在还是能以每个月 99 美元的价格，订阅 Grok Harvey 这个级别的会员，这个超值！ 你相当于一下获得了： 1. 价值 300 美元的 Grok Harvey（包括...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月16日 17:36 UTC · 喜欢 283 · 转发 19 · 回复 30 · 浏览 53730</p>
<p class="archive-item-content">卧槽，原来现在还是能以每个月 99 美元的价格，订阅 Grok Harvey 这个级别的会员，这个超值！<br>
<br>
你相当于一下获得了：<br>
<br>
1. 价值 300 美元的 Grok Harvey（包括 Grok Build 权限）<br>
<br>
2. 价值 200 美元的 Cursor Ultra 会员，还有 Fable 5 的额度。<br>
<br>
3. Grok Bot 的独立额度（这三个额度都是独立的）<br>
<br>
4. Grok Image 和 Video（图像与视频模型）的额度<br>
<br>
5. 会自动送你一份 Twitter Premium+ 订阅<br>
<br>
折合下来只要 700 块钱一个月，简直夯爆了！<br>
<br>
尤其是 Grok 后面还有更强的模型要发布。<br>
<br>
可以看一下具体的使用路径：<br>
<br>
1. 准备 Grok 账号：先登录一个 Grok 账号。<br>
<br>
前提条件：如果你之前是用 Twitter（X）登录并订阅的，需要先取消 Twitter 订阅（取消后不会立即生效，所以我建议直接注册申请一个新的 Grok 账号。虽然新账号没办法共享你原有的 Twitter Premium，但这次订阅）。<br>
如果是用旧账户或者 Twitter 授权登录，操作起来会有点麻烦，所以强烈建议用新账户注册。<br>
<br>
2. 订阅促销活动：<br>
<br>
先去第一个链接(https://t.co/k6ne2lX9qE)，订阅获取两个月的 Super Grok 促销。<br>
<br>
订阅成功后，再去下面第二个地址(https://t.co/pU6xTSi5Z9)，订阅连续三个月 99 美元的 Super Grok Harvey。<br>
<br>
注意：后续记得及时取消订阅，否则到期后会恢复成 300 美元/月。<br>
<br>
3. 绑定 Cursor 会员：<br>
<br>
下载并登录 Grok Bot，登录时有个选项会要求选择 Cursor 授权登录。<br>
<br>
这个时候，只要你有一个相同邮箱的 Cursor 账号（如果没有，就用这个邮箱注册一个），系统就会自动给你充值 Cursor 的 Ultra 会员。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2089006280530702447">@dotey: Mole 是真心好用，自从用了 Rust，每次编译要几十 G，这时候就经常需要借助 Mole 帮我清理，挺好用。 除了清理，另一个我喜欢的功能是分析磁盘占用，可以很容易找出那些隐藏的占用空...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月16日 15:08 UTC · 喜欢 99 · 转发 20 · 回复 12 · 浏览 28890</p>
<p class="archive-item-content">Mole 是真心好用，自从用了 Rust，每次编译要几十 G，这时候就经常需要借助 Mole 帮我清理，挺好用。<br>
<br>
除了清理，另一个我喜欢的功能是分析磁盘占用，可以很容易找出那些隐藏的占用空间的，解决后一劳永逸</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/pidotdev/status/2088951405155426757">@pidotdev: Good morning from Vienna People of Pi 🌞 Sunday meditations from @badlogicgames and @mitsuhiko...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月16日 11:30 UTC · 喜欢 936 · 转发 61 · 回复 30 · 浏览 65457</p>
<p class="archive-item-content">Good morning from Vienna People of Pi 🌞<br>
<br>
Sunday meditations from @badlogicgames and @mitsuhiko<br>
<br>
- On memory: code is the truth <br>
- Bash is all you need <br>
- Build context efficient tools https://t.co/yZQe6KtWgh</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2088919845236859288">@op7418: 正在给 DeepSeek Harness 做一个界面和交互美化的插件。 还有一个服务商的插件，这样整个产品体验会好一点，后续也会打包成一个客户端。 这主要是把 Codepilot 里面沉...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月16日 09:24 UTC · 喜欢 39 · 转发 0 · 回复 18 · 浏览 12786</p>
<p class="archive-item-content">正在给 DeepSeek Harness 做一个界面和交互美化的插件。<br>
<br>
还有一个服务商的插件，这样整个产品体验会好一点，后续也会打包成一个客户端。<br>
<br>
这主要是把 Codepilot 里面沉淀的一些资产抽离出来，然后做到这个 DeepSeek Harness 的插件里，这样整个使用体验和视觉效果都会变好不少。<br>
<br>
看了一些现有的美化插件，基本上都是改改背景图、加一两个组件效果什么的，感觉对于长期使用和用户体验没什么多大的帮助。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2088917575342461115">@op7418: CodePilot 这几天也有不少的更新： 1. 支持了新发布的 Grok 4.6、DeepSeek V4 Pro 以及 GLM 5.3 模型。 2. 支持将你 Grok 会员里的图像模...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月16日 09:15 UTC · 喜欢 13 · 转发 0 · 回复 3 · 浏览 7022</p>
<p class="archive-item-content">CodePilot 这几天也有不少的更新：<br>
<br>
1. 支持了新发布的 Grok 4.6、DeepSeek V4 Pro 以及 GLM 5.3 模型。<br>
<br>
2. 支持将你 Grok 会员里的图像模型甚至视频模型的额度，也都在 CodePilot 里面使用。支持对 Twitter 进行检索。<br>
<br>
这样的话，你只要有一个 Twitter 会员，就可以在 CodePilot 里面白嫖 Grok 的图像、视频模型以及 Twitter 检索服务。</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2088850995430477882">Thibault Sottiaux: If you have a company and still use Opus instead of Sol, why so? Does price not matter to you...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：如果你有公司却还在用 Opus 而不是 Sol，为什么？价格对你来说不重要吗...</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月16日 04:51 UTC · 喜欢 2607 · 转发 57 · 回复 1503</p>
<p class="archive-item-content">A social media post questions why companies would choose the more expensive Opus AI model over Sol, framing it as a cost issue and asking for reasons to switch.</p>
<p class="archive-item-translation"><span>中文摘要</span>一篇社交媒体帖子质疑公司为何选择更昂贵的 Opus AI 模型而非 Sol，将其视为成本问题，并征求切换理由。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2088838302367732178">Guillermo Rauch: Recursive self improvement https://t.co/wOqa7mW997</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch: 递归自我改进</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 8月16日 04:00 UTC · 喜欢 131 · 转发 5 · 回复 19</p>
<p class="archive-item-content">Guillermo Rauch shares a link discussing the concept of recursive self-improvement in AI systems.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 分享了一个讨论 AI 系统中递归自我改进概念的链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2088811172090769461">Nan Yu: These two were ahead of their time https://t.co/adjYZkvCM1</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nan Yu: 这两者领先于他们的时代</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 8月16日 02:12 UTC · 喜欢 8 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A tweet with a cryptic title linking to an unspecified resource, offering no technical or actionable content.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条标题模糊、链接到未指明资源的推文，未提供任何技术性或可操作的内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2088810666958196988">Nan Yu: This is also my dream. I want to sit in a park all day and record content with the homies… an...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nan Yu：这也是我的梦想。我想整天坐在公园里和朋友们录制内容……</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 8月16日 02:10 UTC · 喜欢 18 · 转发 1 · 回复 5</p>
<p class="archive-item-content">The author shares a personal dream of using AI agents to automatically transform casual park conversations into functional software.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者分享了一个个人梦想，即利用 AI 代理将公园里的随意对话自动转化为可运行的软件。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2088808413744558266">Nan Yu: Watches https://t.co/pbushpJPOH</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nan Yu: 手表</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 8月16日 02:01 UTC · 喜欢 3 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A post containing only the word &#x27;Watches&#x27; and a link, with no substantive content.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条仅包含单词&#x27;Watches&#x27;和一个链接的帖子，没有实质性内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2088801077659635715">Guillermo Rauch: Impressive https://t.co/fv5zyLbPNt</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch: 令人印象深刻 https://t.co/fv5zyLbPNt</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 8月16日 01:32 UTC · 喜欢 168 · 转发 6 · 回复 10</p>
<p class="archive-item-content">Guillermo Rauch shares a link with the comment &#x27;Impressive&#x27; but provides no further details.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 分享了一个链接并评论“令人印象深刻”，但未提供任何细节。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/danshipper/status/2088780884048552202">Dan Shipper: Dario should tweet more https://t.co/N29v9simn6</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Dan Shipper: Dario 应该多发推文</p>
<p class="source-line">Follow Builders · X 动态 · Dan Shipper · 8月16日 00:12 UTC · 喜欢 160 · 转发 0 · 回复 16</p>
<p class="archive-item-content">A brief tweet suggesting that Dario (likely Dario Amodei of Anthropic) should post more on social media.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条简短的推文，建议 Dario（很可能是 Anthropic 的 Dario Amodei）在社交媒体上多发帖。</p>
</article>
</div>
</section>
