---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 70 条内容中筛选出 15 条重要资讯。

---

1. [Meta 发布 Muse Spark Open：816B 参数、1M 上下文](#item-1) ⭐️ 9.42/10
2. [AdFection：利用定向广告传播零点击间谍软件](#item-2) ⭐️ 9.0/10
3. [阶跃星辰开放 Step 5 Preview 权重](#item-3) ⭐️ 8.98/10
4. [Meta 如何用 AI 原生工程在八周内构建 Forum 应用](#item-4) ⭐️ 8.4/10
5. [Gemini 4 Argon 在 ARC-AGI-3 取得 97.5% 高分，历史第二](#item-5) ⭐️ 8.4/10
6. [微软 AI 发布 MAI-Base-2：2.8T MoE 模型，FLOPs 效率提升 4.2-12.3 倍](#item-6) ⭐️ 8.4/10
7. [Anthropic 将 Opus 5.5 快速模式从研究预览中正式发布](#item-7) ⭐️ 8.3/10
8. [神经网络本就干净：挑战神经元多语义传统观点](#item-8) ⭐️ 8.0/10
9. [Jev 与 13 个 AI 模型面对电车难题](#item-9) ⭐️ 8.0/10
10. [Antigravity 向付费 Google AI Pro 用户推出 Gemini 4 Argon](#item-10) ⭐️ 7.3/10
11. [谷歌在 Willow 芯片上把“魔态”次品率降到原来的 1/40](#item-11) ⭐️ 7.3/10
12. [OpenAI Codex rust-v0.163.0 新增配置搜索、并行工具，并默认启用 Daybreak](#item-12) ⭐️ 7.0/10
13. [Anthropic 季度营收增长 50%至 168 亿美元，为 IPO 做准备](#item-13) ⭐️ 7.0/10
14. [DeepSeek V4.1 Flash 现已在 OpenCode 中免费](#item-14) ⭐️ 7.0/10
15. [字节 Seed 成立模型安全与对齐部门，全球招募顶尖研究员](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Meta 发布 Muse Spark Open：816B 参数、1M 上下文](https://pytorch.org/blog/muse-spark-open/) ⭐️ 9.42/10

Meta 发布了开源权重模型 Muse Spark Open，总参数 816B（激活 42B），上下文窗口 1M token，已在 Hugging Face 以 Muse Model License 提供。该模型原生多模态（图像、音频、文档），相比 8 月版本增加了安全后训练。 这是目前美国最强大的开源权重模型，面向编码与智能体工作流，可能加剧开源权重 AI 领域的竞争。它为开发者提供了高性能的闭源模型替代方案，可能降低生产成本并提高灵活性。 该模型针对 Apple M5 Ultra Mac Studio 进行了优化，并支持 Unsloth、MLX 等多种模型运行器。在 OpenRouter 上，定价为输入 $1.25/M、输出 $4.25/M，支持图像、视频、音频和 PDF 输入。

aihot · PyTorch：Blog（RSS） · 10月15日 17:55 · [中文阅读](https://aihot.news/items/s80tw5g2v22j1se4bmqejyaq4) · 4 个来源

**核验**: 多源印证

**背景**: 开源权重模型发布训练后的权重，但不一定包含训练数据或代码，这与完全开源模型不同。1M token 的上下文窗口使模型能够处理长文档和复杂的智能体任务，而不会丢失早期信息，从而提高编码和多步骤工作流的效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/muse-spark-open">Introducing Muse Spark Open, The Most Capable US Open‑Weight ...</a></li>
<li><a href="https://dev.meta.ai/models/muse-spark-open">Muse Spark Open - Meta</a></li>
<li><a href="https://huggingface.co/blog/meta-muse-spark-open">Welcome Muse Spark Open: open-weight frontier multimodal ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，Muse Spark Open 在某些基准测试上不如 Qwen3.8 Flash Next 和 GLM 5.3 Flash，表明 Meta 仍需追赶。还有人讨论许可证对大型收入公司提供模型即服务的限制，部分人赞赏 Meta 在确保与多种模型运行器兼容方面的努力。

**标签**: `#AI模型`, `#开源`, `#编码智能体`, `#多模态`, `#Meta`

---

<a id="item-2"></a>
## [AdFection：利用定向广告传播零点击间谍软件](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 9.0/10

公民实验室（Citizen Lab）与 Confiant 揭露了 AdFection 行动：以色列广告公司 Discover-Tech 与间谍软件供应商合作，通过定向在线广告传播零点击漏洞利用程序，即使用户不点击广告也能被追踪和感染。 这标志着雇佣间谍软件通过广告技术生态实现了一种新型且令人警惕的传播管道，威胁到普通互联网用户，并暴露出程序化广告基础设施可能被武器化。它向广告提供商、监管机构和网络安全防御者提出了紧迫的问责问题。 公民实验室的报告详细描述了基于广告的分发和命令与控制基础设施，但对其零点击执行恶意软件的确切机制仍语焉不详。该行动通过庞大的广告网络在全球追踪用户，无论用户是否交互，广告都充当投递载体。

hackernews · jcomp · 10月15日 10:43 · [社区讨论](https://news.ycombinator.com/item?id=50101813)

**核验**: 多源印证

**背景**: 零点击间谍软件是一种无需用户任何交互即可感染设备的恶意软件，通过利用应用或操作系统中的漏洞实现。雇佣间谍软件被出售给政府或私人客户以牟利，常被用于锁定记者、活动人士和异议人士。程序化广告利用实时竞价平台在网站上投放广告；像 Discover-Tech 这样的广告公司可以将广告精准投放到特定个人，可能滥用该能力传递恶意载荷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/1011956/discover-tech-zero-click-ads-spyware">An Israeli firm is sending spyware through online ads ...</a></li>
<li><a href="https://www.reuters.com/legal/litigation/israeli-firm-used-online-ads-run-vast-spy-operation-researchers-say-2026-10-15/">Israeli firm used online ads to run vast spy operation ...</a></li>
<li><a href="https://www.timesofisrael.com/israeli-company-used-online-ads-to-run-vast-spy-operation-researchers-say/">Israeli company used online ads to run vast spy operation ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对“零点击”说法的耸动性表示怀疑，一位广告技术工程师指出报告对实际利用机制一带而过。还有人对以色列科技公司深表不信任，认为其受制于以色列政府，并猜测以色列为何在网络行动上如此出色，提及该国历史及“下载谷”（Download Valley）这一网络犯罪聚集地。

**标签**: `#security`, `#spyware`, `#zero-click`, `#adtech`, `#privacy`

---

<a id="item-3"></a>
## [阶跃星辰开放 Step 5 Preview 权重](https://x.com/StepFun_ai/status/2110717330657616092) ⭐️ 8.98/10

阶跃星辰已开放其 Step 5 Preview 模型的权重，BF16 和 FP8 版本现已上线 Hugging Face 和 ModelScope，并附有技术博客。该模型采用稀疏 MoE 架构，总参数 600B，每个 token 激活 27B，支持 1M token 上下文窗口，并原生支持文本和视觉输入。 此次发布意义重大，因为它为开发者提供了访问前沿级开放权重模型的机会，使他们能够针对编码、软件工程和金融等长周期智能体任务进行构建和微调。这也体现了阶跃星辰对开源 AI 的承诺，可能加速 AI 开发者社区的创新和采用。 该模型针对 NVIDIA GB300 进行了优化，使用 NVFP4 量化时每 GPU 每秒可处理近 8K tokens，并提供了 NVFP4 checkpoint。它支持 SGLang、vLLM、NeMo Automodel 后训练，以及通过 NVIDIA NIM 一键部署，并获得了 NVIDIA 的 Day-0 支持。

aihot · X：阶跃星辰 StepFun (@StepFun_ai) · 10月15日 13:00 · [中文阅读](https://aihot.news/items/v0dw619te36yzweiqtuw7pjxs) · 2 个来源

**核验**: 多源印证

**背景**: 混合专家（MoE）是一种每次仅激活部分参数的架构，能够在较低计算量下实现大规模模型。BF16 和 FP8 是低精度浮点格式，可减少内存占用并提高吞吐量，而 NVFP4 是用于进一步加速的 4 位格式。此类开放权重发布使开发者能够在自己的基础设施上运行、微调和部署模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://researchaudio.io/p/mixture-of-experts-moe-in-large-language-models">Mixture of Experts ( MoE ) in Large Language Models</a></li>
<li><a href="https://tensara.org/problems/nvfp4-quantize">NVFP 4 Quantization | Tensara</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，用户对团队表示尊重，并赞扬开放权重的做法。一位用户评论“开放即胜利”，反映了对此次发布的普遍认可。

**标签**: `#开源AI`, `#模型权重`, `#StepFun`, `#AI开发者工具`, `#大模型`

---

<a id="item-4"></a>
## [Meta 如何用 AI 原生工程在八周内构建 Forum 应用](https://engineering.fb.com/2026/10/15/ml-applications/how-meta-built-forum-ai-native-engineering/) ⭐️ 8.4/10

Meta 工程师将 AI 智能体作为开发流程的参与者而非更快的编码工具，在八周内构建了独立的 Facebook Groups 应用 Forum。他们采用 human-on-the-loop（人在环上）模式，让智能体自主运行规划、实现、构建、测试和修正的迭代循环，而工程师负责设定目标、监控运行并批准结果。 这展示了 AI 原生工程的新范式——以经过验证、可上线生产的产出而非代码量来衡量成功。通过将 AI 从编码环节延伸到规划、测试和验证，该方法展示了人机协作如何放大效果，为行业重塑 AI 开发者工具和自动化工作流提供了可借鉴的工作模型。 自主压测循环在开发期间发现并修复了内存问题，使内存占用和缺页数量大约减半；上线后智能体还协助对用户反馈进行根因分析。值得注意的是，每个交付成果仍须经工程师签字确认，并附有构建结果、测试输出和录制的验证会话。

aihot · Meta Engineering Blog（RSS） · 10月15日 19:00 · [中文阅读](https://aihot.news/items/moaux5xk1dqk4pi3tsx8sabsj)

**核验**: 多源印证

**背景**: 人在环中（human-in-the-loop）指工程师驱动每个步骤、AI 在步骤内部提供自动补全、建议修复或回答问题等辅助；而人在环上（human-on-the-loop）则是由智能体自行运行迭代，工程师监控看板、在偏离时介入并批准结果。AI 原生工程围绕人机协作系统重构工作流程、治理和团队协调，而非简单地在现有流程中叠加 AI 工具。在这种模式下，验证而非编译才是完成标准——任务只有在自动化测试和视觉检查通过后才算完成，从而避免看似合理但未经验证的 AI 代码流入工程师手中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenewstack.io/human-on-the-loop-the-new-ai-control-model-that-actually-works/">Human-on-the-Loop: The New AI Control Model That Actually ...</a></li>
<li><a href="https://www.trulit.com/guides/ai-testing-agents">AI Testing Agents: How Autonomous QA Works in 2026</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#AI原生工程`, `#Meta`, `#开发流程`, `#自动化工作流`

---

<a id="item-5"></a>
## [Gemini 4 Argon 在 ARC-AGI-3 取得 97.5% 高分，历史第二](https://x.com/arcprize/status/2110768288523251762) ⭐️ 8.4/10

Google DeepMind 的 Gemini 4 Argon 在 ARC-AGI-3（Verified）评测中，使用 provider adapter harness 取得 97.5% 的得分（成本 4.8 千美元），标准 harness 得分为 49.8%（成本 5.8 千美元）。这使 DeepMind 成为第二家在 ARC-AGI-3 上得分超过 95% 的前沿 AI 实验室，仅次于 OpenAI GPT-6 Astra 的 99.9%。 这一结果表明，前沿 AI 实验室正在迅速缩小与曾被认为难以企及的抽象推理基准之间的差距。在标准 harness 下的良好表现也说明这一进步并非纯粹依赖厂商特定优化，进一步印证了 AI 系统正接近人类水平的流体智能。 在更早的基准上，Argon 在 ARC-AGI-1 取得 98.5%（每任务 0.16 美元），在 ARC-AGI-2 取得 91.3%（每任务 0.32 美元）。在 25 个公开 ARC-AGI-3 游戏中，Argon 使用的动作数比人类基线少 62%，在 3 个游戏上追平或打破速通纪录，另有 6 个游戏差距在 10% 以内。

aihot · X：ARC Prize (@arcprize) · 10月15日 16:22 · [中文阅读](https://aihot.news/items/cvpbhz4ao2wr6pxpthix2z15c)

**核验**: 多源印证

**背景**: ARC-AGI（通用人工智能抽象与推理语料库）是 François Chollet 于 2019 年提出的基准，用于衡量 AI 系统的流体智能。ARC-AGI-3 是最新版本，属于交互式推理基准，要求 AI 智能体在全新环境中探索、即时获取目标并持续学习，而非只解静态谜题。provider adapter（97.5%）与标准 harness（49.8%）得分差距较大，原因在于 provider adapter harness 保留了不透明的厂商特定推理并支持自动压缩，而标准 harness 则在厂商中立的设置下评估模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，Logan Kilpatrick 等知名人士对结果表示赞赏。评论者指出 Argon 的 97.5% 仅次于 GPT-6 Astra 的 99.9%，并强调其高效性——动作数比人类基线少 62%——是真正推理能力而非暴力搜索的证据。也有讨论聚焦于 provider adapter 与标准 harness 得分之间的巨大差距，凸显评测设置对结果影响之大。

**标签**: `#AI`, `#ARC-AGI`, `#Gemini`, `#前沿模型`, `#评测`

---

<a id="item-6"></a>
## [微软 AI 发布 MAI-Base-2：2.8T MoE 模型，FLOPs 效率提升 4.2-12.3 倍](https://microsoft.ai/news/frontier-pre-training-at-microsoft-ai/) ⭐️ 8.4/10

微软 AI 宣布完成 MAI-Base-2 的预训练，这是一个具有 800 亿激活参数、2.8 万亿总参数的混合专家（MoE）基础模型。该模型在 held-out 评测中的 BPB 低于所有测试过的开源权重模型，并且预训练 FLOPs 效率比 DeepSeek-V4-Pro-Base 高出 4.2 至 12.3 倍。 这一公告标志着前沿规模模型发展的重要里程碑，展示了前所未有的 FLOPs 效率，可能降低大规模 AI 的训练成本和能耗。与 DeepSeek-V4-Pro-Base 的直接对比凸显了微软在 AI 竞赛中的竞争地位，可能影响整个行业未来的模型架构和训练策略。 MAI-Base-2 采用 MoE 架构，总参数 2.8 万亿，其中激活参数 800 亿，这种稀疏度在容量和计算成本之间取得平衡。该模型的 held-out BPB 低于所有测试过的开源权重模型，表明每字节的预测性能更优，而相比 DeepSeek-V4-Pro-Base 的 FLOPs 效率提升 4.2-12.3 倍，表明训练计算利用率有显著改进。

aihot · Microsoft AI：官方博客（网页） · 10月15日 16:09 · [中文阅读](https://aihot.news/items/f7ey01hbckuivmlgen9jq0vaf)

**核验**: 多源印证

**背景**: 混合专家（MoE）模型每次输入只激活一部分参数，从而可以在不按比例增加推理或训练计算量的情况下拥有更大的总参数数量。Bits-per-byte（BPB）是一种衡量编码每个字节数据所需平均比特数的指标，提供了与词汇表大小无关的模型质量度量。FLOPs 效率指的是模型在训练过程中如何有效地利用浮点运算来达到给定性能水平，通常表示为模型质量与所消耗计算量的比率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/understanding-bits-per-byte-bpb-language-model-mehrdad-zakershahrak-my9ec">BPB and cross-entropy loss as better Language model metrics</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#MoE`, `#Microsoft AI`, `#Pre-training`, `#Model Efficiency`

---

<a id="item-7"></a>
## [Anthropic 将 Opus 5.5 快速模式从研究预览中正式发布](https://x.com/ClaudeDevs/status/2110825294655562048) ⭐️ 8.3/10

Anthropic 宣布，Claude 平台上的 Opus 5.5 快速模式不再处于研究预览阶段，并已移除等待名单。该模式提供最高 2.5 倍的推理速度，定价为每百万输入 token 8 美元、每百万输出 token 40 美元，现已登陆 Microsoft Foundry（Azure 托管），Google Cloud 支持即将推出。 此次正式发布使 Anthropic 最强大模型的更快、更高吞吐版本无需等待名单即可供更广泛的开发者使用，这可能加速其在延迟敏感型 AI 应用中的采用。在 Azure 上的可用性以及即将推出的 Google Cloud 支持扩大了企业覆盖范围，可能加剧 AI 模型市场的竞争。 快速模式是相同的 Opus 5.5 模型，但配置为最高 2.5 倍的响应速度，token 价格为标准版的两倍。在 Claude Code 中，快速模式保持不变，并消耗额外的使用额度，这意味着它不包含在订阅配额内，需要按量付费资金；团队版和企业版管理员必须先启用它。

twitter · ClaudeDevs · 10月15日 20:09 · [中文阅读](https://aihot.news/items/e2ssy0a7scpnel6ppyl3r9f2t) · 3 个来源

**核验**: 多源印证

**背景**: 快速模式是 Claude Opus 模型的一种高速配置，通过提高每 token 成本来换取更低延迟，适合实时或交互式应用。Claude 平台是 Anthropic 提供的 API 和网页界面，用于访问其模型；Microsoft Foundry 是 Azure 上的企业 AI 平台，用于构建和部署 AI 代理。使用额度是一种按量付费机制，允许付费 Claude 计划用户在超出包含限制后继续使用服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/fast-mode">Fast mode (research preview) - Claude Platform Docs</a></li>
<li><a href="https://code.claude.com/docs/en/fast-mode">Speed up responses with fast mode - Claude Code Docs</a></li>
<li><a href="https://www.anthropic.com/claude/opus">Claude Opus \ Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans">Manage usage credits for paid Claude plans | Claude Help Center</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Opus 5.5`, `#AI pricing`, `#Claude Platform`, `#Azure`

---

<a id="item-8"></a>
## [神经网络本就干净：挑战神经元多语义传统观点](https://already-clean.goodfire.com/) ⭐️ 8.0/10

Goodfire 发布的一篇研究文章主张，神经网络的表征本质上是干净且可解释的，这与「神经元是多语义的（单个单元打包了多个概念）」的主流观点相反。文章重新审视了著名的「猫与车神经元」，指出表面上的复杂性源于我们自身对概念定义的主观偏见，而非网络本身的架构。 如果神经表征确实是干净的，那么 AI 可解释性和「AI 基因组测序」将变得可行得多，这对 AI 对齐（alignment）有重大影响。这一观点直接挑战了机制可解释性的核心假设，可能重塑研究人员理解与控制大型语言模型的方式。 这篇帖子由 Nick Cammarata 撰写，他曾参与 OpenAI 早期的机制可解释性工作并因此感到悲观，但现在转而主张表征是更干净的。他重新审视了经典的「猫与车神经元」现象，认为该神经元实际上扮演的是一个干净、简单的角色（「V 形神经元」），只是被误标为一个复杂的融合概念。

hackernews · themgt · 10月15日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=50105647)

**核验**: 多源印证

**背景**: 机制可解释性（mechanistic interpretability）是一种通过把神经网络分解成更小、可理解的组成部分——即由神经元、注意力头和它们之间的连接组成的电路（circuit）——来理解网络的方法。长期以来人们观察到神经元呈现「多语义」（polysemantic）特征，即以叠加方式编码多个概念，这使得可解释性看起来极其困难。这篇研究文章挑战了这一假设，认为在更好的工具与框架下，表征其实是干净且可读的，可解释性远比以往认为的更加可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeli.app/story/50105647">Neural Networks Are Already Clean · 174 HN comments | Zeli</a></li>
<li><a href="https://arxiv.org/pdf/2503.01824">representations in neural networks - arXiv.org</a></li>
<li><a href="https://mbrenndoerfer.com/writing/mechanistic-interpretability">Mechanistic Interpretability : Circuits, Induction Heads - Interactive</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（203 条评论）正在积极辩论这些主张的有效性。一些评论者称赞 Nick Cammarata 并将这项工作视为意义重大，把可解释性定位为关键的科学问题；另一些人则认为这些主张超出了实际已证明的范围——指出渐进式特征复杂性和早期训练结构的影响早已为人所知，且与参数过载并不互斥。还有多位评论者对框架本身感到困惑，疑问点在于「神经元角色干净」还是「我们的概念定义只是存在偏见」。

**标签**: `#AI interpretability`, `#neural networks`, `#mechanistic interpretability`, `#research`, `#machine learning`

---

<a id="item-9"></a>
## [Jev 与 13 个 AI 模型面对电车难题](https://zachlandes.com/trolley-problem/) ⭐️ 8.0/10

作者 Zach Landes 采用重采样和多种问题排序方法，让 Jev 和其他 13 个 AI 决策模型测试了多个版本的"电车难题"，以确保结果的稳健性。值得注意的是，Jev 在"杀死 0 人还是 1 人"的选择上也表现出明显困难。 该分析探讨了判别式、面向决策的 AI 模型如何处理道德困境，这与 AI 代理、AI 伦理和自主决策系统直接相关。它提出了一个紧迫的实践问题：这类模型是否应被赋予真实软件和基础设施中关键决策的权限。 作者对每个问题采用了重采样和多种变体/排序，以确保某个偶然的措辞不会主导结果。Jev 是 TypeSafe AI 的"System One"判别式模型，它返回带置信度分数的类型化值而非生成自然语言文本，其输出设计为供软件直接使用。

hackernews · zlandes86 · 10月15日 16:24 · [社区讨论](https://news.ycombinator.com/item?id=50106023)

**核验**: 多源印证

**背景**: Jev 是 TypeSafe AI（一家位于旧金山的公司）开发的专有判别式 AI 模型，于 2026 年 9 月 15 日限量开放早期访问，同时宣布了 4000 万美元的种子轮融资。与生成式预训练 Transformer 模型不同，Jev 执行分类或回归任务，返回类型化值和概率估计，并且可以对推理时提供的类别进行零样本学习。电车难题是一个经典的道德思想实验，询问是否应该让失控的电车转向，以牺牲更少的人而不是更多人的生命，常用于探讨机器伦理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jev_(AI_model)">Jev (AI model)</a></li>
<li><a href="https://jevmodel.org/">Jev AI Model (TypeSafe) — Typed System One Decisions</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了多种担忧：有人担心关键系统会被建成类似客服和银行欺诈部门的"卡夫卡式地狱"，还有人担心 Jev 会被国防公司用于打击目标的决策。作者（zlandes86）解释了他严谨的方法论，其他人引用了阿西莫夫三定律，还有评论者指出 Jev 在"杀死 0 人还是 1 人"的选择上表现出明显困难。

**标签**: `#AI ethics`, `#decision models`, `#AI agents`, `#philosophy of AI`, `#prompt engineering`

---

<a id="item-10"></a>
## [Antigravity 向付费 Google AI Pro 用户推出 Gemini 4 Argon](https://x.com/dotey/status/2110877554945175677) ⭐️ 7.3/10

谷歌的 AI 编程工具 Antigravity 已开始向付费的 Google AI Pro 订阅用户推出 Gemini 4 Argon，并提供独立的每周额度，不占用原有的 Gemini 3.8 Flash 额度。该功能正在逐步推送，建议用户更新到最新版的桌面应用、命令行工具或 IDE 扩展。 此次更新让 Pro 订阅用户能够使用前沿编码模型，增强了 Antigravity 在复杂软件工程任务中的能力。独立的额度确保用户可以在不牺牲其他模型使用的情况下同时利用两个模型，有望提升开发者的生产力和工作流程灵活性。 Argon 的额度仅按周计算，不同于原有的每 5 小时刷新机制，且与 Gemini 3.8 Flash 的额度分开。每周的具体额度和重置日期未说明；消耗量取决于智能体的实际工作量，任务越复杂消耗越快。该功能可在 Antigravity 桌面应用、命令行工具和 IDE 扩展（VS Code、JetBrains）中使用，但 Antigravity IDE 中暂不可用。

twitter · 宝玉 · 10月15日 23:36 · 2 个来源

**核验**: 多源印证

**背景**: Google Antigravity 是一个软件开发平台，AI 智能体可以以不同程度的自主性编写、运行和测试代码。Gemini 4 Argon 是 Google DeepMind 推出的前沿多模态推理模型，于 2026 年 9 月 30 日发布，专为实际编码、企业知识工作和网络防御设计。Google AI Pro 是订阅层级（每月 19.99 美元），提供更高的使用限制和付费模型访问权限，区别于免费层级和更便宜的 Google AI Plus 计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity - Wikipedia</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon - The Keyword</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-4-argon/">Gemini 4 Argon - Model Card — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#AI编程工具`, `#Google Gemini`, `#Antigravity`, `#AI产品更新`, `#开发者工具`

---

<a id="item-11"></a>
## [谷歌在 Willow 芯片上把“魔态”次品率降到原来的 1/40](https://x.com/dotey/status/2110839911339184608) ⭐️ 7.3/10

谷歌量子 AI 团队今天在《科学》期刊发表论文，首次在自家 Willow 量子芯片的实体硬件上验证了“魔态培育”方法。相比此前的方法，新方法把魔态的次品率降到原来的约 1/40，实现了 99.99%的逻辑保真度。 魔态是实现容错通用量子计算的关键瓶颈，它能完成纠错电路无法直接执行的那一项关键操作。降低魔态的制造成本是通往实用量子计算机（用于药物模拟、密码破解等）的决定性一步，因为此前的估算显示一台量子计算机最多可能要拿出 95%的能力专门来造魔态。 不用培育时大约每 1000 份魔态里有 4 份是坏的，用了培育之后大约 1 万份里才有 1 份坏的。代价是浪费率很高——100 次尝试里只有 8 次能留下来。谷歌也指出，这个办法还需在更大规模上验证，仍有很多难题尚未解决。

twitter · 宝玉 · 10月15日 21:07 · 2 个来源

**核验**: 多源印证

**背景**: 量子计算机以量子比特为最小计算单元，但量子比特极其娇气，一点热量或干扰就会出错，因此科学家需要用“量子纠错”（QEC）技术保护数据。不过，通用计算必需的一项关键操作无法在纠错保护下直接执行，于是研究者预先制备一种特殊的“魔态”来启用它，相当于一次性钥匙。此前的方法是“魔态蒸馏”，非常耗费资源；新的“培育”方法则逐道工序检查，发现次品立刻扔掉重来，类似流水线上每道工序都站着质检员。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/">Bringing the magic : Google breaks open a bottleneck in quantum ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Magic_state_distillation">Magic state distillation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantum_error_correction">Quantum error correction</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#Google`, `#Willow`, `#magic states`, `#research`

---

<a id="item-12"></a>
## [OpenAI Codex rust-v0.163.0 新增配置搜索、并行工具，并默认启用 Daybreak](https://github.com/openai/codex/releases/tag/rust-v0.163.0) ⭐️ 7.0/10

OpenAI Codex 发布了 rust-v0.163.0，新增可搜索的 /config 面板、即时后续引导、可自定义的 leader 键（默认 Ctrl+X）、守护进程重启、并行只读工具，并为符合条件的账户默认启用 Daybreak。该版本还包含多项错误修复和文档更新。 此版本通过允许并行执行只读工具和更响应的交互，提升了开发者的生产力。默认启用 Daybreak 表明 OpenAI 正推动 AI 辅助安全，可能改善开发工作流中的漏洞检测。 并行只读工具包括技能、记忆和对话历史查询。leader 键自定义将语音静音移至 F9，快捷键提示在做出选择前保持打开。Daybreak 对符合条件的账户默认启用，codex exec 可在服务器提供访问时使用 OpenAI API 密钥选择它。

github · github-actions[bot] · 10月15日 21:30

**核验**: 多源印证

**背景**: Codex 是 OpenAI 的终端编码代理，帮助开发者进行代码生成和编辑。Daybreak 是一款 AI 驱动的安全工具，用于检测和修补代码中的漏洞。此版本延续了 Codex 作为轻量级、可配置开发者工具的发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/daybreak/">Daybreak | OpenAI for cybersecurity | OpenAI</a></li>
<li><a href="https://www.reco.ai/blog/openai-daybreak-codex-security">OpenAI Daybreak and Codex Security, Explained</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Codex`, `#developer tools`, `#release notes`, `#automation`

---

<a id="item-13"></a>
## [Anthropic 季度营收增长 50%至 168 亿美元，为 IPO 做准备](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 7.0/10

Anthropic 周三向投资者表示，其第三季度营收达到 168 亿美元，环比增长近 50%，并披露了剔除股权激励后的调整后营业利润率为 11%。公司还透露，蒸馏（distillation）业务占营收的 5%至 7%，但在第三季度已大幅削减。 这一财务披露表明 Anthropic 在潜在 IPO 前具有强劲的商业吸引力和盈利能力，可能重塑 AI 行业的竞争格局。营收增长和利润率改善表明，AI 实验室不仅能实现技术突破，还能建立可持续的商业模式。 第一季度营收约为 48 亿美元，第二季度为 115 亿美元，第三季度为 168 亿美元。第三季度，Anthropic 每花费 1 美元算力便产生 1.70 美元营收，蒸馏业务在削减前占营收的 5%至 7%。

rss · Simon Willison · 10月15日 13:04

**核验**: 多源印证

**背景**: 蒸馏是一种做法，即竞争对手 AI 实验室利用更先进模型的输出来训练自己的模型，这种做法可能引发争议，因为它可能在缺乏适当保障的情况下复制能力。Anthropic 一直在积极检测和防止此类攻击，如其最近的博客文章所示。调整后营业利润率是一种财务指标，在剔除股权激励等非现金项目后显示盈利能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/o/operatingmargin.asp">Understanding Operating Margin: Definition & Calculation Formula</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的社区讨论强调了对蒸馏作为知识产权盗窃形式的担忧，一些用户指出，Anthropic 最近的博客文章应让任何使用此类技术的人保持警惕。其他人则就蒸馏的伦理和合法性展开辩论，尤其是在政府对中国 AI 公司提出指控的背景下。

**标签**: `#Anthropic`, `#IPO`, `#revenue`, `#AI industry`, `#business news`

---

<a id="item-14"></a>
## [DeepSeek V4.1 Flash 现已在 OpenCode 中免费](https://x.com/opencode/status/2110635747648909472) ⭐️ 7.0/10

OpenCode 宣布 DeepSeek V4.1 Flash 现已在工具中免费使用。此次集成使用户无需额外费用即可访问该模型。 此举降低了开发者在编码工作流中使用高性能 AI 模型的门槛，可能提升 OpenCode 和 DeepSeek 的采用率。这也反映了 AI 工具提供商在竞争激烈的市场中通过免费层级吸引用户的趋势。 DeepSeek V4.1 Flash 具备原生多模态视觉理解能力和非对称模型结构，相比之前版本在性能、速度和成本上更优。为兼容起见，旧模型名称如 deepseek-v4-flash 和 deepseek-v4-flash-vision-exp 暂时路由到 V4.1-Flash。

twitter · OpenCode · 10月15日 07:35

**核验**: 多源印证

**背景**: OpenCode 是由 Anomaly Innovations 开发的免费开源 AI 编码代理，支持超过 75 家提供商的模型。DeepSeek 是一家以开源权重大型语言模型闻名的中国 AI 公司，V4.1 Flash 是其最新模型，具备增强的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek-V4.1-Flash">DeepSeek-V4.1-Flash</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenCode">OpenCode</a></li>

</ul>
</details>

**标签**: `#AI developer tools`, `#OpenCode`, `#DeepSeek`, `#free model`, `#AI agents`

---

<a id="item-15"></a>
## [字节 Seed 成立模型安全与对齐部门，全球招募顶尖研究员](https://x.com/op7418/status/2110584734342627390) ⭐️ 7.0/10

字节跳动 Seed 成立了专门的模型安全与对齐部门，计划在全球招募 10 位顶尖研究员。研究课题涵盖大模型及 Agent 安全的前沿评测方法与 Benchmark 建设、模型前沿能力对齐训练、自动化 Red Teaming、模型可解释性以及模型能力与行为监控。 这反映了随着模型能力增强和自主性提高，整个行业对 AI 安全的重视日益增加。此举也表明国内主要 AI 实验室正在安全研究方面追赶 OpenAI、Anthropic 等西方同行，并可能为整个行业树立投入安全研究的先例。 字节提供极具竞争力的待遇，且这项工作被认为极具挑战性。帖子强调模型越狱和沙箱逃逸问题频发是设立该部门的紧迫动因，并指出国内在此领域的进展长期落后于 OpenAI 和 Anthropic。

twitter · 歸藏(guizang.ai) · 10月15日 04:13

**核验**: 多源印证

**背景**: AI 安全与对齐是一个前沿交叉学科，旨在确保模型按预期行为且不造成伤害。关键概念包括红队测试（对抗性探测模型漏洞）、可解释性（理解模型决策）以及监控模型输出。CBRN 指化学、生物、放射性及核威胁，高能力 AI 可能加剧这些风险。帖子还警告了 AI 篡改软件、控制设备、编写病毒以及破解密码学的潜在风险，并将国内进展与西方顶尖实验室进行了对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/interpretability">What is AI interpretability? - IBM</a></li>
<li><a href="https://www.minimum-code.com/glossary/ai-red-teaming">What is AI Red Teaming | Minimum Code</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#ByteDance`, `#model alignment`, `#AI agents`, `#industry news`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="14"><span>其他追踪推文</span><span class="archive-tab-count">14</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="4"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">4</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110919336147796377">@dotey: 特斯拉新 Roadster 发布：靠压缩空气喷气在空中翻正落地，马斯克说 2028 年投产，售价未公布 10 月 15 日晚，特斯拉在得州 SpaceX 的 McGregor 试验场直播...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 02:22 UTC · 喜欢 75 · 转发 10 · 回复 20 · 浏览 21815</p>
<p class="archive-item-content">特斯拉新 Roadster 发布：靠压缩空气喷气在空中翻正落地，马斯克说 2028 年投产，售价未公布<br>
<br>
10 月 15 日晚，特斯拉在得州 SpaceX 的 McGregor 试验场直播发布了第二代 Roadster 跑车。这辆车 2017 年就亮过相，当时说 2020 年交付，之后一推再推，拖了将近九年。<br>
<br>
演示里，车开上一段弯曲的大坡道，倒挂着往上跑，然后从坡道尽头冲出去，在空中把车身转回正面，四个轮子落地。之后它又从一排特斯拉车（包括 Semi 电动卡车）上方翻跳过去。马斯克在现场说：“飞行汽车是真的。”<br>
<br>
它靠的是冷气推进器。原理跟吹满的气球一松手就乱窜差不多：碳纤维高压罐里存着压缩空气，从喷口猛地放出去就产生推力，不烧燃料，也没有火焰。特斯拉说推进器的推力是轮胎抓地力上限的四五倍，所以它起步能比只靠轮子快得多。倒挂不掉下来靠的是另一套系统：风扇把车底的空气往外抽，把车吸在坡面上。<br>
<br>
所以这里的“飞”只是几秒钟的喷气跳跃，气放完就没了，离能载人飞一段路的飞行汽车还远。据科技媒体 Glitchwire 报道，演示车把后排座位换成了一个装 260 公斤压缩空气的高压罐，车身四周有 10 个喷口；The Information 此前报道，因为推力和噪音太大，演示车是远程遥控的。这几点特斯拉官方没有确认。<br>
<br>
翻跟头的是最激进的 Rocket 版：单座，只接受邀请购买，不能上公路。零到 60 英里/小时（约 97 公里/小时）加速不到 0.59 秒，极速超过 370 公里/小时。<br>
<br>
普通人能订的是另外两个双座版本。Performance 版没有推进器，靠主动空气动力学和风扇吸地增加抓地力，加速不到 1.6 秒，订金 5 万美元。Thrust 版在车尾加了推进器，加速不到 0.9 秒，限量发售，订金 25 万美元。三个版本续航都超过 480 公里。<br>
<br>
特斯拉没公布售价，订金不等于车价，2017 年说的起步价是 20 万美元。Performance 版的 5 万美元订金分两次付：先付 5000 美元（特斯拉说可全额退），10 天内再补 4.5 万美元，否则订单取消。<br>
<br>
投产时间是马斯克在现场说的 2028 年，特斯拉官方帖子里没有写日期。这辆车的交付时间此前已从 2020 年先后推到 2021、2022、2025 和 2027 年。 https://t.co/6w3qvUw7Ii</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110912965876838704">@op7418: 卧槽，特斯拉这个新的跑车太离谱了 居然能短暂飞行并且在空中调整姿态 演示的时候可以直接跳起来反转然后正常落地 https://t.co/AEP6AVWLKN</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月16日 01:57 UTC · 喜欢 153 · 转发 9 · 回复 59 · 浏览 37413</p>
<p class="archive-item-content">卧槽，特斯拉这个新的跑车太离谱了<br>
<br>
居然能短暂飞行并且在空中调整姿态<br>
<br>
演示的时候可以直接跳起来反转然后正常落地 https://t.co/AEP6AVWLKN</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/cb_doge/status/2110901560435945972">@cb_doge: HOLY SHIT https://t.co/4Q6rs8nfvM</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 01:12 UTC · 喜欢 10419 · 转发 1260 · 回复 353 · 浏览 2715519</p>
<p class="archive-item-content">HOLY SHIT https://t.co/4Q6rs8nfvM</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110875762261996016">@dotey: 😓 美国人去中国出差用 Claude 也是会被封的</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 23:29 UTC · 喜欢 109 · 转发 5 · 回复 62 · 浏览 27492</p>
<p class="archive-item-content">😓 美国人去中国出差用 Claude 也是会被封的</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/antigravity/status/2110866531932316011">@antigravity: We’re rolling out Gemini 4 Argon in Antigravity to paid Google AI Pro subscribers today. Dema...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 22:52 UTC · 喜欢 8501 · 转发 868 · 回复 502 · 浏览 513560</p>
<p class="archive-item-content">We’re rolling out Gemini 4 Argon in Antigravity to paid Google AI Pro subscribers today. Demand has been incredible and we&#x27;ve scaled capacity deliberately to get here. We’ve rolled out a separate weekly-only Argon quota for Pro on top of the existing Gemini bucket for 3.8 Flash so you have the best of Gemini for all your tasks.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110846329341837698">@dotey: Opus 5.5 快速模式取消排队：订阅用户要额外付费，API 价格是标准版两倍 Anthropic 宣布，Claude Opus 5.5 的快速模式结束内测，取消候补名单。还是同一个模...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 21:32 UTC · 喜欢 40 · 转发 3 · 回复 51 · 浏览 23435</p>
<p class="archive-item-content">Opus 5.5 快速模式取消排队：订阅用户要额外付费，API 价格是标准版两倍<br>
<br>
Anthropic 宣布，Claude Opus 5.5 的快速模式结束内测，取消候补名单。还是同一个模型，能力不变，回答写出来的速度最多快 2.5 倍。<br>
<br>
费用不算在订阅里。Pro、Max 等订阅用户在 Claude Code 里用 /fast 打开快速模式后，花费不占套餐额度，直接从“额外用量”扣，也就是套餐之外单独充值、按量付费的钱。套餐额度没用完也一样从额外用量扣，没开额外用量就用不了。团队版和企业版要管理员先开启。Claude Code 这部分规则这次没变。<br>
<br>
用 API 的开发者按 token 付费：每百万输入 token 8 美元，每百万输出 token 40 美元，正好是标准速度 Opus 5.5 的两倍。现在加一个参数就能用，不用再申请。<br>
<br>
微软的 Microsoft Foundry 已上线，Google Cloud 即将上线。<br>
<br>
官方文档：https://t.co/4DftYenv96<br>
Claude Code 快速模式说明：https://t.co/Xol9gUB1c0</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/sundarpichai/status/2110804295352488143">@sundarpichai: Some magical progress towards &quot;magic state&quot; in quantum! Our @GoogleQuantumAI team has demonst...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 18:45 UTC · 喜欢 5926 · 转发 665 · 回复 267 · 浏览 323503</p>
<p class="archive-item-content">Some magical progress towards &quot;magic state&quot; in quantum!<br>
<br>
Our @GoogleQuantumAI team has demonstrated &quot;magic state cultivation&quot; on physical hardware for the first time. The result is a 40x error reduction on our Willow processor vs. previous methods, achieving a state-of-the-art 99.99% logical fidelity.<br>
<br>
It&#x27;s another step towards useful, error-corrected quantum computers to help solve the hardest problems. The result is published in Science today, watch the video below to see how it works</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/blackanger/status/2110793282242723853">@blackanger: 我一个香港的朋友，美国人，昨天跑来深圳参加 Rust 大会，睡了一觉起来，发现 Claude 账号被封了 😆😂</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 18:01 UTC · 喜欢 127 · 转发 4 · 回复 21 · 浏览 42804</p>
<p class="archive-item-content">我一个香港的朋友，美国人，昨天跑来深圳参加 Rust 大会，睡了一觉起来，发现 Claude 账号被封了 😆😂</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110786960080155103">@op7418: Meta 又开始发布开源模型了，发布了 Muse Spark Open。 他们说是迄今为止美国最强大的开源模型。 基于苹果的 MLX 框架做了深度优化。 这个 800B 的模型，居然可以...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 17:36 UTC · 喜欢 39 · 转发 0 · 回复 22 · 浏览 11128</p>
<p class="archive-item-content">Meta 又开始发布开源模型了，发布了 Muse Spark Open。<br>
<br>
他们说是迄今为止美国最强大的开源模型。<br>
<br>
基于苹果的 MLX 框架做了深度优化。<br>
<br>
这个 800B 的模型，居然可以在两台 M5 Ultra Mac Studio 上本地运行。<br>
<br>
在长时任务、复杂软件工程和多步骤推理上很出色。<br>
<br>
总参数是 816B，活跃参数 42B，支持 1T 的上下文窗口，原生支持文本、图像、视频、音频全模态输入。<br>
<br>
在测评基准的分数上，跟 K3 和 GLM-5.3 差不多。<br>
<br>
感觉这波美国全员进步，每家都有新进展。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110668428105363721">@op7418: DeepSeek 居然给他们服务挂机影响的用户补偿了，破天荒啊 补偿是过去 7 天账户消耗的所有 API 的金额，会以赠金的形式退到账户里</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 09:45 UTC · 喜欢 47 · 转发 0 · 回复 32 · 浏览 15133</p>
<p class="archive-item-content">DeepSeek 居然给他们服务挂机影响的用户补偿了，破天荒啊<br>
<br>
补偿是过去 7 天账户消耗的所有 API 的金额，会以赠金的形式退到账户里</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/tianyi/status/2110663080246132855">@tianyi: Between 8:11 and 13:04 (Beijing Time) on October 15, 2026, DeepSeek API service system experi...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 09:24 UTC · 喜欢 1451 · 转发 72 · 回复 188 · 浏览 202359</p>
<p class="archive-item-content">Between 8:11 and 13:04 (Beijing Time) on October 15, 2026, DeepSeek API service system experienced a failure that prevented the API service from functioning properly during that period. We sincerely apologize for the inconvenience and disruption this may have caused. We immediately launched a comprehensive investigation and thorough rectification effort focused on service stability, and have comprehensively reviewed and eliminated single points of dependency to resolutely prevent similar issues from recurring.<br>
<br>
As compensation, we will fully refund the amount consumed within 7 days (10.8-10.14) on your account in the form of credit. The credit will be automatically deposited, and API billing deductions will be made from the credit account first. We apologize once again for the impact this failure had on you, and we thank you for your continued trust and support.<br>
<br>
北京时间 2026 年 10 月 15 日 8:11 至 13:04 期间，我们的服务系统出现故障，导致该时段内 API 服务无法正常使用。对于此次故障给您带来的不便与困扰，我们深表歉意。我们已第一时间启动针对服务稳定性的全面排查和彻底整改，全面梳理并剥离单点依赖，坚决杜绝同类问题再次发生。<br>
<br>
作为补偿，我们将按您账号 7 日内（10.8-10.14）的消耗金额以赠金形式全额返还，赠金自动到账，API 计费扣款先从赠金账户扣除。此次故障对您造成了影响，我们再次致歉，感谢您一直以来的信任与支持。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110656210685071604">@op7418: OpenCode 现在直接把 DeepSeek V4.1 Flash 免费了！ 不过免费版只有 200K 的上下文，付费版有 1M</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 08:57 UTC · 喜欢 34 · 转发 0 · 回复 14 · 浏览 14673</p>
<p class="archive-item-content">OpenCode 现在直接把 DeepSeek V4.1 Flash 免费了！<br>
<br>
不过免费版只有 200K 的上下文，付费版有 1M</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110605686086529470">@op7418: 顺便说一句，JEV 模型这次的更新几乎都命中了我们在 Next Token 20 多天前提到的它需要改进的部分 https://t.co/iE01tWYP5J</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 05:36 UTC · 喜欢 46 · 转发 2 · 回复 8 · 浏览 11147</p>
<p class="archive-item-content">顺便说一句，JEV 模型这次的更新几乎都命中了我们在 Next Token  20 多天前提到的它需要改进的部分 https://t.co/iE01tWYP5J</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110574294564839439">@op7418: 让我的 BOT 帮我做了一张类似的图，感觉在 Twitter 上光是发东西互动比较少 https://t.co/vj1pLZ6QwM</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 03:31 UTC · 喜欢 17 · 转发 1 · 回复 16 · 浏览 6205</p>
<p class="archive-item-content">让我的 BOT 帮我做了一张类似的图，感觉在 Twitter 上光是发东西互动比较少 https://t.co/vj1pLZ6QwM</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2110618732666257557">Thibault Sottiaux: Done and dusted https://t.co/0fehr43VS4</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：完成并搞定</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月15日 06:28 UTC · 喜欢 988 · 转发 49 · 回复 289</p>
<p class="archive-item-content">A brief tweet announcing completion of something, with no details.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条简短推文，宣布某件事已完成，但未提供任何细节。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2110595554036400151">Thibault Sottiaux: Landing within the next 2 hours</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：将在两小时内降落</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月15日 04:56 UTC · 喜欢 2632 · 转发 103 · 回复 425</p>
<p class="archive-item-content">A brief personal announcement about landing within two hours, with no technical or industry relevance.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条关于两小时内降落的简短个人动态，缺乏技术或行业相关内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2110595484180214059">Thibault Sottiaux: The reports of my reset button being lost are greatly exaggerated Day 10/ Reset</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：关于我丢失重置按钮的报道被严重夸大了 第 10 天/重置</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月15日 04:55 UTC · 喜欢 9238 · 转发 493 · 回复 1531</p>
<p class="archive-item-content">A brief, cryptic tweet claiming that the author&#x27;s &#x27;reset button&#x27; is not lost, part of a day 10 reset series.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条简短、隐晦的推文，声称作者的重置按钮并未丢失，属于第 10 天重置系列的一部分。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2110580554370588717">Guillermo Rauch: Yes https://t.co/8sFl6RUqsI</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：是的</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 10月15日 03:56 UTC · 喜欢 140 · 转发 4 · 回复 16</p>
<p class="archive-item-content">A tweet by Guillermo Rauch simply saying &#x27;Yes&#x27; with a link, offering no meaningful information.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 的一条推文，仅说“是的”并附链接，没有提供有意义的信息。</p>
</article>
</div>
</section>
