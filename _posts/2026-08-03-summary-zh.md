---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 35 条内容中筛选出 6 条重要资讯。

---

1. [Karpathy 称 LLM 已能根据故事生成 3D 渲染](#item-1) ⭐️ 8.6/10
2. [Codex 技巧：用 Sol 指挥 Luna Max 子代理实现产出翻倍](#item-2) ⭐️ 7.12/10
3. [AI 行业公开信揭示开放权重政策分歧](#item-3) ⭐️ 7.0/10
4. [多模态输入对 AI 接地至关重要，DeepSeek 与 Anthropic 在输出上策略不同](#item-4) ⭐️ 7.0/10
5. [Codepilot 0.63.0 更新：新增 AI 素材库与 Deepseek V4 Flash 支持](#item-5) ⭐️ 7.0/10
6. [Karpathy 提出用 100 万 Token 测试 AI 3D 渲染能力](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Karpathy 称 LLM 已能根据故事生成 3D 渲染](https://x.com/karpathy/status/2083749667410727319) ⭐️ 8.6/10

安德烈·卡帕西（Andrej Karpathy）测试了 Anthropic 的 Opus 5 模型，给它《指环王》的第一段文字和 100 万 token 的预算（约 10 美元），模型花了大约两小时编写了 5500 行 three.js 代码，程序化地生成了故事的 3D 渲染。 这标志着 LLM 测试从简单任务（如“生成一个骑自行车的鹈鹕的 SVG”）向雄心勃勃的定制创作的转变，这些创作以前因人力和成本而不可行。它凸显了 LLM 的耐心和低成本如何实现按需生成超定制世界和游戏。 该模型使用程序化生成在 3D 坐标中创建多边形资产和动画，但结果“粗糙”且不完美。卡帕西指出，LLM 难以审计自己的工作，因为它们无法高效地感知视频或玩游戏，只能通过缓慢的截图检查。

twitter · Andrej Karpathy · 8月2日 03:00 · 4 个来源

**核验**: 多源印证

**背景**: Three.js 是一个跨浏览器的 JavaScript 库，利用 WebGL 在网页浏览器中创建和显示动画 3D 计算机图形。程序化生成是一种通过算法而非手动创建数据的方法，常用于视频游戏以自动生成大量内容。Token 预算是指 LLM 在单个请求中可以处理的 token（文本单位）数量上限，直接影响成本和复杂性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Three.js">Three.js</a></li>
<li><a href="https://en.wikipedia.org/wiki/Procedural_generation">Procedural generation</a></li>

</ul>
</details>

**社区讨论**: 评论者反应不一：有人认为不完美的结果可作为物理世界理解的新基准，而另一些人则质疑可重复性，并指出 Anthropic 模型可能专门针对 three.js 代码进行了训练。一些人分享了类似的使用 LLM 生成 3D 动画的经验，还有人指出即使是创建可玩的弹球游戏这样的简单任务仍然难倒前沿 LLM。

**标签**: `#AI agents`, `#LLM capabilities`, `#code generation`, `#3D rendering`, `#technical insight`

---

<a id="item-2"></a>
## [Codex 技巧：用 Sol 指挥 Luna Max 子代理实现产出翻倍](https://x.com/AYi_AInotes/status/2083867265179537565) ⭐️ 7.12/10

Codex 中的一项新技巧允许用户提示 Sol 代理自动配置 Luna Max 子代理，通过任务委托将额度消耗减半并使编码产出翻倍。 该方法通过将昂贵的 Sol 用于规划和审核，而将更便宜的 Luna Max 用于有明确边界的任务，显著降低了使用 Codex 的成本，在不增加订阅费用的情况下使生产力翻倍。 该技巧需要在 `~/.codex/agents/luna-worker.toml` 创建自定义代理配置文件，设置模型为 `gpt-5.6-luna` 和 `reasoning_effort = max`，或者直接指示 Sol 为批量任务生成独立的 Luna Max 线程。

aihot · X：阿易 AI Notes (@AYi_AInotes) · 8月2日 10:47 · [中文阅读](https://aihot.virxact.com/items/cmsbowa0l0m77rohvw8s15ia1)

**核验**: 多源印证

**背景**: Codex 是 OpenAI 开发的 AI 编程代理，用于辅助软件工程任务。它提供不同的模型层级：Sol（能力最强、最贵）、Terra（中等）和 Luna（最快、最便宜）。Luna Max 是指将 Luna 模型与最大推理努力（max reasoning effort）结合使用，从而提升其在有明确边界任务上的表现。子代理功能允许在 Codex 内部委派特定任务，从而实现本文所述的编排模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">OpenAI Codex ( AI agent ) - Wikipedia</a></li>
<li><a href="https://x.com/Voxyz_ai/status/2083545774768402673">Vox on X: "Codex tip: tell Sol to configure 𝗟𝘂𝗻𝗮 𝗠𝗮𝘅 𝗮𝘀 𝗮 𝘀𝘂𝗯𝗮𝗴𝗲𝗻𝘁. 𝗽𝗿𝗼𝗺𝗽𝘁: create a custom agent named luna_worker at ~/.codex/agents/luna-worker.toml. use these settings: model = "gpt-5.6-luna" model_reasoning_effort = "max" give it a description and instructions for bounded delegated work. preserve the rest of my config. validate it against my installed Codex version, show me the diff, then use luna_worker for subagent tasks." / X</a></li>
<li><a href="https://www.reddit.com/r/codex/comments/1vbfcdo/wtf_no_palpable_difference_between_sol_medium_and/">r/codex on Reddit: wtf.... no palpable difference between sol medium and luna-xhigh or luna-max</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，用户确认了 Sol + Luna Max 组合的有效性。一些用户分享了额外技巧，例如在直接子代理支持有限时使用线程来运行 Luna 子代理。Reddit 上的讨论质疑了 Sol Medium 与 Luna Max 之间的性能差异，但总体认为这是一种实用且有价值的优化。

**标签**: `#Codex`, `#AI agents`, `#automation`, `#cost optimization`, `#developer tools`

---

<a id="item-3"></a>
## [AI 行业公开信揭示开放权重政策分歧](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

微软于 2026 年 7 月 24 日发布了一封题为《开放权重与美国 AI 领导力》的公开信，由包括英伟达、亚马逊和 OpenAI 在内的 235 家公司签署，主张不应因安全担忧而禁止开放权重模型。随后，Anthropic 发布了自身立场反对蒸馏，而超过 1300 名前沿 AI 公司员工签署了《掌控前沿》公开信，呼吁国际社会共同治理自动化 AI 开发。 这些公开信标志着 AI 政策的一个重要时刻，主要行业参与者公开辩论开放权重模型的安全与创新权衡。其结果可能影响美国政府对 AI 开发的监管，并塑造开放与封闭 AI 生态系统之间的未来平衡。 值得注意的是，Anthropic 未签署微软的公开信，而是单独发布了回应，强调威权政府滥用模型的风险，并呼吁打击工业规模的蒸馏行为。由 OpenAI 首席科学家和 Anthropic CEO 等知名 AI 研究人员签署的《掌控前沿》公开信，表达了对竞争压力通过自动化研究加速 AI 进展的担忧。

rss · Simon Willison · 8月2日 04:16

**核验**: 多源印证

**背景**: 开放权重模型发布训练好的神经网络权重供下载和微调，但与开源 AI 不同，它们通常不包含训练数据或完整的开发代码。蒸馏是一种模型从另一个模型的输出中学习的技术，一些公司如 Anthropic 将其视为安全风险。随着先进 AI 模型能力增强和滥用担忧加剧，关于开放权重的辩论日益激烈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pbs.org/newshour/science/whats-the-difference-between-closed-open‑source-and-open-weight-ai-a-researcher-explains">What's the difference between closed, open‑source and open-weight AI? A researcher explains | PBS News</a></li>
<li><a href="https://www.fierce-network.com/content/open-weight-ai-vs-open-source-ai-whats-difference">Open-weight AI vs. open-source AI: What’s the difference?</a></li>

</ul>
</details>

**标签**: `#AI development`, `#open weights`, `#open source AI`, `#AI policy`, `#industry analysis`

---

<a id="item-4"></a>
## [多模态输入对 AI 接地至关重要，DeepSeek 与 Anthropic 在输出上策略不同](https://x.com/xleaps/status/2083915353185296650) ⭐️ 7.0/10

分析师 Eric Xu（@xleaps）在 X 上发帖详细解释了多模态输入（尤其是视觉）对于 AI 在人类中心世界中运行不可或缺的原因，并对比了 DeepSeek 和 Anthropic 在 AGI 开发中共同避免多模态输出的策略。 这一澄清厘清了被滥用的‘多模态’概念，并揭示了 AGI 开发中的一个根本性战略分歧：多模态输入对于 AI 在现实世界中落地至关重要，而 DeepSeek 和 Anthropic 等领先实验室则将多模态输出视为可分离的工程问题，而非 AGI 的核心能力。 作者认为，多模态输入（尤其是视觉信号）有助于 AI 在人类中心的世界模型（即围绕人类感官构建的世界）中实现接地。DeepSeek 和 Anthropic 避免多模态输出，因为它涉及扩散/流匹配、分布坍缩和多步一致性等工程挑战，这些可以从通用智能中外化。DeepSeek 的非 API、非开放权重版本已经可以处理视觉信号，一些企业用户正在尝试给 DeepSeek 嫁接 Vision Transformer（ViT）。

twitter · Eric Xu (e/Mettā) · 8月2日 13:58

**核验**: 多源印证

**背景**: 人择原理源自宇宙学，认为宇宙的参数是为有意识生命精细调节的；在 AI 中，它意味着世界是围绕人类感官构建的，因此 AI 必须接受这些模态才能有效交互。AI 中的接地（grounding）是指将模型输出锚定到可验证的外部来源，以确保准确性并减少幻觉。Vision Transformer（ViT）是一种专为计算机视觉设计的 Transformer 架构，它将图像分割成小块并通过自注意力机制处理，使语言模型具备视觉理解能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/人择原理">人择原理 - 维基百科，自由的百科全书</a></li>
<li><a href="https://decagon.ai/glossary/what-is-ai-grounding">What is AI grounding? How it works & why it prevents hallucinations | Decagon | Decagon</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论中观点不一：JUNDE WU 认为多模态是一种能力而非智力，对 AGI 不重要；而 3X Long Labubu 反驳称纯语言无法描述音视频信号，因此多模态是必需的。Y.H 质疑对 AGI 路径的确定性，BinaryTree 则引用 DeepSeek-OCR 论文作为 DeepSeek 积极研究视觉输入的证据，反驳了其忽视多模态的说法。

**标签**: `#multimodal`, `#AI`, `#grounding`, `#DeepSeek`, `#Anthropic`

---

<a id="item-5"></a>
## [Codepilot 0.63.0 更新：新增 AI 素材库与 Deepseek V4 Flash 支持](https://x.com/op7418/status/2083827624070234507) ⭐️ 7.0/10

Codepilot 0.63.0 版本新增了素材库功能，用户可以将任何 AI 生成的内容（如 Codex 中使用 GPT-Image 2.0 生成的图片和 AI 生成的 HTML）保存到素材库并添加标签。同时适配了 Deepseek V4 Flash 0731 模型，增加了可选的推理强度参数。 此次更新将 Codepilot 从单纯的编码工具转变为更通用的 AI 代理桌面，使用户能够跨不同模型组织和复用 AI 生成的资产。对 Deepseek V4 Flash 的支持为编码和推理任务提供了强大且经济高效的选择，扩展了开发者的工具能力。 素材库支持标签分类管理。Deepseek V4 Flash 0731 是一个稀疏混合专家模型，总参数 284B，激活参数 13B，针对编码、推理和代理工作流进行了优化。可选的推理强度参数让用户控制模型的推理深度。

twitter · 歸藏(guizang.ai) · 8月2日 08:09

**核验**: 多源印证

**背景**: Codepilot 是一个开源的多模型 AI 代理桌面，最初作为编码工具，现已发展为通用助手工作空间，包含角色文件、持久记忆和每日签到等功能。GPT-Image 2.0 是 OpenAI 最新的图像生成模型，是 DALL-E 的继任者，以改进的文本渲染和多语言支持著称。Deepseek V4 Flash 是 Deepseek 的一系列高效模型，0731 版本是经过重新训练后的版本，特别适合代理工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/op7418/CodePilot">GitHub - op7418/CodePilot: A multi-model AI agent desktop ...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek -ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT_Image">GPT Image</a></li>

</ul>
</details>

**社区讨论**: 社区反馈包括对 Linux 版本的请求，表明用户对跨平台支持的兴趣。另一条评论似乎是垃圾信息或无关内容。总体而言，讨论有限但显示了用户对更新的关注。

**标签**: `#Codepilot`, `#AI developer tools`, `#product update`, `#AI-generated content`, `#Deepseek`

---

<a id="item-6"></a>
## [Karpathy 提出用 100 万 Token 测试 AI 3D 渲染能力](https://x.com/op7418/status/2083764056994017647) ⭐️ 7.0/10

Andrej Karpathy 加入 Anthropic 后首次发布长帖，提出一项新测试：给 Claude Opus 5 约 100 万 Token 的预算，要求它生成三个 3D 渲染版本来讲述《指环王》的故事。模型成功生成了 3D 渲染，但 Karpathy 指出一个关键问题：AI 在生成过程中无法连续感知自己的工作，只能分段截图。 这项测试超越了简单的图像生成基准（如“骑自行车的鹈鹕”），用复杂的长期创作任务挑战 AI。它暴露了当前 AI 系统在自我监控和长时间生成过程中保持连贯性的根本局限，这对电影制作、游戏开发和长内容创作等应用至关重要。 Karpathy 使用了 Claude Opus 5，该模型拥有高达 100 万 Token 的上下文窗口。模型生成了 3D 渲染，但过程显示 AI 无法连续感知自己的输出，只能间隔截图，丢失了帧之间的连续状态。

twitter · 歸藏(guizang.ai) · 8月2日 03:57

**核验**: 多源印证

**背景**: 大型语言模型中的上下文窗口定义了模型一次能处理的最大 Token 数量。Claude Opus 5 是 Anthropic 于 2026 年 7 月发布的强大代理编码模型，拥有大上下文窗口。传统的 AI 基准测试通常涉及根据文本提示生成简单图像，而 Karpathy 的测试通过要求在大 Token 预算下生成连贯的 3D 叙事，推动了边界，突显了在长时间生成任务中保持自我意识和连续性的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/opus">Claude Opus \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/">Tokens and Context Windows in LLMs - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#AI testing`, `#Karpathy`, `#Anthropic`, `#AI limitations`, `#3D generation`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="4"><span>其他追踪推文</span><span class="archive-tab-count">4</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="11"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">11</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2083958428045820092">@op7418: 可能很多朋友不知道，Code Pilot 是全平台的一个软件。 而且支持 Cloud Code、AI SDK 和 CodeX 三种 Agent 框架的切换，以及市面上所有主流和常见 To...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月2日 16:49 UTC · 喜欢 13 · 转发 1 · 回复 29 · 浏览 8563</p>
<p class="archive-item-content">可能很多朋友不知道，Code Pilot 是全平台的一个软件。<br>
<br>
而且支持 Cloud Code、AI SDK 和 CodeX 三种 Agent 框架的切换，以及市面上所有主流和常见 Token Plan 的使用，还有各种自己做的特殊功能。<br>
<br>
前段时间上这个版本重构的时候，短暂地去掉了 Linux 版本的构建，0.64.0 现在 Linux 版本已经重新加入了。<br>
<br>
各位 Linux 用户，如果不知道用啥 Agent 的，可以试试。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2083921281951617148">@op7418: 玩玩 Midjourney https://t.co/C2fx2QRFKt</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 8月2日 14:22 UTC · 喜欢 29 · 转发 0 · 回复 3 · 浏览 7573</p>
<p class="archive-item-content">玩玩 Midjourney https://t.co/C2fx2QRFKt</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2083783368475361697">@dotey: AJ 这 3D 渲染测试确实比鹈鹕骑自行车靠谱多了👍</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月2日 05:14 UTC · 喜欢 37 · 转发 0 · 回复 73 · 浏览 21172</p>
<p class="archive-item-content">AJ 这 3D 渲染测试确实比鹈鹕骑自行车靠谱多了👍</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2083755374994415904">@petergyang: I&#x27;m feeling spicy tonight so let me just say it: I think Opus 4.6 was the Opus model with the...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.3 out of 10">5.3</span>
</div>
<p class="source-line">Twitter/X · @dotey · 8月2日 03:22 UTC · 喜欢 2432 · 转发 83 · 回复 385 · 浏览 227856</p>
<p class="archive-item-content">I&#x27;m feeling spicy tonight so let me just say it:<br>
<br>
I think Opus 4.6 was the Opus model with the best personality and writing style.<br>
<br>
Something&#x27;s off with Opus 5 - it tends to give me overly long replies, use Claude-speak way too much (e.g., &quot;here&#x27;s the honest truth&quot;), and is too judgemental. <br>
<br>
Opus used to be a joy to talk to like a trusted friend. Not so much anymore.</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2083759812970786997">Peter Steinberger: After accepting for years that GMail is blinding me I finally asked my agent and it installed...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Steinberger: 忍受 Gmail 刺眼多年后，我终于让我的代理安装了解决方案</p>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 8月2日 03:40 UTC · 喜欢 239 · 转发 10 · 回复 48</p>
<p class="archive-item-content">Peter Steinberger shares that he used an AI agent to install a solution for GMail&#x27;s blinding brightness.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Steinberger 分享了他使用 AI 代理自动安装工具来解决 Gmail 界面过亮问题的个人经历。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2083755374994415904">Peter Yang: I&#x27;m feeling spicy tonight so let me just say it: I think Opus 4.6 was the Opus model with the...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 8月2日 03:22 UTC · 喜欢 751 · 转发 19 · 回复 165</p>
<p class="archive-item-content">I&#x27;m feeling spicy tonight so let me just say it:<br>
<br>
I think Opus 4.6 was the Opus model with the best personality and writing style.<br>
<br>
Something&#x27;s off with Opus 5 - it tends to give me overly long replies, use Claude-speak way too much (e.g., &quot;here&#x27;s the honest truth&quot;), and is too judgemental. <br>
<br>
Opus used to be a joy to talk to like a trusted friend. Not so much anymore.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2083753582160191988">Swyx: one of my curses as organizer is i rarely get to attend the conference i run. so i basically...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：作为组织者的一个诅咒是我很少能参加自己举办的会议。所以我基本上...</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 8月2日 03:15 UTC · 喜欢 53 · 转发 3 · 回复 12</p>
<p class="archive-item-content">Swyx reflects on rarely attending his own conference, recommends a talk on &#x27;fighting slop with slop,&#x27; and discusses the value of slop-tolerant AI-native programming languages.</p>
<p class="archive-item-translation"><span>中文摘要</span>Swyx 反思自己很少能参加自己举办的会议，推荐了一场关于“以次充好对抗次品”的演讲，并讨论了容忍次品的 AI 原生编程语言的价值。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/danshipper/status/2083750803437724016">Dan Shipper: AI creates more work for human experts https://t.co/j3r4aTuQoi https://t.co/ruFncXlpmu</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Dan Shipper：AI 为人类专家创造更多工作</p>
<p class="source-line">Follow Builders · X 动态 · Dan Shipper · 8月2日 03:04 UTC · 喜欢 34 · 转发 2 · 回复 2</p>
<p class="archive-item-content">Dan Shipper claims that AI increases workload for human experts.</p>
<p class="archive-item-translation"><span>中文摘要</span>Dan Shipper 认为人工智能实际上增加了人类专家的工作量。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/karpathy/status/2083749667410727319">Andrej Karpathy: We&#x27;re starting to leave the territory where you&#x27;d test an LLM by e.g. &quot;create an svg of pelic...</a></h3>
<span class="score-badge" data-tier="low" aria-label="? out of 10">?</span>
</div>
<p class="source-line">Follow Builders · X 动态 · Andrej Karpathy · 8月2日 03:00 UTC · 喜欢 9895 · 转发 674 · 回复 595</p>
<p class="archive-item-content">We&#x27;re starting to leave the territory where you&#x27;d test an LLM by e.g. &quot;create an svg of pelican on a bicycle&quot;. As one idea to generalize it, I was interested what Opus 5 would do if I gave it the first paragraph of the Lord of the Rings, a 1M token budget (~$10) and asked for three js render of it. Opus went off for ~2 hours and wrote 5500 lines of code that (procedurally) rendered the story. It&#x27;s kind of janky but fun. But it&#x27;s a bit mindboggling that the LLM has to place and orchestrate various polygon assets in (x,y,z) coordinates and write code that animates it all, and that it even does anything at all.<br>
<br>
I also like this kind of examples because no one in their right mind would ever spend the time to write something this custom but LLMs have all the stamina and patience in the world, so it&#x27;s an example where we go from &quot;no one would ever do this&quot; to &quot;sure, why not, it&#x27;s ~free&quot;. There might be a lot more. But I&#x27;m excited about creating hyper custom worlds that you can imagine dropping players into, e.g. here to participate in the LoTR story as a spectator NPC, or one of the characters, or etc. Something like an ephemeral GTA of X on demand.<br>
<br>
Last thought is that the domain o...</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2083743952319225938">Zara Zhang: Agency is the most important human quality The world will try to box you, label you, define y...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang: 主动性是人类最重要的品质</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 8月2日 02:37 UTC · 喜欢 68 · 转发 5 · 回复 4</p>
<p class="archive-item-content">Zara Zhang tweets that agency is the most important human quality and encourages resisting external definitions.</p>
<p class="archive-item-translation"><span>中文摘要</span>Zara Zhang 发推文表示主动性是人类最重要的品质，并鼓励抵制外界的定义和标签。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2083738503851258201">Zara Zhang: When asked that question, send them a copy of The Innovator’s Dilemma https://t.co/pkLhEvTZxc</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang: 当被问到那个问题时，给他们一本《创新者的窘境》</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 8月2日 02:15 UTC · 喜欢 22 · 转发 1 · 回复 1</p>
<p class="archive-item-content">Recommends reading The Innovator&#x27;s Dilemma as a response to a certain question.</p>
<p class="archive-item-translation"><span>中文摘要</span>推荐在回答某个问题时，给对方一本《创新者的窘境》。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/amasad/status/2083730074147389898">Amjad Masad: Cool! https://t.co/n0rX8Poczi</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Amjad Masad: 酷！https://t.co/n0rX8Poczi</p>
<p class="source-line">Follow Builders · X 动态 · Amjad Masad · 8月2日 01:42 UTC · 喜欢 32 · 转发 0 · 回复 3</p>
<p class="archive-item-content">Amjad Masad expresses excitement about an unknown link.</p>
<p class="archive-item-translation"><span>中文摘要</span>Amjad Masad 对一个未知链接表示兴奋。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/danshipper/status/2083727039048118304">Dan Shipper: this tweet under review as further details emerge https://t.co/QVF9CjxF5s</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Dan Shipper: 此推文正在审查中，更多细节待公布</p>
<p class="source-line">Follow Builders · X 动态 · Dan Shipper · 8月2日 01:30 UTC · 喜欢 29 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A tweet stating that it is under review with no further details provided.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文表示正在审查中，没有提供更多信息。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2083726824924737971">Nan Yu: Oh, and pangram issue itself, obviously</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nan Yu: 哦，还有全字母句问题本身，显然</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 8月2日 01:29 UTC · 喜欢 0 · 转发 0 · 回复 0</p>
<p class="archive-item-content">A brief mention of a pangram issue without elaboration.</p>
<p class="archive-item-translation"><span>中文摘要</span>简短提及全字母句问题，没有详细说明。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2083722999430050281">Nan Yu: You should be able to pledge tokens for issues that you open and open source repos. Write a s...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nan Yu: 你应该能够为你提出的问题和开源仓库质押代币。写一个规范...</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 8月2日 01:14 UTC · 喜欢 28 · 转发 0 · 回复 13</p>
<p class="archive-item-content">A proposal to allow pledging tokens for open source issues, with GitHub passing accepted issues to a cloud coding agent at the requester&#x27;s expense.</p>
<p class="archive-item-translation"><span>中文摘要</span>一个提议，允许为开源问题质押代币，GitHub 将接受的问题传递给云端编码代理，费用由请求者承担。</p>
</article>
</div>
</section>
