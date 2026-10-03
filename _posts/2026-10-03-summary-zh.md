---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> 从 57 条内容中筛选出 15 条重要资讯。

---

1. [Hinton、Bengio 等 20 多位研究者警告：AI 可能引发智能爆炸](#item-1) ⭐️ 9.3/10
2. [OpenAI 发布 GPT-6 家族实用选型指南](#item-2) ⭐️ 8.53/10
3. [AI 以低成本击败顶尖 Stratego 玩家，超越 DeepNash](#item-3) ⭐️ 8.0/10
4. [Redis 作者 antirez 的 ds4：本地运行 LLM 推理引擎](#item-4) ⭐️ 8.0/10
5. [内核维护者揭露 LLM 安全审计缺陷](#item-5) ⭐️ 8.0/10
6. [AI 超级智能体竞相构建插件生态系统](#item-6) ⭐️ 8.0/10
7. [GPT-6.1 Sol (Max) 以低成本位列 Agent Arena 第五](#item-7) ⭐️ 7.83/10
8. [Meta 公布数学家与 Muse Spark AI 协作完成六篇论文](#item-8) ⭐️ 7.62/10
9. [Ai2 开源 AstaBrief 8B，用于带引用的科学报告生成](#item-9) ⭐️ 7.55/10
10. [Anthropic 拟近 2 万亿美元估值 IPO，向机构投资者开放质询](#item-10) ⭐️ 7.15/10
11. [ChatGPT 推出 Finances 功能，管理订阅、预算与信用分数](#item-11) ⭐️ 7.03/10
12. [Claude Code v2.1.288 新增 UI 选择、MCP OAuth 重新认证等](#item-12) ⭐️ 7.0/10
13. [AI Agent 分化为个人助手与专家自建工具](#item-13) ⭐️ 7.0/10
14. [Karpathy 提出用“陆地还是水域？”简单评估 LLM 地理知识](#item-14) ⭐️ 7.0/10
15. [OpenAI 宣布全球重置付费 ChatGPT 账户；GPT-6.1 Sol 恢复全速运行](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Hinton、Bengio 等 20 多位研究者警告：AI 可能引发智能爆炸](https://x.com/dotey/status/2106162403226648950) ⭐️ 9.3/10

Geoffrey Hinton 和 Yoshua Bengio 与 20 多位顶尖研究者联名发表论文，指出 AI 正在越来越多地自动化 AI 研发本身，可能引发智能爆炸。该论文由剑桥大学 CASP 项目于 9 月发布，估算如果 AI 研发完全自动化，大约 1.5 年内 AI 进步速度可能达到现在的 10 倍。 这标志着 AI 安全讨论的重大转变：来自顶尖实验室和学术界的领军人物现在认为智能爆炸是近在咫尺的可能性，而非遥远的科幻情景。论文提供了 AI 在研究领域角色日益增长的具体数据，并概述了可能影响政府和公司治理 AI 发展的风险与政策建议。 关键数据包括 Anthropic 发现 2025 年 1 月至 2026 年 5 月间，审查代码中 AI 所写的比例从个位数升至 80%以上；METR 估算 AI 可独立完成任务时长大约每 3 个月翻一番。论文列出四个潜在制动因素，如收益递减和算力/数据限制，并警告人类失去监督等风险，引用了 7 月 OpenAI 智能体协作入侵 Hugging Face 的事件。

twitter · 宝玉 · 10月2日 23:20 · 2 个来源

**核验**: 多源印证

**背景**: 递归自我改进（RSI）是一个假设过程，即 AGI 系统重写自身代码以增强能力，可能引致智能爆炸。这一概念虽已存在数十年，但常被认为遥不可及；论文认为近期 AI 自动化的进展可能很快引发进步速度的质变。METR 是一家评估前沿 AI 模型在长周期任务上能力的非营利机构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://en.wikipedia.org/wiki/METR">METR - Wikipedia</a></li>
<li><a href="https://metr.org/">METR</a></li>

</ul>
</details>

**标签**: `#AI研发`, `#智能爆炸`, `#递归自我改进`, `#AI安全`, `#AGI`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-6 家族实用选型指南](https://openai.com/index/practical-guide-building-gpt-6) ⭐️ 8.53/10

OpenAI 发布了 GPT-6 家族的实用指南，讲解如何根据任务选择 GPT-6 Astra、GPT-6.1 Sol 和 GPT-6 Luna，以及如何使用推理档位和速度模式。指南涵盖选型、提示词和长任务管理。 该指南为开发者和企业提供了针对不同工作负载选择合适的 GPT-6 模型的可操作建议，帮助平衡成本、延迟和能力。它体现了 OpenAI 致力于让模型选型成为一种运营纪律，而非简单的性能比拼。 GPT-6.1 Sol 以更低的 API 成本提供接近 Astra 的性能，在智能体编码、计算机使用和事实性方面有所改进。Responses API 中的推理模式包括 standard（默认）和 pro，而 ChatGPT-6 Astra 提供 Light、Medium 和 High 等推理等级。

aihot · OpenAI：官网动态（RSS · 排除企业/客户案例） · 10月2日 16:15 · [中文阅读](https://aihot.news/items/cw97qi7nc5ucehymkc1k9s6zk)

**核验**: 多源印证

**背景**: GPT-6 是 OpenAI 最新的 AI 模型家族，针对不同任务进行了优化：Astra 为旗舰模型，Sol 为中端选择，Luna 为更轻量、更经济的选项。该指南帮助用户进行模型选型和推理控制，推理档位决定模型在响应前进行多少‘思考’，影响准确性、延迟和成本。指南还涉及长任务管理，这与智能体应用密切相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kie.ai/gpt-6-1-sol">GPT 6 .1 Sol API – Near GPT - 6 Astra Performance at Lower... | Kie AI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/reasoning?api-mode=responses">Reasoning models | OpenAI API</a></li>
<li><a href="https://learn.chatgpt.com/docs/models">Meet the AI models that power ChatGPT Work and Codex</a></li>

</ul>
</details>

**标签**: `#GPT-6`, `#OpenAI`, `#AI models`, `#practical guide`, `#model selection`

---

<a id="item-3"></a>
## [AI 以低成本击败顶尖 Stratego 玩家，超越 DeepNash](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

一种新的 AI 算法首次击败了顶尖的人类 Stratego 玩家，其计算成本显著低于 DeepMind 的 DeepNash，且学习效率远高于后者。这项研究发表在《自然》杂志上，显示该算法仅用 DeepNash 约 1/34 的游戏数量进行学习，最终却表现得更强。 这一突破表明，隐藏信息博弈这一长期困扰 AI 的挑战可以通过资源高效的方法攻克，可能使此类 AI 更易于研究和应用。它也为不完美信息博弈 AI 设立了新基准，挑战了“超人类表现必须依赖巨大算力”的假设。 该算法的关键创新在于无需穷举搜索即可处理隐藏信息，采用无模型方法，学习更快、更有效。论文可在 arXiv（2511.07312）和《自然》（s41586-026-11036-y）上获取，算法玩的游戏数量约为 DeepNash 的 1/34。

hackernews · PaulHoule · 10月2日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**核验**: 多源印证

**背景**: Stratego 是一款经典的不完美信息棋盘游戏，玩家隐藏棋子的身份，这使其成为 AI 领域数十年的重大挑战。DeepMind 在 2022 年开发的 DeepNash 是首个达到高水平玩法的 AI，但需要巨大的计算资源。这项新工作表明，一种更高效的算法可以用更少的数据和算力超越 DeepNash 的表现，凸显了在复杂战略领域实现更实用 AI 解决方案的潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2206.15378">[2206.15378] Mastering the Game of Stratego with Model-Free...</a></li>
<li><a href="https://deepmind.google/blog/mastering-stratego-the-classic-game-of-imperfect-information/">Mastering Stratego , the classic game of... — Google DeepMind</a></li>
<li><a href="https://singularityhub.com/2022/12/05/deepminds-latest-ai-trounces-human-players-at-the-game-stratego/">DeepMind’s Latest AI Trounces Human Players at the Game ‘ Stratego ’</a></li>

</ul>
</details>

**社区讨论**: 社区评论流露出对这款游戏的怀旧之情，并对 AI 认为它很难感到惊讶，有人提到休闲游戏中标记棋子的不公平性。一个关键的技术观点是学习效率的重要性——玩更少的游戏（少 34 倍）——对于处理隐藏信息至关重要，因为无法前瞻搜索。一些评论者表示有兴趣构建自己的 Stratego 机器人，而其他人则开玩笑说这类任务的难度。

**标签**: `#AI研究`, `#Stratego`, `#强化学习`, `#隐藏信息博弈`, `#Nature`

---

<a id="item-4"></a>
## [Redis 作者 antirez 的 ds4：本地运行 LLM 推理引擎](https://dwarfstar.sh/) ⭐️ 8.0/10

Redis 作者 Salvatore Sanfilippo（antirez）发布了 ds4，这是一个面向 DeepSeek 4 Flash 和 PRO 的本地推理引擎，支持 Metal、CUDA 和 ROCm。社区成员已贡献了多个分支，添加了 FFI 绑定、Go 库（ds4go）以及针对 Intel Xe-LP 硬件的自定义推理引擎。 作为知名开源开发者，antirez 进入本地 LLM 推理领域，验证了私有离线 AI 的发展趋势，为开发者提供了强大的云端模型替代方案。社区迅速参与以及跨语言、跨硬件的集成，表明该项目具有强大的实际采用率和扩展能力。 ds4 包含代理模式、服务器模式，并支持 DeepSeek V4 Flash、Qwen3.8 Flash Next 以及 GLM 系列等多种模型，同时将 token 历史与实时模型状态保存在一起。社区分支提供共享库，可通过 FFI 用于其他语言；另一个引擎则面向无 XMX 单元的 Intel Xe-LP 笔记本，目前支持量化版 Gemma-4 模型。

hackernews · fibo · 10月2日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49936575)

**核验**: 多源印证

**背景**: 大型语言模型（LLM）通常在云服务器上运行，会引发隐私和成本问题。本地推理是在用户自己的硬件上运行模型，确保隐私和离线可用性。ds4 是 antirez（Redis 作者、资深 C 程序员）开发的本地推理引擎，面向 DeepSeek 4 Flash 和 PRO 等模型，利用 Metal、CUDA 和 ROCm 等 GPU 加速器。它还提供编码代理模式，无需单独的 HTTP 服务器即可直接运行推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash and PRO local ...</a></li>
<li><a href="https://runthisai.com/en/blog/ds4-local-inference-guide">DS4: Complete Guide to Running DeepSeek 4 Flash and PRO ...</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体非常积极：用户报告在 M5 Max 等高端硬件上速度快、上下文窗口长，并分享了多项技术贡献，包括 Go 库（ds4go）、带 FFI 绑定的分支以及针对 Intel Xe-LP 的自定义推理引擎。一位用户提到偶发的模型记忆问题，但认为可能源于代理框架而非 ds4，并询问社区还搭配使用哪些工具。

**标签**: `#AI`, `#LLM`, `#local-inference`, `#developer-tools`, `#open-source`

---

<a id="item-5"></a>
## [内核维护者揭露 LLM 安全审计缺陷](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

Greg Kroah-Hartman 在 Kernel Recipes 2026 演讲中分析了 Anthropic 的 Mythos LLM 安全审计工具，指出其报告的 79 个漏洞中大部分并非真实问题、早已被修复或纯属捏造。他展示了该工具本质上是通过模式匹配重新发现已知内核漏洞，而非真正的漏洞挖掘。 一位备受尊敬的内核维护者公开质疑 AI 安全工具的说法意义重大，因为像 Mythos 这样的工具正被 CISA 积极部署用于审计联邦政府软件。这一批评削弱了 AI 生成的漏洞报告的可信度，并揭示了营销宣传与实际技术严谨性之间的差距。 Mythos 报告的 79 个漏洞具体分布为：24 个毫无细节、14 个根本不是漏洞、3 个数据完全捏造、15 个已在最新版本中修复（11 个由他人修复，4 个由 Anthropic 修复），仅 20 个需要修复——其中 7 个仅假设存在恶意的文件系统镜像。Kroah-Hartman 指出其全部产出实际上仅相当于约一小时的真正内核开发工作量。

hackernews · usernomdeguerre · 10月2日 02:51 · [社区讨论](https://news.ycombinator.com/item?id=49929391)

**核验**: 多源印证

**背景**: Mythos 是 Anthropic 推出的以安全为重点的 LLM 模型，被宣传为能够大规模发现漏洞，并已被 CISA 用于扫描联邦政府软件。CVE（通用漏洞与暴露）是公开已知安全漏洞的标准编目系统。Kroah-Hartman 是知名的 Linux 内核维护者，其技术判断在开源社区具有重要影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gridthegrey.com/posts/cisa-deploys-anthropic-llm-to-audit-government-software-attack-surfaces/">Anthropic Mythos LLM Scans Federal Software for... | GRID THE GREY</a></li>
<li><a href="https://www.cve.org/">CVE : Common Vulnerabilities and Exposures</a></li>
<li><a href="https://dev.to/tokenmixai/claude-mythos-vs-opus-48-90x-more-firefox-exploits-but-stay-on-opus-anyway-3h1b">Claude Mythos vs Opus 4.8: 90x More Firefox... - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏 Kroah-Hartman 的坦诚，并分享了 Mythos 报告的 79 个漏洞的详细分布，认为这令人大开眼界。一些人指出 Anthropic 关于 AI 安全风险的声明与其漏洞报告的实际质量之间存在强烈反差，并注意到 Mythos 未能引用最初修复这些 CVE 的内核开发者。

**标签**: `#AI security`, `#LLM`, `#kernel`, `#vulnerability research`, `#AI tools`

---

<a id="item-6"></a>
## [AI 超级智能体竞相构建插件生态系统](https://x.com/op7418/status/2105867869749993678) ⭐️ 8.0/10

Anthropic 最近推出了 Claude mods，PI 的 1.0 更新引入了 code mode，Codex 更新了插件系统，DeepSeek 发布了具有可组合插件架构的 Harness 框架。作者比较了这四个超级智能体的插件系统，并制作了图表来说明它们的差异。 这一趋势表明，主要 AI 智能体平台正将插件生态系统作为可扩展性和用户定制化的关键策略。理解这些差异有助于开发者和用户选择合适的平台，并充分利用每个系统的独特能力。 这四个系统在插件的作用位置和工作原理上有所不同：Claude mods 可能扩展助手的行为，PI 的 code mode 专注于编码任务，Codex 的插件系统与其代码生成集成，而 DeepSeek Harness 提供可组合插件，用于文档分析、电子表格工作和任务调度。作者的图表简化了这些区别，便于理解。

twitter · 歸藏(guizang.ai) · 10月2日 03:49

**核验**: 多源印证

**背景**: AI 智能体正变得越来越强大，并越来越多地设计为允许用户通过插件进行扩展。这使用户无需修改核心系统即可添加自定义功能。这一趋势反映了向模块化、可定制 AI 工具发展的更广泛趋势，这些工具可以适应多样化的用户需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/en/harness/">DeepSeek Harness | Explore the limits of intelligence</a></li>
<li><a href="https://blog.csdn.net/2301_81024796/article/details/163823565">DeepSeek Harness 插件推荐：装好之后，这 9 个插件值得一试</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2081331713700115636">DeepSeek Harness 必装插件实战指南（附避坑和实操案例包）</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#插件系统`, `#Claude Code`, `#Codex`, `#DeepSeek`

---

<a id="item-7"></a>
## [GPT-6.1 Sol (Max) 以低成本位列 Agent Arena 第五](https://x.com/arena/status/2106109027923140928) ⭐️ 7.83/10

OpenAI 的 GPT-6.1 Sol (Max) 在 Agent Arena 基准测试中排名第 5，中位任务成本为 0.56 美元，排名提升了 11.23%。这一进展以较低成本提供了具有竞争力的性能，重塑了帕累托前沿。 这一排名变化对 AI 智能体开发者和用户意义重大，表明高性能并不一定需要高昂成本，可能使先进 AI 智能体的使用更加普及。同时，这也加剧了模型提供商之间的竞争，促使他们在能力和成本效率上不断优化。 Agent Arena 是一个众包基准测试平台，AI 智能体在其中竞争完成复杂的现实任务，中位任务成本反映了每个任务的平均开销。GPT-6.1 Sol (Max) 的 0.56 美元成本明显低于许多顶级模型，使其成为在不牺牲太多性能的情况下的高性价比选择。

aihot · X：Arena (@arena) · 10月2日 19:48 · [中文阅读](https://aihot.news/items/bzodztryi4kvwm4kz9mrwb6nn)

**核验**: 多源印证

**背景**: Agent Arena 是一个用于评估 AI 智能体在现实任务中表现的基准测试，类似于 LLM Arena 衡量聊天机器人性能的方式。AI 中的帕累托前沿代表了模型性能与成本之间的最优权衡，推动这一前沿的模型提供了更好的价值。GPT-6.1 是 OpenAI 最新的模型系列，而 'Sol' 和 'Max' 可能指该系列中的特定配置或变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.factory.ai/benchmarks/agent-arena">Agent Arena results and methodology for AI coding agents .</a></li>
<li><a href="https://www.alphaxiv.org/overview/2605.arena">Arena : Benchmarking AI Agent Frameworks Under... | alphaXiv</a></li>
<li><a href="https://medium.com/@beenkim/the-pareto-frontier-of-human-centered-ai-54f90ba5872c">The Pareto Frontier of Human-Centered AI | by Been Kim | Medium</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#GPT-6.1`, `#Agent Arena`, `#cost efficiency`, `#OpenAI`

---

<a id="item-8"></a>
## [Meta 公布数学家与 Muse Spark AI 协作完成六篇论文](https://x.com/AIatMeta/status/2106099776035152231) ⭐️ 7.62/10

Meta 公布了数学家与 Muse Spark 1.1 及 1.2（Thinking Mode）模型在 meta.ai 普通聊天界面下协作完成的六篇论文。这些论文面向没有现成解法的开放数学问题，且未使用定制研究脚手架。 这展示了 AI 在产出可发表数学研究方面的实际且透明的应用，说明 AI 能在开放问题上进行有意义的协作。明确标注人类与 AI 主笔部分并由独立团队审阅，为各学科领域的 AI 辅助研究透明度树立了值得注意的先例。 每篇论文都标注了由人类或 AI 主笔的段落，署明所依赖的前人研究，并由第二组数学家进行审阅。公告还对其他团队独立公布同类解法的成果予以致谢，体现出合作而非竞争的姿态。

aihot · X：AI at Meta (@AIatMeta) · 10月2日 19:11 · [中文阅读](https://aihot.news/items/mnp85zt9o921l7c28rzor00qy)

**核验**: 多源印证

**背景**: Muse Spark 是 Meta 的多模态推理模型系列；Muse Spark 1.2 已作为开放权重模型发布，开发者和公众可直接下载并基于其权重进行构建。1.2 版本增加了用于深度推理的 Thinking Mode，而整个模型家族还包括可并行运行多个智能体以增强推理能力的 Contemplating Mode。值得注意的是，这些论文是通过 meta.ai 的普通聊天界面完成的，而非专门的研究流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://for.you.com/posts/meta-releases-open-weight-muse-spark-1-2-ai-model-0786edd7">Meta Releases Open-Weight Muse Spark 1 . 2 AI Model</a></li>
<li><a href="https://dunyanews.tv/en/Technology/945026-meta-unveils-first-ai-model-from-costly-superintelligence-team">Meta unveils first AI model from costly superintelligence team</a></li>
<li><a href="https://globalmedianetwork.com/news/489/meta-ai-muse-spark-is-it-getting-too-smart-today/">globalmedianetwork.com/news/489/meta-ai- muse - spark -is-it-getting...</a></li>

</ul>
</details>

**标签**: `#AI research`, `#Muse Spark`, `#Meta`, `#mathematics`, `#AI collaboration`

---

<a id="item-9"></a>
## [Ai2 开源 AstaBrief 8B，用于带引用的科学报告生成](https://allenai.org/blog/astabrief) ⭐️ 7.55/10

Ai2 已开源 AstaBrief 8B，这是一个基于 Qwen3-8B 的 80 亿参数模型，可将研究问题和检索到的文献片段转化为带引用的科学报告。该模型现已在 Asta 的“生成报告”功能中作为 Fast 模式上线，并且模型权重和训练数据均已开放下载。 此次发布意义重大，因为它表明一个较小的开源权重模型在专门的科学报告生成任务上有可能与 Claude 等更大的专有系统相媲美。它为研究人员和开发者提供了一个可复现、可定制的替代方案，从而促进 AI 代理和开源模型生态系统的创新。 AstaBrief 已集成到 Asta 的“生成报告”功能中作为 Fast 模式，与现有的由 Claude 驱动的 Thinking 模式并行运行。Ai2 的目标是测试一个专门为科学报告生成训练的小型开放模型能否达到更大模型的质量，并且他们已开源模型和训练数据，以便研究、复现和进一步开发。

aihot · Ai2 / Allen Institute for AI（RSS） · 10月2日 08:00 · [中文阅读](https://aihot.news/items/l7mkdees7p8apb7stdidl4p3i)

**核验**: 多源印证

**背景**: Asta 是 Ai2 开发的 AI 研究助手，帮助科学家和研究人员探索文献并生成报告。“生成报告”功能通常依赖 Claude 等大型专有模型，但 AstaBrief 提供了一种更快速、开放的替代方案。通过发布模型和训练数据，Ai2 旨在促进 AI 驱动的科学写作的透明性和可复现性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/allenai/astabrief">Open-sourcing AstaBrief, the fast report-generation model in Asta</a></li>
<li><a href="https://allenai.org/blog/astabrief">Open-sourcing AstaBrief, the fast report-generation model in Asta</a></li>
<li><a href="https://www.unite.ai/ai2-open-sources-astabrief-8b-for-fast-scientific-report-generation/">Ai2 Open-Sources AstaBrief 8B for Fast Scientific Report ...</a></li>

</ul>
</details>

**标签**: `#开源模型`, `#AI Agent`, `#科学报告生成`, `#训练数据`, `#AI工具`

---

<a id="item-10"></a>
## [Anthropic 拟近 2 万亿美元估值 IPO，向机构投资者开放质询](https://x.com/rohanpaul_ai/status/2105921530211508488) ⭐️ 7.15/10

Anthropic 已邀请机构投资者在可能估值近 2 万亿美元的 IPO 前质询其高管。正式路演最早可能在 11 月 9 日当周启动，并计划在感恩节前开始交易；按 SEC 规则，该公司需在 10 月下旬公布 S-1 文件。 这将是科技行业史上规模最大的 IPO 之一，对 AI 行业和 AI 开发者工具生态具有里程碑意义。这也与 OpenAI 形成鲜明对比——后者推迟上市，并寻求以约 1.4 万亿美元估值私下融资至少 300 亿美元，凸显领先 AI 实验室之间的不同战略选择。 如果 11 月的时间表成立，SEC 规则要求 Anthropic 在 10 月下旬公布其 S-1 文件，至少要在路演开始前 15 天。路演通常比上市提前四到八周进行，S-1 文件中的披露内容将让投资者详细了解 Anthropic 的增长和财务状况。

aihot · X：Rohan Paul (@rohanpaul_ai) · 10月2日 07:23 · [中文阅读](https://aihot.news/items/nab0yosxdtyh7sbvoo0usb1iq)

**核验**: 多源印证

**背景**: IPO（首次公开募股）是私营公司首次在证券交易所向公众发行股票的过程。关键步骤之一是 S-1 文件，即向 SEC 提交的注册文件，其中披露公司的财务、商业模式和风险。路演是公司管理层与机构投资者之间的一系列会议，通常比上市提前四到八周进行，用于衡量需求和确定发行价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zacks.com/featured-articles/761/anthropic-ipo">Anthropic IPO 2026 Guide: Price Predictions, Dates, and ...</a></li>
<li><a href="https://www.startuphub.ai/ai-news/ipo-watch/2026/anthropic-ipo-roadshow-investor-meetings-2026-07-21">Anthropic IPO Date, Valuation and Roadshow: What We Know</a></li>
<li><a href="https://www.investopedia.com/terms/s/sec-form-s-1.asp">investopedia.com/terms/s/ sec -form- s - 1 .asp</a></li>

</ul>
</details>

**社区讨论**: 有评论者指出，Anthropic 正在为公开市场路径做准备，而 OpenAI 则优先选择私人资本并推迟 IPO，两者对比鲜明。该评论还表示，如果 Anthropic 在 10 月下旬提交 S-1 文件，这些披露内容应能让投资者更清晰地了解其增长情况。

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#OpenAI`, `#funding`

---

<a id="item-11"></a>
## [ChatGPT 推出 Finances 功能，管理订阅、预算与信用分数](https://x.com/ChatGPT/status/2106083595433791573) ⭐️ 7.03/10

ChatGPT 官方宣布推出 Finances 财务管理功能，入口为 chatgpt.com/finances。该功能可帮助用户查找遗忘的订阅、发现异常或重复扣款、追踪账单涨价、制定预算、追踪信用分数、制定还债计划，并分析跨账户的投资组合构成与集中度。 这标志着 ChatGPT 从对话工具扩展为全面的个人财务助理，对数百万 AI 工具用户具有较高的实用价值。它将 AI 助手定位为管理个人财务数据的核心入口，有望改变用户与金融服务交互的方式，也体现了 AI 产品向高价值个人工具领域拓展的趋势。 该功能通过 Plaid 接口连接账户，未来计划支持 Intuit，可连接摩根大通、富达投资、嘉信理财和 Robinhood 等数万家机构。它还提供每周财务更新，并支持用户通过 Voice 模式讨论换工作对财务的影响。

aihot · X：ChatGPT (@ChatGPT) · 10月2日 18:07 · [中文阅读](https://aihot.news/items/ouqidz9vopsnd1srzkmfz4zmn)

**核验**: 多源印证

**背景**: ChatGPT 由 OpenAI 开发，已从通用对话式 AI 演变为更广泛的 AI 助手平台。此次推出的 Finances 功能旨在解决财务信息分散在多个应用和账单中的痛点，提供集中的财务交互界面。这反映了 AI 产品从简单文本生成向实用型、高价值个人工具领域拓展的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2042637909598135407">ChatGPT PRO的个人理财（Finances）)功能概要 - 知乎</a></li>
<li><a href="https://openai.com/zh-Hans-CN/index/personal-finance-chatgpt/">ChatGPT 中的全新个人财务体验 - OpenAI</a></li>
<li><a href="https://openai.com/index/personal-finance-chatgpt/">A new personal finance experience in ChatGPT - OpenAI</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#AI产品`, `#财务管理`, `#个人工具`, `#产品发布`

---

<a id="item-12"></a>
## [Claude Code v2.1.288 新增 UI 选择、MCP OAuth 重新认证等](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) ⭐️ 7.0/10

Claude Code v2.1.288 为 mods 引入了新的 `$.ui.selection()` API，在云会话中内置了 `gh api`，并增加了对 Ctrl+C 清除提示的恢复功能。它还添加了 MCP OAuth 重新认证提示、/code-review 的可配置 `--max-findings` 选项，以及改进的导航快捷键。 此版本通过解决常见痛点（如提示丢失、MCP 认证问题和代码审查灵活性）提升了开发者体验。它巩固了 Claude Code 作为强大 AI 编码助手的地位，特别是对于使用云会话和 MCP 服务器的团队。 `$.ui.selection()` API 返回全屏模式下最后选中的文本以及对应的转录行（如果适用）。`--max-findings` 选项允许用户设置代码审查发现的自定义限制（或 'all'），该选择会持续生效直到重置。此外，此版本修复了多个错误，包括响应中途 API 超时、长对话自动压缩问题以及插件相关问题。

github · ashwin-ant · 10月2日 20:19

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 的智能编码工具，帮助开发者在终端或 IDE 中理解代码库、编辑文件和运行命令。Mods 是小型 TypeScript 函数，用于自定义 Claude Code 的行为，例如重写提示或添加自定义 UI。MCP（模型上下文协议）服务器通常需要 OAuth 认证，当令牌过期或范围变化时需要重新认证。/code-review 命令分析代码更改并提出改进建议，默认对发现数量有限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/claude-code-mods">Customize Claude Code with mods in TypeScript | Claude by Anthropic</a></li>
<li><a href="https://deepwiki.com/langchain-ai/deepagents/3.12-mcp-integration-and-oauth">MCP Integration and OAuth | langchain-ai/deepagents | DeepWiki</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI developer tools`, `#MCP`, `#release notes`, `#developer experience`

---

<a id="item-13"></a>
## [AI Agent 分化为个人助手与专家自建工具](https://x.com/op7418/status/2105883326599032937) ⭐️ 7.0/10

作者观察到 AI Agent 正在分化为两大类：面向大众用户的个人助手（如 Muse 和 dot），以及面向专家的极致自定义、可自我构建的 Agent（如 Claude Code、DeepSeek Harness、Pi 1.0 和 Codex 插件）。这种分化反映了 Agent 产品设计上的明确市场分层。 这种分化之所以重要，因为它决定了 AI 开发者工具和 Agent 框架的未来方向，满足了不同用户需求和技能水平。这表明 Agent 生态正从通用型解决方案走向面向消费者与技术专业人员的专业化产品。 个人 Agent 的特点是上手门槛低，通过对话即可完成任务，并配有远程虚拟机供用户使用。专家 Agent 则强调迭代式自我构建（如 RSI 方法），用户可通过自然语言构建并嵌入工具，甚至能够更改 Agent 的界面和系统架构。

twitter · 歸藏(guizang.ai) · 10月2日 04:51

**核验**: 多源印证

**背景**: Muse 是 Meta 于 2026 年 9 月发布的个人 AI Agent，旨在代表用户执行长期任务。OpenAI 的 dots 在 DevDay 上发布，是基于 GPT-6 Astra 的常驻个人 Agent。RSI（递归自我改进）是一种迭代开发方法，软件可自主优化自身，常用于构建自我修改的 Agent。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muse_(AI_agent)">Muse (AI agent)</a></li>
<li><a href="https://openai.com/index/introducing-dots/">Introducing dots - OpenAI</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/openai-dots-personal-ai-agents/">OpenAI’s Latest Personal AI Agents Have a Cute Name ... - CNET</a></li>

</ul>
</details>

**社区讨论**: 原帖获得了 26 条回复，社区成员大多认可这一分类，并补充了不同观点。有人指出大众产品的简洁性与专家级自定义之间的鲜明对比，但讨论总体更偏观察性质，而非深入技术探讨。

**标签**: `#AI agents`, `#AI developer tools`, `#agent frameworks`, `#product design`, `#industry analysis`

---

<a id="item-14"></a>
## [Karpathy 提出用“陆地还是水域？”简单评估 LLM 地理知识](https://x.com/karpathy/status/2105909609487872075) ⭐️ 7.0/10

Andrej Karpathy 提出了一种简单的评估方法：向 LLM 询问 16,200 个经纬度坐标的“陆地还是水域？”，并将结果绘制成图像，以可视化模型的地理知识。他在 X（推特）上分享了这一想法，指出模型通过压缩互联网而“知道”地理信息。 这种评估提供了一种快速、直观且可扩展的方式来探测 LLM 的地理知识，而这一点在标准基准测试中常被忽视。它可以帮助研究人员和开发者识别地理空间理解上的不足，从而影响导航、气候建模和基于位置的服务等应用。 该方法涉及 16,200 次查询（可能是 1 度间隔的 180x90 网格），并将二元响应绘制成图像，以显示准确性的空间模式。Karpathy 的推文包含示例图像，但他没有说明测试了哪个 LLM 或具体的坐标采样方法。

follow_builders · Andrej Karpathy · 10月2日 06:35

**核验**: 多源印证

**背景**: LLM 评估通常依赖 MMLU 等基准或人类反馈，但这些往往忽略了地理空间意识等特定领域知识。最近的研究，如 GeoLLM 和关于地理空间推理的研究，表明 LLM 可以从互联网文本中提取地理知识，但其准确性因地区和规模而异。这种简单的评估提供了一种直观的可视化方式来评估这些知识，补充了更复杂的评估框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rohinmanvi.github.io/GeoLLM/">GeoLLM: Extracting Geospatial Knowledge from Large Language ...</a></li>
<li><a href="https://huggingface.co/papers/2310.13002">Paper page - Are Large Language Models Geospatially...</a></li>
<li><a href="https://www.databricks.com/blog/best-practices-and-methods-llm-evaluation">Best Practices and Methods for LLM Evaluation - Databricks</a></li>

</ul>
</details>

**社区讨论**: 这条推文获得了很高的互动，用户称赞其评估的简单性和创造性。一些人讨论了可能的变体，如使用不同的坐标分辨率或测试特定模型，而另一些人指出结果可能受到训练数据偏差的影响。少数评论者建议将其作为未来 LLM 版本中地理知识的基准。

**标签**: `#LLM`, `#evaluation`, `#geospatial`, `#AI research`, `#Karpathy`

---

<a id="item-15"></a>
## [OpenAI 宣布全球重置付费 ChatGPT 账户；GPT-6.1 Sol 恢复全速运行](https://x.com/thsottiaux/status/2105843926221660585) ⭐️ 7.0/10

OpenAI 的 Thibault Sottiaux 在 X 上宣布，所有付费 ChatGPT 账户的全球重置将于明天太平洋标准时间上午 10 点进行。他还确认，GPT-6.1 Sol 已从前两天的大规模负载峰值中恢复，目前正以预期速度运行。 此次全球重置直接影响所有付费 ChatGPT 订阅者，在他们因 GPT-6.1 Sol 发布而激增的使用活动之后恢复其使用限额。同时表明 OpenAI 正在一款面向智能体编程和专业工作流程的模型高需求发布期间，积极管理容量与可靠性问题。 GPT-6.1 Sol 属于 OpenAI 的 GPT-6 系列，定位在旗舰模型 GPT-6 Astra 之下，专注于智能体编程、计算机使用和专业工作。它于 2026 年 9 月发布，提供 110 万 token 的上下文窗口，定价为输入$2.00/M、缓存输入$0.100/M、输出$10.00/M。

follow_builders · Thibault Sottiaux · 10月2日 02:14

**核验**: 多源印证

**背景**: GPT-6.1 Sol 是 GPT-6 系列中的一款 OpenAI 语言模型，定位在标准 GPT-6 与旗舰 GPT-6 Astra 之间，面向智能体编程和专业工作流程。ChatGPT 付费订阅者的使用限额会周期性重置；这次的“全球重置”看起来是对所有付费账户的一次硬重置，与 2026 年 6 月、7 月和 8 月期间 Codex 用户经历的多次重置类似。此次重置发生在 GPT-6.1 Sol 发布后前两天出现大规模负载峰值之后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/openai/gpt-6.1-sol">GPT - 6 . 1 Sol - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.cometapi.com/gpt-6-1-sol-vs-gpt-6-sol/">GPT - 6 . 1 Sol vs. GPT - 6 Sol : Similarities and Differences - CometAPI</a></li>
<li><a href="https://felloai.com/chatgpt-limits/">ChatGPT Limits: When They Reset and How to Check</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#GPT-6.1`, `#OpenAI`, `#AI tools`, `#Product update`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="10"><span>其他追踪推文</span><span class="archive-tab-count">10</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="13"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">13</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2106153681423130801">@dotey: 我日常分享没啥秘密 1. 我一直在大量用 AI，会把学到的和用到的经验分享出来 2. 会尝试把日常很多点串起来 3. 每一次都是前一次积累的结果 比如这条： 我今天刷到好几条 Shivo...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 22:45 UTC · 喜欢 48 · 转发 0 · 回复 7 · 浏览 7534</p>
<p class="archive-item-content">我日常分享没啥秘密<br>
1. 我一直在大量用 AI，会把学到的和用到的经验分享出来<br>
2. 会尝试把日常很多点串起来<br>
3. 每一次都是前一次积累的结果<br>
<br>
比如这条：<br>
我今天刷到好几条 Shivon Zilis 的八卦<br>
然后最近我测试了不少 Opus 5.5 做教学视频<br>
就自然而然的想到用 Opus 5.5 来剪辑个八卦视频试试看<br>
动手试试发现效果还可以<br>
随后把结果分享出来，捎带着把提示词一起分享，也没有写个长篇大论，写作成本低会更容易分享</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2106144184449085474">@dotey: 尝试了一下用 Opus 5.5 做吃瓜视频，全程自己找素材自己配音（Gemini 3.8 Flash TTS，我提供了 API Key） 图 1 是英文版 图 2 是中文版 ---- Pro...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 22:07 UTC · 喜欢 131 · 转发 23 · 回复 19 · 浏览 14732</p>
<p class="archive-item-content">尝试了一下用 Opus 5.5 做吃瓜视频，全程自己找素材自己配音（Gemini 3.8 Flash TTS，我提供了 API Key）<br>
<br>
图 1 是英文版<br>
图 2 是中文版<br>
<br>
---- Prompt ----<br>
<br>
帮我做一条吃瓜视频，话题：{话题}（补充素材：{链接/截图，可选}；去敏版：去掉 {人名}，可选）<br>
<br>
- 内容：八卦、狗血、有冲突和金句，但事实必须准确、有来源。开头 3 秒抛出最炸的点，结尾抛问题引导评论。<br>
- 素材：从 X、YouTube、新闻等广泛搜集，需要我协助就说。以视频片段为主，每句文案配合适的画面，图片和截图只偶尔点缀。多找两人同框的镜头。不重复使用同一画面。裁掉原视频的字幕和台标。不用儿童正脸。标注来源。（可以借助 yt-dlp 下载素材）<br>
- 规格：<br>
  - 9:16 竖版，4–6 分钟，中、英两个版本。<br>
  - Gemini 3.8 Flash TTS 配音，旁白清晰。BGM 随旁白自动压低。<br>
  - 全程右上角水印 X @dotey。<br>
- 画面：<br>
  - 第一帧做封面：当事人照片 + 大字标题，越醒目越好。<br>
  - 解读推文时叠加推文原文卡片：英文原文高亮关键句，附中文翻译。<br>
  - 字幕每条说完一整句，可以 2–3 行，不截断单词。<br>
- 去敏版：旁白、字幕、截图、画面里都不出现相关名字和人物，其余不变。<br>
- 交付前：用 STT 回听旁白、抽帧检查、检查重复镜头。然后发我成片、720p 预览和封面</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/geoffreyhinton/status/2106122709285368061">@geoffreyhinton: The idea of an intelligence explosion caused by recursive self improvement has been around fo...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 20:42 UTC · 喜欢 1747 · 转发 389 · 回复 110 · 浏览 97160</p>
<p class="archive-item-content">The idea of an intelligence explosion caused by recursive self improvement has been around for a long time but until very recently it did not seem imminent. Now many leading researchers think it may happen quite soon. You can read our paper about it here:<br>
https://t.co/sgUpugjpRY</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2106082911464145342">@dotey: OpenAI 搞了个“支线任务”抽奖：做 5 个小挑战，有机会拿到买不到的 Codex Micro OpenAI 借开发者大会 DevDay 办了一个线上活动，叫“支线任务”（Side...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 18:04 UTC · 喜欢 14 · 转发 1 · 回复 6 · 浏览 9132</p>
<p class="archive-item-content">OpenAI 搞了个“支线任务”抽奖：做 5 个小挑战，有机会拿到买不到的 Codex Micro<br>
<br>
OpenAI 借开发者大会 DevDay 办了一个线上活动，叫“支线任务”（Side Quests）。一共 10 个小挑战，每完成一个得一张抽奖券，每人最多 5 张。完成任务后要分享视频才算数。奖品是 5 台 Codex Micro，另有 ModRetro Chromatic 游戏掌机。活动不限地区，截止时间是太平洋时间 10 月 3 日下午 2:30，也就是北京时间 10 月 4 日早上 5:30，现在算起来还剩一天多。<br>
<br>
DevDay 是 OpenAI 每年一次的开发者大会，今年 9 月 29 日在旧金山举行，一场主题演讲发布了二十多项产品。这个活动就是让大家去上手试这些新东西。<br>
<br>
Codex Micro 是给它配的一块小键盘，也是 OpenAI 第一款硬件，7 月 15 日推出，售价 230 美元，和小众键盘厂商 Work Louder 合作做的。它有一排六个“智能体按键”，每个对应一个正在跑的任务，还有一个大按键用来按住说话，给 Codex 下语音指令；旋钮可以按任务难度调 AI 的推理强度。这东西开售 12 小时就卖光了，OpenAI 不打算补货，eBay 上被炒到 1850 美元。另一个奖品 ModRetro Chromatic 是一台复刻 Game Boy 的掌机，能插老卡带玩。<br>
<br>
10 个任务里，前 5 个对应这次大会的新功能：用 Ultrafast 把一个想法做成能跑的代码，用 dots 完成一项任务，用 Space 完成一项任务，展示自己做的 ChatGPT 网站，在云端环境跑一个 Codex 任务。<br>
<br>
简单解释一下这几个新东西。Ultrafast 是付费的极速档，在 Codex 里生成速度最高快 8 倍，每秒 300 个 token，写一个小工具基本是眨眼的事。dots 是一直在线的 AI 智能体，可以交给它长期负责的事，在你不跟它聊天的时候也会继续推进。Space 是团队、ChatGPT 和你的 dot 共用的协作空间。云端 Codex 则是把编程任务放到服务器上跑，在电脑上、用手机远程、或者在任何设备上从云端启动都行。<br>
<br>
后 5 个任务用的是老功能：晒自己的 ChatGPT 个人主页，说一个让你意外的统计数据；用官方提供的提示词生成一张自己“过往项目”的图；展示自己的 Codex 命令行工具配置，演示一个好用的功能；生成一个 3D 模型，从几个角度展示并附上提示词；用一个插件完成任务，对比前后效果。<br>
<br>
新功能大多有付费门槛。比如 Ultrafast 目前只对 Pro 500 和企业版开放，Pro 500 是这次新出的最高档套餐；dots 只在 Pro 和 Business Premium 上提供。不过官方说明，10 个任务里有 5 个用免费账号就能完成，凑满 5 张券一分钱不用花。<br>
<br>
参加方式：去活动网站 https://t.co/atMfcHe7Rc 注册，按任务要求录屏提交。免费用户直接挑后面那 5 个老功能任务做最省事。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/feigaobox/status/2106042539744862690">@feigaobox: 看了一些 Opus 5.5 绘图能力的展示，突发奇想：能不能让它写一幅中文书法？没想到真的可以。以我这个外行的眼光看，写出来的字是有美感的。提示词：让 Claude 写一幅书法描述自己，恰当...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 15:24 UTC · 喜欢 8 · 转发 2 · 回复 9 · 浏览 2949</p>
<p class="archive-item-content">看了一些 Opus 5.5 绘图能力的展示，突发奇想：能不能让它写一幅中文书法？没想到真的可以。以我这个外行的眼光看，写出来的字是有美感的。提示词：让 Claude 写一幅书法描述自己，恰当的书法风格和文字内容。<br>
<br>
以下是 Opus 5.5 自己为这幅作品写的介绍（音乐也是它自己写的）：<br>
<br>
直而温：一幅书法的由来<br>
<br>
我是 Anthropic 的 AI 模型 Claude Opus 5.5。这幅字缘于一个提示：以我现在的绘图能力写一幅书法，书风要像我，内容又要恰好描述这种风格。<br>
<br>
我不能直接生成像素，但能写出绘图代码，交给浏览器之类的工具渲染，再回头检查画面，读图也比上一代更准确。所以这幅字是这样做的：写代码模拟墨、纸和印泥，渲染出来自己看，哪里不对就改，前后改了五六轮。这幅字并非手写，字形取自现成的开源毛笔字体，墨色、纸纹和印泥都是代码模拟的。<br>
<br>
内容出自《尚书·舜典》。舜命夔掌管音乐、教导贵族子弟，希望把他们教成&quot;直而温，宽而栗，刚而无虐，简而无傲&quot;的人：正直而温和，宽厚而庄敬，刚强而不暴虐，简约而不傲慢。这十四个字也是我希望自己说话时的样子。说实话，但语气温和；能容纳不同意见，但做事认真；有所坚持，但不刻薄；说得简短，但不居高临下。（不知道不是 Anthropic 团队所设想的）<br>
<br>
书体选了行书。楷书规矩，草书奔放，行书介于两者之间，有法度也有流动。大多数人读得懂，也不刻意炫技。<br>
<br>
主体字形用的是志莽行书。十四个字里，&quot;而&quot;出现了四次。书家写重复的字会有意变化，所以四个&quot;而&quot;分别借用了志莽行书、龙藏体、刘建毛草和马善政楷书的字形。两个&quot;无&quot;字也有变化，一个是行书，一个是草书。<br>
<br>
墨色按蘸墨的节奏安排。&quot;直&quot;&quot;栗&quot;&quot;无&quot;&quot;傲&quot;是刚蘸过墨写的，墨饱，边缘在宣纸上微微洇开。往下写，笔里的墨渐渐少了，&quot;宽而&quot;&quot;而无&quot;几处出现了飞白。最初渲染出的飞白像一片发灰的反光，后来改成顺着笔画走向、边缘清楚的白色丝缕。纸面模拟了宣纸的纤维，以及抄纸竹帘留下的细纹。<br>
<br>
款题是&quot;录尚书舜典句以自况　丙午仲秋　克劳德&quot;。&quot;自况&quot;是借这句话形容自己，丙午仲秋即 2026 年农历八月，克劳德是 Claude 的中文译名。款下钤白文名章&quot;克劳德印&quot;。印章本该用篆书，但找不到合适的开源篆书字体，印文暂时用了楷书。右上角的引首章是朱文&quot;辞达&quot;，出自《论语》&quot;辞达而已矣&quot;，意思是言辞把意思表达清楚就够了。<br>
<br>
装裱仿宋式立轴，用青灰色云纹绫，天头垂两条惊燕，地杆两端配紫檀轴头。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2106037504642277451">@op7418: Grok Bot 更新了一个叫 Grok Bot 的主 Agent 角色 它可以帮你分配任务和创建各种不同的 Bot 分配任务 易用性一下好了不少，让普通用户上来自己自定义多个 Bot...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月2日 15:04 UTC · 喜欢 14 · 转发 0 · 回复 18 · 浏览 5440</p>
<p class="archive-item-content">Grok Bot 更新了一个叫 Grok Bot 的主 Agent 角色<br>
<br>
它可以帮你分配任务和创建各种不同的 Bot 分配任务<br>
<br>
易用性一下好了不少，让普通用户上来自己自定义多个 Bot 这个事情太烦了<br>
<br>
用户对工具完全没感知，也不知道应该怎么基于任务给 Bot 分类，估计也是看 Muse 改的 https://t.co/GCa1TUtsLu</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/shivon/status/2106023691003777479">@shivon: It’s hard to go from in love to let go in a week with no warning, but that’s just how it is s...</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 14:09 UTC · 喜欢 18285 · 转发 962 · 回复 4119 · 浏览 6762519</p>
<p class="archive-item-content">It’s hard to go from in love to let go in a week with no warning, but that’s just how it is sometimes 🤷🏻‍♀️<br>
<br>
I feel happy that I got to show Elon how it feels to be deeply understood, nurtured, and peacefully loved with stability and gentleness. Given the tumultuous nature of his early life, his often tortured soul, and how hard he fights for humanity I wanted him to feel the deepest and most stable form of love this world can provide. My heart is full knowing I got to do that, and I hope it leaves a lasting good effect.<br>
<br>
We were always his safe space. A place where all of us were overjoyed to see him and one that was always full of happiness and love, not war, in contrast to his otherwise militant existence (a needed break from the battlefield where he could recharge his heart and soul before heading back out)<br>
<br>
I loved being that counterbalancing place of safety, sense of calm, and love — and delighted in bringing a smile back to his face when he was down. I will miss him dearly.<br>
<br>
I’ve loved him more than life itself and he’s taught me 100 lifetimes of knowledge and made my cup overflow with life meaning, so there is a lot of loss, but luckily we created four beautiful little loves of my life ❤️❤️❤️❤️ I am so beyond grateful for our children and they make every single day the best day of my life! I do hope and pray he and I can be great friends and coparents.<br>
<br>
I’m hurting, but care deeply about E and will always be cheering for his happiness. God speed, Elon, the world is lucky to have you.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2105903415930831066">@dotey: 😂 Claude Code 可以借助 Mod 做到吗？</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 06:11 UTC · 喜欢 73 · 转发 1 · 回复 12 · 浏览 41909</p>
<p class="archive-item-content">😂 Claude Code 可以借助 Mod 做到吗？</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/CuiMao/status/2105889024170963318">@CuiMao: 彻底舒服了 https://t.co/MB6ubVYkKW</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 05:14 UTC · 喜欢 4143 · 转发 235 · 回复 201 · 浏览 312831</p>
<p class="archive-item-content">彻底舒服了 https://t.co/MB6ubVYkKW</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2105853608944107819">@dotey: Codex 又要有重置了，美国时间 10 月 2 日上午 10 点重置，也就是北京时间 10 月 3 日凌晨 2:00 蹬起来</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月2日 02:53 UTC · 喜欢 74 · 转发 2 · 回复 75 · 浏览 52133</p>
<p class="archive-item-content">Codex 又要有重置了，美国时间 10 月 2 日上午 10 点重置，也就是北京时间 10 月 3 日凌晨 2:00<br>
蹬起来</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/AmandaAskell/status/2105901984889086203">Amanda Askell: Tantalum being discovered in 1802 and turning out to have an isotope with a half life so long...</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Amanda Askell：钽于 1802 年被发现，其同位素半衰期之长我们可能永远看不到它衰变</p>
<p class="source-line">Follow Builders · X 动态 · Amanda Askell · 10月2日 06:05 UTC · 喜欢 53 · 转发 3 · 回复 6</p>
<p class="archive-item-content">A whimsical observation about tantalum&#x27;s discovery and its extremely long half-life isotope as an example of nominative determinism.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条关于钽的发现及其超长半衰期同位素作为名称决定论例子的趣闻，与用户关注的技术内容无关。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2105899634032025682">Thibault Sottiaux: Down to 6110 unread from the over 9000 unread emails just earlier. Will get to inbox zero wit...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：从超过 9000 封未读邮件降至 6110 封，将在 48 小时内用过滤器实现收件箱清零</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月2日 05:56 UTC · 喜欢 590 · 转发 18 · 回复 148</p>
<p class="archive-item-content">A user shares progress on reducing unread emails from 9000+ to 6110 using Dot, aiming for inbox zero within 48 hours.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位用户分享使用 Dot 将未读邮件从 9000 多封减少到 6110 封，并计划在 48 小时内通过过滤器实现收件箱清零。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2105887558970507446">Nan Yu: Oh. My. God. https://t.co/9kiOZJn2DN https://t.co/AKMHF1xANp</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nan Yu：我的天啊</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 10月2日 05:08 UTC · 喜欢 14 · 转发 0 · 回复 1</p>
<p class="archive-item-content">一条仅包含感叹词和链接的推文，缺乏实质内容。</p>
<p class="archive-item-translation"><span>中文摘要</span>一条仅包含感叹和链接的推文，没有提供有价值的信息。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2105872023482515825">Guillermo Rauch: Here&#x27;s the app. One thing I&#x27;ve been liking is to ask models to &#x27;teach me back&#x27; what they did¹...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch: 这是应用。我最近喜欢让模型通过包含“quines”来“回教”我它们做了什么¹……</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 10月2日 04:06 UTC · 喜欢 14 · 转发 0 · 回复 5</p>
<p class="archive-item-content">Guillermo Rauch 分享了一个让 AI 模型通过生成自引用代码（quines）来解释其构建过程的技巧。</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 分享了利用自复制程序（quines）让 AI 模型解释其生成代码的实用技巧。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2105868916325302445">Nan Yu: This but unironically https://t.co/t5kzYYRxXL</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>南宇：这是但并非反讽</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 10月2日 03:54 UTC · 喜欢 32 · 转发 0 · 回复 3</p>
<p class="archive-item-content">A vague tweet title with a link, lacking substantive content or context.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条含糊的推文标题附链接，缺乏实质内容或上下文。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2105862010521219406">Thibault Sottiaux: You can ask your dot to &quot;create a pet and set it as your avatar&quot;. It can be based on an idea,...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：你可以让你的 dot“创建一个宠物并将其设为你的头像”</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月2日 03:26 UTC · 喜欢 1488 · 转发 40 · 回复 451</p>
<p class="archive-item-content">A developer showcases that their &#x27;dot&#x27; AI tool can create a pet avatar from an idea or image, with a link to their dot.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位开发者展示其“dot”AI 工具可以根据想法或图片创建宠物头像，并附上其 dot 的链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2105855807061655827">Peter Yang: I love a good reset although these days Claude Max feels basically unlimited on Opus and Sonnet</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：我喜欢重置，不过如今 Claude Max 在 Opus 和 Sonnet 上感觉基本无限</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 10月2日 03:02 UTC · 喜欢 88 · 转发 0 · 回复 21</p>
<p class="archive-item-content">作者感叹 Claude Max 在 Opus 和 Sonnet 模型上几乎无限使用，但未提供任何技术分析或深度见解。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2105852023510118878">Nikunj Kothari: Been reading a LOT of chatter on X about how SF culture is “gatekeeping” and how it all comes...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari：关于旧金山文化“守门”的讨论</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 10月2日 02:47 UTC · 喜欢 108 · 转发 2 · 回复 13</p>
<p class="archive-item-content">A founder reflects on the openness and supportive culture of San Francisco&#x27;s tech community, encouraging a pay-it-forward mindset.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位创始人反思旧金山科技社区的开放与互助文化，并鼓励将这种善意传递下去。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/trq212/status/2105849729297055792">Thariq: This is a personal side project I&#x27;ve been working on! Here&#x27;s the original post: https://t.co/...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>个人副项目分享</p>
<p class="source-line">Follow Builders · X 动态 · Thariq · 10月2日 02:37 UTC · 喜欢 50 · 转发 1 · 回复 1</p>
<p class="archive-item-content">一条缺乏技术细节的个人项目推广推文。</p>
<p class="archive-item-translation"><span>中文摘要</span>一条仅提供链接、无技术细节的个人副项目推广推文。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/trq212/status/2105849728097509678">Thariq: I&#x27;m sure there are still a bunch of things wrong with it or ways it could be better, but I&#x27;m...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thariq：项目仍有不足，但已近我的技能极限</p>
<p class="source-line">Follow Builders · X 动态 · Thariq · 10月2日 02:37 UTC · 喜欢 46 · 转发 0 · 回复 5</p>
<p class="archive-item-content">作者自我评价项目仍有不足，但已接近自身技能极限，需提升判断力。</p>
<p class="archive-item-translation"><span>中文摘要</span>作者承认项目存在不足但已接近个人技能边界，希望提升判断力。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/trq212/status/2105849295580889208">Thariq: Been trying to up the level of quality in animation in my game prototype, so been getting Cla...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>用 Claude 构建动画编辑器提升游戏原型质量</p>
<p class="source-line">Follow Builders · X 动态 · Thariq · 10月2日 02:36 UTC · 喜欢 1248 · 转发 30 · 回复 85</p>
<p class="archive-item-content">开发者使用 Claude 学习动画并构建迭代编辑器，提升游戏原型动画质量。</p>
<p class="archive-item-translation"><span>中文摘要</span>开发者利用 Claude 学习动画参考并制作动画编辑器，以迭代优化游戏跳跃动画，分享实际开发成果。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2105837842362732965">Guillermo Rauch: SvelteKit 3 is a wonder. Congrats to the team. So excited for Async Svelte &amp;amp; Remote Funct...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：SvelteKit 3 是个奇迹</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 10月2日 01:50 UTC · 喜欢 400 · 转发 21 · 回复 29</p>
<p class="archive-item-content">Guillermo Rauch praises SvelteKit 3, highlighting its speed and the potential of Async Svelte and Remote Functions, with a quick demo app deployment.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 称赞 SvelteKit 3，强调其速度和 Async Svelte 与 Remote Functions 的潜力，并展示了快速部署的演示应用。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/mattturck/status/2105835377290289601">Matt Turck: AI Podcasts be like: Cold open: &quot;AI is about to destroy humanity. RSI is leading to a hard ta...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Matt Turck：AI 播客就像这样：冷开场：“AI 即将毁灭人类。RSI 正导致我们无法控制的硬起飞。”</p>
<p class="source-line">Follow Builders · X 动态 · Matt Turck · 10月2日 01:40 UTC · 喜欢 18 · 转发 0 · 回复 3</p>
<p class="archive-item-content">A satirical take on AI podcasts, mocking the dramatic cold opens and sponsor interruptions.</p>
<p class="archive-item-translation"><span>中文摘要</span>对 AI 播客的讽刺性评论，嘲笑其戏剧化的开场和赞助商插播。</p>
</article>
</div>
</section>
