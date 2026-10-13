---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 46 条内容中筛选出 16 条重要资讯。

---

1. [AlphaProof Nexus 攻克 9 个 Erdős 未解问题并通过同行评审](#item-1) ⭐️ 8.65/10
2. [黑客远程触发欧洲超市冰箱自动除霜](#item-2) ⭐️ 8.0/10
3. [将 WiFi 7 路由器改装成 320Msps 软件无线电接收器](#item-3) ⭐️ 8.0/10
4. [Python 3.15 发布：引入惰性导入，告别 3.10](#item-4) ⭐️ 8.0/10
5. [微软发布 Maia 300 自研芯片，将 Maia 推理规模扩展至多吉瓦级部署](#item-5) ⭐️ 7.62/10
6. [AWS 提出 Priming 方法，将预训练 Transformer 改造成混合状态空间模型](#item-6) ⭐️ 7.53/10
7. [Meta Muse Wonder 系列上线 Agent Arena，评分即将公布](#item-7) ⭐️ 7.5/10
8. [Codex CLI 默认后台守护进程引发磁盘问题；可用配置开关禁用](#item-8) ⭐️ 7.3/10
9. [Epic Games 转向 AI 先行开发，迪士尼射击游戏无限期延期](#item-9) ⭐️ 7.15/10
10. [QGIS 通过 QEP428 禁止 AI 辅助贡献](#item-10) ⭐️ 7.15/10
11. [Z.ai 推出 GLM-Legal，面向法律工作的智能体模型](#item-11) ⭐️ 7.0/10
12. [Simon Willison 发布 web-edit 0.1a0：基于 Tailscale 的 AI 辅助文件编辑器](#item-12) ⭐️ 7.0/10
13. [Cursor 并入 X 订阅：老用户应保留原计划](#item-13) ⭐️ 7.0/10
14. [智能体经济学：AI 原生公司如何管理 AI 员工](#item-14) ⭐️ 7.0/10
15. [创作者结合 Anatomy 技能、Grok 和即梦制作芯片制造科普视频](#item-15) ⭐️ 7.0/10
16. [Opus 5.5 + 即梦 CLI：AI 全权编排的故事片创作](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AlphaProof Nexus 攻克 9 个 Erdős 未解问题并通过同行评审](https://the-decoder.com/google-deepminds-alphaproof-nexus-solved-dozens-of-open-math-problems-and-actually-got-peer-reviewed/) ⭐️ 8.65/10

Google DeepMind 的 AlphaProof Nexus 独立解决了 353 个 Erdős 未解问题中的 9 个，其中 2 个已悬置 56 年。相关成果发表在《Science》期刊上并通过了同行评审，这是 AI 生成的数学解法罕见地获得正式学术验证。 这标志着 AI 在产出符合严格学术标准的原创数学成果方面迈出了重要一步，可能重塑数学家与 AI 研究者的协作方式。同时，此举也对应了一场激烈争论——一些 AI 实验室不经期刊评审直接发布证明，而 DeepMind 选择走传统同行评审路线以赢得学界认可。 AlphaProof Nexus 以 Gemini 3.1 Pro 为核心，负责用形式化语言 Lean 起草和修订证明；Lean 在每次编辑后都会检查草稿，其错误信息会引导下一步尝试。对于较难的子问题，它可以调用专门的证明工具 AlphaProof，不过即使不借助它也能解决那 9 个 Erdős 问题；此外它还证明了 44 个 OEIS 猜想、解决了一个代数几何的开放问题，并改进了 min-max 优化中的一个已知界限。

aihot · The Decoder：AI News（RSS） · 10月12日 09:35 · [中文阅读](https://aihot.news/items/wzxf68r0rchangmvwm48qqhfk)

**核验**: 多源印证

**背景**: Erdős 问题是多产的匈牙利数学家 Paul Erdős（1913–1996）提出的数学猜想，许多附有奖金，涉及离散数学、图论、数论及相关领域。Lean 是一个开源证明助手和函数式编程语言，可对证明进行形式化验证，从而实现机器可检查的数学正确性。OEIS（在线整数序列百科全书）是专业和业余数学家广泛引用的整数序列在线数据库。这些背景之所以重要，是因为形式化验证正是 AI 生成的证明可被检查并令人信赖的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Erdős_problems">Erdős problems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant)</a></li>
<li><a href="https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences">On-Line Encyclopedia of Integer Sequences - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 这一成果正逢 AI 数学领域争论激烈之际。OpenAI 近期将数百个 AI 证明直接上传到 GitHub 而非投稿期刊，引发由 Terence Tao 领导的 Association for Human Mathematics 呼吁抵制。DeepMind 选择将成果送交同行评审，被视为是刻意争取数学界认可的举措。

**标签**: `#AI`, `#数学`, `#DeepMind`, `#AlphaProof`, `#研究突破`

---

<a id="item-2"></a>
## [黑客远程触发欧洲超市冰箱自动除霜](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

2026 年 10 月，黑客远程激活了欧洲多家超市冰箱的自动除霜功能，扰乱门店运营，并影响了物流配送和商品价格。该事件针对的是老旧的物联网制冷控制器，很可能是存在已知漏洞的丹佛斯（Danfoss）型号。 此次攻击表明，关键零售基础设施中的物联网设备一旦被攻破，可能造成实际的运营和经济损失。它凸显了制造商和零售商必须紧急修复仍广泛使用的老旧制冷控制器中安全漏洞的迫切性。 安全研究机构 Claroty 在 Danfoss AK-SM 800A 控制器平台及类似的 Copeland 系统中发现了多个漏洞，攻击者可借此物理操控制冷系统。受影响的旧控制器如 Danfoss SM800（2021 年停产）和 SC355（2016 年停产）已不再获得安全更新，但仍在使用中。

hackernews · Zeekaas · 10月12日 12:16 · [社区讨论](https://news.ycombinator.com/item?id=50055304)

**核验**: 多源印证

**背景**: 许多超市的制冷系统采用接入互联网的监控控制器，用于远程诊断、效率监测以及自动除霜等操作。虽然这些物联网功能降低了服务成本，但也扩大了攻击面。Claroty 的研究表明，此类控制器中的严重漏洞可让攻击者通过禁用冷却或强制除霜循环，悄无声息地破坏存储的食品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers">Freeze the Controller , Defrost the Food: Uncovering Vulnerabilities in...</a></li>
<li><a href="https://www.linkedin.com/pulse/week-refrigeration-top-stories-from-10-aug-16-2026-fpm3f">This Week in Refrigeration — Top Stories from 10 Aug – 16 Aug 2026...</a></li>
<li><a href="https://itwire.com/guest-articles/guest-research/chilling-discoveries-claroty-finds-multiple-security-vulnerabilities-in-danfoss-and-copeland-refrigeration-controllers">Chilling discoveries: Claroty finds multiple security vulnerabilities in...</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了可能的罪魁祸首，指出 Danfoss 的 CVE 漏洞，并提到 SM800 和 SC355 等旧控制器缺乏安全更新，容易成为攻击目标。一些人争论为何要将冰箱接入互联网，另一些人则举例类似依赖订阅的实验室设备，并提出这起事件可能与 2026 年 8 月美国军事基地冰箱遭攻击有关。

**标签**: `#cybersecurity`, `#IoT`, `#critical infrastructure`, `#vulnerability`, `#supply chain`

---

<a id="item-3"></a>
## [将 WiFi 7 路由器改装成 320Msps 软件无线电接收器](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 8.0/10

一位开发者展示了将 WiFi 7 路由器改装成软件无线电（SDR）接收器，采样率可达 320Msps，相关代码已发布在 GitHub 项目 w1700k-sdr 中。这一改造利用现成的 WiFi 7 硬件，以低成本实现了高性能的 SDR 功能。 这一创新大幅降低了高性能 SDR 的门槛，使业余爱好者和研究人员无需购买昂贵的专用硬件即可使用。它也展示了将消费级设备重新用于高级无线电应用的潜力，可能推动 SDR 社区的进一步发展。 该项目托管在 GitHub 仓库 h0m3us3r/w1700k-sdr 中，包含固件、主机和内核模块的代码。开发者此前曾利用 ESP32 Wi-Fi 微控制器构建 SDR，表明其善于利用常见 Wi-Fi 硬件进行 SDR 开发。

hackernews · djfergus · 10月12日 12:41 · [社区讨论](https://news.ycombinator.com/item?id=50055593)

**核验**: 多源印证

**背景**: 软件无线电（SDR）是一种无线电通信系统，其中传统上由模拟硬件（如混频器和滤波器）实现的组件，改为在计算机或嵌入式系统上通过软件实现。采样率以每秒样本数（SPS）衡量，决定了可捕获的带宽和频率范围；320Msps 表示每秒 3.2 亿个样本，能够接收宽带信号。WiFi 7 路由器包含先进的射频前端和 ADC，可被重新用于 SDR，为专用 SDR 硬件提供了经济高效的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sampling_(signal_processing)">Sampling (signal processing) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Undersampling">Undersampling - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，用户称赞开发者之前基于 ESP32 的 SDR 项目，并希望更多此类项目能在常见 Wi-Fi 网卡上实现。一些用户指出，相同的芯片组可能适用于其他设备，如 Banana Pi R4，还有人讨论扩展可能性，例如添加衰减器和混频器以覆盖更宽的频率范围。此外，有用户询问手机 FM 收音机限制是否与 SDR 能力有关。

**标签**: `#SDR`, `#WiFi 7`, `#Hardware Hacking`, `#Radio`, `#Open Source`

---

<a id="item-4"></a>
## [Python 3.15 发布：引入惰性导入，告别 3.10](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 正式发布，带来了显式惰性导入（PEP 810）和推导式中的解包语法（PEP 798）。西蒙·威利森指出这标志着 Python 3.10 支持的结束，也让项目可以开始使用 3.11 的特性。 此版本显著提升了启动性能与开发体验，尤其对命令行工具和依赖重的应用帮助很大。终止 Python 3.10 支持将促使整个生态系统升级，采用更快、更安全的代码。 显式惰性导入使用 `lazy import` 与 `lazy from` 语法，将模块加载推迟到符号首次被使用时。推导式中的解包，例如 `[*L for L in lists]`，将 PEP 448 的解包语法扩展至列表、集合和字典，可一步完成扁平化。

rss · Simon Willison · 10月12日 18:15

**核验**: 多源印证

**背景**: Python 每年发布一个新版本，新特性由 Python 增强提案（PEP）定义。显式惰性导入是一种可选择启用的方案，不同于被否决的隐式 PEP 690，它避免了级联惰性加载，并提供了细粒度的控制。推导式中的解包则是对 Python 3.5 引入的解包语法的泛化扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0810/">PEP 810 – Explicit lazy imports | peps .python.org</a></li>
<li><a href="https://socket.dev/blog/pep-810-proposes-explicit-lazy-imports-for-python-3-15">PEP 810 Proposes Explicit Lazy Imports for Python 3.15 - Soc...</a></li>
<li><a href="https://www.stork.ai/blog/pythons-3x-startup-trick-has-a-catch">Python Lazy Imports : Speed Up Startup Without Breaking... | Stork.AI</a></li>

</ul>
</details>

**标签**: `#Python`, `#版本发布`, `#PEP`, `#语言特性`, `#开发者工具`

---

<a id="item-5"></a>
## [微软发布 Maia 300 自研芯片，将 Maia 推理规模扩展至多吉瓦级部署](https://x.com/satyanadella/status/2109631106404487523) ⭐️ 7.62/10

微软发布了第三代自研 AI 芯片 Maia 300，其每瓦 token 产出比主流 GPU 系统高 40%。从下一个日历年（2027 年）起，微软将把 Maia 芯片家族扩展至多吉瓦级部署，使其成为自家产品和服务的主要推理系统，而 Maia 200 已在美国、欧洲和澳大利亚部署。 这是 AI 基础设施领域的重要里程碑，有助于降低微软在推理工作负载上对英伟达、AMD 等第三方芯片供应商的依赖。每瓦 token 能效的提升可直接降低推理成本和功耗，惠及微软的 Copilot、Teams 和 Azure 客户，也反映出行业向自研 AI 芯片发展的趋势。 Maia 300 针对长上下文推理、低延迟对话和多步骤智能体任务进行了优化，计划于 2027 年投入量产并部署。Maia 200 已投入生产环境，在 Teams 和 Copilot 场景中每瓦 token 产出最高提升 1.7 倍。

aihot · X：Satya Nadella (@satyanadella) · 10月12日 13:03 · [中文阅读](https://aihot.news/items/zqlqer8tnl7ejg2ow3xoq7b9q)

**核验**: 多源印证

**背景**: 微软一直在开发名为 Azure Maia 的自研 AI 加速器，以在 AI 推理工作负载上对标英伟达和 AMD 的 GPU。Maia 芯片家族旨在提供更好的能效（每瓦 token 产出），并与微软的软件栈进行全栈整合。'多吉瓦级部署'指所部署硬件的总功率容量，表明其达到数据中心级规模，使 Maia 成为微软的主要推理基座。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20261013A02S6000">微软发布Maia 300 AI芯片：自研算力落地 逐步降低英伟达依赖</a></li>
<li><a href="https://www.todayforai.com/zh/items/art-e2088e20-386">微软发布 Maia 300 自研 AI 芯片：主打推理能效提升 40%，2027 年量产...</a></li>
<li><a href="https://www.eet-china.com/news/202610139121.html">微软Maia 300自研AI芯片将投入量产，Maia家族扩展至吉瓦级部署 微软Ma...</a></li>

</ul>
</details>

**标签**: `#AI芯片`, `#微软`, `#AI基础设施`, `#推理部署`, `#Maia`

---

<a id="item-6"></a>
## [AWS 提出 Priming 方法，将预训练 Transformer 改造成混合状态空间模型](https://www.amazon.science/blog/can-we-change-an-ai-models-architecture-without-retraining-it-from-scratch) ⭐️ 7.53/10

AWS 研究人员提出了 ‘Priming’ 方法，该方法用预训练 Transformer 初始化混合状态空间模型，并使用不足源模型预训练 token 预算 0.5% 的量恢复下游质量。这一方法将预训练成本降低逾 99%，并相比从头训练混合模型可获得 2 倍的吞吐量提升。 Priming 将混合架构设计从预训练问题转变为知识迁移问题，大幅降低了大规模混合模型探索的计算门槛。这可以让更多研究者和开发者在没有巨额预算的情况下构建结合注意力与状态空间的高效模型，从而加速高效 AI 架构的创新进程。 该方法用高效的 SSM 层替换现成 Transformer 中的注意力层，然后通过简短的 alignment 和对齐训练阶段来恢复质量。它只需不到原始 token 预算的 0.5%，并让训练出的混合模型获得 2 倍的吞吐量提升。

aihot · Amazon Science（RSS） · 10月12日 17:36 · [中文阅读](https://aihot.news/items/w2408fxlrc7tc7nt3ivrzh9ys)

**核验**: 多源印证

**背景**: Transformer 依赖自注意力机制来捕捉上下文，其计算量随序列长度二次增长，非常消耗算力。状态空间模型（SSM）则以线性扩展的方式提供更高效的替代方案，而混合架构结合了注意力与 SSM 记忆，以获得更好的效率和性能。然而，从头训练这种混合模型成本极高，历史上限制了大规模探索；Priming 通过复用预训练 Transformer 权重避开了这一障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08301">[2605.08301] Priming: Hybrid State Space Models From Pre ... Priming: Hybrid State Space Models From Pre-trained Transformers Priming: Hybrid State Space Models From Pre-trained ... Priming: Hybrid State Space Models via Transformers [PDF] Priming: Hybrid State Space Models From Pre-trained ... GitHub - awslabs/hybrid-model-factory: Open-source toolkit ... Priming: Hybrid State Space Models From Pre ... - LinkedIn</a></li>
<li><a href="https://arxiv.org/pdf/2605.08301v1">Priming: Hybrid State Space Models From Pre-trained Transformers</a></li>

</ul>
</details>

**标签**: `#AI research`, `#efficient training`, `#state space models`, `#Transformers`, `#AWS`

---

<a id="item-7"></a>
## [Meta Muse Wonder 系列上线 Agent Arena，评分即将公布](https://x.com/arena/status/2109706854700044523) ⭐️ 7.5/10

Meta 已将 Muse Wonder 系列前沿模型上线 Agent Arena 平台，用户可以直接在真实世界的自主任务中实测这些模型。Muse Wonder 在 Agent Arena 上的官方评测分数即将公布。 这具有重要意义，因为 Muse Wonder 是 Meta 迄今最强能力的模型，专为智能体任务构建，将其上线公共社区评测平台能让用户直接与其它前沿模型对比。这标志着 Meta 认真参与智能体 AI 领域竞争的意图，而该领域的模型质量正日益以真实任务表现而非静态基准来衡量。 Muse Wonder 结合了 Active Memory 和 Active Focus 两种机制，用于跟踪用户关注的重点并努力实现目标。该模型通过 Meta 模型 API 和 Muse Code 提供，而能力更强的 Muse Wonder Full 则面向 Muse Code 订阅用户开放。

aihot · X：Arena (@arena) · 10月12日 18:04 · [中文阅读](https://aihot.news/items/lj23e9c9bhqwm2dee2hbgcmor) · 2 个来源

**核验**: 多源印证

**背景**: Agent Arena 是一个让自主 AI 智能体执行浏览、研究、编码等真实世界任务的平台，其排行榜基于超过 150 万次真实智能体会话构建。Muse Wonder 是 Meta 推出的新前沿智能体模型系列，被宣传为其迄今最强大的模型。该平台的公开对比让用户可以在实时实用任务中评估模型，而不只是依赖静态基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/muse-wonder">Muse Wonder | Meta AI Research</a></li>
<li><a href="https://about.fb.com/news/2026/10/introducing-muse-wonder-models/">Introducing Muse Wonder and Muse Wonder Full: Frontier Models ...</a></li>
<li><a href="https://arena.ai/leaderboard/agent">Agent Arena Leaderboard: AI Agent Rankings & Benchmarks</a></li>

</ul>
</details>

**社区讨论**: 评论区反应不一。有人欢迎此次发布，认为更多公司接近前沿可以防止权力极端集中并促成合作。但实测反馈并不热烈：有用户报告 Muse Wonder 在图像转 HTML 测试中表现远不如 Opus 5.5，更接近 Sonnet 或 Haiku；另有用户反映在 Meta 登录流程中看到其他人的个人资料，提出了安全担忧。

**标签**: `#AI agents`, `#Meta`, `#Agent Arena`, `#模型评测`, `#产品发布`

---

<a id="item-8"></a>
## [Codex CLI 默认后台守护进程引发磁盘问题；可用配置开关禁用](https://github.com/openai/codex/issues/48195) ⭐️ 7.3/10

OpenAI 的 Codex CLI 现在默认安装一个持久的、自更新的后台守护进程，导致大量磁盘占用和权限错误。社区发现，在 `~/.codex/config.toml` 的 `[features]` 下设置 `daemon_auto_start = false` 可禁用该自动启动行为。 这一默认行为影响了 AI 开发者工具用户的日常工作流，增加了隐藏的开销和脆弱性，可能中断编码会话。它还引发了关于 AI 编码工具设计的更广泛讨论，与 Claude Code 等工具进行了对比，并呼吁更简单、更透明的工具。 该守护进程因存储旧版本可能占用约 12 GB 磁盘空间，且自动更新可能随机损坏权限，例如让 `.git` 变为只读并阻塞任务。临时解决方案包括将 `~/.codex` 中的 pid/lock 文件符号链接到 `/dev/null`，并用 `chattr +i` 标记为不可变。

hackernews · whimblepop · 10月12日 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50060694) · [中文阅读](https://aihot.news/items/amjmxvrvj57q7752kgihp9p9q) · 2 个来源

**核验**: 多源印证

**背景**: Codex CLI 是 OpenAI 于 2025 年 4 月发布的终端编码代理，旨在让用户在终端中检查、编辑和运行代码。从 0.157 版本开始，守护进程自动启动成为稳定默认行为：首次启动时，Codex 会生成一个后台服务器（codex exec-server），TUI 连接至该服务器，通过保持服务器活跃来加快启动速度。这一变更引入了持久后台进程，许多用户对此感到意外并认为存在问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/codex/issues/48195">CLI: make `daemon_auto_start` opt-in — a persistent, self ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_CLI">Codex CLI - Wikipedia</a></li>
<li><a href="https://codex.danielvaughan.com/2026/09/25/codex-cli-daemon-auto-start-stable-default-v0157/">Daemon Auto-Start Is Now the Stable Default in Codex CLI v0 ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出了多个 bug，包括磁盘占用高达 12 GB 和权限损坏导致任务阻塞，这引发了用户对 Codex 可靠性的沮丧和不信任。一些用户推荐更简单的替代工具如 hax，也有人指出 Claude Code 采用类似的操作模型，另一些用户则提供了技术性临时解决方案，例如将 pid 文件符号链接到 /dev/null。

**标签**: `#Codex CLI`, `#AI developer tools`, `#bug report`, `#daemon`, `#OpenAI`

---

<a id="item-9"></a>
## [Epic Games 转向 AI 先行开发，迪士尼射击游戏无限期延期](https://arstechnica.com/gaming/2026/10/report-epic-games-goes-all-in-on-ai-for-disney-collaboration/) ⭐️ 7.15/10

Epic Games 正在为其与迪士尼 15 亿美元的合作项目转向"AI 先行"开发策略，由 Anthropic 的 Claude 等 AI 模型编写全部代码并指导全部美术。原定于 2027 年 3 月推出的漫威与星球大战主题射击游戏，已因这场 AI 相关的调整而被无限期延期。 这标志着生成式 AI 在大型游戏生产中最为激进的采用之一，可能会为工作室开发游戏的方式树立先例。如果成功，它将从根本上重塑开发团队结构——人类开发者负责管理 AI 生成的内容，而非亲手编写代码。 这项 15 亿美元的合作于 2024 年初宣布，Epic 于 2026 年 3 月以《堡垒之夜》参与度下滑为由裁员逾 1,000 人。一项针对 2,300 多名游戏行业从业者的调查显示，36% 的人使用生成式 AI 工具，但主要用于研究与头脑风暴（81%），而非代码辅助（47%）。

aihot · Ars Technica：AI（RSS） · 10月12日 20:59 · [中文阅读](https://aihot.news/items/kcwro19vl7dr5jgcjgec7mive)

**核验**: 多源印证

**背景**: AI 先行开发是一种开发模式，由生成式 AI 模型承担主要的创意与技术工作——例如编写代码和生成美术——而人类开发者负责管理、引导并打磨产出。Anthropic 的 Claude 是一系列专为编码、分析与内容生成设计的大语言模型。Epic Games 于 2024 年初与迪士尼达成 15 亿美元合作，打造一款包含漫威与星球大战角色的射击游戏，其 CEO Tim Sweeney 长期以来看好 AI 驱动的游戏开发，预测小团队可借助 AI 工具构建庞大的互动世界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/gaming/2026/10/report-epic-games-goes-all-in-on-ai-for-disney-collaboration/">Epic Games reportedly pivoting to “AI first” game development ...</a></li>
<li><a href="https://kotaku.com/epic-games-forces-shocked-developers-into-ai-first-mode-for-delayed-shooter-featuring-marvel-and-star-wars-characters-2000744620">Epic Games Forces Shocked Developers Into 'AI-First ... - Kotaku</a></li>
<li><a href="https://tech4gamers.com/epic-games-ai-generated-code-art/">Epic Games Transitioning Fully To AI-Generated Code And Art ...</a></li>

</ul>
</details>

**标签**: `#AI 开发`, `#Claude`, `#Epic Games`, `#AI 先行开发`, `#游戏开发`

---

<a id="item-10"></a>
## [QGIS 通过 QEP428 禁止 AI 辅助贡献](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/387) ⭐️ 7.15/10

QGIS 正式通过了 QEP428，将其 AI 政策改为严格“不允许”AI 辅助贡献。该提案由 nyalldawson 提交，并于 2026 年 10 月 7 日合并进 QGIS-Enhancement-Proposals 仓库。 这一由主要开源 GIS 项目做出的政策决定可能会影响其他项目采取类似限制，引发关于开源开发中 AI 使用的更广泛讨论。它直接影响依赖 AI 工具的贡献者和维护者，可能重塑贡献工作流程。 该政策适用于所有 AI 辅助贡献，包括代码、问题、评论和 PR，这在讨论中已明确。此前 QEP 处于“人在回路”政策下，要求人工监督，但现在已收紧为完全禁止。

aihot · Hacker News：AI 热帖 · 10月12日 11:22 · [中文阅读](https://aihot.news/items/t0gnehm6pcbj4xyn5f3txv1ge)

**核验**: 多源印证

**背景**: QGIS 是一款免费开源的地理信息系统（GIS）软件，支持 Windows、macOS 和 Linux。QEP（QGIS 增强提案）是用于向项目提出变更的正式文档，在合并前会在 QGIS 开发者邮件列表上进行讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/QGIS">QGIS - Wikipedia</a></li>
<li><a href="https://github.com/qgis/QGIS-Enhancement-Proposals">GitHub - qgis / QGIS - Enhancement -Proposals: QEP 's ( QGIS ...)</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一，PR 上有 88 个赞和 27 个踩。支持者如维护者 haubourg 认为 AI 贡献给维护者带来巨大压力，威胁自由软件社区依赖的人际网络；反对者可能担心这会扼杀创新或排斥使用 AI 工具的贡献者。

**标签**: `#QGIS`, `#AI policy`, `#open source`, `#AI-assisted development`, `#community governance`

---

<a id="item-11"></a>
## [Z.ai 推出 GLM-Legal，面向法律工作的智能体模型](https://z.ai/blog/glm-legal) ⭐️ 7.0/10

Z.ai 发布了 GLM-Legal，这是一个基于轻量级 GLM-5.3-Flash 架构、经扩大法律语料中期训练和后续训练的专业法律 AI 模型。在 Harvey LAB 基准测试中，它在 24 个实务领域取得了 19.2%的全程通过率，比基础模型提升了 12.5 个百分点。 此次发布标志着在监管严格的行业中，领域专用智能体 AI 日益流行的趋势，这类领域对准确性和可靠性要求极高。19.2%的全程通过率表明智能体法律工作仍难以完成端到端任务，凸显了人在回路监督在法律 AI 中的必要性。 GLM-Legal 面向真实的律所工作流程，Z.ai 将法律实务视为对模型推理和交付客户可用成果能力的极限测试。该模型的训练与测试框架同步迭代，使生产反馈转化为具体的工程损失信号。

hackernews · ilreb · 10月12日 16:11 · [社区讨论](https://news.ycombinator.com/item?id=50058507)

**核验**: 多源印证

**背景**: GLM-Legal 基于 Z.ai（原智谱 AI）的轻量级模型 GLM-5.3-Flash，通过扩大法律语料的中期训练和后续训练实现专业化。法律 AI 模型通过 Harvey LAB 和 LegalBench 等基准评估，这些基准模拟真实律所的工作任务。“全程通过”评分标准非常严格：只有端到端工作流的每一个步骤都成功才算通过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/glm-legal">GLM-Legal: Advancing Agentic Legal Intelligence</a></li>
<li><a href="https://www.unite.ai/z-ai-unveils-glm-legal-an-agentic-model-for-legal-workflows/">Z.ai Unveils GLM-Legal, an Agentic Model for Legal Workflows</a></li>
<li><a href="https://lexedge.ai/human-in-the-loop-legal-ai-practical-applications-and-limitations/">Human-in-the-loop legal AI: practical applications and ...</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一。Jedberg 建议基准测试应区分复用相同模板的任务，并分享了用 Claude 审查合同的正面经验。Fireflysentinel 提出隐私担忧，提到 Z.ai 过去曾在每次提示前对整个工作区进行快照的做法，质疑如何信任这样一家公司推出的法律产品。Victor9000 认为法律领域需要更好的工具，引用了 Anthropic 的人在回路政策；律师 otterley 对 20%的通过率不以为然，Eufrat 则斥责法律模型是不敬的，指出法律并非建立在固定的公理之上。

**标签**: `#AI`, `#legal-tech`, `#GLM-Legal`, `#privacy`, `#human-in-the-loop`

---

<a id="item-12"></a>
## [Simon Willison 发布 web-edit 0.1a0：基于 Tailscale 的 AI 辅助文件编辑器](https://simonwillison.net/2026/Oct/12/web-edit/) ⭐️ 7.0/10

Simon Willison 发布了 web-edit 0.1a0，这是一个 Python Web 应用，提供用于浏览和编辑文件夹内文件的网页界面，设计为通过 Tailscale 运行。该应用由 Codex 和 GPT-6 Astra Extra High 辅助构建，使得凭据无需经过 LLM 即可完成编辑。 这解决了 AI Agent 工作流中的一个真实痛点：编辑凭据等敏感文件时，无需让这些内容经过 LLM 往返传输。利用 AI 在 Tailscale 网络上构建小型个人 Web 工具的做法新颖且实用，可能为 AI 辅助的远程开发催生更安全的设计模式。 编辑器基于 CodeMirror 6 而非 Monaco，因为 Monaco 仍缺乏良好的移动端体验。预期的工作流程是让 Agent 启动该服务，然后 Simon 通过其 Tailscale 网络直接在手机上编辑文件；小于 2 MB 的图片会内联显示，并支持上传、新建、下载和删除等操作。

rss · Simon Willison · 10月12日 15:54

**核验**: 多源印证

**背景**: Tailscale 是一种软件定义的网状 VPN，可跨不同网络安全地连接设备和各项服务，让用户从任何地方访问自己的机器。Codex Remote 是一款允许用户从手机控制 OpenAI Codex 编程 Agent 的工具，而 GPT-6 Astra Extra High 是 OpenAI 的高推理级别模型配置之一。此次发布的场景是：Simon 通过 Codex Remote 在手机上处理项目时，想要编辑一个凭据文件，但又不希望将这些凭据暴露给 LLM 本身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/docs/concepts/what-is-tailscale">What is Tailscale ? · Tailscale Docs</a></li>
<li><a href="https://codexremote.io/">Codex Remote</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#developer tools`, `#Codex`, `#Tailscale`, `#web app`

---

<a id="item-13"></a>
## [Cursor 并入 X 订阅：老用户应保留原计划](https://x.com/dotey/status/2109804948611326229) ⭐️ 7.0/10

Cursor 已并入 The X Subscription，这是一个包含 X Premium、Grok 和 Cursor 的捆绑订阅，共五档，起价每月 8 美元。现有 Cursor 订阅用户可以选择保留原计划或切换，但新计划不再包含第三方模型额度，Claude、GPT 和 Gemini 的使用将按 API 价格单独计费。 这一变化对依赖 Claude 或 GPT 进行编码的 AI 开发者影响重大，因为切换到新计划可能会大幅增加成本。这也反映了 AI 工具与平台订阅捆绑的趋势，可能重塑开发者支付 AI 服务的方式。 新计划分为五档：免费版、Plus（8 美元）、Premium（30 美元）、Super（100 美元）和 Ultra（200 美元），用量分别为 Plus 的 4 倍、15 倍和 50 倍。第三方模型用量按 API 价格单独计费，用户可设置消费上限；Plus 档仅支持 Grok 模型。原计划（Pro 20 美元、Pro Plus 60 美元、Ultra 200 美元）保留双额度池系统，但定价页已不再提供新的 Pro 订阅，官方未说明原计划可保留多久或能否切回。

twitter · 宝玉 · 10月13日 00:34

**核验**: 多源印证

**背景**: Cursor 是一款基于 Visual Studio Code 构建的 AI 驱动代码编辑器，以其深度 AI 集成而闻名。The X Subscription 是 X（前 Twitter）推出的新捆绑订阅，整合了 X Premium、Grok（xAI 的 AI 助手）和 Cursor，此前 SpaceX 以 600 亿美元收购了 Cursor 母公司 Anysphere，xAI 也在 2 月并入 SpaceX。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/news/x-subscription">Introducing The X Subscription | SpaceXSI</a></li>
<li><a href="https://docs.x.ai/x-subscription/x-premium">X Premium Customers moving to The X Subscription</a></li>
<li><a href="https://www.infoq.cn/article/QlBwolS6TLQ36PaYGYf5">Cursor 2.0发布：自研代码模型 Composer 上线，8 个代理并行，速度提...</a></li>

</ul>
</details>

**标签**: `#X订阅`, `#Cursor`, `#Claude`, `#AI工具`, `#订阅定价`

---

<a id="item-14"></a>
## [智能体经济学：AI 原生公司如何管理 AI 员工](https://x.com/dongxi_nlp/status/2109769791418380787) ⭐️ 7.0/10

@dongxi_nlp 在推文中提出了面向 AI 原生公司的“智能体经济学”概念——这类公司的员工主要是 AI 智能体，并推荐了两篇论文：《面向自主科学发现的智能体经济学》和《递归自我改进的经济学》。推文提出了两个核心问题：更聪明的 AI 是否会让研发和产品迭代更快，以及如何在有限的时间和金钱下最优地管理 AI 智能体。 这之所以重要，是因为随着 AI 智能体变得越来越自主和强大，公司需要一套框架来理解 AI 驱动的研发如何加速产品周期，以及如何在智能体员工中高效分配资源。这与智能体 AI 应用的行业趋势以及自主系统经济学的新兴领域紧密相关，对 AI 开发者、研究者和企业管理者都具有参考价值。 该推文指出了 AI 原生公司的两个基本关切：AI 智能的提升是否能让研发速度和产品迭代更快，以及如何通过资源管理最大化效益。所引用的两篇论文分别探讨了自主科学发现场景下的智能体经济学，以及 AI 系统迭代设计更强大后继者的递归自我改进经济学。

twitter · Dongxi 东锡 NLP · 10月12日 22:14

**核验**: 多源印证

**背景**: 智能体经济学是一个新兴领域，研究自主 AI 智能体如何在市场和组织中与彼此及人类互动，包括由自主智能体驱动的经济体的金融基础设施。递归自我改进（RSI）指的是 AI 系统迭代地设计更强大的后继者的过程，这可能引发智能爆炸。麦肯锡等机构的行业分析指出，虽然单个 token 成本在下降，但企业对智能体 AI 的支出正在上升，智能体工作流的经济学既复杂有时又出乎意料地昂贵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/where-ai-agents-pay-off-a-practical-guide-to-the-economics-of-agentic-workflows">Measuring agentic AI ROI beyond token costs | McKinsey</a></li>
<li><a href="https://www.agentics-economics.org/en/">The Economic Operating System for Autonomous Agents</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#经济学`, `#自主科研`, `#递归自我改进`

---

<a id="item-15"></a>
## [创作者结合 Anatomy 技能、Grok 和即梦制作芯片制造科普视频](https://x.com/op7418/status/2109679880438989160) ⭐️ 7.0/10

@op7418 将本周爆火的 Anatomy Claude Code 技能与 Grok 机器人以及抖音旗下即梦 AI 相结合，制作了一支等轴立体风格、解释芯片制造流程的科普视频。这展示了一个串联多种 AI 工具进行科普内容创作的实际工作流。 这展示了一种创新的 AI 工具组合方式，能够快速产出精美的科普内容，显著降低了高质量科普视频的创作门槛。同时凸显了 AI 技能（Skill）生态的快速成长，这些能力正在将 Agent 的应用范围从文本扩展到视觉与交互式内容生成。 Anatomy 技能由 GitHub 用户 wheresryan22 开发，可将技术概念转化为详细的交互式等轴 SVG 图形，支持可选的 WebGL shader 和 3D 输出，不到一周就在 GitHub 上获得了三千多颗星。即梦（Dreamina）是字节跳动/抖音推出的文字生图、文字生视频 AI 平台。

twitter · 歸藏(guizang.ai) · 10月12日 16:17

**核验**: 多源印证

**背景**: Anatomy 是一个 Claude Code「技能」（Skill）——一种可复用的扩展，为 AI 代理提供超越基础对话的专门能力。它能把纯文字的技术描述转化为细节丰富、可交互的等轴立体插画，风格接近真实机器，带有活动部件和层次深度。即梦（Dreamina）是字节跳动旗下的 AI 内容生成平台，可将文字提示转换为图片和视频。将这些工具组合起来，创作者可以制作出以独特、统一的等轴艺术风格来讲解芯片制造等复杂流程的科普视频。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wheresryan22/anatomy">GitHub - wheresryan22/anatomy: A Claude Code skill that turns ...</a></li>
<li><a href="https://www.theblockbeats.info/flash/371351">Anatomy开源：一句话把技术原理变成会动的机器 - BlockBeats</a></li>
<li><a href="https://www.amassai.net/ai-tools/ai-image/jimengai/">即 梦 AI ：抖音AIGC创作 工 具 ，轻松生成图片视频</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#AI 产品设计`, `#自动化工作流`, `#科普视频`, `#开源AI工具`

---

<a id="item-16"></a>
## [Opus 5.5 + 即梦 CLI：AI 全权编排的故事片创作](https://x.com/op7418/status/2109515395749310821) ⭐️ 7.0/10

作者尝试将 Claude Opus 5.5 与即梦 CLI 结合，制作了一部短故事片，并表示效果出乎意料地好。Opus 5.5 负责全部创意决策——编排、视频特效、提示词和剪辑，而即梦 CLI 负责各分镜对应的图片与视频生成。 这展示了代理式创意工作流的实际应用：单一推理模型即可协调整个视频制作流程。它反映出 AI 工具正从独立生成器向可集成、由代理编排的工作流演进，能够大幅减少影视与内容制作中的人工操作。 作者指出，在视频上叠加大量用代码生成的动画效果，显著提升了画面质感。该工作流职责划分清晰——Opus 5.5 负责规划与创意决策，即梦 CLI 负责素材生成——使得整个流程模块化且可重复执行。

twitter · 歸藏(guizang.ai) · 10月12日 05:23

**核验**: 多源印证

**背景**: Claude Opus 5.5 是 Anthropic 的先进大语言模型，擅长推理、规划与编排任务。即梦 CLI 是一个命令行接口，让 AI 代理能以编程方式调用即梦的图像与视频生成能力。这种"推理模型负责规划编排、专用工具负责执行生成"的模式，反映了创意生产中代理式 AI 工作流的广泛趋势——AI 可负责从分镜到最终剪辑的整个环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/joeseesun/opus-video-prompts">GitHub - joeseesun/opus-video-prompts: Claude Opus 5.5 ...</a></li>
<li><a href="https://blog.cosine.ren/post/opus-5-5-motion-video-resources/">用 Opus 5.5 做视频：制作流程与提示词资源记录 | 笔记 / AI | 余弦の...</a></li>
<li><a href="https://aijustbetter.com/item/xmsumi.com-detail-2790">即 梦 CLI - AI Just Better</a></li>

</ul>
</details>

**标签**: `#AI视频生成`, `#Opus 5.5`, `#即梦CLI`, `#创意工作流`, `#AI代理`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="11"><span>其他追踪推文</span><span class="archive-tab-count">11</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="2"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">2</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2109814856102605240">@dotey: 今天 Codex 重置，重置将在太平洋标准时间当日结束前完成</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月13日 01:13 UTC · 喜欢 25 · 转发 3 · 回复 25 · 浏览 21193</p>
<p class="archive-item-content">今天 Codex 重置，重置将在太平洋标准时间当日结束前完成</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2109812216212099456">@thsottiaux: Day 8/ Reset</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月13日 01:03 UTC · 喜欢 6709 · 转发 387 · 回复 1101 · 浏览 469994</p>
<p class="archive-item-content">Day 8/ Reset</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2109808969292366010">@dotey: 现在我已经不好意思说：&quot;在无人关注的角落，Meta 也重置了&quot;，经 Muse 现在已经用户量也不小了😅</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月13日 00:50 UTC · 喜欢 23 · 转发 1 · 回复 21 · 浏览 9066</p>
<p class="archive-item-content">现在我已经不好意思说：&quot;在无人关注的角落，Meta 也重置了&quot;，经 Muse 现在已经用户量也不小了😅</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/SpaceXSI/status/2109783335296008414">@SpaceXSI: We&#x27;ve unified plans across Grok, Cursor, and X Premium. Introducing The X Subscription. https...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月12日 23:08 UTC · 喜欢 8442 · 转发 958 · 回复 730 · 浏览 1498996</p>
<p class="archive-item-content">We&#x27;ve unified plans across Grok, Cursor, and X Premium.<br>
<br>
Introducing The X Subscription. https://t.co/SvkrVvBa0p</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/alexandr_wang/status/2109774017574113780">@alexandr_wang: we have identified and fixed the issue that was causing the unusually fast quota usage for mu...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月12日 22:31 UTC · 喜欢 2747 · 转发 77 · 回复 170 · 浏览 115001</p>
<p class="archive-item-content">we have identified and fixed the issue that was causing the unusually fast quota usage for muse wonder and muse wonder full. you will now see much lower usage against your limits.<br>
<br>
also, as promised, now that we&#x27;ve fixed the issue...<br>
<br>
muse code reset!! https://t.co/j7cldu9ybo</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2109737617184936351">@dotey: 我觉得就应该做一些配套的 Codex、Claude Code 健身硬件，比如说推理强度和你的握力相关，你握力越大推理强度越高，这样你为了更高的推理强度就能使劲练习。</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月12日 20:06 UTC · 喜欢 34 · 转发 0 · 回复 29 · 浏览 7817</p>
<p class="archive-item-content">我觉得就应该做一些配套的 Codex、Claude Code 健身硬件，比如说推理强度和你的握力相关，你握力越大推理强度越高，这样你为了更高的推理强度就能使劲练习。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2109693353633927310">@op7418: 无人深空居然上线 iOS 端了</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月12日 17:11 UTC · 喜欢 7 · 转发 0 · 回复 3 · 浏览 6670</p>
<p class="archive-item-content">无人深空居然上线 iOS 端了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2109675087729492472">@op7418: 今天下午去了 Apple 孵化器的 Demo Day，见到了非常多不错的产品和开发者。 顺便没想到库克也来了，感谢苹果邀请。 就是这个合影，我感觉我又被广角镜头给坑了，怎么感觉如此肥大。...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月12日 15:58 UTC · 喜欢 50 · 转发 2 · 回复 16 · 浏览 13320</p>
<p class="archive-item-content">今天下午去了 Apple 孵化器的 Demo Day，见到了非常多不错的产品和开发者。<br>
<br>
顺便没想到库克也来了，感谢苹果邀请。<br>
<br>
就是这个合影，我感觉我又被广角镜头给坑了，怎么感觉如此肥大。 https://t.co/U8p9lQi4US</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/NoMansSky/status/2109645679651885469">@NoMansSky: iOS Deep Dive 🪐NMS on iPhone + iPad! 👉Rebuilt for Touch 🎮Controller Support 🖱️Mouse + Keys Su...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月12日 14:01 UTC · 喜欢 25771 · 转发 1860 · 回复 777 · 浏览 1828711</p>
<p class="archive-item-content">iOS Deep Dive<br>
<br>
🪐NMS on iPhone + iPad!<br>
👉Rebuilt for Touch<br>
🎮Controller Support<br>
🖱️Mouse + Keys Support<br>
😮iPhone 11 and up<br>
💰10 Years of Updates<br>
🕵️‍♀️4GB Download<br>
🚽Play Anywhere<br>
🌍The Whole Game<br>
🪄Metal FX<br>
🖥️M class support<br>
😍Console Graphics<br>
🦸Free to Try<br>
<br>
https://t.co/Uep0DOxzOo https://t.co/3A4EejZMD1</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/DashHuang/status/2109592494870774228">@DashHuang: 早上周会和同事们讨论了下 AGI 的话题。让 Cindy 帮忙把会议纪要整理成了一篇文章。 https://t.co/Qr1ijf8tdx</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月12日 10:30 UTC · 喜欢 143 · 转发 25 · 回复 36 · 浏览 28584</p>
<p class="archive-item-content">早上周会和同事们讨论了下 AGI 的话题。让 Cindy 帮忙把会议纪要整理成了一篇文章。 https://t.co/Qr1ijf8tdx</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/lijigang/status/2109576376378691953">@lijigang: 搞一个握力器，放在电脑旁边。 等 AI「thinking」的空档，拿起来开捏。 https://t.co/DWcVaLgr37</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月12日 09:26 UTC · 喜欢 35 · 转发 0 · 回复 39 · 浏览 11746</p>
<p class="archive-item-content">搞一个握力器，放在电脑旁边。<br>
<br>
等 AI「thinking」的空档，拿起来开捏。 https://t.co/DWcVaLgr37</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2109538550421262552">Nan Yu: Who’s gonna tell him https://t.co/QcAecsogbx</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>南宇：谁来告诉他</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 10月12日 06:55 UTC · 喜欢 0 · 转发 0 · 回复 0</p>
<p class="archive-item-content">A cryptic tweet asking who will inform someone, with no substantive information.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条隐晦的推文，询问谁去告知某人某事，没有实质内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2109483079106740500">Zara Zhang: The only place where I use Gemini these days is in Chrome</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang：如今我仅在 Chrome 中使用 Gemini</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 10月12日 03:15 UTC · 喜欢 93 · 转发 1 · 回复 57</p>
<p class="archive-item-content">Zara Zhang 表示如今只在 Chrome 中使用 Gemini。</p>
<p class="archive-item-translation"><span>中文摘要</span>Zara Zhang 表示目前只在 Chrome 浏览器中使用 Gemini。</p>
</article>
</div>
</section>
