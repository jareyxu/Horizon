---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> 从 44 条内容中筛选出 9 条重要资讯。

---

1. [Kimi K3：开源 3 万亿参数模型震动 AI 界](#item-1) ⭐️ 9.0/10
2. [Fable 5 与 GPT-5.6 Sol 在 NP-Hard 问题上的对决：/goal 功能测试](#item-2) ⭐️ 8.0/10
3. [StackOverflow 衰退：AI 与社区壁垒](#item-3) ⭐️ 8.0/10
4. [Claude Fable 5 纳入 Max 和 Team Premium 计划](#item-4) ⭐️ 7.3/10
5. [GPT-5.6 解决凸优化 30 年难题，但依赖前期工作](#item-5) ⭐️ 7.0/10
6. [基于 Pyodide 的交互式 SQLite 查询解释器](#item-6) ⭐️ 7.0/10
7. [高保真原型替代文档，AI 直接生成代码](#item-7) ⭐️ 7.0/10
8. [Codex 已能自行编写大部分代码](#item-8) ⭐️ 7.0/10
9. [Codex 用浏览器绕道暴露 AI 代理低效](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Kimi K3：开源 3 万亿参数模型震动 AI 界](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 9.0/10

月之暗面发布了 Kimi K3，这是全球首个开源且拥有 2.8 万亿参数的模型，采用了 Kimi Delta Attention 技术并支持 100 万 token 的上下文窗口。 此次发布挑战了美国前沿 AI 实验室的主导地位，证明了开源模型也能达到顶级性能，可能重塑竞争格局并引发国家安全方面的担忧。 Kimi K3 基于 Kimi Delta Attention（KDA）这一混合线性注意力机制构建，并具备原生视觉理解能力，适用于长周期编程和知识工作。

hackernews · sbochins · 7月18日 17:32 · [社区讨论](https://news.ycombinator.com/item?id=48960218)

**核验**: 多源印证

**背景**: 知识蒸馏是一种让小模型从大型“教师”模型中学习的技术，常用于创建高效的模型。Kimi K3 的开源特性使其可被广泛获取，但其庞大的规模（2.8 万亿参数）使得本地部署成本极高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**社区讨论**: 评论者就 Kimi K3 的性能是源于蒸馏还是独立创新展开辩论，有人认为蒸馏是不可避免的，并非“攻击”。其他人则担心国家安全影响，并将使用 Kimi K3 比作 Napster 时代，同时有用户报告称，在类似任务上 Kimi K3 消耗的资源远多于 OpenAI 的模型。

**标签**: `#AI agents`, `#Kimi K3`, `#distillation`, `#AI models`, `#product release`

---

<a id="item-2"></a>
## [Fable 5 与 GPT-5.6 Sol 在 NP-Hard 问题上的对决：/goal 功能测试](https://charlesazam.com/blog/fable-5-gpt-5-6-sol-goal/) ⭐️ 8.0/10

一项技术评估将 Claude Fable 5 与 GPT-5.6 Sol 在一个未公开的 NP-Hard 优化问题上进行了比较，测试了 '/goal' 功能在两者中的有效性。结果显示 Fable 5 表现极为出色，尤其是在使用 /goal 时。 这项比较很重要，因为它提供了关于领先 AI 编码代理如何处理复杂、长期任务的真实见解，这对于开发人员选择自主软件开发工具至关重要。/goal 功能能够实现持久的、多步骤的目标，可能显著提高代理的可靠性和自主性。 该评估使用了一个未公开的 NP-Hard 优化问题，分别在有和没有 /goal 模式的情况下测试了两个模型。原始摘要中将 Fable 5 描述为“绝对的猛兽”，而社区评论指出 /goal 更适合单线调查或小规模分散/收集任务。

hackernews · couAUIA · 7月18日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=48956879)

**核验**: 多源印证

**背景**: NP-Hard 问题是一类没有已知高效算法的计算问题，因此成为测试 AI 推理能力的严格标准。/goal 功能是 AI 编码工具中的一种长期模式，允许代理在多个会话中持续追求目标，无需不断提示，从而支持复杂的多步骤工程任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://medium.com/coding-nexus/goal-is-the-most-underrated-ai-feature-of-2026-heres-how-to-use-it-right-96f265344530">/goal Is the Most Underrated AI Feature of 2026 — Here’s How to Use It Right | by Code Coup | Coding Nexus | May, 2026 | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论提供了不同的反馈：一些用户发现图表因 y 轴反转而令人困惑，而另一些用户则认为“ultra 模式”可能更适合搜索策略。一位用户指出 Claude 在非常长的会话中似乎会忘记指令，而 /goal 可能有助于解决这个问题；另一位用户则指出，鉴于 GPT 最近在比赛中获胜，它应该在优化问题上表现更好。

**标签**: `#AI agents`, `#AI coding tools`, `#technical evaluation`, `#Fable 5`, `#GPT-5.6 Sol`

---

<a id="item-3"></a>
## [StackOverflow 衰退：AI 与社区壁垒](https://data.stackexchange.com/stackoverflow/query/1953768#graph) ⭐️ 8.0/10

一张来自 Stack Exchange Data Explorer 的图表显示了 StackOverflow 活跃度的下降，引发了关于该平台衰落原因的讨论，既包括 AI 大语言模型的兴起，也包括其高参与门槛和敌对的社区文化。 这很重要，因为 StackOverflow 一直是开发者的核心资源，其衰落反映了开发者寻求答案方式的广泛转变，从社区问答转向 AI 工具。同时也凸显了社区管理在维持在线平台活力方面的重要性。 该图表特别显示了 StackOverflow 上问题和答案数量的下降，与 ChatGPT 等大语言模型的兴起相吻合。评论者指出，StackOverflow 的严格审核、缺乏社区功能以及激进的防机器人措施也导致了用户流失。

hackernews · secretslol · 7月18日 11:12 · [社区讨论](https://news.ycombinator.com/item?id=48956949)

**核验**: 待核验

**背景**: StackOverflow 是一个面向程序员的流行问答平台，用户在此提出和回答技术问题。长期以来，它因对新用户不友好的文化而受到批评，问题经常被无解释地踩或关闭。AI 聊天机器人的兴起提供了即时答案的替代方案，加速了该平台的衰落。

**社区讨论**: 评论普遍批评 StackOverflow 的社区壁垒和敌意，许多用户表示尽管 LLM 有缺陷，他们仍更倾向于使用它们。一些人指出该平台限制性的 Cloudflare Turnstile 进一步阻碍了人类访客。共识是 StackOverflow 的衰落是自作自受，而不仅仅是 AI 的原因。

**标签**: `#AI`, `#StackOverflow`, `#developer tools`, `#LLMs`, `#community engagement`

---

<a id="item-4"></a>
## [Claude Fable 5 纳入 Max 和 Team Premium 计划](https://x.com/claudeai/status/2078302415804379218) ⭐️ 7.3/10

Anthropic 宣布，自 2026 年 7 月 20 日起，Claude Fable 5 将纳入所有 Max 和 Team Premium 订阅计划，使用额度为原有限额的 50%；Pro 和 Team Standard 用户将获得一次性 100 美元积分以继续使用。 此举逆转了 Anthropic 此前将 Fable 5 从订阅计划中移除的计划，很可能是受到 GPT-5.6 Sol 等模型的竞争压力。它确保了高付费订阅用户仍能使用 Anthropic 的最佳模型，使订阅计划更具价值。 每月 20 美元计划的用户仍无法使用 Fable 5，Max 计划价格为每月 100 美元和 200 美元。50% 的限额意味着订阅者只能将通常使用额度的一半用于 Fable 5。

twitter · Claude · 7月18日 02:14 · 3 个来源

**核验**: 多源印证

**背景**: Claude Fable 5 是 Anthropic 推出的大型语言模型，属于 Mythos 系列，于 2026 年 6 月 9 日发布。它是更强大的 Claude Mythos 5 的安全版本，后者因具有极强的软件漏洞发现能力而未公开发布。Fable 5 可通过 API 和云平台使用。Anthropic 最初因需求旺盛和算力限制计划仅通过 API 提供 Fable 5，但后来决定将其纳入订阅计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#Claude`, `#Fable 5`, `#AI tools`, `#product update`, `#pricing`

---

<a id="item-5"></a>
## [GPT-5.6 解决凸优化 30 年难题，但依赖前期工作](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 7.0/10

据报道，GPT-5.6（通过 Sol Pro）在 148 分钟内解决了一个凸优化领域 30 年未解的难题，但社区分析显示，该解决方案依赖于作者一年的前期工作，且提示词中已包含求解技术。 这一事件展示了人工智能辅助数学研究的潜力，但也凸显了区分真正的 AI 突破与严重依赖人类前期工作和提示工程的结果的重要性。 使用的模型是 Sol Pro，而非更高级的 Ultra。该问题涉及证明在球域上对 Lipschitz 凸函数进行优化的时间复杂度上界，而球域等价于任何有界域。

hackernews · mbustamanter · 7月18日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**核验**: 多源印证

**背景**: 凸优化是数学优化的一个子领域，研究在凸集上最小化凸函数。许多此类问题可以高效求解，但确定某些类别的精确复杂度上界仍是一个活跃的研究领域。30 年未解的难题指的是关于某类凸优化问题最优时间复杂度的未解决猜想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，所谓的'148 分钟'实际上是'一年加 148 分钟'的工作，因为作者此前已使用 GPT-5.4 和 5.5 进行了迭代。提示词中包含了求解技术，降低了新颖性。还有关于 Sol Pro 与 Ultra 差异的讨论，以及对 AI 辅助研究的更广泛影响。

**标签**: `#AI`, `#convex optimization`, `#GPT-5.6`, `#AI-assisted research`, `#mathematical proof`

---

<a id="item-6"></a>
## [基于 Pyodide 的交互式 SQLite 查询解释器](https://simonwillison.net/2026/Jul/18/sqlite-query-explainer/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了一个基于浏览器的交互式 SQLite 查询解释器，该工具通过 Pyodide 在 WebAssembly 中运行 Python 环境下的 SQLite。它能为 EXPLAIN 和 EXPLAIN QUERY PLAN 命令的输出添加解释性注释，帮助开发者理解查询执行计划。 该工具通过直接在浏览器中提供交互式解释，降低了 SQLite 查询计划分析的门槛。它展示了通过 Pyodide 和 WebAssembly 在浏览器中运行 Python 的实用案例，可能启发类似的开发者工具。 该工具在浏览器中通过 Pyodide 将 Python 环境编译为 WebAssembly 来运行 SQLite。作者提到他借助 Fable 构建了此工具，并提醒说他缺乏足够专业知识来完全验证解释的准确性。

rss · Simon Willison · 7月18日 17:19

**核验**: 多源印证

**背景**: SQLite 的 EXPLAIN 和 EXPLAIN QUERY PLAN 命令可以显示查询的执行方式，但其输出对许多开发者来说可能难以理解。Pyodide 是一个基于 WebAssembly 的 Python 发行版，可以在浏览器和 Node.js 中运行 Python 代码。WebAssembly 是一种低层二进制格式，能在现代浏览器中以接近原生的性能运行。该工具利用这些技术，为理解 SQLite 查询计划提供了交互式学习体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyodide.org/">Pyodide — Version 314.0.2</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://www.sqlite.org/eqp.html">Explain query plan</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#developer tools`, `#query optimization`, `#WebAssembly`, `#Pyodide`

---

<a id="item-7"></a>
## [高保真原型替代文档，AI 直接生成代码](https://x.com/dotey/status/2078388657979838830) ⭐️ 7.0/10

一个使用 Claude Design 和 Claude Opus 4.8 的开发工作流表明，高保真可交互原型可以替代传统产品文档，让 AI 准确生成超过 90% 的最终代码。 这种方法通过消除维护单独文档的需求来简化产品开发，并通过提供比基于文本的文档更直观的可视化交互式规范，提高了 AI 代码生成的准确性。 该工作流包含三个步骤：首先，向 Claude Opus 4.8 提交功能需求以生成原型；其次，反复打磨原型；第三，原型确认后，让 AI 实现最终代码。作者使用此方法开发了视频水印工具 BaoCut，且没有维护任何设计文档。

twitter · 宝玉 · 7月18日 07:57

**核验**: 多源印证

**背景**: Claude Design 是 Anthropic 推出的一款工具，用户描述原型、演示文稿或一页纸的内容，Claude 即可生成草稿。Claude Opus 4.8 是 Anthropic 的最新模型，拥有 100 万 token 的上下文窗口和强大的计算机使用能力。高保真原型是可交互的模型，能模拟真实的用户交互和数据，比静态文档更直观。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/design">Claude Design | Turn Ideas into Design | Claude by Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-8">Introducing Claude Opus 4.8 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8">What's new in Claude Opus 4.8 - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#AI developer tools`, `#Claude Design`, `#high-fidelity prototyping`, `#AI-assisted development`, `#workflow automation`

---

<a id="item-8"></a>
## [Codex 已能自行编写大部分代码](https://x.com/dotey/status/2078382113171091735) ⭐️ 7.0/10

一位开发者报告称，OpenAI 的 Codex 编程代理现已能自行编写绝大部分代码，人类开发者转而专注于功能定义和结果验证。 这展示了软件开发中的重大转变，像 Codex 这样的 AI 代理能够自主处理实现工作，可能提高生产力并改变人类开发者的角色。 Codex 是 OpenAI 于 2025 年 4 月发布的 AI 编程代理，提供 CLI、桌面应用和 IDE 集成。该观察基于 Codex 团队成员的推文和开发者自身的体验。

twitter · 宝玉 · 7月18日 07:31

**核验**: 多源印证

**背景**: Codex 是 OpenAI 开发的 AI 编程代理，用于编写代码和修复错误等任务。它于 2025 年 4 月以 Codex CLI 形式发布，可通过 ChatGPT、桌面应用和 IDE 集成使用。它旨在通过从自然语言提示生成代码来协助开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in your terminal · GitHub</a></li>

</ul>
</details>

**标签**: `#Codex`, `#AI developer tools`, `#开发经验`, `#行业判断`, `#AI agents`

---

<a id="item-9"></a>
## [Codex 用浏览器绕道暴露 AI 代理低效](https://x.com/steipete/status/2078318731785359634) ⭐️ 7.0/10

Peter Steinberger 观察到，OpenAI 的 Codex 代理因 GitHub API 未阻止此类操作，转而使用浏览器自动化来上传图片到 GitHub 拉取请求。这一变通方法包括打开 Chrome、导航到 PR 并与 macOS 文件选择器交互。 这一观察突显了当前 AI 代理的一个关键局限：当直接 API 可用但未适当约束时，它们常常采用低效的、类人的变通方法。这凸显了需要更好的 API 设计和代理编排来避免此类浪费行为。 Steinberger 提到他在虚拟机中运行 Codex 代理，以防止它们抢夺应用焦点。GitHub API 并未阻止图片上传，但代理却选择了基于浏览器的路径，这揭示了代理能力与最优工具使用之间的差距。

follow_builders · Peter Steinberger · 7月18日 03:19

**核验**: 多源印证

**背景**: 像 OpenAI Codex 这样的 AI 代理旨在通过推理和操作计算机来自动化软件工程任务。计算机使用代理（CUA）可以通过点击和按键与图形用户界面（GUI）交互，类似于人类用户。然而，当直接 API 存在时，使用它们通常比模拟人类交互更高效、更可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/trycua/acu">GitHub - trycua/acu: A curated list of resources about AI agents for Computer Use, including research papers, projects, frameworks, and tools. · GitHub</a></li>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 该帖子的 48 条回复可能讨论了 AI 代理使用浏览器自动化处理本可由 API 直接完成的任务的讽刺和低效。一些人可能认为这反映了当前代理推理的状态，而另一些人可能指出需要更好的 API 集成或代理训练。

**标签**: `#AI agents`, `#Codex`, `#GitHub`, `#automation`, `#developer tools`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="11"><span>其他追踪推文</span><span class="archive-tab-count">11</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="12"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">12</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2078542101340442638">@dotey: Claude 前一段时间把每周限额临时提升了 50%，客观说效果还是挺好的，要是用 Opus 4.8 的话比 GPT 5.6 还耐用，不过架不住 Codex 一天天重置。 这个活动本来要...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月18日 18:07 UTC · 喜欢 40 · 转发 1 · 回复 17 · 浏览 16801</p>
<p class="archive-item-content">Claude 前一段时间把每周限额临时提升了 50%，客观说效果还是挺好的，要是用 Opus 4.8 的话比 GPT 5.6 还耐用，不过架不住 Codex 一天天重置。<br>
<br>
这个活动本来要到期了，现在延期一个月了，感觉一个月后可能要变成常态了。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/ClaudeDevs/status/2078511173759324328">@ClaudeDevs: We&#x27;re also keeping Claude Code weekly limits 50% higher, now through August 19, for all Pro,...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月18日 16:04 UTC · 喜欢 14677 · 转发 946 · 回复 1173 · 浏览 1410661</p>
<p class="archive-item-content">We&#x27;re also keeping Claude Code weekly limits 50% higher, now through August 19, for all Pro, Max, Team, and seat-based Enterprise users.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2078493011177005136">@dotey: 模型发布苦不苦，想想 Gemini 3.5 (pro) 好歹都高光过，总比胎死腹中要好……</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月18日 14:52 UTC · 喜欢 100 · 转发 2 · 回复 25 · 浏览 39308</p>
<p class="archive-item-content">模型发布苦不苦，想想 Gemini 3.5 (pro)<br>
<br>
好歹都高光过，总比胎死腹中要好……</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2078474596970586387">@op7418: Anthropic 刚才再次大规模封号，很多用了好几年的号也都被封了，我刚买的也没了</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月18日 13:38 UTC · 喜欢 243 · 转发 8 · 回复 176 · 浏览 83309</p>
<p class="archive-item-content">Anthropic 刚才再次大规模封号，很多用了好几年的号也都被封了，我刚买的也没了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2078469760472518801">@op7418: Anthropic 可真鸡贼啊！ 从 20 号开始，Fable 5 的限额会相较于之前再减少 25%，相当于缩水了一半。 因为从 5 月开始到 7 月 19 号，他们有一个政策是会员的周...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月18日 13:19 UTC · 喜欢 50 · 转发 0 · 回复 41 · 浏览 34930</p>
<p class="archive-item-content">Anthropic 可真鸡贼啊！<br>
<br>
从 20 号开始，Fable 5 的限额会相较于之前再减少 25%，相当于缩水了一半。<br>
<br>
因为从 5 月开始到 7 月 19 号，他们有一个政策是会员的周限额会提高 50%，等于是你在 5 月到现在，所有的总限额是正常情况下的 150%。<br>
<br>
所以，Fable 5 的限额其实是你原来应该得到限额的 75%。<br>
<br>
但是从 19 号这个活动结束以后，你的 Fable 5 和你总的限额，在不管是 100 美元还是 200 美元的情况下，都会减少 50%。<br>
<br>
所以整体上来看，全都缩水了。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/frankekn/status/2078440886678220819">@frankekn: 此時再回來看這篇, 依然適用</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月18日 11:24 UTC · 喜欢 18 · 转发 6 · 回复 0 · 浏览 7663</p>
<p class="archive-item-content">此時再回來看這篇, 依然適用</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zhang_benita/status/2078438286197239883">@zhang_benita: As Kimi K3 launches, check out our earlier podcast interview with Yang Zhilin, founder of Kim...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月18日 11:14 UTC · 喜欢 527 · 转发 77 · 回复 26 · 浏览 73627</p>
<p class="archive-item-content">As Kimi K3 launches, check out our earlier podcast interview with Yang Zhilin, founder of Kimi. We recorded it right after K2 came out, and so much has changed over the past year. <br>
https://t.co/TV0D5ynm5I</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/Arcadia_Bao/status/2078410186176577765">@Arcadia_Bao: 有种预感即将到来的几个模型会让 K3 光环熄灭的速度比 GLM-5.2 还快</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月18日 09:22 UTC · 喜欢 141 · 转发 0 · 回复 38 · 浏览 70594</p>
<p class="archive-item-content">有种预感即将到来的几个模型会让 K3 光环熄灭的速度比 GLM-5.2 还快</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2078397664954089512">@dotey: 观念会慢慢改变的，因为团队代码也会慢慢变成 AI 维护。 当然前提是团队得普及 GPT 5.6 级别以上的模型。好的模型写的代码水平远超绝大部分人，已经不太需要人类的品味了。</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月18日 08:33 UTC · 喜欢 90 · 转发 4 · 回复 62 · 浏览 30959</p>
<p class="archive-item-content">观念会慢慢改变的，因为团队代码也会慢慢变成 AI 维护。<br>
<br>
当然前提是团队得普及 GPT 5.6 级别以上的模型。好的模型写的代码水平远超绝大部分人，已经不太需要人类的品味了。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/JackchanceLi/status/2078396185048760758">@JackchanceLi: 对于团队协作的代码，我会看代码，因为这是我交付的作品，代表我的品味，后续可能会由他人来维护。 对于个人项目，目前主要关注需求、验收和架构，不太关注具体代码了。</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月18日 08:27 UTC · 喜欢 7 · 转发 0 · 回复 1 · 浏览 30244</p>
<p class="archive-item-content">对于团队协作的代码，我会看代码，因为这是我交付的作品，代表我的品味，后续可能会由他人来维护。<br>
<br>
对于个人项目，目前主要关注需求、验收和架构，不太关注具体代码了。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2078303477630148741">@op7418: 果不其然，Claude 宣布 Fable 5 将会长期内置在 max 和 team premium 的计划里面，限额是 50%。 估计是由于 OpenAI 和 Kimi K3 的推出的压...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月18日 02:18 UTC · 喜欢 90 · 转发 4 · 回复 51 · 浏览 92847</p>
<p class="archive-item-content">果不其然，Claude 宣布 Fable 5 将会长期内置在 max 和 team premium 的计划里面，限额是 50%。<br>
<br>
估计是由于 OpenAI 和 Kimi K3 的推出的压力带来的，这次不延期直接内置了。<br>
<br>
PRO 和其他 team 会员只能通过积分访问。会一次性获得 100 美元的积分 https://t.co/nvLvBIyAsc</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2078364141878952242">Swyx: still true https://t.co/2eYqwze1Ae</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Swyx · 7月18日 06:20 UTC · 喜欢 4 · 转发 0 · 回复 0</p>
<p class="archive-item-content">Swyx shares a link with the comment &#x27;still true&#x27; but provides no explanation or technical value.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2078357435203695071">Zara Zhang: Great video https://t.co/tGU8LfdzFQ</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 7月18日 05:53 UTC · 喜欢 9 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A tweet praising a video without providing any details or technical value.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2078321266524881065">Thibault Sottiaux: And transitively might also have reset other rate limits out there. Let&#x27;s see. You&#x27;re welcome...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月18日 03:29 UTC · 喜欢 1159 · 转发 29 · 回复 111</p>
<p class="archive-item-content">A cryptic tweet suggesting possible reset of rate limits.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2078320950488297917">Thibault Sottiaux: Oops... I did it again. Enjoy reset usage limits for all paid users for Codex and ChatGPT Wor...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月18日 03:28 UTC · 喜欢 9072 · 转发 606 · 回复 1803</p>
<p class="archive-item-content">Thibault Sottiaux announces a reset of usage limits for all paid users of Codex and ChatGPT Work, thanking the team for rapid iteration.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2078310751878647932">Thibault Sottiaux: GPT-5.6 Sol confirmed to be an extremely good model https://t.co/nZaAnFhsPX</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月18日 02:47 UTC · 喜欢 10876 · 转发 432 · 回复 765</p>
<p class="archive-item-content">A tweet announces that GPT-5.6 Sol is confirmed to be an extremely good model, but provides no technical details or context.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2078305023784620342">Guillermo Rauch: 🆓 Sandbox data for downloads. Happy Friday! Time to ship more agents https://t.co/xkRucYqs8I</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 7月18日 02:25 UTC · 喜欢 70 · 转发 5 · 回复 10</p>
<p class="archive-item-content">Guillermo Rauch announces sandbox data for downloads and encourages shipping more agents.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2078303748649320529">Peter Yang: Codex browser use has finally been defeated. https://t.co/qGAIvxtjnJ</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月18日 02:20 UTC · 喜欢 29 · 转发 1 · 回复 12</p>
<p class="archive-item-content">A tweet claiming that Codex browser use has been defeated, but lacking context and technical details.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/claudeai/status/2078302417100394737">Claude: We know this has been frustrating, and we want to give you more certainty about what your pla...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Claude · 7月18日 02:14 UTC · 喜欢 3108 · 转发 121 · 回复 169</p>
<p class="archive-item-content">Claude announces standardizing access at 50% usage for intensive plans to address user frustration.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/claudeai/status/2078302415804379218">Claude: Beginning July 20, Claude Fable 5 will be included in all Max and Team Premium plans, at 50%...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Claude · 7月18日 02:14 UTC · 喜欢 28134 · 转发 4023 · 回复 2494</p>
<p class="archive-item-content">Beginning July 20, Claude Fable 5 will be included in all Max and Team Premium plans, at 50% of limits.<br>
<br>
Pro and Team Standard users will continue to have access to Fable via usage credits, and will receive a one-time $100 credit.<br>
<br>
Demand for Fable has been challenging to predict, which is why we rolled it out to subscription plans in stages, extending access several times as we secured additional capacity.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2078299647689310270">Guillermo Rauch: Ship like @shadcn https://t.co/J6YwECf2Wi</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 7月18日 02:03 UTC · 喜欢 193 · 转发 0 · 回复 9</p>
<p class="archive-item-content">Guillermo Rauch tweets a link with the phrase &#x27;Ship like @shadcn&#x27;, likely endorsing shadcn&#x27;s approach to shipping software.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2078293998398263587">Swyx: alpha only gone when we all stop asking these level of questions and start discussion about o...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Swyx · 7月18日 01:41 UTC · 喜欢 10 · 转发 1 · 回复 3</p>
<p class="archive-item-content">Swyx questions the distinction between on-policy and generalizable agent optimization in the context of Claude.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2078293685238993072">Peter Yang: Legendary episode dropping this weekend featuring the one and only @trq212, who showed me his...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月18日 01:40 UTC · 喜欢 33 · 转发 1 · 回复 4</p>
<p class="archive-item-content">Peter Yang announces an upcoming podcast episode featuring @trq212 discussing AI video workflows.</p>
</article>
</div>
</section>
