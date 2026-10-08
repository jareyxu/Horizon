---
layout: default
title: "Horizon Summary: 2026-10-08 (ZH)"
date: 2026-10-08
lang: zh
---

> 从 70 条内容中筛选出 17 条重要资讯。

---

1. [OpenAI 发布 GPT-6，多模态升级但安全性能回退](#item-1) ⭐️ 10.0/10
2. [Anthropic 发布 Claude Haiku 5.5，降价并采用新 tokenizer](#item-2) ⭐️ 9.3/10
3. [Docker 开源代理编排工具](#item-3) ⭐️ 8.0/10
4. [Chrome 逆转决策，正式支持 JPEG XL](#item-4) ⭐️ 8.0/10
5. [研究质疑 OpenAI 对纳维-斯托克斯证明的 Lean 形式化](#item-5) ⭐️ 8.0/10
6. [OpenAI 用 Lean 证明 Barnette 猜想引发复杂情绪](#item-6) ⭐️ 8.0/10
7. [马斯克：SpaceX 将按任务选用最佳 AI 模型，包括 Claude Opus 5.5](#item-7) ⭐️ 8.0/10
8. [Nemotron 3 微调后在 IOI 与 IMO 2026 达到金牌水平](#item-8) ⭐️ 7.88/10
9. [NVIDIA 与微软推出 RTX Spark 平台，让 AI Agent 落地 Windows PC](#item-9) ⭐️ 7.85/10
10. [微软亚洲研究院开源 Agent Lightning v1.0，用于 Harness 强化学习训练](#item-10) ⭐️ 7.72/10
11. [OpenRouter 上线 GPT-6 Luna Decisions API，输出免费且速度更快](#item-11) ⭐️ 7.65/10
12. [Perplexity 开源多模态 late-interaction 嵌入模型](#item-12) ⭐️ 7.62/10
13. [LangChain 重构 Deep Agents 技能支持，新增工具绑定、固定技能与线程内重载](#item-13) ⭐️ 7.5/10
14. [Claude Code v2.1.293 新增 Haiku 5.5 并修复多项问题](#item-14) ⭐️ 7.3/10
15. [OpenAI Codex rust-v0.161.0 新增 GPT-6.1 Sol 默认模型、MCP 登录和语音设备选择](#item-15) ⭐️ 7.0/10
16. [AI 逆向工程或使所有软件开源化](#item-16) ⭐️ 7.0/10
17. [Peter Steinberger 将团队 AI 代理接入 X 以加速工作](#item-17) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6，多模态升级但安全性能回退](https://openai.com/index/gpt-6-for-everyone/) ⭐️ 10.0/10

OpenAI 发布了新一代旗舰 AI 模型 GPT-6，具备更强的多模态能力和安全考量，提供 Sol 和 Luna 两个版本。2026 年 10 月的更新整合了 Astra 的安全进展，并加强了对网络、生物和暴力等高危滥用的防护。 GPT-6 标志着 AI 能力的重大进步，对 AI 代理、开发者工具和产品设计具有深远影响。其发布可能重塑企业和开发者构建多模态应用的方式，而报告中的安全回退则凸显了在能力与负责任部署之间平衡的持续挑战。 系统卡显示，与 GPT-5.6 对应版本相比，GPT-6 Sol 在标准自残评估上出现统计显著回退，而 GPT-6 Luna 在自残、血腥和性内容上出现统计显著回退。GPT-6 Astra 在网络能力上达到 OpenAI 的“关键”阈值，意味着它能自主发现并利用此前未知的安全漏洞。

hackernews · joshuawright11 · 10月7日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49996425) · [中文阅读](https://aihot.news/items/uir31g728myjry383z17txvrw) · 5 个来源

**核验**: 多源印证

**背景**: GPT-6 是 OpenAI 最新的旗舰模型，接替 GPT-5.6 并整合了 Astra 项目的进展。多模态 AI 模型能够处理和生成文本、图像等多种数据类型，从而实现更丰富的交互。安全评估采用聚合方式，权衡改进与特定领域的回退。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deploymentsafety.openai.com/gpt-6-october">GPT-6 Sol and GPT-6 Luna: October 2026 update - OpenAI ...</a></li>
<li><a href="https://cdn.openai.com/pdf/gpt-6-october.pdf">GPT-6 Sol and GPT-6 Luna: October 2026 update - cdn.openai.com</a></li>
<li><a href="https://openai.com/index/safety-overview-gpt-6-astra/">Safety overview: GPT‑6 Astra - OpenAI</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：一些用户对模型生成交互式解释器的能力印象深刻，而另一些则批评 UI 设计并担忧安全回退。一位评论者强调了系统卡中关于自残和内容回退的发现，另一位则讨论了与 GPT 进行交互式学习的有效性。

**标签**: `#GPT-6`, `#OpenAI`, `#AI model release`, `#multimodal AI`, `#product design`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Haiku 5.5，降价并采用新 tokenizer](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/) ⭐️ 9.3/10

Anthropic 发布了 Claude Haiku 5.5，这是一款新的快速低成本模型，在 100,000 token 以内的提示词上，定价与 OpenAI 的 GPT-6 Luna 持平，为每百万 token $0.10/$0.50。该模型还采用了新的、更不慷慨的 tokenizer，与 Haiku 4.5 相比，token 使用量增加了约 1.25 倍。 此次发布大幅降低了开发者使用 Anthropic 模型的成本门槛，使 Haiku 5.5 在低成本 AI 模型市场上成为 GPT-6 Luna 的有力竞争者。新的 tokenizer 和定价结构可能会影响开发者设计提示词和管理成本的方式，尤其是在长上下文或基于代理的工作负载中。 对于超过 100,000 token 的提示词，Haiku 5.5 的价格将上涨 5 倍，达到每百万 token $0.50/$2.50，而 Luna 在 272,000 token 时的价格上涨仅为 $0.20/$0.75。该模型默认使用中等推理强度，且无法禁用推理，选项从低到最高；一次最高强度的 pelican SVG 生成耗时 5 分 9 秒，花费 3.3826 美分。

rss · Simon Willison · 10月7日 20:56 · 3 个来源

**核验**: 多源印证

**背景**: Tokenizer 是 AI 模型中的关键组件，它将原始文本转换为模型可以处理的数字 token ID。token 的数量直接影响 API 调用的成本，因为定价通常按每百万 token 计算。Claude Haiku 是 Anthropic 的快速低成本模型系列，专为高吞吐量和延迟敏感的应用设计，与 OpenAI 的 GPT-6 Luna 在同一类别中竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qianwenai.com/discover/what-is-tokenizer">Tokenizer ：文本到 模 型 输入 的 转换机制 - 千问 AI 平台</a></li>
<li><a href="https://huggingface.co/learn/llm-course/zh-CN/chapter2/4">Tokenizers · Hugging Face</a></li>
<li><a href="https://www.thinpa.com/ai-glossary/">AI 名词百科 | Token、Prompt、Context Window 解释 — THINPA</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了不寻常的定价结构，认为 100k token 的截止点对于基于代理的工作负载来说过低。一些用户赞赏为 Max 和 Team 订阅者提供的新的月度 API 积分，而另一些用户则指出 Haiku 5.5 在基准测试中表现良好，比 Haiku 4.5 便宜 9 倍，且准确率更高，但仍与 Luna 处于相似水平。

**标签**: `#AI模型`, `#Anthropic`, `#Claude Haiku`, `#模型发布`, `#价格对比`, `#技术分析`

---

<a id="item-3"></a>
## [Docker 开源代理编排工具](https://github.com/docker/docker-agent) ⭐️ 8.0/10

Docker 发布了一个名为 docker-agent 的开源项目，旨在无需编写代码即可创建和运行智能 AI 代理，以协作解决复杂问题。该项目托管在 GitHub 上，并引发了活跃的社区讨论。 此举标志着 Docker 进入 AI 代理编排领域，可能为管理 AI 工作流提供一种标准化的、容器原生的方式。它可能影响开发者在容器化环境中构建和部署多代理系统的方式。 该项目强调“无需代码”的方法，这引发了关于其价值的讨论，因为 AI 生成代码已变得容易。安全文档虽然存在，但一些用户发现难以找到，因此有人提供了沙箱配置的链接。该工具使用 Go 编写，与 Docker 现有的技术栈一致。

hackernews · saikatsg · 10月7日 17:48 · [社区讨论](https://news.ycombinator.com/item?id=49996259)

**核验**: 多源印证

**背景**: AI 代理是自主执行任务的软件程序，通常使用大型语言模型。编排是指协调多个代理共同解决复杂问题。Docker 提供容器化技术，将应用程序及其依赖打包，使其可移植且隔离。docker-agent 项目可能利用 Docker 的容器和沙箱能力来安全地运行代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.docker.com/">Docker | Secure Sandboxes for AI Agents</a></li>
<li><a href="https://www.linkedin.com/posts/awaiskhawar_docker-coding-agents-as-credential-surface-activity-7488314908271558656-NpOi">Docker Agent Security : Runtime Isolation Key to... | LinkedIn</a></li>
<li><a href="https://hugs4bugs.me/how-microvm-isolation-actually-secures-your-autonomous-agents/">How microVM Isolation Actually Secures your Autonomous Agents</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：有人称赞开源贡献和 Go 实现，也有人质疑“无需代码”的卖点，并将其与类似代理框架的泛滥进行比较。用户提出了安全担忧，并分享了沙箱文档的链接。此外，用户对 docker-agent 与 kagent、agent-sandbox 和 Cloudflare Sandboxes 等其他工具的区别感到困惑。

**标签**: `#AI agents`, `#Docker`, `#开源`, `#编排`, `#自动化工作流`

---

<a id="item-4"></a>
## [Chrome 逆转决策，正式支持 JPEG XL](https://developer.chrome.com/blog/jpeg-xl-in-chrome) ⭐️ 8.0/10

谷歌宣布 Chrome 现已原生支持 JPEG XL 图像格式，推翻了此前移除该功能的决定。这标志着浏览器支持的重大变化，Chrome 155 和 Firefox 157 均引入了对 JPEG XL 的原生支持。 这一逆转意义重大，因为 Chrome 此前的不支持是 JPEG XL 在网络上普及的主要障碍。如今 Chrome 和 Firefox 均已支持，JPEG XL 获得了多数浏览器的覆盖，可能加速其作为多功能、高效图像格式在网络上的应用。 Chrome 的支持包括从官方 libjxl 组织引入的内存安全 Rust 解码器 jxl-rs（2025 年 12 月）。虽然 JPEG XL 在有损压缩方面不一定总是优于 AVIF，但其优势在于极强的多功能性，支持有损和无损压缩以及渐进式解码。

hackernews · AshleysBrain · 10月7日 11:25 · [社区讨论](https://news.ycombinator.com/item?id=49991227)

**核验**: 多源印证

**背景**: JPEG XL 是由 JPEG 委员会、谷歌和 Cloudinary 开发的图像格式，旨在压缩效率和画质上超越 PNG、JPEG 和 WebP 等旧格式。它支持有损和无损压缩，并提供渐进式解码，即使数据部分加载也能快速显示图像。Chrome 曾在 2023 年移除 JPEG XL 支持，理由是生态系统采用不足，但社区压力和其技术优势促使其重新支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://jpegxl.info/">JPEG XL : Superior Image Compression</a></li>
<li><a href="https://www.neowin.net/news/google-chrome-155-brings-support-for-jpeg-xl-jxl/">Google Chrome 155 brings support for JPEG XL (.jxl) - Neowin</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，用户对 Chrome 重新支持表示兴奋，并指出 Firefox 很快将在稳定版中包含该功能，从而实现多数浏览器覆盖。一些用户讨论了 JPEG XL 与 AVIF 之间的权衡，另一些人则认为这标志着 WebP 的最终淘汰。还有用户提到了历史背景，包括之前关于 Chrome 移除该功能的 HN 讨论以及重新打开的问题。

**标签**: `#JPEG XL`, `#Chrome`, `#web standards`, `#image formats`, `#browser support`

---

<a id="item-5"></a>
## [研究质疑 OpenAI 对纳维-斯托克斯证明的 Lean 形式化](https://arxiv.org/abs/2610.08144) ⭐️ 8.0/10

一篇批判性分析论文认为，OpenAI 对纳维-斯托克斯证明的 Lean 形式化并未准确对应原始自然语言证明。作者特别声称，形式化的 Lean 证明与关于纳维-斯托克斯方程解爆破的自然语言证明并不匹配。 这项研究挑战了关于 LLM 辅助定理证明的重要 AI 声明，引发了对 AI 生成的正式证明是否真正捕获被形式化的数学论证的质疑。它还引发了关于 AI 辅助数学中形式化保真度和研究严谨性的实质性技术讨论。 该论文区分了 Lean 证明本身的正确性与自然语言证明和 Lean 形式化之间的等价性。评论者指出，自然语言本质上不如 Lean 精确，因此同一论证可能存在多种有效翻译。

hackernews · nill0 · 10月7日 15:24 · [社区讨论](https://news.ycombinator.com/item?id=49994145)

**核验**: 多源印证

**背景**: Lean 是一个开源证明助手和函数式编程语言，基于归纳构造演算，能够实现可由计算机检查的形式化证明。基于 LLM 的形式化是指将自然语言陈述和证明翻译为正式形式，这一任务因 OpenAI 尝试形式化克莱研究所千禧年大奖难题之一的纳维-斯托克斯爆破问题而备受关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant)</a></li>
<li><a href="https://lean-lang.org/">Lean Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_proof">Formal proof - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区意见存在分歧。一些评论者认为该论文的说法是对 OpenAI 成就的重大挑战，而另一些人则将其斥为'大量废话'，因为自然语言本质上不如 Lean 精确，允许多种有效翻译。一位评论者认为，如果 Lean 定理与克莱研究所原始问题陈述等价，则不匹配并无影响，建议验证工作应聚焦于这种等价性。

**标签**: `#AI agents`, `#theorem proving`, `#Lean`, `#Navier-Stokes`, `#LLM formalization`, `#research integrity`

---

<a id="item-6"></a>
## [OpenAI 用 Lean 证明 Barnette 猜想引发复杂情绪](https://simonwillison.net/2026/Oct/7/jake-boggan/) ⭐️ 8.0/10

OpenAI 的数学仓库中包含一个关于 Barnette 猜想的正式证明，这是一个图论中长期未解的问题，已在 Lean 证明助手中验证。该证明列在 openai/math GitHub 仓库的问题 180 中。 这标志着 AI 辅助数学研究的一个重要里程碑，表明 AI 能够处理纯数学中深层次的未解问题。同时，它也引发了关于人类数学家角色以及 AI 发现对那些为此投入多年的人的情感影响的深刻思考。 该证明在 Lean 中形式化，确保其逻辑正确性，但尚未经过同行评审或在传统数学期刊上发表。该仓库还包含 722 篇手稿，但只有一部分经过正式验证，且部分验证状态被标记为未检查。

rss · Simon Willison · 10月7日 04:47

**核验**: 多源印证

**背景**: Barnette 猜想由 David Barnette 提出，断言每个 3-连通二分立方平面图都有哈密顿回路。该猜想几十年来一直未解，仅有一些部分结果。Lean 是一个交互式定理证明器，允许数学家编写可机械检查的正式证明，提供高水平的确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Barnette's_conjecture">Barnette's conjecture - Wikipedia</a></li>
<li><a href="https://mathworld.wolfram.com/BarnettesConjecture.html">Barnette's Conjecture -- from Wolfram MathWorld</a></li>
<li><a href="https://github.com/openai/math">GitHub - openai / math · GitHub</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上 Jake Boggan 的评论，一位在猜想上花费了 24 年的图论爱好者，表达了悲伤和反思的复杂情绪，将这一消息比作听到前女友突然去世。这凸显了 AI 成就对人类研究者的情感冲击，讨论可能既包含对 AI 能力的惊叹，也包含对人类主导数学未来的担忧。

**标签**: `#AI数学证明`, `#图论`, `#OpenAI`, `#数学研究`, `#Hacker News`

---

<a id="item-7"></a>
## [马斯克：SpaceX 将按任务选用最佳 AI 模型，包括 Claude Opus 5.5](https://x.com/elonmusk/status/2107724314451878104) ⭐️ 8.0/10

埃隆·马斯克宣布，SpaceX 将采用多模型策略，针对每项任务使用最佳后端 AI 模型，包括 Claude Opus 5.5、MidJourney、Suno 等领先 API。这标志着从依赖单一专有模型（如 Grok）的转变。 这种务实的方法挑战了供应商锁定，并验证了多样化 AI API 在企业环境中的价值。它表明，即使拥有自家模型的公司也会优先考虑性能而非品牌忠诚度，可能影响行业采用趋势。 该公告特别提到了 Claude Opus 5.5、MidJourney 和 Suno 作为领先 API 的例子。马斯克的帖子获得了高互动（9.7 万点赞，7 千转发），表明人们对 AI 模型选择和企业采用有浓厚兴趣。

twitter · Elon Musk · 10月7日 06:46

**核验**: 多源印证

**背景**: Claude Opus 5.5 是 Anthropic 在 Claude 5.5 系列中的旗舰模型，以复杂推理能力著称。MidJourney 是领先的 AI 图像生成工具，Suno 是生成式 AI 音乐平台。此举反映了企业采用最佳 AI 解决方案而非绑定单一供应商的更广泛趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4.1">Claude Opus 4.1</a></li>
<li><a href="https://grokipedia.com/page/Claude_Opus_55">Claude Opus 5.5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Suno">Suno - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Midjourney,_Inc.">Midjourney, Inc.</a></li>

</ul>
</details>

**社区讨论**: 未提供社区评论，但高互动表明人们对多模型策略的优点及其对 AI 供应商竞争的影响进行了积极讨论。

**标签**: `#AI models`, `#Claude Opus`, `#multi-model strategy`, `#enterprise AI`, `#Elon Musk`

---

<a id="item-8"></a>
## [Nemotron 3 微调后在 IOI 与 IMO 2026 达到金牌水平](https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026) ⭐️ 7.88/10

NVIDIA Nemotron 团队报告，基于 Nemotron 3 基础模型，通过监督微调（SFT）、强化学习（RL）和反馈驱动推理构建的系统在 IOI 2026 与 IMO 2026 均达到金牌水平。IOI 系统得分 535.4/600，IMO 系统得分 30/42，双双超过官方金牌分数线。 这表明一个可适配的基础模型可以通过可复用的微调配方，专精于两个高难度领域：竞赛编程与奥林匹克数学。这一发现意味着无需从头训练新的基础模型，即可构建世界级专业 AI 系统，对 AI 研究与开发者工具生态具有重要参考价值。 IOI 结果是在与人类选手相同的时间、网络访问和提交限制条件下进行的非官方、无监督基准测试，未计入官方 IOI 排名；而 IMO 的证明则是由官方 IMO 阅卷人评分。团队整理了 2.2 万个题目并生成合成推理轨迹，发现 550B 参数的 Ultra 模型仅需一个 SFT epoch 就能在 IOI、ICPC 和 LiveCodeBench Pro 上全面超越完全后训练的 30B Nano 模型。

aihot · Hugging Face 社区博客（混合发现） · 10月7日 12:45 · [中文阅读](https://aihot.news/items/r96kyuxfie0w9mup4206gzn29)

**核验**: 多源印证

**背景**: 微调是一种后训练过程，通过带标签的示例（SFT）或奖励信号（RL）将预训练大语言模型适配到特定任务。IOI 考验在严格时间和提交限制下通过隐藏测试的算法编程能力，而 IMO 要求严密的自然语言数学证明。NVIDIA 的 Nemotron 3 系列包括 550B 总参数的 Ultra 和 30B 总参数的 Nano 等模型，基于 MoE 混合 Mamba-Transformer 架构构建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/topics/ai/nemotron">Nemotron AI Models | NVIDIA Developer</a></li>
<li><a href="https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/">NVIDIA Nemotron 3 Ultra</a></li>
<li><a href="https://korshunov.ai/en/article/32368-nemotron-achieves-gold-level-ioi-and-imo-results-via-fine-tuning/">Nemotron achieves gold-level IOI and IMO results via fine ...</a></li>

</ul>
</details>

**标签**: `#AI research`, `#NVIDIA`, `#Nemotron`, `#competitive programming`, `#mathematical reasoning`, `#RL`

---

<a id="item-9"></a>
## [NVIDIA 与微软推出 RTX Spark 平台，让 AI Agent 落地 Windows PC](https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event/) ⭐️ 7.85/10

NVIDIA 与微软在旧金山活动上联合发布了面向 Windows 笔记本和紧凑型台式机的 RTX Spark 平台——一款专为本地运行 AI Agent 设计的 Arm 架构超级芯片，同时宣布了 MXC（Microsoft Execution Containers），用于推动 AI Agent 在 Windows PC 上的部署与安全执行。 这项合作将本地 AI Agent 推理带到消费级 Windows PC，减少对云计算的依赖，同时改善延迟表现、隐私保护和离线能力。它为开发者提供了标准化的软硬件目标，便于构建和交付 Windows 原生 AI Agent，也巩固了两家公司在 Agentic AI 生态中的地位。 RTX Spark 将 20 核 Arm 架构 Grace CPU（与联发科联合设计）、配备 6144 个 CUDA 核心和第五代 Tensor Core 的 Blackwell RTX GPU，以及最高 128GB 的 LPDDR5X 统一内存集成于单颗 3nm 系统级芯片。该平台于 2026 年 5 月 31 日宣布，并于 2026 年 6 月 1 日在 GTC Taipei 正式发布，面向笔记本电脑和紧凑型台式机。

aihot · NVIDIA Blog（RSS） · 10月7日 18:45 · [中文阅读](https://aihot.news/items/t02toac3ii8mp1lxzl4blewdd)

**核验**: 多源印证

**背景**: RTX Spark 是 NVIDIA 面向 Windows 笔记本和紧凑型台式机开发的 Arm 架构系统级芯片计算平台，由 NVIDIA 与微软于 2026 年 5 月 31 日联合宣布。MXC（Microsoft Execution Containers）提供了安全且资源可控的跨平台 AI Agent 运行时，利用 Windows Job Object 的 CPU 速率控制等机制来调度 Agent 工作负载，使其在企业工作流中既强大又可控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_RTX_Spark">Nvidia RTX Spark - Wikipedia</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2045569000080406418">NVIDIA RTX Spark超级芯片：技术架构深度报告 - 知乎</a></li>
<li><a href="https://zhupite.com/sec/microsoft-execution-containers-ai-agents.html">深度解析 Microsoft Execution Containers（ MXC ）：跨平台 AI Agent ...</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#NVIDIA`, `#Microsoft`, `#Windows`, `#硬件`

---

<a id="item-10"></a>
## [微软亚洲研究院开源 Agent Lightning v1.0，用于 Harness 强化学习训练](https://www.microsoft.com/en-us/research/blog/agent-lightning-v1-0-a-3500-line-lightweight-agentic-rl-framework-for-training-agents-with-real-harnesses/) ⭐️ 7.72/10

微软亚洲研究院开源了 Agent Lightning v1.0，这是一个仅 3,500 行的轻量级框架，允许使用部署时相同的 agent harness 进行智能体强化学习（RL）训练，无需在训练框架内重写 agent。其编码 agent 流水线将 Qwen3.5-9B 在 SWE-bench Verified 上的得分从 41.8% 提升至 56.4%。 这解决了 agent 训练中的一个关键痛点：训练时与部署时 harness 的不匹配，这常常迫使开发者重写 agent 并导致性能下降。通过让部署时的 harness 直接参与 RL，Agent Lightning v1.0 有望加速生产级 AI agent 的开发，并提升其实际应用效果。 该框架相比原版进行了完全重建，并引入了“Harnessed Agentic RL”范式。它仅有 3,500 行代码，轻量易用，且在编码基准测试中展现了显著提升。

aihot · Microsoft Research 博客（RSS） · 10月7日 16:00 · [中文阅读](https://aihot.news/items/t9wypjd9cbb42ttuq7vrpp07l)

**核验**: 多源印证

**背景**: Agent harness 是将语言模型转化为 agent 的运行时脚手架，负责管理工具调用、对话状态和任务推进。传统的 RL 训练通常需要在训练框架内重写 agent，这可能导致训练与部署之间的不一致。Harnessed Agentic RL 直接将部署时的 harness 纳入 RL 循环，确保一致性并可能提升性能。这一方法是 agentic RL 更广泛趋势的一部分，其他工作如 Harness-1 和 Harness-RL 也体现了类似方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/agent-lightning-v1-0-a-3500-line-lightweight-agentic-rl-framework-for-training-agents-with-real-harnesses/">Agent Lightning v1.0: A 3,500-Line Lightweight Agentic RL Framework...</a></li>
<li><a href="https://www.brocker.org/microsoft-research-asia-agent-lightning-v1-training-ai-agents-real-harnesses">Microsoft releases Agent Lightning v 1 . 0 for agent training</a></li>
<li><a href="https://jacar.es/en/agent-lightning-microsoft-rl-agents/">Agent Lightning : RL for agents without a rewrite</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#reinforcement learning`, `#open source`, `#Microsoft Research`, `#agentic RL`

---

<a id="item-11"></a>
## [OpenRouter 上线 GPT-6 Luna Decisions API，输出免费且速度更快](https://x.com/OpenRouter/status/2107929204142874759) ⭐️ 7.65/10

OpenRouter 已在平台上新增 OpenAI 的 GPT-6 Luna Decisions API，使开发者能够进行结构化决策并获得带概率的类型化输出。该 API 定价为每百万输入 token 0.10 美元，输出免费，并声称比通过 Responses API 使用 GPT-6 Luna 快最多 10 倍。 此次发布为开发者提供了一个高性价比、高速的决策任务选项，可能提升需要分类、路由或动作选择的应用效率。同时，它也扩展了 OpenRouter 的模型库，巩固了其作为多样化 AI 模型统一入口的地位。 该 API 支持文本、JSON 和图像输入，返回带概率的类型化答案，并具有 1M token 的上下文窗口。速度声明基于 OpenAI 开发者账号，且该模型目前处于预览状态。

aihot · X：OpenRouter (@OpenRouter) · 10月7日 20:21 · [中文阅读](https://aihot.news/items/x40bi9csoomsdaflejehop22y)

**核验**: 多源印证

**背景**: OpenAI 的 Decisions API 专为实时决策设计，将模型智能聚焦于一组有限的预定义答案。开发者可用它来分类内容、路由请求或选择代理的下一步动作，为自由文本生成提供了更结构化的替代方案。OpenRouter 是一个 AI 模型聚合器，通过统一 API 提供来自多家提供商的数百种模型，使开发者能够通过单一界面比较和使用它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/decisions">Decisions | OpenAI API</a></li>
<li><a href="https://vercel.com/i/what-is-openai-decisions-api">What is OpenAI's Decisions API? - Vercel</a></li>
<li><a href="https://openai.com/index/devday-2026-recap/">DevDay 2026 Recap - OpenAI</a></li>
<li><a href="https://openrouter.ai/models">Compare AI Models : Pricing , Context & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI API`, `#OpenAI`, `#GPT-6`, `#OpenRouter`, `#决策模型`

---

<a id="item-12"></a>
## [Perplexity 开源多模态 late-interaction 嵌入模型](https://x.com/AravSrinivas/status/2107871834205196784) ⭐️ 7.62/10

Perplexity 开源了 pplx-embed-v2-late，这是一对多模态 late-interaction 嵌入模型（9B 和 0.6B 参数），共享文本和图像的嵌入空间。权重已在 Hugging Face 上提供，支持无需 OCR 的 PDF 检索。 此次发布使最先进的多模态检索技术得以普及，开发者可以构建同时处理文本和图像的高效文档搜索系统。9B 模型可索引大规模多模态数据，而 0.6B 模型支持设备端查询，使高级检索能力惠及更广泛的应用场景。 该模型在 MADQA 基准上达到 92.4%，在 BrowseComp+ 上达到 64%。9B 模型用于索引，0.6B 模型针对设备端查询优化，两者共享同一嵌入空间，实现无缝检索。

aihot · X：Aravind Srinivas（Perplexity CEO） (@AravSrinivas) · 10月7日 16:33 · [中文阅读](https://aihot.news/items/lfy2ww68p9lgpxxhu5jssflwf)

**核验**: 多源印证

**背景**: Late-interaction 嵌入模型（如 ColBERT）使用多向量表示，每个 token 单独嵌入，并通过 MaxSim 计算相似度。这种方法在双编码器的效率和交叉编码器的准确性之间取得平衡。MADQA 是一个多模态智能体文档问答基准，测试对 PDF 集合的检索和推理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.03992">Nemotron ColEmbed V2: Top-Performing Late Interaction ...</a></li>
<li><a href="https://github.com/OxRML/MADQA">MADQA: Multimodal Agentic Document QA - GitHub</a></li>
<li><a href="https://www.mixedbread.com/evals/madqa">MADQA benchmark · Agents - Mixedbread</a></li>

</ul>
</details>

**标签**: `#多模态嵌入`, `#开源模型`, `#Perplexity`, `#信息检索`, `#AI 工具`

---

<a id="item-13"></a>
## [LangChain 重构 Deep Agents 技能支持，新增工具绑定、固定技能与线程内重载](https://www.langchain.com/blog/revamping-skills-in-deep-agents) ⭐️ 7.5/10

LangChain 重构了 Deep Agents 中的技能支持，引入了三项关键改进：工具现在可以绑定到技能，并仅在技能被读取时加载；用户可以通过类似 '/meeting-prep' 的显式请求固定技能，以便在首次模型调用前加载；长线程可以通过将 'skills_metadata' 设为 None 来重载新增或变更的技能。 此更新解决了 AI agent 开发中的一个实际痛点：企业技能库可能增长到数千个技能，使得高效加载和管理变得至关重要。它为开发者提供了对技能加载的更细粒度控制，从而提升大规模 agent 部署的性能和灵活性。 三项改进包括：工具绑定（工具仅在关联技能被读取时加载）、固定技能（类似 '/meeting-prep' 的显式请求会在首次模型调用前强制加载）以及线程内重载（将 'skills_metadata' 设为 None 可在长线程中重载新增或变更的技能）。这些功能是 Deep Agents 堆栈的一部分，该堆栈使用 SkillsMiddleware 来处理技能的发现和读取。

aihot · LangChain：Blog（RSS） · 10月7日 18:49 · [中文阅读](https://aihot.news/items/m3vyz2bex4i58vffqfx586u3h)

**核验**: 多源印证

**背景**: Deep Agents 中的技能是可重用、模块化的能力，可以加载到 agent 中，类似于插件。它们遵循渐进式披露模式，agent 首先只看到技能的名称和描述，仅在调用时才读取完整的技能内容。这种方法通过减少初始上下文加载来帮助管理大型技能库。SkillsMiddleware 处理此过程的前两个级别，而 LLM 处理第三个级别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.langchain.com/oss/python/deepagents/skills">Skills - Docs by LangChain</a></li>
<li><a href="https://docs.langchain.com/oss/javascript/deepagents/skills">Skills - Docs by LangChain</a></li>
<li><a href="https://reference.langchain.com/python/deepagents/middleware/skills/SkillsStateUpdate/skills_metadata">skills_metadata | deepagents | LangChain Reference</a></li>

</ul>
</details>

**标签**: `#LangChain`, `#AI Agents`, `#开发者工具`, `#Skills`, `#产品更新`

---

<a id="item-14"></a>
## [Claude Code v2.1.293 新增 Haiku 5.5 并修复多项问题](https://github.com/anthropics/claude-code/releases/tag/v2.1.293) ⭐️ 7.3/10

Claude Code v2.1.293 已发布，将 Claude Haiku 5.5 设为 Anthropic API 上的默认 Haiku 模型，提供 1M 上下文窗口，定价为每百万 token 0.10/0.50 美元（超过 100K 的提示为 0.50/2.50 美元）。该版本还包含多项与上下文处理、MCP 连接等相关的错误修复。 此更新对 AI 开发者工具意义重大，因为 Claude Haiku 5.5 提供大上下文窗口和具有竞争力的定价，使其成为高容量、成本敏感任务的强有力选择。错误修复，尤其是内存泄漏和上下文压缩问题的修复，提高了 Claude Code 的可靠性和用户体验。 该版本在 `subagentStatusLine` 负载中新增了 `agentType` 字段，并为 mods 在 `$.tool.register` 中新增了 `isDeferred` 选项。它还修复了 HTTP MCP 连接中的内存泄漏、上下文压缩问题，以及与会话管理、插件测试和远程控制相关的各种其他错误。

github · ashwin-ant · 10月7日 18:10 · [中文阅读](https://aihot.news/items/vd2lvzvjz4tujiqupl30ifq3k) · 3 个来源

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 的命令行 AI 辅助编程工具，与 Claude Haiku 和 Sonnet 等模型集成。模型上下文协议（MCP）是一种开放标准，允许 Claude Code 连接到外部工具和数据源。Haiku 模型专为快速、高容量和成本敏感的任务而设计，适用于分类、路由和子代理任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/mcp">Connect Claude Code to tools via MCP - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI developer tools`, `#Model release`, `#Bug fixes`, `#MCP`

---

<a id="item-15"></a>
## [OpenAI Codex rust-v0.161.0 新增 GPT-6.1 Sol 默认模型、MCP 登录和语音设备选择](https://github.com/openai/codex/releases/tag/rust-v0.161.0) ⭐️ 7.0/10

OpenAI 发布了 Codex rust-v0.161.0，将 GPT-6.1 Sol 设为捆绑版和 Amazon Bedrock 目录中的默认模型，新增 `/mcp login <name>` 用于 MCP 服务器认证，并引入语音设备选择功能。该更新还使 Daybreak 通过 `--enable cli_daybreak` 变为可选，并增加了按轮次选择 Cyber 访问程序的功能。 此次更新通过简化 MCP 服务器认证和提供更灵活的模型与语音配置，提升了 Codex 对 AI 开发者和自动化工作流的易用性。默认的 GPT-6.1 Sol 模型提供了高性价比选项，可能降低重度用户的运营成本。 GPT-6.1 Sol 支持 1,050,000 token 的上下文窗口和 128,000 token 的输出，知识截止日期为 2026 年 4 月 30 日。Daybreak 需要通过 `--enable cli_daybreak` 或 `features.cli_daybreak=true` 显式启用；仅设置 `daybreak=true` 不够。语音偏好保存在本地，Cyber 访问程序选择可通过 `codex exec --cyber-access-program` 或 TypeScript SDK 的 `cyberAccessProgram` 选项使用。

github · github-actions[bot] · 10月7日 15:58

**核验**: 多源印证

**背景**: Codex 是 OpenAI 的 AI 编程代理，运行在终端中，帮助开发者自动化编码任务。MCP（模型上下文协议）是连接 AI 模型与外部工具和数据源的标准，新的 `/mcp login` 命令简化了此类服务器的认证。Daybreak 是一个启用高级路由和控件的功能，现在需要显式启用以避免意外行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://router.one/blog/gpt-6-1-sol-api-guide.md">router.one/blog/ gpt - 6 - 1 - sol -api-guide.md</a></li>
<li><a href="https://codexhandbook.com/en/skills/mcp/connect-an-mcp-server/">Connect an MCP server | Codex Handbook</a></li>
<li><a href="https://codexinsider.com/config/connect-an-mcp-server/">Connect an MCP server — Codex config — Codex Insider</a></li>

</ul>
</details>

**社区讨论**: 此新闻条目未提供社区评论。

**标签**: `#AI agents`, `#Codex`, `#MCP`, `#开源AI工具`, `#版本发布`

---

<a id="item-16"></a>
## [AI 逆向工程或使所有软件开源化](https://x.com/amasad/status/2107671204639465961) ⭐️ 7.0/10

Replit 首席执行官 Amjad Masad 在 X 上指出，AI 驱动的逆向工程和反编译技术正飞速发展，并预测不久后所有软件都将事实上的开源。他的帖子获得了超过 3200 个赞和 257 次转发，引发广泛关注。 这一转变可能从根本上改变软件安全、知识产权和专有软件的经济模式，因为任何编译后的程序都可能被轻易分析和复制。这也引发了关于开发者和公司如何在 AI 时代保护其代码和商业模式的紧迫问题。 这一说法基于近期出现的工具，如 OpenBin.ai，这是一个免费、开源、基于浏览器的平台，利用 AI 对原生二进制、Android APK、npm/PyPI 包和脚本进行反编译和分析。尽管该技术令人印象深刻，但在处理混淆代码时仍可能面临挑战，且法律和伦理影响尚未解决。

follow_builders · Amjad Masad · 10月7日 03:15

**核验**: 多源印证

**背景**: 逆向工程是分析编译后程序以理解其结构和功能的过程，传统上是一项劳动密集型任务。反编译将机器代码转换回高级语言，而 AI 现在可以以越来越高的准确性自动化这一过程。开源软件以源代码形式分发，任何人都可以查看、修改和再分发，而专有软件则隐藏源代码。如果 AI 能够有效地反编译任何二进制文件，开源与闭源之间的界限将变得模糊，可能使所有软件实际上都变为开源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openbin.ai/">OpenBin — Free AI Decompiler & Online Reverse Engineering Platform</a></li>
<li><a href="https://www.xpert4cyber.com/2026/08/openbin-ai-review-free-ai-decompiler.html">OpenBin. ai & OpenAPK. ai Review: Free AI Reverse Engineering Tool</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-source_software">Open-source software - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体热烈，许多人同意 AI 正在迅速消除理解编译代码的障碍。一些评论者表达了对软件安全影响的担忧，以及可能增加盗版或恶意逆向工程的风险，而另一些人则指出这一趋势可能加速创新和透明度。

**标签**: `#AI`, `#reverse engineering`, `#decompilation`, `#open-source`, `#software`

---

<a id="item-17"></a>
## [Peter Steinberger 将团队 AI 代理接入 X 以加速工作](https://x.com/steipete/status/2107697554448421160) ⭐️ 7.0/10

Peter Steinberger 宣布他将团队的 AI 代理（称为“claw”）连接到 X（原 Twitter）以更快地触发工作。未分配的会话可供任何人获取，代理会自动识别并在团队服务器上通知相关的代码所有者。 这种集成展示了 AI 代理在团队工作流程中的新颖应用，通过自动化任务分配和通知，可能提高生产力。它凸显了将 AI 代理嵌入通信平台和开发工具的趋势，这可能影响未来团队的协作方式。 整个设置是通过一个提示词实现的，并且由于插件现在支持热重载，团队服务器得以自我扩展。这表明代理的功能可以在不重启服务器的情况下更新，从而实现快速迭代和定制。

follow_builders · Peter Steinberger · 10月7日 05:00

**核验**: 多源印证

**背景**: 像“claw”这样的 AI 代理在开发者工具中越来越常见，通常基于开源框架（如 OpenClaw 或 Claw Code）构建，这些框架提供终端原生环境以支持自主编码任务。热重载插件允许开发人员即时修改代理行为，这对于适应不断变化的团队需求至关重要。将此类代理与 X 等社交平台集成可以简化沟通和任务管理，使团队更容易协调工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openclaw.ai/">OpenClaw — Open-Source AI Assistant</a></li>
<li><a href="https://www.toolify.ai/tool/claw-code">Claw Code: Open-source Python/Rust rewrite of the Claude Code AI ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#developer tools`, `#workflow automation`, `#team collaboration`, `#X integration`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="15"><span>其他追踪推文</span><span class="archive-tab-count">15</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="12"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">12</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2107925907914498365">@dotey: 🎉 Tibo 为了庆祝 Codex 和 ChatGPT Work 的活跃用户达到了 4000 万 的新高，为每个付费用户送一张重置卡。 将在 PST 时区当天结束前送达。</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 20:07 UTC · 喜欢 27 · 转发 1 · 回复 3 · 浏览 8658</p>
<p class="archive-item-content">🎉 Tibo 为了庆祝 Codex 和 ChatGPT Work 的活跃用户达到了 4000 万 的新高，为每个付费用户送一张重置卡。<br>
<br>
将在 PST 时区当天结束前送达。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2107917964146012485">@dotey: GPT-6 进入 ChatGPT 日常聊天，回答可以是一个能点、能调的智能界面 OpenAI 今天开始在 ChatGPT 推送 GPT-6，主打功能叫 Intelligent UI（智能...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 19:36 UTC · 喜欢 72 · 转发 5 · 回复 13 · 浏览 24049</p>
<p class="archive-item-content">GPT-6 进入 ChatGPT 日常聊天，回答可以是一个能点、能调的智能界面<br>
<br>
OpenAI 今天开始在 ChatGPT 推送 GPT-6，主打功能叫 Intelligent UI（智能界面）。<br>
<br>
Plus、Pro、Business、Enterprise 用户今天起可用，免费版和 Go 版（OpenAI 的低价订阅套餐）明天开始陆续开放，ChatGPT 每周 12 亿用户都会用上。企业版能不能用，要看公司管理员的设置。<br>
<br>
有了 Intelligent UI，GPT-6 会根据问题决定回答长什么样：对比类问题并排摆，讲原理配一张能拖动参数的示意图，简单问题照样一段文字答完。<br>
<br>
官方举的例子是周日请朋友吃烤羊腿，人数还没定。上一代模型给的是一大段菜谱加时间表；GPT-6 给的是一张带人数调节器的购物清单，把人数从 5 改成 8，羊肉、土豆的分量跟着变，下面再接一条烹饪时间线。你也可以直接让它做个工具，比如存钱计算器、聚餐分账器，或者一个能在对话里玩的小游戏。<br>
<br>
做法上，OpenAI 搭了一套原生界面组件库，再配一个“编译器”，模型边生成，界面边显示，不用等整段回答写完。训练时还专门评估模型做出的界面清不清楚、好不好用。<br>
<br>
GPT-6 还能边想边答。以前用推理模型，得等它想完才出结果，现在它会先把已经想清楚的部分写出来。需要联网搜索的问题，GPT-6 Instant 平均比上一代 GPT-5.6 Instant 早 44% 开始回答。<br>
<br>
付费用户用的是 GPT-6 Sol，免费版和 Go 版用的是 GPT-6 Luna。这两个模型 9 月 22 日已经在 Work（工作模式）、Codex（编程工具）和 API 上线，这次是补进日常聊天的 Chat 页面，Work 和 Codex 的模型不变。<br>
<br>
Anthropic 今年 3 月 12 日给 Claude 上线了“交互式可视化”测试版，包括免费版在内的所有用户默认开启。Claude 自己判断什么时候该画图，在对话里直接生成图表、流程图、时间线，或者带滑块、按钮的小部件，比如一张能逐个点开元素的元素周期表。这个功能脱胎于 2025 年秋天的实验项目 Imagine with Claude。<br>
<br>
两家想做的是同一件事：回答一个问题时，直接给你一个能操作的界面。区别在做法。<br>
<br>
据报道，Claude 的可视化是模型现写的网页代码和矢量图，形式更自由，但每次都是从零画。OpenAI 用固定的组件库，模型负责挑组件、排版，样式统一，手机上原生显示，还能一块块流式出现。<br>
<br>
OpenAI 这次还把“这题该不该用界面、用什么界面”放进了模型训练，并且和 GPT-6 一起推给所有用户。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2107913674593644711">@thsottiaux: Day 3/ The big one is GPT-6 in Chat, but today is also a little celebration day with a new hi...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 19:19 UTC · 喜欢 15494 · 转发 559 · 回复 1171 · 浏览 765056</p>
<p class="archive-item-content">Day 3/<br>
<br>
The big one is GPT-6 in Chat, but today is also a little celebration day with a new high of 40M active users across Codex and ChatGPT Work.<br>
<br>
Loading a banked reset in everyone&#x27;s paid accounts. See you again tomorrow!</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2107902563953582145">@dotey: 这是一个 Decisions API 很好的案例，用来做手势识别，OpenAI 的 API 相对 Jev 多模态能力更好</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 18:35 UTC · 喜欢 14 · 转发 1 · 回复 18 · 浏览 6172</p>
<p class="archive-item-content">这是一个 Decisions API 很好的案例，用来做手势识别，OpenAI 的 API 相对 Jev 多模态能力更好</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2107898828053504166">@dotey: Lauren 每天 Token 消耗真不少，30 天 1.5 T，我还以为都是 Fable，没想到用的最多的模型是 Opus 5.5 另外 Cloud 是 Token 消耗大头，如果你想同...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 18:20 UTC · 喜欢 25 · 转发 1 · 回复 15 · 浏览 10695</p>
<p class="archive-item-content">Lauren 每天 Token 消耗真不少，30 天 1.5 T，我还以为都是 Fable，没想到用的最多的模型是 Opus 5.5<br>
<br>
另外 Cloud 是 Token 消耗大头，如果你想同时多个任务并行，那么 Cloud 是最简单方便，每个任务都可以独立虚拟机，不担心相互干扰，只是 cloud 上的改动验证起来不如本机方便。<br>
<br>
我没有去计算 Token 消耗要多少钱，这个不太好算，因为有很多是 Cache 的，还有不同模型混合，还有 Cursor 自家模型。<br>
<br>
只是一个参考，有兴趣可以去看看资料：<br>
https://t.co/OZv78HJGrM</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2107897671335989304">@dotey: 本周起，Claude 的 Max 和 Team 订阅用户每月会拿到一笔 API 额度：Max 5x 送 100 美元，Max 20x 送 200 美元，Team 最多 500 美元，团队...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 18:15 UTC · 喜欢 66 · 转发 3 · 回复 11 · 浏览 19219</p>
<p class="archive-item-content">本周起，Claude 的 Max 和 Team 订阅用户每月会拿到一笔 API 额度：Max 5x 送 100 美元，Max 20x 送 200 美元，Team 最多 500 美元，团队成员共用。这笔额度只能在 Claude Platform 上用。<br>
<br>
https://t.co/CzGsHY44lY https://t.co/wJO84SEuCE</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/OpenAI/status/2107894997538525580">@OpenAI: GPT-6 and Intelligent UI, now rolling out in ChatGPT for everyone. Intelligent UI in ChatGPT...</a></h3>
<span class="score-badge" data-tier="high" aria-label="9.0 out of 10">9.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 18:05 UTC · 喜欢 16070 · 转发 1180 · 回复 703 · 浏览 2612230</p>
<p class="archive-item-content">GPT-6 and Intelligent UI, now rolling out in ChatGPT for everyone.<br>
<br>
Intelligent UI in ChatGPT delivers fast, interactive answers that make everyday questions more visual, complex topics easier to grasp, and interactive tools for your task available on the spot. https://t.co/XL2gDCPBwG</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/mtrainier2020/status/2107890851389288806">@mtrainier2020: 你被人耗了那么长时间。 人家系统里给你打标签了。 以后会有更多更真的诈骗过来。 其实你第一步就可以阻止诈骗。 挂断电话，打回去。 他们这种靠 spoofing 来电显示的诈骗，最怕的就是你...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 17:48 UTC · 喜欢 80 · 转发 9 · 回复 12 · 浏览 16169</p>
<p class="archive-item-content">你被人耗了那么长时间。<br>
人家系统里给你打标签了。<br>
以后会有更多更真的诈骗过来。<br>
其实你第一步就可以阻止诈骗。<br>
挂断电话，打回去。 <br>
他们这种靠 spoofing 来电显示的诈骗，最怕的就是你挂机再打。<br>
卫生部，要工号。找到官网，打进去，再找这个人。<br>
北京公安，要警号，或者部门，挂了，再打回去。<br>
<br>
所有转接的，统统挂掉，再打。<br>
能过滤掉 80%，诈骗电话。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/wuerbangbang/status/2107885150633857262">@wuerbangbang: 诈骗流程是这样的：下午一个英国号来电，自称英国卫生部工作人员，称有人盗用我的护照号注册了一个英国手机号，并前往伦敦皇家医院。该医院有传染病，此人因此违反了公共安全条例。对方称如 17:00...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 17:25 UTC · 喜欢 51 · 转发 6 · 回复 31 · 浏览 27725</p>
<p class="archive-item-content">诈骗流程是这样的：下午一个英国号来电，自称英国卫生部工作人员，称有人盗用我的护照号注册了一个英国手机号，并前往伦敦皇家医院。该医院有传染病，此人因此违反了公共安全条例。对方称如 17:00 前无法收到北京市公安局的关于冒用护照的报警联系单，我在英国的生活将受到影响，随后帮我通过专线&quot;转接&quot;到&quot;北京市公安局&quot;。<br>
<br>
电话转接后，一名自称北京警方的人让我下载 Teams 软件与我视频通话，不停批评教育我没有保护好个人信息安全（小词儿一套一套的，视频场景和语气都非常真！）说将帮我发传真过去，不用担心。但过了一会儿又说我名下居然有一张银行卡涉嫌洗钱案。我表示对那张卡毫不知情，也不是我注册的。他随即要求我保持 24 小时监听，并每 2 小时汇报一次行程，还要求我对家人朋友保密。17:30 他终于说完了，说之后再跟我进行案情沟通。这一停下来我感觉不对，就拉黑了。<br>
<br>
这个诈骗的核心是利用我初来乍到制造恐慌，然后切断联系并冒充权威。骗子先用&quot;护照被冒用、涉传染病、涉嫌洗钱&quot;等话术制造恐慌，让你急于自证清白，一旦开始想&quot;怎么证明不是我&quot;，就进入了对方节奏。随后以&quot;案件涉密&quot;为由，要求你对亲友保密，切断你与外界的信息来源，使骗子成为你唯一的信息源。再通过改号软件伪装官方号码（我收到的电话自动显示是“北京市公安局”）、伪造警官证和通缉令，利用你对公权力的敬畏，让人难以质疑。这就跟传销一样，关键是要风林火山地密集洗脑，不能停，不能让你琢磨，否则就有破绽。白白一个下午啊，可惜了我今天的新生招待会！</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/seflless/status/2107860983498817689">@seflless: Gesture recognition using the Decisions API by @OpenAIDevs. Thanks to it&#x27;s vision understandi...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月7日 15:49 UTC · 喜欢 615 · 转发 25 · 回复 30 · 浏览 42599</p>
<p class="archive-item-content">Gesture recognition using the Decisions API by @OpenAIDevs. <br>
<br>
Thanks to it&#x27;s vision understanding it is way more accurate than my previous Jev-based demo. It was also faster. cc @thsottiaux @jxnlco @pvncher @tldraw @steveruizok https://t.co/3P2iKffdWW</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2107794249051951205">@op7418: 开始抢入口了，不硬推模型了，Personal agent 这一仗估计是要硬打了</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月7日 11:24 UTC · 喜欢 42 · 转发 1 · 回复 11 · 浏览 21634</p>
<p class="archive-item-content">开始抢入口了，不硬推模型了，Personal agent 这一仗估计是要硬打了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2107788042929160367">@op7418: 我操，Grok bot 现在无敌了！ 老马刚才说，Grokbot 会根据特定任务使用当前任务的最佳模型。 也就是说，它不止使用 Grok 4.7 或者 4.6 了。 还会使用 Opus...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月7日 11:00 UTC · 喜欢 97 · 转发 3 · 回复 49 · 浏览 48360</p>
<p class="archive-item-content">我操，Grok bot 现在无敌了！<br>
<br>
老马刚才说，Grokbot 会根据特定任务使用当前任务的最佳模型。<br>
<br>
也就是说，它不止使用 Grok 4.7 或者 4.6 了。<br>
<br>
还会使用 Opus 5.5、Midjourney、Suno 等各种 API 帮你构建内容或者是执行任务。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2107696000899158404">@op7418: 尝试让 Opus 5.5 做个网站解释奇门遁甲 https://t.co/1A2C36q226</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月7日 04:54 UTC · 喜欢 66 · 转发 4 · 回复 30 · 浏览 16245</p>
<p class="archive-item-content">尝试让 Opus 5.5 做个网站解释奇门遁甲 https://t.co/1A2C36q226</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2107676475336044892">@op7418: 重置了居然！</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月7日 03:36 UTC · 喜欢 28 · 转发 0 · 回复 11 · 浏览 14010</p>
<p class="archive-item-content">重置了居然！</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2107676072871600470">@thsottiaux: We shipped four things that were deemed good to great and some math proofs, but the vote is c...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.3 out of 10">2.3</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月7日 03:35 UTC · 喜欢 15673 · 转发 652 · 回复 2246 · 浏览 1422692</p>
<p class="archive-item-content">We shipped four things that were deemed good to great and some math proofs, but the vote is clear and the community demands a reset. I did calibrate it and it *seems* that the game is rigged in reset&#x27;s favor, but such are the rules at the moment.<br>
<br>
Therefore ... the reset has been processed. Enjoy!</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2107706522457497753">Nikunj Kothari: Too many VCs are chasing dopamine.. or rage baiting purposely just to get more views on this...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>尼库尼·科塔里：太多风投在追逐多巴胺或故意引战以获取流量</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 10月7日 05:36 UTC · 喜欢 13 · 转发 0 · 回复 2</p>
<p class="archive-item-content">A VC criticizes other VCs for chasing dopamine and rage baiting on X, noting it harms their long-term brand and even causes lost deals.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位风投批评同行在 X 平台上追逐多巴胺或故意引战，认为这损害长期品牌并导致交易流失。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/sama/status/2107691577015755196">Sam Altman: and thank you to the untold number of people who put in the technical work, brick by brick ov...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>山姆·奥特曼：感谢无数代代相传、一砖一瓦付出技术工作的人们……</p>
<p class="source-line">Follow Builders · X 动态 · Sam Altman · 10月7日 04:36 UTC · 喜欢 1639 · 转发 59 · 回复 84</p>
<p class="archive-item-content">Sam Altman expresses gratitude to the many people whose technical work over generations made a recent achievement possible.</p>
<p class="archive-item-translation"><span>中文摘要</span>山姆·奥特曼感谢历代无数技术人员一砖一瓦的积累，使如今的奇迹成为可能。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/sama/status/2107691262795239805">Sam Altman: thank you to the machines, and the structure of reality, for letting us understand a little m...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Sam Altman：感谢机器与现实结构让我们多懂一点</p>
<p class="source-line">Follow Builders · X 动态 · Sam Altman · 10月7日 04:35 UTC · 喜欢 1458 · 转发 52 · 回复 60</p>
<p class="archive-item-content">Sam Altman 发表了一条感谢机器和现实结构的简短推文，无技术细节。</p>
<p class="archive-item-translation"><span>中文摘要</span>Sam Altman 发了一条无实质内容的简短感想，感谢机器和现实结构，缺乏技术细节。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/sama/status/2107691261776052633">Sam Altman: looking up at the stars with extra awe tonight. &quot;thy sea is so great and my boat is so small.&quot;</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Sam Altman 感慨夜空：大海如此浩瀚，我的小船如此渺小</p>
<p class="source-line">Follow Builders · X 动态 · Sam Altman · 10月7日 04:35 UTC · 喜欢 4460 · 转发 238 · 回复 578</p>
<p class="archive-item-content">Sam Altman shares a personal, awe-inspired reflection on the ocean and stars, with no technical or business insight.</p>
<p class="archive-item-translation"><span>中文摘要</span>Sam Altman 发布了一条个人情感推文，表达对星空和大海的敬畏，没有任何技术或行业相关内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/levie/status/2107680435644039269">Aaron Levie: Cyber will be one of the most defining domains for AI in the coming years, and a huge area of...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Aaron Levie：网络将成为未来几年 AI 最具决定性的领域之一，也是大多数企业的重点领域。</p>
<p class="source-line">Follow Builders · X 动态 · Aaron Levie · 10月7日 03:52 UTC · 喜欢 164 · 转发 24 · 回复 47</p>
<p class="archive-item-content">Aaron Levie argues that cybersecurity will be a major AI domain, driven by new threats from AI-generated code and agentic attacks, and sees a huge opportunity for agentic security products and professionals.</p>
<p class="archive-item-translation"><span>中文摘要</span>Aaron Levie 认为，网络安全将成为 AI 的重要领域，因为 AI 生成的代码和智能体攻击带来了新威胁，而智能体安全产品和专业人员将迎来巨大机遇。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/joshwoodward/status/2107679061854273656">Josh Woodward: Mask-based editing is my favorite from today, much more coming soon! https://t.co/Y0VeDg2P4j</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Josh Woodward：基于遮罩的编辑是我今天最喜欢的，更多功能即将推出！</p>
<p class="source-line">Follow Builders · X 动态 · Josh Woodward · 10月7日 03:47 UTC · 喜欢 92 · 转发 4 · 回复 7</p>
<p class="archive-item-content">Josh Woodward teases mask-based editing as a favorite feature, with more updates coming soon.</p>
<p class="archive-item-translation"><span>中文摘要</span>Josh Woodward 预告基于遮罩的编辑功能是其今日最爱，并暗示更多更新即将到来。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2107676653895967106">Thibault Sottiaux: Also! Good evening!!</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：还有！晚上好！！</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月7日 03:37 UTC · 喜欢 1309 · 转发 6 · 回复 59</p>
<p class="archive-item-content">A brief social media greeting with no substantive content.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条没有实质内容的社交媒体问候。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2107676261099426030">Thibault Sottiaux: And we won&#x27;t unship the improvements. You get to have your cake and eat it too. See you tomor...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：我们不会撤回这些改进。你可以两者兼得。明天见……</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月7日 03:35 UTC · 喜欢 2256 · 转发 17 · 回复 144</p>
<p class="archive-item-content">A teaser post promising that improvements will not be removed, with a vague reference to &#x27;Day 3&#x27; of an unspecified event.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条预告帖子，承诺不会移除改进，并模糊提及某活动的第三天。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2107676072871600470">Thibault Sottiaux: We shipped four things that were deemed good to great and some math proofs, but the vote is c...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月7日 03:35 UTC · 喜欢 10173 · 转发 497 · 回复 1487</p>
<p class="archive-item-content">We shipped four things that were deemed good to great and some math proofs, but the vote is clear and the community demands a reset. I did calibrate it and it *seems* that the game is rigged in reset&#x27;s favor, but such are the rules at the moment.<br>
<br>
Therefore ... the reset has been processed. Enjoy!</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2107674122612555953">Garry Tan: Connie Chan doesn’t want to see a strong Dem party bring about a boom loop to SF and Californ...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Garry Tan：Connie Chan 不希望强大的民主党为旧金山和加州带来繁荣循环</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 10月7日 03:27 UTC · 喜欢 52 · 转发 2 · 回复 9</p>
<p class="archive-item-content">Garry Tan 批评 Connie Chan 反对促进旧金山和加州繁荣的政策。</p>
<p class="archive-item-translation"><span>中文摘要</span>Garry Tan 批评 Connie Chan 投票反对能促进旧金山和加州活力的措施，并攻击为城市奋斗的人。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2107669485549400474">Peter Yang: Do I know anyone at @Fourthwall or a related platform? My 8-year-old and I want to use her dr...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：我认识 @Fourthwall 或相关平台的人吗？我 8 岁的孩子和我……</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 10月7日 03:08 UTC · 喜欢 7 · 转发 1 · 回复 2</p>
<p class="archive-item-content">A user asks for introductions to Fourthwall to sell t-shirts featuring his 8-year-old&#x27;s drawings.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位用户寻求 Fourthwall 的引荐，想用他 8 岁孩子的画作卖 T 恤。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2107646238585950540">Swyx: what is your default/workhorse coding agent today, Oct 2026?</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：2026 年 10 月，你默认的主力编码代理是什么？</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 10月7日 01:36 UTC · 喜欢 19 · 转发 0 · 回复 66</p>
<p class="archive-item-content">Swyx asks the developer community which coding agent they currently use as their default workhorse as of October 2026.</p>
<p class="archive-item-translation"><span>中文摘要</span>Swyx 向开发者社区提问，截至 2026 年 10 月，他们目前默认使用哪个编码代理作为主力工具。</p>
</article>
</div>
</section>
