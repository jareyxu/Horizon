---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 41 条内容中筛选出 10 条重要资讯。

---

1. [OpenAI Astra 以约 2000 美元解决 10 项数学难题](#item-1) ⭐️ 9.85/10
2. [LLM 流式输出 UI 渲染性能优化策略](#item-2) ⭐️ 8.0/10
3. [Codex 上下文压缩减少新开 Session 的必要性](#item-3) ⭐️ 7.3/10
4. [RipGrep musl 二进制文件在大搜索中段错误，分配器问题导致](#item-4) ⭐️ 7.0/10
5. [Cursor 从使用页面和 CSV 导出中移除费用信息](#item-5) ⭐️ 7.0/10
6. [Datasette-apps 0.2a0 新增 AI 代理工具及隐形 iframe 测试](#item-6) ⭐️ 7.0/10
7. [两步交接摘要法在 Codex 中节省大量 Token 消耗](#item-7) ⭐️ 7.0/10
8. [Swyx 认为 AI 领袖过早放弃 /loop 和 /goal 命令](#item-8) ⭐️ 7.0/10
9. [8B 参数模型国际象棋达到约 1500 Elo，超越前沿模型和 Stockfish Level 0](#item-9) ⭐️ 7.0/10
10. [AI 任务消耗数亿 token，编排层成关键变量](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Astra 以约 2000 美元解决 10 项数学难题](https://x.com/gdb/status/2083457463337287721) ⭐️ 9.85/10

OpenAI 的下一代模型 Astra（内部版）解决了数学和理论计算机科学领域的 10 个长期未解难题，每个问题花费不到 2000 美元（按 GPT-5.6 Sol 代币价格计算）。这些证明已随 Lean 4 形式化验证和思维链逐步推导一同发布。 这展示了人工智能能够以极低成本做出重大研究贡献，可能加速数学发现并改变数学家的角色。同时，它也凸显了形式化验证（Lean）在确保 AI 生成证明正确性方面的强大能力。 解决的难题包括非 sofic 群的存在性、推翻 Connes 刚性猜想、高维球堆积的更好界限、电路复杂度以及多色图中的单色三角形等。OpenAI 发布了一篇论文和一份由 LLM 生成的 PDF，其中重构了推理过程。

aihot · X：Greg Brockman (@gdb) · 8月1日 07:39 · [中文阅读](https://aihot.virxact.com/items/cmsa302cc01xaro41omun2e1h) · 4 个来源

**核验**: 多源印证

**背景**: Lean 是一个用于数学定理形式化验证的证明助手和函数式编程语言。思维链推理是一种提示技术，能引导大型语言模型逐步推理，从而提高其解决复杂问题的能力。Astra 解决的难题，如非 sofic 群的存在性和 Connes 刚性猜想，是至少十年未有进展的重要开放问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chain-of-thought_reasoning">Chain-of-thought reasoning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sofic_group">Sofic group - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论和 Simon Willison 的博客中既有惊叹也有担忧。数学家 Kirwin Hampshire 将此前 AI 成果描述为一场‘深刻的精神危机’，一些评论者希望看到所使用的提示词。总体而言，人们认为这是数学领域的‘深蓝时刻’，既令人兴奋也引发存在性反思。

**标签**: `#AI`, `#Mathematics`, `#OpenAI`, `#Astra`, `#Theorem Proving`

---

<a id="item-2"></a>
## [LLM 流式输出 UI 渲染性能优化策略](https://x.com/xiongchun007/status/2083560171243274256) ⭐️ 8.0/10

一位开发者分享了在 LLM 流式输出模式下优化 UI 渲染性能的实用策略，包括增量追加节点、节流批量更新、使用轻量自定义组件以及分离交互与渲染能力。评论中还建议对长对话使用虚拟滚动。 随着基于 LLM 的应用日益普及，高效的流式 UI 渲染对用户体验至关重要。这些策略帮助开发者避免常见的性能陷阱，构建更流畅、响应更迅速的 AI 界面。 关键建议包括将 UI 更新节流至 100-300 毫秒间隔，对长对话使用虚拟滚动，以及避免使用重型第三方组件，转而采用自定义轻量渲染器。

twitter · 山中大熊 · 8月1日 14:27

**核验**: 多源印证

**背景**: 大型语言模型（LLM）逐 token 生成文本，流式输出将每个 token 实时发送，使用户能够看到逐步生成的响应。然而，每收到一个 token 就更新 UI 会导致过多的重绘和性能下降，尤其是在输出较长时。节流是一种限制 UI 更新速率的技术，通过固定间隔批量更新来平衡响应速度与性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dartmouth.github.io/langchain-dartmouth-cookbook/04-streaming.html">Streaming LLM output — langchain_dartmouth Cookbook</a></li>
<li><a href="https://valiancesolutions.com/learning-hub/optimizing-frontend-performance-with-throttling-and-debouncing/">Optimizing Frontend Performance with Throttling and Debouncing</a></li>

</ul>
</details>

**社区讨论**: 在评论中，用户@iArchiArchi 建议答案是使用'markstream'，而原帖作者补充了第六点：对长对话使用虚拟滚动。该帖子获得了大量关注，浏览量超过 9000 次，并获得众多点赞和转发。

**标签**: `#LLM`, `#流式渲染`, `#UI性能优化`, `#AI Agent`, `#开发经验`

---

<a id="item-3"></a>
## [Codex 上下文压缩减少新开 Session 的必要性](https://x.com/dotey/status/2083620982338486614) ⭐️ 7.3/10

作者 @dotey 分享，随着 Codex 上下文压缩能力的提升，为节约上下文而新开 Session 进行 handoff 的做法已不再必要，使用 /compact 命令或继续在同一 Session 中即可。他还强调，设置严格的验收标准对于确保 AI 编码代理的输出质量至关重要。 这一建议反映了 AI 编码工具的快速演进，上下文管理的改进为开发者节省了时间并减少了 token 消耗。设置验收标准等正确的工作流程直接影响 AI 生成代码的质量，使得这一指导对使用 Codex 和 Claude Code 等工具的开发者非常有价值。 Codex 的上下文压缩现在足够有效，以至于通过新 Session 进行 handoff 已很少需要，但在跨 Agent 场景（如将工作从 Claude Code 传递给 Codex）中仍然有用。作者使用 Claude Code 配合 Fable 5 编写技术方案文档，然后通过 /goal 命令交给 Codex 执行。

twitter · 宝玉 · 8月1日 18:28 · 2 个来源

**核验**: 多源印证

**背景**: AI 编码代理，如 OpenAI 的 Codex 和 Anthropic 的 Claude Code，是在终端或 IDE 中运行的工具，帮助开发者编写和编辑代码。它们维护对话和代码库的上下文窗口，但长会话可能消耗大量 token。Handoff 是将当前状态总结后转移到另一个会话或代理的做法。上下文压缩技术可以在保留重要信息的同时减少 token 使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-codex/">Introducing Codex | OpenAI</a></li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 在评论中，用户 Tz 分享了一种节省 token 的方法：要求生成 handoff 摘要，然后在新 Session 中以此开始。另一位用户 wilbeibi 创建了一个名为 'catchup' 的开源工具，用于跨 Agent 的上下文 handoff。Kenyon 指出，上下文压缩可能仅限于 Codex 调用 GPT 模型时，因为 GPT 的压缩是在服务端进行的。整体情绪积极，用户们验证了这些建议并贡献了额外技巧。

**标签**: `#AI agents`, `#Codex`, `#Claude Code`, `#developer tools`, `#best practices`

---

<a id="item-4"></a>
## [RipGrep musl 二进制文件在大搜索中段错误，分配器问题导致](https://github.com/BurntSushi/ripgrep/issues/3494) ⭐️ 7.0/10

使用 musl libc 编译的 RipGrep 二进制文件在执行极大规模搜索时会出现段错误。根本原因与 musl 的 mallocng 分配器有关，并引发了关于内核补丁和性能影响的讨论。 此漏洞影响使用 musl 构建的 RipGrep 二进制文件用户，这些文件常见于 Alpine Linux 和 Docker 容器等轻量级 Linux 环境。它凸显了在性能关键型工具中选择分配器的重要性，以及 musl 的 mallocng 分配器在多线程工作负载下的持续挑战。 段错误仅出现在链接 musl 的二进制文件中，而不会出现在 glibc 中。社区成员的一份详细分析将问题追溯到 musl 分配器与内核内存管理之间的交互，并提出了一个解决根本原因的内核补丁。

hackernews · throwaway2037 · 8月1日 12:34 · [社区讨论](https://news.ycombinator.com/item?id=49133889)

**核验**: 多源印证

**背景**: RipGrep（ripgrep）是一个命令行工具，用于递归搜索目录中的正则表达式模式，以其速度和遵循 .gitignore 而闻名。musl 是一个为 Linux 设计的轻量级 C 标准库，常用于 Alpine Linux 和 Docker 镜像以减小体积。musl 的默认分配器 mallocng 优先考虑内存效率，但在多线程工作负载下可能面临争用和性能问题，从而导致此类段错误。该问题还涉及一个与虚拟内存管理相关的内核漏洞，加剧了问题的严重性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Musl">Musl</a></li>
<li><a href="https://github.com/burntsushi/ripgrep">GitHub - BurntSushi/ripgrep: ripgrep recursively searches directories for a regex pattern while respecting your gitignore · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区讨论突出了内核补丁和对该漏洞的 AI 生成分析。一些评论者质疑为什么 ripgrep 不替换 musl 的默认分配器为更高效的分配器，鉴于其专注于速度。其他人指出，在 HPC 集群文件系统上使用 ripgrep 是不可取的，因为会产生大量小 I/O 开销。

**标签**: `#ripgrep`, `#musl`, `#segfault`, `#allocator`, `#performance`

---

<a id="item-5"></a>
## [Cursor 从使用页面和 CSV 导出中移除费用信息](https://forum.cursor.com/t/usage-page-to-token-amount-what/167153) ⭐️ 7.0/10

Cursor 从其使用页面和 CSV 导出中移除了美元费用显示，改用 Token 数量。公司表示这一变化部分是有意为之以澄清计费，部分是无意的，CSV 导出问题现已修复。 这一变化引发了社区关于 Token 效率以及 Cursor、Claude Code 和 Codex 等 AI 编码工具之间成本比较的讨论。它凸显了开发者在使用 AI 代理时理解 Token 使用量的重要性。 Cursor 员工指出，美元使用量图表显示的是套餐使用量（以美元计），而非用户实际支付的按需使用量，这造成了混淆。CSV 导出中的美元费用在清理功能标志时被意外破坏，但现已修复。

hackernews · EugeneOZ · 8月1日 15:25 · [社区讨论](https://news.ycombinator.com/item?id=49135257)

**核验**: 多源印证

**背景**: Cursor 是一款 AI 驱动的代码编辑器，是 Visual Studio Code 的分支，由 Anysphere 开发（现为 SpaceXAI 的一部分）。它允许开发者使用自然语言编辑代码、搜索代码库和完成任务。Token 效率是指 AI 模型完成一项任务所使用的 Token 数量，直接影响成本和性能。不同的 AI 编码工具在执行相同任务时，即使使用相同的底层模型，Token 使用量也可能存在巨大差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>
<li><a href="https://www.verdent.ai/guides/model/token-efficient-coding-models-real-project-cost">Token - Efficient Coding Models : Real Project Cost - Verdent Guides</a></li>

</ul>
</details>

**社区讨论**: 讨论聚焦于 Token 效率，用户如 'tosh' 分享了不同框架和模型之间 Token 使用量的巨大差异数据。一些用户如 'aroman' 质疑 Cursor 在 2026 年相对于 Claude Code 和 Codex 的价值，Cursor 员工则澄清了变化。整体情绪是分析性的且略带批评，还有一些关于 Token 取代货币的讽刺评论。

**标签**: `#AI developer tools`, `#Cursor`, `#token efficiency`, `#AI agents`, `#code editors`

---

<a id="item-6"></a>
## [Datasette-apps 0.2a0 新增 AI 代理工具及隐形 iframe 测试](https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything) ⭐️ 7.0/10

Datasette-apps 0.2a0 引入了两个新工具 app_debug() 和 app_list()，以增强 AI 代理的集成能力。app_debug() 工具通过一个不可见的 iframe（opacity: 0, pointer-events: none）让代理在沙盒环境中执行 JavaScript 来对应用进行冒烟测试。 此版本显著提升了 AI 代理以编程方式创建、编辑和测试 Datasette Apps 的能力。它代表了 Datasette 生态系统中更自主的代理工作流程的一步，使代理无需用户交互即可验证应用功能。 app_debug() 工具依赖于 datasette-agent 0.4a0 中新增的 context.browser_task() 机制。隐形 iframe 方法避免了视觉干扰，同时允许代理检查元素尺寸并执行冒烟测试。

rss · Simon Willison · 8月1日 21:23

**核验**: 多源印证

**背景**: Datasette Apps 是一个插件，允许在 Datasette 内部托管自定义 HTML 应用，这些应用在沙盒化的 iframe 中运行，并带有 CSP 头以防止恶意操作。Datasette Agent 是一个用于 Datasette 的 AI 助手，可以编写 SQL 查询并与数据交互。此版本将两者桥接，使代理能够以编程方式管理和测试应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/blog/2026/datasette-apps/">Host applications inside Datasette with Datasette Apps - Datasette Blog</a></li>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps: Host custom HTML applications inside Datasette</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Datasette`, `#developer tools`, `#release`, `#testing`

---

<a id="item-7"></a>
## [两步交接摘要法在 Codex 中节省大量 Token 消耗](https://x.com/Tz_2022/status/2083535287267774908) ⭐️ 7.0/10

一位开发者发现了一种在 OpenAI Codex 中执行连续任务时节省 Token 消耗的两步方法：任务完成后，要求生成一个交接摘要，然后在新会话中将其作为第一条信息发送给 AI。 该方法在不损失上下文质量的前提下大幅降低 Token 消耗，使使用 AI 编程代理的多步骤开发工作流更加经济高效。 交接摘要相当于对之前上下文窗口的极限摘要提取，丢弃了原始代码和日志等冗余信息，只保留核心推理逻辑和任务理解，使 AI 能够轻装上阵。

twitter · Tz · 8月1日 12:48

**核验**: 多源印证

**背景**: OpenAI Codex 是 OpenAI 于 2025 年 4 月发布的一款 AI 编程代理，可协助完成编写代码、修复错误和完成拉取请求等软件工程任务。Token 消耗是使用大型语言模型时的关键成本因素，因为每个处理的 Token 都会产生费用。该方法通过压缩连续任务之间的上下文窗口来优化 Token 使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software Engineering | OpenAI</a></li>

</ul>
</details>

**标签**: `#Codex`, `#token optimization`, `#AI developer tools`, `#workflow automation`, `#handoff`

---

<a id="item-8"></a>
## [Swyx 认为 AI 领袖过早放弃 /loop 和 /goal 命令](https://x.com/swyx/status/2083439562437673053) ⭐️ 7.0/10

Swyx 在推文中表示，他仍然积极使用 Claude Code 中的 /loop 和 /goal 命令，并认为其他 AI 领袖过早放弃这些命令是错误的。他认为这些命令在复杂任务中提供了可操控性和自主性的正确平衡。 Swyx 是 AI 开发者工具领域备受尊敬的声音，他的逆向观点凸显了社区可能存在的过度修正。这表明随着 AI 编码工具的发展，用户可能过早地抛弃了在某些工作流程中仍有价值的有用功能。 Swyx 提到，当你想要可操控性和自主性的正确组合，以及想要开放式“循环生成循环”的最终状态而不深入指定路径时，他会使用 /loop 和 /goal。他举了一个例子，说明在一个非常长的行动推理回合中，设定目标如何救了他。

follow_builders · Swyx · 8月1日 06:27

**核验**: 多源印证

**背景**: Claude Code 中的 /loop 命令是一个会话级调度器，它按指定间隔重复提示，无需手动重新启动。/goal 命令设置一个完成条件，Claude 会持续朝该目标工作，无需每一步都提示，每次轮次后由一个小型快速模型检查条件是否满足。这些命令是 Claude Code 工具使用循环的一部分，Claude 可以读取代码、编辑文件、运行命令以及与外部服务交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/goal">Keep Claude working toward a goal - Claude Code Docs</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-claude-code-loop-command-recurring-tasks">What Is the Claude Code / loop Command ? How to Run... | MindStudio</a></li>
<li><a href="https://www.xda-developers.com/finally-understood-claude-code-goal-command/">I finally understood Claude Code's /goal command after realizing I was using it completely wrong</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#developer tools`, `#Claude Code`, `#AI workflow`, `#practical AI`

---

<a id="item-9"></a>
## [8B 参数模型国际象棋达到约 1500 Elo，超越前沿模型和 Stockfish Level 0](https://x.com/amasad/status/2083424608993300824) ⭐️ 7.0/10

Amjad Masad 宣布，一个 80 亿参数的语言模型在国际象棋中达到了约 1500 Elo，持续击败前沿模型和 Stockfish Level 0。该模型采用高推理和响应链技术，每步仅用 1-2 秒，而其他模型需要 30 秒。 这表明小型高效模型也能实现高水平的推理性能，挑战了复杂任务需要更大模型的假设。这对在资源受限环境中部署 AI 代理以及需要快速决策的实时应用具有重要意义。 该模型是一个 80 亿参数的变体，通过更快的推理和响应链技术超越了 GPT-5.6（可能指某个前沿模型）。它达到了约 1500 Elo，高于人类棋手平均水平，并击败了最低难度设置（Level 0）的 Stockfish。

follow_builders · Amjad Masad · 8月1日 05:28

**核验**: 多源印证

**背景**: Elo 等级分是用于计算国际象棋等竞技游戏中相对技能水平的系统；1500 分被认为高于俱乐部棋手平均水平。Stockfish 是一个强大的开源国际象棋引擎，其技能水平可从 1 调整到 20，Level 0（或 Level 1）代表初学者水平。推理和响应链，也称为思维链提示，涉及将问题分解为中间步骤，以改善 AI 模型的逻辑推理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kingdomofchess.com/how-to-use-stockfish-in-chess/">What is Stockfish ? How It Works, Features & Analysis Guide</a></li>
<li><a href="https://www.ibm.com/think/topics/chain-of-thoughts">What is chain of thought (CoT) prompting? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#chess`, `#small language model`, `#reasoning`, `#Elo rating`

---

<a id="item-10"></a>
## [AI 任务消耗数亿 token，编排层成关键变量](https://x.com/levie/status/2083389460679373135) ⭐️ 7.0/10

Aaron Levie 指出，随着 AI 任务消耗数千万到数亿个 token，编排层（harness）在提升准确性和降低成本方面变得与模型能力同等重要。 这一观点凸显了 AI 堆栈的转变：随着任务复杂度增加，负责分解工作并路由到合适模型的编排层成为影响性能和成本效率的关键因素，对 AI 智能体和工具开发产生深远影响。 Levie 指出，当任务仅消耗数十万到数百万 token 时，编排层并不重要；但当任务消耗数千万到数亿 token 时，它成为关键变量。他承认这些数字可能不适用于所有任务。

follow_builders · Aaron Levie · 8月1日 03:08

**核验**: 多源印证

**背景**: AI 编排层（harness）是一个连接 AI 智能体与工作流、工具、数据、记忆和治理控制的中间层，使智能体能够完成实际任务。随着 AI 智能体承担更复杂的多步骤任务，需要更大的上下文窗口，编排层高效分解工作并路由到最合适模型的能力对于控制成本和保持准确性变得至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blueflame.ai/blog/ai-harnesses-explained">AI Harnesses Explained: The Missing Layer Between AI Models and Investment Workflows</a></li>
<li><a href="https://github.com/ai-boost/awesome-harness-engineering">GitHub - ai-boost/awesome-harness-engineering: Awesome list for AI agent harness engineering: tools, patterns, evals, memory, MCP, permissions, observability, and orchestration. · GitHub</a></li>

</ul>
</details>

**标签**: `#AI stack`, `#harness`, `#orchestration`, `#AI agents`, `#cost efficiency`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="11"><span>其他追踪推文</span><span class="archive-tab-count">11</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="5"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">5</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/Jenny_the_Bunny/status/2083663347925569933">@Jenny_the_Bunny: 这种血的教训真的是得自己踩过坑之后才会发现有多痛。 我们团队也是 3 个月前买.io 域名，但是没买.ai 因为要美金五位数。当时的逻辑是先开始 stealth 开发，验证产品，把价值做到位再说。...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月1日 21:17 UTC · 喜欢 12 · 转发 2 · 回复 5 · 浏览 7464</p>
<p class="archive-item-content">这种血的教训真的是得自己踩过坑之后才会发现有多痛。<br>
<br>
我们团队也是 3 个月前买.io 域名，但是没买.ai 因为要美金五位数。当时的逻辑是先开始 stealth 开发，验证产品，把价值做到位再说。<br>
<br>
但是 2 周前，我在停车场等队友来开门时刷手机突然刷到另一个团队的 launch video。没错，撞名了，而且是竞品。人家买了.ai 的域名并且上个月开始申请注册商标了。晴天霹雳。<br>
<br>
经过一轮激烈讨论后，我们从“跟他们一杠到底”转到了“算了，不值得，还有很多更重要的事情需要我们的精力和时间”。之后我们连夜重新起名、买新域名、改代码。我至今还会经常口误提起那个不再属于我们的名字。<br>
<br>
所以，如果再来一次的话，我也一定会像这个 startup 这样一开始就把域名和商标盘下来。倒也不一定要花 25 万美金这么多，但最起码省去很多后顾之忧。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/middlefeng/status/2083647550775767231">@middlefeng: 我从没有说 code review 要坚持古法，我说的是至少先看到下面的程度。得到的回应是，就是不看 code，宁可去看其它东西（比如最喜爱的 test case）来问问题，就是故意不看...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月1日 20:14 UTC · 喜欢 3 · 转发 2 · 回复 5 · 浏览 3471</p>
<p class="archive-item-content">我从没有说 code review 要坚持古法，我说的是至少先看到下面的程度。得到的回应是，就是不看 code，宁可去看其它东西（比如最喜爱的 test case）来问问题，就是故意不看生成的 code。这就是为了不看而不看。为了 ego 而不看。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/paulg/status/2083628660708561075">@paulg: A recent YC startup spent 250k on a domain. I was slightly shocked. But when I asked how much...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月1日 18:59 UTC · 喜欢 2293 · 转发 41 · 回复 202 · 浏览 345187</p>
<p class="archive-item-content">A recent YC startup spent 250k on a domain. I was slightly shocked. But when I asked how much they raised after YC, the answer was 6.5m. So 1/26 of their round. This is the time we live in; one shocking number counterbalances the other.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2083628609298645065">@dotey: 我一直觉得这种测试只能测试 SVG 画图能力，并不太能体现智能水平，或者有什么理由通过这个测试能反映智能水平？</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月1日 18:59 UTC · 喜欢 35 · 转发 1 · 回复 25 · 浏览 10801</p>
<p class="archive-item-content">我一直觉得这种测试只能测试 SVG 画图能力，并不太能体现智能水平，或者有什么理由通过这个测试能反映智能水平？</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2083620270959480931">@dotey: 为了节约上下文 handoff 新开 Session，这在半年一年前是很好的实践，现在没太有必要，因为 codex 自己上下文压缩做的很好了，或者 /compact 一下继续就足够了。...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月1日 18:25 UTC · 喜欢 63 · 转发 7 · 回复 18 · 浏览 12161</p>
<p class="archive-item-content">为了节约上下文 handoff 新开 Session，这在半年一年前是很好的实践，现在没太有必要，因为 codex 自己上下文压缩做的很好了，或者 /compact 一下继续就足够了。<br>
<br>
当然如果关系不大的任务，还是新开 Session 更好。<br>
<br>
当然除此之外 handoff 还是适用于跨 Agent session 的，比如 Claude Code 里面没完成的 session 让 Codex 继续。<br>
<br>
不过我更习惯于 Claude Code 里面用 Fable 5 写技术方案文档，然后反复 Review、修改后把文档交给 Codex，配合 /goal 让它按照文档执行推进。<br>
<br>
当然设置好严格的验收标准也很有必要，否则它会偷懒。<br>
<br>
之前一个迁移任务没有设置验收标准，它就给我交付了一个差强人意的，离我要求的还有比较大差距。（参考图 1）<br>
<br>
重新加上了验收标准：UI 界面像素要和原版完全一致，那么它每一步都会截图对比像素差异，直到完全一致（或者可以忽略的差异）</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2083579533391777935">@op7418: OpenAI 感觉翻身了啊，已经在预热他们的下一代模型 Astra。 他们用这个模型解决了 10 个至少存在了十年的数学问题。 这些问题如果是数学家解决的话，感觉这数学家已经相当牛逼了；...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月1日 15:44 UTC · 喜欢 75 · 转发 5 · 回复 32 · 浏览 33846</p>
<p class="archive-item-content">OpenAI 感觉翻身了啊，已经在预热他们的下一代模型 Astra。<br>
<br>
他们用这个模型解决了 10 个至少存在了十年的数学问题。<br>
<br>
这些问题如果是数学家解决的话，感觉这数学家已经相当牛逼了；<br>
<br>
而解决这一堆非常难的问题，算力成本居然只有 2000 美元。<br>
<br>
Sam 亲自飞到华盛顿去跟美国政府沟通这个模型的发布，感觉这玩意儿会很顶，不知道是 GPT-6 还是 GPT-5.7</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2083572191845585036">@dotey: 帮转招人信息</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月1日 15:14 UTC · 喜欢 7 · 转发 0 · 回复 9 · 浏览 5119</p>
<p class="archive-item-content">帮转招人信息</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/monday_chen/status/2083530528473444806">@monday_chen: 啊，所以有没有人有兴趣来跟我工作？美国英国都可以 https://t.co/xt9JocSXzH</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月1日 12:29 UTC · 喜欢 3 · 转发 2 · 回复 1 · 浏览 5628</p>
<p class="archive-item-content">啊，所以有没有人有兴趣来跟我工作？美国英国都可以 https://t.co/xt9JocSXzH</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/SebastienBubeck/status/2083456300692979886">@SebastienBubeck: yes, nonsofic groups exist: this statement is one of many new beautiful results proved by Ast...</a></h3>
<span class="score-badge" data-tier="high" aria-label="9.0 out of 10">9.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月1日 07:34 UTC · 喜欢 5479 · 转发 796 · 回复 221 · 浏览 2347409</p>
<p class="archive-item-content">yes, nonsofic groups exist: this statement is one of many new beautiful results proved by Astra, our next major model.<br>
<br>
We&#x27;re releasing 10 such Astra proofs, complete with lean certificates and CoT walkthroughs for each of them. The results are wide-ranging, from von Neumann algebras (disproof of Connes&#x27; Rigidity Conjecture) to better bounds for high dimensional sphere packing, for circuit complexity, for monochromatic triangles in multicolored graphs, and more.<br>
<br>
More thoughts here: https://t.co/8SjXONeh38</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2083434423564009647">@op7418: 重置！</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月1日 06:07 UTC · 喜欢 13 · 转发 0 · 回复 7 · 浏览 8468</p>
<p class="archive-item-content">重置！</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2083395449814229287">@thsottiaux: To celebrate a week of efficiency and let you run 100&#x27;000 Luna threads this weekend... that&#x27;s...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.3 out of 10">3.3</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月1日 03:32 UTC · 喜欢 24013 · 转发 1130 · 回复 2893 · 浏览 1658825</p>
<p class="archive-item-content">To celebrate a week of efficiency and let you run 100&#x27;000 Luna threads this weekend... that&#x27;s right... wait for it... I have reset usage limits for Codex and ChatGPT Work.<br>
<br>
Enjoy.</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2083427516996292992">Thibault Sottiaux: Optimize for curiosity</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>为好奇心优化</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月1日 05:40 UTC · 喜欢 1442 · 转发 70 · 回复 212</p>
<p class="archive-item-content">A tweet encouraging a mindset of optimizing for curiosity.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文，倡导以好奇心为优先的思维方式。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2083395449814229287">Thibault Sottiaux: To celebrate a week of efficiency and let you run 100&#x27;000 Luna threads this weekend... that&#x27;s...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月1日 03:32 UTC · 喜欢 15067 · 转发 869 · 回复 2213</p>
<p class="archive-item-content">To celebrate a week of efficiency and let you run 100&#x27;000 Luna threads this weekend... that&#x27;s right... wait for it... I have reset usage limits for Codex and ChatGPT Work.<br>
<br>
Enjoy.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2083387677945036995">Thibault Sottiaux: ChatGPT Work counted https://t.co/XlnkkYvx1s</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux: ChatGPT Work 已被计数</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 8月1日 03:01 UTC · 喜欢 320 · 转发 5 · 回复 63</p>
<p class="archive-item-content">A tweet stating that ChatGPT Work has been counted, with a link to further information.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文称 ChatGPT Work 已被计数，并附有链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/danshipper/status/2083380721607921904">Dan Shipper: pretty cool to have the kicker in this @WSJ piece on OpenAI vs Anthropic! i stand behind this...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Dan Shipper：很高兴能在《华尔街日报》关于 OpenAI 与 Anthropic 的文章中看到这样的结尾……我支持这个观点……自春初以来就很明显，势头正在转向 OpenAI，这是一个迷人的逆袭故事</p>
<p class="source-line">Follow Builders · X 动态 · Dan Shipper · 8月1日 02:34 UTC · 喜欢 132 · 转发 7 · 回复 20</p>
<p class="archive-item-content">Dan Shipper comments on a WSJ article about OpenAI vs Anthropic, stating that momentum is shifting to OpenAI and calling it a fascinating comeback story.</p>
<p class="archive-item-translation"><span>中文摘要</span>Dan Shipper 评论《华尔街日报》一篇关于 OpenAI 与 Anthropic 的文章，指出势头正在转向 OpenAI，并称之为一个迷人的逆袭故事。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2083369880599015713">Peter Steinberger: Queue was the way but with 5.5 the model doesn’t get confused anymore, you can just throw stu...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Queue 是过去的方式，但 5.5 版本让模型不再混淆，你可以随意向它抛任务，它会勤勉处理。</p>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 8月1日 01:51 UTC · 喜欢 183 · 转发 5 · 回复 33</p>
<p class="archive-item-content">Peter Steinberger notes that with version 5.5, the model no longer gets confused when handling concurrent tasks, allowing users to freely submit work while it processes.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Steinberger 指出，5.5 版本的模型在处理并发任务时不再混淆，用户可以随意提交任务，模型会勤勉处理。</p>
</article>
</div>
</section>
