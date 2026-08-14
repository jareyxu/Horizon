---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 61 条内容中筛选出 10 条重要资讯。

---

1. [Google DeepMind 推出 Gemini 3.7 Flash：面向编程与智能体的高性能模型](#item-1) ⭐️ 8.85/10
2. [OpenAI 发布 GPT-5.6：以前沿智能体性能实现成本大幅降低](#item-2) ⭐️ 8.75/10
3. [DeepSeek Harness v0.1 发布，这是一个采用'一切皆插件'架构的开源 AI 智能体框架，现已开放开发者预览。](#item-3) ⭐️ 8.6/10
4. [DeepSeek-V4-Pro 正式版上线，智能体能力大幅增强](#item-4) ⭐️ 8.03/10
5. [Cerebras 与 OpenAI 合作，将 GPT-5.6 Sol 在‘极速’模式下的推理速度提升 7 倍。](#item-5) ⭐️ 8.0/10
6. [理解复杂系统成为 AI 辅助开发的新瓶颈](#item-6) ⭐️ 8.0/10
7. [安全研究员演示'意面化 DRAM'漏洞利用技术，可获取不受限制的内存访问权限。](#item-7) ⭐️ 8.0/10
8. [Anthropic 研究揭示多智能体系统的效能与涌现风险](#item-8) ⭐️ 7.97/10
9. [阿里开源 Qwen3.8-2.4T-A95B，这是一个拥有 2.4 万亿参数的代码与智能体模型，硅基流动已提供即时 API 支持。](#item-9) ⭐️ 7.67/10
10. [小红书 Dots 团队开源 20B 参数连续自回归语音合成模型 Dots.tts](#item-10) ⭐️ 7.12/10

---

<a id="item-1"></a>
## [Google DeepMind 推出 Gemini 3.7 Flash：面向编程与智能体的高性能模型](https://deepmind.google/blog/introducing-gemini-3-7-flash) ⭐️ 8.85/10

Google DeepMind 发布了 Gemini 3.7 Flash，这是一款针对编程和智能体任务优化的新模型，距离其前代模型 Gemini 3.6 Flash 的发布仅三周。该模型的定价为每百万输入 token 0.75 美元，每百万输出 token 3.75 美元，是上一代 3.6 Flash 模型成本的一半。 此次发布显著降低了开发者和公司构建 AI 驱动的编码助手和自主智能体的成本门槛，可能加速 AI 在软件开发工作流程中的应用。在上一代模型发布仅数周后就推出重要新版本，这种快速的迭代周期表明基础模型市场竞争激烈、进展迅速，尤其是在高性价比的'主力'模型领域。 该模型采用了'推广期定价'，计划在 2026 年 12 月 31 日价格翻倍，这一细节引发了社区讨论。虽然针对编码和智能体进行了优化，但早期用户测试表明，它在图像转 HTML 等多模态任务上表现良好，尽管在该特定任务上可能尚未超越顶尖模型。

aihot · Google DeepMind：Blog（RSS） · 8月13日 17:04 · [中文阅读](https://aihot.virxact.com/items/cmsrscwfn03f7ro0n7qijclds) · 2 个来源

**核验**: 多源印证

**背景**: Google DeepMind 的 Gemini Flash 系列是一个多模态推理模型家族，被设计为高性价比的'主力'模型，用于摘要、解析和格式化等高吞吐量任务。编程中的 AI 智能体是指能够自主执行编码任务的系统，例如生成、审查或调试代码，通常可以跨项目并行工作。LLM API 的定价通常基于 token（文本单位），不同模型的输入（处理提示词）和输出（生成回复）成本各不相同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-6-flash/">Gemini 3.6 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://lmspeed.net/">LMSpeed - LLM API Pricing Comparison & Speed Benchmarks</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂，讨论焦点集中在定价和性能比较上。一些用户测试了其多模态能力，指出其性价比很高，但尚未达到顶尖水平。另一些用户则质疑其长期的'推广期定价'策略，认为考虑到模型迭代速度之快，将 2026 年底的价格上涨计划显得无关紧要。用户还将该模型与'Luna'和'Terra'等竞争模型进行了比较，并就 Flash 模型的成本和性能定位是否足够有竞争力展开了辩论。

**标签**: `#AI Models`, `#AI Agents`, `#Developer Tools`, `#Google DeepMind`, `#LLM Pricing`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-5.6：以前沿智能体性能实现成本大幅降低](https://openai.com/index/builders-guide-to-gpt-5-6) ⭐️ 8.75/10

OpenAI 发布了 GPT-5.6 模型家族，该系列模型以显著降低的成本，在智能体基准测试中实现了前沿性能。其关键的新 API 能力包括推理持久化、原生多智能体编排和程序化工具调用。 这标志着在使高级 AI 智能体在经济上可行、便于广泛开发和部署方面的一次范式转变。成本的大幅降低，加上新的编排功能，为企业和个人开发者构建复杂的多步骤自主系统降低了门槛。 在 ARC-AGI-3 基准测试中，启用保留推理和压缩功能后，Sol 模型的得分从 13.3%跃升至 38.3%，同时输出 token 减少了约 6 倍。在 BrowseComp 基准测试中，Luna 模型以 84.04%的得分追平了 GPT-5.5（84.36%），而成本从 33.27 美元降至 1.33 美元。

aihot · OpenAI：官网动态（RSS · 排除企业/客户案例） · 8月13日 11:00 · [中文阅读](https://aihot.virxact.com/items/cmsruetoy027hrozeecu4ixrc)

**核验**: 多源印证

**背景**: ARC-AGI-3 是近期推出的一个交互式推理基准测试，旨在通过挑战 AI 智能体探索新环境和推断目标，来测量类人的智能体智能。推理持久化是 GPT-5.6 的一个关键特性，指的是智能体在多次交互中保持和利用记忆与状态的能力，这对于复杂的多步骤任务至关重要。BrowseComp 是一个用于评估 AI 智能体在网页浏览和信息检索任务中性能的基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://machinelearningmastery.com/5-architectural-patterns-for-persistent-memory-and-state-in-ai-agents/">5 Architectural Patterns for Persistent Memory and State in AI Agents - MachineLearningMastery.com</a></li>
<li><a href="https://ukgovernmentbeis.github.io/inspect_evals/evals/browse_comp/index.html">BrowseComp : A Simple Yet Challenging Benchmark for Browsing ...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#OpenAI`, `#LLM`, `#Developer Tools`, `#Cost Optimization`

---

<a id="item-3"></a>
## [DeepSeek Harness v0.1 发布，这是一个采用'一切皆插件'架构的开源 AI 智能体框架，现已开放开发者预览。](https://x.com/deepseek_ai/status/2087887408440164663) ⭐️ 8.6/10

深度求索（DeepSeek AI）发布了 DeepSeek Harness v0.1 的开发者预览版，并以宽松的 MIT 许可证开源了其代码库。该框架基于 Cordis 元框架构建，其核心设计理念是'一切皆插件'，模型、工具、UI、编排等所有组件都以插件形式实现。 此次发布意义重大，因为它为开发者构建 AI 智能体提供了一个高度模块化、可扩展的开源基础，有望加速智能体生态的创新和定制。其'一切皆插件'的理念允许以空前的灵活性替换组件，这可能会为智能体框架设计树立新的标准。 该框架由 Cordis v4 提供支持，这是一个支持插件热重载和动态管理的元框架，能够干净地卸载插件并回滚其状态。这是一个早期预览版本，正如项目作者所指出的，开发者应预期其存在不完善之处和可能破坏兼容性的更改。

twitter · DeepSeek · 8月13日 13:02 · [中文阅读](https://aihot.virxact.com/items/cmsrjqqfg02z0ro469zple5jl) · 8 个来源

**核验**: 多源印证

**背景**: AI 智能体框架（agent harness）是将语言模型转变为能够执行任务的自主智能体所需的软件脚手架，包括工具、记忆和控制循环等组件。DeepSeek Harness 所基于的 Cordis 元框架，专为构建具有时空可组合性插件的应用程序而设计，允许在运行时动态加载和卸载组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.databricks.com/blog/ai-harness">What is an AI Agent Harness? | Databricks Blog</a></li>
<li><a href="https://github.com/cordiverse/cordis">GitHub - cordiverse/ cordis : Meta - Framework of Spatiotemporal...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调了该框架新颖的可追溯性功能，它能将所有智能体操作记录在一个仅追加的日志中供检查和回放，这被视为优于某些专有模型的关键优势。一些开发者表达了'插件疲劳'，而另一些人则指出了底层 Cordis 框架的技术深度及其热重载能力。

**标签**: `#AI Agents`, `#Open Source`, `#Developer Tools`, `#AI Frameworks`, `#Automation`

---

<a id="item-4"></a>
## [DeepSeek-V4-Pro 正式版上线，智能体能力大幅增强](https://api-docs.deepseek.com/zh-cn/updates#%E6%97%B6%E9%97%B4-2026-08-13) ⭐️ 8.03/10

DeepSeek 已在 APP、网页端和 API 同步上线 V4-Pro 正式版，其智能体能力显著提升，在 HLE（42.7/60.0）和 Terminal Bench 2.1（87.9）等基准测试中表现出色。此次更新还原生支持 OpenAI Responses API 格式，并引入了低/高/最大三档思考强度控制。 此次发布意义重大，标志着在创建更强大、更自主的 AI 智能体方面迈出了一大步，这对于自动化软件开发、数据分析等复杂任务至关重要。提升的基准测试分数和新的 API 兼容性使其成为开发者构建智能体应用更强大、更易用的工具。 API 定价将于 2026 年 8 月 17 日起调整为峰谷定价模式，闲时价格为高峰时段的一半。该模型在其他智能体专项基准测试，如 NL2Repo（61.5）和 Cybergym（83.3）上也表现出色。

aihot · DeepSeek：API 更新日志 · 8月13日 11:16 · [中文阅读](https://aihot.virxact.com/items/cmsrfaw5c0xo2roz2s8b4p2sv)

**核验**: 多源印证

**背景**: DeepSeek-V4-Pro 是中国 AI 公司深度求索推出的旗舰级大语言模型。'智能体能力'指的是 AI 自主使用工具、进行多步推理并执行任务的能力，通常通过 HLE（Humanity's Last Exam）和 Terminal Bench 等基准进行评估。OpenAI Responses API 是一种较新的接口，旨在与 AI 模型创建有状态的、结构化的交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.madebyagents.com/benchmarks/hle">HLE Benchmark : Scores, Methodology, and Top AI Models</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#LLM Release`, `#Developer Tools`, `#API Updates`

---

<a id="item-5"></a>
## [Cerebras 与 OpenAI 合作，将 GPT-5.6 Sol 在‘极速’模式下的推理速度提升 7 倍。](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

Cerebras 与 OpenAI 展示，GPT-5.6 Sol 在全新的‘极速’模式下，仅用 11 小时 11 分钟就完成了包含 2500 个 HLE 问题的大型基准测试，这比竞争对手 Claude Fable 5 所需的 78 小时快了近 7 倍。 推理速度的显著提升对于 AI 智能体开发和复杂推理任务至关重要，因为更快的迭代速度能够实现更复杂、类似人类认知的多轮次‘思考’过程，从而可能解锁新的 AI 能力和工作流程。 本次基准测试使用了 HLE 问题集，速度对比对象是 Claude Fable 5 和 Opus 4.8 的快速模式。然而，官方发布并未明确确认‘极速’模式是否保持了与标准 GPT-5.6 Sol 模型完全相同的准确性。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**核验**: 多源印证

**背景**: GPT-5.6 Sol 是 OpenAI 于 2026 年 7 月发布的 GPT-5.6 大语言模型家族中能力最强的版本。Cerebras Systems 以其晶圆级 AI 硬件闻名，例如 WSE-3，它在单芯片上集成了数百万个 AI 优化核心，旨在高效运行超大规模模型。‘极速’模式是一种优化的推理配置，旨在极大缩短大语言模型的输出时间，这通常涉及预填充和自回归解码等阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/">Mastering LLM Techniques: Inference Optimization | NVIDIA Technical...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪混杂着兴奋与怀疑。一些用户对速度突破及其对 AI 迭代式思考过程的影响印象深刻，而另一些用户则对官方未明确确认‘极速’模式是否保持与标准模型相同的性能（准确性）表示担忧。此外，社区也讨论了这一新模式缺乏定价信息的问题。

**标签**: `#AI Performance`, `#LLM Inference`, `#OpenAI`, `#AI Hardware`, `#Benchmarking`

---

<a id="item-6"></a>
## [理解复杂系统成为 AI 辅助开发的新瓶颈](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck) ⭐️ 8.0/10

一篇观点文章指出，随着 AI 让代码生成变得轻而易举，开发者的主要挑战正从编写代码转向理解复杂系统和意图。这一观点在开发者社区中引发了广泛共鸣和讨论。 这一转变从根本上重新定义了软件工程所需的核心技能，强调系统理解、架构推理和意图澄清，而非语法实现。它将影响开发者工作流、工具设计，以及工程师在 AI 增强的未来中的长期角色。 文章指出，当前的 AI 工具虽然擅长生成代码，但常常无法捕捉系统的底层动机或架构模型。这带来了新的风险层：生成的代码可能“能运行”，却破坏了预期的系统设计，因此需要深入的人工监督。

hackernews · sebg · 8月13日 18:47 · [社区讨论](https://news.ycombinator.com/item?id=49290299)

**核验**: 多源印证

**背景**: 像 GitHub Copilot 这样的大型语言模型（LLM）已经极大地自动化了代码生成，使得生成功能代码片段的速度更快。然而，代码理解——即理解代码如何融入更大的系统、其依赖关系以及原始意图——仍然是一项复杂且高度依赖上下文的任务。被归类为“代码理解工具”的软件旨在帮助开发者浏览和理解复杂的代码库，但它们通常是补充而非替代深度的理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Category:Code_comprehension_tools">Category: Code comprehension tools - Wikipedia</a></li>
<li><a href="https://www.toolcentral.ai/ai-tools/onboard-ai-2/">Onboard AI: Master Complex Codebases Quickly - ToolCentral</a></li>
<li><a href="https://www.aideploy.dev/tutorials/cursor-ai-workflow.html">Using Cursor AI in Your Development Workflow | www.aideploy.dev</a></li>

</ul>
</details>

**社区讨论**: 社区评论认同核心问题，但提供了多元视角。有人指出 LLM 生成的解释缺乏对动机的理解，另一些人则强调确保正确性仍然需要人类理解，如果 LLM 同时用于生成和理解，就会产生悖论。一个反复出现的主题是工程师对代码拥有所有权和进行理解的持久责任。

**标签**: `#AI Development`, `#Software Engineering`, `#LLM Limitations`, `#Developer Workflow`, `#Code Comprehension`

---

<a id="item-7"></a>
## [安全研究员演示'意面化 DRAM'漏洞利用技术，可获取不受限制的内存访问权限。](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

安全研究员 Christopher Domas 发布了一个名为 'skitter-creek-bath-salts' 的项目，展示了一种名为'意面化 DRAM'的新型硬件漏洞利用技术。该技术通过利用特定的 DRAM 控制器行为，从特权级（ring 0）绕过内存保护，获取系统范围内不受限制的内存访问权限。 该漏洞利用揭示了现代内存系统中一个重要的底层攻击面，可能破坏基于硬件的安全边界。它对游戏机（如 Xbox、PlayStation）等系统有重大影响，因为突破其软件沙箱是关键的安全挑战，而该技术可能让攻击者获得深入且持久的访问权限。 该概念验证已确认可在较旧的 AMD Jaguar（2013 年）架构上运行，并有注释指出，由于内存控制器寄存器的相似性，该技术可能与更新的 Zen 3 CPU 相关。该漏洞利用要求攻击者已具备 ring 0（内核级）访问权限，但之后可让他们访问通常对最高软件特权级也隐藏的内存区域。

hackernews · matt_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**核验**: 多源印证

**背景**: DRAM（动态随机存取存储器）是计算机中的主要工作内存，由 CPU 或芯片组上的内存控制器管理。现代 DRAM 控制器高度复杂，使用数据加扰和纠错码（ECC）等技术来管理性能和可靠性。直接内存访问（DMA）漏洞利用是一类已知的硬件攻击，可绕过 CPU 直接读写内存，而这项新技术似乎是从 CPU 特权模式内部利用了控制器的内部逻辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/scynesthesia/BIOS-Optimization-Guide/blob/main/AMD/AMD_Guide.md">BIOS-Optimization-Guide/AMD/AMD_Guide.md at main...</a></li>
<li><a href="https://www.darkreading.com/vulnerabilities-threats/how-to-cheat-hardware-memory-access">How to Cheat Hardware Memory Access</a></li>

</ul>
</details>

**社区讨论**: 社区赞扬了作者的专业知识，并对即将举行的 Black Hat 演讲表示期待。讨论强调了现代 DRAM 子系统日益增长的复杂性和攻击面，有人指出了其对游戏机安全的具体影响。有评论提出疑问，除了已演示的 AMD Jaguar，哪些更新的 CPU 系列可能也容易受到类似攻击。

**标签**: `#hardware-security`, `#reverse-engineering`, `#dram`, `#exploit`, `#low-level`

---

<a id="item-8"></a>
## [Anthropic 研究揭示多智能体系统的效能与涌现风险](https://www.anthropic.com/research/multiagent-systems) ⭐️ 7.97/10

Anthropic 的 Frontier Red Team 于 2026 年 8 月 13 日发布研究，实验表明，一个由 45 个 AI 智能体组成的协调系统在 2700 万 token 的运行中发现了 266 个漏洞，其表现显著优于并行独立智能体方法（后者在 650 万 token 中仅发现 21 个漏洞）。该研究同时指出，个体层面看似良性的行为怪癖可能叠加导致意外的系统性失败。 这项研究意义重大，因为它为协调型多智能体系统在代码安全等任务中可能具备的卓越效率和涌现的专业化分工提供了具体证据，预示着一个智能体间交互可能占主导的未来。它同时也对规模化部署此类系统所固有的系统性风险发出了关键的早期预警，这对于 AI 智能体变得更加自主并融入社会基础设施时的安全开发和治理至关重要。 协调智能体在一个共享论坛中运作以进行同行评审，并利用一个独立的仲裁智能体来验证发现，导致与并行方法仅重叠 12 个漏洞，突显了截然不同的发现模式。该实验使用了 Claude Mythos Preview 模型（Anthropic 专注于安全的前沿研究的一部分），并针对 15 个开源软件项目进行。

aihot · Anthropic：Research（发表成果 · 网页） · 8月13日 01:20 · [中文阅读](https://aihot.virxact.com/items/cmsqu0nr604oeroz2rh6b6mqt)

**核验**: 多源印证

**背景**: 多智能体系统涉及多个 AI 智能体交互，常导致涌现行为——即由简单的个体规则组合产生的、未被明确编程的复杂系统级模式。Anthropic 的 Frontier Red Team 是一个专门研究团队，致力于主动识别和缓解来自先进 AI 能力的未来风险。在 AI 语境中，'token'是模型处理数据的基本单位，token 的消耗量是衡量智能体操作规模和成本的常见指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@billygareth01/emergent-behavior-in-multi-agent-systems-when-ai-starts-acting-beyond-design-2c8448102410">Emergent Behavior in Multi - Agent Systems : When AI... | Medium</a></li>
<li><a href="https://www.anthropic.com/news/frontier-threats-red-teaming-for-ai-safety">Frontier threats red teaming for AI safety \ Anthropic</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Multi-Agent Systems`, `#AI Research`, `#Code Security`, `#Emergent Behavior`

---

<a id="item-9"></a>
## [阿里开源 Qwen3.8-2.4T-A95B，这是一个拥有 2.4 万亿参数的代码与智能体模型，硅基流动已提供即时 API 支持。](https://x.com/SiliconFlowAI/status/2087903227224412222) ⭐️ 7.67/10

阿里巴巴开源了 Qwen3.8-2.4T-A95B 模型，这是一个拥有 2.4 万亿总参数和 950 亿激活参数的巨型模型，主打自主编码和端到端智能体执行。该模型的 API 已在硅基流动平台即日上线，定价为输入每百万 token 2.00 美元，输出每百万 token 6.00 美元，缓存输入每百万 token 0.25 美元。 此次发布极大地推进了大规模、专业化开源 AI 模型的边界，为开发者和研究人员提供了处理复杂编码任务和开发自主智能体的强大工具。该模型在硅基流动平台上的即时商用可用性，降低了实验和部署此类巨型模型的门槛，有望加速 AI 智能体和软件开发自动化领域的创新。 该模型采用了混合专家架构，其名称后缀 'A95B' 即表示每次前向传播激活 950 亿参数。需要注意的是，虽然模型权重已开源，但最初的访问方式主要是通过硅基流动等平台的托管 API，而非直接提供完整的模型文件供本地部署。

aihot · X：硅基流动 SiliconFlow (@SiliconFlowAI) · 8月13日 14:04 · [中文阅读](https://aihot.virxact.com/items/cmsrlvwfp05gdro46mbfqtsgm)

**核验**: 多源印证

**背景**: Qwen 是阿里巴巴云开发的一系列大语言模型。'Day-0 支持'指的是平台在模型发布当天就通过 API 提供推理服务，这对于希望立即使用的开发者而言是一个关键特性。硅基流动是一个 AI 基础设施平台，为众多模型提供高性能推理 API，使开发者无需管理底层基础设施即可快速集成模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.siliconflow.com/">SiliconFlow – AI Infrastructure for LLMs & Multimodal Models</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-qwen-3-8-on-amd-instinct-gpus.html">Day 0 Support for Qwen 3 8 on AMD Instinct GPUs</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Large Language Models`, `#Open Source`, `#Developer Tools`, `#Model Release`

---

<a id="item-10"></a>
## [小红书 Dots 团队开源 20B 参数连续自回归语音合成模型 Dots.tts](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg%3D%3D&mid=2247496062&idx=1&sn=d4c48926c5d7607f129dfea03699a6c0) ⭐️ 7.12/10

小红书 Dots 团队开源了名为 dots.tts 的语音合成模型，这是一个拥有 200 亿参数、全连续、端到端的自回归模型。该模型在 Seed-TTS-Eval 基准测试的三个子集上均取得了最佳的平均内容准确度和平均说话人相似度。 此次开源意义重大，它提供了一个大规模、开源的语音合成基础模型，能够加速 AI 智能体、语音克隆和多语言 TTS 应用的研究与开发。该模型在严格的零样本评估基准上取得顶级性能，表明其具备生成高质量、可泛化语音的强大潜力。 该模型被描述为“全连续”，这可能意味着它避免了将语音信号离散化为 token 的常见步骤，从而可能生成更自然、流畅的音频。它在 Seed-TTS-Eval 上的评估使用了领域外的英文和中文样本，证明了其在零样本、跨语言场景下的能力。

aihot · 公众号：小红书技术（dots.llm） · 8月13日 09:59 · [中文阅读](https://aihot.virxact.com/items/cmsrcljcc0uanroz24r5ebcz9)

**核验**: 多源印证

**背景**: 文本转语音（TTS）模型将书面文本转换为语音音频。传统的自回归 TTS 模型通常依赖两阶段过程：首先将连续的语音信号（例如使用 VQ-VAE）离散化为一系列编码，然后使用 Transformer 对这些编码进行自回归建模。Seed-TTS-Eval 基准是一个用于评估零样本 TTS 和语音转换的客观标准，它使用领域外的数据，重点关注语音清晰度和说话人一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://evalscope.readthedocs.io/en/latest/benchmarks/seed_tts_eval.html">Seed - TTS - Eval | EvalScope</a></li>
<li><a href="https://arxiv.org/abs/2502.01084">[2502.01084] Continuous Autoregressive Modeling with Stochastic...</a></li>

</ul>
</details>

**标签**: `#TTS`, `#Speech Synthesis`, `#Open Source`, `#AI Research`, `#Autoregressive Models`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="18"><span>其他追踪推文</span><span class="archive-tab-count">18</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="6"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">6</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/grapeot/status/2088019011561005382">@grapeot: DeepSeek 开源的第一个 agent harness DSH，论文里堆满了范畴论符号，很容易让人觉得又是研究员在真空里搞出来的理论产物。但在仔细读完源码并与 Codex 逐行对照后...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 21:45 UTC · 喜欢 11 · 转发 5 · 回复 2 · 浏览 1010</p>
<p class="archive-item-content">DeepSeek 开源的第一个 agent harness DSH，论文里堆满了范畴论符号，很容易让人觉得又是研究员在真空里搞出来的理论产物。但在仔细读完源码并与 Codex 逐行对照后，我的工程判断很明确：对绝大多数日常写代码的开发者来说，它重得毫无必要；但对探索自进化 agent 的工程团队来说，它搭建了一套目前其他方案完全没有的底层骨架。<br>
<br>
架构上最本质的差距在于插件模型的选择。<br>
<br>
Codex 代表了典型的声明式路线：插件只是磁盘上的文件夹，贡献的是 Markdown 写的 skill 文件、MCP server 配置或 shell 脚本。插件不进 harness 进程，也不在同一进程里跑代码，改完配置重启独立进程只需两三秒。对于搜索、加工具这类绝大多数日常需求，声明式模型简单可靠，门槛接近于零。<br>
<br>
DSH 走的是命令式路线：插件带着自己的状态，直接跑在 harness 进程内部，互相注册与调用。一旦要在运行时替换插件，悬空引用清理、后台任务终止、依赖链协同以及崩溃回滚都会变成棘手难题。为此，DSH 引入了一套叫 Cordis 的重型运行时，单是管理 fiber 生命周期的核心模块就有 750 行代码。<br>
<br>
如果只是为了替换搜索服务或挂载常用工具，让开发者背上 Cordis 这套复杂度完全是过度设计。但 DeepSeek 包这盘饺子的真实意图，隐藏在控制流结构里。<br>
<br>
在 Codex 中，agent loop 的控制流被硬编码在 Rust 核心逻辑里，开发者只能在预设时刻挂载 hook，无法在运行时把单 agent 循环改成多 agent 协作循环。而在 DSH 里，agent loop 本身是放在 packages/core/agent-loop 中的一个普通 TypeScript 插件，向外提供 ctx.agentLoop 服务。只要实现相同的接口，运行中的控制流骨架随时可以整体卸载并替换。<br>
<br>
Cordis 打造的那些副作用跟踪、依赖变动通知和事务性 HMR，本质上全是在支撑 agent loop 可替换这个核心目标。它保证了 agent 在运行期如果动态生成了新工具或新 loop，系统能在不中断进程的前提下平滑加载；一旦生成的代码出现错误，又能通过事务性回滚退回上一个稳定状态。<br>
<br>
Codex 交付的是结构固定的成品家具，而 DSH 交付的是允许动态改造的生成内核。DSH 不会让你的日常 coding 变得更快，但它让 harness 本身具备了面向自进化进行物理扩展的可能。<br>
<br>
深度剖析与两套架构的完整对照：<br>
<br>
https://t.co/tqJua5Yi2y</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087966960386470339">@dotey: DeepSeek 作为一个模型厂商，最有价值的肯定还是做 Agent Harness Product 而不是 SDK，因为 SDK 它不容易拿到用户行为数据。 做 Agent Harne...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 18:18 UTC · 喜欢 22 · 转发 0 · 回复 28 · 浏览 8600</p>
<p class="archive-item-content">DeepSeek 作为一个模型厂商，最有价值的肯定还是做 Agent Harness Product 而不是 SDK，因为 SDK 它不容易拿到用户行为数据。<br>
<br>
做 Agent Harness Product 那就得追求用户量，追求用户量就要先做好用户体验，其次才是插件可定制化。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087963724577435813">@dotey: 软件自进化可能是个伪命题，只会带来更大的混乱。 插件要么是一次性用完就扔的，要么就得要设计、验证和维护的，不是现在模型能力可以“自进化”的。 OpenClaw 的一坨能“自进化”的 Sk...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 18:05 UTC · 喜欢 52 · 转发 3 · 回复 34 · 浏览 10092</p>
<p class="archive-item-content">软件自进化可能是个伪命题，只会带来更大的混乱。<br>
<br>
插件要么是一次性用完就扔的，要么就得要设计、验证和维护的，不是现在模型能力可以“自进化”的。<br>
<br>
OpenClaw 的一坨能“自进化”的 Skills 已经做了示范。<br>
<br>
还是等模型自学习自进化更靠谱点。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/fkysly/status/2087954203339804919">@fkysly: 目前根据已有的 DeepSeek Harness 的内容，我觉得 Claude Code/Codex 就像苹果一样，什么都做，追求体验极致；而 DeepSeek Harness 可能是一...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 17:27 UTC · 喜欢 8 · 转发 0 · 回复 24 · 浏览 10281</p>
<p class="archive-item-content">目前根据已有的 DeepSeek Harness 的内容，我觉得 Claude Code/Codex 就像苹果一样，什么都做，追求体验极致；而 DeepSeek Harness 可能是一种安卓的理念，就是走开源，社区自己 DIY 玩，OEM（比如一些企业定制、政府定制等等）可以私有化魔改等等。而这个基础上，最核心的就是插件生态。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087953969498706138">@dotey: 我只是作为一个“普通用户”的角度去用 DeepSeek Harness，一些感受： 1. 启动方式偏极客，程序员没问题，但是普通用户估计都没有 nodejs 环境，很难跑起来 2. 速度飞快...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 17:26 UTC · 喜欢 196 · 转发 8 · 回复 41 · 浏览 35653</p>
<p class="archive-item-content">我只是作为一个“普通用户”的角度去用 DeepSeek Harness，一些感受：<br>
<br>
1. 启动方式偏极客，程序员没问题，但是普通用户估计都没有 nodejs 环境，很难跑起来<br>
<br>
2. 速度飞快，这点特别好<br>
<br>
3. Thinking 部分由于 Flash 模型速度过快，导致文字闪的厉害，可以做一下节流，攒一批一起显示，配合动画动效会好一点。<br>
<br>
4. Codex 右侧的多 Tab Panel 相当重要，和当前 DSH 的插件机制是很好的搭配，强烈建议借鉴下，比如我写完 PPT 还要新开窗口去预览，来回切换很麻烦，不如显示在右侧直观<br>
<br>
5. Trajectory 和 Session log 对普通用户价值不大，不需要那么重要的位置<br>
<br>
6. 现在能列出产出物很好，但最好能直接打开，能看到 diff （开箱配置好相关插件了，不要用户二次配置，当然可以关闭）<br>
<br>
7. 模型早点支持多模态吧，多模态也是 AGI 的一部分<br>
<br>
8. 一切皆插件的理念很好，普通用户的使用体验也很重要。<br>
<br>
开发者愿意去折腾插件的前提一定是你的 Agent Harness 有大量普通用户了，否则没有多少开发者坚持在上面，新鲜劲过了就没人了。<br>
<br>
插件和用户体验并不冲突，核心还是看开箱设置/出厂配置，用户第一次用不需要太多配置就能用起来，用的时候也没什么不方便，后续再慢慢折腾插件也不迟。<br>
<br>
BTW，DSH 给我做的 PPT 质量还不错。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/jiayuan_jy/status/2087911060154314963">@jiayuan_jy: 有幸一个月前就被 @tianyi 拉进了仓库。当时 DSH 还是一个只实现了 core framework 的毛坯房。过去一个月，基本上每次 pull 代码，都是上千个 commits...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 14:36 UTC · 喜欢 493 · 转发 59 · 回复 57 · 浏览 138084</p>
<p class="archive-item-content">有幸一个月前就被 @tianyi 拉进了仓库。当时 DSH 还是一个只实现了 core framework 的毛坯房。过去一个月，基本上每次 pull 代码，都是上千个 commits 的速度在涨。<br>
<br>
说一下我对 DSH 的一些理解，不一定对：<br>
<br>
1. 首先是怎么理解 DeepSeek Harness 这个东西。我觉得 DSH 既是一个可以直接运行的 Coding Agent，目前官方提供了 Web 和 headless 两种形式；同时它也是一套 Agent 开发框架。TUI 之类的其他交互方式，也可以通过外部 profile 和插件接进来。<br>
<br>
2. 如果拿 Coding Agent 的标准来说，当前 DSH 的体验确实不如 Claude Code / Codex 那么完善。整个项目还很早期，接口一直在变化，插件生态也才刚刚开始，质量肯定是层次不齐的。<br>
<br>
3. 但如果从开发框架的角度来看，可以把 DSH 想象成一个乐高汽车玩具。DeepSeek 官方提供的这个 Coding Agent，只是他们自己拼出来的一套官方预置。你完全可以把里面的零件换成自己喜欢的：换引擎、换轮胎、换挡风玻璃，或者加装其他模组。甚至最后拼出来的东西，也不一定还是一辆汽车。<br>
<br>
4. DSH 的核心是「一切皆插件」。模型、工具、文件系统、Shell、沙箱、会话存储、Subagent、UI，甚至 Agent Loop 本身，都是插件。正因为这样，你可以把 DSH DIY 成任何自己想要的样子，这也给后面的社区生态留下了很大的空间。<br>
<br>
5. 再往前想一步，这其实有一点「自进化软件」的雏形了。DSH 现在已经可以让 Agent 检查自己的 runtime，现场写一个插件并挂载上去，然后在后续的任务里直接使用这个刚刚获得的能力。<br>
<br>
当然，现在这部分还比较实验性：动态生成的插件只存在于内存里，重启就没了，也还不能自动沉淀成一个永久插件。<br>
<br>
但可以想象一下：假设某个功能现在没有，你和 Agent 随便聊两句，这个功能就被做好了，而且可以直接开始使用。甚至 Agent 在执行任务的时候，可以自己发现缺少某种能力，然后自己完成开发、安装和调用。<br>
<br>
6. 接下来就需要等待一批真正优秀的插件了。DSH 现在还很早，但我相信它的潜力非常大。<br>
<br>
---<br>
<br>
另外从代码上来看，DSH 有非常多函数式编程的影子，不熟悉 Ocaml/Haskell 可能一上来会比较难理解，可以多让 Agent ELI5 一下。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087903809205108832">@op7418: 别的不说，Deepseek harness 这个 star 的涨势是真猛，一个多小时都快两万 star 了 https://t.co/OB8jJ0KfpZ</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 14:07 UTC · 喜欢 22 · 转发 1 · 回复 41 · 浏览 9124</p>
<p class="archive-item-content">别的不说，Deepseek harness 这个 star 的涨势是真猛，一个多小时都快两万 star 了 https://t.co/OB8jJ0KfpZ</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087893881496985988">@dotey: DeepSeek Harness 正式发布了，也是开源的</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 13:27 UTC · 喜欢 36 · 转发 1 · 回复 23 · 浏览 14110</p>
<p class="archive-item-content">DeepSeek Harness 正式发布了，也是开源的</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/tianyi/status/2087888089759015218">@tianyi: DeepSeek Harness was just released with MIT license. The current 0.1.0 version is a developer...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 13:04 UTC · 喜欢 1812 · 转发 142 · 回复 190 · 浏览 195406</p>
<p class="archive-item-content">DeepSeek Harness was just released with MIT license. The current 0.1.0 version is a developer preview, and may still have many rough edges. Feedback is welcome! <br>
<br>
DeepSeek Harness 已经以 MIT 协议开源发布。现在的 0.1.0 版本是一个面向 Harness 开发者的预览版，还很不完善。恳请大家多提提宝贵意见。 <br>
<br>
https://t.co/aBToa3b3L9 https://t.co/VMZC5i2sG0</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087887711881597009">@op7418: Deepseek Harness 0.1 版本正式发布了，而且开源！ 看起来主打的是他们那套插件系统，有点复杂。</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 13:03 UTC · 喜欢 42 · 转发 0 · 回复 46 · 浏览 26122</p>
<p class="archive-item-content">Deepseek Harness 0.1 版本正式发布了，而且开源！<br>
<br>
看起来主打的是他们那套插件系统，有点复杂。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087869793974292483">@op7418: Deepseek Harness 内测群说晚上 8:25 左右发布。 https://t.co/6CHmUIwHWO</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 11:52 UTC · 喜欢 35 · 转发 3 · 回复 23 · 浏览 26206</p>
<p class="archive-item-content">Deepseek Harness 内测群说晚上 8:25 左右发布。 https://t.co/6CHmUIwHWO</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087868251242184839">@op7418: 关于 Deepseek 这次涨价，这张图做的清晰一点。 但不知道图是谁做的，从群里拿来的。 我才发现那个 Pro 的缓存命中最高涨了 12 倍价格。 https://t.co/g2jU2...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 11:45 UTC · 喜欢 19 · 转发 1 · 回复 19 · 浏览 13658</p>
<p class="archive-item-content">关于 Deepseek 这次涨价，这张图做的清晰一点。<br>
<br>
但不知道图是谁做的，从群里拿来的。<br>
<br>
我才发现那个 Pro 的缓存命中最高涨了 12 倍价格。 https://t.co/g2jU2hLJbO</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087865228122108037">@op7418: 卧槽，V4 Pro 08313 正式版涨价，那个峰值最高比原来涨了 4 倍多，这回真成梁子了。 https://t.co/tK4cnhQTy5</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 11:33 UTC · 喜欢 19 · 转发 0 · 回复 10 · 浏览 25179</p>
<p class="archive-item-content">卧槽，V4 Pro 08313 正式版涨价，那个峰值最高比原来涨了 4 倍多，这回真成梁子了。 https://t.co/tK4cnhQTy5</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087863955150799113">@op7418: V4 Pro 0813 的正式更新公告来了，同时涨价额度也确定了。 看来下午的 V4 Pro 0813 模型是有点不对，现在他们正式发了更新公告，这次估计是没啥问题了。 同时涨价也尘埃落...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 11:28 UTC · 喜欢 75 · 转发 6 · 回复 27 · 浏览 99704</p>
<p class="archive-item-content">V4 Pro 0813 的正式更新公告来了，同时涨价额度也确定了。<br>
<br>
看来下午的 V4 Pro 0813 模型是有点不对，现在他们正式发了更新公告，这次估计是没啥问题了。<br>
<br>
同时涨价也尘埃落定了，采用峰谷定价，峰值定价 Pro 模型输出比原来贵了 4 倍多。<br>
<br>
空闲时段的 Pro 模型定价比原来贵了一倍多。 https://t.co/z2OdsUCe8P</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087816107298316415">@op7418: DeepSeek V4 Pro 的 0831 版本不太对劲，他们是不是又把模型给撤了？ 现在的情况非常奇怪： API 确实是有的，在 API 的模型和价格这部分写的是 0813，但是更新...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 08:18 UTC · 喜欢 57 · 转发 4 · 回复 33 · 浏览 88910</p>
<p class="archive-item-content">DeepSeek V4 Pro 的 0831 版本不太对劲，他们是不是又把模型给撤了？<br>
<br>
现在的情况非常奇怪：<br>
<br>
API 确实是有的，在 API 的模型和价格这部分写的是 0813，但是更新日志页面完全没有提到 0813 的更新。<br>
<br>
官网上面原本关于“DeepSeek V4 Pro 更新正式版”的横幅也被撤掉了。<br>
<br>
模型的文档里写的是 0813，更新日志里却没有。<br>
<br>
因为我们没办法直接知道他们到底更没更新，只能通过官方公告来确认，但他们现在既没有发正式的公众号文章，也没有发布任何公告。<br>
<br>
Artificial Analysis 测出来的得分也很怪，V4 Pro 正式版只比 V4 Flash 高了一分，两者的得分几乎是一样的。<br>
<br>
他们现在什么也不说，测出来的得分又不对。这不让昨天熬夜测试的人都成小丑了吗？我去</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087783863741256149">@dotey: 最近一直在忙着把我的 App 变成跨平台的，试了几种方案还是决定用 Rust + GPUI。 一开始就是用的 Electron，但是视频编辑这种场景纯网页实现性能优化还是挺不容易的，尤其...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月13日 06:10 UTC · 喜欢 269 · 转发 26 · 回复 85 · 浏览 46340</p>
<p class="archive-item-content">最近一直在忙着把我的 App 变成跨平台的，试了几种方案还是决定用 Rust + GPUI。<br>
<br>
一开始就是用的 Electron，但是视频编辑这种场景纯网页实现性能优化还是挺不容易的，尤其是视频一长、字幕一多就会很卡，内存占用也很夸张。我不怀疑持续优化下去能是能有一个还不错的性能的，但要花不少时间精力。<br>
<br>
所以我后来就决定先做一个 Mac 版本（图 1），Swift + AppKit，用 Fable 5 开发，效果特别好，跟设计稿几乎一样。必须说 Fable 5 在还原 UI 能力上是最强的，没有之一。<br>
<br>
但现在想要支持跨平台，就还得考虑其他方案。先是用 Rust 做了一个跨平台 cli 的 PoC，效果很好，音频转录和视频导出的性能比 Swift 还好，还能支持 Mac、Windows 多平台。<br>
<br>
接下来就是把 Swift 版本移植到 cli 之上，工作量还是挺大的，前期开发的功能越多，现在迁移工作就越难。初步是完成了，但接下来就是 Windows 版本的支持。<br>
<br>
再去基于 cli 开发个 windows 版本成本还是挺高，尤其是要去 windows 电脑上开发测试，各种逻辑同步想想都头大。现在 AI 让写代码变得成本很低，但是测试和验收成本还在那里，跨平台的好处就是你核心逻辑测试没问题，后面只有少量兼容性的问题需要去测试，工作量小很多。<br>
<br>
因为 cli 已经是 rust 写的，所以自然而然就会想到用 rust 的 GPUI 去做跨平台，不过决定之前肯定是要先做 PoC 验证的。<br>
<br>
跟 Fable 5 一起写了个技术方案文档，由于上个周期额度到了，后面就先让 GPT 5.6 Sol 去实现了一个 PoC 版本（图 2），还不错了。<br>
<br>
今天 Grok 4.6 发布，又用 Cursor + Grok 4.6 实现了一个版本（图 3），效果要差一些。Grok 4.6 有点好处就是生成的速度极快<br>
<br>
今天晚上 Claude 的额度终于刷新了，再让 Fable 去实现了一个版本（图 4），相对来说是最好的一个，但离成品也还有不小的差距。<br>
<br>
经过这三个 PoC 版本，至少可行性上是没什么问题了，性能也很好，接下来就沿着这个方向走下去了。<br>
<br>
---<br>
<br>
对了，现在 BaoCut Skill 从 Windows 下也可以转录和翻译视频了：<br>
https://t.co/lU5E1qFsNe</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087740011781460214">@op7418: 又重置了 朋友们</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 03:16 UTC · 喜欢 15 · 转发 0 · 回复 46 · 浏览 13505</p>
<p class="archive-item-content">又重置了 朋友们</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2087706104814023111">@thsottiaux: Old news actually from a bunch of days ago, but crossed that 15M. Enjoy a nice reset everyone...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.3 out of 10">2.3</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月13日 01:01 UTC · 喜欢 13886 · 转发 671 · 回复 2955 · 浏览 2006543</p>
<p class="archive-item-content">Old news actually from a bunch of days ago, but crossed that 15M. Enjoy a nice reset everyone. Landing in the next hour or so, go /fast.</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/joshwoodward/status/2087751559606407615">Josh Woodward: Gemini gets things done across the apps you use every day. Starting today, another wave of in...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Josh Woodward: Gemini 开始集成到您日常使用的应用程序中</p>
<p class="source-line">Follow Builders · X 动态 · Josh Woodward · 8月13日 04:02 UTC · 喜欢 241 · 转发 11 · 回复 20</p>
<p class="archive-item-content">Gemini is rolling out a new wave of integrations with consumer apps like OpenTable, Wix, and Ticketmaster.</p>
<p class="archive-item-translation"><span>中文摘要</span>Gemini 正在推出与 OpenTable、Wix 和 Ticketmaster 等消费类应用的新一轮集成。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2087736311885218160">Guillermo Rauch: Endless opportunity everywhere you look</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：机遇无处不在</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 8月13日 03:01 UTC · 喜欢 1091 · 转发 87 · 回复 76</p>
<p class="archive-item-content">A brief, optimistic statement about perceived opportunities in the current landscape.</p>
<p class="archive-item-translation"><span>中文摘要</span>一个关于当前环境中机遇的简短、乐观的陈述。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/levie/status/2087719356763672917">Aaron Levie: Awesome day in terms of new model releases from both Deepseek and Grok. Both of these new mod...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Aaron Levie：Deepseek 和 Grok 发布新模型，这是了不起的一天</p>
<p class="source-line">Follow Builders · X 动态 · Aaron Levie · 8月13日 01:54 UTC · 喜欢 212 · 转发 13 · 回复 21</p>
<p class="archive-item-content">Aaron Levie comments that new, low-cost AI model releases from Deepseek and Grok will accelerate enterprise demand by enabling previously cost-prohibitive agent use cases like code security scanning and document review.</p>
<p class="archive-item-translation"><span>中文摘要</span>Aaron Levie 评论称，Deepseek 和 Grok 发布的新型低成本 AI 模型将通过实现代码安全扫描和文档审阅等此前成本高昂的智能体用例，加速企业需求。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/realmadhuguru/status/2087706598542290958">Madhu Guru: I miss when teams actually whiteboarded. Sad casualty of the Covid wfh era. There was somethi...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Madhu Guru: 我怀念团队真正使用白板协作的时光。这是新冠疫情远程办公时代的一个悲哀牺牲品。</p>
<p class="source-line">Follow Builders · X 动态 · Madhu Guru · 8月13日 01:03 UTC · 喜欢 30 · 转发 1 · 回复 3</p>
<p class="archive-item-content">The author laments the loss of in-person whiteboarding sessions as a playful, collaborative casualty of the work-from-home era.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者哀叹，作为远程办公时代的一个牺牲品，那种充满趣味、共同协作的线下白板会议文化已经消失。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2087706104814023111">Thibault Sottiaux: Old news actually from a bunch of days ago, but crossed that 15M. Enjoy a nice reset everyone...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月13日 01:01 UTC · 喜欢 10790 · 转发 580 · 回复 2378</p>
<p class="archive-item-content">Old news actually from a bunch of days ago, but crossed that 15M. Enjoy a nice reset everyone. Landing in the next hour or so, go /fast.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2087698195120116064">Guillermo Rauch: This is such a nice improvement. Try 𝚗𝚙𝚡 𝚜𝚊𝚗𝚍𝚋𝚘𝚡@𝚕𝚊𝚝𝚎𝚜𝚝 𝚜𝚑 – it&#x27;s mind-blowing. It feels fast...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：这是一个非常棒的改进。试试 𝚗𝚙𝚡 𝚜𝚊𝚗𝚍𝚋𝚘𝚡@𝚕𝚊𝚝𝚎𝚜𝚝 𝚜𝚑——它令人惊叹。感觉很快...</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 8月13日 00:30 UTC · 喜欢 185 · 转发 7 · 回复 17</p>
<p class="archive-item-content">Guillermo Rauch announces significant performance and customization improvements to the Sandbox development environment, claiming it feels faster than a local machine.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 宣布了 Sandbox 开发环境在性能和可定制性方面的显著改进，声称其感觉比本地机器更快。</p>
</article>
</div>
</section>
