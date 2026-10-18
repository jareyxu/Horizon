---
layout: default
title: "Horizon Summary: 2026-10-19 (ZH)"
date: 2026-10-19
lang: zh
---

> 从 22 条内容中筛选出 6 条重要资讯。

---

1. [Together AI 发布 HybridAgent：在潜在空间推理、以文本行动](#item-1) ⭐️ 8.0/10
2. [Anthropic 内部研究：AI Agent 工时达人类六倍，技术初级岗位大幅萎缩](#item-2) ⭐️ 7.2/10
3. [德国两家法院裁定 Google 须为其 AI Overview 内容负责](#item-3) ⭐️ 7.17/10
4. [文章观点：AI 时代，人的品味与意图仍是软件不可替代的核心](#item-4) ⭐️ 7.0/10
5. [RepRapMicron：开源项目瞄准微米级自复制 3D 打印](#item-5) ⭐️ 7.0/10
6. [DeepSeek 推出搜索与抓取 API，每千次成功请求收费 0.75 美元](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Together AI 发布 HybridAgent：在潜在空间推理、以文本行动](https://arxiv.org/abs/2610.18861) ⭐️ 8.0/10

Together Computer（Together AI）推出了 Hybrid Reasoning Agents（HybridAgents）框架，让 LLM 智能体在同一个统一的生成过程中动态地在潜在空间推理与文本交互之间切换。该发布同时开源了权重（托管于 Hugging Face）、代码（GitHub 上的 togethercomputer/HybridAgent），并在 arXiv 论文 2610.18861 中给出了基准评测结果；论文由 Jiaru Zou、Yunzhe Qi、Sirui Chen、Federico Bianchi、Shang Zhu、Pan Lu、Jingrui He 和 James Zou 于 2026 年 10 月 13 日提交。 当前的 LLM 智能体仍然完全依赖文本进行推理和行动，这种方式冗长且存在信息损耗；而纯潜在空间推理虽然高效，却缺乏原生的工具调用能力和推理过程的可解释性。HybridAgents 试图通过在生成过程中切换模式来兼得两者优势。由于它开源了权重、代码和公开评测，智能体开发者获得了一个可以直接试验的、替代传统 token 级思维链的方案，这也与近期把智能体推理移出 token 流的研究趋势（例如潜在空间多智能体通信）相呼应。 其核心机制是一个“Hybrid Link”，让模型在一次生成过程中交替进入潜在模式（内部 deliberation）和文本模式（工具调用与外部交互），而不是把推理阶段与行动阶段简单拼接起来。早期的第三方测试结果并不一致：有社区成员在 llama.cpp 中运行该 14B 模型的 8-bit 量化版本时，发现它在处理一个简单的网络搜索与摘要任务时会反复输出同一段落的变体，直到用尽回合预算，这可能是因为 llama.cpp 尚需更新以支持该架构。

hackernews · allinonai · 10月18日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=50145337)

**核验**: 多源印证

**背景**: 思维链（chain-of-thought）提示让 LLM 通过写出中间步骤来进行推理，但这会把丰富的内部表示压缩成离散的 token。潜在空间推理则让模型在其连续的隐状态（嵌入）空间中进行思考，成本更低、表达能力更强，但过去无法调用工具，也难以展示模型的思考过程。“开放权重”（open weights）意味着模型的训练参数被公开发布，任何人都可以下载、在本地运行并加以修改，这与只能通过 API 访问的闭源模型不同。HybridAgents 的定位正是在 token 级方法与潜在空间方法之间架起桥梁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.18861">[2610.18861] Hybrid Reasoning Agents - arXiv.org</a></li>
<li><a href="https://github.com/Gen-Verse/LatentMAS">GitHub - Gen-Verse/LatentMAS: [ICML 2026 Spotlight] Latent ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_artificial_intelligence">Open weights - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一架构思路颇感兴趣，但也提出了实际使用中的担忧：有人反馈在 llama.cpp 中运行该 14B 模型的 8-bit 量化版本时，面对同类规模模型（如 Gemma 4 12B）能轻松完成的简单网络搜索与摘要任务，它会低效地反复输出内容，并推测 llama.cpp 的支持可能尚未跟上。另一位评论者则建议更进一步：把输入嵌入加宽，使其在文本模式下也同时携带 Hybrid Link 之后的潜在向量和 token 嵌入（或干脆把两个向量直接相加），从而在输出文本时仍能持续进行潜在推理，因为反正已经在支付完整的潜在模式计算开销。

**标签**: `#AI agents`, `#LLM reasoning`, `#latent space`, `#open source AI`, `#Together AI`

---

<a id="item-2"></a>
## [Anthropic 内部研究：AI Agent 工时达人类六倍，技术初级岗位大幅萎缩](https://the-decoder.com/anthropic-has-nearly-stopped-hiring-junior-staff-because-ai-agents-now-work-six-times-as-many-hours/) ⭐️ 7.2/10

Anthropic 发布了一项内部研究，显示其技术部门的初级岗位占比自 2025 年初的 21% 降至 14%，新招员工中的初级占比从 27% 骤降至 9%，空缺初级职位仅剩 6%。公司将这一变化归因于自家 AI Agent 能力的提升——截至 2026 年 8 月，全公司 AI Agent 记录的工作时长已是人类员工的六倍，研究部门更是达到 19:1。 这是目前最具体的数据之一，表明 AI Agent 已在一家前沿 AI 实验室内部真实地改变了初级技术岗位的招聘，而不再只是停留在预测层面。由于初级岗位历来是培养未来专家的主要通道，若 AI 密集型企业持续减少入门级招聘，整个经济体系可能在长期面临资深工程师、分析师与法律研究人才短缺的问题。 Anthropic 称各部门生产率均有所提升：工程师提交的代码提交量达到 5.1 倍，数据科学家运行的查询数为 3.1 倍，法务团队处理的合同数为 3.1 倍，销售成交量为 1.7 倍，招聘与会计处理量各为 1.4 倍。该研究本身也承认 Anthropic 属于特例——它是一家 AI 使用极其密集的软件公司，且业务高速增长、员工自愿采用 AI 工具，这些因素都可能扭曲数据；研究同时指出，更广泛的经济体迄今尚未显现出可测量的 AI 生产率提升。

aihot · The Decoder：AI News（RSS） · 10月18日 13:22 · [中文阅读](https://aihot.news/items/c7pt5mbzh5h0atlbprfzbs8o0)

**核验**: 多源印证

**背景**: AI Agent 是指利用 Claude 等大语言模型自主完成多步骤任务的系统——在 Anthropic 的案例中即编写代码和查找缺陷——而不仅仅是回答单个提示。初级技术岗位历来是应届生通过处理常规工作积累经验、逐步成长为专家的地方，因此用 Agent 取代这一层会直接改变人才供给链条。北约特种作战大学的研究员 Nolan Lovett 将这种现象称为“认知公地的悲剧”：单个企业获得了效率收益，而资深人才断层的代价却由整个社会承担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@dprapria/ai-agents-explained-simply-why-every-intelligent-system-has-a-brain-and-a-body-ec7b400560ba">AI Agents Explained Simply: Why Every Intelligent System... | Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/where-ai-agents-actually-belong-your-business-spoiler-kyler-cheatham-o7xbf">Where AI Agents Actually Belong in Your Business (Spoiler: It’s the...)</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#hiring trends`, `#AI labor impact`, `#Anthropic`, `#developer careers`

---

<a id="item-3"></a>
## [德国两家法院裁定 Google 须为其 AI Overview 内容负责](https://the-decoder.com/two-german-courts-now-hold-google-liable-for-what-its-ai-overviews-say/) ⭐️ 7.17/10

今年五月底，慕尼黑地区法院 I 裁定 Google 须直接为其 AI 生成的搜索摘要内容负责，认定 AI Overview 属于 Google 自身的陈述，而非指向第三方网站的中立链接。Google 曾公开宣布上诉，但最终以和解结案；而在 2026 年 9 月 24 日作出的一项裁定中，亚琛地区法院明确援引慕尼黑的裁判理由，禁止 Google 通过其“AI 模式”功能传播针对一名医生的虚假指控。 若这一法律观点被确立，Google 将无法再以“仅转述第三方信息的中立中间人”身份免责，这可能会动摇 AI 搜索在德国的整个商业模式，并影响其他国家的监管与司法态度。该推理还打开了另一条战线：其文本被用于生成 AI 答案的出版商，未来也可能主张自身权利；而对于一个每次查询都会生成新表述的功能来说，这种风险规模极难量化。 慕尼黑一案因以和解结案，上诉始终未获上级法院裁决，因此该裁判理由尚未在二审层面得到确认；和解原因及是否涉及金钱赔偿均不为人知，Google 与受影响出版商都拒绝置评。亚琛的禁令源于 8 月 28 日一位同事告知该医生其遭遇了被虚构的性侵指控和凭空捏造的司法程序，该禁令目前尚未生效，Google 仍可提出异议。

aihot · The Decoder：AI News（RSS） · 10月18日 10:52 · [中文阅读](https://aihot.news/items/bbr25r9mbi8zbbtmu2uiati7f)

**核验**: 多源印证

**背景**: AI Overview 是 Google 搜索中的生成式 AI 功能，会在搜索结果顶部展示由 AI 撰写的答案；它于 2024 年 5 月在美国上线，同年 10 月扩展至全球，由 Google 的 Gemini 系列模型驱动，此外还有一个对话式的“AI 模式”实验功能。按照传统搜索法律框架，Google 通常被视为仅提供第三方内容链接的中间人，可享受针对他人发布内容的免责保护。此次裁决则将 AI 生成的摘要重新定性为 Google 自身的言论；而 AI Overview 此前已因不准确、幻觉以及导致网站流量下降而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Overviews">Google AI Overviews</a></li>
<li><a href="https://blog.google/products-and-platforms/products/search/ai-mode-search/">Expanding AI Overviews and introducing AI Mode</a></li>

</ul>
</details>

**标签**: `#AI 法律责任`, `#AI Overviews`, `#AI 监管`, `#搜索`, `#AI 产品设计`

---

<a id="item-4"></a>
## [文章观点：AI 时代，人的品味与意图仍是软件不可替代的核心](https://karrisaarinen.com/posts/someone-behind-the-software/) ⭐️ 7.0/10

Karri Saarinen 发表了题为《Someone behind the software》的文章，认为在 AI 已能编写代码、并逐渐涉足架构设计的时代，人类不可替代的价值在于决定要做什么、定义产品愿景，以及投入品味与意图。这篇文章在 Hacker News 上引发了热烈讨论，获得 260 分和 109 条评论。 随着 AI 编程助手承担越来越多机械性的实现工作，开发者、产品经理和 SaaS 创业者都需要重新思考自身的独特价值所在，而这篇文章给出了一个被广泛讨论的答案：价值在于产品判断力，而非代码产出。它正处在关于 AI 辅助开发以及软件中人类作者身份意义的行业大讨论的中心。 这是一篇反思性的观点文章，而非技术深度剖析或产品发布，因此其论点建立在论证与个人经验之上，而非基准测试或数据。其核心提醒在于：文章所推崇的“决定要做什么”这项工作，恰恰是整份工作中最慢、最难自动化的一环，这也正是作者将其视为人类长期领地的原因。

hackernews · tosh · 10月18日 16:32 · [社区讨论](https://news.ycombinator.com/item?id=50142573)

**核验**: 已核对原文

**背景**: AI 编程工具已经进步到能够生成大量可用代码并辅助架构决策的程度，这促使人们重新评估软件工程师的独特贡献究竟是什么。讨论这篇文章的 Hacker News 是一个读者广泛的科技论坛，其评论区往往会影响此类观点在开发者社区中的传播。文章的思路也延续了更早关于软件工匠精神与产品设计的讨论——这些讨论早已认为，理解用户需求比单纯的实现技能更为重要。

**社区讨论**: 评论者大体从不同角度赞同该文观点：SaaS 作者 jwr 表示价值已不在代码、甚至不在架构，而在于决定要做什么、以及每个界面如何帮助客户完成工作；allenu 则认为 AI 根本不具备价值观、意图与品味。elliotto 提出异议，警告说将商业软件创作拟人化是错误的想法，因为这类系统的存在是为了体现资本的欲望，只要有可能，资本会把人完全排除在软件生产过程之外。ajrouvoet 则补充了一条文学线索，指出多萝西·塞耶斯（Dorothy Sayers）的《The Mind of the Maker》——被 Fred Brooks 在《人月神话》中引用——将创作活动分为想法、实现与交互三个阶段。

**标签**: `#AI-assisted development`, `#product design`, `#AI and creativity`, `#software craftsmanship`, `#developer experience`

---

<a id="item-5"></a>
## [RepRapMicron：开源项目瞄准微米级自复制 3D 打印](https://github.com/VikOlliver/RepRapMicron/wiki) ⭐️ 7.0/10

Vik Olliver 的 RepRapMicron（μRepRap）项目在 GitHub Wiki 上介绍了其目标：仅使用常见且易获取的材料，打造一台能够实现微米（1µm，即 1/1000 毫米）乃至亚微米级加工的开放硬件 3D 打印机，其精度最初依托 OpenFlexure 项目设计的 3D 打印显微镜平台。该条目在 Hacker News 上引发强烈关注，获得 312 分和 48 条评论。 如果微米级增材制造真的能靠廉价的开源硬件实现，芯片制造、微流控和光学等领域就可能向爱好者和小型实验室开放，而不再只是昂贵工业设备的专属领域。这延续了 RepRap 让生产工具普及化的传统，也可能让大量目前只存在于软件中的芯片设计变成真正的实体硬件。 项目称其微米级精度最初得益于 OpenFlexure 项目设计的 3D 打印显微镜平台，此后又发展出更适合原型制作与加工的变体。其长期目标是实现自我复制，而社区中有人激烈争论它能否打印出自身千分之一大小的复制品（即 1/1,000,000 比例的 3D 打印）。

hackernews · RobotToaster · 10月18日 13:48 · [社区讨论](https://news.ycombinator.com/item?id=50141076)

**核验**: 多源印证

**背景**: RepRap 是“replicating rapid prototyper”（可自我复制的快速成型机）的缩写，是一个长期运行的开源项目，旨在开发低成本、能打印自身大部分零件的 3D 打印机，所有设计均以 GNU GPL 等自由许可发布。RepRapMicron 把这一自复制血统延伸到微米和亚微米尺度，而这一尺度正是微流控、光学元件乃至类半导体结构所需要的。工业界已有 BMF、Nanofabrica 等厂商推出商用微米级 3D 打印机，但它们都是昂贵的工业设备，而 µRepRap 希望用常见材料达到相近的精度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/VikOlliver/RepRapMicron">GitHub - VikOlliver/RepRapMicron: μRepRap - A 3D printer ...</a></li>
<li><a href="https://reprap.org/wiki/RepRapMicron">RepRapMicron - RepRap GitHub - VikOlliver/RepRapMicron: μRepRap - A 3D printer ... RepRapMicron - YouTube RepRapMicron - hn.today RepRapMicron | Hacker News RepRapMicron – Hackaday The Latest From RepRapMicron – Nail Gel, First Objects, And ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/RepRap">RepRap - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者把这一进展与 18 世纪末的机床突破相类比——Ramsden 的分度机、Maudslay 的螺纹车床和 Wilkinson 的镗床，认为这些基础工具曾把手工技艺变成可批量复制的可靠制造能力；也有人贴出了介绍相关前置技术的 YouTube 视频系列。不少人十分兴奋（“再过 18 个月我们就能自己造 RAM 了”），并指出许多很酷的芯片设计目前只是电脑里的软件，若能廉价、可持续地打印出来，硬件领域会迎来很有意思的转折；也有人反问，为什么“打印出自身千分之一的复制品”会被认为是荒谬的想法。

**标签**: `#open-source-hardware`, `#3D-printing`, `#RepRap`, `#microfabrication`, `#self-replication`

---

<a id="item-6"></a>
## [DeepSeek 推出搜索与抓取 API，每千次成功请求收费 0.75 美元](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

DeepSeek 于 10 月 17 日上线了两个新的原生 JSON 接口：Search API 使用 DeepSeek 自研搜索引擎按查询词检索网页并返回结构化结果，Fetch API 则抓取单个网页并以 Markdown 形式返回标题与正文。两者定价均为每 1000 次成功请求 0.75 美元（5 元人民币），并设有账户级别的速率限制。 这一价格远低于同类托管搜索 API——Brave Search API 约为每千次 5 美元，Perplexity 为 5 美元，Kagi 则高达 12 美元——有望大幅降低需要联网检索的智能体与 RAG 流水线的大规模运行成本。同时这也让 DeepSeek 从单纯的大模型供应商延伸为面向智能体开发者的全栈服务商，加剧了智能体联网访问这一新兴市场的竞争。 计费严格与成功挂钩：只有当请求返回 HTTP 200 并且确实产出了结果时才会计费，因此失败的请求、空的搜索结果和超时都不收费；控制返回结果数量的 `count` 参数也不影响单次请求价格。文档还提示，若通过 DeepSeek Harness、Claude Code 等工具调用 DeepSeek API，可能适用不同的计费规则。

hackernews · fagnerbrack · 10月18日 06:50 · [社区讨论](https://news.ycombinator.com/item?id=50138531)

**核验**: 多源印证

**背景**: AI 智能体和检索增强生成（RAG）系统需要最新的网页内容来回答训练数据之外的问题，但直接爬取网页既脆弱又常被封禁，因此开发者越来越倾向于购买托管式搜索 API。长期以来 Google 并未为此提供通用的付费搜索接口，从而给 Brave、Kagi、Perplexity、Exa 和 Firecrawl 等服务智能体开发者留下了空间。DeepSeek 此次入场，把自研搜索索引以远低于市场主流单次请求价格的水平带入这一市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/guides/search/">Search & Fetch | DeepSeek API Docs</a></li>
<li><a href="https://runtimewire.com/article/deepseek-search-fetch-api-pricing-liang-wenfeng">DeepSeek puts web search on the API meter at $0.75 per 1,000 ...</a></li>
<li><a href="https://docs.perplexity.ai/docs/getting-started/pricing">Pricing - Perplexity</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论对托管搜索服务商的价值看法不一：有开发者认为 searxng-ai-kit 这类自托管工具或基于抓取的智能体成本更低（免费），也有人指出这些服务之所以存在，正是因为 Google 拒绝提供付费搜索 API。还有人推测，随着智能体驱动的搜索增长，SEO 经济可能推动搜索 API 价格趋近于零甚至转为负值，因为谁控制 API 谁就控制排名影响力；另有评论者呼吁 DeepSeek 采用“来源感知”训练，让模型能区分哪些事实来自已有文献、哪些是自己的推理。

**标签**: `#AI agents`, `#search API`, `#DeepSeek`, `#developer tools`, `#pricing`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="1"><span>其他追踪推文</span><span class="archive-tab-count">1</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="3"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">3</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/LufzzLiz/status/2111659007564026121">@LufzzLiz: Claude 账号申请解封失败，也不退钱。用 Opus 5.5 做个视频给它吧， 一个悲惨的故事：我用 codex 做了三天迭代了好几版。结果发现还是 Opus 5.5 做的更好，一下午就出来了...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 10月18日 03:21 UTC · 喜欢 21 · 转发 2 · 回复 12 · 浏览 9605</p>
<p class="archive-item-content">Claude 账号申请解封失败，也不退钱。用 Opus 5.5 做个视频给它吧，<br>
一个悲惨的故事：我用 codex 做了三天迭代了好几版。结果发现还是 Opus 5.5 做的更好，一下午就出来了😭 https://t.co/N5zSUhmJG3</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2111663267995361287">Peter Yang: Tim is so right. Hope the devs building StarCraft 3 sees this tweet and embrace AI to ship be...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：Tim 说得太对了。希望开发《星际争霸 3》的开发者能看到这条推文并拥抱 AI，在……之前发布</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 10月18日 03:38 UTC · 喜欢 71 · 转发 1 · 回复 5</p>
<p class="archive-item-content">Peter Yang agrees with a tweet urging StarCraft 3 developers to embrace AI so the game ships before 2030.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 认同一条推文的观点，呼吁《星际争霸 3》的开发者拥抱 AI，让游戏在 2030 年前发布。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2111643672274165938">Guillermo Rauch: “What matters is the end product, whether it&#x27;s a game or an engine”. Well said! https://t.co/...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：“真正重要的是最终产品，无论它是一个游戏还是一个引擎”。说得好！</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 10月18日 02:20 UTC · 喜欢 381 · 转发 12 · 回复 43</p>
<p class="archive-item-content">Guillermo Rauch endorses the idea that the quality of the end product—whether a game or an engine—is what ultimately matters.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 赞同“真正重要的是最终产品——无论它是一个游戏还是一个引擎”这一观点。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2111597172840083574">Nan Yu: I had the same conversation reminiscing at a team offsite the other day. “What did we pay att...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nan Yu：前几天在团队团建时我也聊起过同样的话题。“在 AI 之前，我们都关注什么？”</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 10月17日 23:16 UTC · 喜欢 56 · 转发 2 · 回复 4</p>
<p class="archive-item-content">Nan Yu observes that before AI, team offsites were spent obsessing over front-end JavaScript frameworks, highlighting how developer attention has shifted toward AI.</p>
<p class="archive-item-translation"><span>中文摘要</span>Nan Yu 指出，在 AI 出现之前，团队团建讨论的焦点是前端 JavaScript 框架，反映出开发者注意力已转向 AI。</p>
</article>
</div>
</section>
