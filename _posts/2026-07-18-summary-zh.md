---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 66 条内容中筛选出 11 条重要资讯。

---

1. [月之暗面开源替代 Transformer 三大基础组件](#item-1) ⭐️ 9.3/10
2. [Schema 框架在 ARC-AGI-3 公开集上取得约 99% 成绩](#item-2) ⭐️ 8.7/10
3. [Kimi K3 登顶前端编码榜，开放权重挑战闭源巨头](#item-3) ⭐️ 8.65/10
4. [Claude Fable 5 在 CursorBench 创下 72.9% 新高](#item-4) ⭐️ 8.35/10
5. [Kimi K3 与鹈鹕基准测试：分词异常与智能体需求](#item-5) ⭐️ 8.0/10
6. [Boris Cherny 谈 Claude Code 自主工作流](#item-6) ⭐️ 8.0/10
7. [美团 LongCat 发布 LoHoSearch，更难搜索智能体基准](#item-7) ⭐️ 7.88/10
8. [NVIDIA Nemotron 3 Embed 8B 登顶 RTEB 基准](#item-8) ⭐️ 7.75/10
9. [OpenAI 提出'有用智能每美元'指标](#item-9) ⭐️ 7.6/10
10. [乡村教育一等奖作品'智绘科普'技术拆解](#item-10) ⭐️ 7.1/10
11. [Simon Willison 推出 LLM 陈词滥调高亮工具](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [月之暗面开源替代 Transformer 三大基础组件](https://x.com/dotey/status/2078172517085085951) ⭐️ 9.3/10

在 GTC 2026 上，月之暗面杨植麟介绍了三个开源替代方案：MuonClip 优化器替代 Adam、QK-Clip 稳定注意力层、Attention Residue 替代残差连接。演讲还详细介绍了 Kimi Linear 长上下文注意力、Agent Swarm 多智能体协作，以及通过视觉训练提升文本推理能力的早期融合方法。 这些创新解决了 AI 训练中的关键扩展挑战，如数据稀缺和万亿参数规模下的注意力不稳定。通过开源这些组件，月之暗面使更广泛的研究社区能够提升数据效率和模型性能，可能加速开源模型向闭源前沿水平逼近。 MuonClip 基于 Muon 优化器，通过正交化参数更新使数据效率接近翻倍，但需要 QK-Clip 防止大规模下注意力 logit 爆炸。Attention Residue 允许每层关注所有前序层的输出，用学习到的注意力机制替代标准残差连接。

twitter · 宝玉 · 7月17日 17:38 · [中文阅读](https://aihot.virxact.com/items/cmrp8wsr10bhobitotnd5hzeq) · 2 个来源

**核验**: 多源印证

**背景**: Transformer 架构依赖于 2014-2017 年间引入的三个基础组件：Adam 优化器、注意力机制和残差连接。Adam 为每个参数自适应学习率，注意力机制让模型能加权输入的不同部分，残差连接通过提供梯度捷径使深层网络训练成为可能。月之暗面的替代方案旨在通过提高数据效率、稳定极端规模下的训练以及允许更灵活的跨层信息流来改进这些组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tianshijing.github.io/ScalingOpt/pages/blogs/Jianlin/QK-Clip：让Muon在Scaleup之路上更进一步.html">QK-Clip: Advancing Muon Further in Scale-up | Scientific Spaces</a></li>
<li><a href="https://github.com/AkulDatta/muonclip">GitHub - AkulDatta/muonclip: Implementation of the MuonClip ...</a></li>

</ul>
</details>

**标签**: `#AI Training`, `#Open Source`, `#Transformer Architecture`, `#Optimizer`, `#Moonshot AI`

---

<a id="item-2"></a>
## [Schema 框架在 ARC-AGI-3 公开集上取得约 99% 成绩](https://schema-harness.github.io/) ⭐️ 8.7/10

Schema Harness 是一种将观测转化为可编辑程序的新框架，它使用 Claude Opus 4.8 和 Fable 5 在 ARC-AGI-3 公开基准上取得了约 99% 的相对人类行动效率（RHAE），使用 GPT-5.6 Sol 取得了 95.35%，且无需修改任何模型权重。 这一结果代表了 ARC-AGI-3 上的重大突破，该基准对前沿模型来说异常困难，它表明改进模型周围的推理过程可以在不扩大模型规模或修改权重的情况下获得近乎完美的分数。 该框架通过将观测视为原始数据并转化为可执行程序，联合解决了状态归因和机制发现问题，并采用回退规则：得分低于 80% 的游戏会使用其他模型重新运行。这两项得分均为自行报告，尚未经过 ARC Prize 验证。

aihot · Hacker News 热门（buzzing.cc 中文翻译） · 7月17日 08:41 · [中文阅读](https://aihot.virxact.com/items/cmropqooe05tqbitodvnqnc6u)

**核验**: 多源印证

**背景**: ARC-AGI-3 是一个交互式基准测试，智能体必须从头开始学习玩新颖的游戏，每一步只接收一个 64×64 的颜色索引网格和一组合法动作，没有明确的规则或目标。它使用相对人类行动效率（RHAE）来衡量性能，该指标将智能体每关的行动次数与人类基线进行比较。在 Schema 之前，半私有集上经过验证的最佳前沿模型得分仅为 7.78%（GPT-5.6 Sol）。Schema 采用“物理学家”方法：首先将原始观测归因于对象和变量（状态归因），然后发现动作如何改变该状态，并将规则编写为可执行程序（机制发现）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://daily.dev/posts/frontier-models-with-our-harness-achieve-99-on-arc-agi-3-public-schema-dqa4is0zk">Frontier Models with Our Harness Achieve ~99% on...</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence Announcing ARC-AGI-3 - ARC Prize ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence ARC-AGI-3: The New Interactive Reasoning Benchmark ARC-AGI-3: Interactive AGI Benchmark - emergentmind.com ARC-AGI-3 Leaderboard & Scores — July 2026 | BenchLM.ai</a></li>

</ul>
</details>

**标签**: `#ARC-AGI`, `#AI agents`, `#program synthesis`, `#Claude Opus`, `#GPT-5.6`

---

<a id="item-3"></a>
## [Kimi K3 登顶前端编码榜，开放权重挑战闭源巨头](https://x.com/AYi_AInotes/status/2077981025905316253) ⭐️ 8.65/10

Kimi K3 是一款 2.8 万亿参数的混合专家模型，拥有百万上下文窗口，在 Frontend Code Arena 中以 1679 分登顶，超越了 Claude Fable 5 和 GPT-5.6 Sol。月之暗面宣布将于 2026 年 7 月 27 日开放模型权重，使其成为首个在该基准测试中领先的开放权重模型。 这标志着 AI 编码领域的重大转变，一家中国公司的开放权重模型超越了 Anthropic 和 OpenAI 的最佳闭源模型。这表明开源方法可以在最高水平上竞争，可能加速 AI 辅助前端开发和智能体编码工具的创新。 该模型采用 2.8 万亿参数 MoE 架构和百万上下文窗口，API 定价为每百万输入 tokens 15 美元，定位对标高端闭源模型而非价格竞争。Kimi K3 在 7 个前端细分赛道中拿下 6 个第一，仅在游戏赛道暂居第二。

aihot · X：阿易 AI Notes (@AYi_AInotes) · 7月17日 04:57 · [中文阅读](https://aihot.virxact.com/items/cmroipdr803rvbito8t018vr1)

**核验**: 多源印证

**背景**: Frontend Code Arena 是一个评估 AI 模型在真实用户前端编码任务（包括 HTML 和 React 开发）上的基准测试，采用全球开发者匿名盲测来评估代码质量和交互体验。Claude Fable 5 和 GPT-5.6 Sol 分别是 Anthropic 和 OpenAI 的最新旗舰模型，均为闭源，被认为是编码领域的顶尖水平。Kimi K3 由月之暗面（Moonshot AI）开发，这家中国 AI 公司以 Kimi 聊天机器人闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/arena/status/2056803664606679059">Arena.ai on X: "Code Arena: Frontend evaluates models on agentic frontend coding tasks from real users building apps and websites (HTML and React). Agents are an entirely different contest. More from Arena soon. Filter and dive into all the Code Arena: Frontend leaderboard details at:" / X</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#AI developer tools`, `#open-source AI`, `#coding benchmark`, `#Kimi K3`

---

<a id="item-4"></a>
## [Claude Fable 5 在 CursorBench 创下 72.9% 新高](https://claude.com/blog/working-at-the-frontier-cursor) ⭐️ 8.35/10

Anthropic 的新模型 Claude Fable 5 在 Cursor 的内部基准 CursorBench 上取得了 72.9% 的分数，创下新高。该模型在模糊的真实编程任务中表现出色，例如仅凭一句提示就自主规划并成功登月。 这一成就标志着 AI 智能体在自主编程和推理能力上的重大飞跃。它表明 AI 模型能够更好地处理复杂且定义模糊的工程任务，无需人类持续指导，这将极大提升开发者的生产力。 评估使用了 Cursor 的 Max effort 模式，该模式允许模型使用更多 token 进行推理。Claude Fable 5 以更少的操作和 token 消耗取得了这一分数，并且能够从极简提示中推断意图，甚至挑战用户的假设。

aihot · Claude：Blog（网页） · 7月17日 16:32 · [中文阅读](https://aihot.virxact.com/items/cmrp5pfjw0af6bitoudv35oqk)

**核验**: 多源印证

**背景**: CursorBench 是 Cursor（一个 AI 编程智能体平台）开发的基准测试，用于评估模型在源自真实用户会话的模糊、多文件编程任务上的表现。与传统基准不同，CursorBench 测试模型在没有明确指令的情况下推断意图、查找根本原因和验证修复的能力。Claude Fable 5 是 Anthropic 的 Mythos 系列的一部分，专为高级推理和编程任务设计，而 Max effort 模式是一种控制模型用于推理的 token 数量的设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/cursorbench">Cursor · CursorBench</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/effort">Effort - Claude Platform Docs</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Claude`, `#benchmark`, `#developer tools`, `#autonomous coding`

---

<a id="item-5"></a>
## [Kimi K3 与鹈鹕基准测试：分词异常与智能体需求](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 8.0/10

Simon Willison 使用鹈鹕基准测试分析 Kimi K3 模型时发现了分词异常：简单提示词被计为 95 个 token，而其他模型仅需 10 个，暗示可能存在隐藏的系统提示。社区同时呼吁开发更好的智能体工具调用基准测试。 这些发现揭示了潜在的隐藏提示和分词不一致性，影响模型评估和透明度。讨论强调了开发智能体基准测试以评估实际工具使用能力的重要性。 Kimi K3 拥有 2.8 万亿参数和 100 万 token 的上下文窗口，但其分词器将‘生成一只骑自行车的鹈鹕的 SVG’计为 95 个 token，而其他模型仅需 10 个。这表明存在一个 85 token 的隐藏系统提示，可能用于推理努力控制。

hackernews · droidjj · 7月17日 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48947717)

**核验**: 多源印证

**背景**: 鹈鹕基准测试由 Simon Willison 于 2024 年创建，是一个非正式测试，要求大语言模型‘生成一只骑自行车的鹈鹕的 SVG’。它已成为比较模型指令遵循和代码生成能力的流行方式。Kimi K3 由 Moonshot AI 于 2026 年 7 月发布，拥有 2.8 万亿参数，采用混合线性注意力机制和 100 万 token 上下文窗口，定位为与美国领先模型竞争的产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark)</a></li>

</ul>
</details>

**社区讨论**: 社区评论对训练数据污染表示怀疑，指出了暗示隐藏系统提示的分词异常，并提出了新的对抗性智能体基准测试。一些用户还提供了不同模型的成本和速度实际比较。

**标签**: `#AI models`, `#benchmark`, `#Kimi K3`, `#tokenization`, `#agentic tools`

---

<a id="item-6"></a>
## [Boris Cherny 谈 Claude Code 自主工作流](https://x.com/bcherny/status/2077929390806073807) ⭐️ 8.0/10

Boris Cherny 概述了让 Claude 能够端到端自主验证其工作的实用方法，包括权限自动模式、自动化代码审查、通过 Agent 视图进行多智能体管理，以及 /loop、/batch 和子智能体的工作树隔离等高级功能。 这一指导为团队信任 AI 智能体自动化整类工作提供了路线图，显著提升开发者的生产力和可靠性。它反映了行业向智能体工作流和带有适当护栏的 AI 辅助开发的更广泛趋势。 Cherny 强调，实现更高自主性并非依赖单一功能，而是将正确功能与护栏结合使用，例如用于迭代优化的 /loop、用于并行任务的 /batch、动态工作流，以及防止子智能体冲突的工作树隔离。Agent 视图可在 CLI、桌面、iOS 和 Android 应用中使用。

follow_builders · Boris Cherny · 7月17日 01:32

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 推出的 AI 编程助手，能够读取代码、编辑文件、运行命令并与外部服务交互。工作树隔离允许并行运行多个 Claude Code 会话，各自在独立的 git 分支上工作而不产生冲突；Agent 视图则提供了一个统一面板来监控和管理多个后台智能体。/loop 和 /batch 命令分别支持任务的迭代优化和批量处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/worktrees">Run parallel sessions with worktrees - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/agent-view">Manage multiple agents with agent view - Claude Code Docs</a></li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/cli-reference">Complete reference for Claude Code command -line interface...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Claude Code`, `#automated code review`, `#developer tools`, `#workflow automation`

---

<a id="item-7"></a>
## [美团 LongCat 发布 LoHoSearch，更难搜索智能体基准](https://x.com/Meituan_LongCat/status/2078119654632124547) ⭐️ 7.88/10

美团 LongCat 发布了 LoHoSearch，这是一个基于 762 万实体维基百科知识图谱的开源搜索智能体基准。在对 11 个前沿模型的测试中，最佳得分仅为 34.74%，远低于现有 BrowseComp 基准上约 90%的成绩。 LoHoSearch 解决了现有搜索智能体基准（如 BrowseComp）趋于饱和的问题，后者在十个月内得分从 30%升至 90%。它提供了一个更具挑战性的评估，凸显了 AI 智能体在长程推理和上下文管理方面仍有很大的改进空间。 该基准包含 544 道问题，涵盖 11 个领域，采用树与图结构。现有的上下文管理策略在 LoHoSearch 上仅带来+6.8 个百分点的提升，而在 BrowseComp 上为+14 个百分点。

aihot · X：美团 LongCat (@Meituan_LongCat) · 7月17日 14:08 · [中文阅读](https://aihot.virxact.com/items/cmrp0qw3s090ybitorwj6diwi)

**核验**: 多源印证

**背景**: BrowseComp 是一个浏览智能体基准，要求模型持续浏览互联网以寻找难以找到的信息。搜索智能体基准用于评估 AI 模型从大型语料库中搜索和综合信息的能力。LoHoSearch 采用自动化的知识图谱驱动方法生成问题，最大化搜索空间和结构复杂性，超越了人类标注者所能设计的范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12837v2">LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling</a></li>
<li><a href="https://openai.com/index/browsecomp/">BrowseComp : a benchmark for browsing agents | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmark`, `#search agent`, `#knowledge graph`, `#open source`

---

<a id="item-8"></a>
## [NVIDIA Nemotron 3 Embed 8B 登顶 RTEB 基准](https://www.marktechpost.com/2026/07/17/nvidia-ai-releases-nemotron-3-embed-an-open-embedding-collection-whose-8b-checkpoint-ranks-1-on-rteb) ⭐️ 7.75/10

NVIDIA 发布了 Nemotron 3 Embed 系列，这是一个开源的嵌入模型集合。其中 8B-BF16 版本在 RTEB 基准上以平均 NDCG@10 78.46 的成绩排名第一。 此次发布为检索型嵌入模型设立了新的标杆，这类模型对搜索和 RAG 系统至关重要。开源特性以及 1B-NVFP4 版本在 Blackwell 上的高吞吐量，使得先进的嵌入技术更加易用和高效。 该系列包含三个开源 checkpoint：8B-BF16、1B-BF16 和 1B-NVFP4。1B-NVFP4 版本在 Blackwell 上的吞吐量比 BF16 高 2 倍，精度保留 99.5%，所有模型支持最大 32,768 tokens 的序列长度。

aihot · MarkTechPost（RSS） · 7月17日 07:53 · [中文阅读](https://aihot.virxact.com/items/cmronvv4105bdbitohe86a4un)

**核验**: 多源印证

**背景**: 嵌入模型是将文本转换为稠密向量表示的神经网络，从而实现语义搜索和检索。RTEB（检索型文本嵌入基准）是一个新的基准，旨在评估搜索和 RAG 等实际应用中的检索准确性。NDCG@10（归一化折损累计增益在排名 10）衡量排序检索结果的质量。NVFP4 是 NVIDIA 的 4 位浮点格式，可在 Blackwell GPU 上加速推理，同时精度损失极小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/nvidia/omni-embed-nemotron-3b">nvidia/omni-embed-nemotron-3b · Hugging Face</a></li>
<li><a href="https://huggingface.co/blog/rteb">Introducing RTEB: A New Standard for Retrieval Evaluation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discounted_cumulative_gain">Discounted cumulative gain - Wikipedia</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#embedding models`, `#open-source`, `#AI`, `#benchmark`

---

<a id="item-9"></a>
## [OpenAI 提出'有用智能每美元'指标](https://openai.com/index/a-scorecard-for-the-ai-age) ⭐️ 7.6/10

OpenAI 提出了一个名为'有用智能每美元'的新指标，用于衡量 AI 投资回报，评估维度包括完成的有用工作量、成功任务的实际成本和结果可靠性。 该指标将关注点从 token 成本转向基于结果的价值，帮助企业更实际地评估 AI 投资回报，并解决了行业对衡量 AI 实际价值的关键需求，尤其适用于 AI 智能体和开发工具。 该指标从三个维度评估：完成的有用工作量、成功任务的实际成本和结果可靠性。它是 OpenAI 的 AI 记分卡的一部分，示例显示 GPT-5.6 Sol 在编码和规划任务上以更低的每任务成本超越了 Claude Fable 5。

aihot · OpenAI：官网动态（RSS · 排除企业/客户案例） · 7月17日 10:00 · [中文阅读](https://aihot.virxact.com/items/cmrozfoiv08mhbitofbllzxl4)

**核验**: 多源印证

**背景**: 传统的 AI 评估通常依赖 token 价格或基准分数，这些并不能反映实际价值。新指标旨在衡量每美元实际完成的工作量，包括重试和工具使用。这与新兴的'每成功任务成本'和'每美元智能'等概念一致，这些概念关注基于结果的投资回报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://andresseo.expert/ai/openais-new-ai-scorecard-the-metric-that-finally-measures-roi-beyond-token-costs/">OpenAI's AI Scorecard: Measuring Useful Intelligence per Dollar</a></li>
<li><a href="https://www.digitalapplied.com/blog/cost-per-successful-task-new-ai-evaluation-metric">Cost - Per - Successful - Task : A New AI Evaluation Metric</a></li>

</ul>
</details>

**标签**: `#AI metrics`, `#OpenAI`, `#cost efficiency`, `#AI evaluation`, `#useful intelligence per dollar`

---

<a id="item-10"></a>
## [乡村教育一等奖作品'智绘科普'技术拆解](https://mp.weixin.qq.com/s/a2YKWmyMoyIc3GKLbXffpQ) ⭐️ 7.1/10

首届'小有可为'大赛乡村教育赛道一等奖作品'智绘科普'的技术细节被公开，该系统采用 Qwen3.5 大语言模型与 Manim 动画引擎，通过多 Agent 分阶段协作与自动修复机制生成教学动画。 该项目展示了多 Agent AI 系统在教育领域的实际应用，尤其适用于教学资源匮乏的乡村地区。其分阶段协作与自动修复的工程范式可迁移至其他领域，有望降低高质量教育内容的创作门槛。 系统包含规划、草稿、实现、审查、合成五个阶段。渲染失败时可自动提取日志并修复，确保鲁棒性。它使用 Qwen3.5-397B-A17B 模型和 Manim Python 动画引擎。

aihot · 公众号：通义实验室（千问） · 7月17日 09:41 · [中文阅读](https://aihot.virxact.com/items/cmrorbywu06cebitoixzgpb5l)

**核验**: 多源印证

**背景**: Qwen3.5 是阿里云开发的大语言模型系列，在推理、编程和 Agent 任务上表现强劲。Manim 是一款基于 Python 的开源动画引擎，因 3Blue1Brown 的数学科普视频而广受欢迎。多 Agent 分阶段协作是指多个 AI 代理按顺序处理任务的不同阶段，从而实现自动化内容生成等复杂工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1936458621694227414">Manim 安装与使用全指南：从入门到动画创作 - 知乎</a></li>
<li><a href="https://juejin.cn/post/7593771861323546650">AI Agent 框架演进文章梳理 Agent 六 阶 段 ，从 ReAct、Autonomous...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#multi-agent collaboration`, `#educational animation`, `#Qwen3.5`, `#automation workflow`

---

<a id="item-11"></a>
## [Simon Willison 推出 LLM 陈词滥调高亮工具](https://simonwillison.net/2026/Jul/17/llm-cliche-highlighter/#atom-everything) ⭐️ 7.0/10

Simon Willison 开发了一个网页工具，用于高亮 LLM 生成文本中常见的十种陈词滥调，例如“无废话、无填充、无行话”。该工具通过 Anthropic 的 Claude Fable 5 模型以 vibe coding 方式创建。 该工具解决了 LLM 生成内容中日益严重的陈词滥调问题，帮助写作者和编辑产出更自然、更多样的文本。同时，它也展示了 AI 在写作质量控制方面的实际应用。 该工具可通过 r.jina.ai 从 URL 加载内容，将网页转换为 LLM 友好的 Markdown 格式。它会高亮特定模式，如 'is real and' 和 'worth naming'，并提供匹配和标记句子的摘要。

rss · Simon Willison · 7月17日 12:11

**核验**: 多源印证

**背景**: Vibe coding 是 Andrej Karpathy 提出的术语，指 AI 辅助软件开发，开发者描述目标后由 AI 生成代码，通常不进行详细审查。Claude Fable 5 是 Anthropic 专为长时间自主任务设计的最新模型。r.jina.ai 是 Jina AI 提供的服务，可将任意 URL 转换为适合 LLM 处理的干净 Markdown 格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/docs/models/claude-fable-5">Claude Fable 5 | Cursor Docs</a></li>
<li><a href="https://github.com/jina-ai/reader">GitHub - jina - ai /reader: Convert any URL to an LLM-friendly input with...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#LLM`, `#writing`, `#cliché detection`, `#Simon Willison`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="15"><span>其他追踪推文</span><span class="archive-tab-count">15</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="18"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">18</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2078205785100652663">@dotey: 可以添加专门的 AI 时间线，看到更多 AI 相关信息 https://t.co/0SuDsVpD9r</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 19:50 UTC · 喜欢 18 · 转发 1 · 回复 6 · 浏览 7114</p>
<p class="archive-item-content">可以添加专门的 AI 时间线，看到更多 AI 相关信息 https://t.co/0SuDsVpD9r</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2078199263415205978">@dotey: Claude Code 刚才短暂下架了 Fable 5，然后又恢复了。有个朋友比较倒霉，因为开启了“Usage credits”，一个正在进行中的任务就开始使用 API 额度了，一小会轻...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 19:24 UTC · 喜欢 42 · 转发 2 · 回复 12 · 浏览 18540</p>
<p class="archive-item-content">Claude Code 刚才短暂下架了 Fable 5，然后又恢复了。有个朋友比较倒霉，因为开启了“Usage credits”，一个正在进行中的任务就开始使用 API 额度了，一小会轻松 $18 就没了。<br>
<br>
他们要真下了也挺好，我周末就可以好好放松一下了，现在要忙于把剩余额度在周末消耗完，不然 19 日到期就不能再在 Claude Code 内用了。<br>
<br>
忠告：千万别打开“Usage credits”</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2078195610696482895">@dotey: 买 Mac 是没错的，现在主流 Agent 应用都是 Mac 支持最好，比如 Compter Use，只有 Mac 支持的好。 对于开发者来说，开发 App 肯定也优先 Mac。我之前也...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 19:10 UTC · 喜欢 54 · 转发 3 · 回复 5 · 浏览 15142</p>
<p class="archive-item-content">买 Mac 是没错的，现在主流 Agent 应用都是 Mac 支持最好，比如 Compter Use，只有 Mac 支持的好。<br>
<br>
对于开发者来说，开发 App 肯定也优先 Mac。我之前也试过 Electron，性能还是远比不上原生的。<br>
<br>
如果不需要移动办公 Mac Mini 或者 Mac Studio 也挺好，但是内存一定要高，16 G 都小了，硬盘也一步到位 1T 以上。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/huangyun_122/status/2078190928175739321">@huangyun_122: 宝玉老师的 BaoCut , 用来学英语，做信息搜集，简直太疯狂了 1/ 可以转录 Youtube 上任意视频，丢个 URL 就好 2/ 把翻译的中文，合轨到双语字幕 工具免费，skill 开源...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 18:51 UTC · 喜欢 75 · 转发 15 · 回复 2 · 浏览 26217</p>
<p class="archive-item-content">宝玉老师的 BaoCut , 用来学英语，做信息搜集，简直太疯狂了<br>
<br>
1/ 可以转录 Youtube 上任意视频，丢个 URL 就好<br>
2/ 把翻译的中文，合轨到双语字幕<br>
<br>
工具免费，skill 开源。你唯一要准备的是，Mac !! https://t.co/AQNX24KmXp</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2078170007121305707">@dotey: 设计能力好、品味好的人，不需要 AI 都能做出漂亮的设计，有 AI 更是如虎添翼，但普通人不行。 AI 能提升普通人的下限，但是提升不了上限； AI 能放大和加速专业能力。</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 17:28 UTC · 喜欢 33 · 转发 3 · 回复 4 · 浏览 12023</p>
<p class="archive-item-content">设计能力好、品味好的人，不需要 AI 都能做出漂亮的设计，有 AI 更是如虎添翼，但普通人不行。<br>
<br>
AI 能提升普通人的下限，但是提升不了上限；<br>
AI 能放大和加速专业能力。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2078164555188875366">@dotey: UI Design Opus 4.8 是最好的，Fable 5 也不见得比它更好。GPT 5.6 Design 只能说比 GPT 5.5 好点，还是很差。 推荐多用用 Claude De...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 17:06 UTC · 喜欢 63 · 转发 9 · 回复 9 · 浏览 13005</p>
<p class="archive-item-content">UI Design Opus 4.8 是最好的，Fable 5 也不见得比它更好。GPT 5.6 Design 只能说比 GPT 5.5 好点，还是很差。<br>
<br>
推荐多用用 Claude Design + Opus 4.8 做做原型设计 UI 设计，会让你的软件设计水平提升一大截。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/akazwz_/status/2078149922680135905">@akazwz_: opus 4.8 现在处于一个非常尴尬的位置，复杂点的需求我用 fable / GPT 5.6 sol，其他的需求我用 sonnet 5 也不会选 opus 4.8</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 16:08 UTC · 喜欢 17 · 转发 0 · 回复 17 · 浏览 17752</p>
<p class="archive-item-content">opus 4.8 现在处于一个非常尴尬的位置，复杂点的需求我用 fable / GPT 5.6 sol，其他的需求我用 sonnet 5 也不会选 opus 4.8</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2078100047489888652">@op7418: 虽然人没去 WAIC，但是东西去了。 https://t.co/NNJsJ0EdHN</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月17日 12:50 UTC · 喜欢 39 · 转发 0 · 回复 22 · 浏览 7189</p>
<p class="archive-item-content">虽然人没去 WAIC，但是东西去了。 https://t.co/NNJsJ0EdHN</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/Jackywine/status/2078049562376507648">@Jackywine: KIMI CEO 杨植麟，一个视频带你彻底看懂大规模 AI 系统训练的秘密 自己看一遍比什么都重要 https://t.co/F1YvOc3ZI6</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 09:29 UTC · 喜欢 627 · 转发 128 · 回复 27 · 浏览 134823</p>
<p class="archive-item-content">KIMI CEO 杨植麟，一个视频带你彻底看懂大规模 AI 系统训练的秘密<br>
自己看一遍比什么都重要 https://t.co/F1YvOc3ZI6</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikitabier/status/2078027748011086021">@nikitabier: If you want to keep track of the latest AI model releases, pin the AI custom timeline. It’s p...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月17日 08:03 UTC · 喜欢 3760 · 转发 327 · 回复 837 · 浏览 314351</p>
<p class="archive-item-content">If you want to keep track of the latest AI model releases, pin the AI custom timeline. It’s personalized for you, ranked and labeled by Grok. The best way to monitor the situation as it’s happening. https://t.co/E54JkKsAi7</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2077969583018066116">@op7418: 藏师傅的 Kimi K3 测评来了，这次确实非常牛逼！ 可以说是一个比较小的 DeepSeek 时刻 我直接拿它跟 Opus 4.8 做了对比测试。 从结果来看，互有胜负。 在复杂前端和...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月17日 04:12 UTC · 喜欢 210 · 转发 29 · 回复 83 · 浏览 81036</p>
<p class="archive-item-content">藏师傅的 Kimi K3 测评来了，这次确实非常牛逼！<br>
<br>
可以说是一个比较小的 DeepSeek 时刻<br>
<br>
我直接拿它跟 Opus 4.8 做了对比测试。<br>
<br>
从结果来看，互有胜负。<br>
<br>
在复杂前端和复杂开发的情况下，我觉得它跟 Opus 4.8 差不多是相当的水平。<br>
<br>
至于 Fable 5 和 5.6，我觉得还差一些，但已经是一个非常牛逼的成绩了。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2077969109506277602">@op7418: https://t.co/jEa8btnknH</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月17日 04:10 UTC · 喜欢 68 · 转发 10 · 回复 13 · 浏览 107888</p>
<p class="archive-item-content">https://t.co/jEa8btnknH</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2077959202627285056">@op7418: Codex 昨晚的更新在交互上终于对味了： 1. 左上角的切换：从 Work 和 Codex 切换成 ChatGPT 和 Codex 2. 历史聊天整合：ChatGPT 的历史聊天全部并...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月17日 03:30 UTC · 喜欢 75 · 转发 2 · 回复 75 · 浏览 23969</p>
<p class="archive-item-content">Codex 昨晚的更新在交互上终于对味了：<br>
<br>
1. 左上角的切换：从 Work 和 Codex 切换成 ChatGPT 和 Codex<br>
<br>
2. 历史聊天整合：ChatGPT 的历史聊天全部并进了左边“最近聊天”里面，你可以筛选是普通聊天还是 ChatGPT Work 的任务<br>
<br>
3. 顶部导航：分了 Chat 和 Work 两个 Tab，交互逻辑跟网页版和移动端一致了 https://t.co/e7kCJAVYH7</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2077928174252630286">@op7418: 离谱 Frontend Code Are 排第一</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月17日 01:27 UTC · 喜欢 19 · 转发 1 · 回复 9 · 浏览 11728</p>
<p class="archive-item-content">离谱 Frontend Code Are 排第一</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2077927715639017633">@op7418: 我的时间线上已经全是 Kimi K3 了 估计 Anthropic 达里奥又要气疯了，可能今天晚上又得发一篇博客来强调开源模型的危害了</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月17日 01:25 UTC · 喜欢 80 · 转发 7 · 回复 41 · 浏览 32090</p>
<p class="archive-item-content">我的时间线上已经全是 Kimi K3 了<br>
<br>
估计 Anthropic 达里奥又要气疯了，可能今天晚上又得发一篇博客来强调开源模型的危害了</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2078007598758895769">Garry Tan: Just be a YC startup Problem solved https://t.co/UWByP04Uio</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 7月17日 06:43 UTC · 喜欢 27 · 转发 2 · 回复 8</p>
<p class="archive-item-content">Garry Tan tweets a sarcastic remark about being a YC startup.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2078004977294032991">Swyx: HOLY FUCKING SHIT the react avengers have assembled https://t.co/8hqGSTOM16</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Swyx · 7月17日 06:32 UTC · 喜欢 12 · 转发 0 · 回复 6</p>
<p class="archive-item-content">Swyx expresses excitement about a gathering of notable React developers.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/amasad/status/2077989946565206267">Amjad Masad: $NVDA should be pumping on the K3 news. Instead it’s down.</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Amjad Masad · 7月17日 05:33 UTC · 喜欢 145 · 转发 0 · 回复 34</p>
<p class="archive-item-content">Amjad Masad tweets that Nvidia stock should be rising on K3 news but is down.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2077988898601369978">Garry Tan: Please join @garryslist We are trying to organize the common sense builders It’s going to be...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 7月17日 05:28 UTC · 喜欢 115 · 转发 3 · 回复 14</p>
<p class="archive-item-content">Garry Tan promotes Garryslist to organize common sense builders for a political fight in California and America.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/adityaag/status/2077983583168278961">Aditya Agarwal: If you have something very valuable....but letting people use it allows them to recreate it.....</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Aditya Agarwal · 7月17日 05:07 UTC · 喜欢 38 · 转发 1 · 回复 4</p>
<p class="archive-item-content">A tweet questioning whether something truly valuable can be easily recreated if people are allowed to use it.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/adityaag/status/2077983435000324125">Aditya Agarwal: I am literally switching models off of Fable right now for our systems. This isn&#x27;t trying to...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Aditya Agarwal · 7月17日 05:07 UTC · 喜欢 68 · 转发 3 · 回复 12</p>
<p class="archive-item-content">Developer switches from paid AI model service to free alternative due to cost.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2077982627278303279">Peter Yang: Underrated reply 🤣 https://t.co/TkpX22Be1e</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月17日 05:04 UTC · 喜欢 295 · 转发 11 · 回复 7</p>
<p class="archive-item-content">A trivial reply on X with no meaningful content or technical value.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2077979212569522461">Thibault Sottiaux: Spurious correlation or causation? https://t.co/9XVcUBfT74</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月17日 04:50 UTC · 喜欢 372 · 转发 3 · 回复 176</p>
<p class="archive-item-content">A tweet questioning spurious correlation vs causation, linking to an external article.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2077968093406707970">Peter Yang: I&#x27;m surprised Claude Code doesn&#x27;t have any Google Workspace connectors beyond Drive while Cha...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月17日 04:06 UTC · 喜欢 2 · 转发 0 · 回复 0</p>
<p class="archive-item-content">Peter Yang observes that Claude Code lacks Google Workspace connectors beyond Drive, unlike ChatGPT.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2077966904938127502">Peter Yang: smh trying to use Claude Code browser use Hope they hire some good folks to fix this https://...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月17日 04:01 UTC · 喜欢 12 · 转发 0 · 回复 4</p>
<p class="archive-item-content">A brief complaint about Claude Code&#x27;s browser use feature with a hope for fixes, lacking substance.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2077961425008382029">Nikunj Kothari: this is who runs this account https://t.co/5xGlSlZwTl https://t.co/ot04FHFqoq</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 7月17日 03:39 UTC · 喜欢 19 · 转发 0 · 回复 2</p>
<p class="archive-item-content">A brief self-introduction tweet with links to the account owner.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2077953473535176772">Zara Zhang: So many interesting hardware ideas from China Like this face mask that doubles as a mic so th...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 7月17日 03:08 UTC · 喜欢 88 · 转发 3 · 回复 16</p>
<p class="archive-item-content">A face mask that doubles as a mic for private voice dictation is an interesting hardware idea from China.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2077938877407633857">Swyx: we make sure some of the top YC AI companies are featured at AIE every single year. this year...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Swyx · 7月17日 02:10 UTC · 喜欢 36 · 转发 1 · 回复 12</p>
<p class="archive-item-content">Swyx thanks Garry Tan and Eve Bouff for speaking at the AIE event featuring top YC AI companies.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/_catwu/status/2077933568282755145">Cat Wu: You know your workflows best. Show our team how you use Cowork so we can make it work better...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Cat Wu · 7月17日 01:49 UTC · 喜欢 155 · 转发 9 · 回复 11</p>
<p class="archive-item-content">Cat Wu asks non-engineering users to share their workflows using Cowork to help improve the product.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/bcherny/status/2077929404219474148">Boris Cherny: The bigger payoff comes when fixing and maintaining happens in the background and your teams...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Boris Cherny · 7月17日 01:32 UTC · 喜欢 89 · 转发 3 · 回复 21</p>
<p class="archive-item-content">Boris Cherny shares a high-level thought on the value of background maintenance work and asks where teams are on an unspecified progression scale.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/bcherny/status/2077929397495959693">Boris Cherny: Once your teams are bought in, how do you track it? Usage is worth watching (e.g. a dashboard...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Boris Cherny · 7月17日 01:32 UTC · 喜欢 83 · 转发 2 · 回复 11</p>
<p class="archive-item-content">Suggests tracking return on engineering effort by comparing to manual effort cost rather than just usage.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2077928889750520141">Thibault Sottiaux: Look at this beauty https://t.co/arLnM9smr9</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月17日 01:30 UTC · 喜欢 703 · 转发 13 · 回复 164</p>
<p class="archive-item-content">A tweet expressing admiration for an unspecified item via a link without any explanatory content.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2077928427936710901">Thibault Sottiaux: Evening! We’ve gotten lots of great feedback on the new ChatGPT desktop app (which we didn&#x27;t...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月17日 01:28 UTC · 喜欢 4657 · 转发 203 · 回复 1229</p>
<p class="archive-item-content">ChatGPT desktop app gets sidebar history/projects, sync across platforms, and mode switching, with no changes to Codex mode.</p>
</article>
</div>
</section>
