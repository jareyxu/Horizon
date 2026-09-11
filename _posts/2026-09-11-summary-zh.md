---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> 从 59 条内容中筛选出 15 条重要资讯。

---

1. [DeepSeek 发布 V4.1-Flash：1M 上下文、FP4 KV 缓存与跨层注意力复用](#item-1) ⭐️ 9.53/10
2. [OpenAI 的 Navier-Stokes 反例包含 Lean 4 形式证明](#item-2) ⭐️ 9.0/10
3. [微软正式将 Rust 列为一级（Tier-1）语言](#item-3) ⭐️ 9.0/10
4. [WeWorm：首个通过微信通话传播的零点击蠕虫，AI 辅助构建](#item-4) ⭐️ 9.0/10
5. [OpenAI 发布 Agents API 公测版](#item-5) ⭐️ 8.78/10
6. [Shopify 从 React Native 回归原生 Swift 和 Kotlin](#item-6) ⭐️ 8.6/10
7. [Claude Code v2.1.268：新增网关定价、Runner 会话清理与插件 JSON 输出](#item-7) ⭐️ 8.0/10
8. [Cognition 发布 SWE-2 编程模型，对标 Fable 5.1 和 GPT-Astra](#item-8) ⭐️ 8.0/10
9. [Cursor 推出 Projects：协调者智能体调度数千子智能体处理大型任务](#item-9) ⭐️ 7.92/10
10. [OpenAI 在 API 中推出全双工语音模型 GPT-Live-1](#item-10) ⭐️ 7.75/10
11. [Anthropic 评测 AI 模型的战术情报定位与常规武器开发能力](#item-11) ⭐️ 7.17/10
12. [OpenAI Codex Python SDK v0.154.0 新增 Max/Ultra 推理努力值与 ExternalMessage](#item-12) ⭐️ 7.0/10
13. [Vibe Coding 让普通人也能自己搓工具](#item-13) ⭐️ 7.0/10
14. [AI Agent 代码审查的三步提示词框架](#item-14) ⭐️ 7.0/10
15. [OpenClaw 实现快速云端会话，支持远程终端、WebVNC 与 CUA](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DeepSeek 发布 V4.1-Flash：1M 上下文、FP4 KV 缓存与跨层注意力复用](https://www.marktechpost.com/2026/09/10/deepseek-ai-released-deepseek-v4-1-flash-with-1m-context-fp4-kv-cache-and-cross-layer-attention-reuse) ⭐️ 9.53/10

DeepSeek AI 以 MIT 许可开源发布了多模态 MoE 模型 DeepSeek-V4.1-Flash，支持 1M 上下文窗口，全局 KV 缓存仅每 token 890 字节，约为 V4-Flash 的 1/4、V1 的 1/437。 该发布代表了长上下文推理效率的重大突破，大幅降低 KV 缓存内存占用和以输入为主的工作负载（如长时程智能体）的推理成本。它为大型 MoE 模型如何在庞大参数量与现实可部署性之间取得平衡树立了新标杆。 40 层骨干分为 20 层因果编码器和 20 层解码器；解码器不自行计算全局 KV，而是通过每层投影权重从编码器最终隐藏状态推导。模型采用 CSA2 压缩稀疏注意力，每层静态分配 Full、Reindex、Reuse 三种模式之一以跨层复用 KV 和索引，同时每层保留 128 token 的滑动窗口注意力。

aihot · MarkTechPost（RSS） · 9月10日 07:31 · [中文阅读](https://aihot.news/items/cmtv7kmzk02vdrok9y0y8njiv) · 7 个来源

**核验**: 多源印证

**背景**: 混合专家模型（MoE）每个 token 仅激活部分参数，从而在更低推理计算下实现更大模型容量。KV 缓存存储中间注意力键值，并随上下文长度线性增长，成为百万级上下文的主要内存瓶颈。FP4 量化将缓存值压缩为 4 位浮点，在保持精度的同时进一步降低内存占用。这些技术共同解决了长上下文、输入密集型 AI 工作负载的主要成本驱动因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/674698482">混合专家模型 (MoE) 详解 - 知乎 混合专家模型（MoE）详解 - Hugging Face 一文看懂混合专家模型 (MoE) 到底是什么？-CSDN博客 混合专家模型 - 百度百科 万字长文！小白也能懂的混合专家模型（MoE）深度解析-CSDN博客 MoE是什么？一文读懂“混合专家模型 (MoE)”看这篇就够了！</a></li>
<li><a href="https://forceinjection.github.io/09_inference_system/kv_cache/01_concepts/compression/kv_cache_compression.html">大模型 KV Cache 压缩技术详解：原理、架构与趋势</a></li>
<li><a href="https://www.ultralytics.com/zh/glossary/fp4">FP4：四位浮点 AI 量化详解 - ultralytics.com</a></li>

</ul>
</details>

**社区讨论**: 硅基流动宣布 DeepSeek-V4.1-Flash 在其平台 Day 0 上线，DeepSeek 还开源了多个部署代码仓库以简化落地。MIT 许可证和公开的 API 定价档位在开源社区引发了积极反响。

**标签**: `#DeepSeek`, `#AI模型`, `#MoE`, `#KV缓存`, `#长上下文`

---

<a id="item-2"></a>
## [OpenAI 的 Navier-Stokes 反例包含 Lean 4 形式证明](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/) ⭐️ 9.0/10

OpenAI 于 2026 年 9 月 8 日宣布了 Navier-Stokes 方程存在性与光滑性问题的一个无界反例，该发布包含一个经 Lean 4 验证的形式证明。这标志着 AI agent 成功在证明助手中形式化了一个重大数学结果的里程碑。 这展示了 AI 在数学推理和形式化验证方面日益增长的能力，可能加速千禧年大奖难题等开放问题的解决进程。它可能重塑数学家的研究方式，将 AI 生成的证明与机器验证的形式化相结合，从而提高对结果的信心。 该反例是在 Levent Alpöge 和 Tristan Buckmaster 关于三维不可压缩欧拉方程有限时间爆破的研究之后产生的，OpenAI 的解决方案尚未经过外部数学家验证。Lean 4 形式证明提供了可由机器检查的保证，但社区成员指出验证本身需要约 15 小时的运行时间和 230GB 内存。

hackernews · ibobev · 9月10日 21:22 · [社区讨论](https://news.ycombinator.com/item?id=49650326)

**核验**: 多源印证

**背景**: Navier-Stokes 存在性与光滑性问题询问描述粘性流体运动的 Navier-Stokes 方程在三维空间中是否总有光滑解；这是克莱数学研究所为七个千禧年大奖难题之一提供的 100 万美元奖项。Lean 是一种基于归纳构造演算的证明助手和函数式编程语言，用于以机器可检查的严谨性形式化验证数学证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_equations">Navier-Stokes equations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Lean 验证仅比 agent 生成快一个数量级左右（15 小时、230GB 内存对比 11 天），质疑 Lean 为可审计性而保持简单是否限制了优化潜力。另一位评论者计算成本比较约为 $132M 人力成本对比 $40M agent 成本，质疑"四个数量级"的说法，还有人认为"每页四十小时"的经验法则反映的是 2005 年的局限而非当前 Lean 的能力。一位评论者提出了哲学担忧：当 AI 解决人类在生物学上或资源上可能无法独立验证的问题时会发生什么。

**标签**: `#AI`, `#Lean 4`, `#形式化验证`, `#数学证明`, `#OpenAI`

---

<a id="item-3"></a>
## [微软正式将 Rust 列为一级（Tier-1）语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

微软正式将 Rust 提升为一级（Tier-1）语言工程状态，在公司内部正式承认其为一线语言。这一地位为内部团队提供了从本地开发到生产环境的完整支持路径，包括安全的工具链构建、高效的开发者工具、质量流程和深度平台集成。 这是一次里程碑式的背书，验证了 Rust 的成熟度，并巩固了其在系统编程领域作为 C++ 和 C# 真正竞争对手的地位。这与整个行业向内存安全开发方向转变的大趋势一致，事实也证明微软产品中约 70% 的 CVE 都是内存安全问题。 一级状态涵盖安全的工具链构建、高效的开发者工具、质量流程和深度平台集成。社区讨论还提到微软计划在 2030 年前通过自动化工具将多达 10 亿行代码转换为 Rust，同时有传闻称 Rust 的后端已从 LLVM 切换到 MSVC。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**核验**: 待核验

**背景**: Rust 是一种专注于内存安全和性能的系统编程语言，无需垃圾回收即可提供内存安全保障。在微软获得一级语言地位意味着公司官方支持并在内部投资该语言，提供与其他一流语言同等级别的支持。作为 Windows 背后的主要操作系统厂商，微软的这一决定增强了 Rust 在整个行业的可信度，也标志着所有主要操作系统厂商都已在系统编程语言选择上实现了多元化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier - 1 Language at Microsoft</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区对此消息总体持积极态度，许多人称这是对 Rust 成熟度的重要验证。评论者强调了微软到 2030 年转换 10 亿行代码为 Rust 的雄心目标、DARPA 的 C 到 Rust 自动转换工作、从 LLVM 到 MSVC 的后端切换，以及这一举措背后内存安全的战略动机。有人认为 Rust 如今已是 C++ 和 C# 的成熟稳定竞争对手，而不再是一个新兴的、不稳定的语言。

**标签**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#Programming Languages`

---

<a id="item-4"></a>
## [WeWorm：首个通过微信通话传播的零点击蠕虫，AI 辅助构建](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm，这是首个通过微信语音通话在 iOS 和 Android 间传播的零点击蠕虫，无需用户任何交互即可接管目标账号。团队借助 AI 在约两天内发现漏洞并编写了 RCE 利用，随后用一周时间构建出该蠕虫。 这标志着 AI 辅助攻击性安全的重大升级，表明以往需要更大团队数月才能构建的蠕虫如今可在约一周内完成。它凸显了 AI 如何加速漏洞发现与利用开发，为移动平台和超级应用的安全防御带来了迫在眉睫的新挑战。 该漏洞是微信 VoIP 协议栈中的内存损坏问题；受害者无需接听电话，即使接听也听不到任何声音，利用仍会成功。9 月 4 日，腾讯确认该漏洞可被用于远程命令执行，演示中蠕虫会自动传播到受害者的其他联系人。

rss · Simon Willison · 9月10日 00:56

**核验**: 多源印证

**背景**: 零点击蠕虫是一种无需用户交互（如点击链接或打开文件）即可感染设备的自我传播恶意软件。远程代码执行（RCE）允许攻击者在目标系统上运行任意代码，而这类漏洞在微信等广泛使用的超级应用中尤为危险。AI 助手和大语言模型正越来越多地用于安全研究，以加速漏洞分析、利用构建和载荷生成，从而降低了这些任务所需的技能和时间门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://calif.io/research/weworm">The first zero-click worm to spread through WeChat calls across iOS...</a></li>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm - First 0 - Click Worm Spreading Through WeChat Calls...</a></li>
<li><a href="https://www.infosecurity-magazine.com/news/wechat-zeroclick-worm-hijack/">Researchers Build WeChat Zero-Click Worm Hijacking Phones via Calls</a></li>

</ul>
</details>

**标签**: `#ai-security-research`, `#cybersecurity`, `#zero-click-worm`, `#AI-assisted-exploit`, `#WeChat`

---

<a id="item-5"></a>
## [OpenAI 发布 Agents API 公测版](https://openai.com/index/introducing-the-agents-api) ⭐️ 8.78/10

OpenAI 已发布 Agents API 的公测版，这是一个托管式云端服务，开发者可通过一次 API 调用访问 Codex harness 及其基础设施。 这一发布大幅降低了构建生产级 AI 智能体的门槛，使自动化工作流和 AI 产品设计更加容易。这也标志着 OpenAI 将托管式智能体编排作为核心开发者服务的战略方向。 Agents API 由 Codex harness 提供支持，负责会话管理、编排、上下文压缩与恢复，开发者只需提供工具并选择执行环境。它支持长时间运行会话、工具调用以及多智能体并行协作。

aihot · OpenAI：官网动态（RSS · 排除企业/客户案例） · 9月10日 00:00 · [中文阅读](https://aihot.news/items/cmtvywm6902omrojit3fo7bjv)

**核验**: 多源印证

**背景**: Codex harness 是 OpenAI 用 Rust 实现的框架，是 Codex 的基础，专为生产级智能体嵌入而设计。此前，开发者需要自行组装智能体基础设施和编排逻辑；Agents API 将其打包为 OpenAI 管理的服务，类似于托管数据库或计算服务将运维复杂性抽象化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>
<li><a href="https://segmentfault.com/a/1190000048185190">人工智能 - 刚刚！ Codex Harness ... - SegmentFault 思否</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#OpenAI`, `#API`, `#开发者工具`, `#自动化`

---

<a id="item-6"></a>
## [Shopify 从 React Native 回归原生 Swift 和 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.6/10

Shopify 工程团队宣布将其移动应用从 React Native 迁移回 iOS 原生 Swift 和 Android 原生 Kotlin。该公司称，日益增长的复杂性和维护成本是此次转变的主要原因。 这家大型电商平台的决策发出了关于跨平台框架权衡的强烈信号，可能影响其他公司的移动开发策略选择。这也加剧了业内关于跨平台开发与原生开发哪一方长期更可持续的争论。 此次迁移涉及用 Swift 和 Kotlin 重写 Shopify 应用，放弃共享的 React Native 代码库。该工程博客文章引发了 462 条评论，讨论其影响，包括 AI 在代码生成中的作用以及长期维护的考量。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982) · [中文阅读](https://aihot.news/items/cmtvom4k90ghtronbwks6e67t) · 4 个来源

**核验**: 多源印证

**背景**: React Native 是 Meta 开发的开源框架，允许开发人员使用 JavaScript 和 React 构建 iOS 和 Android 移动应用。相比之下，原生开发使用针对特定平台的语言，例如 iOS 的 Swift 和 Android 的 Kotlin，通常能提供更好的性能和平台集成。跨平台开发与原生开发之间的选择一直是软件工程中长期的争论话题，需要在代码共享与用户体验及维护复杂性之间进行权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native - Wikipedia</a></li>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://neptechpal.com.np/blogs/cross-platform-vs-native-app-nepal">Cross - Platform vs Native App Development : Which... | NepTechPal</a></li>
<li><a href="https://www.jafton.com/insights/kotlin-vs-swift">Kotlin vs. Swift: How are they different? | Jafton</a></li>

</ul>
</details>

**社区讨论**: 评论中的工程师对原生开发方法表示认同，其中一位指出长期以来高管对共享代码库的压力。一些人分享了使用 AI 辅助转换的积极经验，而另一些人则警告说，AI 并不能消除管理复杂性的需求。一位评论者观察到二十年来团队采用跨平台框架却最终发现原生开发更有效的循环。

**标签**: `#React Native`, `#Swift`, `#Kotlin`, `#Mobile Development`, `#Engineering Strategy`

---

<a id="item-7"></a>
## [Claude Code v2.1.268：新增网关定价、Runner 会话清理与插件 JSON 输出](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) ⭐️ 8.0/10

Claude Code v2.1.268 为网关新增了定价支持，使已登录客户端通过托管设置获得一致费率，同时增加了 CIDR 安全警告和新的 `gatewayInternalNetworks` 托管设置。本次还新增了用于会话清理的 `claude self-hosted-runner --remove-session-state` 命令，以及插件安装/卸载/更新/启用/禁用命令的 JSON 输出。 这些改动让 Claude Code 更适合生产环境中的自托管部署，为管理员提供了对网关访问、定价和 Runner 资源清理的更精细控制。JSON 输出改进有助于开发者在 CI/CD 流水线和其他工具中编写脚本并自动化插件管理。 本次发布还修复了多个 bug，包括第三方 Anthropic 兼容端点出现 HTTP 400 错误、WebFetch 无限挂起（现限制为 300 秒，可通过 `CLAUDE_CODE_WEBFETCH_DEADLINE_MS` 覆盖），以及空闲会话中忙循环导致的高 CPU 占用。同时修复了符号链接目录上权限规则不生效、以及 git URL 和 MCP 配置中 `${VAR}` 占位符的密钥在错误信息中泄露等安全问题。

github · ashwin-ant · 9月10日 20:30

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 基于命令行的 AI 编码助手，在终端中运行。在企业使用中，它支持 “Claude apps gateway” 部署，组织通过 gateway.yaml 文件自托管网关，以控制身份验证、路由、策略和遥测。自托管 Runner 让团队在自己的基础设施中运行 Claude Code 会话，而非 Anthropic 托管环境；托管设置则允许管理员强制执行覆盖用户级设置的组织级策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/claude-apps-gateway-config">Claude apps gateway configuration - Claude Code Docs</a></li>
<li><a href="https://docs.claude.com/en/docs/claude-code/settings">Claude Code settings - Claude Docs</a></li>
<li><a href="https://www.dusanpetrovic.dev/cc-self-hosted-runners-test-infra/">Run Claude Code Where Your Test Environment Already Lives</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI developer tools`, `#release notes`, `#gateway`, `#self-hosting`

---

<a id="item-8"></a>
## [Cognition 发布 SWE-2 编程模型，对标 Fable 5.1 和 GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 8.0/10

Cognition 发布了基于 Moonshot 2.8 万亿参数 Kimi K3 基座模型后训练的编程模型 SWE-2，现已可在 Devin Desktop 和 CLI 中使用。该模型引入了可配置的推理努力层级，并宣称其基准测试表现对标 Anthropic 的 Claude Fable 5.1 和 OpenAI 的 GPT-Astra。 SWE-2 的发布加剧了 AI 编程代理领域的竞争，闭源实验室正在争夺市场领导地位。其对 GPT-5.6 Sol 宣称的成本性能优势可能给竞争对手带来定价压力，同时也重新引发了关于闭源与 DeepSeek 等开源模型的争论。 SWE-2 采用 NVFP4/FP8 内核和量化感知训练，尽管基座模型参数量接近 SWE-1.7 的三倍，仍降低了内存占用和训练-推理差异。Cognition 还将强化学习环境数量增加三倍，并构建了飞轮机制，让之前的 SWE-2 检查点迭代地强化其验证器。

hackernews · seelos · 9月10日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49645443)

**核验**: 多源印证

**背景**: SWE-2 是 Cognition 公司开发的软件工程编程模型，该公司是 Devin 自主编程代理的开发商。该模型基于 Moonshot AI 的 Kimi K3（2.8 万亿参数基座模型）进行后训练，整个成本-性能曲线在单次强化学习运行中通过数学推导的成本惩罚项完成优化。Anthropic 的 Claude Fable 5.1 和 OpenAI 的 GPT-6 Astra（GPT-Astra）是这一领域的领先竞品模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE-2: Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://alphasignal.ai/news/cognition-s-swe-2-beats-gpt-5-6-sol-at-64-lower-cost">Cognition's SWE-2 Beats GPT-5.6 Sol at 64% Lower Cost | AlphaSignal</a></li>
<li><a href="https://ai-tldr.dev/releases/cognition-swe-2/">SWE-2 — Cognition's coding model lands within a… | AI/TLDR</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍持怀疑态度。评论者指出 Terminal Bench 2.1（92.8%）与 Terminal Bench 4（27.3%）之间的巨大差距是基准过拟合的证据，回忆起 Cognition 早前 Devin 演示的失败，并批评闭源策略，质疑用户为何不选择 DeepSeek Flash 4.1 等开源模型。一些人承认，在 Kimi K3 这样强大的基座上做后训练，SWE-2 不太可能完全不行。

**标签**: `#AI agents`, `#coding model`, `#benchmark`, `#closed-weights`, `#Cognition`

---

<a id="item-9"></a>
## [Cursor 推出 Projects：协调者智能体调度数千子智能体处理大型任务](https://cursor.com/blog/projects) ⭐️ 7.92/10

Cursor 发布了 Projects（beta），通过协调者智能体调度数千个子智能体并行处理功能开发、迁移和持续性维护等大型任务。协调者本身不写代码，而是委派其他智能体执行，因此始终保持响应、不会被阻塞。 这是 AI 驱动开发工具领域的重要里程碑，代表了 Cursor 所设想的'软件开发第三时代'愿景的具体落地——由智能体集群承接整体工作。Cursor 报告了显著的效率提升：新用户合并的 PR 数量增加 30%，而主要使用 Projects 的用户合并量达到六倍之多。 Projects 默认在云端计算上运行，关闭笔记本不会中断工作，当需要在用户机器上测试时可以启动本地智能体。其三大核心能力包括：默认云端执行、跨所有智能体同步的共享上下文文件，以及订阅机制——协调者可以监控 Slack 频道、按计划运行、跟踪 PR 并修复 CI，无需用户手动提示。

aihot · Cursor Blog · 9月10日 12:00 · [中文阅读](https://aihot.news/items/cmtw4o8qc03iwrolkwc03elil)

**核验**: 多源印证

**背景**: 协调者智能体（coordinator agent）是多智能体系统中的中央监督组件，负责路由任务、管理状态并让自主运行的子智能体保持对齐以产出连贯结果。子智能体（subagent）是任务型的专门化智能体，由主智能体统一编排而不是各自追求独立目标。Cursor 的 Projects 将这一架构应用于软件开发，让开发者从管理单个智能体的层面上升到更高抽象层级，直接指挥工作本身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2045243203360642661">多智能体系统（Multi-Agent Systems）：协调器、专门化 Agent 与通信机制 - 知乎</a></li>
<li><a href="https://www.emergentmind.com/topics/coordinator-agent">Coordinator Agent in Multi-Agent Systems</a></li>
<li><a href="https://developer.aliyun.com/article/1754388">一文读懂什么是 Subagent -阿里云 开 发 者社区</a></li>

</ul>
</details>

**标签**: `#Cursor`, `#AI 开发者工具`, `#智能体`, `#产品发布`

---

<a id="item-10"></a>
## [OpenAI 在 API 中推出全双工语音模型 GPT-Live-1](https://openai.com/index/introducing-gpt-live-1-in-the-api) ⭐️ 7.75/10

OpenAI 在 API 中发布了全双工语音模型 GPT-Live-1，可同时进行听与说。前端语音层定价为每分钟 $0.05，推理和工具调用则委派给 GPT-6 Astra 等后端模型。 这是 AI 开发者工具的一大进展，可实现实时、接近人类的语音交互。它有望改变语音应用的开发方式，消除轮次式对话的延迟，并允许用户自然地打断对话，相比以往语音助手是重要一步。 GPT-Live-1 负责语音前端（听与说），将推理和工具调用委派给 GPT-6 Astra 等后端大模型。语音层按每分钟 $0.05 计费，对开发语音应用的开发者而言定价清晰且门槛较低。

aihot · OpenAI：官网动态（RSS · 排除企业/客户案例） · 9月10日 00:00 · [中文阅读](https://aihot.news/items/cmtvsgyqs05vkrofbgg06yzsa)

**核验**: 多源印证

**背景**: 传统语音 AI 系统采用半双工轮次机制，就像对讲机一样，一方说话时另一方只能听，导致明显延迟且难以打断对话。全双工模型支持同时听与说，更接近人类自然对话方式。此前的模型如基于 GPT-4o 的 ChatGPT 高级语音模式（Advanced Voice Mode）仍遵循一来一回的轮次机制，因此 GPT-Live-1 是重要的一步进展。文中提到的后端模型 GPT-6 Astra 是 OpenAI 的大语言模型，支持 105 万 token 的上下文窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mblank5.github.io/llm-wiki/concepts/full-duplex-speech-model.html">全双工语音模型（Full-Duplex Speech Model） — LLM 研究知识库</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#语音模型`, `#API`, `#AI开发者工具`, `#全双工`

---

<a id="item-11"></a>
## [Anthropic 评测 AI 模型的战术情报定位与常规武器开发能力](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities) ⭐️ 7.17/10

Anthropic 前沿红队发布了新的评测，用于衡量 AI 模型在战术情报定位（例如根据碎片化信息确定人员位置）和常规武器开发（例如设计无人机攻击移动目标）方面的能力。随附报告还记录了 AI 在监视和武器开发领域被滥用的真实案例，并介绍了 Anthropic 为阻断此类滥用而新部署的分类器。 这项研究表明，AI 模型正逐渐被试图滥用平台从事监视和常规武器开发的行动者所利用，而这类领域的研究远少于网络安全与生物风险。该报告凸显了平台内安全措施的必要性，并警示 AI 在情报与军事领域的能力短期内不太可能进入平台期。 在同一评测中，来自中国开发者的开放权重模型表现落后于前沿水平（通常介于 Sonnet 级与 Mythos 级模型之间），但仍展现出识别与瞄准对手、提升武器性能的令人担忧的能力。评测对应'杀伤链'各环节（发现、定位、跟踪、瞄准、打击、评估），而历史上这些环节的显著改进都依赖稀缺的高水平人类专家。

aihot · Anthropic：Research（发表成果 · 网页） · 9月10日 17:28 · [中文阅读](https://aihot.news/items/cmtvsxbrc068orofbs09dpez3)

**核验**: 多源印证

**背景**: 情报定位是指'发现'并'锁定'人员、账户、设施或车辆等目标的过程，位于情报循环的最前端，历史上投入了大量人力。常规武器开发则包括为无人机设计末段制导以及 GPS 干扰条件下的导航能力，正如近期冲突中光纤制导无人机在乌克兰等战场上的部署。由于这些任务劳动密集且依赖专家判断，AI 在数据分析与编码方面的进步如今引发了新的国家安全担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/team/frontier-red-team">Frontier Red Team Research \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/frontier-threats-red-teaming-for-ai-safety">Frontier threats red teaming for AI safety \ Anthropic</a></li>
<li><a href="http://www.news.cn/milpro/20250409/bd40a0a29f8043f7911ba44f0dbfc944/c.html">俄乌战场上的创新——光纤无人机 -新华网</a></li>

</ul>
</details>

**标签**: `#AI安全`, `#模型评估`, `#Anthropic`, `#军事应用`, `#前沿研究`

---

<a id="item-12"></a>
## [OpenAI Codex Python SDK v0.154.0 新增 Max/Ultra 推理努力值与 ExternalMessage](https://github.com/openai/codex/releases/tag/python-v0.154.0) ⭐️ 7.0/10

OpenAI 发布了 Codex Python SDK 的 python-v0.154.0 版本，可通过 `pip install --upgrade openai-codex==0.154.0` 安装（需 Python 3.10 及以上）。该版本新增 `max` 和 `ultra` 推理努力值，在同步与异步的 `run()` 和 `turn()` 调用中引入 `ExternalMessage`，并新增 `include_turns`、`turn_service_tier` 和 `source` 元数据选项。 这次更新让将 Codex 作为 SDK 使用的开发者能更精细地控制模型推理努力程度，并允许外部智能体或工具向 Codex 回合注入内容，而无需授予用户级授权。这些能力对于构建多智能体工作流的团队，以及需要 Codex 处理异常困难问题的用户都很有价值。 升级时需注意迁移改动：`HookMetadata` 现在将 handler 包装在 `.root` 中（例如 `hook.root.command`），部分此前未知的通知现在带有类型化载荷，应通过具名字段读取。手动构造或迟加入的 turn handle 只能从其挂载点开始接收事件，因此结果可能不完整，在完成后挂载可能抛出 `TransportClosedError`；自定义 `codex_bin` 覆盖需要 CLI 0.151.0 及以上版本。

github · aibrahim-oai · 9月10日 19:51

**核验**: 多源印证

**背景**: Codex 是 OpenAI 的轻量级编程智能体，可在本地运行，能够可靠地完成构建功能、复杂重构和迁移等任务，由 OpenAI 的前沿编程模型驱动。推理努力值是一种路由决策而非质量标签，`max` 适用于单个异常困难的问题，`ultra` 则适用于并行子智能体可能有帮助的场景。`ExternalMessage` 专为来自其他智能体、工具或应用程序的不可信内容设计，保留工具级权限而非授予用户授权或批准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in ...</a></li>
<li><a href="https://github.com/openai/codex/blob/main/sdk/python/examples/README.md">codex/sdk/python/examples/README.md at main · openai/codex</a></li>
<li><a href="https://kingy.ai/news/openai-codex-reasoning-levels-low-medium-high-extra-high/">Codex Reasoning Levels: Light to Ultra Explained</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#AI工具`, `#版本更新`, `#Python`

---

<a id="item-13"></a>
## [Vibe Coding 让普通人也能自己搓工具](https://x.com/dotey/status/2097946976524399075) ⭐️ 7.0/10

微博 VibeLab AI 创意赛收官，共收到 2500 多件原创作品，话题阅读量超过 2.4 亿。作者以评委身份观察到，Vibe Coding 已把编程从专业技能降为语言表达能力，普通人无需专业代码知识即可指挥 AI Agent 造出自己的工具。 这标志着软件开发领域的重大变化：AI Agent 正在让编程平民化，让个人能够满足被商业软件忽视的长尾需求。它重新定义了“谁能做软件”，重塑个人开发生态，让编程从专家专属技能变成一种创意表达能力。 文中列举的案例包括 SiaoCut——面向 Windows 用户的 macOS 专用工具 BaoCut 替代品，以及开源的 Bridgic Agent，能把目标转化为可长期运行、随时修改的工作流。作者还回顾了模型能力从 GitHub Copilot 的代码补全到 Claude Code 自主探索项目的演进，并提到赛期正值 Kimi K3 发布，很快被创作者用于体检报告、斗地主等工具。

twitter · 宝玉 · 9月10日 07:15

**核验**: 多源印证

**背景**: Vibe Coding 是由 Andrej Karpathy 推广的术语，指的是一种“完全跟着感觉走”的编程方式：使用者接受 AI 生成的代码而不必完全理解，程序员主要承担引导、测试和反馈的角色，而不是手写代码。它源于大语言模型的快速进步，从 GitHub Copilot 这类补全助手，演进到 Claude Code 这类能自主探索项目并实现完整功能的 Agent。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/Vibe_coding">vibe coding - 维基百科，自由的百科全书</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>
<li><a href="https://zenn.dev/aoyamadev/articles/7befbf4f5a0448">Vibe Coding - 概 要</a></li>

</ul>
</details>

**标签**: `#Vibe Coding`, `#AI Agent`, `#长尾需求`, `#个人开发者`, `#AI工具`

---

<a id="item-14"></a>
## [AI Agent 代码审查的三步提示词框架](https://x.com/dotey/status/2097878840655626568) ⭐️ 7.0/10

开发者@dotey 分享了一个引导 AI Agent 进行代码审查的三步提示词框架：先搞清楚 PR 要解决的问题，再思考在没看实现的情况下你会如何解决，最后在审查时将你自己的方案与实际代码进行对比。 该框架为提升 AI 辅助代码审查的质量提供了一种实用的方法，帮助开发者从 Agent 编程工具中获得更一致、更有洞察力的反馈。随着 AI 编程助手在日常开发流程中越来越普及，这类提示词设计模式可以有效改善开发成果。 该方法先让 Agent 在未受实际实现影响的情况下形成自己的解决方案，从而更容易发现实现中的缺陷或更优的替代方案。提示词简洁可操作，仅由三个有序步骤构成，引导 Agent 一步一步地进行连贯推理。

twitter · 宝玉 · 9月10日 02:44

**核验**: 待核验

**背景**: 代码审查是常见的工程实践，开发者通过审核 pull request（PR）来发现缺陷、保证质量并共享知识。AI Agent 可以自动化或辅助这一过程，但效果很大程度上取决于提示词的写法。该框架采用先独立构思再对比的方案，使审查更有价值，也更不容易被已提交的代码带偏。

**标签**: `#AI Agent`, `#代码审查`, `#提示词工程`, `#开发经验`

---

<a id="item-15"></a>
## [OpenClaw 实现快速云端会话，支持远程终端、WebVNC 与 CUA](https://x.com/steipete/status/2097935551735423464) ⭐️ 7.0/10

Peter Steinberger 宣布 OpenClaw 中的云端会话现已实现快速运行。新增功能包括远程终端（Remote Terminal）、WebVNC 以及用于计算机操作的 CUA。 这显著增强了 OpenClaw 作为开源 AI 代理的实力，使用户能够通过基于浏览器的终端和可视化界面远程控制机器。它将基于云的代理操作进一步融入主流开发者工作流，拓展了自主 AI 代理的运行场景。 该功能将远程终端、WebVNC（基于浏览器的 VNC 客户端）和 CUA（计算机使用代理）能力整合到同一云端会话中。这使得 AI 代理能够像人类一样与图形用户界面交互，同时保持基于浏览器且响应快速的访问体验。

follow_builders · Peter Steinberger · 9月10日 06:29

**核验**: 多源印证

**背景**: OpenClaw（原名 Clawdbot）是一款免费开源的自主 AI 代理，通过大语言模型执行任务，并以 WhatsApp、Telegram 等即时通讯平台作为主要用户界面。VNC 是一种远程桌面控制协议，而 noVNC 是业界标准的基于浏览器的 VNC 客户端，无需安装插件。CUA（Computer-Using Agent，计算机使用代理）是一种将视觉能力与推理相结合的模型概念，使代理能够像人类一样操作图形用户界面——按钮、菜单和文本字段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://www.cendio.com/novnc/">noVNC, the universal web-based VNC client | ThinLinc by Cendio</a></li>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent - OpenAI</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#开源AI工具`, `#开发者工具`, `#云端会话`, `#CUA`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="9"><span>其他追踪推文</span><span class="archive-tab-count">9</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="5"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">5</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2098183477950603367">@dotey: Shopify 宣布：从 React Native 全面回归原生开发 Shopify 曾经是 React Native 铁杆支持者，2020 年，Shopify 选择“All-in”全面...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月10日 22:54 UTC · 喜欢 37 · 转发 5 · 回复 3 · 浏览 9218</p>
<p class="archive-item-content">Shopify 宣布：从 React Native 全面回归原生开发<br>
<br>
Shopify 曾经是 React Native 铁杆支持者，2020 年，Shopify 选择“All-in”全面拥抱 React Native，实现了功能的“一次编写，多端运行”，而现在 Shopify 正在将旗下所有的移动端应用，从 React Native 彻底迁移回 Swift 和 Kotlin。<br>
<br>
这个决定主要是由于 AI 在 Coding 能力的增强，现在的 Coding Agent 可以直接拿着 iOS 版本的代码写出对应的 Android 版本，反之亦然。<br>
<br>
AI 能帮助开发者打破技术栈的边界，去编写自己平时并不熟悉的编程语言，还能通过共享的代码规范、测试用例和代码审查机制，让两个平台的应用始终保持高度一致。<br>
<br>
而且借助 AI 效率很高，Shopify 的核心购物应用 Shop 仅仅用了 12 个星期，就完成了从最初的概念验证，到完全重构的原生 App 并在应用商店上架的整个过程。Shopify 其他应用的重构工作目前也在紧锣密鼓地推进中。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2098117256282558799">@dotey: 官宣了，暂停 200 美元的 ChatGPT Pro 订阅……</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月10日 18:31 UTC · 喜欢 94 · 转发 3 · 回复 40 · 浏览 65785</p>
<p class="archive-item-content">官宣了，暂停 200 美元的 ChatGPT Pro 订阅……</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2098113585683808624">@thsottiaux: To make sure our current users have an incredible experience and continued access to Astra, w...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月10日 18:17 UTC · 喜欢 11870 · 转发 681 · 回复 1938 · 浏览 2523654</p>
<p class="archive-item-content">To make sure our current users have an incredible experience and continued access to Astra, we are going to pause subscriptions to our $200 Pro plan. These put the most strain on our systems and we wanted to take the smallest step that allows us to continue giving the broadest access possible. All other plans and the api remain available.<br>
<br>
There is no impact to existing accounts and we are working on adding more capacity as fast as we can. Thanks!</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/mustafa01ali/status/2098047492772249730">@mustafa01ali: https://t.co/PcXPOu2rAf</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月10日 13:54 UTC · 喜欢 4050 · 转发 347 · 回复 186 · 浏览 1059581</p>
<p class="archive-item-content">https://t.co/PcXPOu2rAf</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/tianyi/status/2097993855778046379">@tianyi: DeepSeek 开源了一些新的代码仓库，方便更容易地部署 V4.1 Flash 以及后续的开源模型： https://t.co/rPbPtWOFYi https://t.co/6Qrd...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月10日 10:21 UTC · 喜欢 959 · 转发 80 · 回复 68 · 浏览 59970</p>
<p class="archive-item-content">DeepSeek 开源了一些新的代码仓库，方便更容易地部署 V4.1 Flash 以及后续的开源模型：<br>
<br>
https://t.co/rPbPtWOFYi<br>
https://t.co/6Qrd21r3mG<br>
https://t.co/RFo1xIhV8h</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2097905476382118107">@op7418: 真的很离谱，这个人之前在 OpenAI，后来去 Anthropic 上班，上了三个星期还是六个星期就离职了。 然后输出了一堆 AI 末日论的信息，全是观点，没有事实。 1.3 亿的曝光，...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 9月10日 04:30 UTC · 喜欢 315 · 转发 5 · 回复 153 · 浏览 75273</p>
<p class="archive-item-content">真的很离谱，这个人之前在 OpenAI，后来去 Anthropic 上班，上了三个星期还是六个星期就离职了。<br>
<br>
然后输出了一堆 AI 末日论的信息，全是观点，没有事实。<br>
<br>
1.3 亿的曝光，很难想象大家为什么都很相信这个东西</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2097887156396003698">@dotey: 在无人关注的角落，Meta 也重置了</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月10日 03:17 UTC · 喜欢 57 · 转发 1 · 回复 112 · 浏览 34352</p>
<p class="archive-item-content">在无人关注的角落，Meta 也重置了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/alexandr_wang/status/2097880616041885901">@alexandr_wang: we just reset everyone’s muse token usage. enjoy!!! https://t.co/Kgfr9sCVvn</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月10日 02:51 UTC · 喜欢 5476 · 转发 156 · 回复 751 · 浏览 995486</p>
<p class="archive-item-content">we just reset everyone’s muse token usage.<br>
<br>
enjoy!!! https://t.co/Kgfr9sCVvn</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/uge198568/status/2097866584639606855">@uge198568: 这是一封年入百万知识付费的检讨书： 同样作为一把“镰刀”，这是我停更 3 个月一直在思考的事。 所有事情都有周期性的，而这就是知识付费的周期 就是所有观众都被教育之后，群体意识觉醒，慢慢...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月10日 01:55 UTC · 喜欢 37 · 转发 9 · 回复 78 · 浏览 6903</p>
<p class="archive-item-content">这是一封年入百万知识付费的检讨书：<br>
同样作为一把“镰刀”，这是我停更 3 个月一直在思考的事。<br>
<br>
所有事情都有周期性的，而这就是知识付费的周期<br>
<br>
就是所有观众都被教育之后，群体意识觉醒，慢慢发现做知识付费的博主，自身没有知识付费以外的商业版图，那就是一场收割盛宴谢幕之时。<br>
<br>
知识付费应该是额外增加现金流，同时个人偏好喜欢帮助别人，获取自我价值的实现。<br>
<br>
如果一个知识付费的博主，特别是商业博主，自身都没落地的项目在实现被动收入的时候，那这个人至少在搞流量，获客，卖课的这件事上是值得我们学习的，而不是那个人的课程。<br>
<br>
而对于知识博主来说，可能也存在一个很大的陷阱，足以让自己翻车的陷阱。<br>
<br>
那就是真的稳定，长期的实体项目，盈利效率前期是很低的，甚至是亏损的，那怎么都不如知识付费来钱快。<br>
<br>
这也就是大多数知识付费的博主扛不住第一个生命周期的原因。<br>
<br>
这件事的客观规律是什么？<br>
<br>
1，利润是对承担不可转移风险与解决物理摩擦的补偿。<br>
卖课程的高毛利，很大程度是因为它避开了供应链、物流、售后、团队组织等沉重的物理世界阻力。<br>
但商业世界的规律是：没有阻力的地方，通常也没有壁垒。<br>
实体或深度落地业务前期之所以盈利艰难甚至亏损，是因为资本和精力都沉淀在了那些“脏活、累活、慢活”上。<br>
这些繁琐的交付细节虽然拉低了短期收益率，但它们也是在构筑护城河，让别人无法在三五天内靠复制文案就抢走自己的生意。<br>
<br>
2，现金流不等于商业资产，很多博主容易把“高爆发的短期现金流”误判为“可持续的商业资产”。<br>
卖课赚到的是即时兑现的流水，但纯 IP 本身的生命周期极其脆弱，一旦受众对博主的人设产生疲劳或信任透支，获客成本就会呈指数级飙升。<br>
而真正的商业资产是稳定的供应链、标准化的产品体系、可复用的组织流程和具有高黏性的客群关系，这才能在周期轮动中提供长久的抗风险能力。<br>
所以当我做了一年知识付费之后就发现，我无法教会的人，他们最终会对我失去信任，这里不在乎是谁的责任，只看结果。这里最尴尬的地方是，这些用户必须对我失去信任，因为只有这样，才能合理化为什么同样的方法有点人成功，而我没有成功？那肯定不是我的问题，必须是外部原因。这是人性。<br>
<br>
3，健康的商业循环遵循“能力溢出”，而非“内卷自噬”。<br>
长期立得住的商业形态，往往是自身主营业务跑通后形成的副产品。<br>
实战经验是主资产，分享与教学只是近乎零边际成本的渠道放大器和信任放大器。<br>
一旦主客颠倒，一个人唯一的造血来源变成了“教别人如何赚钱”，商业逻辑就沦为了自我参照的封闭循环。<br>
靠售卖方法论维持的方法论，终究会被现实的交付结果击穿。<br>
<br>
当这些思考完毕之后，我决定停掉所有知识付费产品，只保留和我链接的付费社群，从而开始落地自己非知识付费的商业资产和落地业务，用自己的认知和知识去完成具体的业务，而不是打包变现。</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/levie/status/2097920810543468551">Aaron Levie: The world is going to be using coding agents for far more than anyone would have thought befo...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Aaron Levie：编码代理的使用范围将远超想象</p>
<p class="source-line">Follow Builders · X 动态 · Aaron Levie · 9月10日 05:31 UTC · 喜欢 70 · 转发 10 · 回复 14</p>
<p class="archive-item-content">Aaron Levie 认为编码代理将大幅扩展应用场景，降低成本并提升工程师杠杆，而非减少需求。</p>
<p class="archive-item-translation"><span>中文摘要</span>Aaron Levie 表示降低代码成本将催生更多软件应用，提升工程师杠杆，并增加而非减少对工程师的需求。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2097912273264095536">Thibault Sottiaux: One of the greatest joys is debating new model names with researchers. They come up with the...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>研究者分享模型命名讨论的乐趣</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 9月10日 04:57 UTC · 喜欢 2971 · 转发 58 · 回复 808</p>
<p class="archive-item-content">一位研究者分享关于模型命名讨论的趣味观察。</p>
<p class="archive-item-translation"><span>中文摘要</span>一位研究者分享关于模型命名讨论的趣味观察，无实际技术内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2097880507753382201">Peter Steinberger: Dashboards/Mini-Apps was something I pushed two months ago and now it replaced lots of custom...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Steinberger：我两个月前推动的仪表盘/小程序现已取代大量定制工具</p>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 9月10日 02:51 UTC · 喜欢 161 · 转发 5 · 回复 21</p>
<p class="archive-item-content">Peter Steinberger 分享了他推动 Dashboards/Mini-Apps 取代团队定制工具的经验，强调一切成为侧边栏条目、仪表盘或插件。</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Steinberger 分享了他两个月前推动的仪表盘/小程序现已取代团队服务器上大量定制工具，所有功能都变成侧边栏条目、仪表盘或插件。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2097870497505837478">Nikunj Kothari: Finally https://t.co/7cyHiAyVQO</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari：终于</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 9月10日 02:11 UTC · 喜欢 44 · 转发 1 · 回复 1</p>
<p class="archive-item-content">一条含糊的推文，仅表示&#x27;终于&#x27;并附上链接，未提供任何实质内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2097837950612717804">Guillermo Rauch: AI Benchmarks with @Benchmark &amp; @Vercel. It&#x27;s ① the most aptly named event in SF history and...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：与@Benchmark 和@Vercel 共同举办的 AI 基准测试活动</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 9月10日 00:01 UTC · 喜欢 183 · 转发 4 · 回复 25</p>
<p class="archive-item-content">Guillermo Rauch 推广一场关于 AI 基准测试的活动，由 Benchmark 和 Vercel 合作举办。</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 在推广一场由 Benchmark 和 Vercel 合作举办的 AI 基准测试活动。</p>
</article>
</div>
</section>
