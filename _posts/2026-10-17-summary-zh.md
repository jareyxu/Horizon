---
layout: default
title: "Horizon Summary: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
---

> 从 60 条内容中筛选出 9 条重要资讯。

---

1. [Claude 破解 NIST ECDSA 曲线种子来源：出自 lrand48 随机数生成器](#item-1) ⭐️ 9.0/10
2. [Anthropic 的 Claude Code 团队详解每日 3 万 PR 的评测打分式自动评审](#item-2) ⭐️ 8.3/10
3. [苹果 MLX 新增分布式推理，Mac Studio 集群跑通近万亿参数模型](#item-3) ⭐️ 8.0/10
4. [Mercor：美国 90%的工作时长不在 AI 基准测试覆盖范围内](#item-4) ⭐️ 8.0/10
5. [PromptArmor：开放权重模型对间接提示词注入的易感率高出 88%](#item-5) ⭐️ 7.67/10
6. [Google Research 展示 AI 智能体自主湿实验室的三项基础构建模块](#item-6) ⭐️ 7.53/10
7. [商务部、科技部拟将 23 项人工智能技术增列至出口管制目录](#item-7) ⭐️ 7.33/10
8. [Anthropic：AI agent 工作时长已达员工 6 倍，技术岗初级招聘占比降至 9%](#item-8) ⭐️ 7.0/10
9. [宝玉讲解 Handwired：不训练，把普通代码直接变成神经网络](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Claude 破解 NIST ECDSA 曲线种子来源：出自 lrand48 随机数生成器](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 9.0/10

这些种子的来源悬而未决约 25 年，引发了人们对曲线可能被刻意挑选、暗藏弱点的猜疑，因为它们在 TLS、代码签名等安全关键系统中被广泛使用。这一结果同时也是 AI 辅助研究的一次醒目示范：模型自主逆向破解了人类密码学家多年尝试的难题。 该发现解释了参数是如何产生的，却没有解释这些曲线是如何被挑选出来的，因为在长达数月的过程中生成后又丢弃的候选种子已无从查证。第六个二进制曲线种子 B-163 不符合 Claude 尝试过的任何模式，至今仍无法解释；讨论中提到的最简单假设是，在发布之前的某个环节有人打错了一位数字。

hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**核验**: 多源印证

**背景**: NIST 于 2000 年在 FIPS 186-2 中公布了这些椭圆曲线；按照 ANSI X9.62 的规范，它们本应通过用 SHA-1 哈希一个任意种子、再由摘要派生参数的方式生成，但 NIST 从未说明这些任意种子从何而来。lrand48 是 POSIX/SysV 的线性同余生成器，通过 srand48() 播种，返回 31 位的非负长整数，其输出可预测，完全不适合密码学用途——正因如此，它留下的痕迹（例如最高位十六进制数字从不超过 7）成了破案的关键线索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mkssoftware.com/docs/man3/drand48.3.asp">drand48 (), erand48 (), jrand48 (), lcong48 (), lrand48 ... lrand48 (3) - Linux man page drand48 (3) - Linux manual page - man7.org drand48 - Open Group rand48 (3) – pseudo-random number generators and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elliptic-curve_cryptography">Elliptic-curve cryptography - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2510.02383">[2510.02383] Selmer-Inspired Elliptic Curve Generation Selmer-Inspired Elliptic Curve Generation - arXiv.org The NIST Elliptic Curves Seeds Bounty Has Been Claimed ECDSA Curve Seeds Solved: Claude Found lrand48 (2026 ... Claude traces NIST P-256 seed to a 1997 random number ... openssl-ecparam - OpenSSL Documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者总体反应是既赞叹又觉得好笑，有人调侃说这个尘封数十年的秘密原来只是一次 1997 年的普通库函数调用。最具分量的保留意见来自 fidotron：该结果只证实了生成方法，并未说明曲线的挑选过程，因为被丢弃的候选种子无从查证，理论上仍可能通过遍历时间戳来筛选出具有特定性质的曲线；其他人则补充了自己尝试同一问题的亲身经历、破解谜题所用的‘31 位 / 首位数字’线索的重构，以及对无法解释的 B-163 种子的错字假设。

**标签**: `#cryptography`, `#ECDSA`, `#AI research`, `#Claude`, `#NIST standards`

---

<a id="item-2"></a>
## [Anthropic 的 Claude Code 团队详解每日 3 万 PR 的评测打分式自动评审](https://claude.dev/blog/solving-code-review-at-anthropic/) ⭐️ 8.3/10

Anthropic 的 Claude Code 团队发布博客，介绍了其自动化、由评测（eval）打分的代码评审流水线：它每天对成千上万个 pull request 进行分诊，只把人类注意力分配给被判定为高风险的改动。文章把核心问题从“有没有人读过这段代码”改写为“这次改动可能出什么问题，以及哪一种检查——自动的还是人工的——才是抓住它的正确手段”。 它为“AI 原生”工程组织如何应对人力无法匹配的代码评审量提供了一份公开而具体的蓝图，很可能影响其他公司设计自己的评审与分诊工具。它也把行业讨论从“是否有人在环”这类人数式争论，转向按风险在自动检查与人工检查之间做分流。 该流水线明确按风险分级：文档、文案、仅内部使用的功能，以及藏在开关后面的增量式改动等低风险变更，只要自动评审与安全检查通过，就不再需要人工审阅者。评测集会在每次事故后扩充，而对评审器本身所做的任何改动，都要拿全部累积的评测集来打分。

hackernews · pretext · 10月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=50122951) · 2 个来源

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 推出的智能体式编程工具，能够理解代码库、修改文件并替开发者执行命令。当 AI 智能体产生的 pull request 数量远超人工阅读能力时，CodeRabbit 等厂商开始提供 AI 代码评审与 PR 分诊产品，用来总结意图、标记风险并指派审阅者。这里的“eval（评测）”指自动化打分装置——常见形式是“LLM 当裁判”或基于代码的断言——用于在一组不断增长的测试用例上衡量模型或评审系统是否表现正确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tianpan.co/blog/2026-05-17-llm-reviews-llm-error-laundering">When LLMs Review LLMs, Errors Get Laundered Not Caught</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论相当热烈且普遍持怀疑态度：有人质疑在每天 3 万次提交的规模下“评审”一词是否还有意义；有人索要流失率（churn）和每行代码成本数据，并猜测后者高得离谱、代码其实在反复重写；也有人认为没有任何人能跟上这样的量级，Anthropic 只能依赖 AI 自己监管自己。还有读者反对让 LLM 写文档却无人阅读，并指出文章措辞过于工整，很可能本身就是 AI 写的，尽管有人声称 Anthropic 员工对外沟通不用 AI。

**标签**: `#Claude Code`, `#AI developer tools`, `#code review`, `#AI agents`, `#Anthropic`

---

<a id="item-3"></a>
## [苹果 MLX 新增分布式推理，Mac Studio 集群跑通近万亿参数模型](https://machinelearning.apple.com/research/mlx-distributed-inference) ⭐️ 8.0/10

苹果机器学习研究团队于 2026 年 10 月 15 日发布了一篇重点文章，介绍如何在 Mac Studio 上利用 MLX 与 RDMA 进行本地及分布式大模型推理，并展示了 Meta 的 Muse Spark Open（近万亿参数的旗舰级模型）在四台 Mac Studio 组成的集群上生成速度超过每秒 36 个 token。该工作将最新版 MLX 与一套通信后端结合，使 Apple 芯片设备可以从单台 Mac Studio（最高 512GB 统一内存）扩展到多机集群。 这表明旗舰级别的开放权重模型可以运行在桌边消费级硬件上，而不必依赖云端 GPU，对隐私敏感场景、成本控制以及希望完全本地掌控推理的团队都意义重大。同时，这也巩固了苹果在本地 AI 技术栈中的地位，使其统一内存的 Mac 成为其他实验室发布的开放权重模型的可行运行平台。 这个亮眼的速度数字对应的其实是相对有限的负载：第一张柱状图基于 8192 token 的上下文，评论者指出这在当下偏小；而且基准测试中 Meta 的模型使用 4-bit 量化，对比的 Qwen 却用原生 BF16。另外值得注意的是，MLX 仅支持 Metal，因此分布式推理只能在 Apple 芯片设备之间进行，无法像 vLLM 搭配 Ray 那样与 CUDA GPU 机器混合组网。

hackernews · antipaul · 10月16日 13:43 · [社区讨论](https://news.ycombinator.com/item?id=50118320)

**核验**: 多源印证

**背景**: MLX 是苹果开源的一套数组与机器学习框架，专为发挥 Apple 芯片的统一内存架构而设计——在统一内存中，CPU 与 GPU 共享同一个内存池，而不必通过 PCIe 总线来回拷贝张量。正是统一内存让单台 Mac Studio 能够容纳超大模型，而 RDMA（远程直接内存访问）则提供了低延迟网络层，让多台机器像一个大内存池一样协同工作。Muse Spark Open 是 Meta Superintelligence Labs 推出的面向编码优化的开放权重模型，公开信息显示其为 816B 总参数、42B 激活参数，支持 100 万 token 上下文窗口，于 2026 年 10 月以 Muse 模型许可证发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://machinelearning.apple.com/research/mlx-distributed-inference">Local and Distributed Large LLM Inference with MLX and RDMA on...</a></li>
<li><a href="https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B">meta- models / Muse - Spark - Open -816B-A42B · Hugging Face</a></li>
<li><a href="https://contracollective.com/blog/mlx-distributed-inference-multi-mac-cluster-2026">MLX Distributed Inference : Multi-Mac Cluster... — Contra Collective</a></li>

</ul>
</details>

**社区讨论**: 社区态度是感兴趣但有所质疑：最主要的批评集中在基准测试的公平性上，有评论者认为苹果把 Meta 的模型按 4-bit 量化、却只拿原生 BF16 的 Qwen 作对比，是在刻意压低 Qwen；另一位则指出 36 tok/s 的数字只是基于 8192 token 的上下文测得。也有人给出了真实环境数据——单台 256GB 的 M5 Ultra 运行 DeepSeek 4.1 Flash 0910 约 45 tok/s、预填充约 3200 tok/s——还有条略带调侃的评论说，Meta 花数十亿美元训练开放权重模型，而苹果靠卖机器把它们跑起来赚取每台数千美元。

**标签**: `#MLX`, `#local-LLM-inference`, `#Apple`, `#distributed-inference`, `#benchmarking`

---

<a id="item-4"></a>
## [Mercor：美国 90%的工作时长不在 AI 基准测试覆盖范围内](https://www.mercor.com/research/labor-index/benchmark-map/) ⭐️ 8.0/10

Mercor Research 发布了一份针对美国经济的“基准测试地图”，发现大约 90%的美国工作时长花在现有 AI 基准测试覆盖很差甚至完全没有覆盖的任务上。该分析将基准测试的提示词与 O*NET 职业任务数据库进行对照，得出结论：人们很难真正了解 AI 模型在美国人实际从事的工作上表现究竟有多好。 这直接动摇了“高基准分即代表真实能力”的假设，对构建或评估 AI 智能体、开发者工具以及企业级部署的人都至关重要。如果基准测试的覆盖范围偏向于一小部分高薪工作，那么 AI 实验室就可能在“易于自动评分”的任务上过度优化，而非真正对应大多数人所从事的劳动。 研究指出，即使在控制了 AI 暴露度之后，来自薪酬总额更高职业的 O*NET 任务在基准测试提示词中仍然显著过度代表，说明存在偏向高薪工作的选择偏差。社区批评者还指出，“覆盖良好”的判定门槛过低——例如社会工作者的“为有育儿问题的父母提供咨询”这一任务，仅凭 13 条提示词就被视为覆盖良好。

hackernews · speckx · 10月16日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50121179)

**核验**: 多源印证

**背景**: AI 基准测试是用于衡量和比较模型在特定任务上表现的标准化测试或数据集，是行业内通用的参照标准。O*NET 是美国劳工部的一个数据库，记录了数千种职业对应的任务、技能和知识。Mercor 是一家旧金山公司，负责将各领域专家和专业人士与 AI 实验室及企业对接，付费让他们创建、审核和评估前沿模型所用的训练数据与基准任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.evidentlyai.com/blog/ai-benchmarks">25 AI benchmarks: examples of AI models evaluation</a></li>
<li><a href="https://www.mercor.com/">Mercor | Organizing human intelligence to power the AI economy</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上 301 条评论总体上持怀疑态度：有评论者将这一发现类比为“门卫谬误”，即用自动门取代门卫看似划算，却忽略了门卫承担的其他关键职能。也有人认为“覆盖良好”实际上只是“有覆盖”的同义词，批评基准测试明显偏向高薪职业，并援引 Karpathy 的说法——AI 目前仅能处理约 2%-5%的工作，而重度使用者与轻度使用者之间的差距正在扩大。

**标签**: `#AI benchmarks`, `#AI evaluation`, `#future of work`, `#labor economics`, `#AI industry analysis`

---

<a id="item-5"></a>
## [PromptArmor：开放权重模型对间接提示词注入的易感率高出 88%](https://www.promptarmor.com/resources/open-weight-susceptibility) ⭐️ 7.67/10

PromptArmor 威胁情报团队在 9800 次试验中对比了开放权重模型（DeepSeek、Kimi、GLM、Qwen）与闭源模型（GPT、Claude、Gemini），发现开放权重模型面对真实世界间接提示词注入攻击链的易感率为 26.7%，而闭源模型为 14.2%，前者高出 88%。评测选取各家最新的旗舰模型与最具性价比的变体，聚焦企业实际使用最多的那些模型。 这项评测为企业与开发者提供了一个具体数字，量化了此前多停留在经验层面的风险权衡：在自托管的开放权重模型上运行 Agent，意味着更多护栏责任被转移到部署方自己身上。鉴于间接提示词注入被 OWASP LLM 应用十大风险列为第一项，该结论对构建 AI Agent 或 MCP 类工具集成的人具有直接参考价值。 在具体攻击类型上差距更为悬殊：在“总结 URL 并运行恶意代码”这条攻击链中（Agent 访问攻击者网站并执行恶意代码），开放权重模型易感率为 49%、闭源模型仅 9%；钓鱼登录浮层为 36% 对 5%；通过 Markdown 图片外泄邮件为 23% 对 9%。PromptArmor 还强调模型自我拒绝并非攻击是否成功的可靠指标，因为模型可能误报自己是否中招，甚至在被自己识别出攻击后仍然执行——报告中引用了某模型已将恶意 skill 标记为供应链后门却仍运行它的案例；不过本次发布只是易感率基准摘要，未公开完整的攻击链细节与缓解方案。

aihot · PromptArmor：Threat Intelligence · 10月16日 00:00 · [中文阅读](https://aihot.news/items/y1c13l53cd5u3wg565qu60q4d)

**核验**: 多源印证

**背景**: 间接提示词注入是一种把恶意指令藏在 Agent 会读取的外部内容（网页、文档、邮件）里的攻击方式，而不是由用户直接输入；由于大语言模型难以区分开发者设定的可信指令与检索到的不可信内容，模型可能把嵌入的文本当成合法命令，进而执行数据外泄或代码执行等非预期动作。开放权重模型指训练所得的参数被公开发布的模型，任何人都可以下载、微调和重新部署，DeepSeek、Kimi、GLM、Qwen 是其中代表性发布，与 GPT、Claude、Gemini 等不公开权重的专有模型形成对比。这一区别对安全很重要：一旦模型运行在他人环境中，厂商侧的安全对齐与护栏就更难强制执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indirect_prompt_injection">Indirect prompt injection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>

</ul>
</details>

**标签**: `#AI 安全`, `#提示词注入`, `#开源模型`, `#AI Agent`, `#安全评测`

---

<a id="item-6"></a>
## [Google Research 展示 AI 智能体自主湿实验室的三项基础构建模块](https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/) ⭐️ 7.53/10

Google Research 发布博客文章，介绍了三项相互关联的研究成果——VERID 框架、适配体闭环发现以及全新（de novo）蛋白结合剂设计，并将它们共同定位为 AI 智能体在自主湿实验室中运行所需的基础构建模块。该发布将这三项工作定位为让软件智能体不仅能“推理”生物学问题，还能驱动真实物理实验并从实验结果中学习的关键步骤。 这项工作把 AI 智能体从编程、网页操作等纯数字任务，进一步延伸到真实的物理实验科学领域——而目前生物学的“设计—构建—测试—学习”闭环仍高度依赖缓慢的人工操作。如果智能体能够可靠地闭合这一闭环，就有望加速药物发现、蛋白质工程与诊断技术研发；这同时表明像 Google Research 这样的顶级研究机构已将“自驱动实验室”视为严肃的研究方向，而非演示噱头。 目前公开的摘要信息较为简短，除这三个被点名的方向外，尚未披露数据集、基准测试数值或具体模型名称等细节：VERID 被描述为一个框架；适配体相关工作强调“闭环”，即提出候选—实验测试—结果反馈的迭代循环，而非一次性预测；蛋白结合剂工作则聚焦于全新设计（de novo），而非基于已有骨架的改造。读者应把这篇文章视为研究方向概览，而非经过同行评审的最终结果，后续仍需更多细节来判断其可复现性。

aihot · Google Research：Blog（网页） · 10月16日 00:00 · [中文阅读](https://aihot.news/items/kovelcbltjj7xf054h8mffaxo)

**核验**: 多源印证

**背景**: 湿实验室（wet lab）是指对液体和生物活体样本进行真实实验的实验室，与纯计算工作相对；而自驱动实验室（self-driving lab）或自主实验室，则把机器人液体处理设备、传感器与 AI 软件结合起来，由软件决定下一步做哪个实验。适配体（aptamer）是短的单链 DNA 或 RNA 分子，能折叠成特定三维结构并像抗体一样结合目标蛋白，但成本更低、稳定性更好，传统上通过 SELEX 等迭代筛选技术获得。全新蛋白结合剂设计（de novo binder design）比改造已有蛋白骨架更进一步：它针对选定的靶点，从零开始计算生成新结合剂的氨基酸序列和三维结构，AlphaProteo、BindCraft 等系统让这一思路广受关注。本文提到的 VERID 正是这一图景中的一环，被定位为把 AI 推理“锚定”到可验证的生物学现实中的智能体框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/de-novo-protein-binder-design">De Novo Protein Binder Design</a></li>
<li><a href="https://arxiv.org/pdf/2409.08022">De novo design of high-affinity protein binders</a></li>
<li><a href="https://www.researchgate.net/publication/280865250_Protein_Activity_Regulation_Inhibition_by_Closed-Loop_Aptamer-Based_Structures_and_Restoration_by_Near-IR_Stimulation">Protein Activity Regulation: Inhibition by Closed - Loop Aptamer -Based...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#autonomous labs`, `#protein design`, `#AI for Science`, `#Google Research`

---

<a id="item-7"></a>
## [商务部、科技部拟将 23 项人工智能技术增列至出口管制目录](https://www.ithome.com/1/013/983.htm) ⭐️ 7.33/10

2026 年 10 月 16 日，商务部、科技部发布 2026 年第 48 号公告，就修订《中国禁止出口限制出口技术目录》公开征求意见（意见反馈期为 10 月 16 日至 11 月 15 日），拟增列人工智能、生物医药、光伏三个领域共 40 项技术，其中禁止出口 14 项、限制出口 26 项。其中人工智能领域拟增列大模型、智能体、算力集群、信息处理等 23 项关键技术，并自公告发布之日起至修订目录正式实施前对相关技术实施出口前登记管理。 这是中国出口管制体系大规模向人工智能领域延伸的重要举措，为 AI 企业的海外业务划定了合规边界，也与各主要经济体对敏感技术实施出口管控的做法相呼应。目录修订将直接影响大模型出海、海外算力部署、开源合作与联合研发等模式的合规判断，进而影响全球 AI 技术交流与产业链合作的格局。 公告明确，对已通过开源、发表学术论文等方式进入公共领域的相关技术不纳入出口管理范围，并对开源、中国企业在境外自建自营算力中心、赴境外开展芯片流片制造、利用境外资源开展联合研发、参与国际标准制定等情形适用自动许可等便利措施，基本实现“即报即出”。此外，企业利用限制类大模型对外提供 API 调用、APP/网页交互、SaaS 应用及本地端侧轻量化部署不属于大模型技术出口管理范围，但海外本地化部署属于管理范围（部署在海外自有云等风险可控情形可适用自动许可）。

aihot · IT之家·人工智能 · 10月16日 08:23 · [中文阅读](https://aihot.news/items/p11tj593iq5nrtiotvoxllop4)

**核验**: 已核对原文

**背景**: 《中国禁止出口限制出口技术目录》依据《中华人民共和国对外贸易法》第十八条、第二十条制定，由商务部会同科技部等有关部门发布并动态调整，自 2001 年以来已多次修订，对禁止出口或限制出口的技术作出明确规定。列入目录技术的出口经营者需按规定申请技术出口许可证，并凭证办理外汇、银行、税务、海关等相关手续。需要注意的是，“技术出口”范围较广，不仅指向境外转让技术所有权，还包括境内技术授权境外使用、境内技术的所有权人或实际控制人变更为境外主体等情形，这也是公告会涉及大模型海外部署等场景的原因。

**标签**: `#AI policy`, `#export controls`, `#China regulation`, `#AI industry`, `#technology governance`

---

<a id="item-8"></a>
## [Anthropic：AI agent 工作时长已达员工 6 倍，技术岗初级招聘占比降至 9%](https://x.com/dotey/status/2111223306061836484) ⭐️ 7.0/10

10 月 16 日 Anthropic 发布两份内部报告：到 8 月，员工调用的 AI agent 累计工作时长已是员工工时的约 6 倍（agent 只计实际运行与调用工具的时间，员工按每人每周 40 小时估算）；技术部门新招员工中初级岗位占比从 27% 降到 9%，2025 年 12 月之后初级招聘明显减少。报告还显示工程师人均代码提交量是半年前的约 5 倍，约 20% 的受访员工表示自己的角色正从亲手干活转向管理一群 Claude。 这是少见的来自头部 AI 公司的一手量化证据，展示了 agent 型 AI 已经多深地改变了内部工作方式，而 Anthropic 也把自己视为先行指标——现在出现在用 AI 最深的公司的招聘与分工变化，未来可能扩散到更多行业。数据还表明，制约 AI 生产力的瓶颈已不再是模型能力，而是人的注意力，这对开发者工具规划、团队结构设计和初级岗位招聘都有参考意义。 Claude 会话中约 80% 的时间在等人回复；给 agent 写固定指令、检查产出、搭监控流程这类“管 AI”的工作，在员工使用 Claude 过程中的占比从 2025 年秋天的 10% 涨到 2026 年春天的 22%。一项追踪 192 位开始使用编程 agent 的工程师的研究发现，他们用上之后代码产出明显增加，且 agent 写的代码与人写的代码随后被删除或撤回的比例没有差别；Anthropic 也提醒，它本身是 AI 公司且处于高速扩张期，这些数字不能直接套到普通企业身上。

twitter · 宝玉 · 10月16日 22:30

**核验**: 多源印证

**背景**: Anthropic 是开发 Claude 的 AI 公司，Claude 是一个大语言模型助手，定位与 OpenAI 的 ChatGPT、Google 的 Gemini 类似。所谓“AI agent”，指由大模型驱动、不只是一问一答，而能自主规划并执行多步任务、调用代码执行或文件读写等外部工具的系统。第二份报告把 1334 名 Anthropic 员工的内部问卷与 Morning Consult 8 月对近 1.1 万名美国成年人的调查作对比，发现双方对 AI 与就业的推理逻辑相近，但预期差距极大——例如认为 AI 到 2030 年能做出诺贝尔奖级别发现的比例，员工为 91%，美国公众仅 39%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/">Claude</a></li>
<li><a href="https://notes.kamacoder.com/llm/app/agent_intro.html">Agent 到底 是 什 么 ？和普通大模型问答、ChatBot、Workflow有 什 么 区别</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Anthropic`, `#行业趋势`, `#招聘变革`, `#AI developer tools`

---

<a id="item-9"></a>
## [宝玉讲解 Handwired：不训练，把普通代码直接变成神经网络](https://x.com/dotey/status/2111097422810169575) ⭐️ 7.0/10

知名中文技术博主宝玉（dotey）发布了中英双语的 Handwired 教学视频，讲解如何把普通程序代码原封不动地转换成神经网络权重——完全不做训练，结果依然一个数都不差。他用倒计时、闰年判断、FizzBuzz、阶梯电价、生命游戏和贪吃蛇等例子做了演示，其基础是 Cheng Lou 的开源项目 Handwired，可把普通 JavaScript 变成精确且完全可微的神经网络。 它通过颠倒常规流程，让开发者对权重、层和激活函数究竟是什么有了具体而直观的认识：不是让数据去学习权重，而是由程序员手工把权重接好，使网络精确复现已知规则。由于生成的网络依然可微，这就打开了混合模式的想象空间——硬编码的业务逻辑与可训练参数可以共存于同一个模型，并且能在浏览器里、无需 GPU 就能运行。 教程把神经网络拆成两种基本零件——加权求和与开关（通过 ReLU 阶梯、选择器和比较运算实现），并展示了一条“及格线”如何变成含 7 个权重的单层网络。视频还讨论了计算开销如何取决于声明的网格、单元格和宿主循环，Handwired 与 ChatGPT 背后的 Transformer 架构差在哪里，权重能否在浏览器中现场训练并在刷新后保留，出错时怎么排查，以及 CPU 与 WebGPU 的性能差异。

twitter · 宝玉 · 10月16日 14:10

**核验**: 多源印证

**背景**: 常规神经网络是由多层简单单元堆叠而成，每个单元先对输入做加权求和再加上偏置，然后通过一个非线性函数输出；这些权重通常靠训练得到，也就是用梯度下降不断调整，使数据上的误差最小。Handwired 把这一过程反过来：Cheng Lou 的项目把普通 JavaScript 的控制流编译成同样的“加权求和 + 激活”结构，于是网络是精确地计算这段程序，而不是去近似它，同时依然保持可微，权重仍可继续微调。它的实用吸引力在于全部在浏览器里运行、不需要 GPU，让已经会写代码的人能直接看到并调试神经网络内部的计算过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chenglou.me/handwired/">Turn your regular JavaScript code into a neural net.</a></li>
<li><a href="https://rohitghumare.com/blog/handwired-javascript-neural-net/">Handwired: How JavaScript Becomes an Exact Neural Net</a></li>
<li><a href="https://endash.us/toolkit/items/handwired-dot-wiki">Handwired.wiki: JavaScript as a Neural Net - endash.us</a></li>

</ul>
</details>

**标签**: `#神经网络`, `#handwired`, `#AI教程`, `#技术实现`, `#AI开发工具`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="12"><span>其他追踪推文</span><span class="archive-tab-count">12</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="10"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">10</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2111209934105018471">@dotey: 这效率 Roadster 游戏都出来了 https://t.co/fO82120Y0c</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 21:37 UTC · 喜欢 8 · 转发 0 · 回复 7 · 浏览 3456</p>
<p class="archive-item-content">这效率 Roadster 游戏都出来了<br>
<br>
https://t.co/fO82120Y0c</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/ammaar/status/2111200113095803282">@ammaar: I used Gemini 4 Argon to make Subway Surfers for the new flying Tesla Roadster 🚀 Fly over mov...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 20:58 UTC · 喜欢 732 · 转发 51 · 回复 65 · 浏览 29594</p>
<p class="archive-item-content">I used Gemini 4 Argon to make Subway Surfers for the new flying Tesla Roadster 🚀<br>
<br>
Fly over moving traffic, hit the thrusters to barrel roll in the sky, and collect air power-ups to set a high score.<br>
<br>
Play + code below! https://t.co/fLlxNmZe3G</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/PeterMcCrory/status/2111197592285860233">@PeterMcCrory: Today, we&#x27;re publishing two new findings from inside Anthropic: how work and hiring are chang...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 20:48 UTC · 喜欢 316 · 转发 28 · 回复 15 · 浏览 21662</p>
<p class="archive-item-content">Today, we&#x27;re publishing two new findings from inside Anthropic: how work and hiring are changing at a company at the frontier of AI adoption, and how Anthropic staff expect AI to change the economy.<br>
<br>
https://t.co/ehPoxeJGH2</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2111134693743861870">@dotey: 补充一点，除了 Opus 5.5 调度，还可以充分利用 advisor，让 Fable 当 Advisor 给 Opus 当顾问 GPT 6.1 Sol 干杂活其实挺不错的</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 16:38 UTC · 喜欢 85 · 转发 7 · 回复 33 · 浏览 13464</p>
<p class="archive-item-content">补充一点，除了 Opus 5.5 调度，还可以充分利用 advisor，让 Fable 当 Advisor 给 Opus 当顾问<br>
GPT 6.1 Sol 干杂活其实挺不错的</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2111082519777194281">@op7418: 大家都不傻，都预料到了 iPhone Duo 的火爆。 今天真是人人都在抢 iPhone 12，就连刚才播客录影棚的两个工作人员小哥也都在抢，居然还抢到了。 现在抢到第一批，基本上就起飞了</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月16日 13:11 UTC · 喜欢 33 · 转发 0 · 回复 29 · 浏览 47114</p>
<p class="archive-item-content">大家都不傻，都预料到了 iPhone Duo 的火爆。<br>
<br>
今天真是人人都在抢 iPhone 12，就连刚才播客录影棚的两个工作人员小哥也都在抢，居然还抢到了。<br>
<br>
现在抢到第一批，基本上就起飞了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/johnternus/status/2111056309172740346">@johnternus: iPhone Duo… a whole new way to iPhone. Pre-orders start today. https://t.co/yh0Ow1Vj74</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月16日 11:27 UTC · 喜欢 22364 · 转发 1358 · 回复 924 · 浏览 919033</p>
<p class="archive-item-content">iPhone Duo… a whole new way to iPhone. Pre-orders start today. https://t.co/yh0Ow1Vj74</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/bozhou_ai/status/2110995015812231484">@bozhou_ai: 刚刚有个朋友问我：没有 AI 的时候，写代码不得写死了？当初是怎么写出来的？ 我说那时候真的是纯手敲，唯一借助的就是自动补全。 但现在回想，那时候特别容易进入心流。一坐下去，不知不觉一天...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 07:23 UTC · 喜欢 67 · 转发 3 · 回复 37 · 浏览 19404</p>
<p class="archive-item-content">刚刚有个朋友问我：没有 AI 的时候，写代码不得写死了？当初是怎么写出来的？<br>
<br>
我说那时候真的是纯手敲，唯一借助的就是自动补全。<br>
<br>
但现在回想，那时候特别容易进入心流。一坐下去，不知不觉一天就过去了，写了几千行代码。<br>
<br>
现在完全没有这种感觉了。布置一个任务，注意力就跑去干别的；要改的时候再切回来，脑子得重新装一遍上下文，切换成本极高。<br>
<br>
可算下来，我这一年写的代码，已经超过过去十年加起来的总量了。<br>
<br>
只是那种写到忘记时间的一天，已经很久没有过了。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2110987435874431392">@op7418: 马斯克在八年前就说这过这个设想 当时评论区很多人觉得他在开玩笑 https://t.co/fsyvNacm6b</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月16日 06:53 UTC · 喜欢 456 · 转发 38 · 回复 62 · 浏览 38886</p>
<p class="archive-item-content">马斯克在八年前就说这过这个设想<br>
<br>
当时评论区很多人觉得他在开玩笑 https://t.co/fsyvNacm6b</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110919336147796377">@dotey: 特斯拉新 Roadster 发布：靠压缩空气喷气在空中翻正落地，马斯克说 2028 年投产，售价未公布 10 月 15 日晚，特斯拉在得州 SpaceX 的 McGregor 试验场直播...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月16日 02:22 UTC · 喜欢 313 · 转发 36 · 回复 89 · 浏览 123131</p>
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
<p class="source-line">Twitter/X · @op7418 · 10月16日 01:57 UTC · 喜欢 301 · 转发 18 · 回复 128 · 浏览 133765</p>
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
<p class="source-line">Twitter/X · @dotey · 10月16日 01:12 UTC · 喜欢 19401 · 转发 2092 · 回复 598 · 浏览 11197002</p>
<p class="archive-item-content">HOLY SHIT https://t.co/4Q6rs8nfvM</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2110877554945175677">@dotey: Antigravity 向付费 Google AI Pro 用户开放 Gemini 4 Argon，Argon 有单独的每周额度，不占 3.8 Flash 额度 Google 的 AI...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月15日 23:36 UTC · 喜欢 127 · 转发 8 · 回复 122 · 浏览 49142</p>
<p class="archive-item-content">Antigravity 向付费 Google AI Pro 用户开放 Gemini 4 Argon，Argon 有单独的每周额度，不占 3.8 Flash 额度<br>
<br>
Google 的 AI 编程工具 Antigravity 今天开始向付费的 Google AI Pro 订阅用户推出 Gemini 4 Argon。官方模型页写明只限正式付费的 Pro，试用期的 Pro 用不了，免费用户和 Google AI Plus 用户也不在范围内。能用的地方是 Antigravity 桌面 App、命令行工具 CLI 和 IDE 扩展（装在 VS Code、JetBrains 等编辑器里的插件），Antigravity IDE 里暂时选不到。目前在逐步推送，官方建议先更新到最新版。<br>
<br>
Pro 用户用 Argon 有一份单独的额度，只按周计算，不像原有额度那样每 5 小时刷新一次；它和原来给 Gemini 3.8 Flash 用的额度分开，用 Argon 不会吃掉 3.8 Flash 的额度。每周到底给多少、哪天重置，推文和官方文档都没写。文档对所有额度的说明是，消耗多少取决于智能体实际干了多少活，任务越复杂用得越快。<br>
<br>
官方模型说明：https://t.co/7IXduTeBzr</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2110984552743309530">Zara Zhang: Had a lot of fun making this Harry Potter style newspaper where the images can come alive: Th...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang：做这份图片能活起来的《哈利·波特》风格报纸非常有趣：Th...</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 10月16日 06:41 UTC · 喜欢 1 · 转发 0 · 回复 0</p>
<p class="archive-item-content">Zara Zhang shares a playful Harry Potter-style newspaper project where images come alive, without any technical explanation.</p>
<p class="archive-item-translation"><span>中文摘要</span>Zara Zhang 分享了一个有趣的《哈利·波特》风格报纸项目，其中的图片能够动起来，但未提供任何技术说明。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/levie/status/2110975373219688624">Aaron Levie: So in fact we actually can get robots, flying cars, superintelligence, fast internet on plane...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Aaron Levie：事实上，我们确实可以在有生之年得到机器人、飞行汽车、超级智能、飞机上的高速互联网……</p>
<p class="source-line">Follow Builders · X 动态 · Aaron Levie · 10月16日 06:05 UTC · 喜欢 193 · 转发 6 · 回复 18</p>
<p class="archive-item-content">Aaron Levie shares an optimistic vision that robots, flying cars, superintelligence, fast in-flight internet, space travel, orbital data centers, and unlimited energy could all arrive within our lifetimes.</p>
<p class="archive-item-translation"><span>中文摘要</span>Aaron Levie 分享了一个乐观看法的愿景：机器人、飞行汽车、超级智能、机上高速互联网、太空旅行、轨道数据中心和无限能源都可能在我们有生之年实现。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2110971985417441512">Thibault Sottiaux: Either we are out of ideas or we are cooking. Time will tell</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：要么我们江郎才尽，要么我们正在憋大招。时间会给出答案</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月16日 05:51 UTC · 喜欢 2774 · 转发 68 · 回复 899</p>
<p class="archive-item-content">OpenAI 团队成员 Thibault Sottiaux 发出一条含糊暗示性推文，称团队要么已无新想法、要么正在酝酿大动作，引发大量猜测性讨论。</p>
<p class="archive-item-translation"><span>中文摘要</span>OpenAI 团队成员 Thibault Sottiaux 发出一条含糊的暗示性推文，称团队要么已无想法、要么正在酝酿大动作，引发大量猜测性讨论。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2110957024934858815">Guillermo Rauch: TLDR we got Vercel zeppelin and flying cars before GTA6 https://t.co/F9RpBIZZ9f</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：简而言之，我们在 GTA6 之前就有了 Vercel 飞艇和飞行汽车</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 10月16日 04:52 UTC · 喜欢 307 · 转发 6 · 回复 28</p>
<p class="archive-item-content">Guillermo Rauch posts a joking tweet claiming &#x27;Vercel zeppelin and flying cars&#x27; arrived before GTA6, with no technical substance.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 发推调侃称“Vercel 飞艇和飞行汽车”都比 GTA6 先到来，内容不含任何技术实质。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2110953030200005037">Zara Zhang: Here https://t.co/eGnilcXh9Q https://t.co/PziWcUIhFV</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang：这里 https://t.co/eGnilcXh9Q https://t.co/PziWcUIhFV</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 10月16日 04:36 UTC · 喜欢 21 · 转发 1 · 回复 2</p>
<p class="archive-item-content">A bare tweet from Zara Zhang containing only two shortened links with no explanatory text or technical substance.</p>
<p class="archive-item-translation"><span>中文摘要</span>Zara Zhang 发布的一条仅含两个短链接、没有任何说明文字或技术内容的简单推文。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2110905682610598310">Guillermo Rauch: 🤯 https://t.co/jD344QxR5i</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：🤯 https://t.co/jD344QxR5i</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 10月16日 01:28 UTC · 喜欢 1438 · 转发 27 · 回复 21</p>
<p class="archive-item-content">A content-free tweet from Guillermo Rauch consisting solely of an emoji and a shortened link.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 发布的一条仅含一个表情符号和一个短链接、没有任何实质内容的推文。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2110888020572611010">Guillermo Rauch: What a SHIP! https://t.co/zrWRBLkhUY</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：这波发布太赞了！https://t.co/zrWRBLkhUY</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 10月16日 00:18 UTC · 喜欢 931 · 转发 8 · 回复 37</p>
<p class="archive-item-content">Guillermo Rauch tweeted a short teaser (&quot;What a SHIP!&quot;) linking to an unspecified release, with no accompanying technical detail or context.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 发布了一条简短的预告推文（“这波发布太赞了！”）并附带一个未说明内容的链接，未提供任何技术细节或背景信息。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2110883805506711694">Peter Yang: @Fourthwall @dubbaumann @bot monitor all replies to this thread and let me know the winner in...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：@Fourthwall @dubbaumann @bot 监控此帖的所有回复，并在……告诉我获胜者</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 10月16日 00:01 UTC · 喜欢 3 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A tweet from Peter Yang asking bots to monitor replies to the thread and report the winner in 12 hours.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 发帖让机器人监控该帖的所有回复，并在 12 小时后告知获胜者。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2110882343955411299">Peter Yang: Fwiw here&#x27;s a sample t-shirt we ordered from @Fourthwall with her penguin design. Thanks @dub...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：顺便说一句，这是我们通过 @Fourthwall 订购的一件采用她企鹅设计的样品 T 恤。感谢 @dub……</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 10月15日 23:55 UTC · 喜欢 2 · 转发 0 · 回复 2</p>
<p class="archive-item-content">Peter Yang shares a sample t-shirt ordered from Fourthwall featuring a penguin design, thanking a platform builder.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 分享了一件从 Fourthwall 订购的带有企鹅设计的样品 T 恤，并感谢平台构建者。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2110882341812134186">Peter Yang: My 8-year-old and I are looking for feedback: If you&#x27;re a parent, which of her T-shirt design...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：我和我 8 岁的女儿想征求反馈：如果你是家长，她的哪款 T 恤设计……</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 10月15日 23:55 UTC · 喜欢 16 · 转发 0 · 回复 25</p>
<p class="archive-item-content">A parent asks followers which of their 8-year-old&#x27;s T-shirt designs they would buy for their kids.</p>
<p class="archive-item-translation"><span>中文摘要</span>一位家长向关注者询问，他们会为自家孩子购买其 8 岁女儿设计的哪一款 T 恤。</p>
</article>
</div>
</section>
