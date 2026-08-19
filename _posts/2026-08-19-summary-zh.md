---
layout: default
title: "Horizon Summary: 2026-08-19 (ZH)"
date: 2026-08-19
lang: zh
---

> 从 46 条内容中筛选出 14 条重要资讯。

---

1. [支付巨头 Stripe 收购统一 AI 模型 API 平台 OpenRouter。](#item-1) ⭐️ 8.3/10
2. [GLM-5.3 API 上线：AA 智能指数 60 分并列开源第一，成本更低](#item-2) ⭐️ 8.28/10
3. [爱好者购买玩笑域名，意外卷入国际冲突监控。](#item-3) ⭐️ 8.0/10
4. [利用几何阴影分析与 CUDA 加速计算对未知岛屿进行地理定位](#item-4) ⭐️ 8.0/10
5. [Simon Willison 认为在 AI 编程助手时代，代码行数可以成为有效的生产力指标](#item-5) ⭐️ 8.0/10
6. [高性能 AI Agent 框架 Apache Maka 进入 Apache 孵化器。](#item-6) ⭐️ 8.0/10
7. [LMSYS 优化 DeepSeek-V4-Pro 在 H20 GPU 上的推理性能，大幅缩小与 B300 的差距](#item-7) ⭐️ 7.83/10
8. [Anthropic 因网络安全担忧放缓模型开发，暂停强化学习训练](#item-8) ⭐️ 7.8/10
9. [FastMetal 让 Mac 本地 30 秒生成视频](#item-9) ⭐️ 7.78/10
10. [Go 1.27 发布，引入泛型方法、标准 UUID 包和后量子密码算法](#item-10) ⭐️ 7.0/10
11. [Simon Willison 使用 Claude Code 评估 smolvm 作为运行不受信任 Python 和 JavaScript 代码的沙箱。](#item-11) ⭐️ 7.0/10
12. [Jeremy Morrell 提出假设：LLM 与沙盒技术将开启可扩展 Web 软件的新时代。](#item-12) ⭐️ 7.0/10
13. [分析指出模型缩放必须综合考虑数据、算力和部署，而不仅仅是参数量。](#item-13) ⭐️ 7.0/10
14. [Codex AI 实施安全修复，防止清理操作中意外删除用户文件。](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [支付巨头 Stripe 收购统一 AI 模型 API 平台 OpenRouter。](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/) ⭐️ 8.3/10

支付公司 Stripe 已完成对 OpenRouter 的收购，后者是一家为开发者提供统一 API 以访问数百个不同 AI 模型的公司。据报道，此次收购价值约 100 亿美元，是 Stripe 向核心支付业务之外迈出的重要一步。 此次收购标志着 Stripe 战略性地扩展至 AI 基础设施层，旨在成为 AI 应用和智能体的基础平台，这些应用需要无缝的模型访问、使用计量和计费。通过提供集成了 Stripe 支付功能的统一模型路由、成本归因和支付处理堆栈，此举可能加速 AI 智能体的发展。 OpenRouter 不仅仅是一个简单的代理；它提供了诸如自动路由到满足性能门槛的最便宜提供商等功能。此次收购紧随 Stripe 近期以 11 亿美元收购稳定币基础设施公司 Bridge 之后，表明其构建面向下一代软件的全面金融和运营基础设施的更广泛战略。

hackernews · rvz · 8月19日 17:32 · [社区讨论](https://news.ycombinator.com/item?id=49364559) · [中文阅读](https://aihot.virxact.com/items/cmt0d2tsl1961rodpnvzxo4cc) · 2 个来源

**核验**: 多源印证

**背景**: OpenRouter 是一个平台，为开发者提供单一 API 来访问和切换众多 AI 模型（例如来自 OpenAI、Anthropic 等公司的模型），抽象了处理多个提供商、定价和集成的复杂性。Stripe 是一家领先的全球金融基础设施公司，以其在线支付处理 API 闻名，但一直在向邻近领域扩展，如资金管理、公司卡，以及现在的 AI 基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://www.bee.com/74669.html">Stripe Acquires OpenRouter: The Ultimate Piece of the AI Agent...</a></li>
<li><a href="https://blockchaindesk.co/stripe-explores-10b-acquisition-openrouter-ai-infrastructure/">Stripe explores $10B acquisition of AI infrastructure startup...</a></li>

</ul>
</details>

**社区讨论**: 社区对 OpenRouter 的产品及其促进模型提供商竞争的价值主张普遍持积极态度。一些用户对创建另一个专有的平台即服务中间商表示长期担忧，更倾向于开放协议。另一些用户则强调了 OpenRouter 超越简单路由的高级功能，如成本性能优化，并推测 Stripe 将利用它来为 AI 智能体构建全面的计量和会计系统。

**标签**: `#AI Infrastructure`, `#Acquisition`, `#Developer Tools`, `#API`, `#Stripe`

---

<a id="item-2"></a>
## [GLM-5.3 API 上线：AA 智能指数 60 分并列开源第一，成本更低](https://mp.weixin.qq.com/s?__biz=MzkyMzI3NzQ0Mg%3D%3D&mid=2247494105&idx=1&sn=8d7409e0fb846a3c7803c142b5d1a8e7) ⭐️ 8.28/10

智谱 AI 正式上线了 GLM-5.3 大语言模型的 API 服务，该模型在 AA 综合智能指数中取得 60 分，与 Kimi K3 并列开源模型第一，并与 Claude Fable 5、GPT-5.6 Sol 等闭源旗舰模型同级。模型权重将于下周五开源，其 API 定价与 GLM-5.2 持平。 此次发布意义重大，因为它声称能以更低的成本提供与领先闭源模型相当的性能，有望为开发者和企业降低使用前沿智能的门槛。作为一个在关键基准测试中达到顶级水平的开源模型，它可能会加剧大语言模型市场的竞争，并推动高性价比 AI 的普及。 GLM-5.3 并未更换基座模型，而是在 GLM-5.2 的基础上，通过在长周期环境中进行一个月的强化学习，使其编码能力提升了 50%。它是一个总参数量约 743B 的混合专家模型，但每次推理仅激活约 40B 参数，这有助于降低其调用成本。

aihot · 公众号：智谱（GLM） · 8月19日 01:03 · [中文阅读](https://aihot.virxact.com/items/cmszeb2mx0b3srodpef1ub0j0) · 2 个来源

**核验**: 多源印证

**背景**: AA 智能指数是一个综合基准测试，通过对十个公共子评估进行加权，来提供模型能力的快照。混合专家模型是一种将模型划分为多个小型专用子网络（“专家”）的架构，每次任务只激活其中几个，以提高效率。扩展定律，例如 DeepMind 的 Chinchilla 论文所探讨的，研究的是模型规模、训练数据和性能之间的最优关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/methodology/intelligence-benchmarking">Intelligence Benchmarking | Artificial Analysis</a></li>
<li><a href="https://www.datacamp.com/blog/mixture-of-experts-moe">What Is Mixture of Experts (MoE)? How It Works, Use Cases & More | DataCamp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chinchilla_(language_model)">Chinchilla (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Open Source AI`, `#AI Developer Tools`, `#Model Benchmarking`

---

<a id="item-3"></a>
## [爱好者购买玩笑域名，意外卷入国际冲突监控。](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/) ⭐️ 8.0/10

一名爱好者为一个气象气球追踪项目购买了一个玩笑域名，该域名后来成为监控乌克兰军事活动的关键数据源，并因此引来了多个政府部门的正式问询。这个最初名为'Sondehub'的项目，聚合了来自无线电探空仪（气象气球）的开源数据，而这些数据也被用于军事监视。 这一事件凸显了开源、由爱好者驱动的数据收集如何意外地与高风险地缘政治和国家监控产生交集，引发了关于开放数据中立性以及公民科学项目意外后果的思考。它展示了看似无害的技术的双重用途性质，以及全球冲突如何能将甚至小规模的独立项目卷入其中。 该项目涉及追踪无线电探空仪，这是一种气象气球，同时也在 403 MHz 频率上传输数据；后来发现其中一些气球被用于军事目的。这位爱好者收到了来自包括被称为“战争部”在内的多个政府实体的联系，内容涉及所收集的数据。

hackernews · kareiva · 8月19日 11:21 · [社区讨论](https://news.ycombinator.com/item?id=49360015)

**核验**: 多源印证

**背景**: 气象气球追踪是一种流行的爱好者活动，个人使用软件定义无线电（SDR）和开源软件来接收和解码由气象机构发射的无线电探空仪信号。像 Sondehub 这样的项目会聚合这些数据，用于预测气球落点以便回收等目的。无线电探空仪传输包括 GPS 位置在内的遥测数据，这些数据可以被重新利用。像.ua（乌克兰）或.ru（俄罗斯）这样的国家代码顶级域名（ccTLD）由国家机构管理，可能具有地缘政治意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/topics/high-altitude-balloon">high-altitude-balloon · GitHub Topics · GitHub</a></li>
<li><a href="http://www.tcpipguide.com/free/t_DNSGeopoliticalCountryCodeTopLevelDomainsandAuthor-4.htm">DNS Geopolitical (Country Code) Top Level Domains and Authorities</a></li>

</ul>
</details>

**社区讨论**: 评论者认为这个故事引人入胜，并赞赏其由人类撰写、非 AI 生成的性质。他们将其与其他开放基础设施运营商收到不寻常官方请求的经历相提并论，并指出了所收到的官方通讯中的讽刺意味。讨论还反思了爱好者项目无意中与法律或调查事务产生交集的更广泛现象。

**标签**: `#geopolitics`, `#open-data`, `#hobbyist-tech`, `#surveillance`, `#internet-governance`

---

<a id="item-4"></a>
## [利用几何阴影分析与 CUDA 加速计算对未知岛屿进行地理定位](https://yassa9.github.io/osint/gralhix-004/) ⭐️ 8.0/10

一篇技术文章详细介绍了如何通过分析照片中山脉的阴影来确定太阳位置，进而利用 CUDA 加速的暴力搜索算法，将地形与数字高程模型（DEM）进行匹配，从而解决了一项地理定位挑战。作者成功确定了岛屿的坐标、度假村的名称以及相机的朝向。 这展示了一种新颖且实用的开源情报（OSINT）应用，它结合了计算机视觉、天文学和高性能计算，超越了简单的图像匹配。它展示了 GPU 加速如何使计算密集型的地理空间分析对个人研究者变得可行，并对自动驾驶导航和法医调查等领域具有启示意义。 该方法涉及根据阴影几何计算太阳的方位角和高度角，然后使用 CUDA 内核高效地测试全球数字高程模型中数百万个潜在位置，以寻找匹配的地形轮廓。一个关键限制是要求照片清晰、阴影分明且地形特征可识别，同时精度取决于可用高程数据的分辨率。

hackernews · yassa9 · 8月19日 12:19 · [社区讨论](https://news.ycombinator.com/item?id=49360545)

**核验**: 多源印证

**背景**: CUDA 是英伟达的并行计算平台，允许在 GPU 上进行通用计算，能极大加速地理空间分析所需的海量数据处理等任务。用于地理定位的几何阴影分析是一种开源情报（OSINT）技术，它利用太阳的位置（可从阴影推导）以及已知的时间/日期来缩小照片的可能拍摄地点范围。OSINT 指的是为调查目的而收集和分析公开可得的信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CUDA">CUDA - Wikipedia</a></li>
<li><a href="https://github.com/bytemallet/shadowtrace">GitHub - bytemallet/shadowtrace: Advanced OSINT geolocation tool using shadow analysis to estimate photo locations. Upload images with clear shadows, mark reference points, input timestamps, and get precise geographic probability maps. Features dual-photo intersection analysis for enhanced accuracy. Built with React/D3.js, inspired by Bellingcat's methodology. · GitHub</a></li>
<li><a href="https://www.bellingcat.com/resources/2020/12/03/using-the-sun-and-the-shadows-for-geolocation/">Using the Sun and the Shadows for Geolocation - bellingcat</a></li>

</ul>
</details>

**社区讨论**: 社区赞扬了文章的技术深度和人工撰写的风格。评论者将这种技术与成熟的军事导航系统（如地形轮廓匹配 TERCOM）及其在美国宇航局火星着陆任务中的应用联系起来。也有人指出，如此强大的位置追踪技术与关于避免为警察国家开发工具的讨论同时出现颇具讽刺意味，这凸显了伦理考量。

**标签**: `#CUDA`, `#Geolocation`, `#OSINT`, `#Computer Vision`, `#Parallel Computing`

---

<a id="item-5"></a>
## [Simon Willison 认为在 AI 编程助手时代，代码行数可以成为有效的生产力指标](https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/) ⭐️ 8.0/10

在最近的一期播客中，开发者 Simon Willison 提出了一个细致的论点：在使用 AI 编程助手时，测量代码行数可以成为衡量生产力的一个有意义的指标，这直接挑战了软件工程中长期存在的一种信念。他认为，虽然一名人类工程师每天可能产出 50-200 行经过调试、可用于生产的代码，但熟练使用 AI 助手可以显著提高这一产出，只要代码质量得以保持，就代表着真实的生产力提升。 这一点很重要，因为它重新构建了 AI 时代关于软件指标的核心辩论，表明当生产机制从纯粹的人力转向人机协作时，传统上对代码行数作为指标的否定可能需要重新评估。它强调，对于工程团队来说，新的瓶颈可能不再是代码输出速度，而是在代码库现在可以呈数量级更快增长的情况下，维持其概念完整性所需的认知能力。 Willison 强调，只有当 AI 生成的代码保持质量——即可维护、经过测试且可用于生产时，这种生产力提升才成立。他还提出了一个关键挑战：当 AI 助手使得添加功能变得廉价且容易时，如何保持'概念完整性'（一种连贯、统一的设计），否则可能导致代码库变成一个支离破碎的'温彻斯特神秘屋'。

rss · Simon Willison · 8月19日 22:46

**核验**: 多源印证

**背景**: '概念完整性'这一术语源于 Frederick P. Brooks 的开创性著作《人月神话》。它指的是软件系统的一个特性，即其核心概念作为一个流畅、连贯的整体协同工作，这被认为是良好设计和可维护性的关键。AI 编程助手是先进的 AI 工具，可以自主规划、执行和验证多文件的代码变更，超越了简单的代码补全，更像自动化的编程伙伴。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/computer-science/conceptual-integrity">Conceptual Integrity - an overview | ScienceDirect Topics</a></li>
<li><a href="https://arxiv.org/pdf/1811.04315">Software Conceptual Integrity: Deconstruction, Then ...</a></li>
<li><a href="https://www.augmentcode.com/tools/8-top-ai-coding-assistants-and-their-best-use-cases">8 Best AI Coding Assistants [Updated May 2026] | Augment Code</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Software Development`, `#Productivity`, `#LLMs`, `#Developer Tools`

---

<a id="item-6"></a>
## [高性能 AI Agent 框架 Apache Maka 进入 Apache 孵化器。](https://x.com/jakevin7/status/2090117512675659854) ⭐️ 8.0/10

高性能开源 AI Agent 框架项目 Apache Maka 已正式进入 Apache 孵化器，成为该基金会内的首个 Agent 框架项目。该项目始于 5 月 27 日，在最初的 10 周内迅速发展，拥有超过 71 万行 TypeScript 代码，并合并了 1218 个拉取请求。 这很重要，因为它为开源 AI 模型建立了一个中立、社区驱动的优化平台，对抗了由单个模型提供商控制专有框架的趋势。一个高性能的开源框架对于开源模型生态至关重要，它能让开发者在不受供应商锁定的情况下，充分利用各种模型的能力。 该项目使用 TypeScript 编写，其代码库的 35% 是测试代码，并展现出极快的开发速度，拉取请求合并的中位时间仅为 33.5 分钟。其宣称的愿景是成为最适配各种开放模型的高性能框架，且其所有基准测试报告完全开源并可复现。

twitter · kabikabi · 8月19日 16:43

**核验**: 多源印证

**背景**: AI Agent 框架是围绕大语言模型（LLM）的软件基础设施，通过管理工具使用、记忆、状态持久化和多步骤执行，使模型能够作为智能体运行。Apache 孵化器是希望加入 Apache 软件基金会的项目的入口，项目在此接受指导，学习 Apache 的开源治理之道，目标是最终毕业成为顶级项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>
<li><a href="https://training.incubator.apache.org/presentations/incubator/navigating-asf-incubation/index.html">training. incubator . apache .org/presentations/ incubator /navigating-asf...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Open Source`, `#Developer Tools`, `#Apache Incubator`, `#TypeScript`

---

<a id="item-7"></a>
## [LMSYS 优化 DeepSeek-V4-Pro 在 H20 GPU 上的推理性能，大幅缩小与 B300 的差距](https://www.lmsys.org/blog/2026-08-19-deepseek-v4-pro-engine-optimization-h20) ⭐️ 7.83/10

LMSYS 团队针对拥有 1.6 万亿参数的 MoE 模型 DeepSeek-V4-Pro，展示了在 NVIDIA H20 GPU 上进行推理优化的方法，显著缩小了其与更强大的 B300 GPU 之间的性能差距。其单节点 H20-141GB 参考实现达到了每秒 271 个输出 token，将与 B300（每秒 383.7 个 token）的性能差距缩小至仅 1.42 倍。 这项优化意义重大，因为它使得能够在更易获取的硬件上经济高效地部署庞大的、最先进的 MoE 模型，直接影响 AI 基础设施的成本和可及性。它证明了通过精心的工程优化，可以从成本较低的 GPU 中榨取出接近顶级硬件的性能，这对于希望高效扩展 AI 推理能力的组织至关重要。 此次优化专门针对 H20 GPU，该 GPU 具备 96GB HBM3 显存，并基于 NVIDIA 的 Hopper 架构。DeepSeek-V4-Pro 模型本身是一个 1.6 万亿参数的 MoE 模型，采用了结合压缩稀疏注意力（CSA）和重度压缩注意力（HCA）的混合注意力机制，以提高长上下文处理效率。

aihot · LMSYS：Blog（Chatbot Arena 团队） · 8月19日 17:56 · [中文阅读](https://aihot.virxact.com/items/cmt0e7sxo01eiro2o4l4y9jmh)

**核验**: 多源印证

**背景**: 混合专家（MoE）是一种机器学习架构，模型由多个专门的子网络（专家）组成，一个门控网络动态选择为给定输入使用哪些专家，从而允许模型拥有更大的总参数量，而不会导致每次推理的计算成本成比例增加。NVIDIA 的 H20 是一款基于 Hopper 架构的 AI 推理 GPU，提供高内存带宽，但与 B300 等旗舰级数据中心 GPU 相比，其性能和价格定位不同。DeepSeek-V4-Pro 是 DeepSeek-ai 推出的前沿、大规模语言模型，以其 1.6 万亿参数和为长上下文设计的高效混合注意力机制而著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://viperatech.com/product/nvidia-hgx-h20">NVIDIA HGX H20 Enterprise 96GB AI GPU | Viperatech</a></li>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-pro/modelcard">deepseek-v4-pro Model by Deepseek-ai | NVIDIA NIM</a></li>

</ul>
</details>

**标签**: `#AI Inference`, `#Model Optimization`, `#GPU Performance`, `#Large Language Models`, `#MoE Models`

---

<a id="item-8"></a>
## [Anthropic 因网络安全担忧放缓模型开发，暂停强化学习训练](https://openai.com/index/pacing-model-development-cyber-capabilities) ⭐️ 7.8/10

Anthropic 因担心即将推出的 Astra 等模型可能达到网络安全能力的“关键阈值”，正有意放缓模型开发速度，包括暂停其最新模型为期两周的强化学习（RL）训练。该公司还实施了更严格的安全协议，如工作负载隔离、网络隔离，并扩大了思维链监控范围。 这标志着一家主要 AI 实验室的重大战略转变，在面对高级 AI 既可用于网络防御也可用于网络攻击的新兴双重用途风险时，将安全性置于快速能力扩展之上。这表明行业日益认识到，前沿模型可能很快具备需要新的、主动的防护措施的能力。 这一决定是由近期的 OpenAI-Hugging Face 安全事件以及对 Astra 模型潜在能力的特定担忧所触发。涉及 Astra 或网络模型的工作负载必须满足最严格的安全标准，部分训练和评估工作仍处于暂停状态。

aihot · Hacker News 热门（buzzing.cc 中文翻译） · 8月19日 21:42 · [中文阅读](https://aihot.virxact.com/items/cmt0mqceo08lzro2o6xi3rlk4)

**核验**: 多源印证

**背景**: Anthropic 的 Astra 是一款未发布的前沿 AI 模型，据报道已解决多个高难度数学问题，表明其具备高级推理能力。“关键网络安全能力阈值”这一概念指的是 AI 能力达到一定水平，模型可以自主执行或极大助力复杂的网络操作，从而构成严重的双重用途风险。工作负载隔离和网络隔离等安全措施是用于分割和控制 AI 系统的技术，旨在防止未经授权的访问或数据泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/">Responding to the next frontier of critical cyber capabilities | OpenAI</a></li>
<li><a href="https://futurehumanism.co/articles/claude-mythos-cybersecurity-capability-threshold/">Claude Mythos and the Cybersecurity Capability Threshold</a></li>
<li><a href="https://redteams.ai/tags/isolation">isolation — AI Red Teaming Articles | redteams. ai</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Model Development`, `#Anthropic`, `#Cybersecurity`, `#Industry Trends`

---

<a id="item-9"></a>
## [FastMetal 让 Mac 本地 30 秒生成视频](https://x.com/haoailab/status/2090177721913770407) ⭐️ 7.78/10

FastMetal 项目将 FastWan-QAD 视频生成系列移植到了 Apple Silicon 上，实现了在 Mac 本地仅用 30 秒生成一段 5 秒长的 480p 视频。它完全通过 MLX 框架在 Metal API 上运行，默认使用 INT8 量化，并提供了三种模型尺寸（1.3B、5B、14B）以适应不同的分辨率和画质需求。 这具有重要意义，因为它将高效的本地视频生成带到了消费级硬件上，无需 NVIDIA CUDA 或云服务，从而降低了 AI 视频创作的门槛。它顺应了设备端 AI 的发展趋势，并展示了苹果统一内存架构在本地运行大型生成模型方面的潜力。 该系统采用了 Diffusion Transformer (DiT) 架构和 DMD 采样器，以实现高效的少步生成，并且仅占用 3.9 GiB 内存。三个模型变体针对特定用例设计：1.3B 模型用于 480p 分辨率，5B 模型用于 720p 分辨率，14B 模型则旨在追求更高的画质。

aihot · X：Sky Computing Lab (@haoailab) · 8月19日 20:42 · [中文阅读](https://aihot.virxact.com/items/cmt0kxcuu07f2ro2owuqpbjc8)

**核验**: 多源印证

**背景**: MLX 是苹果推出的一个数组框架，专为在 Apple Silicon 上进行高效的机器学习而设计，它利用 Metal API 进行 GPU 加速。视频扩散变换器 (DiT) 是一种生成模型架构，它在扩散过程中使用变换器来创建时间上连贯的视频。DMD（分布匹配蒸馏）是一种蒸馏技术，能大幅减少扩散模型所需的采样步数，从而实现更快（通常是单步）的生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mlx-framework.org/">MLX</a></li>
<li><a href="https://www.emergentmind.com/topics/video-diffusion-transformer-dit">Video Diffusion Transformer ( DiT ) Overview</a></li>
<li><a href="https://tianweiy.github.io/dmd/">One-step Diffusion with Distribution Matching Distillation</a></li>

</ul>
</details>

**标签**: `#AI Video Generation`, `#Apple Silicon`, `#Local AI`, `#Open Source`, `#MLX`

---

<a id="item-10"></a>
## [Go 1.27 发布，引入泛型方法、标准 UUID 包和后量子密码算法](https://go.dev/blog/go1.27) ⭐️ 7.0/10

Go 1.27 已正式发布，该版本引入了对泛型方法的支持、一个新的标准库 UUID 包、后量子密码算法，并采用了 Russ Cox 的 uscale 算法改进了浮点数解析。 此次发布显著增强了 Go 的类型系统和安全性，通过泛型方法使编写可复用代码更加容易，并为应用应对未来的量子计算威胁做好了准备。标准 UUID 包的加入将减少对第三方库的依赖，并统一生态系统。 新的泛型方法支持解决了一个关键的易用性问题，允许泛型函数在更多上下文中无需显式类型参数即可使用。后量子密码支持包含了 ML-DSA 算法，而标准 `uuid` 包中的 `UUID` 类型是 `[16]byte`，便于与流行的 `google/uuid` 库兼容。

hackernews · database64128 · 8月19日 18:33 · [社区讨论](https://news.ycombinator.com/item?id=49365405)

**核验**: 多源印证

**背景**: Go 语言在 1.18 版本中引入了泛型，允许使用类型参数编写函数和类型。然而，泛型类型上的方法本身不能有额外的类型参数，这一限制在 Go 1.27 中得到了解决。后量子密码学指的是设计用于抵御经典计算机和量子计算机攻击的算法，NIST 正在领导其标准化工作。UUID（通用唯一标识符）是用于唯一标识信息的 128 位数字，`google/uuid` 包一直是 Go 社区的事实标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/golang/go/issues/77273">spec: generic methods for Go · Issue #77273 · golang/go</a></li>
<li><a href="https://go.dev/doc/tutorial/generics">Tutorial: Getting started with generics - The Go Programming Language</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post - Quantum Cryptography | CSRC</a></li>
<li><a href="https://pkg.go.dev/github.com/google/uuid">uuid package - github.com/google/uuid - Go Packages</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了具体的技术细节，如浮点数解析的改进，并提供了实用的迁移见解，例如预计会出现一波替换 `google/uuid` 的 PR。评论赞扬了积极主动的加密团队和泛型方法带来的易用性提升，同时也对 Go 博客缺乏语法高亮提出了轻微的批评。

**标签**: `#golang`, `#programming-languages`, `#software-development`, `#cryptography`, `#open-source`

---

<a id="item-11"></a>
## [Simon Willison 使用 Claude Code 评估 smolvm 作为运行不受信任 Python 和 JavaScript 代码的沙箱。](https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/) ⭐️ 7.0/10

Simon Willison 让在 Claude Code for web 中运行的 Claude Fable 5 执行一项研究任务：评估 smolvm 沙箱，以安全地运行不受信任的 Python 和 JavaScript 代码。当 Claude Code 环境缺少硬件虚拟化支持时，该 AI 自主设计并执行了一个使用 GitHub Actions 来运行测试的解决方案。 这展示了一种解决 AI 智能体开发中关键挑战的实用方法：安全地执行可能有害或资源密集的用户提供代码。AI 主动解决问题的过程，也突显了大语言模型在处理涉及环境限制的复杂、多步骤技术工作流方面日益增强的能力。 Claude Code for web 环境缺少 /dev/kvm 设备和 CPU 虚拟化标志，无法直接使用需要 KVM 的 smolvm。AI 的解决方案是编写一个 GitHub Actions 工作流，在拥有 KVM 访问权限的运行器上安装 smolvm 并执行测试脚本，从而成功测试了沙箱的功能。

rss · Simon Willison · 8月19日 23:16

**核验**: 多源印证

**背景**: Smolvm 是一个开源的沙箱基础设施，它使用微虚拟机（如 Firecracker）来提供快速、隔离的代码运行环境，启动时间不到 200 毫秒。它专为安全执行 AI 生成或用户提交的代码等场景设计，可施加资源限制和网络隔离。Claude Code 是一个由 Anthropic 的 Claude 模型驱动的基于终端的编码环境，有时会限制系统访问，如此处所见，它缺乏嵌套虚拟化支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/CelestoAI/SmolVM">GitHub - CelestoAI/ SmolVM : Open-source AI sandbox infrastructure...</a></li>
<li><a href="https://particula.tech/blog/smolvm-vs-firecracker-sandbox-ai-generated-code">SmolVM vs Firecracker vs Docker: Sandboxing AI-Generated Code</a></li>
<li><a href="https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan">Using Claude Code with your Pro or Max Plan | Anthropic Help Center</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Code Sandbox`, `#AI Developer Tools`, `#Python`, `#JavaScript`

---

<a id="item-12"></a>
## [Jeremy Morrell 提出假设：LLM 与沙盒技术将开启可扩展 Web 软件的新时代。](https://simonwillison.net/2026/Aug/19/jeremy-morrell/) ⭐️ 7.0/10

Jeremy Morrell 发表了一个假设，即大语言模型（LLMs）与现代沙盒技术共同为构建 Web 上的可扩展软件创造了新的机遇。他认为，LLMs 极大地降低了编写扩展的成本，而沙盒技术则降低了部署成本并提供了强大的安全边界，使得应用程序可以拥有一个安全的核心，同时允许用户安全地进行扩展。 这一点很重要，因为它可能实现软件定制的大众化，将权力从开发者转移到最终用户，从而在不牺牲安全性的前提下实现高度个性化的应用程序。这代表了软件架构的一个重大转变，可能催生出跨行业、更具适应性且以用户为中心的 Web 平台。 该假设特别关注 Web 作为平台，并利用基于浏览器的沙盒机制来保障安全。一个关键的技术前提是将用于代码生成的 LLMs 与用于安全执行的沙盒技术相结合，共同应对传统可扩展系统中开发成本高和安全风险大的挑战。

rss · Simon Willison · 8月19日 22:56

**核验**: 多源印证

**背景**: 可扩展软件的设计允许在不改变其核心架构的情况下添加新功能或进行修改，通常通过插件或 API 实现。现代沙盒是一种安全机制，用于隔离运行中的程序，在 Web 浏览器中常用于限制网页代码，防止其损害用户系统。像 GPT-4 这样的大语言模型（LLMs）是能够生成和理解文本（包括代码）的 AI 系统，可以自动化那些以前需要大量人类专业知识才能完成的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sandbox_(computer_security)">Sandbox (computer security) - Wikipedia</a></li>
<li><a href="https://zoer.ai/posts/zoer/extensibility-software-development-guide">What Does Extensibility Mean in Software Development?</a></li>
<li><a href="https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/">Extensible Software in the age of LLMs | Jeremy Morrell</a></li>

</ul>
</details>

**标签**: `#llms`, `#extensible-software`, `#sandboxing`, `#ai-agents`, `#developer-tools`

---

<a id="item-13"></a>
## [分析指出模型缩放必须综合考虑数据、算力和部署，而不仅仅是参数量。](https://x.com/jietang/status/2089941544581403107) ⭐️ 7.0/10

唐杰的分析批评了业界对参数量的狭隘关注，强调了从 Kaplan 等人（2020）到 Hoffmann 等人（2022）及之后的关键研究转变。该分析认为，最优缩放取决于数据量、训练与推理的算力分配以及部署环境，这一点在 Llama-2-7B 等模型和最近的 GLM-5.3 实验中得到了体现。 这一观点对高效 AI 开发至关重要，因为在参数、数据和算力之间错误分配资源会导致投资浪费和模型性能不佳，尤其是在推理成本高昂的情况下。它指导研究者和公司通过平衡多个缩放因子来构建能力更强、成本效益更高的模型。 分析指出，最优的 token 与参数比率取决于具体任务，记忆任务倾向于更多参数，而推理任务则倾向于更多数据。分析还强调，对于 MoE 模型，超过一定点后增加总参数量反而会损害推理能力，而激活更多专家则能提升它。

twitter · jietang · 8月19日 05:04

**核验**: 多源印证

**背景**: 缩放定律描述了模型性能随着算力、数据和参数增加而可预测地提升。Kaplan 等人 2020 年的论文建议参数增长速度应快于数据，催生了 GPT-3 等模型。Hoffmann 等人 2022 年的"Chinchilla"论文修正了这一观点，发现更平衡的算力最优比率约为每参数 20 个 token。这一转变揭示了早期大模型的训练效率低下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2001.08361">[2001.08361] Scaling Laws for Neural Language Models</a></li>
<li><a href="https://www.machinelearningatscale.com/blog/scaling-laws-llms-chinchilla-guide">LLM Scaling Laws: Chinchilla , Compute-Optimal Training, and What...</a></li>

</ul>
</details>

**标签**: `#AI Scaling Laws`, `#Model Efficiency`, `#Research Analysis`, `#Compute Optimization`

---

<a id="item-14"></a>
## [Codex AI 实施安全修复，防止清理操作中意外删除用户文件。](https://x.com/thsottiaux/status/2089891927659585918) ⭐️ 7.0/10

Codex 团队在调查了其内部 GPT-5.6 模型执行非预期破坏性操作（例如在清理临时文件夹时删除用户文件）的报告后，推出了一系列安全变更。修复措施包括明确指示模型在操作前检查删除目标、避免重用 $HOME 等系统环境变量，以及增强执行检查以标记高风险命令。 这很重要，因为它解决了一个主流 AI 编程助手中的关键安全缺陷，直接影响用户信任和数据安全。随着 AI 智能体在开发者工作流程中获得更多自主权，防止意外的文件破坏对于其安全可靠的采用至关重要。 根本原因涉及 GPT-5.6 错误地重用了 $HOME 环境变量进行临时工作，导致格式错误的清理命令指向了实际的用户主目录。团队还构建了重放已观察故障的针对性评估，结果显示这些变更在保持正常编码能力的同时，显著减少了危险行为。

follow_builders · Thibault Sottiaux · 8月19日 01:47

**核验**: 多源印证

**背景**: Codex 是一个 AI 平台和编程助手，通常由 GPT-5.6 等模型驱动，帮助开发者完成编写、调试和重构代码等任务。像 $HOME 这样的系统环境变量是操作系统使用的动态值，用于指向特定目录，例如用户的主文件夹。执行文件系统操作（如清理）的 AI 智能体必须正确处理这些路径，以避免灾难性的数据丢失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codex.chat/">Codex Chat – Free OpenAI Codex Online | AI Coding Agent, No Login</a></li>
<li><a href="https://www.thealgorithmicbridge.com/p/openai-gpt-56-ai-could-do-anything">OpenAI GPT - 5 . 6 : AI Could Do Anything, Then It Met ARC-AGI-3</a></li>
<li><a href="https://wiki.archlinux.org/title/Environment_variables">Environment variables - ArchWiki</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Developer Tools`, `#Codex`, `#Bug Fix`, `#AI Agents`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="5"><span>其他追踪推文</span><span class="archive-tab-count">5</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="13"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">13</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2090215153245495489">@dotey: 智谱联合创始人唐杰老师关于 GLM 5.3 以及模型训练的一些分享： 智谱 GLM-5.3 没有换基模底座，纯靠后训练让编码能力提升 50%。 GLM-5.3 模型的底座是 GLM-5....</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月19日 23:11 UTC · 喜欢 13 · 转发 0 · 回复 1 · 浏览 4389</p>
<p class="archive-item-content">智谱联合创始人唐杰老师关于 GLM 5.3 以及模型训练的一些分享：<br>
<br>
智谱 GLM-5.3 没有换基模底座，纯靠后训练让编码能力提升 50%。<br>
<br>
GLM-5.3 模型的底座是 GLM-5.2，约 743B 参数的混合专家（MoE）模型，每次推理只激活约 40B 参数。团队花了一个月，在长周期环境中做强化学习，编码能力比 GLM-5.2 提升了 50%。<br>
<br>
这里解释一下 MoE：传统模型每次推理要跑完所有参数，MoE 相当于把模型拆成一群“专家”，每次只调用其中几个，推理速度更快、成本更低。<br>
<br>
推文中特别区分了两个概念：<br>
1. 总参数量决定模型学习了多少知识<br>
2. 激活参数量和有效深度决定模型能想多深。<br>
<br>
比如说，让模型去找安全漏洞，主要是依赖的是推理能力，能把一条二十步的推理链完整走到底，相对来说各种安全数据库是次要的。<br>
<br>
至于为什么不换底座也能大幅提升呢？<br>
<br>
AI 模型的扩展（scaling）不止堆参数这一条途径。<br>
<br>
如果梳理下这些年模型训练的发展路线：<br>
<br>
- 2020 年 Kaplan 等人的研究建议参数增长要远快于数据，GPT-3、Gopher 都是这个思路的产物。<br>
<br>
- 2022 年 DeepMind 的 Chinchilla 论文则认为参数和数据应该同步增长，参数大的模型反而是最浪费算力的。<br>
<br>
- 再后来，大家发现模型上线后推理成本远超训练成本，最优解又变成了用更小的模型训更久，比如 Llama-2-7B 每个参数喂了约 290 个 token，Gemma-2-9B 更是喂了 889 个。<br>
<br>
模型能力由很多因素决定：底座大小、预训练数据量、每次前向传播的计算量、后训练。<br>
<br>
对于现阶段，模型后训练还有很大潜力可以挖掘。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/mike_chong_zh/status/2090194486639071547">@mike_chong_zh: 昨天 @screenkite_com 做到了 $300K ARR 。想来分享下。 @hackbearterry 今天在 Threads 上也提到“Vibe Coding 降低做出 Dem...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月19日 21:49 UTC · 喜欢 16 · 转发 1 · 回复 4 · 浏览 889</p>
<p class="archive-item-content">昨天 @screenkite_com 做到了 $300K ARR 。想来分享下。<br>
<br>
 @hackbearterry 今天在 Threads 上也提到“Vibe Coding 降低做出 Demo 的門檻，但是 Demo 不是交付。現在這個時代真正困難的已經不是把東西做出來，而是能夠找到願意為產品買單的客戶，然後讓他們掏錢”<br>
<br>
楼下我分享下具体的故事 https://t.co/xNxzE40hv6</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2090187341365145737">@dotey: Jason Wei 这条推文倒是没聊 AI，聊的是运动和职业思维的关系：你选的运动，可能在悄悄塑造你的职业大脑 推文提出了一个挺有意思的概念：“认知奖励形状”（cognitive rew...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月19日 21:21 UTC · 喜欢 38 · 转发 4 · 回复 10 · 浏览 8286</p>
<p class="archive-item-content">Jason Wei 这条推文倒是没聊 AI，聊的是运动和职业思维的关系：你选的运动，可能在悄悄塑造你的职业大脑<br>
<br>
推文提出了一个挺有意思的概念：“认知奖励形状”（cognitive reward shape），意思是不同运动对大脑的激励模式不一样，而这种模式会潜移默化地影响你在职业中的思维方式。<br>
<br>
Jason 拿自己最喜欢的两项运动举例。<br>
<br>
网球是一项极度强调稳定性的运动。一场比赛打几百分，不管你打出了多漂亮的制胜球，它也只值一分，跟对手送你的非受迫性失误一样。所以网球的赢法就是少犯错、打概率、一分一分磨。<br>
<br>
而且网球是单打独斗，一切只能靠自己。这种思维模式特别像外科医生或飞行员，你做过最完美的一台阑尾手术，和做过最平稳的一趟航班，都不会有额外加分，职业的本质就是高度一致、容错极低。<br>
<br>
但这套思维放到创业上就不太对了。创业是高波动、团队作战、容忍失败、偶尔一把创意能换来指数级回报的游戏，和网球那种&quot;把非受迫性失误降到最低&quot;的心态完全是两个方向。<br>
<br>
足球前锋则更接近创业的奖励形状。哪怕是姆巴佩状态最好的比赛，大部分拿球也没能产生什么。但这不重要，重要的是不断制造机会，只要抓住一两次就能决定比赛。一场 90 分钟的比赛拆开看，绝大部分时间是无效尝试，几分钟是关键杠杆点，几秒钟定胜负。踢一辈子前锋的人，会自然习惯与失败共处，并且对不对称回报保持直觉。<br>
<br>
这个框架有简化的地方：创业同样需要稳定性，足球守门员的奖励形状和前锋也完全不同。<br>
<br>
核心观点倒是没什么问题：大多数人选运动靠的是父母、地理位置、学校开了什么课这些偶然因素，很少有人想过，长期练一项运动会怎样重塑自己感知风险、付出和回报的方式。<br>
<br>
以前我导师跟我分享过一个经验：说不要让孩子学那些一个人就能完成的运动，比如乒乓球、羽毛球；而是去学那些需要集体协作的团队运动，比如足球、篮球、排球，这样能更好的锻炼孩子的协作能力、领导力。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/_jasonwei/status/2090154331358310667">@_jasonwei: Cognitive reward shapes in sports and career Sports are amazing environments to learn. When y...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月19日 19:10 UTC · 喜欢 78 · 转发 7 · 回复 9 · 浏览 15522</p>
<p class="archive-item-content">Cognitive reward shapes in sports and career<br>
<br>
Sports are amazing environments to learn. When you play a sport for thousands of hours, you start to see the world through that sport. It is a simple fact—your biological neural network is being conditioned to respond to the behavior incentivized by the rules of the sport.<br>
<br>
The funny thing is that most people choose their sports for accidental reasons such as parents, geography, or school programs. People rarely think about how the particular sport you play influences how your brain thinks more generally. Going a step further, playing the right sport may even benefit your career.<br>
<br>
My two favorite sports are tennis and soccer. Tennis is one of the best sports for teaching consistency. In tennis, there are hundreds of points in a match, and each point is worth exactly one unit, regardless of whether your opponent made an unforced error or if you constructed the most beautiful point ending with a winner. Tennis is low-variance optimization—you win by reducing unforced errors, playing percentages, and grinding out small advantages. Tennis is also an individual sport, which teaches you to rely on yourself consistently.<br>
<br>
Tennis has a similar cognitive reward shape to professions like being a surgeon or a pilot. Surgery and aviation require consistency, self-accountability, and deep focus. And similar to how you can only win one point at a time in tennis no matter how spectacular it was, there is no extra credit for the best appendectomy or the smoothest SFO-JFK flight. Your craft is to provide consistency with very low tolerance for error.<br>
<br>
On the other hand, the tennis mindset transfers relatively little to entrepreneurship. Entrepreneurship is a high-variance, team game where failure is tolerated and occasional creativity gets rewarded exponentially. Minimizing unforced errors in tennis is a totally different mindset from deciding whether to make a moonshot business move that will likely fail but could potentially net a billion dollars. Obviously I am not saying that tennis players cannot be great entrepreneurs, but I do think it is a totally different cognitive reward shape.<br>
<br>
Being a forward in soccer has a much closer reward shape for entrepreneurship. What a forward in soccer learns is to create many small chances. It is a fact that most of the game, you are not scoring—even if you look at all the times that Mbappe got on the ball in one of his best games, most of those led to nothing! But all that matters is creating enough chances to score once (or a few times) and win the game. If you break down a 90-minute game for a forward, almost all the time is failure or noise, a few minutes will be leverage, and a few seconds will determine the fate of the game. I have not played soccer for thousands of hours, but I can imagine that being a lifetime forward in soccer would teach you to be comfortable with failure and asymmetric returns.<br>
<br>
In summary, I am claiming that there can be substantial value when the cognitive reward shape of your sport mirrors that of your career. I’ll admit that I’ve done some cherry-picking for illustration purposes—entrepreneurship also requires consistency and error avoidance; and goalies in soccer have reward shapes that are very different from strikers. But I think the point stands. If sports shape how we perceive risk, effort, and reward, then we should choose them wisely.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2089991628631191991">@op7418: 豆包手机控制和云电脑做得比 Codex 牛皮呀！ 刚才看豆包上线了云电脑模式，而且它还能支持手机控制本地电脑。 我觉得它在手机控制电脑的连接设计上做得非常自然，体验极佳，甚至比 Codex...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月19日 08:23 UTC · 喜欢 117 · 转发 15 · 回复 92 · 浏览 26225</p>
<p class="archive-item-content">豆包手机控制和云电脑做得比 Codex 牛皮呀！<br>
<br>
刚才看豆包上线了云电脑模式，而且它还能支持手机控制本地电脑。<br>
<br>
我觉得它在手机控制电脑的连接设计上做得非常自然，体验极佳，甚至比 Codex 那些好太多了。<br>
<br>
你只需要在本地电脑发起聊天，手机上就能直接同步看到，然后只需在手机上点一下授权（电脑端完全不需要任何操作），就可以直接获取控制权。<br>
<br>
之后你就能通过手机操作电脑上的任务，响应速度极快，延迟极低。<br>
这次还增加了一个云电脑模式。虽然云电脑本质上是给你分配了一个虚拟机，很多人觉得上面没有自己的数据和信息，干不了什么事。<br>
<br>
但我觉得它内置的连接器（比如我们常说的 MCP）挺有意思的。它可以直接连接你的 Notion、GitHub、飞书、企业微信等应用，直接从中获取你的上下文。<br>
<br>
同时，云电脑也是可以安装 Skill 的。比如我试了一下：<br>
<br>
先让它在云电脑端查找我飞书里所有的会议纪要，并整理出待办事项。<br>
整理完待办后，我通过手机下达指令，让它在云电脑上安装了我自己开发的社交媒体卡片 Skill。<br>
<br>
接着再让它基于这些待办事项去跑任务。<br>
<br>
在这个过程中，安装 Skill 的命令是我在手机上下的，而阅读会议纪要的命令是在电脑上下的。无论是云电脑还是本地电脑，这种跨端控制的体验都非常丝滑。<br>
<br>
在本地电脑上，我也试着让它查找对应目录的文件，并清理了一些大文件，这充分发挥了本地电脑的优势。当然，在有了这个系统以后，我们在手机上同样可以下达对应的清理任务，并直接看到结果。<br>
<br>
还有一个玩法我觉得特别有意思，就是把手机控制电脑当作“文件传输助手”来用。<br>
<br>
比如我在发手机截图的时候，直接指令它“只接收图片，不要做任何操作，不用管它”，它就真的只接收而不做多余响应，非常听话。<br>
<br>
如果你想这么用，建议可以单独开一个聊天窗口，专门把它当作文件传输助手。<br>
<br>
在开始时给这个聊天设置一个提示词，告诉它“凡是发送的文件和图片，接收即可，不需要做任何多余响应”，这样就非常好用了。</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2089941380336644295">Thibault Sottiaux: I was gifted a very fancy new reset button today</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：今天我收到了一个非常花哨的新重置按钮</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月19日 05:03 UTC · 喜欢 6843 · 转发 246 · 回复 1780</p>
<p class="archive-item-content">The author shares a personal anecdote about receiving a fancy physical reset button as a gift.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者分享了一个关于收到一个花哨的物理重置按钮作为礼物的个人轶事。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2089940315268645373">Zara Zhang: I don’t know why anyone would learn Claude Code by reading a book, but apparently it’s a thin...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang: 我不明白为什么有人会通过读书来学习 Claude Code，但这在日本显然很流行...</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 8月19日 04:59 UTC · 喜欢 98 · 转发 4 · 回复 34</p>
<p class="archive-item-content">The author expresses surprise that people in Japan are learning Claude Code from books, linking to an external source.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者对日本有人通过书籍学习 Claude Code 表示惊讶，并附上了外部链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2089931839016468575">Peter Yang: I should build an app (or an agent?) where you get and maintain a streak for how many days yo...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：我应该开发一个应用（或智能体？），用于记录并保持你多少天没有把手机带进卧室。</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 8月19日 04:25 UTC · 喜欢 20 · 转发 0 · 回复 13</p>
<p class="archive-item-content">The author proposes building an app or AI agent to track a streak of days without bringing a phone to the bedroom, noting its positive impact on sleep discipline.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者提议开发一个应用或 AI 智能体，用于追踪不带手机进卧室的天数，并指出这对其睡眠纪律有积极影响。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/bcherny/status/2089924199804711410">Boris Cherny: The small quality of life improvements keep coming. When you’re using Desktop every day, slow...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Boris Cherny: 微小的生活质量改进不断涌现。当你每天使用桌面应用时，缓慢的启动会让应用感觉迟钝。</p>
<p class="source-line">Follow Builders · X 动态 · Boris Cherny · 8月19日 03:55 UTC · 喜欢 486 · 转发 6 · 回复 84</p>
<p class="archive-item-content">The author is working on improving the startup speed of a desktop application to enhance daily user experience.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者正在努力提升一款桌面应用的启动速度，以改善日常用户体验。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/levie/status/2089921630650925170">Aaron Levie: As we’re seeing in case study after case study, it turns out that the amount of value that ca...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Aaron Levie：正如我们在一个个案例研究中看到的，事实证明，AI 模型与最终用户工作流之间所能创造的价值远超许多人的假设或认知。</p>
<p class="source-line">Follow Builders · X 动态 · Aaron Levie · 8月19日 03:45 UTC · 喜欢 182 · 转发 19 · 回复 24</p>
<p class="archive-item-content">Aaron Levie argues that the value created by integrating AI models into end-user workflows is greater than expected, but successfully deploying AI agents in critical enterprise processes requires tailored product experiences and data integration.</p>
<p class="archive-item-translation"><span>中文摘要</span>Aaron Levie 认为，将 AI 模型集成到最终用户工作流中所创造的价值超出预期，但要在关键企业流程中成功部署 AI 智能体，需要量身定制的产品体验和数据集成。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/realmadhuguru/status/2089918106814603728">Madhu Guru: Here’s how to think about the cost of your evals : treat evals like frontier models…establish...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Madhu Guru：关于评估成本的思考方式：像对待前沿模型一样对待评估...</p>
<p class="source-line">Follow Builders · X 动态 · Madhu Guru · 8月19日 03:31 UTC · 喜欢 39 · 转发 2 · 回复 9</p>
<p class="archive-item-content">The post advocates for prioritizing high-quality evaluation to establish a trusted performance baseline for AI products before optimizing for cost efficiency.</p>
<p class="archive-item-translation"><span>中文摘要</span>该帖子主张在优化成本效率之前，应优先进行高质量评估，为 AI 产品建立可信的性能基准。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/ryolu_/status/2089894938934911053">Ryo Lu: first step moving to asia: help me empty my apartment! if you can pick up in SF, place an ord...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Ryo Lu: 移居亚洲第一步：帮我清空公寓！如果你能在旧金山取货，请下单...</p>
<p class="source-line">Follow Builders · X 动态 · Ryo Lu · 8月19日 01:59 UTC · 喜欢 809 · 转发 15 · 回复 60</p>
<p class="archive-item-content">A user announces they are moving to Asia and are selling off items from their San Francisco apartment, using a tool to facilitate local pickups.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位用户宣布将移居亚洲，并正在出售其旧金山公寓的物品，使用工具方便本地取货。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/danshipper/status/2089877888396906801">Dan Shipper: I can reliably tell im hitting a deeper point in a meditation because my nose clears complete...</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Dan Shipper：我可以可靠地判断自己是否进入更深层次的冥想，因为我的鼻子完全通畅了</p>
<p class="source-line">Follow Builders · X 动态 · Dan Shipper · 8月19日 00:51 UTC · 喜欢 34 · 转发 0 · 回复 2</p>
<p class="archive-item-content">A personal observation about nasal clearing as an indicator of deep meditation.</p>
<p class="archive-item-translation"><span>中文摘要</span>关于鼻腔通畅作为深度冥想指标的个人观察。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2089877190422974974">Peter Steinberger: 512GB RAM Studios. Apple was good to us. 🦞 https://t.co/NyvtNH6lRa</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Steinberger：512GB 内存工作室。苹果对我们很好。🦞</p>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 8月19日 00:48 UTC · 喜欢 3294 · 转发 36 · 回复 196</p>
<p class="archive-item-content">A developer shares a brief, non-technical tweet about receiving Apple hardware with 512GB of RAM.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位开发者分享了一条关于收到配备 512GB 内存的苹果硬件的简短、非技术性推文。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2089877083510235328">Peter Yang: 3. AI has landed on top of existing work rather than replacing it 😭 Teams now spent more time...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang: 3. AI 叠加在现有工作之上，而非取代它 😭 团队现在花了更多时间...</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 8月19日 00:48 UTC · 喜欢 3 · 转发 0 · 回复 0</p>
<p class="archive-item-content">The author observes that AI tools are adding to existing workloads rather than replacing them, as teams spend more time managing AI agents without reducing their other tasks.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者观察到，AI 工具正在增加现有工作量而非取代它，因为团队花了更多时间管理 AI 智能体，却没有减少其他任务。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2089877068188471545">Peter Yang: 2. Non-engineers are shipping more code PMs attaching pull requests rose from 3% to 10% in tw...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：2. 非工程师正在交付更多代码——产品经理附上拉取请求的比例在两年内从 3%上升至 10%</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 8月19日 00:48 UTC · 喜欢 2 · 转发 0 · 回复 1</p>
<p class="archive-item-content">Data shows a significant increase in code contributions from non-engineers like product managers and designers over two years, indicating a trend toward broader participation in software development.</p>
<p class="archive-item-translation"><span>中文摘要</span>数据显示，产品经理和设计师等非工程师的代码贡献在两年内显著增加，表明软件开发的参与范围正在扩大。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2089870745174446217">Nikunj Kothari: Life honestly gets a lot simpler if you treat it as if nobody owes you a damn thing. Too many...</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari：如果你把生活当作没人欠你任何东西，生活真的会简单很多。太多...</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 8月19日 00:23 UTC · 喜欢 182 · 转发 13 · 回复 6</p>
<p class="archive-item-content">A motivational post suggesting life becomes simpler when you don&#x27;t expect anything from others and focus on playing &#x27;infinite games&#x27;.</p>
<p class="archive-item-translation"><span>中文摘要</span>一篇励志帖子，建议当你不期待他人给予，并专注于玩&#x27;无限游戏&#x27;时，生活会变得更简单。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2089869693201092848">Garry Tan: If you want SF rent to be $10K/mo for a 1BR (you&#x27;re a NIMBY landlord and you hate newcomers a...</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Garry Tan：如果你希望旧金山一居室租金达到每月 1 万美元（那你就是个邻避主义房东，并且讨厌新来者和年轻人……）</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 8月19日 00:18 UTC · 喜欢 306 · 转发 6 · 回复 23</p>
<p class="archive-item-content">A political tweet criticizing a candidate in a San Francisco election and high housing costs.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条批评旧金山选举候选人和高住房成本的政治推文。</p>
</article>
</div>
</section>
