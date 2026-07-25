---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> 从 63 条内容中筛选出 14 条重要资讯。

---

1. [Claude Opus 5 发布：性能提升，无数据保留](#item-1) ⭐️ 10.0/10
2. [Anthropic 为 Claude Opus 5 精简 Claude Code 系统提示词超 80%](#item-2) ⭐️ 8.38/10
3. [Flux 3 Mimic：用于机器人控制的视频-动作模型](#item-3) ⭐️ 8.3/10
4. [Claude Code v2.1.219 新增 Opus 5 模型及开发者增强功能](#item-4) ⭐️ 8.0/10
5. [编码已解决，软件为何更糟？](#item-5) ⭐️ 8.0/10
6. [大模型与产品创新必须协同进化](#item-6) ⭐️ 8.0/10
7. [黄仁勋开推特账号，力挺开源 AI](#item-7) ⭐️ 8.0/10
8. [Codex 集成 GPT Live 语音模型，实现免提编程](#item-8) ⭐️ 8.0/10
9. [蚂蚁百灵发布 Ling-3.0-flash 原生混合推理模型](#item-9) ⭐️ 7.88/10
10. [Anthropic 与 Andon Labs 联合发布 Drone-Bench 基准测试](#item-10) ⭐️ 7.83/10
11. [Boris Cherny 称 Opus 5 是最难被提示注入的模型](#item-11) ⭐️ 7.0/10
12. [BaoCut 新增视频画面翻译功能，支持 Agent 自动化](#item-12) ⭐️ 7.0/10
13. [国际象棋自动研究代理在 LLM 微调中达到博士级水平](#item-13) ⭐️ 7.0/10
14. [AI 是专家的力量倍增器](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Claude Opus 5 发布：性能提升，无数据保留](https://www.anthropic.com/news/claude-opus-5) ⭐️ 10.0/10

Anthropic 发布了其新的旗舰 AI 模型 Claude Opus 5，在编码、专业工作和长期运行的代理任务方面性能均有提升。与之前的 Fable 模型不同，Opus 5 对通用访问不施加任何数据保留要求。 此次发布为组织提供了一个兼具强大性能和无数据保留义务的顶级模型，解决了采用的关键障碍。这也表明 Anthropic 继续致力于将 Opus 层级作为最强大的产品，用于复杂的代理工作流程。 Opus 5 是 Opus 层级的阶段性改进，支持长期运行的代理，并在编码和专业工作方面带来提升。该模型的系统卡提供了技术细节，提示文档强调了行为差异，例如在禁用思考时的响应冗长和代理叙述。

hackernews · alvis · 7月24日 16:57 · [社区讨论](https://news.ycombinator.com/item?id=49038433) · [中文阅读](https://aihot.virxact.com/items/cmrz7mrck00gprox8j0j9qfst) · 5 个来源

**核验**: 多源印证

**背景**: Claude 是 Anthropic 开发的一系列大型语言模型，使用宪法 AI 进行训练以确保伦理合规。自 Claude 3 以来，每一代都发布了三种尺寸：Haiku、Sonnet 和 Opus，其中 Opus 是最强大的。2026 年，Anthropic 推出了 Claude Mythos 和后来的 Claude Fable（一个具有更严格安全措施的版本），但 Fable 要求 30 天数据保留。Opus 5 延续了 Opus 系列，没有此类保留要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus">Claude Opus</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5">Prompting Claude Opus 5 - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者强调，没有数据保留要求是相对于 Fable 的一大优势，使 Opus 5 对组织更具可访问性。早期测试显示 Opus 5 在图像到 HTML 转换方面优于 Fable，尽管有人指出 Opus 5 在写作风格上保留了某些 Fable 已摒弃的 'Claude 特色'。

**标签**: `#Claude Opus 5`, `#Anthropic`, `#AI model`, `#product launch`, `#developer tools`

---

<a id="item-2"></a>
## [Anthropic 为 Claude Opus 5 精简 Claude Code 系统提示词超 80%](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 8.38/10

Anthropic 在其新一代 Claude Opus 5 和 Claude Fable 5 模型中，删除了 Claude Code 超过 80% 的系统提示词，且编码评测成绩未出现明显下降。 这表明新一代模型需要的显式指令更少，简化了提示工程，使 AI 编码代理更高效、更易用。 被删除的提示词包括相互矛盾的指令，如“适当留下文档”和“不要添加注释”，这些指令迫使模型协调重叠的约束。Anthropic 现在转而依赖模型的判断力和上下文信息。

aihot · Claude：Blog（网页） · 7月24日 17:25 · [中文阅读](https://aihot.virxact.com/items/cmrz7ov4300lfrox82ri8kia1)

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 开发的智能编码代理工具，帮助开发者编辑文件、运行命令并加速交付。上下文工程是指通过系统提示词、技能、CLAUDE.md 文件和记忆等元素来引导 AI 行为的实践。此前，Anthropic 使用大量系统提示词来防止意外删除文件等最坏情况，但 Opus 5 等新模型能够在更少的显式指导下处理此类决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://www.promptingguide.ai/guides/context-engineering-guide">Context Engineering Guide | Prompt Engineering Guide</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI models`, `#context engineering`, `#Anthropic`

---

<a id="item-3"></a>
## [Flux 3 Mimic：用于机器人控制的视频-动作模型](https://bfl.ai/blog/flux-3-mimic) ⭐️ 8.3/10

Black Forest Labs 与 Mimic Robotics 合作推出了 FLUX-mimic，这是一种从视频生成中提取世界模型来控制工业机器人的视频-动作模型，已在奥迪进行测试。 这项工作表明，视频生成模型内在地包含可用于物理控制的世界表征，从而连接了生成式 AI 与机器人技术。它可能通过利用大规模视频预训练来加速机器人学习。 FLUX 3 是一个多模态流模型系列，联合训练图像、视频和音频，其中视频预测占训练算力的 95% 以上。加入动作预测后，视频生成质量最初下降最多 10%，但经过 3500 步微调后恢复原有水平。

hackernews · kensai · 7月24日 09:31 · [社区讨论](https://news.ycombinator.com/item?id=49033127) · [中文阅读](https://aihot.virxact.com/items/cmrywwsva05zgrolgrh7uc4ls) · 2 个来源

**核验**: 多源印证

**背景**: 视频-动作模型旨在统一视频预测和动作生成以用于机器人技术，其中视频提供丰富的场景信息，动作提供动力学信息。世界模型是模拟环境的内部表征，最近的研究表明，大型视频生成模型隐式地学习了这种表征。FLUX-mimic 提取这个世界模型用于直接机器人控制，代表了生成式视频模型的一种新颖应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bfl.ai/blog/flux-3-mimic">FLUX 3 x mimic : The Next Generation of Video-Action Models</a></li>
<li><a href="https://runtimewire.com/article/black-forest-labs-flux-3-mimic-audi-robots">Mimic Robotics connects FLUX 3 to industrial robots at... - RuntimeWire</a></li>
<li><a href="https://korshunov.ai/en/article/13955-black-forest-labs-releases-flux-3-multimodal-flow-models-and-flux-mimic-robotics/">Black Forest Labs releases FLUX 3 multimodal flow models and...</a></li>

</ul>
</details>

**社区讨论**: 社区认为这种方法很有趣，并指出这是视频生成实验室转向机器人领域的首个实例。一些评论者提出了关于解耦表征的技术担忧，而其他人则赞赏欧洲初创公司之间的合作。少数人对机器人反复尝试重新安装车窗饰条感到不安。

**标签**: `#AI agents`, `#robotics`, `#video generation`, `#world models`, `#AI research`

---

<a id="item-4"></a>
## [Claude Code v2.1.219 新增 Opus 5 模型及开发者增强功能](https://github.com/anthropics/claude-code/releases/tag/v2.1.219) ⭐️ 8.0/10

Claude Code v2.1.219 引入了 Claude Opus 5 模型，支持 100 万 token 上下文。同时新增了沙箱网络严格白名单、DirectoryAdded 钩子以及多项错误修复和改进。 此版本通过更强大的模型和改进的安全控制显著增强了 Claude Code 的能力。Opus 5 模型的 100 万上下文窗口可处理更大的代码库，而严格白名单和新钩子则改善了开发者的工作流程和安全性。 Opus 5 快速模式定价为每百万输入 token 10 美元，每百万输出 token 50 美元。子代理现在默认可以嵌套生成最多 3 层，沙箱网络严格白名单会直接拒绝非白名单主机而无需提示。

github · ashwin-ant · 7月24日 17:14

**核验**: 多源印证

**背景**: Claude Code 是 Anthropic 推出的 AI 编程助手，可与开发环境集成。它使用子代理来执行代码探索和生成等专门任务。模型上下文协议（MCP）是一个开放标准，用于将 AI 助手连接到外部工具和数据源。DirectoryAdded 钩子允许 Claude Code 在会话期间加载来自额外目录的设置和钩子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>
<li><a href="https://madplay.github.io/en/post/claude-code-subagent-architecture">Claude Code Subagents : How Is Work Divided and... | MadPlay</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI developer tools`, `#product release`, `#Anthropic`, `#AI models`

---

<a id="item-5"></a>
## [编码已解决，软件为何更糟？](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/) ⭐️ 8.0/10

文章指出，尽管编码工具和人工智能取得了进步，但由于非技术决策者优先考虑变化而非改进，以及糟糕的用户体验实践，软件质量正在下降。 这一批评引起了许多开发者和用户的共鸣，他们觉得更新往往降低功能而非增强功能，突显了科技行业中用户体验被表面变化所牺牲的系统性问题。 文章特别提到了 macOS 更新引发恐惧、Slack 窃取焦点等例子，以及软件每次更新都变得更差的普遍趋势。它还指出，AI 代码生成加快了开发速度，但并未提高正确性的信心。

hackernews · pchm · 7月24日 09:08 · [社区讨论](https://news.ycombinator.com/item?id=49033004)

**核验**: 已核对原文

**背景**: 这篇文章建立在关于软件质量与功能速度之间长期争论的基础上。近年来，非技术产品经理和设计师的崛起将焦点从稳健、用户友好的软件转移到频繁的视觉和功能变化上，这些变化常常破坏现有的工作流程。社区讨论呼应了这些担忧，用户感叹更新失去了兴奋感，以及决策角色中充斥着冒名顶替者。

**社区讨论**: 评论表达了对文章论点的强烈认同。用户分享了更新引发恐惧的个人经历，批评非技术决策者优先考虑变化而非质量，并强调了具体的用户体验失败，如焦点窃取。一位评论者还指出，AI 代码生成加速了开发，但不能确保正确性，需要额外努力进行验证。

**标签**: `#software quality`, `#user experience`, `#development experience`, `#tech industry`, `#Hacker News`

---

<a id="item-6"></a>
## [大模型与产品创新必须协同进化](https://x.com/istdrc/status/2080713146080383107) ⭐️ 8.0/10

Twitter 用户 @istdrc 发表长文，认为大语言模型的发展与产品创新必须协同进化，产品的成功选择模型能力，模型能力也反过来选择产品，并以 Manus、Claude Code 和 Anthropic 的 Agent Teams 等为例。 这一观点挑战了 AI 将削弱软件产品的悲观看法，强调人类的适应力和创造力将推动新的人机交互形态，模型能力也会被产品设计所塑造。 该长文具体指出，Transformer 通过翻译产品被选择，工具使用能力通过 LLM 补全工具指令被选择，智能体任务通过 Manus 被选择，编程能力通过 Claude Code 被选择，团队协作能力通过内部的 Agent Teams 和 Claude Tag 被选择，并预测 AGI 正在通过这种协同进化逐步到来。

twitter · stdrc · 7月24日 17:54

**核验**: 多源印证

**背景**: Manus 是由 Butterfly Effect 开发的自主 AI 智能体，可以执行任务和自动化工作流。Claude Code 是 Anthropic 的智能编程工具，帮助开发者理解代码库、编辑文件和运行命令。Anthropic 的 Agent Teams 允许协调多个 Claude Code 实例协同完成复杂任务。该长文认为这些产品和模型能力是协同进化的，彼此推动发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://code.claude.com/docs/en/agent-teams">Orchestrate teams of Claude Code sessions - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM development`, `#product innovation`, `#Claude Code`, `#co-evolution`

---

<a id="item-7"></a>
## [黄仁勋开推特账号，力挺开源 AI](https://x.com/op7418/status/2080659283340087565) ⭐️ 8.0/10

英伟达 CEO 黄仁勋开通了自己的 Twitter 账号并发布了第一篇帖子，公开支持开源 AI 模型，主张美国不应为了保护少数头部公司而限制中国的开源模型。 这是美国关于是否限制中国开源 AI 模型的持续讨论中，首位明确表态的行业头部 CEO，可能影响政策走向，并凸显了开放生态对 AI 创新的重要性。 黄仁勋的帖子呼吁为初创公司和研究机构提供更多算力，建设共享数据集和评估体系，并避免因潜在风险而过早限制开源模型。

twitter · 歸藏(guizang.ai) · 7月24日 14:20

**核验**: 多源印证

**背景**: 美国政府和企业界近期一直在讨论是否要限制中国的开源 AI 模型（如 DeepSeek），理由是国家安全担忧。英伟达作为领先的 AI 硬件供应商，受益于广泛采用需要其 GPU 的 AI 模型。黄仁勋的立场与其公司对广泛 AI 生态系统的利益一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chaobro.com/posts/china-open-source-ai-multipolar-2026">国 产 开 源 AI 不再一家独大：GLM、Kimi、MiniMax 全面崛起 - ChaoBro</a></li>
<li><a href="https://www.jiuyangongshe.com/a/1hr38fk6b1j">20260625盘前： AI 算 力 进入“数十年 基 建”叙事，工业5G与量子硬件发酵</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#NVIDIA`, `#Jensen Huang`, `#AI policy`, `#AI ecosystem`

---

<a id="item-8"></a>
## [Codex 集成 GPT Live 语音模型，实现免提编程](https://x.com/op7418/status/2080486709729587300) ⭐️ 8.0/10

Codex 现已集成 OpenAI 的 GPT Live 实时语音模型，开发者可以完全通过语音指令与编码代理交互，无需任何键盘输入。 此次更新使 Codex 成为真正的免提开发工具，开发者可以通过自然对话进行编码、审查和管理任务，这可能会极大地提高生产力，并让更多用户能够轻松使用。 GPT Live 采用全双工架构，可以同时进行听和说。该功能支持 AirPods 等无线耳机，并保持待命状态，随时准备执行命令。

twitter · 歸藏(guizang.ai) · 7月24日 02:54

**核验**: 多源印证

**背景**: Codex 是 OpenAI 推出的一款 AI 编码代理，可帮助开发者自动化处理拉取请求、代码审查和重构等任务。GPT Live 是新一代语音模型，具备全双工能力，能够实现实时、自然的对话。Vibe coding（氛围编程）由 OpenAI 联合创始人 Andrej Karpathy 提出，指开发者用自然语言描述项目并接受 AI 生成的代码而无需仔细审查的编程方式，从而实现快速原型开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT - Live | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**标签**: `#Codex`, `#AI developer tools`, `#voice interaction`, `#vibe coding`, `#product update`

---

<a id="item-9"></a>
## [蚂蚁百灵发布 Ling-3.0-flash 原生混合推理模型](https://mp.weixin.qq.com/s/5ic54FCsy334JJsQcyBr1g) ⭐️ 7.88/10

蚂蚁集团旗下百灵 AI 发布了 Ling-3.0-flash 原生混合推理模型，总参数量 124B，激活参数量仅 5.1B。该模型采用混合线性注意力架构与 1/64 稀疏 MoE，大幅提升了长文本推理效率。 该模型展示了通过稀疏激活和混合注意力实现高效推理的可能性，有望降低长文本任务的计算成本。它为高性价比 AI 推理设立了新标杆，对标甚至超越了上一代旗舰模型 Ring-2.6-1T。 该模型在长输入下将首 Token 时延（TTFT）降低了 60%至 80%，并在超过 10,000 个可交互训练环境中进行训练。总参数 124B，但每个 token 仅激活 1/64 的专家，因此激活参数仅 5.1B。

aihot · 公众号：蚂蚁百灵（Ling） · 7月24日 13:40 · [中文阅读](https://aihot.virxact.com/items/cmrz0ch8700m7roeygv4eshdv)

**核验**: 多源印证

**背景**: 混合线性注意力将线性注意力机制（如 Mamba）与传统全注意力结合，以平衡效率与质量。稀疏混合专家模型（MoE）每次输入仅激活部分专家网络，在保持模型容量的同时减少计算量。TTFT（首 Token 时延）衡量模型生成第一个输出 token 前的延迟，是用户感知响应速度的关键指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eu.36kr.com/zh/p/3731179814519046">阿里、Kimi、蚂蚁集体押 注 ！ 混 合 注 意 力 从可选项成必答题</a></li>
<li><a href="https://blog.csdn.net/simoncool23/article/details/145329310">什么是稀疏 MoE？Doubao-1.5-pro 如何以少胜多？_稀疏moe-CSDN博客</a></li>
<li><a href="https://tianpan.co/zh/blog/2026-04-16-streaming-ttft-latency-perception">TTFT 才是用户真正感知到的唯一延迟 指 标</a></li>

</ul>
</details>

**标签**: `#AI模型`, `#混合推理`, `#MoE`, `#蚂蚁百灵`, `#长文本推理`

---

<a id="item-10"></a>
## [Anthropic 与 Andon Labs 联合发布 Drone-Bench 基准测试](https://www.anthropic.com/research/project-pilot) ⭐️ 7.83/10

Anthropic 与 Andon Labs 联合发布了 Drone-Bench，这是一个新的基准测试，用于评估 AI 模型自主操控四旋翼无人机在室内环境中进行定位和追踪任务的能力。该基准将任务分解为 3D 地图重建、定位、导航、目标检测和跟随五个子任务，并通过软件仿真实现快速评估。 这一基准测试意义重大，因为它测试了 AI 模型在物理世界中的控制能力，超越了文本和图像任务，迈向现实世界的智能体能力。它提供了一种标准化的方法来衡量 AI 驱动的自动化和机器人技术的进步，可能对监控、物流和搜救等行业产生影响。 该基准测试使用软件仿真来实现快速且可重复的评估，无需使用物理无人机。实验表明，该任务链的难度足以区分不同智能水平的模型，并揭示了 AI 在物理世界操控能力上的进步轨迹。

aihot · Anthropic：Research（发表成果 · 网页） · 7月24日 15:25 · [中文阅读](https://aihot.virxact.com/items/cmrz3eamm01jdroey6e0m62on)

**核验**: 多源印证

**背景**: Drone-Bench 是评估 AI 智能体在交互环境中能力的日益增长的趋势的一部分。传统的 AI 基准测试侧重于静态任务，如语言理解或图像识别，但 Drone-Bench 要求模型在模拟物理世界中执行一系列动作。这不仅测试了感知和规划能力，还测试了实时执行命令的能力。Andon Labs 专注于为 AI 模型创建定制评估，并与包括 Anthropic、Google DeepMind、OpenAI 和 xAI 在内的领先 AI 实验室合作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/project-pilot">Project Pilot: Can AI models fly drones ? \ Anthropic</a></li>
<li><a href="https://andonlabs.com/">Andon Labs develops custom evaluations for AI models</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmark`, `#drone control`, `#physical world AI`, `#Anthropic`

---

<a id="item-11"></a>
## [Boris Cherny 称 Opus 5 是最难被提示注入的模型](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 7.0/10

Anthropic 研究员 Boris Cherny 表示，根据评估和红队测试结果，Claude Opus 5 是目前最不易受提示注入攻击的模型。 这标志着 AI 安全领域的重大进步，因为提示注入是大语言模型的关键漏洞。Opus 5 更强的抵抗力使其成为对安全有高要求的开发者和企业的更可靠选择。 该声明详细记载于 Claude Opus 5 系统卡的第 73 页，其中包含了提示注入评估和红队测试的结果。虽然引用中未给出具体指标，但总体评估是 Opus 5 很难被成功提示注入。

rss · Simon Willison · 7月25日 00:42

**核验**: 多源印证

**背景**: 提示注入是一种网络安全攻击手段，通过精心设计的输入使 AI 模型产生非预期行为，常用来绕过安全防护。红队测试则是模拟对抗性攻击以在部署前发现漏洞。这些概念是 AI 安全的核心，提高对提示注入的抵抗力是模型开发者的关键目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Red_teaming">Red teaming</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#anthropic`, `#claude`, `#ai-safety`, `#generative-ai`

---

<a id="item-12"></a>
## [BaoCut 新增视频画面翻译功能，支持 Agent 自动化](https://x.com/dotey/status/2080770347977113983) ⭐️ 7.0/10

BaoCut 推出了视频画面翻译功能，可以翻译视频中的屏幕文字。该功能可通过 AI Agent（推荐 Codex）自动化操作，支持批量处理，并可直接导出到剪映（CapCut）进行二次编辑。 此次更新将 AI 视频翻译与 Agent 自动化相结合，大幅减少了内容创作者和翻译人员的手动操作。同时，它与流行的免费视频编辑器剪映（CapCut）无缝集成，使其易于被广泛用户使用。 翻译功能采用字幕叠加在原始文字上的方式，而非替换视频帧，便于人工调整。最初的单帧翻译已改为批量队列处理以提高效率，该功能需要 BaoCut v0.8.2 或更高版本。

twitter · 宝玉 · 7月24日 21:41

**核验**: 多源印证

**背景**: BaoCut 是一个开源工具，允许 AI 编程 Agent 驱动视频编辑任务，如转录、添加字幕和翻译。Codex 是 OpenAI 开发的 AI 编程 Agent，可自动化软件工程任务；剪映（CapCut）是一款免费视频编辑器。视频画面翻译功能通过 OCR 检测视频帧中的文字，然后进行翻译，并以字幕形式叠加在原始文字上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jimliu/baocut/">GitHub - JimLiu/ baocut : Open-source Agent Skill that drives the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent)</a></li>
<li><a href="https://capcut.sooftware.com/windows/download">Download CapCut Desktop for free</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#video translation`, `#BaoCut`, `#Codex`, `#automation workflow`

---

<a id="item-13"></a>
## [国际象棋自动研究代理在 LLM 微调中达到博士级水平](https://x.com/amasad/status/2080512523389005894) ⭐️ 7.0/10

Amjad Masad 宣布，他基于国际象棋的自主研究代理（采用 autoresearch 模式）在现代 LLM 微调方面达到了博士级水平。 这表明自主研究代理在 LLM 微调等复杂领域达到专家级水平的潜力，可能加速人工智能研究和开发。 该推文缺乏技术细节，但这一说法建立在 Andrej Karpathy 推广的 autoresearch 模式之上，该模式自主运行实验以优化给定指标。

follow_builders · Amjad Masad · 7月24日 04:36

**核验**: 多源印证

**背景**: Autoresearch 是一种模式，AI 代理自主运行实验、跟踪结果并迭代以改进目标指标。该模式由 Andrej Karpathy 推广，他曾在一夜之间在单个 GPU 上运行了 126 个机器学习实验。此后，该模式已应用于多个领域，包括国际象棋引擎（从专家级提升到大师级）以及现在的 LLM 微调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/deedydas/status/2035551089265906051">Deedy on X: "Karpathy's Autoresearch pushed my vibecoded Rust chess engine AI from "expert" to a top 50 grandmaster, a #311 chess engine. It ran over 70 experiments on its own and tried to hill climb to the top ELO score it could, landing at 2718! https://t.co/PmsldNe4tc" / X</a></li>
<li><a href="https://docs.rs/crate/autoresearch/0.2.1">autoresearch 0.2.1 - Docs.rs</a></li>
<li><a href="https://github.com/paperfoot/autoresearch-cli">GitHub - paperfoot/autoresearch-cli: Autonomous AI experiment loop CLI -- run research overnight with any coding agent · GitHub</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM finetuning`, `#autonomous research`, `#chess`, `#AI research`

---

<a id="item-14"></a>
## [AI 是专家的力量倍增器](https://x.com/levie/status/2080471989060559336) ⭐️ 7.0/10

Box 首席执行官 Aaron Levie 认为，AI 是专家的力量倍增器，使他们能够产出更高质量的成果，并强化了专业化的重要性。 这一观点反驳了 AI 会贬低人类专业知识的担忧，反而表明随着 AI 工具的进步，深厚的领域知识变得更加关键。 Levie 指出，在没有现有专业知识或学习兴趣的情况下使用 AI 会产生‘垃圾’且经济价值很低。专家能够正确引导 AI 代理，并将其输出整合到有用的工作中。

follow_builders · Aaron Levie · 7月24日 01:55

**核验**: 已核对原文

**背景**: ‘力量倍增器’是军事战略中的一个概念，指能够提升部队效能的属性。在 AI 语境下，它意味着 AI 工具放大熟练专业人士的生产力和输出质量，而非取代他们。Aaron Levie 是云内容管理公司 Box 的首席执行官，以其对技术和商业的评论而闻名。

**标签**: `#AI`, `#productivity`, `#expertise`, `#specialization`, `#force multiplier`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="16"><span>其他追踪推文</span><span class="archive-tab-count">16</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="8"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">8</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2080705912923406495">@op7418: 🐂🍺 王冠新的文章，非常清晰且易于理解的描述了当前两条通向 AGI 的路径</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月24日 17:25 UTC · 喜欢 22 · 转发 4 · 回复 5 · 浏览 9788</p>
<p class="archive-item-content">🐂🍺 王冠新的文章，非常清晰且易于理解的描述了当前两条通向 AGI 的路径</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2080704247495029208">@dotey: 猜猜今天哪家会重置额度？ 我估计 Codex 和 Claude Code 都会重置</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月24日 17:18 UTC · 喜欢 71 · 转发 0 · 回复 31 · 浏览 36971</p>
<p class="archive-item-content">猜猜今天哪家会重置额度？<br>
我估计 Codex 和 Claude Code 都会重置</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2080703521364861277">@op7418: 笑死 Anthropic 这么草台？ 这 Opus 5 的测试成绩分数标红不太对吧 53.4 大于 53.5？ https://t.co/ZB6p8bhKo9</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月24日 17:15 UTC · 喜欢 95 · 转发 1 · 回复 33 · 浏览 46459</p>
<p class="archive-item-content">笑死 Anthropic 这么草台？<br>
<br>
这 Opus 5 的测试成绩分数标红不太对吧<br>
<br>
53.4 大于 53.5？ https://t.co/ZB6p8bhKo9</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2080701514402730046">@dotey: Anthropic 今天发布了 Claude Opus 5。API 价格为每百万输入 Token 5 美元、输出 Token 25 美元，与上一代 Opus 4.8 完全相同，但只有 F...</a></h3>
<span class="score-badge" data-tier="high" aria-label="9.0 out of 10">9.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月24日 17:07 UTC · 喜欢 61 · 转发 7 · 回复 17 · 浏览 61057</p>
<p class="archive-item-content">Anthropic 今天发布了 Claude Opus 5。API 价格为每百万输入 Token 5 美元、输出 Token 25 美元，与上一代 Opus 4.8 完全相同，但只有 Fable 5 的一半。官方给出的定位是：以一半的价格，提供接近 Fable 5 的前沿智能。<br>
<br>
Fable 5 是 Anthropic 于 6 月 9 日发布的最强公开模型，输入、输出价格分别为每百万 Token 10 美元和 50 美元，是史上最昂贵的通用模型。同一底座的 Mythos 5 则只向 Project Glasswing 的少数合作伙伴开放。<br>
<br>
【1】性能<br>
<br>
在 Frontier-Bench v0.1 上，Opus 5 的成绩是 Opus 4.8 的两倍多，单任务成本反而更低。在 CursorBench 3.2 上，使用最高 Effort 档时，它与 Fable 5 峰值成绩的差距不到 0.5%，每项任务的成本却只有后者的一半。<br>
<br>
【注：Effort 是可调节的思考强度档位。档位越高，模型思考得越多，价格也越高。】<br>
<br>
ARC-AGI 3 测试的是模型解决未见过的新题的能力，Opus 5 的得分达到第二名模型的三倍。Zapier AutomationBench 测试的是模型能否将一项业务从头到尾完整执行；在成本相同的情况下，Opus 5 的任务通过率约为第二名的 1.5 倍。即使使用最低 Effort 档，它完成的任务也比其他所有模型更多。在电脑操作评测 OSWorld 2.0 上，它仅用 Fable 5 三分之一出头的成本，就超过了后者的最佳成绩。<br>
<br>
在有机化学任务上，Opus 5 比 Opus 4.8 高出 10.2 个百分点；在蛋白质相关任务上，则高出 7.7 个百分点。<br>
<br>
【2】几个比分数更能说明问题的例子<br>
<br>
有一道题给了 Opus 5 一张机械零件图纸，要求它编写代码，在 FreeCAD 中重建三维模型，但故意不让模型直接“看”图。Opus 5 自己编写了一套计算机视觉流程，从原始像素中提取几何形状，再还原出整个零件，而且能够反复成功。同样配置下，其他模型尝试五次都没能完成。<br>
<br>
在一个开源包管理器的真实 Bug 中，社区补丁遗漏了一个边界情况。Opus 5 找到了根因，并补上了这个缺口；对照模型则只修复了表面症状，随后便宣布 Bug 已解决。<br>
<br>
一位交易公司的工程师使用 Opus 5，在一个会话中完成了新交易所的行情数据接入。由于找不到实时数据进行验证，Opus 5 便自行搭建了一套测试框架，用来检查解析结果是否正确。<br>
<br>
【3】谁现在就能用<br>
<br>
Claude Max 的默认模型已经切换为 Opus 5，Pro 用户目前能够使用的最强模型也是它。开发者可以通过 `claude-opus-5` 调用 API。Fast 模式的速度约为普通模式的 2.5 倍，价格则翻倍。<br>
<br>
此次上线的两个 Beta 功能，对开发 Agent 的人很有实际价值。<br>
<br>
一是对话进行到一半时，即使更换工具，也不会导致 Prompt 缓存失效。过去只要修改一次工具列表，整段缓存就会作废，成本随即上升。<br>
<br>
二是 API 可以启用自动降级功能。被安全分类器拦截的请求会自动转交给其他模型处理，而不是直接失败。<br>
<br>
【4】安全与拦截<br>
<br>
Anthropic 表示，Opus 5 是其迄今为止对齐程度最高的模型。在自动化行为审计中，它的综合失准得分为 2.3，低于 Opus 4.8、Sonnet 5 和 Fable 5，欺骗行为所占比例也是最低的。<br>
<br>
网络安全部分有一个值得注意的细节：Anthropic 刻意没有使用网络攻防任务训练 Opus 5，但随着通用能力提升，它发现漏洞的水平已经接近 Mythos 5。不过，在将漏洞转化为可用攻击代码方面，两者仍有很大差距。<br>
<br>
安全分类器允许 Opus 5 在源代码中寻找漏洞，但会拦截二进制层面的漏洞扫描、渗透测试和 Exploit 生成。它的拦截频率比 Fable 5 低约 85%。在 https://t.co/aTfkxmbzQe、Claude Code 和 Cowork 中，被拦截的请求默认会回退至 Opus 4.8。<br>
<br>
生物领域的限制则有所放宽：原本在 Fable 5 上被拦截的生物类请求，现在会转交给 Opus 5，而不是此前的 Opus 4.8。Anthropic 称，Opus 5 是目前面向科研场景能力最强的公开模型，但它在长时间自主研究任务上仍存在明显限制。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2080701512679145525">@op7418: 来了！Opus 5 模型发布，价格跟 Opus 4.8 相同 在测评成绩上大幅优于 Opus 4.8，同时相当多的测评成绩都高于 Fable 5。 终于有个能用的模型了！ 要再不出，我感...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月24日 17:07 UTC · 喜欢 69 · 转发 2 · 回复 23 · 浏览 80569</p>
<p class="archive-item-content">来了！Opus 5 模型发布，价格跟 Opus 4.8 相同<br>
<br>
在测评成绩上大幅优于 Opus 4.8，同时相当多的测评成绩都高于 Fable 5。<br>
<br>
终于有个能用的模型了！<br>
<br>
要再不出，我感觉 Claude Max 都没必要续订了，性价比过低，4.8 跟屎一样 https://t.co/xKBPbQhczz</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/claudeai/status/2080699495453528290">@claudeai: Introducing Claude Opus 5. It&#x27;s a thoughtful and proactive model that comes close to the fron...</a></h3>
<span class="score-badge" data-tier="high" aria-label="9.3 out of 10">9.3</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月24日 16:59 UTC · 喜欢 51139 · 转发 6248 · 回复 2624 · 浏览 10403146</p>
<p class="archive-item-content">Introducing Claude Opus 5.<br>
<br>
It&#x27;s a thoughtful and proactive model that comes close to the frontier intelligence of Fable 5 at half the price. https://t.co/GQWhcq2CQL</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/claudeai/status/2080699495453528290">@claudeai: Introducing Claude Opus 5. It&#x27;s a thoughtful and proactive model that comes close to the fron...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月24日 16:59 UTC · 喜欢 51141 · 转发 6248 · 回复 2624 · 浏览 10403146</p>
<p class="archive-item-content">Introducing Claude Opus 5.<br>
<br>
It&#x27;s a thoughtful and proactive model that comes close to the frontier intelligence of Fable 5 at half the price. https://t.co/GQWhcq2CQL</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/Medeo_AI/status/2080687123691196697">@Medeo_AI: https://t.co/mMArfWLfE7</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月24日 16:10 UTC · 喜欢 42 · 转发 10 · 回复 8 · 浏览 10808</p>
<p class="archive-item-content">https://t.co/mMArfWLfE7</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2080683836963463291">@op7418: Sam 居然发声支持了，这下达里奥真成小丑了 https://t.co/DclM8Vdq5S</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月24日 15:57 UTC · 喜欢 142 · 转发 1 · 回复 30 · 浏览 64749</p>
<p class="archive-item-content">Sam 居然发声支持了，这下达里奥真成小丑了 https://t.co/DclM8Vdq5S</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2080662154798334286">@op7418: 微软 CEO 纳德拉也和黄仁勋发了同样的倡议，看起来是要集体给美国政府施压了 https://t.co/R4dums578p</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月24日 14:31 UTC · 喜欢 51 · 转发 2 · 回复 22 · 浏览 19700</p>
<p class="archive-item-content">微软 CEO 纳德拉也和黄仁勋发了同样的倡议，看起来是要集体给美国政府施压了 https://t.co/R4dums578p</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/xleaps/status/2080660249145459052">@xleaps: 大模型是一个专利期十个月的制药生意 https://t.co/I0rf878sFO</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月24日 14:23 UTC · 喜欢 171 · 转发 49 · 回复 10 · 浏览 21684</p>
<p class="archive-item-content">大模型是一个专利期十个月的制药生意 https://t.co/I0rf878sFO</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/JensenHuang/status/2080643682408321103">@JensenHuang: For my first post, I’m sharing a letter @NVIDIA signed on why open models matter. AI will tra...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 7月24日 13:18 UTC · 喜欢 117683 · 转发 20180 · 回复 12008 · 浏览 32935613</p>
<p class="archive-item-content">For my first post, I’m sharing a letter @NVIDIA signed on why open models matter.<br>
<br>
AI will transform every industry, power every company, and be built by every country.<br>
<br>
Open models strengthen safety and cybersecurity, accelerate innovation and diffusion, and enable sovereignty.<br>
<br>
The world needs both frontier closed models and frontier open models.<br>
<br>
https://t.co/AUKzoQ5Ikb</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/bkingfilm/status/2080629975938748875">@bkingfilm: 2015 年我出版了《中国电竞幕后史》 写了三年，走访上百位电竞人，从街机格斗、星际争霸时代写到移动电竞前夜（1996-2014） 今天我把它全文 25 万字开源到 GitHub，免费，比纸书还...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月24日 12:23 UTC · 喜欢 28 · 转发 10 · 回复 2 · 浏览 3245</p>
<p class="archive-item-content">2015 年我出版了《中国电竞幕后史》<br>
<br>
写了三年，走访上百位电竞人，从街机格斗、星际争霸时代写到移动电竞前夜（1996-2014）<br>
<br>
今天我把它全文 25 万字开源到 GitHub，免费，比纸书还多出十几篇未收录章节（2015-2017）<br>
<br>
甚至有几章是《中国游戏幕后史》的开篇，可惜后来我去做游戏纪录片了<br>
<br>
不知道什么时候还有机会把这本书也写完...<br>
<br>
#Esports #Gaming</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2080568327504642119">@dotey: 且不说他早年看不上 Coding Agent（现在已经变了），但到现在 DeepSeek 居然还不支持多模态，确实理解不了</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月24日 08:18 UTC · 喜欢 178 · 转发 6 · 回复 112 · 浏览 95966</p>
<p class="archive-item-content">且不说他早年看不上 Coding Agent（现在已经变了），但到现在 DeepSeek 居然还不支持多模态，确实理解不了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/turingbook/status/2080562981163921469">@turingbook: 说实话，昨天看了梁文锋的长篇讲话，对他的印象是减分的。如果大家关心的话，我可以再展开讲讲哈哈。</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月24日 07:57 UTC · 喜欢 143 · 转发 2 · 回复 234 · 浏览 190819</p>
<p class="archive-item-content">说实话，昨天看了梁文锋的长篇讲话，对他的印象是减分的。如果大家关心的话，我可以再展开讲讲哈哈。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2080519708189560839">@dotey: 以前玩游戏时间长了点有负罪感，觉得虚度光阴了，现在一边玩游戏一边等 Agent 干活，居然有点心安理得。 可能从砍柴变成了放羊？ https://t.co/NT5ZGzMIU4</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 7月24日 05:05 UTC · 喜欢 459 · 转发 27 · 回复 101 · 浏览 51593</p>
<p class="archive-item-content">以前玩游戏时间长了点有负罪感，觉得虚度光阴了，现在一边玩游戏一边等 Agent 干活，居然有点心安理得。<br>
<br>
可能从砍柴变成了放羊？ https://t.co/NT5ZGzMIU4</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2080543574211666029">Thibault Sottiaux: Should we rename ChatGPT Work to ChatGPT Vibe?</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：我们应该把 ChatGPT Work 改名为 ChatGPT Vibe 吗？</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月24日 06:40 UTC · 喜欢 489 · 转发 17 · 回复 488</p>
<p class="archive-item-content">A tweet proposing to rename ChatGPT Work to ChatGPT Vibe, sparking community discussion.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文提议将 ChatGPT Work 更名为 ChatGPT Vibe，引发了社区讨论。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2080537149204758689">Thibault Sottiaux: From Science Fiction to Science Reality. Join the team if you want to work on some of the coo...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：从科幻到科学现实。如果你想从事一些最酷、最具影响力的技术，请加入团队……</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月24日 06:14 UTC · 喜欢 1003 · 转发 20 · 回复 312</p>
<p class="archive-item-content">A recruitment tweet inviting people to join a team working on impactful technology, but lacking any specific details.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条招聘推文，邀请人们加入团队从事有影响力的技术工作，但缺乏具体细节。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/amasad/status/2080513361301925957">Amjad Masad: Autoscale deployments, which is typically the most expensive of scaled apps is down 80%! http...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Amjad Masad：自动扩展部署成本（通常是扩展应用中最昂贵的部分）下降了 80%！</p>
<p class="source-line">Follow Builders · X 动态 · Amjad Masad · 7月24日 04:40 UTC · 喜欢 92 · 转发 6 · 回复 12</p>
<p class="archive-item-content">Amjad Masad announces an 80% reduction in autoscale deployment costs, typically the most expensive part of scaled applications.</p>
<p class="archive-item-translation"><span>中文摘要</span>Amjad Masad 宣布自动扩展部署成本降低了 80%，这通常是扩展应用中最昂贵的部分。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2080508139091427741">Peter Yang: The next evolution is being able to spin up multiple ChatGPT Voice threads so I can have a fu...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：下一个进化是能够启动多个 ChatGPT 语音线程，这样我就可以拥有一个完整的团队与我交谈并相互交流。</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月24日 04:19 UTC · 喜欢 53 · 转发 5 · 回复 8</p>
<p class="archive-item-content">Peter Yang envisions the next evolution of ChatGPT Voice as enabling multiple concurrent voice threads that can interact with the user and each other, forming a team.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 设想 ChatGPT Voice 的下一个进化是能够启动多个并发语音线程，这些线程可以与用户以及彼此交互，形成一个团队。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2080505964936241226">Peter Yang: Before and after with ChatGPT Voice https://t.co/kzNE5odHSy</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：ChatGPT Voice 的前后对比</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月24日 04:10 UTC · 喜欢 97 · 转发 13 · 回复 7</p>
<p class="archive-item-content">A tweet by Peter Yang showing a before/after comparison of ChatGPT Voice, but with no technical details.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 发布的一条关于 ChatGPT Voice 功能前后对比的推文，但缺乏技术细节。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2080505108216111303">Peter Yang: More feedback: 1. It should let me know when the other threads finish working if I have a bun...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang: 更多反馈：1. 它应该在我有多个线程运行时通知我其他线程完成工作...</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 7月24日 04:07 UTC · 喜欢 16 · 转发 0 · 回复 2</p>
<p class="archive-item-content">User provides brief feedback on a tool regarding thread notifications and Chinese pronunciation.</p>
<p class="archive-item-translation"><span>中文摘要</span>用户就工具的线程通知和中文发音提供了简短反馈。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2080500752183960017">Swyx: btw ive been dogfooding an agentic github clone over the past month or so and its gotten quit...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：顺便说一下，过去一个月我一直在内部测试一个智能体化的 GitHub 克隆，它已经变得相当好用。</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 7月24日 03:50 UTC · 喜欢 42 · 转发 0 · 回复 12</p>
<p class="archive-item-content">Swyx is dogfooding an agentic GitHub clone with built-in CI/CD via Workers for Platforms and invites collaboration.</p>
<p class="archive-item-translation"><span>中文摘要</span>Swyx 正在内部测试一个智能体化的 GitHub 克隆，内置基于 Workers for Platforms 的 CI/CD，并邀请合作。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/realmadhuguru/status/2080460579966501257">Madhu Guru: Great builders understand the jagged frontier of AI models. Great leaders understand the jagg...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Madhu Guru: 伟大的建设者理解 AI 模型的锯齿状前沿。伟大的领导者理解他们团队的锯齿状前沿。</p>
<p class="source-line">Follow Builders · X 动态 · Madhu Guru · 7月24日 01:10 UTC · 喜欢 12 · 转发 0 · 回复 2</p>
<p class="archive-item-content">A tweet stating that great builders understand the jagged frontier of AI models, while great leaders understand the jagged frontier of their people.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文指出，伟大的建设者理解 AI 模型的锯齿状前沿，而伟大的领导者理解他们团队的锯齿状前沿。</p>
</article>
</div>
</section>
