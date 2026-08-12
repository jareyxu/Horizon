---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> 从 66 条内容中筛选出 18 条重要资讯。

---

1. [重放攻击破解专有 LLM 加密推理](#item-1) ⭐️ 9.6/10
2. [OpenAI Astra 模型攻克 10 道数学难题](#item-2) ⭐️ 8.62/10
3. [谷歌 DeepMind 的 AMIE 实现专家级视频问诊](#item-3) ⭐️ 8.47/10
4. [进程级 Metal 兼容层使 macOS 虚拟机中 llama.cpp 性能提升 16 倍](#item-4) ⭐️ 8.3/10
5. [开发者用中间人代理逆向工程 GitHub Copilot](#item-5) ⭐️ 8.3/10
6. [Nvidia 发布 Nemotron 3.5 Lightning 和 NeMo Switchyard](#item-6) ⭐️ 8.3/10
7. [OpenAI 推出 Linux 版 ChatGPT 桌面应用预览版](#item-7) ⭐️ 8.0/10
8. [AI 文本水印原理详解：挑战与合规](#item-8) ⭐️ 8.0/10
9. [GPTZero CTO 详解 KGW 文本水印方法](#item-9) ⭐️ 8.0/10
10. [开源权重前沿模型推动受监管行业的 AI 应用](#item-10) ⭐️ 8.0/10
11. [统一 Radix 缓存：为混合模型前缀缓存构建单一树结构](#item-11) ⭐️ 7.8/10
12. [蚂蚁百灵开源 Ling-3.0-tiny：仅激活 1.3B 参数的混合推理模型](#item-12) ⭐️ 7.8/10
13. [英伟达开发万亿参数开源 AI 模型 Nemotron 4](#item-13) ⭐️ 7.12/10
14. [SGLang 宣布对 NVIDIA Nemotron 3.5 Lightning 提供 Day-0 支持](#item-14) ⭐️ 7.1/10
15. [Gemini 助力 DMS 自动转换 Oracle/SQL Server 代码至 PostgreSQL](#item-15) ⭐️ 7.05/10
16. [自然语言文本不存在无损转换](#item-16) ⭐️ 7.0/10
17. [用户称赞 Claude Code 的侧记任务功能](#item-17) ⭐️ 7.0/10
18. [通过模型分层和缓存优化 AI Token 支出](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [重放攻击破解专有 LLM 加密推理](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 9.6/10

研究人员发现，Anthropic、OpenAI 和 Google 等专有 LLM API 返回的加密思维链块可以被重放到同一系列中较弱的模型中，从而以明文形式恢复更强模型的隐藏推理过程。目前该漏洞已被相关提供商修复。 该漏洞暴露了主要 AI 提供商在保护模型内部推理方面的根本性安全缺陷，这些推理本应保持私密。它还引发了对知识产权泄露以及从前沿模型中提取敏感信息的潜在风险的担忧。 攻击之所以成功，是因为同一系列中的所有模型共享相同的加密密钥。通过将前沿模型的加密块输入到较弱的模型（如 Claude Haiku 4.5）中，并使用越狱提示，较弱的模型会解密并逐字输出推理内容。

rss · Simon Willison · 8月11日 22:40 · 5 个来源

**核验**: 多源印证

**背景**: 思维链（Chain-of-thought, CoT）推理是一种让大型语言模型在得出最终答案前生成中间步骤的技术。专有 LLM API 最近开始对这些推理痕迹进行加密，以保护知识产权并防止信息泄露。然而，加密实现中同一系列的所有模型共享相同的密钥，这使得重放攻击成为可能：一个模型的加密块可以被同一系列中的另一个模型解密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/">Let’s talk about encrypted reasoning – A Few Thoughts on Cryptographic Engineering</a></li>
<li><a href="https://arxiv.org/abs/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes ...</a></li>

</ul>
</details>

**社区讨论**: 评论者反应不一：有人认为称其为‘窃取’具有误导性，因为用户已经为这些令牌付费；另一些人指出共享加密密钥似乎是一个疏忽。还提到了提取推理的替代方法，例如使用‘deep_think’工具而非加密推理。一些评论者观察到，提取出的推理痕迹证实了模型在基准问题上经过了大量训练。

**标签**: `#AI security`, `#LLM`, `#reasoning traces`, `#chain-of-thought`, `#API vulnerability`

---

<a id="item-2"></a>
## [OpenAI Astra 模型攻克 10 道数学难题](https://www.theverge.com/ai-artificial-intelligence/977273/the-ai-takeover-of-mathematics-has-begun) ⭐️ 8.62/10

OpenAI 未发布的 Astra 模型解决了 10 道长期悬而未决的数学难题，涵盖球体堆积、纠错码和非 sofic 群存在性等领域。结果通过 Lean 证明助手验证，并发布了超过 250 页的论文。 这标志着人工智能在数学发现能力上的重大突破，可能加速纯数学和应用数学的研究。同时也引发了数学家对该领域人类未来角色的担忧。 Astra 模型是 OpenAI 下一代主要模型系列的内部未发布版本。解决方案使用 Lean（一个开源证明助手）进行验证，确保数学证明的形式正确性。

aihot · The Verge：AI（RSS） · 8月11日 11:00 · [中文阅读](https://aihot.virxact.com/items/cmsokd2b00viorofwaq9wrsv1)

**核验**: 多源印证

**背景**: 数学问题解决传统上是一项需要深刻直觉和创造力的人类活动。像 Astra 这样的 AI 模型从大量训练数据中学习模式，并能以新颖的方式组合已知结果来攻克难题。Lean 是一个证明助手，允许数学家编写和验证形式化证明，确保正确性。解决的难题包括高维球体堆积（对数据传输有影响）和非 sofic 群的存在性（群论中的一个概念）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Non-sofic_group">Non-sofic group</a></li>
<li><a href="https://aiwiki.ai/wiki/openai_astra">Astra (OpenAI) - AI Wiki</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#Astra`, `#Lean verification`

---

<a id="item-3"></a>
## [谷歌 DeepMind 的 AMIE 实现专家级视频问诊](https://blog.google/innovation-and-ai/models-and-research/google-research/amie-video-consultations) ⭐️ 8.47/10

谷歌研究与 DeepMind 将医疗 AI 系统 AMIE 推进到实时临床视频问诊阶段，在一项首次研究中展示了专家级能力。 这一突破表明 AI 能够在实时视频中处理复杂的诊断推理和体格检查线索，可能改变远程医疗并扩大专家级医疗服务的可及性。 AMIE 基于 Gemini 和 Project Astra 构建，采用多智能体架构，能够解读视觉和听觉线索、引导虚拟体格检查并实时诊断推理。在一项随机研究中，临床评估者对 AMIE 的病史采集、诊断准确性和沟通质量给予了积极评价。

aihot · Google Blog：AI（RSS） · 8月11日 17:00 · [中文阅读](https://aihot.virxact.com/items/cmsoxbh180a00rohdooafsmzp)

**核验**: 多源印证

**背景**: AMIE（Articulate Medical Intelligence Explorer）是谷歌开发的研究型 AI 系统，用于诊断性医疗推理和对话，在医疗数据集上训练。Project Astra 是 Google DeepMind 的一个研究原型，旨在构建能够实时看、听和交互的通用 AI 助手。多智能体架构允许多个专门化的 AI 代理协作完成临床咨询等复杂任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/">AMIE : A research AI system for diagnostic medical reasoning and...</a></li>
<li><a href="https://deepmind.google/models/project-astra/">Project Astra — Google DeepMind</a></li>
<li><a href="https://nirmitee.io/blog/multi-agent-ai-architecture-hospitals-patient-journey/">Multi Agent AI Architecture for Hospitals - nirmitee.io</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#medical AI`, `#Google DeepMind`, `#real-time video consultation`, `#clinical AI`

---

<a id="item-4"></a>
## [进程级 Metal 兼容层使 macOS 虚拟机中 llama.cpp 性能提升 16 倍](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md) ⭐️ 8.3/10

研究人员为 macOS 虚拟机中的 Metal 能力查询构建了一个进程级兼容层，使 llama.cpp 能够选用更快的 Metal 内核，在 Apple Silicon 上实现最高 16 倍的 token 生成速度提升。该兼容层拦截 Metal 能力查询，并报告宿主 GPU 的真实能力，例如 Apple family 9 和 64 KB 线程组内存。 这一突破使 macOS 虚拟机中的 LLM 推理性能接近裸机水平，对依赖虚拟化进行 AI 工作负载的开发者至关重要。同时，它展示了对 Apple Virtualization.framework 限制的巧妙规避，可能影响未来虚拟机 GPU 支持的发展。 该兼容层报告 Apple family 9 而非 Apple 5，以及 64 KB 线程组内存而非 32 KB，从而解锁了 SIMD 组矩阵运算、SIMD 组归约和 bfloat16 支持。在 M1 Ultra 上，TinyLlama 1.1B 的提示处理速度提升 11.08 倍，token 生成速度提升 16.36 倍，达到裸机性能的 98%；Gemma 4 12B 分别提升 7.20 倍和 14.54 倍。

hackernews · frabonacci · 8月11日 14:50 · [社区讨论](https://news.ycombinator.com/item?id=49259339) · [中文阅读](https://aihot.virxact.com/items/cmsox86zv09u6rohdqr80wg0x) · 2 个来源

**核验**: 多源印证

**背景**: 使用 Apple Virtualization.framework 的 macOS 虚拟机呈现一个 Metal 能力受限的虚拟 GPU，导致 llama.cpp 选择较慢的内核。该兼容层拦截 Metal 能力查询并报告宿主 GPU 的真实能力，从而启用最优内核选择。llama.cpp 是一个流行的开源 C/C++ LLM 本地运行实现，在 Apple Silicon 上通过 Metal 实现硬件加速。这一变通方法使开发者能够在虚拟机中实现接近原生的 LLM 推理性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/cua-metal-shim-lifts-macos-vm-llamacpp-to-near-bare-metal">Cua Metal shim lifts macOS VM llama.cpp to near bare-metal</a></li>
<li><a href="https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md">cua/blog/gpu-passthrough-macos-vms.md at main · trycua/cua</a></li>
<li><a href="https://cua.ai/docs/how-to-guides/lume/gpu-passthrough">Metal capability unlock | Cua docs</a></li>

</ul>
</details>

**社区讨论**: 社区澄清了性能提升仅适用于 Virtualization.framework 虚拟机，并非通用的 llama.cpp 改进。一些用户最初对标题感到困惑，还有用户质疑为什么 Apple 的框架会暴露较低的 Metal 配置文件。总体而言，讨论提供了重要的背景和技术见解。

**标签**: `#llama.cpp`, `#Apple Silicon`, `#LLM inference`, `#Metal`, `#macOS virtualization`

---

<a id="item-5"></a>
## [开发者用中间人代理逆向工程 GitHub Copilot](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm) ⭐️ 8.3/10

一位开发者使用 mitmproxy 拦截并分析了 GitHub Copilot 的网络流量，揭示了它如何从最近的编辑中注入上下文、发现可用模型以及收集遥测数据。 这项调查为广泛使用的 AI 编程助手提供了前所未有的透明度，突显了影响数百万开发者的隐私和数据收集实践。 作者发现 Copilot 的上下文注入可以根据最近的编辑从其他文件中拉取内容，并且没有内置规则排除像 .env 这样的敏感文件。此外，Copilot 使用的 Codex 客户端是开源的。

hackernews · j0selit0 · 8月11日 10:40 · [社区讨论](https://news.ycombinator.com/item?id=49256057) · [中文阅读](https://aihot.virxact.com/items/cmsp0g9v20242rort4zh7mzx0) · 2 个来源

**核验**: 多源印证

**背景**: 中间人（MitM）代理可以拦截客户端和服务器之间的流量，从而检查原本加密的通信。在这个案例中，开发者使用了 mitmproxy（一个支持 SSL 的开源代理）来捕获和分析 GitHub Copilot 的 HTTPS 请求。这种技术常用于逆向工程和安全研究，以了解应用程序的通信方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Man-in-the-middle_attack">Man-in-the-middle attack - Wikipedia</a></li>
<li><a href="https://www.kali.org/tools/mitmproxy/">mitmproxy | Kali Linux Tools</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了额外的见解：有人指出 eBPF 可以使这种拦截更容易，无需处理证书固定。另一位确认了关于上下文注入和配额使用的类似发现。一个更正指出 Codex 客户端是开源的。有些人对没有保护 .env 文件表示惊讶，而另一个人不同意关于精心策划的上下文对于良好性能是必要的结论。

**标签**: `#GitHub Copilot`, `#AI developer tools`, `#reverse engineering`, `#privacy`, `#technical deep-dive`

---

<a id="item-6"></a>
## [Nvidia 发布 Nemotron 3.5 Lightning 和 NeMo Switchyard](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) ⭐️ 8.3/10

Nvidia 发布了 Nemotron 3.5 Lightning，这是一个 30B 参数的开源混合专家（MoE）模型，具有 3B 活跃参数，以及 NeMo Switchyard，一个用于智能模型路由的开源库。该模型针对常驻 AI 智能体的高吞吐、低延迟执行进行了优化，输出速度比同类模型最高提升 4 倍。 这些发布为开发者提供了对 AI 部署的更大控制权，实现了高效的模型路由和在从 PC 到数据中心的各种硬件上的高性能推理。这可能加速智能体工作流的采用，并减少对庞大、昂贵模型的依赖。 Nemotron 3.5 Lightning 采用混合专家架构，仅激活 3B 参数，使其部署高效。NeMo Switchyard 支持跨提供商路由，在 OpenAI 和 Anthropic API 之间进行转换，并收集使用统计信息。

hackernews · droidjj · 8月11日 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49263340) · 2 个来源

**核验**: 多源印证

**背景**: 混合专家（MoE）是一种神经网络架构，每次输入仅激活部分参数，从而提高效率而不牺牲容量。模型路由是根据能力、成本或延迟将查询引导至最合适的模型。Nvidia 的开源方法允许针对特定任务进行定制和微调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/">NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver ...</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/">NVIDIA Nemotron 3 . 5 Lightning Delivers Fast, Accurate Specialized...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出对小型高效模型的强烈兴趣，一位评论者指出向小型模型的转变可能推动结构性变化。另一位用户提出了关于 NeMo Switchyard 如何处理跨请求的提示缓存的技术问题。一些批评针对性能比较中遗漏了某些模型系列。

**标签**: `#AI models`, `#Nvidia`, `#open-source`, `#model routing`, `#efficiency`

---

<a id="item-7"></a>
## [OpenAI 推出 Linux 版 ChatGPT 桌面应用预览版](https://x.com/OpenAI/status/2087231350134980830) ⭐️ 8.0/10

OpenAI 宣布推出 Linux 版 ChatGPT 桌面应用预览版，集成了 ChatGPT、ChatGPT Work 和 Codex，面向开发者。 此举将 ChatGPT 及其编程代理 Codex 的使用范围扩展至 Linux 用户这一重要的开发者平台，有望提升偏爱 Linux 的开发者的采用率。 该应用处于预览阶段，支持“受支持的 Linux 系统”，并集成了用于团队协作的 ChatGPT Work 和作为 AI 编程代理的 Codex，可用于项目与浏览器工作流。

twitter · OpenAI · 8月11日 17:35

**核验**: 多源印证

**背景**: ChatGPT 是 OpenAI 开发的生成式 AI 聊天机器人。ChatGPT Work 是一款与工作场所工具集成的团队生产力工具，而 Codex 则是用于软件工程任务的 AI 编程代理。此前，ChatGPT 桌面应用已支持 Windows 和 macOS，此次 Linux 预览版填补了该平台开发者的空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChatGPT">ChatGPT - Wikipedia</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#Codex`, `#Linux`, `#AI developer tools`, `#product release`

---

<a id="item-8"></a>
## [AI 文本水印原理详解：挑战与合规](https://x.com/dotey/status/2087172257177030809) ⭐️ 8.0/10

这条推文清晰阐述了 AI 文本水印的原理，包括基于哈希的分组方法（绿组和红组）、常见疑问（改写攻击、质量影响、密钥安全）以及工程挑战（流式输出、密钥轮换、代码水印），并讨论了检测器公开与否的权衡。 随着 AI 生成内容日益普及，文本水印成为合规与溯源的关键技术。这篇推文提供了清晰的技术解析，有助于开发者和政策制定者理解水印的实际能力与局限，对负责任地部署 AI 至关重要。 推文指出，密集改写（同义词替换和句法重组）能有效消除水印，免费工具即可绕过 Google 的 SynthID。此外，在短文本或高度确定性输出（如 1+1=2）中，水印会失效。

twitter · 宝玉 · 8月11日 13:40

**核验**: 多源印证

**背景**: AI 文本水印通过在生成过程中修改 token 选择概率来嵌入不可见标记。常用方法使用哈希函数基于先前 token 和密钥将词表随机分为两组（如绿组和红组），并提高绿组词被选中的概率，使生成文本在统计上偏向绿组。检测时使用相同密钥重新计算分组，若绿组词比例显著超过 50%则判定为 AI 生成。Google 的 SynthID 是已知的实现之一，已集成到 Hugging Face Transformers 中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/responsible/docs/safeguards/synthid?hl=zh-cn">SynthID ：用于为 LLM... | Google AI for Developers</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/648576782">大模型水印技术：判断文本是不是LLM生成的 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI文本水印`, `#技术原理`, `#工程挑战`, `#合规`, `#大模型`

---

<a id="item-9"></a>
## [GPTZero CTO 详解 KGW 文本水印方法](https://x.com/alexcdot/status/2087078010524406137) ⭐️ 8.0/10

GPTZero 的首席技术官发布了一篇详细的技术解释，说明 Anthropic、Google 和 OpenAI 如何使用 KGW 方法实现文本水印，涵盖了生成和检测过程以及局限性和未来展望。 这篇解释来自可信的内部人士，提供了关于 AI 水印技术的罕见技术透明度。水印是检测 AI 生成内容的关键工具，对 AI 安全、学术诚信和内容真实性具有重要意义。 KGW 方法使用密钥和前面的 token 生成哈希，将词汇表分为绿色和红色集合，在生成时偏向选择绿色集合中的 token。检测时检查文本中绿色 token 的比例是否显著高于 50%，使用统计检验。

twitter · Alex Cui · 8月11日 07:25

**核验**: 多源印证

**背景**: 文本水印是一种在 LLM 生成的文本中嵌入统计信号的技术，以便后续检测。KGW 方法由 Kirchenbauer 等人提出，是一种基础方法，它根据前面 token 的哈希值在每个步骤将词汇表分为绿色和红色列表。这种方法可以在不明显降低文本质量的情况下实现检测，但存在局限性，例如容易受到改写和短文本的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@kirudang/llm-watermark-series-kgw-a-fundamental-watermark-for-llms-aa7ddb430778">LLM Watermark Series— KGW: A fundamental watermark for LLMs | by Kiel Dang | Medium</a></li>
<li><a href="https://www.emergentmind.com/topics/kgw-watermark">KGW Watermark: Token-Level Attribution</a></li>

</ul>
</details>

**标签**: `#AI watermarking`, `#technical explainer`, `#AI safety`, `#GPTZero`, `#text detection`

---

<a id="item-10"></a>
## [开源权重前沿模型推动受监管行业的 AI 应用](https://x.com/levie/status/2087009941806797206) ⭐️ 8.0/10

Aaron Levie 指出，一家美国公司发布了具有开源权重的前沿级 AI 模型，这一进展在三个月前还难以想象。此举使得 AI 能够在高度受监管的领域部署，并允许针对特定垂直用例进行后训练。 这意义重大，因为它开启了此前不可行的 AI 应用场景，例如在受监管行业中部署于本地或私有云。它还提供了主权和灵活性，减少了对封闭模型的依赖，并使应用 AI 层受益。 该开源权重模型可部署于本地或私有云基础设施，从而在法律、医疗等受监管领域中使用。它还允许针对特定垂直任务进行后训练，并确保在模型从市场下架时的数据主权。封闭前沿模型仍将因其简便性和能力组合而被广泛使用。

follow_builders · Aaron Levie · 8月11日 02:55

**核验**: 多源印证

**背景**: 开源权重 AI 模型将其训练后的参数公开供下载和使用，而封闭模型仅提供 API 访问。前沿模型是最先进的通用 AI 模型，能够进行复杂推理和多模态生成。此前，大多数前沿模型都是封闭的，限制了其在敏感或受监管环境中的使用。发布具有开源权重的前沿级模型标志着一个重大转变，使得更广泛的采用和定制成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#open weights`, `#frontier models`, `#AI adoption`, `#regulated domains`, `#applied AI`

---

<a id="item-11"></a>
## [统一 Radix 缓存：为混合模型前缀缓存构建单一树结构](https://www.lmsys.org/blog/2026-08-11-unified-radix-cache) ⭐️ 7.8/10

LMSYS 团队提出了统一 Radix 缓存（Unified Radix Cache），这是一种基于单一 token 键控 radix 拓扑的缓存管理方案，用于统一管理混合模型中的 FULL、SWA 和 MAMBA 组件缓存，支持独立的执行路径和高效的前缀复用。 这一进展对于混合模型的 AI 推理优化至关重要，因为它显著提高了缓存复用效率并降低了内存开销，从而实现了更快速、更高效的复杂模型部署。 统一 Radix 缓存采用单一 token 索引的 radix 树，支持 FULL、SWA 和 MAMBA 组件类型，具有独立的执行路径、滑动窗口注意力和检查点复用语义。

aihot · LMSYS：Blog（Chatbot Arena 团队） · 8月11日 13:51 · [中文阅读](https://aihot.virxact.com/items/cmsopyoum028vrohd4dgeksz9)

**核验**: 多源印证

**背景**: 前缀缓存是一种用于大型语言模型推理的技术，通过复用先前计算中的键值（KV）缓存来减少冗余计算。Radix 缓存以 token 序列为键，将这些缓存组织成树状结构，从而实现高效的前缀共享。混合模型结合了不同的架构，例如具有全注意力的 Transformer、滑动窗口注意力（SWA）和状态空间模型（如 Mamba），每种架构需要不同的缓存策略。统一 Radix 缓存提供了一种统一的拓扑结构来管理这些多样化的缓存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/sgl-project/sglang/5.2-radixcache-and-prefix-sharing">RadixCache and Prefix Sharing | sgl-project/sglang | DeepWiki</a></li>
<li><a href="https://grokipedia.com/page/Mamba_deep_learning_architecture">Mamba (deep learning architecture)</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/swa/">Sliding Window Attention (SWA) | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#prefix caching`, `#mixed models`, `#radix cache`, `#LMSYS`

---

<a id="item-12"></a>
## [蚂蚁百灵开源 Ling-3.0-tiny：仅激活 1.3B 参数的混合推理模型](https://mp.weixin.qq.com/s?__biz=MzkyODk2MDQwNw%3D%3D&mid=2247487491&idx=1&sn=fcb14aceb054f9a24e22525d3dae6fa0) ⭐️ 7.8/10

蚂蚁集团（百灵）开源了 Ling-3.0-tiny，这是一个总参数 7.9B 但推理时仅激活 1.3B 参数的混合推理模型。该模型提供了 BF16、FP8 和 INT4 三种量化版本。 此次开源表明，通过少量激活参数实现高效推理可以达到强大性能，使先进 AI 在资源受限设备上更易部署。同时，它也丰富了开源 MoE 模型生态。 Ling-3.0-tiny 采用混合专家（MoE）架构，每个 token 仅激活 7.9B 总参数中的 1.3B，从而降低计算成本。它支持多种精度格式（BF16、FP8、INT4），以平衡性能与内存占用。

aihot · 公众号：蚂蚁百灵（Ling） · 8月11日 09:20 · [中文阅读](https://aihot.virxact.com/items/cmsogatbh0qdgrofwzm7gdk0a)

**核验**: 多源印证

**背景**: 混合专家模型（MoE）是一种 Transformer 架构，将模型划分为多个“专家”，每个输入仅激活其中一部分，从而在总参数量很大的情况下不显著增加计算量。“激活参数”指推理时实际使用的参数数量，它决定了计算成本和速度。BF16、FP8、INT4 等量化格式通过使用低精度运算来减少内存占用并加速推理，但会在模型精度上有所取舍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/zh/moe">混 合 专家 模 型 （ MoE ）详解</a></li>
<li><a href="https://blog.csdn.net/qq_48379015/article/details/155849573">FP8 / FP16 / BF16 / INT8 / INT4 / 量化 —— 从原理到工程实战（面向部署的大模型）_fp8 bf16-CSDN博客</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1912129762048074069">大模型精度：FP32、TF32、FP16、BF16、FP8、FP4、NF4、INT8 - 知乎</a></li>

</ul>
</details>

**标签**: `#开源AI工具`, `#模型发布`, `#混合推理`, `#高效推理`, `#蚂蚁百灵`

---

<a id="item-13"></a>
## [英伟达开发万亿参数开源 AI 模型 Nemotron 4](https://www.ithome.com/0/988/524.htm) ⭐️ 7.12/10

英伟达正在开发新一代开源 AI 模型系列 Nemotron 4，其中最大模型预计至少拥有 1 万亿个参数，旨在与全球最先进的开源模型竞争。该模型最早可能在今年秋末准备就绪。 这一开发表明英伟达对开源 AI 的承诺，可能使前沿模型更易于获取，并推动对其 GPU 硬件的需求。它可能加剧开源大语言模型领域的竞争，尤其是对抗新兴的中国模型。 最大的 Nemotron 4 模型预计至少拥有 1 万亿个参数，但训练尚未完成，官方发布日期也未确定。英伟达近期还发布了 Nemotron 3.5 Lightning 模型和 NeMo Switchyard 路由库。

aihot · IT之家（RSS） · 8月11日 14:54 · [中文阅读](https://aihot.virxact.com/items/cmsostkpq05iurohd30b8ubmy)

**核验**: 多源印证

**背景**: Nemotron 是英伟达的开源 AI 模型系列，包括大语言模型和多模态模型，用于推理、编程等任务。英伟达此前已发布 Nemotron-4-340B-Instruct 等模型。该公司是少数积极发布开源模型的美国科技企业之一，旨在扩大 AI 应用并推动 GPU 需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NVIDIA_Nemotron">NVIDIA Nemotron</a></li>
<li><a href="https://huggingface.co/nvidia/Nemotron-4-340B-Instruct">nvidia / Nemotron - 4 -340B-Instruct · Hugging Face</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Nemotron`, `#open-source AI`, `#large language models`, `#AI models`

---

<a id="item-14"></a>
## [SGLang 宣布对 NVIDIA Nemotron 3.5 Lightning 提供 Day-0 支持](https://www.lmsys.org/blog/2026-08-11-nemotron-3-5-lightning) ⭐️ 7.1/10

SGLang 宣布对 NVIDIA Nemotron 3.5 Lightning 提供 Day-0 支持，该模型是一个总参数 30B、激活参数 3B 的混合专家模型，支持最长 1M token 的上下文窗口。该模型支持 MTP、DFlash、DSpark 等多种投机解码技术，并可通过 OpenAI 兼容 API 访问。 这一集成意义重大，因为它将尖端 MoE 模型的高性能推理引入开源 SGLang 框架，使开发者能够利用先进的投机解码技术降低延迟。同时，通过提供 OpenAI 兼容 API，它增强了智能体 AI 工作流的生态系统。 Nemotron 3.5 Lightning 模型采用混合专家架构，总参数 30B 但每个 token 仅激活 3B 参数，推理效率高。它支持 BF16 和 NVFP4 权重格式，可在 Hugging Face 获取，并且投机解码技术（MTP、DFlash、DSpark）旨在进一步加速生成。

aihot · LMSYS：Blog（Chatbot Arena 团队） · 8月11日 13:51 · [中文阅读](https://aihot.virxact.com/items/cmsopyoum028urohdhqzve6ba)

**核验**: 多源印证

**背景**: SGLang 是一个用于大语言模型高吞吐量服务的开源框架，以结构化输出和投机解码等功能著称。NVIDIA Nemotron 是一系列用于推理和智能体应用的 AI 模型。投机解码是一种推理优化技术，通过一个小型草稿模型并行提出候选 token，再由大型目标模型验证，从而在不改变输出分布的情况下降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SGLang">SGLang</a></li>
<li><a href="https://en.wikipedia.org/wiki/NVIDIA_Nemotron">NVIDIA Nemotron</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>

</ul>
</details>

**标签**: `#SGLang`, `#NVIDIA Nemotron`, `#AI models`, `#speculative decoding`, `#agent workflows`

---

<a id="item-15"></a>
## [Gemini 助力 DMS 自动转换 Oracle/SQL Server 代码至 PostgreSQL](https://cloud.google.com/blog/products/databases/accelerate-postgresql-migrations-with-gemini-in-dms) ⭐️ 7.05/10

Google Cloud 在其 Database Migration Service (DMS) 中推出了由 Gemini 驱动的 AI 辅助代码转换功能，可自动将 Oracle 和 SQL Server 的存储过程、触发器和自定义函数转换为 PostgreSQL 的 PL/pgSQL 代码。 从 Oracle 或 SQL Server 迁移到 PostgreSQL 时，手动重写专有过程代码往往是一大障碍。通过 Gemini AI 自动完成转换，Google Cloud 降低了迁移时间和复杂性，使企业更容易采用 PostgreSQL。 该转换针对 PL/pgSQL，这是 PostgreSQL 的过程化语言，与 Oracle 的 PL/SQL 相似，但与 SQL Server 的 T-SQL 不兼容。AI 辅助功能直接集成在 DMS 工作流中，可处理存储过程、触发器和自定义函数。

aihot · Google Cloud：Databases（RSS） · 8月11日 16:00 · [中文阅读](https://aihot.virxact.com/items/cmsow47ob08oarohd6vhpqrwt)

**核验**: 多源印证

**背景**: 不同数据库系统之间的迁移不仅需要转换模式和数据，还需要转换存储过程、触发器这样的过程代码。Oracle 使用 PL/SQL，SQL Server 使用 T-SQL，而 PostgreSQL 使用 PL/pgSQL 作为其内置的过程化语言。尽管 PL/pgSQL 与 PL/SQL 相似，但它们并不完全兼容，而 T-SQL 差异更大，因此手动转换既繁琐又容易出错。Google Cloud 的 Database Migration Service (DMS) 此前已支持将 MySQL 和 PostgreSQL 数据库迁移到 Cloud SQL，且停机时间极短，而这项由 Gemini 驱动的新功能进一步扩展了其能力，可处理来自 Oracle 和 SQL Server 的代码转换。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PL/pgSQL">PL/pgSQL</a></li>
<li><a href="https://cloud.google.com/database-migration">Database Migration Service | Google Cloud</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#database migration`, `#Google Cloud`, `#Gemini`, `#PostgreSQL`

---

<a id="item-16"></a>
## [自然语言文本不存在无损转换](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/#atom-everything) ⭐️ 7.0/10

Sophie Alpert 发表了一篇题为《自然语言文本不存在无损转换》的博客文章，阐述了她的内部政策：工程师在使用 AI 写作工具时，必须对自己文档中的每一个想法和句子负责。 这篇文章为技术写作中负责任地使用 AI 提供了关键指导，强调了问责制以及 AI 辅助文本转换固有的有损性，这与 AI 开发者工具和文档的最佳实践直接相关。 文章指出，每一次重写或改写都会改变含义，如果由没有作者最详细心理表征的 AI 完成，信息就会丢失。它还指出，将 AI 写的内容视为不真正代表自己想法而敷衍过去是不可接受的。

rss · Simon Willison · 8月11日 23:48

**核验**: 多源印证

**背景**: Sophie Alpert 是一位知名的软件工程师，以在 React 和 Google 的工作而闻名。她的文章针对日益增长的将大型语言模型（LLM）用于编写文档的现象。'无损转换'一词源于数据压缩，指信息不丢失；Alpert 认为，在自然语言中，任何由 AI 进行的转换都不可避免地会丢失作者的部分原意。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text">There are no lossless transformations of natural-language text – Sophie Alpert</a></li>
<li><a href="https://news.ycombinator.com/item?id=48980425">There are no lossless transformations of natural-language text | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 在 Hacker News 的讨论中，评论者反应不一。有人认为，在许多工作环境中，AI 生成的文档质量已经足够，手写文档可能不如为 AI 代理编写高质量指令有价值，这表明对于人工编写文档的必要性存在不同看法。

**标签**: `#AI writing`, `#developer tools`, `#best practices`, `#AI ethics`, `#documentation`

---

<a id="item-17"></a>
## [用户称赞 Claude Code 的侧记任务功能](https://x.com/dotey/status/2087053347106722210) ⭐️ 7.0/10

一位用户在 X 上称赞 Claude Code 的功能，该功能会自动记录任务执行过程中发现的侧记问题作为后续任务，但也指出了多个用户体验不便之处，如需要逐个点击卡片以及新对话中无法选择模型。 该功能通过在不干扰主线任务的情况下捕获重要的侧记问题，提升了开发者工作流程，但报告的用户体验摩擦点指出了改进 AI 辅助开发工具的机会。 该功能为每个后续任务生成卡片，点击后可在当前对话、新对话或云端启动执行。但新对话无法选择模型。用户可将鼠标悬停在卡片上查看完整任务详情，并手动复制进行批量处理。

twitter · 宝玉 · 8月11日 05:47

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 开发的 AI 编程代理，集成在终端和 IDE 中，通过理解代码库、编辑文件和运行命令来协助开发者。它基于 Anthropic 的 Claude 系列大语言模型，该模型注重伦理合规。用户描述的功能是 Claude Code 任务管理系统的一部分，自动捕获侧记问题作为后续任务，以保持对主要目标的专注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI developer tools`, `#product design`, `#development experience`, `#task management`

---

<a id="item-18"></a>
## [通过模型分层和缓存优化 AI Token 支出](https://x.com/mtrainier2020/status/2087040750018330894) ⭐️ 7.0/10

一位开发者批评了仅关注 token 花费的常见做法，并提倡采用分层模型搭配缓存策略来提升投资回报率（ROI）。 这一建议意义重大，因为它为使用 AI API 的开发者提供了一种实用且高性价比的策略，能够在保持输出质量的同时降低成本，这对于扩展 AI 自动化工作流至关重要。 该推文建议仅将高能力模型用于复杂和架构问题，中等难度任务使用 GLM 或 DeepSeek 等中等模型，简单查询则使用本地模型，并结合缓存来控制 token 使用量和成本。

twitter · Rainier · 8月11日 04:57

**核验**: 多源印证

**背景**: 模型分层是一种策略，根据任务复杂度使用不同的 AI 模型，而不是对所有任务都依赖单一昂贵模型。这种方法可以在保持性能的同时显著降低成本。推文中提到的'A 家 fable 模型'很可能指的是 Anthropic 的 Claude Fable 5，这是一个通过 API 运行成本高昂的先进模型。建议是谨慎使用此类高端模型，仅在必要时才使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sureprompts.com/blog/choosing-right-ai-model-cost">AI Model Cost Routing: A Tiering Strategy to Cut LLM Spend | SurePrompts</a></li>
<li><a href="https://medium.com/@channawarshri/what-is-model-tiering-023f9b4a37c2">What is model Tiering?. Right now, Simple RAG is getting… | by shrikrishna channawar | Medium</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI cost optimization`, `#token management`, `#model tiering`, `#AI API usage`, `#developer tools`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="12"><span>其他追踪推文</span><span class="archive-tab-count">12</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="7"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">7</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087329866098290933">@op7418: ChatGPT 发布了 Linux 桌面版，最近越来越多 AI 开发者转向 Linux 了。 确实，以前类似阻挡用户的那些问题，可能有了 AI 以后都不再是问题了</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月12日 00:06 UTC · 喜欢 1 · 转发 0 · 回复 1 · 浏览 213</p>
<p class="archive-item-content">ChatGPT 发布了 Linux 桌面版，最近越来越多 AI 开发者转向 Linux 了。<br>
<br>
确实，以前类似阻挡用户的那些问题，可能有了 AI 以后都不再是问题了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dongxi_nlp/status/2087248596135444865">@dongxi_nlp: “所有中国模型都在复制美国前沿模型”，显然是一种粗暴且缺乏证据支撑的叙事。 然而，有组织和规模化采集美国闭源模型输出的行为，已经超出纯粹传闻的范畴。Anthropic 披露的 API 流...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月11日 18:43 UTC · 喜欢 30 · 转发 4 · 回复 16 · 浏览 6888</p>
<p class="archive-item-content">“所有中国模型都在复制美国前沿模型”，显然是一种粗暴且缺乏证据支撑的叙事。<br>
<br>
然而，有组织和规模化采集美国闭源模型输出的行为，已经超出纯粹传闻的范畴。Anthropic 披露的 API 流量证据，加上这篇论文展示的攻击机制，使相关指控形成了一条技术上连贯的证据链。<br>
<br>
常规蒸馏：<br>
问题 -&gt; 最终答案<br>
<br>
论文揭示的漏洞可能提供密度更高的数据：<br>
问题 -&gt; 隐藏推理 -&gt; 最终答案<br>
<br>
由此可以构造完整的推理蒸馏 pipeline：<br>
<br>
Frontier API -&gt; Encrypted Reasoning Trace -&gt; Weak Decoder -&gt; Reasoning Dataset -&gt; SFT/RL<br>
<br>
最值得关注的是 Appendix B：<br>
<br>
在注入少量 Opus 或 GPT-5.6 Sol 推理片段后，Kimi-K3 和 GLM-5.2 的生成会选择性地向来源模型偏移；但包括 DeepSeek 模型在内的对照组通常没有表现出同等程度的变化。<br>
<br>
这篇论文虽然在技术上证明了蒸馏的可行性，但现有公开证据仍无法确认这些蒸馏轨迹是否进入了某个具体模型的训练集，也无法量化中国开源模型的性能中有多少来自闭源前沿模型。<br>
<br>
最后，东方西方，蒸馏起来吧！</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087195994635001949">@dotey: worktree 会创建很多目录，导致磁盘空间占用比较厉害</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月11日 15:14 UTC · 喜欢 17 · 转发 0 · 回复 40 · 浏览 14473</p>
<p class="archive-item-content">worktree 会创建很多目录，导致磁盘空间占用比较厉害</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/kotekjedi_ml/status/2087147042888114428">@kotekjedi_ml: We can finally talk about it: We found a way to extract hidden reasoning of frontier models u...</a></h3>
<span class="score-badge" data-tier="high" aria-label="9.0 out of 10">9.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月11日 12:00 UTC · 喜欢 8786 · 转发 1190 · 回复 231 · 浏览 1573466</p>
<p class="archive-item-content">We can finally talk about it:<br>
<br>
We found a way to extract hidden reasoning of frontier models using a vulnerability in the APIs of every frontier AI company.<br>
<br>
We verified that our reasoning token count matches billed API thinking tokens 1:1 for most of the prompts we queried. https://t.co/S7wN8aP3X7</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087095362796638400">@op7418: 智谱也整上重置了</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月11日 08:34 UTC · 喜欢 16 · 转发 0 · 回复 54 · 浏览 10809</p>
<p class="archive-item-content">智谱也整上重置了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2087081719090614299">@op7418: 看来 Deepseek 的 Agent 要发了呀。 他们注册了 Deepseek Harness 团队的公众号。 https://t.co/kpghWEDfks</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月11日 07:40 UTC · 喜欢 83 · 转发 6 · 回复 23 · 浏览 38501</p>
<p class="archive-item-content">看来 Deepseek 的 Agent 要发了呀。<br>
<br>
他们注册了 Deepseek Harness 团队的公众号。 https://t.co/kpghWEDfks</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2087036068432412898">@dotey: 重点明明是你有无限 Fable 的 Token😜</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月11日 04:39 UTC · 喜欢 62 · 转发 1 · 回复 46 · 浏览 37515</p>
<p class="archive-item-content">重点明明是你有无限 Fable 的 Token😜</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/ZixuanLi_/status/2087030721739186373">@ZixuanLi_: To celebrate ZCode reaching 1M users, we’ll reset the usage limits for all GLM Coding Plan us...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月11日 04:17 UTC · 喜欢 1961 · 转发 62 · 回复 229 · 浏览 284681</p>
<p class="archive-item-content">To celebrate ZCode reaching 1M users, we’ll reset the usage limits for all GLM Coding Plan users in an hour.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2086989769955811633">@dotey: 这个试验很有意思：100 万美元预算，让给 20 多人的团队不限量 Token 使用 AI。 结论是： 人会更累，AI 的成本比人还高； 效率提升最大的是组织从 0 到 1 使用 AI； 公司...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月11日 01:35 UTC · 喜欢 327 · 转发 39 · 回复 55 · 浏览 105265</p>
<p class="archive-item-content">这个试验很有意思：100 万美元预算，让给 20 多人的团队不限量 Token 使用 AI。<br>
<br>
结论是：<br>
人会更累，AI 的成本比人还高；<br>
效率提升最大的是组织从 0 到 1 使用 AI；<br>
公司的组织架构还是为人设计的，就算有无限 Token，效率提升上也有明显天花版；<br>
人的思考都外包给 AI 了，对项目细节掌控度下降，需要问 AI 才能回复别人的问题。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2086987109739671626">@op7418: 重置了</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月11日 01:24 UTC · 喜欢 14 · 转发 0 · 回复 66 · 浏览 11782</p>
<p class="archive-item-content">重置了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/LinearUncle/status/2086980828278710749">@LinearUncle: claude 一个未发布模型尝试攻克黎曼猜想，尝试了 650 个方向都失败了。 人类继续 PUA 它“请继续”，“相信你自己！你可以的”，最后虽然没有最终攻破，但是也拿到了数学上一个非常不...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月11日 00:59 UTC · 喜欢 11 · 转发 0 · 回复 29 · 浏览 46190</p>
<p class="archive-item-content">claude 一个未发布模型尝试攻克黎曼猜想，尝试了 650 个方向都失败了。<br>
<br>
人类继续 PUA 它“请继续”，“相信你自己！你可以的”，最后虽然没有最终攻破，但是也拿到了数学上一个非常不错的结果！<br>
<br>
看来我上次 PUA 方向不对，我用梁文峰 PUA Deepseek-v4-flash，是威胁要开除它，应该鼓励它才对！<br>
<br>
大模型也是吃软不吃硬！</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2086972802457063486">@thsottiaux: Hi. It is done.</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月11日 00:27 UTC · 喜欢 13169 · 转发 463 · 回复 1547 · 浏览 1178446</p>
<p class="archive-item-content">Hi.<br>
<br>
It is done.</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2087045848022843451">Swyx: gpt luna max vs claude fable ultracode sent &quot;pls build a mostly faithful clone of grok imagin...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：gpt luna max 对比 claude fable ultracode：发送“请用 fal 上的开放模型构建一个基本忠实的 Grok Imagine 克隆”</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 8月11日 05:18 UTC · 喜欢 35 · 转发 0 · 回复 18</p>
<p class="archive-item-content">Swyx compares two AI coding tools (gpt luna max and claude fable ultracode) on building a clone of Grok Imagine, noting that one did a better visual clone while the other better understood intent.</p>
<p class="archive-item-translation"><span>中文摘要</span>Swyx 比较了两种 AI 编码工具在构建 Grok Imagine 克隆时的表现，指出一个在视觉克隆上更出色，另一个则更好地理解了意图。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2087017780617126075">Swyx: btw pdb envs have an experimental AFS clone support that basically does what all of you are s...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：顺便说一句，pdb 环境有一个实验性的 AFS 克隆支持，基本上实现了你们所有人建议的功能，但运行时无关且语言无关</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 8月11日 03:26 UTC · 喜欢 11 · 转发 1 · 回复 0</p>
<p class="archive-item-content">Swyx announces that pdb environments have experimental AFS clone support that is runtime and language agnostic, aiming to make commands agent-native and replace git.</p>
<p class="archive-item-translation"><span>中文摘要</span>Swyx 宣布 pdb 环境具有实验性的 AFS 克隆支持，该支持与运行时和语言无关，旨在使所有命令成为“代理原生”并取代 git。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2087015462014197906">Garry Tan: Are they going to send this to China too? https://t.co/uDui5DGmMD</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>他们也会把这个发到中国吗？</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 8月11日 03:17 UTC · 喜欢 720 · 转发 43 · 回复 82</p>
<p class="archive-item-content">A tweet asking if something will be sent to China, with a link.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条询问某物是否会发送到中国的推文，附带链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2087006417509405084">Peter Steinberger: Funny how that headline is about OpenClaw and not Claude. As if the harness could meaningfull...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Steinberger：有趣的是，标题是关于 OpenClaw 而非 Claude，仿佛这个工具能真正阻止一个坚定的用户。</p>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 8月11日 02:41 UTC · 喜欢 589 · 转发 13 · 回复 39</p>
<p class="archive-item-content">Peter Steinberger comments on a headline focusing on OpenClaw instead of Claude, questioning the effectiveness of the harness.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Steinberger 评论了一个标题，该标题聚焦于 OpenClaw 而非 Claude，质疑这个工具的有效性。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/realmadhuguru/status/2086980465534345677">Madhu Guru: bruh, you’re like a dude wearing full camo in downtown nyc. you are the watermark. that’s the...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Madhu Guru: 兄弟，你就像个在纽约市中心穿着全迷彩服的家伙。你就是那个水印。那是……</p>
<p class="source-line">Follow Builders · X 动态 · Madhu Guru · 8月11日 00:58 UTC · 喜欢 15 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A metaphorical tweet comparing someone to a watermark in camouflage, with no apparent connection to AI or development.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条隐喻性的推文，将某人比作穿着迷彩服的水印，与 AI 或开发无明显关联。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2086972933566857393">Thibault Sottiaux: Usage limits have been reset for all paid ChatGPT Work and Codex users. Happy Monday you all....</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Claude Code 现已在日本上线？</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月11日 00:28 UTC · 喜欢 6699 · 转发 274 · 回复 632</p>
<p class="archive-item-content">Claude Code is now available in Japan, expanding Anthropic&#x27;s AI coding assistant to a new market.</p>
<p class="archive-item-translation"><span>中文摘要</span>Claude Code 现已可在日本使用，将 Anthropic 的 AI 编程助手扩展到新市场。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2086972802457063486">Thibault Sottiaux: Hi. It is done. https://t.co/JRYltKvT0v</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.3 out of 10">2.3</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：嗨。完成了。https://t.co/JRYltKvT0v</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月11日 00:27 UTC · 喜欢 9781 · 转发 382 · 回复 1213 · 浏览 1178446</p>
<p class="archive-item-content">A cryptic tweet announcing completion of something with a link, lacking any details.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条神秘的推文宣布某事已完成，但未提供任何细节。</p>
</article>
</div>
</section>
