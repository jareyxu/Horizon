---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 68 条内容中筛选出 12 条重要资讯。

---

1. [Meta 开源发布 Muse Spark Open：816B 参数多模态模型](#item-1) ⭐️ 9.12/10
2. [Gemini 4 Argon 在 ARC-AGI-3（Verified）评测中取得 97.5%](#item-2) ⭐️ 8.4/10
3. [Anthropic Opus 5.5 快速模式结束研究预览并登陆 Microsoft Foundry](#item-3) ⭐️ 8.3/10
4. [Google Antigravity 向付费 AI Pro 用户开放 Gemini 4 Argon](#item-4) ⭐️ 8.3/10
5. [Google 在 Willow 量子芯片上首次实现"魔态培育"](#item-5) ⭐️ 8.3/10
6. [Goodfire 提出神经网络是「干净的」，多义性源自人类概念偏见](#item-6) ⭐️ 8.0/10
7. [GNOME 博客文章引发关于用 AI 代理逆向工程硬件的讨论](#item-7) ⭐️ 8.0/10
8. [阶跃星辰发布 Step 5 Preview：600B MoE 开源权重模型，面向长时程智能体](#item-8) ⭐️ 7.95/10
9. [Anthropic 的 Claude Code 团队将代码审查转向机器优先阅读](#item-9) ⭐️ 7.92/10
10. [NVIDIA 开源 Nemotron 3.5 Super VL 及端侧 Bolt 模型](#item-10) ⭐️ 7.75/10
11. [Meta 以 AI 智能体作为开发参与者打造 Forum 应用](#item-11) ⭐️ 7.65/10
12. [DeepSeek V4.1 Flash 在 OpenCode 中免费开放](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Meta 开源发布 Muse Spark Open：816B 参数多模态模型](https://pytorch.org/blog/muse-spark-open/) ⭐️ 9.12/10

Meta 已在 Hugging Face 上以 Muse Model License 发布开源权重模型 Muse Spark Open，总参数 816B、激活参数 42B，上下文窗口达到 1M token，并原生支持图像、音频与文档多模态。该模型面向编码与智能体工作流，并相比 8 月发布的 Muse Spark 增加了安全后训练。 这是迄今规模最大的开源权重发布之一，而其稀疏 MoE 架构让 816B 参数的模型能以接近小得多的稠密模型的成本进行推理，对于希望获得接近前沿能力、又不想按 token 付费调用 API 的团队意义重大。这也表明 Meta 正在直接争夺近期被 Qwen、GLM 等中国开源模型占据的编码与智能体赛道。 Muse Model License 并非完全宽松的开源许可：据一位评论者查阅，它限制被许可方及其关联方在合计毛收入超过约 2000 万美元后把该模型作为托管服务对外提供。Meta 同时在部署生态上投入颇多，官方部署文档列出了 Unsloth、MLX 等运行器，模型也可通过 OpenRouter 访问；不过此次发布的摘要本身并未给出架构细节或评测数据。

aihot · PyTorch：Blog（RSS） · 10月15日 17:55 · [中文阅读](https://aihot.news/items/s80tw5g2v22j1se4bmqejyaq4) · 2 个来源

**核验**: 多源印证

**背景**: MoE（混合专家）模型把参数拆分成许多“专家”子网络，每个 token 只被路由到其中少数几个，因此模型可以拥有极大的总参数量，而每次前向计算只用到一小部分“激活”参数——这里是 816B 中的 42B。这正是 816B 模型仍具备可运行性的原因，不过完整权重加载仍需要相当可观的显存。1M token 上下文窗口意味着模型可以在单次提示中处理约一百万个 token，远超目前仍最常见的 256K 上限。“开源权重”指训练后的权重可下载自托管，而不只能通过 API 访问；Muse Spark 则是 Meta 个人 AI 智能体 Muse 背后的多模态模型家族。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/zh/moe">混合专家模型（MoE）详解 - Hugging Face</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2086958500740067665">Meta Muse 上手：它是什么，怎么注册 - 知乎</a></li>
<li><a href="https://ofox.io/zh/blog/what-is-a-context-window-token-limits-by-model-2026/">【 上 下 文 窗 口 】 1 M 到底能装多少内容：9 个 模 型 实 测，token...</a></li>

</ul>
</details>

**社区讨论**: 评论者对这是否算真正“开源权重”看法不一：一位读者查阅许可后指出其中含有“Model as a Service”条款，在收入超过约 2000 万美元后即生效；另一位则提到 Artificial Analysis 的评测显示它落后于 Qwen3.8 Flash Next 与 GLM 5.3 Flash，而这两者都能在单张 B300 上运行。也有人认为 Meta 把智能“商品化”、围绕粘性极强的 Muse 网络构筑护城河的做法是正确的，还有多位评论者称赞其广泛的运行时支持（Unsloth、MLX）；Simon Willison 因没有能承载这一规模模型的机器，只能通过 OpenRouter 跑“鹈鹕”绘图测试。

**标签**: `#开源大模型`, `#Meta`, `#MoE 架构`, `#长上下文`, `#AI 智能体`

---

<a id="item-2"></a>
## [Gemini 4 Argon 在 ARC-AGI-3（Verified）评测中取得 97.5%](https://x.com/arcprize/status/2110768288523251762) ⭐️ 8.4/10

ARC Prize 公布了 Google DeepMind 旗下 Gemini 4 Argon 的 Verified 评测成绩：在 ARC-AGI-3 上使用 provider adapter harness 取得 97.5%，成本为 4.8 千美元；ARC-AGI-2 得分 91.3%，每任务成本 0.32 美元；ARC-AGI-1 得分 98.5%，每任务成本 0.16 美元。Google DeepMind 由此成为第二家在 ARC-AGI-3 上得分超过 95% 的前沿 AI 实验室。 ARC-AGI 被广泛视为衡量通用推理能力的领先基准，因此前沿实验室在最新的交互式版本上突破 95% 是 AI 能力进展的重要信号，对所有关注 AGI 时间表的人都意义重大。与此同时，不同评测框架之间巨大的分数差距说明，公开成绩越来越取决于“如何把智能体接入模型”，而不仅仅是模型本身，这也对整个基准评测生态提出了标准化报告的压力。 同一模型在 ARC Prize 标准 harness 下仅得 49.8%，成本 5.8 千美元——该 harness 为所有模型提供完全相同的最小化、供应商中立接口，由模型自行决定在可见笔记中保留哪些信息；而 provider adapter harness 则会保留模型不透明的推理状态，并支持对长对话进行自动压缩。ARC Prize 还指出，Argon 在 25 个公开游戏中使用的动作数比人类基线少 62%，在其中 3 个游戏上追平或打破了 speedrun 记录，另有 6 个游戏与记录相差不到 10%。

aihot · X：ARC Prize (@arcprize) · 10月15日 16:22 · [中文阅读](https://aihot.news/items/cvpbhz4ao2wr6pxpthix2z15c)

**核验**: 多源印证

**背景**: ARC-AGI 是由 ARC Prize 基金会（由 François Chollet 与 Mike Knoop 共同创立）推出的一系列推理基准，旨在衡量“流体智力”而非记忆性知识。ARC-AGI-1 与 ARC-AGI-2 是静态解谜任务，而 ARC-AGI-3 是交互式基准：智能体必须探索陌生环境、实时推断目标并构建可适应的世界模型；在其发布之初，所有前沿模型得分均低于 1%，而人类可达 100%。所谓“Verified”是指结果按照 ARC Prize 公布的测试政策被复现，而非仅由实验室自行报告。Gemini 4 Argon 是 Google 的旗舰推理模型，面向复杂软件工程、深度数学与科学问题求解以及自主多步智能体任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/blog/astra">OpenAI's GPT-6 Astra on ARC - AGI -3 | ARC Prize</a></li>
<li><a href="https://andrew.ooo/answers/arc-agi-3-standard-harness-vs-provider-adapter-2026/">ARC - AGI -3: Why GPT-6 Astra Scored 62.7% and 99.9% — andrew.ooo</a></li>
<li><a href="https://openrouter.ai/google/gemini-4-argon">Gemini 4 Argon - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 目前可见的反馈简短且总体正面——Google 的 Logan Kilpatrick 只回复了一句“nice!”；ARC Prize 自己的后续回复则强调该成绩仅次于 GPT-6 Astra 的 99.9%，并突出其动作效率（比人类基线少 62% 的动作）。讨论大多集中在对比 provider adapter 与标准 harness 的两组数字，而非质疑成绩本身，反映出社区对评测方法论的关注正在上升。

**标签**: `#ARC-AGI`, `#AI benchmarks`, `#Gemini`, `#reasoning`, `#Google DeepMind`

---

<a id="item-3"></a>
## [Anthropic Opus 5.5 快速模式结束研究预览并登陆 Microsoft Foundry](https://x.com/ClaudeDevs/status/2110825294655562048) ⭐️ 8.3/10

Anthropic 的 ClaudeDevs 账号宣布，Claude 平台上的 Opus 5.5 fast mode 正式结束研究预览并取消等待名单，开发者可以直接使用。该模式仍是同一款 Opus 5.5，但速度最高提升 2.5 倍，定价为每百万 token 输入 8 美元、输出 40 美元；它同时上线 Microsoft Foundry（由 Azure 托管），Google Cloud 支持也即将推出。 取消等待名单把一项限量试验变成了正式可用的产品，任何开发者无需排队审批即可开启该模式。登陆 Microsoft Foundry 对企业客户意义更大：团队可以利用已有的 Azure 合约、账单、治理与合规体系来采购 Claude，而不必再单独建立供应商关系，而 Google Cloud 支持即将到来则表明 Anthropic 正在推进更大范围的多云分发。 fast mode 只是 Opus 5.5 的一种高速配置，而不是另换或更大的模型，因此输出质量不变，代价完全体现在更高的每 token 价格上（每百万 token 输入 8 美元、输出 40 美元，换取约 2.5 倍速度）。Claude Code 中的 fast mode 保持不变，仍需消耗额外的 usage credits，也就是说 Pro 或 Max 订阅用户无法用套餐额度直接使用，必须开启按量付费的额外用量。

twitter · ClaudeDevs · 10月15日 20:09 · [中文阅读](https://aihot.news/items/e2ssy0a7scpnel6ppyl3r9f2t) · 2 个来源

**核验**: 多源印证

**背景**: fast mode 是 Opus 系列的一种高速推理配置，Anthropic 称其保持相同的模型质量、速度提升约 2.5 倍，但每 token 成本更高；它最早以 research preview（研究预览）的形式在 API 和 Claude Code 中限量开放，并设有等待名单。所谓研究预览，是指在正式发布前先面向部分用户开放的早期阶段，因此结束该阶段并取消等待名单通常意味着功能已被验证为可用于生产环境。Microsoft Foundry 是微软在 Azure 上统一的企业级 AI 平台，用于构建、基于企业数据增强、部署和治理 AI 应用与 Agent，因此 Claude 登陆该平台是一条重要的分发渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans">Manage usage credits for paid Claude plans | Claude Help Center</a></li>
<li><a href="https://azure.microsoft.com/en-us/products/ai-foundry/">Microsoft Foundry | Microsoft Azure</a></li>

</ul>
</details>

**社区讨论**: 回复总体态度积极，但反复出现两点诉求：用户希望 Claude Code 中的 fast mode 不消耗额外 usage credits，也有不少人表示希望该模式能包含在订阅套餐中，而不是按量付费。还有评论者直接表示希望 Anthropic 能提供更多可用算力。

**标签**: `#Claude`, `#Anthropic`, `#AI developer tools`, `#LLM pricing`, `#Microsoft Foundry`

---

<a id="item-4"></a>
## [Google Antigravity 向付费 AI Pro 用户开放 Gemini 4 Argon](https://x.com/antigravity/status/2110866531932316011) ⭐️ 8.3/10

2026 年 10 月 15 日，Google Antigravity 宣布在容量按计划扩容后，开始向正式付费的 Google AI Pro 订阅用户推送 Gemini 4 Argon。Pro 用户会获得一份单独的、只按周计算的 Argon 额度，它叠加在原有的 Gemini 3.8 Flash 额度之上，使用 Argon 不会消耗 Flash 的额度。 Argon 是 Google 面向复杂软件工程场景的旗舰推理模型，为 Antigravity 用户单独划一份额度，意味着长时间运行的智能体编程任务不必再和更便宜的 Flash 额度互相挤占。这也进一步加剧了「智能体优先」开发工具市场的竞争，Antigravity 正与各家终端型编程智能体和 AI IDE 正面交锋。 此次开放仅限正式付费的 Google AI Pro 订阅用户，试用期的 Pro、免费用户以及 Google AI Plus 用户都不在范围内；可用入口包括 Antigravity 桌面 App、命令行工具 CLI，以及装在 VS Code、JetBrains 等编辑器里的 IDE 扩展，但 Antigravity IDE 里暂时还选不到 Argon。推文和官方文档都没有写明每周 Argon 额度具体有多少、哪天重置，官方只说明消耗速度取决于智能体实际干了多少活，任务越复杂额度用掉得越快。

twitter · Google Antigravity · 10月15日 22:52 · 2 个来源

**核验**: 已核对原文

**背景**: Google Antigravity 是 Google DeepMind 推出的「智能体优先」（agent-first）软件开发平台，提供桌面 App、独立 IDE、终端 CLI 和编辑器扩展等多种形态，目标是让 AI 智能体自己规划并执行多步编程任务，而不只是补全代码。Gemini 4 Argon 是 Google 最新的前沿推理模型，主打在编程、金融、法律等领域的复杂真实任务中做「深度工作」；Gemini 3.8 Flash 则是 Flash 档模型，面向长周期软件工程和自主智能体流程，强调速度与成本效率。此前 Antigravity 的额度采用滚动刷新机制（据报道为每 5 小时一次），因此这次单独设立的「按周」额度在计费方式上是一种新模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/dotey/status/2110877554945175677">@dotey: Antigravity 向付费 Google AI Pro 用户开放 Gemini 4 Argon，Argon 有单独的每周额度，不占 3.8 Flash 额度 Google 的 AI...</a></li>

</ul>
</details>

**社区讨论**: 这条公告互动量很高（约 9.3k 点赞、551 条回复），其中最显眼的回复表示这是好消息，但批评 Google 没有在 Antigravity 发布当天就上线 Argon，认为延迟推送损害了其公众形象，并总结为「迟到总比不到好」。整体情绪是认可新模型能力，但同时对分阶段、受额度限制的推送方式带有明显的不满。

**标签**: `#Google Antigravity`, `#Gemini`, `#AI coding agents`, `#LLM release`, `#AI developer tools`

---

<a id="item-5"></a>
## [Google 在 Willow 量子芯片上首次实现"魔态培育"](https://x.com/sundarpichai/status/2110804295352488143) ⭐️ 8.3/10

10 月 15 日，Sundar Pichai 宣布 Google Quantum AI 首次在真实物理硬件上实现了"魔态培育"（magic state cultivation），使用的是其 105 量子比特的 Willow 处理器，相比此前方法将魔态错误率降低约 40 倍，逻辑保真度达到业界领先的 99.99%。该成果当天发表在《科学》（Science）期刊上。 魔态是让量子计算机获得超越经典计算机算力的关键资源，而如何低成本地制造魔态是二十多年来公认的瓶颈。此次是 Google 研究员 2024 年提出的"培育"方案首次在真实硬件上得到验证，是迈向容错、纠错量子计算机的实质性一步，未来有望用于模拟分子、破解加密等难题。 培育之前，大约每 1000 份魔态中就有 4 份是坏的；培育之后，大约每 10000 份里才出现 1 份坏的，但代价是必须大量丢弃——约 100 次尝试中只有 8 次能通过逐级检查留存下来。这一保真度仍远不能满足实际应用：模拟分子或辅助新药设计需要错误率低到百万分之一甚至一亿分之一，破解 RSA 加密则需低到约 100 亿份里最多坏 1 份，Google 自己也表示该方法还需在更大规模上验证。

twitter · Sundar Pichai · 10月15日 18:45 · 2 个来源

**核验**: 多源印证

**背景**: 量子计算机最基本的计算单元量子比特极其娇气，一点热量或干扰就会出错，因此容错依赖"纠错"：用纠错码给逻辑量子比特穿上一层防护服。但穿着防护服后，能直接执行的操作只剩 Clifford 操作，而仅靠这些操作，量子计算机能算的东西经典计算机也能模拟，因此必须具备非 Clifford 操作才能实现通用量子计算。这类操作要靠消耗一种事先制备的特殊状态——"魔态"——来实现，它相当于一把一次性钥匙，每做一次该操作就要用掉一份；过去制造魔态的方法是约二十年前提出的"魔态蒸馏"，需要反复提纯大量粗糙副本，资源开销极大。Google 研究员 2024 年提出的"培育"则是在芯片上划出一小块区域，就地一步步生长并检查魔态，任何一步不过关就立刻丢弃重来，而这次是该方案首次在真实芯片上跑通。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/">Bringing the magic : Google breaks open a bottleneck in quantum...</a></li>
<li><a href="https://arxiv.org/pdf/2610.06828">The practical cost of magic state cultivation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Willow_processor">Willow processor - Wikipedia</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#error correction`, `#Google Quantum AI`, `#research breakthrough`, `#science publication`

---

<a id="item-6"></a>
## [Goodfire 提出神经网络是「干净的」，多义性源自人类概念偏见](https://already-clean.goodfire.com/) ⭐️ 8.0/10

由 Nick Cammarata（前 OpenAI 机制可解释性团队成员）联合创立的可解释性初创公司 Goodfire 发布了一篇题为《Neural networks are clean》的博客文章，主张所谓「多义性」（即单个神经元似乎对多个不相关概念都有响应）很大程度上是人类对「概念」定义方式造成的假象，而非网络真的把不相关的特征塞进同一单元。该文章配合 X 上的一条发布推文，并在 Hacker News 上引发了 555 分、211 条评论的讨论。 如果多义性主要是标注定义的问题而非网络本身的属性，那么让机制可解释性一直显得难以攻克的核心障碍——无法把单一特征对应到单一神经元——就会变得容易处理得多，这将直接影响对大型模型进行审计与对齐的工作。不过这一主张目前仍有争议、尚未被证实，因此它当下的主要价值在于重构讨论框架，而非给出定论。 该论证的方法是重新审视那些著名的「混乱」神经元、盘点多义性在网络不同位置的表现形式，并检查可解释性工具失效的案例，由此提出：同一个神经元既可以被描述为「猫和车」单元，也可以在另一种视角下被描述为一个更简单的「V 形」单元。Cammarata 把目标表述为让「给 AI 基因组测序」变得更容易，但文章并未给出经过同行评审的证明或可复现的基准测试，批评者则指出这一主张与参数过载现象并不互斥。

hackernews · themgt · 10月15日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=50105647)

**核验**: 多源印证

**背景**: 机制可解释性是可解释 AI 的一个子领域，目标是把神经网络内部的具體结构、算法和电路逆向工程出来，而不是把它当成黑箱。该领域长期存在的一个难题就是多义性：单个神经元往往似乎同时表示多种不相关的特征，这使得为某个神经单元指定一个具体特征变得困难，也让以神经元或方向为单位解读网络变得复杂。Goodfire 的这篇文章主张，这个难题有一部分是人类自身带有偏见的概念定义所造成的，而不是网络固有的属性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2210.01892">[2210.01892] Polysemanticity and Capacity in Neural Networks</a></li>
<li><a href="https://www.lesswrong.com/posts/eDicGjD9yte6FLSie/interpreting-neural-networks-through-the-polytope-lens">Interpreting Neural Networks through the Polytope Lens — LessWrong</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体持怀疑态度：bluejay2387 认为文中主张超出了实际已被证明的范围，指出特征复杂度递增以及早期训练结构对后续训练的影响（如 Lottery Ticket Hypothesis、CNN 时代的研究）早已为人所知，而且这些现象与参数过载并不互斥，并引用多模态鸿沟相关研究说明网络倾向于压缩表征。sigbottle 直接质疑其论述框架，追问把某单元称为「V 形神经元」而不是「猫和车神经元」究竟是真的更简单，还是只是对同一现象换了个说法；antics 则把该文读作一份证据简报，意在论证「给 AI 基因组测序」可能比想象中更容易。

**标签**: `#mechanistic-interpretability`, `#neural-networks`, `#AI-alignment`, `#polysemanticity`, `#representations`

---

<a id="item-7"></a>
## [GNOME 博客文章引发关于用 AI 代理逆向工程硬件的讨论](https://blogs.gnome.org/uraeus/2026/10/15/aiandreverseengineerhardware/) ⭐️ 8.0/10

uraeus（Christian Schaller）在 blogs.gnome.org 上发表文章，主张如今可以用 AI 代理来逆向工程硬件；随之而来的 Hacker News 讨论帖（139 分、121 条评论）则充满了亲身实践的例子。评论者描述了导出设备状态、生成替代驱动，甚至在一小时内为一部无文档的路由器搭建出完整的 OpenWRT 编译与刷机流水线。 如果编码代理能够可靠地读取固件镜像、摸清无文档硬件的结构并生成可用驱动，那么对硬件爱好者、安全研究者和小型硬件厂商来说，折腾硬件和维持老旧设备支持的门槛会大幅降低。这也说明 AI 开发者工具正在从应用层代码扩展到二进制、固件和驱动层面的工作。 最具体的案例来自 cookiengineer：他给一部 CPU/SoC 完全无法查证的冷门阿尔卡特调制解调器/路由器焊上 UART 引脚，然后让 DeepSeek v4.1 flash 逆向固件镜像，并在约一小时内搭好了基于 podman 隔离容器的 OpenWRT 编译与刷机流水线。其他人则提到用 Opus 反编译二进制文件并为某款中国 MCU 编写蓝牙控制器固件，以及生成新驱动让老打印机在 macOS 27 上继续工作——不过评论者也指出，像手机这类安全加固严密的设备仍然难得多。

hackernews · ErenayDev · 10月15日 14:35 · [社区讨论](https://news.ycombinator.com/item?id=50104299)

**核验**: 多源印证

**背景**: 硬件逆向工程通常意味着从设备中提取固件镜像、解开其文件系统、反汇编代码，并探测 UART、USB 等接口以弄清设备的启动与通信方式。传统工具包括 FACT、Firmware Analysis Toolkit 这类自动化固件分析框架，它们把提取、静态分析和基于 QEMU 的仿真组合在一起。较新的 REA、Zenyard 等项目则明确面向这一流程，用 AI 代理帮助编码助手理解二进制与设备行为。评论中提到的 OpenWRT 是路由器上广泛使用的开源 Linux 发行版。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/fkie-cad/FACT_core">The Firmware Analysis and Comparison Tool (FACT) - GitHub</a></li>
<li><a href="https://github.com/morluto/rea">GitHub - morluto/rea: Reverse engineer anything with agents ...</a></li>
<li><a href="https://www.zenyard.ai/">Zenyard | AI Agent for Reverse Engineering</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏向兴奋和实操，而非空谈：revolvingthrow 声称自己几乎把拥有的所有带 USB 的设备都逆向了一遍，mrheosuper 则称当前模型在反编译与重新编写固件方面“非常擅长”。唯一的担忧来自 valdiorn——他经营一家小型吉他效果器公司，坦言这几天几乎陷入恐慌，担心 AI 会冲击自己的混响、延迟等算法生意；而 xnx 则呼吁大家把同样的技术用来清除智能电视里的广告和僵尸网络功能。

**标签**: `#AI agents`, `#reverse engineering`, `#hardware hacking`, `#firmware`, `#developer tools`

---

<a id="item-8"></a>
## [阶跃星辰发布 Step 5 Preview：600B MoE 开源权重模型，面向长时程智能体](https://x.com/StepFun_ai/status/2110732706518835353) ⭐️ 7.95/10

阶跃星辰（StepFun）宣布推出 Step 5 Preview，称其为迄今规模最大的开源权重发布——一个 600B 参数的 MoE（混合专家）模型，专为最长 24 小时的智能体任务设计。BF16 和 FP8 权重已上线 Hugging Face 与 ModelScope 并附技术博客，同时还发布了面向 NVIDIA 硬件的 NVFP4 量化 checkpoint（stepfun-ai/Step-5-Preview-NVFP4）。 这把前沿规模的开源权重模型进一步推向智能体（Agent）领域，让开发者可以自行部署长时运行的自主工作流，而不必只依赖闭源 API。对 SGLang、vLLM、NeMo Automodel 与 NVIDIA NIM 的广泛支持降低了部署门槛，也强化了围绕 Blackwell 级硬件的开源模型工具生态。 作为 600B 的 MoE 模型，每个 token 只激活部分专家，因此推理成本远低于同等总参数量的稠密模型；约 8K tokens/sec/GPU 的性能数字来自在 NVIDIA GB300 上使用 NVFP4 量化。值得注意的是，NVIDIA 转发内容称 Step 5 是阶跃星辰最大的开源权重发布，并强调 NVFP4 与 NIM 一键部署，但这些性能数据由厂商提供，尚未经过独立验证。

aihot · X：阶跃星辰 StepFun (@StepFun_ai) · 10月15日 14:01 · [中文阅读](https://aihot.news/items/l3g1uzem751ki1oxckrxa1b3e) · 2 个来源

**核验**: 多源印证

**背景**: MoE（混合专家）是一种模型架构：模型内部包含多个专门化的子网络（专家），但每个 token 只被路由到其中少数几个专家，从而在可控算力成本下实现极大的总参数量。NVFP4 是 NVIDIA 为 Blackwell 代 GPU 推出的 4 位浮点格式，以少量精度损失换取显著更高的吞吐和更低显存占用。GB300 是 NVIDIA 的 Blackwell Ultra GPU，配备 288GB HBM3e 显存，通常以 GB300 NVL72 机架级系统部署。“长时程智能体任务”指 AI 智能体在数小时范围内持续进行多步工具调用与推理循环，这对大上下文和持续且廉价的推理能力提出了要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/NVIDIA_GB300">NVIDIA GB300</a></li>
<li><a href="https://docs.sglang.io/">Welcome to SGLang - SGLang Documentation</a></li>
<li><a href="https://unsloth.ai/docs/models/qwen3.8">Qwen3.8 - How to Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoE`, `#Open-Weight Models`, `#AI Agents`, `#Inference Optimization`

---

<a id="item-9"></a>
## [Anthropic 的 Claude Code 团队将代码审查转向机器优先阅读](https://claude.dev/blog/solving-code-review-at-anthropic/) ⭐️ 7.92/10

Anthropic 发布了一篇第一方工程博客，介绍 Claude Code 团队如何重构代码审查流程：让机器承担大部分代码阅读工作，把人类的注意力集中留高风险决策上。从 6 月到 9 月，合并的 PR 数量翻了一倍以上，需要回退的变更比例下降了 40% 以上，Anthropic 单体仓库（monorepo）的每日变更量也从 5 月的约 2,500 次增长到 9 月的超过 30,000 次。 这是一份有具体数据支撑的案例研究，展示了一个变更量极大的组织如何围绕 AI 智能体重写自己的审查文化，对所有正在采用智能体编程工具的团队都有参考价值。它把代码审查的经典问题从“是否有人类读过这段代码”重新定义为风险分配问题，并提出审查应当像拼写检查一样持续进行，而不是作为开发流程末端的关卡。 该团队明确的目标是：Claude Code 各个仓库（CLI、桌面端、Web 端和移动端应用）的大多数 PR 只需至多一位人类参与（可以是作者本人）即可合并，且不导致回退率或事故率上升。他们通过每个 PR 的人类批准数（中位数和第 95 百分位）、人类评论数量以及 PR 等待人工处理的时间来衡量人力投入，并以回退率和事故率作为护栏——如果这两项上升，就意味着并没有真正节省人力。文章还提到 Claude 编写了 Claude Code 自身约 90% 的代码，同时这篇内容属于博客式总结，而非深入的技术剖析。

aihot · Anthropic：Claude.dev 开发者博客（RSS） · 10月15日 12:00 · [中文阅读](https://aihot.news/items/x02vc0ewajam37hjrbpwsfnre)

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 推出的智能体编程工具，可运行在终端、IDE、桌面端和 Web 端，能够理解代码库、编辑文件并执行命令。由于智能体工具生成变更的速度远超人类逐行阅读的速度，团队面临传统“末端把关式”代码审查从未设计应对的审查瓶颈。Anthropic 的单体仓库（monorepo）是集中存放公司大量代码的大型仓库，其每日变更量正是智能体所写代码快速累积的一个直观指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://code.claude.com/docs/en/how-claude-code-works">How Claude Code works - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI code review`, `#AI developer tools`, `#engineering workflow`, `#Anthropic`

---

<a id="item-10"></a>
## [NVIDIA 开源 Nemotron 3.5 Super VL 及端侧 Bolt 模型](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/) ⭐️ 7.75/10

NVIDIA 发布了开源 1200 亿参数的 Nemotron 3.5 Super VL 多模态混合专家模型，其中激活参数为 120 亿，并推出两款端侧 Bolt 模型：74B-A9B（24GB）与 Bolt E4B（4GB，10 月 23 日上线）。该发布同时开放了权重、数据集和训练配方，NVIDIA 称其任务完成速度在同类中最快，比次优方案快至多 5 倍。 一个完全开放的 1200 亿参数多模态模型，连同透明的权重、数据集和训练配方，为开发者和研究者提供了闭源前沿模型之外的有力选择；而 Bolt 系列则把大模型能力带到本地 RTX 与 DGX Spark 硬件上。这可能加速端侧智能体、自动化流程以及对数据隐私和延迟敏感的企业部署。 Nemotron 3.5 Super VL 采用混合专家（MoE）架构，总参数 1200 亿、激活参数 120 亿，可接收文本、图像、文档、GUI 截图和视频输入并输出文本。端侧 Bolt 模型采用原生 2-bit 量化，因此可在 RTX/DGX Spark 上本地运行；已有数十家机构基于该开源基座用自有数据进行后训练。

aihot · NVIDIA Blog（RSS） · 10月15日 15:00 · [中文阅读](https://aihot.news/items/l9jgzg24ei3a7m8xu1xfhy9n7)

**核验**: 多源印证

**背景**: Nemotron 是 NVIDIA 面向智能体与多模态工作负载推出的开源模型系列。混合专家模型每个 token 只激活部分参数，从而提升效率；量化则通过降低数值精度来减少内存占用并加速推理。DGX Spark 是 NVIDIA 基于 Blackwell 的紧凑型个人 AI 超级计算机，面向希望在本地运行和验证模型的开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/">Open From Data Center to Desktop: NVIDIA Expands Nemotron ...</a></li>
<li><a href="https://openrouter.ai/nvidia/nemotron-3.5-super-vl">Nemotron 3 . 5 Super VL - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#NVIDIA Nemotron`, `#multimodal LLM`, `#edge AI`, `#quantization`

---

<a id="item-11"></a>
## [Meta 以 AI 智能体作为开发参与者打造 Forum 应用](https://engineering.fb.com/2026/10/15/ml-applications/how-meta-built-forum-ai-native-engineering/) ⭐️ 7.65/10

Meta 工程团队详细披露了如何以 AI 智能体作为开发流程的参与者、在 human-on-the-loop 模式下构建独立 Groups 应用 Forum，并以通过验证的生产级产出而非代码量来衡量成功。Forum 在八周内实现与 Facebook Groups 的核心功能对齐，自主压测循环在开发阶段发现并修复了内存问题（内存占用与缺页次数大致减半），上线后智能体还协助对用户反馈进行根因分析。 这是一个来自大规模生产环境的 AI 原生软件开发生命周期的具体案例：智能体被结构性嵌入代码生成、测试与调试环节，而不是偶尔当作代码补全工具使用，这一区别对正在考虑如何重组团队与工具链的工程管理者很重要。八周达到功能对齐、并带来可量化的内存占用与缺页下降，为业界提供了一个少见的量化基准，说明智能体参与式工作流究竟能带来什么实际收益。 human-on-the-loop 模式意味着工程师负责监督、验证和批准智能体的工作，而不是把任务完全外包出去，评判标准是通过验证的生产级产物而非智能体的活跃程度。自主压测循环值得关注，因为它在上线前就捕获了内存问题，不过公开内容并未说明具体使用了哪些模型或智能体框架，因此这些成效与这一单一应用的具体情境绑定。

aihot · Meta Engineering Blog（RSS） · 10月15日 19:00 · [中文阅读](https://aihot.news/items/moaux5xk1dqk4pi3tsx8sabsj)

**核验**: 多源印证

**背景**: AI 原生工程指的是在假设智能体会与人类一起生成、评审、测试和部署代码的前提下，重新设计整个软件开发生命周期；它与“AI 辅助”编码的差别是结构性的，而非表面的。human-on-the-loop 是 human-in-the-loop 的一种变体：人类不必逐项批准 AI 生成的每次改动，而是监督一个自主循环并在需要时介入。Forum 是 Meta 围绕 Groups 式社区功能构建的独立应用。自主压测会把异常或对抗性输入灌入系统，以暴露普通测试难以发现的内存泄漏等故障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.howdy.com/blog/ai-native-engineering-definition-roles-workflow-operating-model">AI-Native Engineering: Definition, Roles, Workflow, and ...</a></li>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2026/08/18/human-in-the-loop-is-no-longer-enough-ai-in-the-loop-is-the-future/">Human-In-The-Loop Is No Longer Enough: AI-In-The ... - Forbes</a></li>
<li><a href="https://testquality.com/agentic-qa-architecture-autonomous-testing-2026/">Agentic QA Architecture: Reasoning Loops, Self-Healing DOM ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#AI-native engineering`, `#developer tools`, `#automated testing`, `#Meta engineering`

---

<a id="item-12"></a>
## [DeepSeek V4.1 Flash 在 OpenCode 中免费开放](https://x.com/opencode/status/2110635747648909472) ⭐️ 7.0/10

OpenCode 在其 X 账号上宣布，DeepSeek V4.1 Flash 现已可在 OpenCode 这款开源 AI 编程智能体中免费使用。该公告获得 2.28 万次点赞和 774 条回复，显示出开发者社区的高度关注。 这降低了智能编程的成本门槛，开发者可以在终端或 IDE 中免费使用一个能力较强的模型，可能加速 AI 编程智能体的普及，并促使竞品提供类似的免费方案。 根据其模型卡，DeepSeek V4.1 Flash 是一个多模态混合专家模型，拥有 552B 骨干参数，并支持最多一百万 token 的上下文。不过，OpenCode 的公告帖并未说明速率限制、上下文上限或免费期限。

twitter · OpenCode · 10月15日 07:35

**核验**: 多源印证

**背景**: OpenCode 是一款开源 AI 编程智能体，帮助开发者在终端、IDE 或桌面环境中编写代码，并支持连接多种模型。DeepSeek V4.1 Flash 是 DeepSeek 新架构家族中最小的一款模型，旨在实现更快的推理和更高的吞吐量，同时保留原生视觉理解能力。AI 编程智能体与简单的助手不同，能够自主规划多步任务、执行代码并根据结果迭代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek-ai/DeepSeek-V4.1-Flash · Hugging Face</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>

</ul>
</details>

**标签**: `#AI developer tools`, `#OpenCode`, `#DeepSeek`, `#coding agents`, `#free AI models`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="14"><span>其他追踪推文</span><span class="archive-tab-count">14</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="3"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">3</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110919336147796377">@dotey: 特斯拉新 Roadster 发布：靠压缩空气喷气在空中翻正落地，马斯克说 2028 年投产，售价未公布 10 月 15 日晚，特斯拉在得州 SpaceX 的 McGregor 试验场直播...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 02:22 UTC · 喜欢 145 · 转发 16 · 回复 40 · 浏览 47843</p>
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
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月16日 01:57 UTC · 喜欢 219 · 转发 11 · 回复 84 · 浏览 58194</p>
<p class="archive-item-content">卧槽，特斯拉这个新的跑车太离谱了<br>
<br>
居然能短暂飞行并且在空中调整姿态<br>
<br>
演示的时候可以直接跳起来反转然后正常落地 https://t.co/AEP6AVWLKN</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/cb_doge/status/2110901560435945972">@cb_doge: HOLY SHIT https://t.co/4Q6rs8nfvM</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 01:12 UTC · 喜欢 12981 · 转发 1473 · 回复 396 · 浏览 3855335</p>
<p class="archive-item-content">HOLY SHIT https://t.co/4Q6rs8nfvM</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110877554945175677">@dotey: Antigravity 向付费 Google AI Pro 用户开放 Gemini 4 Argon，Argon 有单独的每周额度，不占 3.8 Flash 额度 Google 的 AI...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 23:36 UTC · 喜欢 89 · 转发 3 · 回复 91 · 浏览 34454</p>
<p class="archive-item-content">Antigravity 向付费 Google AI Pro 用户开放 Gemini 4 Argon，Argon 有单独的每周额度，不占 3.8 Flash 额度<br>
<br>
Google 的 AI 编程工具 Antigravity 今天开始向付费的 Google AI Pro 订阅用户推出 Gemini 4 Argon。官方模型页写明只限正式付费的 Pro，试用期的 Pro 用不了，免费用户和 Google AI Plus 用户也不在范围内。能用的地方是 Antigravity 桌面 App、命令行工具 CLI 和 IDE 扩展（装在 VS Code、JetBrains 等编辑器里的插件），Antigravity IDE 里暂时选不到。目前在逐步推送，官方建议先更新到最新版。<br>
<br>
Pro 用户用 Argon 有一份单独的额度，只按周计算，不像原有额度那样每 5 小时刷新一次；它和原来给 Gemini 3.8 Flash 用的额度分开，用 Argon 不会吃掉 3.8 Flash 的额度。每周到底给多少、哪天重置，推文和官方文档都没写。文档对所有额度的说明是，消耗多少取决于智能体实际干了多少活，任务越复杂用得越快。<br>
<br>
官方模型说明：https://t.co/7IXduTeBzr</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110875762261996016">@dotey: 😓 美国人去中国出差用 Claude 也是会被封的</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 23:29 UTC · 喜欢 122 · 转发 7 · 回复 65 · 浏览 31059</p>
<p class="archive-item-content">😓 美国人去中国出差用 Claude 也是会被封的</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110846329341837698">@dotey: Opus 5.5 快速模式取消排队：订阅用户要额外付费，API 价格是标准版两倍 Anthropic 宣布，Claude Opus 5.5 的快速模式结束内测，取消候补名单。还是同一个模...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 21:32 UTC · 喜欢 41 · 转发 3 · 回复 54 · 浏览 25165</p>
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
<h3><a href="https://x.com/dotey/status/2110839911339184608">@dotey: Google 量子计算新进展：一种关键“零件”的次品率降到原来的 1/40 Google 今天在《科学》期刊发表论文，在自家量子芯片 Willow 上验证了一种制造“魔态”的新办法，做出...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 21:07 UTC · 喜欢 16 · 转发 4 · 回复 14 · 浏览 7137</p>
<p class="archive-item-content">Google 量子计算新进展：一种关键“零件”的次品率降到原来的 1/40<br>
<br>
Google 今天在《科学》期刊发表论文，在自家量子芯片 Willow 上验证了一种制造“魔态”的新办法，做出来的魔态，坏的比例降到原来的 1/40 左右。魔态是什么、为什么重要，得先从量子计算机的一个大毛病说起。<br>
<br>
量子计算机是一种新型计算机，理论上，在模拟药物分子、破解密码这类题目上，能比普通电脑快得多。它最小的计算单元叫量子比特，相当于普通电脑里存 0 和 1 的那个单元，但极其娇气，一点热量、一点干扰就会出错。所以到今天，还没有一台量子计算机能真正干正事。<br>
<br>
为了不出错，科学家给量子比特设计了一套保护办法，叫“纠错”，可以理解为给数据穿上一层防护服。穿着防护服，大部分操作照样能做。麻烦的是，有一种关键操作，穿着防护服没法直接做。偏偏只靠剩下那些操作，量子计算机能算的东西，普通电脑也都能算，等于白造了。<br>
<br>
魔态就是为这个关键操作准备的。科学家想了个绕道的办法：事先单独把一些量子比特调成一种特殊的状态，这种状态就叫“魔态”。计算中每需要做一次那个关键操作，就把一份魔态“喂”进去，效果就等于做了这个操作。喂进去就用掉了，下次还得再备一份。<br>
<br>
所以可以把魔态想成一把一次性钥匙：量子计算机每开一次那扇关键的门，就要用掉一把。之所以叫“魔态”，是因为量子计算机比普通电脑强的那份“魔力”，就靠它来实现。<br>
<br>
问题出在造钥匙上。魔态本身也是量子比特，一样娇气，很容易造坏，一把坏钥匙用进去，整道题就算错了。以前的办法是先造一大堆粗糙的魔态，再一遍遍提纯，非常费资源。有估算说，一台量子计算机最多可能要拿出 95% 的能力专门造魔态，真正用来算题的只剩一小部分。科学家 20 多年前就预见到这个瓶颈，一直在想办法压低成本。<br>
<br>
2024 年，Google 的研究员提出了一个新办法，叫“培育”：在芯片上划出一小块地方，放进一份粗糙的魔态，然后一步步检查，只要哪一步发现问题，马上扔掉重来，能一路通过所有检查的，就是合格的魔态。有点像流水线上每道工序都站着质检员，次品当场就扔。<br>
<br>
这次是第一次在真实芯片上把这个办法做成。不用培育时，大约每 1000 份魔态里有 4 份是坏的；用了培育之后，大约 1 万份里才有 1 份坏的。代价是扔掉的很多，100 次尝试里只有 8 次能留下来。<br>
<br>
离真正能用还有多远？按《科学美国人》的报道，要用量子计算机模拟分子、帮忙设计新药，魔态坏的比例得低到百万分之一甚至一亿分之一；要破解现在网上广泛使用的 RSA 加密，得低到 100 亿份里最多坏 1 份。现在做到的是 1 万份坏 1 份。Google 自己也说，这个办法还要在更大的规模上验证，还有很多难题没解决。<br>
<br>
原文：https://t.co/fuydV8pM9L<br>
论文：https://t.co/S34VQwG4jD<br>
预印本：https://t.co/iQHz3DFlsK<br>
《科学美国人》报道：https://t.co/NYHGFjTmaC</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/blackanger/status/2110793282242723853">@blackanger: 我一个香港的朋友，美国人，昨天跑来深圳参加 Rust 大会，睡了一觉起来，发现 Claude 账号被封了 😆😂</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 18:01 UTC · 喜欢 155 · 转发 4 · 回复 22 · 浏览 48584</p>
<p class="archive-item-content">我一个香港的朋友，美国人，昨天跑来深圳参加 Rust 大会，睡了一觉起来，发现 Claude 账号被封了 😆😂</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110786960080155103">@op7418: Meta 又开始发布开源模型了，发布了 Muse Spark Open。 他们说是迄今为止美国最强大的开源模型。 基于苹果的 MLX 框架做了深度优化。 这个 800B 的模型，居然可以...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 17:36 UTC · 喜欢 41 · 转发 0 · 回复 24 · 浏览 12157</p>
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
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 09:45 UTC · 喜欢 47 · 转发 0 · 回复 32 · 浏览 15376</p>
<p class="archive-item-content">DeepSeek 居然给他们服务挂机影响的用户补偿了，破天荒啊<br>
<br>
补偿是过去 7 天账户消耗的所有 API 的金额，会以赠金的形式退到账户里</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/tianyi/status/2110663080246132855">@tianyi: Between 8:11 and 13:04 (Beijing Time) on October 15, 2026, DeepSeek API service system experi...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 09:24 UTC · 喜欢 1466 · 转发 73 · 回复 190 · 浏览 206263</p>
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
<p class="source-line">Twitter/X · @op7418 · 10月15日 08:57 UTC · 喜欢 34 · 转发 0 · 回复 14 · 浏览 14949</p>
<p class="archive-item-content">OpenCode 现在直接把 DeepSeek V4.1 Flash 免费了！<br>
<br>
不过免费版只有 200K 的上下文，付费版有 1M</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110605686086529470">@op7418: 顺便说一句，JEV 模型这次的更新几乎都命中了我们在 Next Token 20 多天前提到的它需要改进的部分 https://t.co/iE01tWYP5J</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 05:36 UTC · 喜欢 46 · 转发 2 · 回复 8 · 浏览 11224</p>
<p class="archive-item-content">顺便说一句，JEV 模型这次的更新几乎都命中了我们在 Next Token  20 多天前提到的它需要改进的部分 https://t.co/iE01tWYP5J</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110584734342627390">@op7418: 字节 Seed 成立了专门的模型安全与对齐部门，感觉确实很有必要。 这次他们计划在这个部门全球招募 10 位顶尖研究员。 研究课题有： 大模型及 Agent 安全的前沿评测方法和 Benchma...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月15日 04:13 UTC · 喜欢 17 · 转发 1 · 回复 17 · 浏览 7135</p>
<p class="archive-item-content">字节 Seed 成立了专门的模型安全与对齐部门，感觉确实很有必要。<br>
<br>
这次他们计划在这个部门全球招募 10 位顶尖研究员。<br>
<br>
研究课题有：<br>
大模型及 Agent 安全的前沿评测方法和 Benchmark 建设<br>
模型前沿能力对齐的训练方法<br>
自动化 Red Teaming<br>
模型行为可解释性<br>
模型能力和行为监控<br>
<br>
字节的待遇向来非常顶，事情本身也极具挑战性，最近刚好在看类似方向工作的朋友不妨试试。<br>
<br>
最近不管是大模型还是小模型，都频繁出现模型越狱和突破沙箱隔离环境的问题。<br>
<br>
而且这种风险要么是小打小闹，要么就是憋个大的。提前有这样的储备并持续进行研究，起码在出问题时能快速反应。<br>
<br>
随着模型能力越来越高、自主性越来越强，在一些危险领域的隐患也越来越大：<br>
比如 CBRN 领域（化学、生物、放射性及核领域）<br>
可能很多人觉得上面的四个离我们太远，但是互联网上针对个人的内容攻击离我们可太近了。<br>
AI 甚至有可能直接篡改应用，甚至控制家里的其他设备。<br>
<br>
随着 AI 能破解一切软件，那 AI 写出非常厉害的病毒也是一个顺理成章的事情。<br>
<br>
包括对于我们整个互联网赖以生存的密码学破解，应该也是进展神速。<br>
<br>
客观来说，国内在这方面的进展其实比 OpenAI 和 Anthropic 慢。<br>
<br>
Anthropic 成立初衷就是为了安全，长期在做对齐和可解释性研究；而海外 AI 圈几乎每隔一两周就会爆出安全热点，比如前几天 OpenAI 的安全研究员辞职、之前 Hugging Face 被入侵等。<br>
<br>
模型安全是一个非常前沿的跨学科领域，需要大量的探索，对研究者的综合要求比较高。<br>
<br>
这也是为什么他们要去全球或者公开招聘这种顶尖人才的原因，感兴趣的可以关注一下</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2110618732666257557">Thibault Sottiaux: Done and dusted https://t.co/0fehr43VS4</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：大功告成 https://t.co/0fehr43VS4</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月15日 06:28 UTC · 喜欢 988 · 转发 49 · 回复 289</p>
<p class="archive-item-content">A cryptic one-line tweet from OpenAI Codex contributor Thibault Sottiaux saying &#x27;Done and dusted&#x27; with a link and no further context.</p>
<p class="archive-item-translation"><span>中文摘要</span>OpenAI Codex 贡献者 Thibault Sottiaux 发了一条只有“大功告成”和一个链接、缺乏其他上下文的简短推文。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2110595554036400151">Thibault Sottiaux: Landing within the next 2 hours</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：未来两小时内上线</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月15日 04:56 UTC · 喜欢 2632 · 转发 103 · 回复 425</p>
<p class="archive-item-content">An OpenAI Codex developer teases an imminent launch (&#x27;landing within the next 2 hours&#x27;), drawing heavy engagement but no substantive detail.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位 OpenAI Codex 开发者预告即将上线的新内容（“未来两小时内落地”），引发大量互动但未透露具体细节。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2110595484180214059">Thibault Sottiaux: The reports of my reset button being lost are greatly exaggerated Day 10/ Reset</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：关于我的重置按钮丢失的报道被大大夸大了 第 10 天/重置</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月15日 04:55 UTC · 喜欢 9238 · 转发 493 · 回复 1531</p>
<p class="archive-item-content">A cryptic tweet by Thibault Sottiaux joking that reports of his reset button being lost are greatly exaggerated.</p>
<p class="archive-item-translation"><span>中文摘要</span>Thibault Sottiaux 发布了一条隐晦的推文，开玩笑说关于他的重置按钮丢失的报道被大大夸大了。</p>
</article>
</div>
</section>
