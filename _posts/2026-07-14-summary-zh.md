---
layout: default
title: "Horizon Summary: 2026-07-14 (ZH)"
date: 2026-07-14
lang: zh
---

> 从 29 条内容中筛选出 9 条重要资讯。

---

1. [腾讯混元发布 HyOCR-1.5：首个全栈开源的端到端 OCR 大模型](#item-1) ⭐️ 7.9/10
2. [Anthropic 新版 tokenizer 隐性涨价约 30%](#item-2) ⭐️ 7.17/10
3. [Seedream 5.0 Pro 测评：交互式局部编辑大幅降低图像编辑门槛](#item-3) ⭐️ 7.12/10
4. [不打开 Xcode 即可构建并发布 Mac 和 iOS 应用](#item-4) ⭐️ 7.0/10
5. [苹果全新 SpeechAnalyzer API 与 Whisper 及前代 API 的基准测试对比](#item-5) ⭐️ 7.0/10
6. [DOOMQL：完全由 SQLite 驱动的 Doom 风格游戏](#item-6) ⭐️ 7.0/10
7. [Datasette 的 GitHub 代码频率图揭示 AI 驱动的生产力激增](#item-7) ⭐️ 7.0/10
8. [德国 AI 协会发布开源模型 Soofi S，在英语和德语基准测试中领先](#item-8) ⭐️ 7.0/10
9. [OpenAI 优化 GPT-5.6 Sol 推理并回退 Codex 的上下文与推理参数变更](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [腾讯混元发布 HyOCR-1.5：首个全栈开源的端到端 OCR 大模型](https://mp.weixin.qq.com/s/vKFCa9FfoGBUGK8J1MhFag) ⭐️ 7.9/10

腾讯混元发布了 HyOCR-1.5，这是端到端 OCR 大模型领域首个将训练、推理和模型权重完整开源的专家模型。仅 1B 参数即在 OmniDocBench v1.6 上以 94.74 分取得端到端第一，并通过 DFlash 投机解码框架实现 6.37 倍推理加速。 此次发布通过完整开源训练、推理和权重，使生产级 OCR 技术走向普惠，开发者可以自由微调和部署高性能文档理解系统。1B 参数的小模型规模、331 种语言的广泛覆盖以及每页 1.408 秒的快速推理，使其在大规模实际部署中极具实用价值。 DFlash 框架使用轻量级块扩散模型在单次并行前向传播中生成整块 token 草稿，在 Transformers 下实现 6.37 倍加速，在 vLLM 下实现 2.14 倍加速。Agentic Data Flow 技术通过智能体循环对困难样本生成额外训练对，显著提升了公开样本不足 1 万条的低资源语言的识别性能。

aihot · 公众号：腾讯混元 · 7月13日 11:12 · [中文阅读](https://aihot.virxact.com/items/cmrj4s89p05nhbilkljqel2d5)

**核验**: 多源印证

**背景**: OCR（光学字符识别）将文本图像转换为机器可读文本，近年来的趋势是使用大型视觉语言模型（VLM）进行端到端文档理解，而非传统的流水线方法。OmniDocBench 是 CVPR 2025 提出的基准测试，为 PDF 页面提供边界框标注和文本识别标签，用于全面评估 OCR 性能。投机解码是一种推理加速技术，通过轻量级草稿模型提出候选 token 再由目标模型验证，从而减少所需的串行前向传播次数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.04884">HunyuanOCR-1.5: Making Lightweight OCR VLMs Faster and Better</a></li>
<li><a href="https://github.com/opendatalab/OmniDocBench">GitHub - opendatalab/OmniDocBench: [CVPR 2025] A ...</a></li>
<li><a href="https://arxiv.org/html/2602.06036v1">DFlash: Block Diffusion for Flash Speculative Decoding</a></li>

</ul>
</details>

**标签**: `#OCR`, `#开源AI`, `#端到端模型`, `#腾讯混元`, `#文档理解`

---

<a id="item-2"></a>
## [Anthropic 新版 tokenizer 隐性涨价约 30%](https://playcode.io/blog/real-price-of-frontier-models) ⭐️ 7.17/10

对 16 个真实测试样本的实测显示，Anthropic 最新 tokenizer（用于 Sonnet 5、Opus 4.8、Fable 5）对相同内容产生的 token 数比上一版多约 30%，而标价保持不变。跨厂商对比表明，Claude 新 tokenizer 在相同代码文件上比 GPT 的 o200k tokenizer 多产生 1.50x 至 1.73x 的 token，其中 TypeScript 差距最大，达到 1.73 倍。 这表明不同厂商的 $/Mtok 标价无法直接比较，因为 tokenizer 差异巨大，依赖公开价格表的开发者可能低估 Claude 实际成本 30% 至 73%，具体取决于内容类型。这一发现迫使团队重新评估成本预测和厂商选型，尤其是在 token 膨胀最严重的代码密集型场景中。 该研究仅测量输入 tokenization，使用各厂商官方 token 计数端点，覆盖 16 个测试样本，包括英文散文、HTML、JavaScript、Python、TypeScript、Rust、JSON schema 和中文文本。按实际效果计算，Opus 4.8 的 $5/$25 每百万 token 相当于 $7.50/$37.50，而 Sonnet 5 在促销价到期后（2026 年 8 月 31 日）实际等效成本将达到 $4.50/$22.50，而非促销期的 $2/$10。

aihot · Hacker News 热门（buzzing.cc 中文翻译） · 7月13日 21:50 · [中文阅读](https://aihot.virxact.com/items/cmrjrg5aj0202bis4f9pzo8d3)

**核验**: 多源印证

**背景**: Tokenization 是 LLM 厂商将原始文本切分为数值 token 供模型处理的过程，API 定价按 token 数收费。各厂商使用不同的 tokenizer，同一段文本在不同模型下产生的 token 数不同，因此价格页上的 $/Mtok 指标仅反映单 token 价格，并未考虑你的内容实际会产生多少 token。Anthropic 在发布 Sonnet 5 和 Opus 4.8 时更新了 tokenizer，改变了文本切分方式但未调整标价。这使得跨厂商价格比较具有误导性，除非同时测量特定工作负载下的实际 token 数量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Tokenizer_large_language_model">Tokenizer (large language model)</a></li>
<li><a href="https://www.aicosts.ai/learn/what-is-token-based-pricing">Token-Based Pricing Explained (LLM APIs, 2026) - aicosts.ai</a></li>

</ul>
</details>

**标签**: `#tokenizer`, `#AI模型成本`, `#Claude`, `#GPT`, `#API定价`

---

<a id="item-3"></a>
## [Seedream 5.0 Pro 测评：交互式局部编辑大幅降低图像编辑门槛](https://x.com/op7418/status/2076604797202161800) ⭐️ 7.12/10

字节跳动发布了 Seedream 5.0 Pro 多模态图像生成模型，综合能力接近 OpenAI 的 GPT-Image 2.0。其核心亮点是交互式局部编辑——用户可在图上打点、画框、涂鸦，并在提示词中用 @ 标记实现精准局部编辑（如换沙发、改墙面颜色），其他区域保持不变。 打点/画框/涂鸦的交互式编辑范式大幅降低了专业级图像编辑的门槛，使家装改造可视化、商品图制作、海报排版等复杂商业设计任务对非专业用户变得可行。API 已在火山引擎全量上线，开发者可以立即将其集成到生产流程中。 实测场景包括一次替换六件家具的家装改造、带卖点标注的键盘爆炸拆解图，以及通过框定位置生成文字的海报排版。模型还支持色卡配色和 SKU 换色，用户可通过即梦、豆包和 Lumina 平台体验。

aihot · X：歸藏 (@op7418) · 7月13日 09:48 · [中文阅读](https://aihot.virxact.com/items/cmrj2yiav054pbilkyf6ufbw2)

**核验**: 多源印证

**背景**: Seedream 是字节跳动的 AI 图像生成模型系列，5.0 Pro 是最新版本，专注于精确视觉编辑、分层设计和多语言排版等专业生产能力。GPT-Image 2.0（ChatGPT Images 2.0）是 OpenAI 于 2026 年 4 月发布的最先进图像生成模型，具备改进的文字渲染、多语言支持和高级视觉推理能力。火山引擎是字节跳动的云服务平台，提供包括 Seedream 系列在内的 AI 模型 API 接入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/seedream5_0_pro">Seedream 5.0 Pro - seed.bytedance.com</a></li>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-0/">Introducing ChatGPT Images 2.0 | OpenAI</a></li>
<li><a href="https://www.volcengine.com/docs/82379/1541594">获取 API Key 并配置--火山方舟-火山引擎</a></li>

</ul>
</details>

**标签**: `#AI图像生成`, `#Seedream`, `#字节跳动`, `#图像编辑`, `#API`

---

<a id="item-4"></a>
## [不打开 Xcode 即可构建并发布 Mac 和 iOS 应用](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 7.0/10

一位开发者展示了一套完整的工作流，可以在完全不打开 Xcode 的情况下构建并发布 Mac 和 iOS 应用，全程使用 Claude 等 AI 代理处理整个开发流程。该方法依赖于预先配置好的工具链，使 AI 代理能够独立管理编译、签名和部署。 这挑战了长期以来 Xcode 是 Apple 平台开发必备工具的假设，表明 AI 驱动的工作流已经可以绕过 Apple 生态中最受批评的工具之一。这标志着 AI 代理正在变得足够强大，能够处理端到端的开发流程，有望为对 Xcode 复杂性感到沮丧的开发者降低门槛。 该工作流需要在 Mac 上本地运行 AI 代理而非在沙盒环境中，这带来了安全风险，社区成员引用了 xAI 上传用户主目录的事件来强调这一点。替代工具如 xtool（github.com/xtool-org/xtool）甚至可以在 Linux 上进行 iOS 应用开发和本地安装，无需通过 TestFlight 或 App Store 上传。

hackernews · speckx · 7月13日 18:22 · [社区讨论](https://news.ycombinator.com/item?id=48896665)

**核验**: 已核对原文

**背景**: Xcode 是 Apple 官方的集成开发环境（IDE），用于构建、测试和部署 macOS 和 iOS 平台的应用程序。

**社区讨论**: 社区成员对本地运行 AI 代理提出了重大安全担忧，一位用户引用了 xAI 上传某人主目录（包括 SSH 密钥）的事件作为警示。也有人对此前提提出异议，指出近期的 Xcode 版本（尤其是 Xcode 27 beta 3）非常稳定，类型检查也有改进。多位用户推荐了 xtool 等替代工具用于跨平台 iOS 开发，一位开发者报告称完全在 Linux 上成功构建和测试了 iOS 应用。

**标签**: `#AI agents`, `#iOS development`, `#AI developer tools`, `#automation workflow`, `#Xcode alternatives`

---

<a id="item-5"></a>
## [苹果全新 SpeechAnalyzer API 与 Whisper 及前代 API 的基准测试对比](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) ⭐️ 7.0/10

苹果在 iOS 26 和 macOS 26 中推出了全新的原生语音转文字 API SpeechAnalyzer，取代了 iOS 10 中引入的 SFSpeechRecognizer，目前已有第三方基准测试将其与 OpenAI 的 Whisper-Large-V2 及苹果旧版 API 进行了对比。结果显示 SpeechAnalyzer 在速度和准确率上具有竞争力，但苹果官方并未公布任何准确率数据。 苹果推出的具有竞争力的原生 ASR API 可能会严重冲击大量开发者基于 Whisper 构建的付费封装应用生态，同时为苹果平台开发者提供一个免费、端侧、无需外部依赖的语音识别方案。这也标志着苹果在依赖老旧的 SFSpeechRecognizer 近十年后，重新加大对语音技术的投入。 基准测试在数学讲座转录等任务上将 SpeechAnalyzer 与 Whisper-Large-V2 进行了对比，发现其速度大幅领先但准确率略低。值得注意的是，SpeechAnalyzer 目前缺少旧版 SFSpeechRecognizer 所提供的自定义词汇表功能，该功能允许开发者注册已知关键词以提高特定领域术语的识别准确率。

hackernews · get-inscribe · 7月13日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48894752)

**核验**: 多源印证

**背景**: SFSpeechRecognizer 是苹果在 iOS 10 中引入的语音识别框架，近十年来提供端侧和基于服务器的转录能力。OpenAI 的 Whisper 于 2022 年 9 月作为开源软件发布，成为语音转文字的事实标准，催生了大量封装应用和优化库，如针对 Apple Silicon 优化的 WhisperKit。此后 ASR 领域持续演进，Nvidia 的 Nemotron 和 Parakeet、Mistral 的 Voxtral 以及 Cohere Transcribe 等新模型不断推动准确率的提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer-mdn.apple.com/videos/play/wwdc2025/277/">Bring advanced speech -to-text to your app with... - Apple Developer</a></li>
<li><a href="https://get-inscribe.com/blog/apple-speech-api-benchmark.html">Apple 's New Speech API vs Whisper: The First Real Benchmark</a></li>
<li><a href="https://www.argmaxinc.com/blog/apple-and-argmax">Apple SpeechAnalyzer and Argmax WhisperKit - Argmax</a></li>

</ul>
</details>

**社区讨论**: 社区反馈褒贬不一：部分用户称赞 SpeechAnalyzer 在实时转录场景下的速度表现，而另一些用户则认为 Whisper 已不再是合适的基准对比对象，应与 Nemotron、Voxtral 和 Cohere Transcribe 等 SOTA 模型进行比较。多位评论者预测付费 Whisper 封装应用将走向消亡，有人指出语音转文字正接近成为已解决的问题。还有用户推荐了 Willow 和 Superwhisper 等 macOS 转录工具。

**标签**: `#speech-to-text`, `#Apple API`, `#ASR benchmark`, `#Whisper`, `#developer tools`

---

<a id="item-6"></a>
## [DOOMQL：完全由 SQLite 驱动的 Doom 风格游戏](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) ⭐️ 7.0/10

Peter Gostev 使用 OpenAI 最新发布的 GPT-5.6 Sol 模型构建了 DOOMQL，这是一款终端中的 Doom 风格游戏，其中 SQLite 负责游戏的所有方面——移动、碰撞、敌人、战斗、进度，甚至通过递归 CTE 光线追踪器渲染屏幕上的每个像素。该项目以简单的 Python 脚本形式运行。 DOOMQL 证明了 SQLite——一个轻量级嵌入式数据库——可以作为完整的游戏引擎，将 SQL 的能力推向了超越数据存储的边界。它还展示了 GPT-5.6 Sol 令人印象深刻的代码生成能力，表明 AI 辅助开发已经能够应对越来越复杂和非常规的软件项目。 渲染通过一个使用递归 CTE 的庞大 SQL 查询实现，完全在 SQLite 内部执行光线追踪，通过包含 x、y、r、g、b 列的 frame_pixels 视图输出像素数据。游戏状态存储在本地 SQLite 数据库 /tmp/doomql/.doomql/doomql.sqlite 中，可以使用 Datasette 进行探索，Simon Willison 甚至利用新的 Datasette Apps 插件构建了一个带有小地图的实时网页查看器。

rss · Simon Willison · 7月13日 22:34

**核验**: 多源印证

**背景**: SQLite 是一种广泛使用的嵌入式关系型数据库，以轻量级和无服务器著称，通常用于数据存储而非游戏引擎这样的计算密集型任务。递归 CTE（通用表表达式）是一种 SQL 特性，允许查询引用自身，从而实现迭代计算，例如遍历树结构，或者在本例中模拟光线追踪。GPT-5.6 Sol 是 OpenAI 于 2026 年 7 月发布的最新前沿模型，在编程、科学和网络安全方面具有最先进的能力。Datasette 是一个用于探索 SQLite 数据库的开源工具，其新的 Apps 插件允许构建自定义的 HTML+JavaScript 界面，直接在 Datasette 的 Web UI 中运行 SQL 查询。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>
<li><a href="https://docs.astral.sh/uv/">uv is an extremely fast Python package and project manager, written...</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#AI Developer Tools`, `#Technical Implementation`, `#Open Source`, `#Game Engine`

---

<a id="item-7"></a>
## [Datasette 的 GitHub 代码频率图揭示 AI 驱动的生产力激增](https://simonwillison.net/2026/Jul/13/datasette-code-frequency/#atom-everything) ⭐️ 7.0/10

Simon Willison 观察到他的 Datasette 项目在 GitHub 上的代码频率图显示，2026 年单周代码新增量达到 37,022 行的空前峰值，远超此前所有高峰，且与采用 Opus 4.5 级别模型驱动的 AI 编程助手的时间线吻合。他指出 Opus 4.8、GPT-5.5、Fable 5 和 GPT-5.6 Sol 是与这一产出激增相对应的模型。 这张图表提供了最有说服力的真实世界数据佐证之一，展示了 AI 编程助手如何极大地改变开发者的生产力和开源产出。它提供了一个具体的量化指标，证明了高级大语言模型对个人开发者代码产出能力的巨大影响。 2026 年的峰值（37,022 行新增、-9,528 行删除）大约是 2018 年初约 15,000 行新增这一此前最高峰值的 2.5 倍，图表时间跨度从 2018 年到 2026 年，活动呈间歇性爆发。Willison 指出这是他迄今为止找到的最佳例证，表明该数据属于观察性而非受控实验结果。

rss · Simon Willison · 7月13日 21:45

**核验**: 多源印证

**背景**: Datasette 是 Simon Willison 的开源项目，围绕 SQLite 数据库和 Python Web 应用构建，用于探索、发布和共享结构化数据。GitHub 的代码频率图显示仓库历史中每周的代码新增和删除数量，提供开发活动的时间线可视化。Claude Opus 4.5 是 Anthropic 的前沿推理模型，专为复杂软件工程和智能体工作流优化，代表了越来越多开发者用于自动化编程任务的模型类别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/datasette">GitHub - simonw/datasette: An open source multi-tool for ... GitHub - simonwillison/datasette: Decentralized protocol ... Simon Willison: Datasette: The annotated release notes Datasette Newsletter | Simon Willison | Substack Official project website for Datasette, building a search ... Simon Willison's AI-Augmented Datasette Ecosystem: Agent ...</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-5">Introducing Claude Opus 4 . 5 \ Anthropic</a></li>
<li><a href="https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/analyzing-changes-to-a-repositorys-content">Analyzing changes to a repository's content - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Developer Productivity`, `#Open Source`, `#GitHub`, `#Simon Willison`

---

<a id="item-8"></a>
## [德国 AI 协会发布开源模型 Soofi S，在英语和德语基准测试中领先](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german) ⭐️ 7.0/10

德国 AI 协会协调的研究联盟发布了 Soofi S 30B-A3B，一个完全开源的 MoE 模型，总参数量 316 亿，每个 token 仅激活约 32 亿参数，采用 Mamba-2 与标准注意力层混合的架构。该模型在所有完全开源模型中取得英语和德语综合最高分，超越 OLMo 3 32B 和 Apertus 70B，同时支持最高 100 万 token 的上下文窗口，在 4 万 token 长度下生成吞吐量约为同规模稠密模型的 8 倍。 Soofi S 证明了 Mamba-2 与注意力混合的 MoE 架构能够在完全开源模型中实现最先进性能，同时保持高推理效率，为纯 Transformer 设计提供了有吸引力的替代方案。其出色的双语表现也凸显了构建以非英语为中心的竞争性开源模型的可行性，这对欧洲 AI 生态系统推动数字主权具有重要意义。 该模型完全在德国电信慕尼黑工业 AI 云上训练，训练数据中德语占比从第一阶段的 7.2%提升至第二阶段的 15.3%。在编程基准测试中，HumanEval 得分 73.8%，MBPP 得分 70.2，德语版 MBPP 得分 84.2，模型权重已开源发布。

aihot · The Decoder：AI News（RSS） · 7月13日 11:41 · [中文阅读](https://aihot.virxact.com/items/cmrj6actv0651bilkm5pfz6ub)

**核验**: 多源印证

**背景**: 混合专家（MoE）是一种架构，每个 token 仅激活模型参数（专家）的一个子集，从而允许更大的总参数量而不会按比例增加计算成本。Mamba-2 由 Tri Dao 和 Albert Gu 于 2024 年提出，是一种通过硬件-算法协同设计实现高效序列建模的状态空间模型架构，为 Transformer 中的二次方注意力机制提供了替代方案。将 Mamba-2 层与传统注意力层在混合 MoE 设置中结合，旨在利用两种方法的优势——Mamba 的线性时间序列处理和注意力的精确 token 级交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture)">Mamba (deep learning architecture) - Wikipedia</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#开源大模型`, `#MoE架构`, `#Mamba-2`, `#多语言AI`, `#模型发布`

---

<a id="item-9"></a>
## [OpenAI 优化 GPT-5.6 Sol 推理并回退 Codex 的上下文与推理参数变更](https://x.com/thsottiaux/status/2076495156757577895) ⭐️ 7.0/10

OpenAI 为 GPT-5.6 Sol 上线了推理优化，使所有订阅用户的用量额度增加约 10%，同时将上下文大小限制从 372k 回退至 272k，因为发现此前变更导致 Codex 和 ChatGPT Work 用户出现非预期的用量消耗。团队还回退了对内部推理努力参数（称为 'juice values'）的实验性修改，并正在修复高和超高推理模式下多智能体用量过多的问题。 这些变更直接影响 Codex 和 ChatGPT Work 用户的日常生产力，此前上下文大小和推理努力参数的变更导致用户用量消耗过快。OpenAI 对 'juice values' 和多智能体行为等内部参数的透明披露，为外界了解其推理算力分配机制提供了罕见的视角。 上下文大小从 GPT-5.5 的 272k 增加到 GPT-5.6 Sol 的 372k，但意外导致用量计费超出预期；OpenAI 计划在修复后于未来几天重新推出 372k 限制。5 小时用量限制暂时仍然关闭，自动审查效率优化以及高和超高推理模式下多智能体过度生成的问题也正在修复中。

follow_builders · Thibault Sottiaux · 7月13日 02:33

**核验**: 多源印证

**背景**: Codex 是 OpenAI 面向软件工程任务的 AI 编程智能体，可通过 ChatGPT 网页应用、CLI 工具、桌面应用和 IDE 集成使用，截至 2026 年 3 月已拥有超过 200 万周活跃用户。'Juice values' 是 OpenAI 对推理努力参数的内部称呼，控制模型在生成回复前投入多少计算预算进行内部推理，数值越高代表推理越深入。上下文大小限制决定模型单次请求中可处理的输入文本量（以 token 为单位），更大的上下文会消耗更多用量配额。多智能体设置涉及多个模型实例协作完成任务，其用量成本会随推理努力等级成倍增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent)</a></li>
<li><a href="https://x.com/btibor91/status/2018754586123890717">Tibor Blaho on X: "Looks like the Juice (reasoning effort) values for GPT-5.2 Thinking in ChatGPT have been updated - ChatGPT Plus & Business - Standard (64 -> 32) and Extended (256 -> 128) - ChatGPT Pro - Light (16 -> 8), Standard (64 -> 16/32), Extended (256 -> 128) and Heavy (512)" / X</a></li>
<li><a href="https://www.reddit.com/r/ChatGPTPro/comments/1mpnhjr/gpt5_reasoning_effort_juice_how_much_reasoning/">r/ChatGPTPro on Reddit: GPT-5 Reasoning Effort (Juice): How much reasoning "juice" GPT-5 uses in the API vs ChatGPT, depending on the action you take</a></li>

</ul>
</details>

**标签**: `#Codex`, `#ChatGPT`, `#AI Developer Tools`, `#OpenAI`, `#Product Update`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="0"><span>其他追踪推文</span><span class="archive-tab-count">0</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="7"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">7</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<p class="archive-empty">今天该来源没有其他未入选内容。</p>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2076553742883930455">Peter Steinberger: I shard my work over ~5 machines via Jump Desktop, this is just my beefiest machine.</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 7月13日 06:26 UTC · 喜欢 54 · 转发 0 · 回复 7</p>
<p class="archive-item-content">Peter Steinberger casually mentions sharding work across ~5 machines using Jump Desktop, highlighting his most powerful machine.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2076552605262872904">Peter Steinberger: That&#x27;s about as many sessions as my Mac Studio can take. https://t.co/4OCiZUwqHt</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 7月13日 06:21 UTC · 喜欢 487 · 转发 7 · 回复 82</p>
<p class="archive-item-content">Peter Steinberger mentions that his Mac Studio has reached its limit for concurrent AI sessions.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2076551622227095828">Peter Steinberger: Spent the weekend on a little facelift. https://t.co/STWHLV5OMy</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 7月13日 06:17 UTC · 喜欢 347 · 转发 8 · 回复 49</p>
<p class="archive-item-content">Peter Steinberger tweeted about spending a weekend on a minor visual update, with no further technical details provided.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2076534860064416115">Garry Tan: Craven politicians who disable public safety technology for virtue signal and culture war pur...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 7月13日 05:11 UTC · 喜欢 111 · 转发 9 · 回复 8</p>
<p class="archive-item-content">Garry Tan criticizes politicians who disable public safety technology for virtue signaling and culture war purposes.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2076519927843000448">Peter Yang: Seeing this quite often today. My wild guess is 90%+ of people are using GPT 5.6 Sol and &amp;lt;...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月13日 04:11 UTC · 喜欢 33 · 转发 1 · 回复 16</p>
<p class="archive-item-content">Peter Yang speculates without evidence that the vast majority of users are on GPT 5.6 Sol rather than Terra or Luna models.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2076512796481880270">Peter Yang: There&#x27;s a tendancy when community sentiment turns to communicate less and in a more corporate...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月13日 03:43 UTC · 喜欢 10 · 转发 2 · 回复 1</p>
<p class="archive-item-content">Peter Yang: There&#x27;s a tendancy when community sentiment turns to communicate less and in a more corporate...</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2076510899490480228">Peter Yang: Anthropic makes great models too but I don&#x27;t understand why they communicate like this. I thi...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月13日 03:35 UTC · 喜欢 142 · 转发 1 · 回复 26</p>
<p class="archive-item-content">Peter Yang tweets that Anthropic should engage the community more directly like OpenAI does, rather than using their current communication style.</p>
</article>
</div>
</section>
