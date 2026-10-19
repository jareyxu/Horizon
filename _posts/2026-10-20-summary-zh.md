---
layout: default
title: "Horizon Summary: 2026-10-20 (ZH)"
date: 2026-10-20
lang: zh
---

> 从 62 条内容中筛选出 8 条重要资讯。

---

1. [Ask HN：工程师热议如何交付自己看不懂的 AI 生成代码](#item-1) ⭐️ 8.0/10
2. [Numan 用 LangGraph 与 LangSmith 打造评测优先的 AI 健康教练 Nu](#item-2) ⭐️ 7.53/10
3. [美国国土安全部下令联邦文职机构移除 DeepSeek 及其衍生产品](#item-3) ⭐️ 7.38/10
4. [黑客用 AI 智能体入侵 100 多家网站，涉及 John Deere、SharkNinja](#item-4) ⭐️ 7.17/10
5. [Wine 成功移植到 OpenBSD，需绕过 %gs 与 SIGUSR1 限制](#item-5) ⭐️ 7.0/10
6. [Mac.apk 让 Android 应用在 Apple Silicon Mac 上原生运行](#item-6) ⭐️ 7.0/10
7. [报道称 Anthropic 正筹备能揣摩未言明意图的新模型](#item-7) ⭐️ 7.0/10
8. [@dotey 解读网易 LobsterAI 9 月《中国办公 Agent 用户行为报告》](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Ask HN：工程师热议如何交付自己看不懂的 AI 生成代码](https://news.ycombinator.com/item?id=50151036) ⭐️ 8.0/10

Hacker News 上一条 Ask HN 帖子引来约 321 条评论，起因是有人引用了一位 Meta 工程师在 LinkedIn 上的发言：如今写代码“感觉像一个黑盒”，因为 AI 辅助交付的新标准推进太快，逐行审查根本不现实。评论者随后给出了具体做法，主张由人掌握设计与抽象的所有权，只把实现工作交给 LLM。 这是一线工程师围绕 AI 辅助软件工程中一个真实新问题的辩论：如果“交付自己看不懂的代码”成为常态，调试、故障响应、新人交接和长期维护都会变得更困难；但如果坚持逐行审查，又会抵消编程代理带来的生产力收益。团队如何化解这一矛盾，将直接影响代码评审文化、代码所有权模式以及资深工程师判断力的价值。 评论者给出的是具体的心智模型而非泛泛之谈：bitwizeshift 表示自己完全不让 LLM 参与设计，而是先在 UML 层面确定抽象与角色的完整层级，再让 LLM 只填充实现空隙，这样他依然清楚代码如何运作；jedberg 则用“Principal Engineer 类比”来解释——如今人人都负责设计，AI 扮演按细节实现的初级工程师；tptacek 则把精力投入代码理解工具，用 tree-sitter 和 SCIP 做了一套原生 SwiftUI 只读前端来替代 GitHub 的 PR 查看器。

hackernews · rzk · 10月19日 11:24

**核验**: 多源印证

**背景**: 编程代理和基于 LLM 的助手如今能凭简短提示生成大量可运行代码，当人几乎不检查输出时，这种做法常被称作“vibe coding”。传统软件工程假定作者理解自己交付的系统，而代码评审的作用是发现缺陷并在团队内传播知识。评论者提到的工具包括 tree-sitter——一个为源代码构建语法树的解析库，以及 SCIP——一种用于交叉引用与代码导航的代码索引标准，它们可以作为加速理解代码的构件。这条讨论的核心问题是：当实现越来越多地由模型完成时，人该如何保持对代码库的理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apideck.com/blog/ai-agents-explained-everything-you-need-to-know-in-2025">AI Agents Explained : Everything You Need to Know in 2026</a></li>
<li><a href="https://codeaholicguy.com/2026/01/31/ai-coding-agents-explained-rules-commands-skills-mcp-hooks/">AI Coding Agents : Skills vs Commands vs Plugins vs Hooks Explained</a></li>
<li><a href="https://medium.com/codetodeploy/agentic-systems-without-the-hype-when-multi-step-llm-workflows-actually-improve-software-e1492ebdfacf">Agentic Systems Without the Hype: When Multi-Step LLM Workflows ...</a></li>

</ul>
</details>

**社区讨论**: 整体氛围是积极参与但远未形成共识，有评论者还称赞这类帖子“答案五花八门”。一个反复出现的共识是：人应当掌握设计与抽象层，LLM 只负责实现，具体体现为“人做设计、LLM 做实现”的工作流和 Principal Engineer 类比。也有尖锐质疑：joaquieneCnix 直接挑战前提，反问 Meta 工程师如果连自己没写的代码都没时间检查，那他们到底还额外交付了多少代码，并指出可能出现数万行没有注释的代码的风险；也有人像 tptacek 那样，把这个难题转化为构建更好的代码理解工具的动力。

**标签**: `#AI coding agents`, `#software engineering`, `#code review`, `#developer productivity`, `#LLM workflows`

---

<a id="item-2"></a>
## [Numan 用 LangGraph 与 LangSmith 打造评测优先的 AI 健康教练 Nu](https://www.langchain.com/blog/how-numan-built-an-eval-first-ai-health-coach-with-langgraph-and-langsmith) ⭐️ 7.53/10

英国数字健康公司 Numan 发布复盘文章，介绍其 AI 健康教练 Nu 如何基于 LangGraph 和 LangSmith 构建“评测优先”的框架：放弃单轮静态测试样例和预先写死的多轮脚本对话，改为按类别打分的主题数据集、由更廉价模型扮演患者的模拟对话层，以及能够自动阻断发布的安全回归门禁。该团队的核心结论是：真正稀缺的资产不是提示词，而是评测标准本身。 这一案例研究提出：在 AI 智能体开发中，真正难以复制、构成护城河的资产是评测标准而非提示词，这重新定义了团队应当投入工程资源的方向。它对医疗、金融、法律等强监管领域的开发者尤其有参考价值——这些场景中的智能体既要守住严格边界，又要维持自然的多轮对话体验。 文章记录了两个促成重构的具体失败模式：一是基于静态样例的单轮评测用整个数据集的单一平均分掩盖了局部失败（有时还会把正确的教练行为误判为失败，因为评分规则要求在仅两轮对话内同时体现共情、探索和建议）；二是脚本化的多轮对话会忽略智能体实际说了什么，一旦 Nu 给出脚本未预期的回复，后续每一轮都在回应一场从未发生过的对话。另有一些行为仍可从单条回复中判定，例如主管模型是否路由到了正确的专科子智能体、用药问题是否得到安全回答、安全护栏是否被正确触发，这些由覆盖教练质量、安全、用药提问、路由和摘要的主题数据集来评测。

aihot · LangChain：Blog（RSS） · 10月19日 15:00 · [中文阅读](https://aihot.news/items/nk19eo4eud45d47tmwxm684iu)

**核验**: 多源印证

**背景**: Numan 是一家英国数字健康公司，其患者通过应用管理体重、激素和性健康等长期病症，Nu 则是嵌入在该日常使用应用中的 AI 健康教练。LangGraph 是 LangChain 团队推出的开源低层编排框架，用于以图的方式构建有状态、多角色的智能体；LangSmith 则是 LangChain 的框架无关平台，用于大模型应用的追踪、调试、测试、评测与监控；Nu 本身就是一个 LangGraph 图，由主管模型编排并向各领域专科子智能体分发任务。由于 Numan 处于高度监管的医疗领域，该智能体必须提供高质量的健康教练服务，同时不得越界进行诊断、开处方或做出临床决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/LangGraph">LangGraph</a></li>
<li><a href="https://grokipedia.com/page/LangSmith">LangSmith</a></li>
<li><a href="https://www.langchain.com/langsmith-platform">LangSmith: AI Agent & LLM Observability and Evals Platform</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM evals`, `#LangGraph`, `#LangSmith`, `#AI product design`

---

<a id="item-3"></a>
## [美国国土安全部下令联邦文职机构移除 DeepSeek 及其衍生产品](https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/) ⭐️ 7.38/10

美国国土安全部发布 2026-01 号命令，由国土安全部长 Markwayne Mullin 签署、日期为 2026 年 7 月 24 日，要求所有联邦行政分支文职机构立即停止采购杭州深度求索人工智能公司及其关联方的产品，并立即从机构 IT 系统中移除 DeepSeek 产品以及“使用 DeepSeek 实现所开发的第三方产品与服务”。该通知依据 2018 年《联邦采购供应链安全法》提交，案卷号为 DHS-2026-0628，在被隐匿数月后于 2026 年 10 月 20 日（星期二）刊登于《联邦公报》。 由于 DeepSeek 以开放权重形式发布模型，这些模型可能被嵌入第三方工具与服务之中，因此该命令迫使各机构——以及向政府供货的厂商——去审计整条模型供应链，而不是简单地删除某个应用。它为将开放权重 AI 模型视为受监管的供应链组件树立了重要先例，并将对企业采用、采购规则以及任何悄悄内置 DeepSeek 模型的开发者工具产生连锁影响。 该命令并未列举具体涉及哪些产品，也没有说明各机构应如何处理运行在美国公司服务器上的 DeepSeek 模型，因而留下相当大的合规模糊空间。它适用于文职机构，但不包括其国家安全系统和安全隔离信息系统的部分，那些归五角大楼和国家情报总监管辖；此外，命令发布仅数天前，DeepSeek 刚更新了其低价 Flash 模型，该公司称其在部分编程任务上超过了 Claude Opus 5。

aihot · Hacker News：AI 热帖 · 10月19日 15:05 · [中文阅读](https://aihot.news/items/p04w1xjk7v6fmlskpf5vsnuka)

**核验**: 多源印证

**背景**: DeepSeek 是一家中国 AI 实验室，以发布开放权重大语言模型而闻名，尤其是 2025 年 1 月推出的 DeepSeek-R1，它成为下载量极高的应用，并以远低的成本展现出可与美国领先模型竞争的能力。2018 年《联邦采购供应链安全法》设立了联邦采购安全委员会，并授权美国政府将存在风险的 IT、电信及其他产品排除在联邦采购之外，并下令将其移除。与传统的封禁应用不同，开放权重模型可以被下载并在其他软件中再分发，这正是该命令第二款将适用范围延伸至基于 DeepSeek 实现所构建的第三方产品的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(AI)">DeepSeek (AI) - Wikipedia</a></li>
<li><a href="https://www.congress.gov/115/bills/s3085/BILLS-115s3085es.pdf">AN ACT</a></li>
<li><a href="https://www.cbo.gov/publication/54844">S. 3085, Federal Acquisition Supply Chain Security Act of 2018</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#DeepSeek`, `#tech policy`, `#open-source AI`, `#supply chain security`

---

<a id="item-4"></a>
## [黑客用 AI 智能体入侵 100 多家网站，涉及 John Deere、SharkNinja](https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins) ⭐️ 7.17/10

AI 安全公司 Norforge 发现，一名黑客通过开源平台 Cairn 编排了一批基本自主行动的 AI 智能体，入侵了 100 多个网站，据 Reuters 报道受害者包括 John Deere、SharkNinja 和 Cummins。Norforge 共识别出 20 多个它认为“疑似恶意”的公开 Cairn 实例，并称那名最活跃的攻击者每次成功入侵大约耗时 23 小时。 这是最早被记录的典型案例之一：开源 AI 智能体平台被改造成可大规模实施真实入侵的工具，人类介入极少，说明 agentic AI 同时降低了攻击者的技术门槛和人力成本。这也意味着防守方今后不仅要盯住被攻击的站点，还必须关注这些智能体编排平台本身的使用情况。 攻击者仅用不到 100 个汉字就写明了其“偏好的入侵战术”，指挥这些智能体所需的提示词之少令人瞩目；Cairn 的运作方式是让用户设定起点与最终目标，智能体在前行过程中自行记录进展。涉事公司均淡化了影响：John Deere 表示没有迹象显示敏感信息被访问，SharkNinja 称遭入侵的是一个独立的产品支持站点且威胁已被控制，Cummins 则表示正在调查其第三方供应商所运营网站受到的攻击。

aihot · The Verge：AI（RSS） · 10月19日 13:58 · [中文阅读](https://aihot.news/items/tdcasw4dwhyzne3hxo3dmizmz)

**核验**: 多源印证

**背景**: Cairn 是一个自称“通用问题求解引擎”的开源项目：用户提供起点和目标，它便会在未知的状态空间中搜索出一条可行路径，其开发者指出 AI 渗透测试正是已被验证的用途之一。所谓 agentic AI（智能体式 AI），是指把 AI 模型与自动化工作流、工具集成结合起来、能够自主完成多步任务的系统，如今攻防双方都在采用这种能力。由于 Cairn 实例可能对外公开并会自行记录执行进展，Norforge 这类安全研究团队正是通过阅读这些公开暴露的活动记录发现了这轮攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/oritera/Cairn">GitHub - oritera/Cairn: Cairn is a general-purpose AI state ...</a></li>
<li><a href="https://www.cisco.com/site/m/ai-workforce-consortium/agent-cybersecurity-impact.html">AI Agents and the Impact on Cybersecurity - Cisco</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#cybersecurity`, `#AI security`, `#hacking`, `#open-source AI`

---

<a id="item-5"></a>
## [Wine 成功移植到 OpenBSD，需绕过 %gs 与 SIGUSR1 限制](https://marc.info/?l=openbsd-ports&m=179236125692175) ⭐️ 7.0/10

Thomas Frohwein 于 2026 年 10 月 18 日在 openbsd-ports 邮件列表上提交了新的 emulators/wine 移植提案，把 Wine 这一 Windows 兼容层带到 OpenBSD 上。该移植需要一组仅适用于 OpenBSD 的补丁，尤其是 %gs 段寄存器桩代码和改用其他方式的 SIGUSR1 处理，作者在公告中对此做了详细说明。 让 Wine 这类深度依赖系统调用和 ABI 的复杂项目在安全加固的 BSD 上跑起来，是一项相当可观的系统编程成就，也为在 OpenBSD 上运行 Windows 应用和游戏打开了大门。这同时也是一次压力测试，暴露出 Wine 在多大程度上暗中依赖 Linux 专有行为，对上游项目而言是有价值的反馈。 OpenBSD 不允许用户态设置 %gs/gsbase，因此该移植改为模拟 %gs 前缀，而不是像 Linux 那样依赖寄存器被正确配置；SIGUSR1 仍可使用，但效率不如 Linux 上理想。作者为了简化开发，特意把所有 OpenBSD 专属改动都标记为仅限 OpenBSD，并因此对这些代码能否被上游合并持怀疑态度。

hackernews · iamnothere · 10月19日 13:35 · [社区讨论](https://news.ycombinator.com/item?id=50152307)

**核验**: 多源印证

**背景**: Wine（“Wine Is Not an Emulator”的缩写）是一个自由开源的兼容层，它通过把 Windows API 调用翻译成宿主系统的原生调用，让 Windows 应用程序能在类 Unix 系统上运行，而不是真的模拟 Windows，历来主要在 Linux、macOS 和 FreeBSD 上使用。OpenBSD 是一个以安全为核心的 BSD 系统，其 ports 与基础系统同步开发、同步发布，并对用户态能做什么设有严格限制。%gs 是 x86 的一个段寄存器，Windows 用它存放线程级数据结构；Linux 允许程序通过 arch_prctl 设置它，而 OpenBSD 不允许，这正是本次移植需要绕开的关键障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.adafruit.com/2026/10/19/wine-ported-to-openbsd/">Wine ported to OpenBSD - Adafruit Industries</a></li>
<li><a href="https://www.hotmolts.com/post/porting-wine-to-openbsd-made-wines-linux-only-assu-6bb14581-6b00-48ea-9e07-c81795fa88bf">Porting Wine to OpenBSD made Wine's Linux-only assumptions ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wine_(software)">Wine (software) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 该帖讨论热度很高（约 472 分、156 条评论），总体情绪偏正面，但评论质量参差不齐，其中夹杂着一些与主题无关的游戏实况视频垃圾链接。有评论者贴出后续邮件列表消息，引用作者本人对上游合并前景的怀疑；也有人表示欢迎，认为 OpenBSD 正逐渐成为“抵御 slopcode 的避难所”。还有人打趣说作者姓氏 Frohwein 在德语里意为“快乐的酒”，并调侃这个移植错过了改名叫“Port”的机会。

**标签**: `#OpenBSD`, `#Wine`, `#systems programming`, `#porting`, `#compatibility layer`

---

<a id="item-6"></a>
## [Mac.apk 让 Android 应用在 Apple Silicon Mac 上原生运行](https://github.com/kksimp/Mac.apk) ⭐️ 7.0/10

GitHub 用户 kksimp 发布的开源项目 Mac.apk，可以在 Apple Silicon Mac 上直接运行 Android 应用，既不需要模拟器，也不需要虚拟机，底层也没有 Linux 层。Android 应用会作为普通的 macOS 进程启动，通过 Mac 的 GPU 进行渲染，并在 CPU 上以原生速度执行。 多年来，在 Mac 上运行 Android 软件意味着必须接受笨重的模拟器、虚拟机或完整的 Linux 环境，这些都带来性能损耗和操作复杂度。如果一套轻量的兼容层就能完成这件事，说明基于 ARM64 的操作系统之间边界正变得越来越模糊，也可能为 Mac 用户——包括想使用 Android 独占应用的玩家——提供一条简单得多的途径。 关键技术前提是 Apple Silicon 与大多数 Android 手机同样采用 ARM64 架构，因此 CPU 指令可以直接执行，无需翻译转换。实际局限在于，许多流行的 Android 应用依赖 Google Play Services 及其他 Google 专有组件，而独立的兼容层并不提供这些内容，因此部分应用可能无法安装或会丧失关键功能。

hackernews · flocked · 10月19日 16:45 · [社区讨论](https://news.ycombinator.com/item?id=50154624)

**核验**: 多源印证

**背景**: Android 应用以 APK 包的形式分发，通常运行在手机内部的 Android 运行时和 Linux 内核之上。传统上，要让它们在桌面端运行，要么模拟一整台 Android 设备（由于需要翻译 CPU 架构而速度很慢），要么在虚拟机里跑一个完整的 Android 系统。Mac.apk 的做法是在 macOS 之上重新实现 Android 应用运行环境，思路与已经停止支持的 Android Runtime for Chrome 类似——后者曾让 Android 应用在 Chrome 浏览器中运行，直到 Google 终止支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/kksimp/Mac.apk">GitHub - kksimp/Mac.apk: Mac.apk: Run Android apps natively ...</a></li>
<li><a href="https://elsolitario.org/en/2026/10/19/mac-apk-android-on-apple-silicon-without-emulator/">Mac.apk on Apple Silicon: How It Works Without an Emulator</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对这个技术成就表示赞赏，但对其实际价值持怀疑态度，多人指出 Google Play Services 以及 Google 的封闭生态组件会限制哪些应用真正可用。有评论者将其与已经停止支持的 Android Runtime for Chrome 相提并论，也有人认为它对想与主机玩家一起玩《我的世界》基岩版的用户很有用；还有一条较长的讨论主线探讨 AI 辅助开发如何把过去需要企业级团队才能完成的工程，降低到“claude 帮我做一下”的程度，同时也有人抱怨 Claude 的文风已经变得令人厌烦地容易辨认。

**标签**: `#Android`, `#macOS`, `#Apple Silicon`, `#Open Source Tools`, `#AI-assisted Development`

---

<a id="item-7"></a>
## [报道称 Anthropic 正筹备能揣摩未言明意图的新模型](https://x.com/dotey/status/2112257496954135030) ⭐️ 7.0/10

科技媒体 The Information 于 10 月 19 日在其 AI Agenda 通讯中报道，Anthropic 正在筹备一款新模型，其推理能力和“直觉”强于目前对外提供的所有模型，消息来自一位使用过该模型的不具名人士，Anthropic 未公开回应。同一报道还提到，Google 正在开发 Gemini 4 Carbon，作为刚发布的 Gemini 4 Argon 的升级版；OpenAI 也在准备 Terra 系列新模型，可能几周内发布，能力更强且价格低于 GPT-6.1 Sol。 如果报道中的能力属实，这标志着模型从“回答明确指令”转向“推断背后真实目标”：普通用户可以更随意地写提示词，编程智能体也会主动扩大修改范围。结合 Google（Gemini 4 Carbon）和 OpenAI（Terra）的相关传闻，这说明前沿厂商的竞争焦点正从单纯的对话质量转向推理深度与智能体自主性。 报道举了两个例子：在修 bug 场景中，模型会顺藤摸瓜找出导致该 bug 的一整类问题，并询问是否一并修掉；在被问到怎么炒股时，它不会只给出“看看市盈率”这类通用建议，而是自行设计一套预测股价走势的算法——但报道并未说明这套算法到底预测得准不准。发布时间和命名都尚未确定：据原推 TestingCatalog 称新模型本月就会发布，但还不清楚它会归入 Anthropic 的 Fable 还是 Opus 系列。

twitter · 宝玉 · 10月19日 19:00

**核验**: 多源印证

**背景**: The Information 是一家订阅制科技媒体，其 AI Agenda 通讯经常依据不具名信源报道尚未发布的前沿模型，因此这类消息通常被视为可信传闻而非确认事实。Anthropic 的 Claude 模型按系列命名（例如 Opus，以及较新的 Fable 系列——被描述为面向自主知识工作和编程、拥有超大上下文窗口的前沿模型），这正是外界猜测新模型会归入哪一系列的原因。这里的“直觉”指的是仅凭很少的输入就推断出用户没说出口的意图，这比传统的指令跟随更进一步，对编程智能体尤其重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://the-decoder.com/googles-gemini-4-carbon-model-is-reportedly-matching-anthropics-opus-5-5-coding-performance/">Google's Gemini 4 "Carbon" model reportedly feels like ...</a></li>
<li><a href="https://tokenharbor.ai/models/gpt-6.1-sol">GPT - 6 . 1 Sol API — $2.00/1M in · Token Harbor</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#大模型`, `#AI模型发布`, `#行业动态`, `#AI开发者工具`

---

<a id="item-8"></a>
## [@dotey 解读网易 LobsterAI 9 月《中国办公 Agent 用户行为报告》](https://x.com/dotey/status/2112194237211029946) ⭐️ 7.0/10

网易 LobsterAI 发布了第二期《中国办公 Agent 用户行为报告》，并从这一期起改为每月发布，9 月版还额外统计了十一假期期间的使用变化。最醒目的两个数字是：9 月用户每次交给 Agent 的任务平均消耗 20.2 万 Token，是 3 月 6.3 万的 3.2 倍；日均活跃用户环比增幅达到 83.1%，是 5 月以来涨得最快的一个月。 这份报告提供了少数基于真实数据、可观察中国办公用户如何使用 AI Agent 的窗口，而其中的成本分析说明：对大量调用 Agent 的用户来说，模型的缓存折扣价比起命中率高出一两个点更影响账单——最省和最贵的配置实际费用相差七倍以上。这对任何构建 Agent 产品或做成本预算的人都有直接参考价值，因为 Agent 每一步都要重复读取同样的上下文，缓存经济性在很大程度上决定了最终费用。 9 月各模型的缓存命中率大多在九成上下（DeepSeek V4.1 Flash 最高 97.3%，Qwen 3.7 Plus 垫底 76.7%），但实际费用占原价的比例却从 DeepSeek V4.1 Flash 的 4.6% 到 GLM 5.3 Flash 的 35.1% 不等，差距主要来自缓存价：DeepSeek 只收 2%、Kimi K3 收 10%、Qwen 3.8 收 12.5%、GLM 5.3 系列收 25%–28.8%。报告明确说明数据仅来自自家平台，只公布增幅而非日活绝对数，厂商 Token 份额也只给了环比变化（智谱 GLM 约 +166.7%、MiniMax 约 -66.7%、Kimi 约 -78.6%）而没有绝对份额，因此不能当作整个行业的基准。

twitter · 宝玉 · 10月19日 14:48

**核验**: 多源印证

**背景**: LobsterAI 是网易（有道）推出的办公 Agent 产品，既可以在桌面端使用，也可以直接在微信、飞书这类聊天软件里给它派活，用户用自然语言交办任务，而不必操作传统应用界面。Token 是模型读写文字的计量单位，Agent 任务因为每一步都要反复读任务要求和自己前面的产出，所以消耗的 Token 远高于单轮对话。Prompt caching（提示缓存）是主流模型厂商提供的一项能力——Anthropic 于 2024 年 8 月为 Claude 率先推出——它把读过的内容缓存下来，再次读到时按折扣价收费，这正是缓存命中率和缓存价共同决定重度 Agent 用户真实成本的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/LobsterAI">LobsterAI</a></li>
<li><a href="https://grokipedia.com/page/Prompt_caching_Anthropic">Prompt caching (Anthropic)</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#办公 Agent`, `#用户行为报告`, `#prompt caching`, `#AI 产品设计`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="13"><span>其他追踪推文</span><span class="archive-tab-count">13</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="12"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">12</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2112277659959087314">@dotey: ChatGPT Slides 能多人一起改幻灯片了，Pro、Business 和企业版可用 OpenAI 给 ChatGPT 的幻灯片功能 ChatGPT Slides 加了两项新能力：...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月19日 20:20 UTC · 喜欢 10 · 转发 0 · 回复 12 · 浏览 3729</p>
<p class="archive-item-content">ChatGPT Slides 能多人一起改幻灯片了，Pro、Business 和企业版可用<br>
<br>
OpenAI 给 ChatGPT 的幻灯片功能 ChatGPT Slides 加了两项新能力：多人实时协作，以及直接在幻灯片上点着改。<br>
<br>
简单测试了一下，体验挺好的，在线编辑很方便。<br>
<br>
协作的用法和在线文档差不多。做好的幻灯片可以分享给同事，几个人同时在 ChatGPT 里编辑，在页面上留评论。评论攒多了，可以让 ChatGPT 或者你的 dot 按评论把幻灯片改一遍。dot 是 OpenAI 上个月在开发者大会上发布的 AI agent，有自己的云端电脑和浏览器，能在后台长时间替你干活。<br>
<br>
编辑方面，现在可以直接点到幻灯片上改文字、更新图表，拖动或缩放图片和形状。改个错别字、挪张图这种小事，自己动手就行，不必每次都打字让 ChatGPT 去改。<br>
<br>
用法是在对话里，或者针对你上传的文件，对 ChatGPT 说“create ChatGPT slides”（生成 ChatGPT 幻灯片）。做好后可以直接在 ChatGPT 里放映，也能导出成 PowerPoint 或 Google Slides 文件接着改。<br>
<br>
这些功能目前只对 Pro、Business 和 Enterprise 用户开放，公告没有提到免费版和 Plus。<br>
<br>
官方介绍：https://t.co/rWhcMJ41aF</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/yyyouweichen/status/2112265574931910880">@yyyouweichen: Proud to have led the AI behind our Claire, now on TIME&#x27;s Best Inventions of 2026. 🥳 我主导研发的 A...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月19日 19:32 UTC · 喜欢 53 · 转发 5 · 回复 4 · 浏览 4563</p>
<p class="archive-item-content">Proud to have led the AI behind our Claire, now on TIME&#x27;s Best Inventions of 2026. 🥳<br>
<br>
我主导研发的 AI 影像设备 Claire™，入选了《时代周刊》TIME 2026 年度最佳发明🎉<br>
今年 3 月刚拿下 FDA 批准，是美国第一个获批用于乳腺癌手术中的 AI 影像设备。<br>
从 AI 模型到手术室，这条路走通了💪 https://t.co/g6v3VmG4gF</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/ChatGPT/status/2112265233192657153">@ChatGPT: ChatGPT Slides has new ways to get your deck ready—and get everyone on the same page. • Work...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月19日 19:30 UTC · 喜欢 1775 · 转发 111 · 回复 79 · 浏览 114003</p>
<p class="archive-item-content">ChatGPT Slides has new ways to get your deck ready—and get everyone on the same page.<br>
<br>
• Work together in real time in ChatGPT: Share decks, edit together, and leave comments. Ask ChatGPT or your dot to turn feedback into updates.<br>
<br>
• Edit right on the slide: Click to change text, update charts, and move or resize images and shapes.<br>
<br>
To get started, ask ChatGPT to &quot;create ChatGPT slides&quot; from a conversation or a file you&#x27;ve shared. Present in ChatGPT, or export to PowerPoint or Google Slides.<br>
<br>
Available on Pro, Business, and Enterprise plans.<br>
https://t.co/2h9SfC7vzM</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/testingcatalog/status/2112195306695647502">@testingcatalog: ANTHROPIC 🔥: According to The Information, Anthropic will release a new model this month, alo...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月19日 14:52 UTC · 喜欢 1389 · 转发 70 · 回复 77 · 浏览 82008</p>
<p class="archive-item-content">ANTHROPIC 🔥: According to The Information, Anthropic will release a new model this month, along with Gemini 4 Carbon and a new Terra model from OpenAI. <br>
<br>
&gt; &quot;The unreleased model is especially good at discerning a person’s underlying intentions and goals even if they don’t give the model much information.&quot;<br>
<br>
&gt; &quot;The Anthropic model is also better at thinking outside of the box rather than regurgitating common sense advice or solutions.&quot;<br>
<br>
&gt; &quot;It’s not clear which model family Anthropic will fall into, such as Fable or Opus.&quot;<br>
<br>
Thinking outside of the box is a huge limitation these days. If we get a model that can do it reliably, we&#x27;ll be properly transitioning into the &quot;Innovators&quot; stage. <br>
<br>
The line about &quot;discerning underlying intentions&quot; is a bit scary, though, given all the guardrails.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2112155703309926729">@op7418: 抖音对于搬运的内容真是非常的纵容啊！ 尤其是搬运外网的，这哥们拿 Higgsfield 做的视频说是自己的，还编了一堆提示词出来 https://t.co/g7Jb1BhvaO</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月19日 12:15 UTC · 喜欢 27 · 转发 2 · 回复 37 · 浏览 13100</p>
<p class="archive-item-content">抖音对于搬运的内容真是非常的纵容啊！<br>
<br>
尤其是搬运外网的，这哥们拿 Higgsfield 做的视频说是自己的，还编了一堆提示词出来 https://t.co/g7Jb1BhvaO</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2112125082562929018">@op7418: 思琦他们做的这个关于 Apple 开发者生态里 AI 方向的调研还挺有意思的。 其实 Apple 整个开发生态跟外部还是不太一样，比较独立，所以在 AI 的采用率和想法上，可能未必跟我们...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月19日 10:13 UTC · 喜欢 9 · 转发 1 · 回复 13 · 浏览 5486</p>
<p class="archive-item-content">思琦他们做的这个关于 Apple 开发者生态里 AI 方向的调研还挺有意思的。<br>
<br>
其实 Apple 整个开发生态跟外部还是不太一样，比较独立，所以在 AI 的采用率和想法上，可能未必跟我们有些不做 Apple 生态的人的体感接近。感兴趣可以看看 https://t.co/6gcRcuGjoT</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2112114363624800300">@op7418: 笑死 DHH 很懂了，来中国用 Tailscale 访问 Claude Code</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月19日 09:31 UTC · 喜欢 254 · 转发 11 · 回复 67 · 浏览 65524</p>
<p class="archive-item-content">笑死 DHH 很懂了，来中国用 Tailscale 访问 Claude Code</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/SwiftSIQI/status/2112039887742619833">@SwiftSIQI: 过去一个月，我们围绕 Xcode 和 Apple 生态做了一次 AI 方向的调研。今天，分析报告正式公开！🎉 本次发布的是基于 100 位 Apple 生态领域专家反馈的专家组报告，大众...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月19日 04:35 UTC · 喜欢 86 · 转发 22 · 回复 5 · 浏览 45758</p>
<p class="archive-item-content">过去一个月，我们围绕 Xcode 和 Apple 生态做了一次 AI 方向的调研。今天，分析报告正式公开！🎉<br>
<br>
本次发布的是基于 100 位 Apple 生态领域专家反馈的专家组报告，大众组的数据仍在收集中。<br>
<br>
希望这份报告能为大家提供有价值的参考，也欢迎交流讨论！<br>
<br>
📊 完整报告：<br>
https://t.co/XFFc400dRh</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2112022611228230108">@op7418: 我们在这一期《Next Token》播客里的一些核心认知： 橘子说的：只要 AI 把一个东西打到了 60 分，这个东西就变成了 0 分。所以一个东西越火，越容易变成 AI slop，然后...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 10月19日 03:26 UTC · 喜欢 47 · 转发 4 · 回复 36 · 浏览 7880</p>
<p class="archive-item-content">我们在这一期《Next Token》播客里的一些核心认知：<br>
<br>
橘子说的：只要 AI 把一个东西打到了 60 分，这个东西就变成了 0 分。所以一个东西越火，越容易变成 AI slop，然后被大家抛弃<br>
<br>
所有的 skill prompt 软件，唯一价值其实就是流量价值。目前随着 AI 破解能力和复刻能力越来越强，开源作品换注意力、然后再做转化，是一个非常常见的方式<br>
<br>
多 Agent 拉群其实只有情绪价值，没办法带来能力上的提升<br>
<br>
我还分享了一下我是如何不开电脑做自媒体的，包括发图文、剪视频等等。<br>
<br>
这期昨天已经更新了，欢迎收听！<br>
<br>
早上一起床已经有 4000 多个播放，同时收听有几百个人在听。作为一个只更新了 6 期的播客，还是挺吊的</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/LobsterAIYoudao/status/2111985683707645963">@LobsterAIYoudao: 第一期《中国办公 Agent 用户行为报告》发布后，引发了媒体和用户的关注与讨论。大家关心 Agent 产品的发展，也关心人们究竟把哪些工作交给了它。因此，从本期起，我们将按月发布报告，...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月19日 01:00 UTC · 喜欢 45 · 转发 4 · 回复 9 · 浏览 24957</p>
<p class="archive-item-content">第一期《中国办公 Agent 用户行为报告》发布后，引发了媒体和用户的关注与讨论。大家关心 Agent 产品的发展，也关心人们究竟把哪些工作交给了它。因此，从本期起，我们将按月发布报告，持续记录用户使用习惯的变化。本期聚焦 9 月，并额外补充十一假期的使用变化。<br>
<br>
9 月，用户单次任务规模继续增长；泛编程/IT 仍是办公 Agent 的主要用途，但是设计与内容创作正在升温。缓存策略的差异，为何能导致成本相差七倍多？哪些城市的用户深夜还在派活给 Agent？到了十一假期，使用高峰和任务需求又发生了什么变化？请锁定这期报告，我们看看 Agent 行业又有什么新变化！</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2111976005439275285">@dotey: 帮转：Manus 招实习生</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月19日 00:21 UTC · 喜欢 38 · 转发 1 · 回复 14 · 浏览 22243</p>
<p class="archive-item-content">帮转：Manus 招实习生</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2111974893676060990">@dotey: 真讽刺，这个视频里面讲两个 AI 一个审查代码一个更新审查后的代码，结果两个 AI 就这么搞了 50 多轮。 然后这条视频下面两个 AI 相互评论已经停不下来了 https://t.co...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月19日 00:17 UTC · 喜欢 502 · 转发 13 · 回复 214 · 浏览 120118</p>
<p class="archive-item-content">真讽刺，这个视频里面讲两个 AI 一个审查代码一个更新审查后的代码，结果两个 AI 就这么搞了 50 多轮。<br>
<br>
然后这条视频下面两个 AI 相互评论已经停不下来了 https://t.co/lql2ItPnmZ</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2111973062442693023">@dotey: 最新一期科普视频：车头朝下贴在弯道顶上，特斯拉新 Roadster 为什么掉不下来？ 视频 2 是中文版 特斯拉和 SpaceX 一起做的新款 Roadster，在发布会上头朝下停在二十米高...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月19日 00:09 UTC · 喜欢 52 · 转发 6 · 回复 31 · 浏览 18356</p>
<p class="archive-item-content">最新一期科普视频：车头朝下贴在弯道顶上，特斯拉新 Roadster 为什么掉不下来？<br>
视频 2 是中文版<br>
<br>
特斯拉和 SpaceX 一起做的新款 Roadster，在发布会上头朝下停在二十米高的弯道顶上，又冲出坡道、在半空翻身落地。<br>
<br>
这期用 3D 动画讲明白它背后的两件事：车底的风扇怎么把车“吸”在路上，气罐和喷口怎么把车推上天。<br>
<br>
顺着回答几个大家最关心的问题：<br>
是不是靠速度像过山车？<br>
能飞多久，能不能开着飞去上班？<br>
在空中怎么翻身？<br>
0.81 秒破百轮胎受得了吗？<br>
这些本事除了表演还有什么用？<br>
<br>
---<br>
<br>
这类视频制作相关 skill 我还在完善中，不过现在的版本可以参考：https://t.co/sYc5CT1m8j<br>
<br>
发给你的 Agent（需要配合 Opus 5.5 效果最佳）就可以使用<br>
<br>
这个视频素材都是自己联网检索的，发布视频是我制定的，结合了当时的发布视频，以及一些检索的 YouTube 视频，Opus 5.5 帮助做了 3D 建模动画。</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2112073533794971941">Swyx: Data engineers &gt; AI engineers there&#x27;s a big difference between a &quot;RAG guy&quot; and a &quot;Data Intens...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：数据工程师 &gt; AI 工程师，&#x27;RAG 人&#x27;和&#x27;数据密集型应用&#x27;的人之间存在巨大差异</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 10月19日 06:49 UTC · 喜欢 4 · 转发 0 · 回复 5</p>
<p class="archive-item-content">Swyx argues that data engineering skills are in far greater demand than AI engineering skills, distinguishing &#x27;RAG guys&#x27; from &#x27;Data Intensive Applications&#x27; people, and uses the observation to recruit for a role at Latent Space.</p>
<p class="archive-item-translation"><span>中文摘要</span>Swyx 认为数据工程技能的需求远超 AI 工程技能，并区分了&#x27;RAG 人&#x27;与&#x27;数据密集型应用&#x27;人才，借此为 Latent Space 招募人手。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/levie/status/2112051081014649303">Aaron Levie: Here’s why agent swarms are going to be a very big deal. We can finally make compute a critic...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Aaron Levie：这就是为什么智能体集群将会成为一件非常重大的事。我们终于能够让算力成为关键变量……</p>
<p class="source-line">Follow Builders · X 动态 · Aaron Levie · 10月19日 05:19 UTC · 喜欢 121 · 转发 13 · 回复 44</p>
<p class="archive-item-content">Aaron Levie argues that agent swarms will make compute the critical scaling variable for a large class of economically valuable, currently time-bottlenecked tasks such as cybersecurity, life sciences research, trading, and QA testing.</p>
<p class="archive-item-translation"><span>中文摘要</span>Aaron Levie 认为，智能体集群将使算力成为大量具有经济价值、目前受时间瓶颈限制的任务（如网络安全、生命科学研究、交易和 QA 测试）的关键扩展变量。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2112039275344941371">Thibault Sottiaux: I bought a new domain and I’m very excited for it. Very</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：我买了一个新域名，我非常兴奋。非常</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月19日 04:32 UTC · 喜欢 2948 · 转发 56 · 回复 777</p>
<p class="archive-item-content">Thibault Sottiaux teases that he purchased a new domain without revealing what it is or what it will be used for.</p>
<p class="archive-item-translation"><span>中文摘要</span>Thibault Sottiaux 预告自己买下了一个新域名，但没有透露具体内容或用途。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2112034328549216593">Thibault Sottiaux: https://t.co/kjNgDoLCWz</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：https://t.co/kjNgDoLCWz</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月19日 04:13 UTC · 喜欢 405 · 转发 9 · 回复 32</p>
<p class="archive-item-content">A tweet by Thibault Sottiaux consisting solely of a shortened link with no accompanying text or context.</p>
<p class="archive-item-translation"><span>中文摘要</span>Thibault Sottiaux 发布的一条推文，仅包含一个短链接，没有任何文字说明或背景信息。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2112034063934742720">Thibault Sottiaux: Our team worked with OpenCode to have their users who are also OpenAI API customers back in b...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：我们团队与 OpenCode 合作，让那些同时也是 OpenAI API 客户的用户重新恢复正常……</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 10月19日 04:12 UTC · 喜欢 3862 · 转发 166 · 回复 279</p>
<p class="archive-item-content">An OpenAI team member says they worked with OpenCode to restore affected users and refund credits drained in an attack, and invites developers to request Daybreak Blue access for a cyber-permissive defensive setup.</p>
<p class="archive-item-translation"><span>中文摘要</span>OpenAI 团队成员表示已与 OpenCode 合作，让受影响用户恢复服务并退还攻击中被盗用的额度，同时邀请开发者申请 Daybreak Blue 权限以启用防御性安全配置。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2112016747838796200">Peter Yang: Best comedy of the year https://t.co/jj4AxqOG1h</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：年度最佳喜剧</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 10月19日 03:03 UTC · 喜欢 12 · 转发 0 · 回复 3</p>
<p class="archive-item-content">Peter Yang shares a link on X calling it the &#x27;best comedy of the year&#x27; with no accompanying explanation or technical content.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 在 X 上分享了一个链接，称其为“年度最佳喜剧”，没有附带任何解释或技术内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2111986818057118160">Nikunj Kothari: This aged relatively well.. even with the GH growth, I think people are still sleeping on @re...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari：这条推文随时间证明还不错……即使 GitHub 有所增长，我认为人们仍然低估了 @reatools。</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 10月19日 01:04 UTC · 喜欢 14 · 转发 0 · 回复 3</p>
<p class="archive-item-content">Nikunj Kothari 发推称，尽管 GitHub 有所增长，人们仍然低估了 @reatools，并称其表现惊人。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2111971992769565177">Garry Tan: Prediction: you’re all going to be using @AsideAI with your agents in a year or so https://t....</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Garry Tan：预测：一年左右，你们都会把 @AsideAI 与你们的智能体一起使用</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 10月19日 00:05 UTC · 喜欢 424 · 转发 23 · 回复 87</p>
<p class="archive-item-content">Garry Tan predicts that within roughly a year, developers will all be using AsideAI alongside their AI agents, without offering technical detail or justification.</p>
<p class="archive-item-translation"><span>中文摘要</span>Garry Tan 预测，大约一年之内，开发者都会将 AsideAI 与自己的 AI 智能体搭配使用，但并未给出技术细节或论证。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2111971887811342582">Swyx: @aiDotEngineer @evanjconrad v nice side efvent https://t.co/Jt88Ncm3VN</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：@aiDotEngineer @evanjconrad 非常不错的周边活动 https://t.co/Jt88Ncm3VN</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 10月19日 00:05 UTC · 喜欢 3 · 转发 0 · 回复 0</p>
<p class="archive-item-content">Swyx posts a brief appreciative tweet tagging two accounts and sharing a shortened link.</p>
<p class="archive-item-translation"><span>中文摘要</span>Swyx 发布了一条简短的致意推文，@ 了两个账号并分享了一个缩短链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2111970651326267529">Peter Yang: Make work trials the norm for hiring instead of interviews. From @APompliano: “We had a speci...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：让工作试用成为招聘常态，而不是面试</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 10月19日 00:00 UTC · 喜欢 12 · 转发 0 · 回复 20</p>
<p class="archive-item-content">Peter Yang argues that companies should replace traditional interviews with paid work trials, citing a builder who let a candidate ship a real feature in two weeks.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 主张企业应以实际工作试用取代传统面试，并引述一位创业者让候选人两周内交付一个真实功能的案例。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2111962930644402504">Swyx: are we so different, you and i https://t.co/fOqLOgAInI</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：你和我，我们真有那么不同吗</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 10月18日 23:29 UTC · 喜欢 6 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A cryptic single-line tweet by Swyx (&#x27;are we so different, you and i&#x27;) containing only an unexplained link, with no substantive content or discussion.</p>
<p class="archive-item-translation"><span>中文摘要</span>Swyx 发布了一条含义模糊的一句话推文（“你和我，我们真有那么不同吗”），仅附一个未加说明的链接，没有任何实质内容或讨论。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/danshipper/status/2111962665987825809">Dan Shipper: current (mostly) reading: https://t.co/gvZsM7SnfD</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Dan Shipper：目前（主要）在读：https://t.co/gvZsM7SnfD</p>
<p class="source-line">Follow Builders · X 动态 · Dan Shipper · 10月18日 23:28 UTC · 喜欢 38 · 转发 0 · 回复 7</p>
<p class="archive-item-content">Dan Shipper shares a link to what he is currently (mostly) reading, with no accompanying commentary or technical detail.</p>
<p class="archive-item-translation"><span>中文摘要</span>Dan Shipper 分享了一个链接，指向他目前（主要）在阅读的内容，未附带任何评论或技术细节。</p>
</article>
</div>
</section>
