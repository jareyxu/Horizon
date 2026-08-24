---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 31 条内容中筛选出 9 条重要资讯。

---

1. [《复杂系统如何失效》（1998）仍是工程师必读之作](#item-1) ⭐️ 9.0/10
2. [Anthropic 最强 AI 模型用户增长乏力，廉价工具更受欢迎](#item-2) ⭐️ 8.0/10
3. [作者分享 agent.md 指南，提升 LLM 辅助代码质量](#item-3) ⭐️ 8.0/10
4. [什么是 Harness？解析 LLM Agent 的控制层](#item-4) ⭐️ 8.0/10
5. [Fable 高昂成本终结 AI 模型改进的免费午餐时代](#item-5) ⭐️ 7.0/10
6. [AI 智能体或让布鲁克斯外科手术团队模式变得可行](#item-6) ⭐️ 7.0/10
7. [AI 辅助开发将数月工作压缩至一天，价值转向高级角色](#item-7) ⭐️ 7.0/10
8. [服务应提供 MCP 或 CLI，而非内置 Agent](#item-8) ⭐️ 7.0/10
9. [Codex 团队发现限流低效问题，明日修复并重置付费用量](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [《复杂系统如何失效》（1998）仍是工程师必读之作](https://how.complexsystems.fail/) ⭐️ 9.0/10

1998 年的经典文章《复杂系统如何失效》正在 Hacker News 上被广泛分享和讨论，并获得 9.0/10 的高分。文章指出，复杂系统尽管有多层防御，仍会不可避免地失效；根因分析常常是误导性的；无故障运行实际上需要经历故障的经验。 这篇文章是可靠性工程、站点可靠性工程和混沌工程的基础文献，持续影响着工程师对分布式系统故障的思考方式。由于现代软件和基础设施日益复杂，文中关于“根因”思维的警示以及可控故障实验的价值，比以往任何时候都更加重要。 这篇文章篇幅简短，常被引用的核心观点包括：复杂系统长期在降级状态下运行；事故之前往往有一系列“准事故”的历史；事后“根因”归因通常是一种简化。文章还指出，无故障运行需要经历故障的经验，这一观点直接启发了混沌工程。

hackernews · shortcrct · 8月23日 15:13 · [社区讨论](https://news.ycombinator.com/item?id=49409473)

**核验**: 多源印证

**背景**: 这篇文章的观点与正常事故理论和高可靠性组织研究的概念相一致，这些理论探讨的是复杂且紧密耦合的系统为何在层层防御下仍会失效。在软件领域，这些思想催生了混沌工程，即通过有意向系统中注入故障，来建立系统抵御动荡条件的信心。该文章常被推荐为从事可靠性、可观测性和事件响应工作的工程师的必读材料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chaos_engineering">Chaos engineering - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Normal_Accidents">Normal Accidents - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_reliability_organization">High reliability organization</a></li>

</ul>
</details>

**社区讨论**: 评论者大多称赞这篇文章是必读之作。tptacek 强调，在复杂系统上做“根因分析”是徒劳的，而且没有亲身经历故障就很难真正理解这一点；jedberg 将文章论点与混沌工程的起源联系起来；stAInley 分享了运维人员的轶事，说明人们如何让降级系统继续运转。还有评论者推荐了 Tom Wessels 的《The Myth of Progress》作为补充阅读。

**标签**: `#complex systems`, `#reliability engineering`, `#failure analysis`, `#chaos engineering`, `#root cause analysis`

---

<a id="item-2"></a>
## [Anthropic 最强 AI 模型用户增长乏力，廉价工具更受欢迎](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) ⭐️ 8.0/10

据《金融时报》报道，Anthropic 最强的 AI 模型在吸引用户方面遇到困难，而更便宜的替代工具正在蓬勃发展。社区讨论指出，定价混乱和词元成本是关键因素，尤其是在使用 Claude 模型进行代理式编码时。 这件事很重要，因为 Anthropic 是领先的 AI 实验室，其定价策略直接影响开发者工具和 AI 代理市场。如果更便宜的工具持续赢得用户，Anthropic 可能需要重新考虑其前沿模型的打包和定价方式。 评论者提到套餐变更带来的困惑，例如 Fable 在$20 套餐中仅提供一周，后来被移到$200 套餐。一些用户怀疑 Opus 5 被刻意做得不如 Opus 4.8，以拉大差距，而词元成本仍是长时间代理式编码会话的最大痛点。

hackernews · naves · 8月23日 18:16 · [社区讨论](https://news.ycombinator.com/item?id=49411102)

**核验**: 多源印证

**背景**: 代理式编码是一种软件开发方式，由自主 AI 代理在最少人工干预下规划、编写、测试和修改代码，不同于等待用户输入的传统 AI 编程助手。词元成本之所以重要，是因为大语言模型按词元处理文本，一个词元大约相当于 4 个字符或 0.75 个英文单词，而各大 AI 提供商都按词元收费，因此长时间自主运行可能变得非常昂贵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-coding">What is Agentic Coding? | IBM</a></li>

</ul>
</details>

**社区讨论**: 讨论中的整体情绪偏负面，用户批评货币化方式令人困惑以及词元成本过高。也有人为顶级模型辩护，称 Fable 无可匹敌，并成功完成了一次 18 小时的自主重构；另一些人则认为，对于大多数日常编码和知识工作，更便宜的模型已经足够好。

**标签**: `#Anthropic`, `#Claude`, `#AI pricing`, `#AI agents`, `#developer tools`

---

<a id="item-3"></a>
## [作者分享 agent.md 指南，提升 LLM 辅助代码质量](https://fabiensanglard.net/agent.md/index.html) ⭐️ 8.0/10

法比安·桑格拉德（Fabien Sanglard）在 fabiensanglard.net 上公开了自己的 agent.md 文件，其中包含一系列提升 LLM 辅助编程代码质量的实用指南。这篇文章在 Hacker News 上引发了关于用 lint 工具强制执行规范、以及将编码规范与 agent 上下文分离的讨论。 随着 AI 编程助手越来越普及，agent.md 文件作为项目级指令直接影响智能体的行为；分享具体指南有助于开发者从 LLM 获得更一致、更高质量的代码。相关讨论还触及了更广泛的工作流问题：编码规范应该放在哪里，以及如何强制执行这些规范。 文章中的指南包括：即使是一行 if 语句也要始终使用花括号、函数名不超过 30 个字符、添加简短注释说明代码块做什么以及为什么，并用 ASCII 图解释完整系统。评论者指出，AGENTS.md 并不是存放这些规则的最佳位置，建议改用 CODING_STANDARDS.md，以免在阅读代码时污染上下文。

hackernews · ibobev · 8月23日 17:59 · [社区讨论](https://news.ycombinator.com/item?id=49410932)

**核验**: 多源印证

**背景**: agent.md（也写作 AGENTS.md）是一种清单文件，供 Claude Code、Cursor、Copilot、Codex 等 AI 编程助手读取，以了解项目约定和指令。与面向人类的 README.md 不同，AGENTS.md 被设计为可跨多种 AI 智能体使用。上下文工程（context engineering）研究表明，这些指令文件的结构和范围会显著影响智能体的表现；把所有内容放在一个文件里，会让助手更难筛选出相关信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agents.md/">AGENTS . md</a></li>
<li><a href="https://hackernoon.com/ai-coding-tip-014-one-agentsmd-is-hurting-your-ai-coding-assistant?embedable=true">AI Coding Tip 014 - One AGENTS . md Is Hurting Your... | HackerNoon</a></li>
<li><a href="https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html">Context Engineering for Coding Agents</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这篇文章有趣且有用，但多人对指南应该放在哪里提出了不同意见。有评论者认为许多规则应该用 lint 工具强制执行，让手写代码也得到同样的反馈；另一位建议将 AGENTS.md 与 CODING_STANDARDS.md 分开，以避免污染上下文；还有一位分享了自己极简的 AGENTS.md，其核心是围绕任务完成的“收敛规则”（convergence rule）。

**标签**: `#AI agents`, `#LLM-assisted coding`, `#code quality`, `#agent.md`, `#developer tools`

---

<a id="item-4"></a>
## [什么是 Harness？解析 LLM Agent 的控制层](https://earendil.com/posts/what-is-a-harness/) ⭐️ 8.0/10

Earendil 发表的一篇文章将“harness”定义为围绕 LLM agent 的脚手架与控制层；Hacker News 上的讨论进一步探讨了 CLI 工具、交接（handoff）和 agent 架构等实践问题。 随着 AI agent 从演示走向生产，真正为开发者创造价值的地方越来越是 harness 而非模型本身，因此建立共同词汇很重要。这篇文章有助于从业者和厂商在架构、工具链和投入方向上达成共识。 这篇文章面向非技术读者，使用了类比；作者后来提出“harness=底盘，model=引擎，fuel=tokens，agent=汽车”的替代类比。社区评论强调内部 CLI 是极具价值的 agent 工具，并指出 CLI、Web UI、模型和提供商之间的交接（handoff）仍是未解决的问题。

hackernews · tosh · 8月23日 14:24 · [社区讨论](https://news.ycombinator.com/item?id=49409092)

**核验**: 多源印证

**背景**: Agent harness 是包裹 LLM 的运维层，将模型连接到工具、记忆、规划循环、沙箱、编排和输出通道，从而把被动的聊天机器人变成真正工作的 agent。它与 Harness.io（CI/CD 产品）是两回事；常见例子包括 Salesforce Agentforce、Claude Agent SDK 和 Princeton 的 HAL。多 agent 系统中的交接（handoff）是相关模式，可通过 supervisor 节点或 agent 子图在 LangChain、OpenAI Agents SDK 等框架中实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chercode.com/en/blog/agent-harness-ai-2026">What Is an Agent Harness ? The Architecture That Makes... | CherCode</a></li>
<li><a href="https://lessie.ai/blog/agent-harness-vs-harness-io">Agent Harness vs Harness .io: Two Completely Different Things With...</a></li>
<li><a href="https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs">Handoffs - Docs by LangChain</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认可这一概念：一位为会计 agent 构建 harness 的从业者强烈推荐内部 CLI，另一位认为 harness 是“下一个前沿”，一旦模型差异尘埃落定，它将成为真正的价值提供者。还有人希望出现能跨 CLI、Web UI、模型和提供商处理交接的 harness，并有人预测“harness”将成为 2026 年的 AI 热词。

**标签**: `#AI agents`, `#harness`, `#LLM tooling`, `#agent architecture`, `#developer tools`

---

<a id="item-5"></a>
## [Fable 高昂成本终结 AI 模型改进的免费午餐时代](https://simonwillison.net/2026/Aug/23/drew-breunig/) ⭐️ 7.0/10

Drew Breunig 在 2026 年 8 月 23 日的文章中提出，Fable 的高成本以及 Opus、5.6、K3、GLM 等现有模型对大多数编码任务已经足够好用，标志着“模型升级等于免费午餐”时代的结束。团队现在不得不有意识地决定哪些编码工作交给哪个模型。 这一观察很重要，因为 AI 编码工作流长期以来依赖新模型以相同或更低价格发布，来自动弥补提示词和工具链中的低效问题。如果这一假设不再成立，使用 Claude 等模型的开发者与团队就必须投入改进编码工具链、上下文策略，并按成本合理分配任务。 Anthropic 于 2026 年 6 月 9 日发布的 Fable 5 虽然达到最先进水平，但定价为每百万输入 token 10 美元、每百万输出 token 50 美元，并支持 100 万 token 的上下文窗口。Breunig 的观点更多是策略性评论而非基准测试结论，他指出 Opus、5.6、K3 甚至 GLM 对大多数代码任务仍然够用。

rss · Simon Willison · 8月23日 19:55

**核验**: 多源印证

**背景**: 多年来，前沿编码模型快速进步，价格却持平或下降，因此开发者可以依赖每次新版本发布来“掩盖”编码工具链和上下文策略中的低效问题。Fable 5 是 Anthropic 于 2026 年 6 月发布的旗舰模型，能力超越此前模型，但价格明显更高。K3 指的是中国公司 Moonshot AI 开发的开源权重模型 Kimi K3，GLM 则是 Z.ai 推出的开源权重模型系列。Breunig 的文章将 Fable 的定价视为“免费午餐”的终结，促使团队优化在编码中如何使用以及在哪里使用 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI coding`, `#Claude`, `#Fable`, `#developer tools`, `#AI economics`

---

<a id="item-6"></a>
## [AI 智能体或让布鲁克斯外科手术团队模式变得可行](https://x.com/dotey/status/2091662478425899254) ⭐️ 7.0/10

一位软件工程评论者认为，Claude Code、Codex 等 AI 编程智能体可能终于让弗雷德·布鲁克斯的“外科手术团队”模式变得可行：由一名有判断力的人担任架构师，AI 智能体负责执行。 这一观点把 AI 开发工具重新定位为组织变革的推动者，而不仅仅是效率提升工具。它意味着小团队甚至单个开发者可能完成过去需要完整跨职能团队才能交付的工作，从而重塑软件组织的结构。 作者运用康威定律和《人月神话》中布鲁克斯的讨论，指出外科手术团队模式当年未能流行是因为顶尖人才稀缺、系统复杂度爆炸以及工具进步改变了团队形态。他认为瓶颈仍然在于人类大脑的工作记忆，因此该模式在中小规模系统上可能极其高效，而超大规模系统仍需要多个“外科医生”各自带领 AI 团队、通过接口契约进行模块化分工。

twitter · 宝玉 · 8月23日 23:02

**核验**: 多源印证

**背景**: 康威定律认为，组织设计出的系统会镜像其沟通结构。《人月神话》中，弗雷德·布鲁克斯提出“外科手术团队”模式：由一名主程序员集中做出所有设计决策，其他专家提供支持，从而把沟通路径从网状变为星型。Claude Code 和 Codex 是能够编辑代码、运行命令并端到端完成任务的 AI 编程智能体，可以充当该模式中的支持团队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/The_Mythical_Man-Month">The Mythical Man-Month - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software Engineering</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software engineering`, `#AI developer tools`, `#Claude Code`, `#Conway's Law`

---

<a id="item-7"></a>
## [AI 辅助开发将数月工作压缩至一天，价值转向高级角色](https://x.com/ixiaowenz/status/2091454090056450445) ⭐️ 7.0/10

作者 @ixiaowenz 观察到，十年前需要写一个多月的项目，如今在 AI 辅助下一天就能完成。过去必须先搭建项目骨架、编写基础类才能开始业务逻辑，现在开发者打开笔记本先写提示词，测试通过后 AI 已承担大部分实现工作。 这一观点挑战了常见的组织策略——把 AI Token 批量分发给基层工程师，只追求每人 20% 的提效。AI 的真正价值在于让高一级角色直接做出完整结果，把过去需要协调数周才能交付的事情压缩到一天完成。 作者区分了个人效率与组织效率：个人效率是“更快地完成眼前这件事”，组织效率是“省掉哪些不值得做的事”。把 AI 杠杆交给只会执行局部指令的人，他们只是把原本一小时的事缩短到半小时，组织层面看不到任何变化。

twitter · Xiaowen · 8月23日 09:14

**核验**: 多源印证

**背景**: AI 辅助开发是指利用大语言模型根据自然语言提示词生成代码，从而减少搭建项目骨架、编写基础类等重复性工作。Token 是 AI 模型处理文本的基本单位，组织会批量购买 Token 并把 AI 工具分发给员工使用。提示词工程（Prompt Engineering）是结构化地向 AI 模型描述任务的方法，已成为软件开发中落地 AI 的关键技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.margrop.net/post/ai-token-context-window-sticky-notes/">AI 为 什 么 总说‘我忘了’？ Token ... | 魔都水滴</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1946958326966489748">什么是提示词？构建提示词的结构化方法有哪些？ - 知乎</a></li>
<li><a href="https://blog.csdn.net/xiazaizhuanyong1231/article/details/80655048">maven生成archetype项目骨架_-darchetype.properties-CSDN博客</a></li>

</ul>
</details>

**标签**: `#AI辅助开发`, `#开发者效率`, `#AI工具`, `#组织效率`, `#个人开发者`

---

<a id="item-8"></a>
## [服务应提供 MCP 或 CLI，而非内置 Agent](https://x.com/dotey/status/2091425749739643124) ⭐️ 7.0/10

AI 评论者 @dotey 在 X 上发文指出，服务和 App 应该提供 MCP 或 CLI 接口，而不是内置自己的 agent，因为大多数用户只会固定使用两三个常用的 agent。该帖已引发 62 条回复，在 AI agent 社区中引起热议。 这一设计原则可能影响 AI 产品与 agent 的集成方式，推动厂商提供开放、可互操作的接口，而不是封闭的自有助手。如果被广泛采纳，用户将能从自己偏好的 agent 中访问任意服务，减少 AI 生态的碎片化。 MCP 是 Anthropic 于 2024 年 11 月推出的开放标准，用于将 AI 系统与外部工具和数据源连接；CLI 则提供基于文本的命令行接口，便于直接以程序化方式访问。这条推文特别主张 MCP 或 CLI 是服务集成的最佳形式，而不是在应用内单独开发 agent。

twitter · 宝玉 · 8月23日 07:22

**核验**: 多源印证

**背景**: AI agent 是使用大语言模型来规划和执行任务的软件系统，通常需要调用外部工具或服务。MCP 将 agent 连接工具和数据的方式标准化，相当于 AI 集成的通用“USB-C 接口”；而 CLI 长期以来是开发者和程序与应用程序交互的标准方式。这条推文反映了行业中的一个更广泛争论：每个应用是否都应该自建 AI 助手，还是应该提供任何 agent 都能使用的标准接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://www.bitsight.com/learn/ai/mcp-model-context-protocol">Model Context Protocol ( MCP ): A Guide to AI Integration</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#MCP`, `#CLI`, `#AI product design`, `#developer tools`

---

<a id="item-9"></a>
## [Codex 团队发现限流低效问题，明日修复并重置付费用量](https://x.com/thsottiaux/status/2091407991736332689) ⭐️ 7.0/10

OpenAI Codex 团队负责人 Thibault Sottiaux 表示，限流问题源于长会话中大量使用图片、Computer History 的高 p95+ 用量，以及一个消耗超出预期的对话标题生成功能。修复将于明天上线，同时所有付费订阅的用量将完全重置。 这直接回应了 Codex 用户在进行高强度 AI 编码会话时遭遇限流的痛点。全面重置能让付费订阅用户立即恢复可用额度，而效率修复有望减少未来的用量峰值，改善长时间 AI 编码工作流的经济性。 修复针对三个原因：多次压缩（compaction）的长会话中的图片处理、Computer History 的高 p95+ 用量，以及一个消耗超出预期的对话标题生成功能。另有一个不相关的效率提升方案将于下周推进；用量重置预计在明天太平洋时间下午 2 点左右进行。

follow_builders · Thibault Sottiaux · 8月23日 06:11

**核验**: 多源印证

**背景**: Codex 是 OpenAI 的 AI 编程智能体，能够处理长时间会话；'compaction（压缩）'是在上下文过大时对对话进行摘要的机制。Computer History 是一项将应用和网站活动转化为可搜索时间线与记忆的功能，ChatGPT 和 Codex 都可以使用。Codex 的限流与付费套餐的用量相关，因此低效功能可能导致用户比预期更快耗尽额度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simzhou.com/en/posts/2026/how-codex-compacts-context/">Investigating how Codex context compaction works - Simon's Dream Universe</a></li>
<li><a href="https://learn.chatgpt.com/docs/whats-new">A weekly digest of ChatGPT and Codex features that can change how...</a></li>
<li><a href="https://unrollnow.com/status/2091407991736332689">Thread By @thsottiaux - Update on rate limits in Codex ....</a></li>

</ul>
</details>

**社区讨论**: 这条公告获得了很高的关注（约 1382 个赞和 248 条回复）。在帖子中，Sottiaux 更正了重置时间，说明大约在太平洋时间下午 2 点，而不是 14 点；提供的材料中没有包含更多用户评论细节。

**标签**: `#Codex`, `#rate limits`, `#OpenAI`, `#AI developer tools`, `#usage reset`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="6"><span>其他追踪推文</span><span class="archive-tab-count">6</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="1"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">1</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2091738749734666258">@op7418: 我实在搞不懂那些用 AI 回复的人是什么心理和心态。 这样只会加大你被别人拉黑的概率，而且你的内容一眼就能看出来是 AI 生成的，AI 圈所有人都能看懂。 你转发，我不管，再强调一遍：所...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月24日 04:05 UTC · 喜欢 47 · 转发 1 · 回复 27 · 浏览 6742</p>
<p class="archive-item-content">我实在搞不懂那些用 AI 回复的人是什么心理和心态。<br>
<br>
这样只会加大你被别人拉黑的概率，而且你的内容一眼就能看出来是 AI 生成的，AI 圈所有人都能看懂。<br>
<br>
你转发，我不管，再强调一遍：所有用 AI 回复我的内容的人，我都会拉黑<br>
<br>
这是一个非常吃力不讨好、闲得没事干、浪费 token 的行为，怎么还有人锲而不舍地这么干？</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2091691189531750722">@op7418: Codex 重置了，提到的 Token 过度消耗问题也得到了修复</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月24日 00:56 UTC · 喜欢 11 · 转发 0 · 回复 19 · 浏览 10368</p>
<p class="archive-item-content">Codex 重置了，提到的 Token 过度消耗问题也得到了修复</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2091688655828246890">@thsottiaux: Good Sunday. Reset has been propagated to accounts and we landed some fixes to usage for thin...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月24日 00:46 UTC · 喜欢 6635 · 转发 298 · 回复 984 · 浏览 518182</p>
<p class="archive-item-content">Good Sunday. Reset has been propagated to accounts and we landed some fixes to usage for things mentioned yesterday as issues we found. You should feel a positive difference. More to come tomorrow and will keep communicating.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2091456254669709671">@op7418: 对比得更彻底一点： Ox Alpha 模型、DeepSeek V4 Flash、Vision EXP 模型和 Claude Fable 5 模型，用同样的提示词和同样的参考图进行对比。...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月23日 09:23 UTC · 喜欢 95 · 转发 6 · 回复 54 · 浏览 32709</p>
<p class="archive-item-content">对比得更彻底一点：<br>
<br>
Ox Alpha 模型、DeepSeek V4 Flash、Vision EXP 模型和 Claude Fable 5 模型，用同样的提示词和同样的参考图进行对比。<br>
<br>
Claude Fable 5 在排版细节和方块的色散处理上更好一点 https://t.co/mu2uEjZdTb</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2091396289229664590">@op7418: Ox Alpha 做的这个还是动态的 https://t.co/N4tGAfM2Id</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月23日 05:25 UTC · 喜欢 103 · 转发 5 · 回复 47 · 浏览 28025</p>
<p class="archive-item-content">Ox Alpha 做的这个还是动态的 https://t.co/N4tGAfM2Id</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2091395283028738303">@op7418: Ox Alpha 多模态和代码能力真的牛皮 给了他一张图片，让他用 WebGL 还原这个网页。 他真的做出来了这种 3D 玻璃材质的质感和透视，非常清晰。 最牛逼的是，我如果不是拿原图跟...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月23日 05:21 UTC · 喜欢 281 · 转发 17 · 回复 21 · 浏览 95360</p>
<p class="archive-item-content">Ox Alpha 多模态和代码能力真的牛皮<br>
<br>
给了他一张图片，让他用 WebGL 还原这个网页。<br>
<br>
他真的做出来了这种 3D 玻璃材质的质感和透视，非常清晰。<br>
<br>
最牛逼的是，我如果不是拿原图跟这个图片对比的话，我都以为它是直接把原图垫在下面，只有一些字体上的区别，然后文字的位置、排版细节都是一样的 https://t.co/iyoq9PMS9O</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2091403643815604629">Nikunj Kothari: Few things: 1) These are Twitter DMs. I try to be helpful to as many cold DMs as I can. This...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>几点想法</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 8月23日 05:54 UTC · 喜欢 23 · 转发 0 · 回复 0</p>
<p class="archive-item-content">Author shares brief thoughts on handling cold DMs, avoiding doxxing, and choosing trustworthy advisors.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者分享关于处理陌生私信、不人肉搜索以及选择正确建议来源的几点个人看法。</p>
</article>
</div>
</section>
