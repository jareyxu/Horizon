---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> 从 59 条内容中筛选出 12 条重要资讯。

---

1. [OpenAI 声称 AI 智能体破解 Navier-Stokes 变体问题，引发抄袭争议](#item-1) ⭐️ 10.0/10
2. [Kimi K3（2.8T）在 MacBook Pro 上通过四块 SSD 流式运行，速度约 1 token/秒](#item-2) ⭐️ 8.0/10
3. [Qwen3 27B 量化基准测试：4-bit 保持质量，1-bit 崩溃](#item-3) ⭐️ 8.0/10
4. [i-have-adhd 技能阻止编码代理埋没答案](#item-4) ⭐️ 8.0/10
5. [基于网页的 LLM 注意力可视化工具获教育者好评](#item-5) ⭐️ 8.0/10
6. [研究：预训练进步主要来自数据改进](#item-6) ⭐️ 7.5/10
7. [OpenAI 发布 ChatGPT Images 2.5 及双 API 模型](#item-7) ⭐️ 7.3/10
8. [字节跳动秘密研发实时空间视频模型，预计 10 月发布](#item-8) ⭐️ 7.0/10
9. [安全警报：Scoppr 和 Nook 是恶意的 Mole 仿冒版本](#item-9) ⭐️ 7.0/10
10. [GPT-6 Astra 不依赖编译器直接生成二进制可执行文件](#item-10) ⭐️ 7.0/10
11. [DeepSeek V4.1 Flash 发布，增强原生多模态能力](#item-11) ⭐️ 7.0/10
12. [Codex 新增 AI 聊天记录整理与自定义分组功能](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 声称 AI 智能体破解 Navier-Stokes 变体问题，引发抄袭争议](https://x.com/OpenAI/status/2097375276384567642) ⭐️ 10.0/10

OpenAI 宣布，一组使用能力显著超过 GPT-6 Astra 的下一代模型的 AI 智能体，给出了一个与 Navier-Stokes 相关问题的解，并声称流体动力学会在有限时间内形成奇点。这一公告恰逢一场公开争议：数学家 Tristan Buckmaster 指控 OpenAI 试图抢先发布成果，以压制他和 Levent Alpöge 独立利用大语言模型取得的成果。 这标志着 AI 在攻克深度数学问题上的能力发生了范式转变，可能加速数学与物理学领域的研究进度。这场争议也引发了关于研究伦理、用户数据是否被用于模型训练，以及 AI 辅助发现中功劳应如何分配等关键问题。 两个团队都未解决悬赏 100 万美元的完整 Clay 千禧年问题：双方证明的均是光滑外力条件下相关方程（不可压缩多孔介质、Boussinesq 以及三维不可压缩 Euler 方程）的有限时间爆破，对应 Fefferman 表述中的 c 和 d 选项。Buckmaster 的结果于 8 月 22 日通过 Lean 形式化验证，陶哲轩称其为"了不起的成就"，同时指出论文包含大量 AI 生成的内容。

twitter · OpenAI · 9月8日 17:23 · [中文阅读](https://aihot.news/items/cmtsynojw01xqro5wb8n7ysor) · 10 个来源

**核验**: 多源印证

**背景**: Navier-Stokes 存在性与光滑性问题是由 Clay 数学研究所在 2000 年选定的七大千禧年难题之一，每个问题悬赏 100 万美元。它探讨的是由 Navier-Stokes 方程描述的三维光滑流体运动是否会在有限时间内失去光滑性（即"爆破"），这个问题已悬置约 90 年，被视为理解湍流现象的第一步。AI 智能体是能够自主追求目标、使用外部工具并执行多步任务的程序，其控制流通常由大语言模型驱动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier–Stokes Millennium Prize Problem | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 OpenAI 表达了强烈愤怒，指控该公司查看用户数据、窃取一流研究人员成果，并通过威胁迫使其就范。评论者指出，OpenAI 声明中"无法排除"去标识化用户数据帮助改进模型的说法存在模糊性，质疑 Buckmaster 是否选择了退出数据使用。也有人认为，这可能是长期存在的学术竞争在 AI 工具催化下加速上演。

**标签**: `#AI agents`, `#OpenAI`, `#Mathematical breakthrough`, `#Navier-Stokes`, `#AI capabilities`

---

<a id="item-2"></a>
## [Kimi K3（2.8T）在 MacBook Pro 上通过四块 SSD 流式运行，速度约 1 token/秒](https://github.com/argonautlabsai/deltafin) ⭐️ 8.0/10

argonautlabsai/deltafin 项目（gavamedia/deltafin 的一个分支，加入了 ARGODRIVE 存储相关工作）展示了在配备 128 GB 内存的 M5 Max MacBook Pro 上，通过四块 SSD 流式传输 1.45 TB 的专家权重，运行 2.8T 参数的混合专家（MoE）模型 Kimi K3。在生成 512 个 token 的回答时，稳定解码速度达到每秒 1.00 个 token；在公开的 17-token 提示上为每秒 0.96 个 token。 这是一次引人注目的本地大模型推理演示，表明即使是 2.8T 参数的模型也可以在消费级硬件上运行，而无需服务器级 GPU。它展示了 SSD 流式传输作为一种可行的推理策略，可能让更多开发者和研究人员能够接触到前沿规模的开源权重模型。 Kimi K3 支持 100 万 token 的上下文窗口，并采用 Kimi Delta Attention（KDA）和 Attention Residuals（AttnRes），具备原生视觉能力。这种方法利用了 MoE 模型每个 token 只激活一小部分参数的特性，因此完整权重集无需同时驻留在内存中。

hackernews · Argonautlabs · 9月8日 20:07 · [社区讨论](https://news.ycombinator.com/item?id=49616257)

**核验**: 多源印证

**背景**: Kimi K3 是 Moonshot AI 于 2026 年 7 月发布的开源权重、原生多模态智能体模型，也是有史以来发布的最大开源权重模型。混合专家（MoE）模型包含许多专门的"专家"子网络，但每个 token 只激活其中一小部分，这使得权重可以从较慢的存储介质流式读取，而不必完全驻留于内存。Apple Silicon 的统一内存架构（M5 Max 为 128 GB）限制了可容纳在内存中的模型大小，因此从 NVMe SSD 流式传输专家权重，可以运行远超内存容量的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/Kimi-K3 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://sodevelopment.medium.com/run-massive-ai-models-on-tiny-hardware-with-ollm-ab8e3140acd7">Run Massive AI Models on Tiny Hardware with oLLM | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者的反应兼具幽默与务实：有人将这种方法比作《银河系漫游指南》中的"深思"计算机，并开玩笑说"一个中等长度的提示只需 11 天"；还有评论者指出 SSD 之所以必要，是因为 Apple 的架构不允许升级 RAM。尽管速度极慢，仍有评论者认为这是一个"好的开始"，因为目前没有其他方法可以在本地运行 2.8T 模型。还有用户询问 SSD 具体是如何连接的，这个细节在项目描述中并未完全解释清楚。

**标签**: `#AI inference`, `#local LLM`, `#SSD streaming`, `#large model`, `#developer tool`

---

<a id="item-3"></a>
## [Qwen3 27B 量化基准测试：4-bit 保持质量，1-bit 崩溃](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 8.0/10

一项对 Qwen3 27B 量化级别的新基准测试发现，4-bit 量化保持了模型质量，而 1-bit 量化导致性能严重下降。 这为在有限硬件上部署大型开源权重模型的开发者提供了实用指导，帮助他们在选择量化级别时兼顾内存占用和输出质量，避免过大的质量损失。 基准结果显示，4-bit 以内的量化质量几乎没有差异，2-bit 时分数略低，1-bit 则严重下降。社区评论还指出，质量拐点可能位于 2-bit 与 4-bit 之间，并建议针对低于 16GB 显存的 GPU 测试 Q3 级量化。

hackernews · stared · 9月8日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49611128)

**核验**: 多源印证

**背景**: 量化是一种将模型权重和激活值的数值精度降低的技术，例如从 32 位浮点转换为 8 位或 4 位整数，以降低内存占用和计算成本。它被广泛用于在边缘设备和消费级 GPU 上部署大型语言模型。然而，激进的量化会降低输出质量，因此像这样的实证基准测试有助于开发者理解其中的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/model-quantization-concepts-methods-and-why-it-matters/">Model Quantization: Concepts, Methods, and Why It Matters | NVIDIA Technical Blog</a></li>
<li><a href="https://www.ibm.com/think/topics/quantization">What is Quantization ? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区评论增加了技术深度：一位评论者批评了用 Wilson 置信区间表示运行间波动的方法，另一位分享了 Qwen3 的扩展思考可以抵消量化引起的采样差异的理论。还有人请求对 KV 缓存量化进行基准测试，并指出在低于 16GB 显存的 GPU 上缺少 Q3 级别的测试，另有一位用户质疑如何评估 AI 辅助撰写的文章的可信度。

**标签**: `#quantization`, `#Qwen3`, `#benchmark`, `#AI models`

---

<a id="item-4"></a>
## [i-have-adhd 技能阻止编码代理埋没答案](https://github.com/ayghri/i-have-adhd) ⭐️ 8.0/10

一个名为“i-have-adhd”的开源技能已在 GitHub 上发布，它向 Claude 等编码代理注入针对 ADHD 友好型的简洁指令，使代理把答案放在首位、给步骤编号，并避免在冗长输出中埋没关键结论。 这直接回应了 AI 编码代理的核心痛点——冗长、跑题的输出会埋没真正的答案。它提供了一个可执行的社区驱动解决方案，可以提升使用遵循 Agent Skills 开放标准的各类工具的开发者生产力。 该技能通过向代理提示注入“Action first”（行动优先）、“Steps numbered”（步骤编号）等简洁性指令来工作，并以 SKILL.md 文件形式安装，遵循 Claude Code 等工具采用的 Agent Skills 开放标准。社区反馈指出，其效果往往在几轮对话后就消退，需要反复强化。

hackernews · domhudson · 9月8日 14:13 · [社区讨论](https://news.ycombinator.com/item?id=49610631)

**核验**: 多源印证

**背景**: Agent Skills 是一种以标准化方式扩展 Claude Code 等编码代理的机制——即 SKILL.md 文件，其中包含代理在相关时可调用的指令、模板和上下文。研究表明，以缩短长度为目标的提示策略可将 LLM 响应能耗降低 25-60%同时保持质量，这凸显出冗长既是用户体验问题，也是可持续性问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ayghri/i-have-adhd">GitHub - ayghri/ i - have - adhd : A skill to stop your coding agent from...</a></li>
<li><a href="https://code.claude.com/docs/en/skills">Extend Claude with skills - Claude Code Docs</a></li>
<li><a href="https://arxiv.org/html/2506.08686v1">Brevity is the soul of sustainability: Characterizing LLM response lengths</a></li>

</ul>
</details>

**社区讨论**: 社区对该技能所针对的问题普遍持肯定态度，但多位用户反映 Claude 模型只能维持几轮简洁输出，之后就会恢复冗长行为，即使反复强化也是如此。有用户指出了模型叙述“自己没有做什么”这一顽固的“Claudism”习惯，还有用户对将安装指令复制粘贴进 CLI 提示符表示轻微的安全顾虑。

**标签**: `#AI agent`, `#Claude`, `#开发工具`, `#LLM行为优化`, `#开源`

---

<a id="item-5"></a>
## [基于网页的 LLM 注意力可视化工具获教育者好评](https://ishamf.dev/p/llm-attention-visualizer/) ⭐️ 8.0/10

一位开发者在 ishamf.dev 发布了基于网页的 LLM 注意力可视化工具，使注意力机制变得直观且可交互。该工具被教育者和学习者誉为目前最清晰的注意力解释。 该工具解决了 AI 教育中一个众所周知的难点：注意力机制因其加权方案在概念上难以理解。通过提供直观的可视化，它帮助教师、学生和开发者理解 LLM 如何处理上下文，可能加速 AI 技术的学习和采用。 该可视化工具是一个单一网页，演示注意力层如何组合来自多个短语的信息，使跨短语交互变得可见。它引发了实质性的技术讨论，包括一个问题：后层注意力是否会因为累积求和而被前层注意力淹没。

hackernews · ifz · 9月8日 16:59 · [社区讨论](https://news.ycombinator.com/item?id=49613068)

**核验**: 多源印证

**背景**: 注意力机制是一种机器学习技术，指导深度学习模型优先处理输入数据中最相关的部分。自注意力、多头注意力等变体是当今 LLM 的核心，通过使模型能够捕获长文本跨度中复杂的词关系，推动翻译、摘要和问答等任务的发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/attention-mechanism-in-llms-intuition">Attention Mechanism in LLMs: An Intuitive Explanation</a></li>
<li><a href="https://www.ai21.com/knowledge/attention-mechanisms-language-models/">What are Attention Mechanisms in Language Models? | AI21</a></li>
<li><a href="https://www.ibm.com/think/topics/attention-mechanism">What is an attention mechanism? | IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞该可视化的清晰度，一位教育者表示他们周五就要教这个内容，觉得时机正好；一位学习者称这是他们见过的最清晰的示例。一位技术评论者提出了一个问题：在求和过程中，较早层是否会掩盖较后层的注意力；其他人则表达了热情，如评论"INSANE"。

**标签**: `#LLM`, `#attention`, `#visualization`, `#AI education`, `#developer tools`

---

<a id="item-6"></a>
## [研究：预训练进步主要来自数据改进](https://www.dwarkesh.com/p/pretraining-progress-is-mostly-data) ⭐️ 7.5/10

Dwarkesh Patel 在最高 1e19 FLOPs 算力预算下训练了 2019 至 2025 年各年度代表性模型配方与数据语料，发现数据改进带来 12.0 倍的算力效率提升，而模型改进仅带来 3.7 倍。数据贡献约为模型的 3.24 倍。 这项量化证据表明，数据规模与质量（而非架构变化）是预训练进步的主要驱动力。这可能引导人工智能实验室调整研发资源分配，将数据整理视为提升算力效率的关键抓手。 实验在统一的最高 1e19 FLOPs 算力预算下，逐年对比了 2019 至 2025 年的代表性模型配方与数据语料。数据改进带来的 12.0 倍提升约为模型改进 3.7 倍的 3.24 倍。

aihot · Dwarkesh Patel：Podcast & Blog（RSS） · 9月8日 16:10 · [中文阅读](https://aihot.news/items/cmtsx0wm4041jrob5liwjypsq)

**核验**: 待核验

**背景**: 预训练是指在大规模数据集上对大型模型进行初始训练，以学习通用表征。算力效率衡量每单位计算成本所带来的性能提升；数值越高意味着每单位 FLOP 的进步越大。该研究通过保持算力不变、逐年变动数据与模型配方，从而分离出数据改进的贡献。

**标签**: `#预训练`, `#数据`, `#AI研究`, `#行业分析`, `#算力效率`

---

<a id="item-7"></a>
## [OpenAI 发布 ChatGPT Images 2.5 及双 API 模型](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 7.3/10

OpenAI 发布了 ChatGPT Images 2.5，改进了指令遵循能力、响应速度更快，并且在参考照片中能更好地保留主体。API 端新增两个模型 ID：gpt-image-2.5-sunburst 和 gpt-image-2.5-flare。 此次升级直接影响每周通过 ChatGPT 生成超过 30 亿张图像的庞大用户群体，并为开发者提供了精度（Sunburst）和速度（Flare）之间的明确选择。这标志着 OpenAI 持续推动图像编辑更加交互化，Sketch 和模板功能降低了非技术用户的使用门槛。 Sunburst 专注于编辑精度要求最高的流程，而 Flare 针对快速、高质量的日常生成进行了优化。此次发布还引入了 Sketch（在 ChatGPT 中绘制草图以生成完整图像）、海报和商品图等模板预设，以及可在图像上直接标注修改位置的图片评论编辑功能。

rss · Simon Willison · 9月8日 22:46 · 2 个来源

**核验**: 多源印证

**背景**: OpenAI 的图像生成模型已在 ChatGPT 和 GPT-Image API 模型中被用于生成超过 30 亿张图像。新 API 模型采用相同的 token 定价（输入每百万 8 美元，输出每百万 30 美元），开发者应根据工作流对精度与速度的权衡进行选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-5/">Introducing ChatGPT Images 2 . 5 | OpenAI</a></li>
<li><a href="https://www.orcarouter.ai/blog/gpt-image-2-5-flare-sunburst">GPT - Image - 2 . 5 Flare vs Sunburst : New OpenAI Image APIs</a></li>
<li><a href="https://www.youtube.com/watch?v=eCl-W2Asq1g">ChatGPT Images 2 . 5 — Tested With Real Generations ( Reference ...)</a></li>

</ul>
</details>

**社区讨论**: 早期视频评测者测试了官方宣称的四大要点——参考图像保真度、精确编辑、多轮一致性和速度——并指出每一方面都有明显改进。一些开发者强调了新 CLI 工具集成的实用价值，讨论总体呼应了官方建议：精度选 Sunburst，速度选 Flare。

**标签**: `#OpenAI`, `#图像生成`, `#AI模型`, `#产品发布`

---

<a id="item-8"></a>
## [字节跳动秘密研发实时空间视频模型，预计 10 月发布](https://x.com/FeitengLi/status/2097338830584234321) ⭐️ 7.0/10

据彭博社消息，字节跳动在创始人张一鸣亲自牵头下，正在秘密研发基于 Seedance 的实时空间视频模型，最早有望于今年 10 月亮相。核心突破在于“实时交互”——能根据用户的语音与动作实时生成可互动的 3D 虚拟世界，并与 Pico 头显深度绑定，通过云端推流实现 20fps 渲染帧率和约 0.05 秒的端到端延迟。 这标志着 AI 视频生成与空间计算的重要融合，可能在消费级 VR 设备上实现低成本、可交互的 3D 体验，从而重塑 VR/AR 生态，并加剧科技巨头在世界模型和实时渲染领域的竞争。 该模型基于字节跳动的 Seedance 底座构建，采用云端推流架构将核心计算放在云端，大幅降低头显端的本地算力门槛与硬件成本。不过，该消息来源于彭博社的媒体报道，尚未得到字节跳动官方确认。

twitter · Feiteng · 9月8日 14:58

**核验**: 多源印证

**背景**: Seedance 是字节跳动的多模态 AI 视频生成模型，支持文本和图片生成视频，原生具备多镜头叙事能力，可输出 1080p 高清视频。世界模型（如 Google DeepMind 的 Genie 3）能从文本提示实时生成可交互的 3D 环境，是沉浸式空间计算的关键组成部分。云端渲染将繁重的图形处理从本地设备转移到数据中心，使轻量级 VR 头显能以低延迟运行复杂场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/zh/seedance">Seedance</a></li>
<li><a href="https://pixverse.blog/zh/blog/what-is-google-deepmind-genie-3/">什 么 是 Google DeepMind Genie 3 ？ 世 界 模 型 的新前沿</a></li>
<li><a href="https://blog.dolit.cn/from-one-device-one-pc-to-cloud-sharing-real-time-cloud-rendering-reshapes-virtual-simulation-training-in-higher-education">blog.dolit.cn/from-one-device-one-pc-to-cloud-sharing-real-time-cloud...</a></li>

</ul>
</details>

**社区讨论**: 该帖内容包含作者对 Google 在 AI 发展中所扮演角色的评论，指出 Google 经常率先探索技术（如 Transformer、LaMDA、Veo3 和 Genie 3），而其他公司随后成功商业化。这反映出一种观点，即 Google 扮演着行业开路先锋的角色，但该讨论本身缺乏直接用户评论，很大程度上属于主观推测。

**标签**: `#AI视频生成`, `#字节跳动`, `#空间计算`, `#实时交互`, `#行业动态`

---

<a id="item-9"></a>
## [安全警报：Scoppr 和 Nook 是恶意的 Mole 仿冒版本](https://x.com/HiTw93/status/2097330901676126446) ⭐️ 7.0/10

开发者 @HiTw93 发出警告，称 Scoppr 和 Nook 是 Mole 的未授权仿冒版本，两者均与能窃取密码和个人数据的恶意软件有关。用户被强烈建议仅从官方网站下载 Mole。 这一警告保护了开发者和 Mac 用户，使其免受针对热门系统工具的真实恶意软件威胁。同时它也揭示了一种常见的攻击模式：网络犯罪分子克隆可信工具来传播窃取密码的恶意软件。 Scoppr 和 Nook 均与 Mole 的开发者没有任何关联。Mole 唯一的官方网站是 mole.fit，用户应仅从该网站下载此软件。

twitter · Tw93 · 9月8日 14:27

**核验**: 多源印证

**背景**: Mole 是一款原生 Mac 应用，用于清理缓存、卸载和更新应用、分析磁盘空间以及检查系统状态。克隆热门软件来分发恶意软件是网络犯罪分子常用的手段，其目的是诱骗用户安装能够窃取凭据和敏感数据的恶意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mole.fit/">Mole · Native Mac Cleaner, App Manager, and System Monitor</a></li>

</ul>
</details>

**标签**: `#security`, `#malware`, `#AI tools`, `#developer safety`

---

<a id="item-10"></a>
## [GPT-6 Astra 不依赖编译器直接生成二进制可执行文件](https://x.com/tombkeeper/status/2097259068419391596) ⭐️ 7.0/10

开发者 @tombkeeper 用 GPT-6 Astra 做了一项实验，成功生成了 MessageBox 弹框、系统进程列举、通过发送消息输入文字以及计算器等多个 Windows 二进制可执行程序。据报道，该模型能够直接从自然语言提示输出可运行的二进制文件。 这标志着 AI 编程工具的能力边界又向前推进了一步：无需传统编译器流程即可生成可直接运行的二进制文件。如果这一能力得到确认，可能会简化开发者的部署流程，并扩展 AI 助手在软件交付中的应用方式。 生成的程序是 Windows 可执行文件，从 MessageBox、SendMessage 和进程列举 API 可以推断这一点，四个测试据说全部成功。帖子并未说明二进制输出是如何生成或验证的技术细节。

twitter · Yang Yu · 9月8日 09:41

**核验**: 多源印证

**背景**: GPT-6 Astra 是一款先进的 AI 模型，据报道在推理和编程方面表现强劲。传统上，AI 编程助手会生成源代码，开发者需要用 GCC 或 MSVC 等工具链编译后才能运行。这个实验表明模型可以绕过这一步骤，直接输出机器可执行的二进制文件，但背后的机制尚不清楚。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/L65R3EQU0511AQHO.html?clickfrom=w_dy">GPT - 6 Astra 杀疯了：只要你学得够慢，就可以不用学了？</a></li>
<li><a href="https://m.leiphone.com/category/yanxishe/FQUliuw9lt15UH54.html">打穿 AI 智商测试！ GPT - 6 Astra ...</a></li>

</ul>
</details>

**标签**: `#AI coding`, `#GPT-6`, `#binary generation`, `#AI capabilities`, `#developer tools`

---

<a id="item-11"></a>
## [DeepSeek V4.1 Flash 发布，增强原生多模态能力](https://x.com/op7418/status/2097232704509006270) ⭐️ 7.0/10

DeepSeek 发布了 V4.1 Flash 模型，原生多模态能力有所增强。用户只需改用公告图片中显示的模型名称即可调用。 这次发布是 DeepSeek 模型系列的重要更新，尤其在多模态处理方面，为开发者提供了更强大且性价比更高的选择。不过，作者表示自己更关注智谱的 GL5.3Flash，这反映出中国 AI 模型市场竞争的激烈。 据公告，DeepSeek V4.1 Flash 是测试版本，其定价会根据一天中的时段而变化。相关 DeepSeek 文档显示，它保持较快的响应速度和成本效益，同时推理能力接近 V4-Pro 模型。

twitter · 歸藏(guizang.ai) · 9月8日 07:56

**核验**: 多源印证

**背景**: DeepSeek 是一家中国 AI 研究公司，主要开发大语言模型。'Flash' 版本通常是比完整模型更轻量、更快、更便宜的替代品，专为高效任务设计，能力略有降低。多模态能力指模型能够理解和处理多种类型的数据（如文本和图像）。智谱 AI 的 GLM 系列是中国市场上的主要竞品模型家族。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://commandcode.ai/models/deepseek-v4-1-flash-beta">DeepSeek V 4 . 1 Flash (beta) — pricing, benchmarks... - Command Code</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.3-Flash">zai-org/GLM- 5 . 3 - Flash · Hugging Face</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#模型发布`, `#多模态`, `#AI工具`

---

<a id="item-12"></a>
## [Codex 新增 AI 聊天记录整理与自定义分组功能](https://x.com/op7418/status/2097174249333219551) ⭐️ 7.0/10

Codex 现在支持查看所有内容并整理左侧聊天历史，用户可按照项目划分、归档不用的对话，还能根据自己定义的逻辑重新分组。例如，原来只有一个项目，现在它可以帮你分成“持续迭代”、“待跟进”和“最近”等类别，原来的项目列表则被清空。 这一功能通过自动化聊天管理，减少了手动整理的工作量，提升了 AI 开发工具使用者的效率。它也反映了开发环境中 AI 辅助生产力功能的发展趋势，即用自然语言指令控制界面整理。 该功能似乎是用户引导式的：用户说明分组逻辑（例如按项目或自定义类别），Codex 就会相应地重新整理聊天列表。用户还可以在分组标签前加上 emoji，使展示更清晰，而且重新排序后原来的项目分组可能会被清空。

twitter · 歸藏(guizang.ai) · 9月8日 04:04

**核验**: 待核验

**背景**: Codex 是 OpenAI 开发的 AI 编程助手/代理，能够执行任务、管理代码项目并与开发环境交互。随着 AI 工具积累大量聊天历史，整理这些对话成为常见的痛点。该功能利用自然语言指令管理界面，体现了开发工具和流程自动化迈向对话式控制的更广泛趋势。

**标签**: `#AI开发工具`, `#Codex`, `#产品功能`, `#工作流优化`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="8"><span>其他追踪推文</span><span class="archive-tab-count">8</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="12"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">12</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2097436643963842954">@dotey: OpenAI 发布了 ChatGPT Images 2.5，对其图像生成能力做了一次全面升级。核心改进有三个方向：速度更快（延迟比上一代降低约 50%），画面更逼真（光影和纹理更自然，人...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月8日 21:27 UTC · 喜欢 127 · 转发 18 · 回复 7 · 浏览 23247</p>
<p class="archive-item-content">OpenAI 发布了 ChatGPT Images 2.5，对其图像生成能力做了一次全面升级。核心改进有三个方向：速度更快（延迟比上一代降低约 50%），画面更逼真（光影和纹理更自然，人物面部特征保持得更好），以及编辑更精准（能只改你指定的部分，其余细节不动）。<br>
<br>
目前 ChatGPT 每周的图像生成量已经超过 30 亿张，这次升级直接影响的就是这个庞大的用户群体。<br>
<br>
除了模型本身的提升，OpenAI 还上线了几个实用功能。一个叫 Sketch，可以直接在 ChatGPT 里画草图，比如你画个大致的布局或轮廓，ChatGPT 会把它变成完整的图像。有时候画比说更快，这个功能就解决了&quot;想法在脑子里但描述不出来&quot;的问题。在对话框输入 @Sketch 就能用。<br>
<br>
另一个是模板功能，提供了海报、商品图等常见格式的模板，不用每次都从零开始描述。还有一个图片评论编辑功能，可以直接在图上标注你想修改的地方，比反复用文字描述&quot;把左上角那个东西改一下&quot;要直观得多。<br>
<br>
对开发者来说，API 端同步推出了两个新模型。GPT-Image-2.5 Flare 和 ChatGPT 里的体验一致，速度快、质量好，适合大多数场景。GPT-Image-2.5 Sunburst 则是面向高端创意工作的，生成时间更长但精度更高，适合做需要精细控制的品牌素材或产品图。<br>
<br>
ChatGPT Images 2.5 今天起向所有 ChatGPT、ChatGPT Work 和 Codex 用户开放，覆盖桌面端、移动端和网页端。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2097383059679060353">@dotey: OpenAI 正式宣布：其内部模型解决了 Navier-Stokes 千禧年难题。论文和 Lean 形式化证明已公开。 这是 Buckmaster 声明 https://t.co/Bwk...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月8日 17:54 UTC · 喜欢 88 · 转发 12 · 回复 19 · 浏览 27492</p>
<p class="archive-item-content">OpenAI 正式宣布：其内部模型解决了 Navier-Stokes 千禧年难题。论文和 Lean 形式化证明已公开。<br>
<br>
这是 Buckmaster 声明 https://t.co/BwkY0K4CLg 发出后数小时内的回应，但 OpenAI 的说法远不止辩解，他们声称拿到了更强的成果。<br>
<br>
【OpenAI 称证明了什么】<br>
<br>
OpenAI 称，其尚未发布的内部模型（比 GPT-6 Astra 强得多）生成了一个解析证明：三维不可压缩流体在光滑外力作用下，可以在有限时间内从光滑初始状态发展出奇点（即速度趋向无穷大），同时能量保持有限。这对应 Clay 千禧年问题中 Fefferman 表述的 C 和 D 项。<br>
<br>
此外，OpenAI 还声称顺带解决了无外力 Euler 方程的正则性问题。注意“无外力”三个字，Buckmaster 和 Alpöge 证明的是带光滑外力的 Euler 爆破，而 OpenAI 声称做到了不加外力。如果成立，这是一个严格更强的结果。<br>
<br>
两项成果均配有 Lean 形式化验证，代码已发布在 GitHub 上。<br>
<br>
【怎么做到的：上万个 Agent 军团】<br>
<br>
OpenAI 描述的方法相当有冲击力。他们使用了一套由内部模型驱动的多 Agent 协作系统。Agent 被分成若干组，组内可以通信，每组尝试不同的进攻方向。处理 Navier-Stokes 的那组涉及约一万个并发 Agent。<br>
<br>
整个过程中，Agent 发送了 270 万条消息，消耗约 1300 亿输出 token。Navier-Stokes 的解在首批 Agent 启动约 88 小时后到达。随后 GPT-6 Astra 用 17 小时完成 Lean 形式化。<br>
<br>
无外力 Euler 方程的解是意外收获——约 100 个 Agent 工作了大约 50 小时，把它当作较容易的&quot;热身题&quot;时解决的。<br>
<br>
OpenAI 表示，他们在过程中让不同组交叉借鉴彼此的中间成果，并用 Codex 汇总各组最有用的洞见。找到 Navier-Stokes 解的那个组就是在这种引导下工作的。<br>
<br>
【两边叙事的关键分歧】<br>
<br>
OpenAI 的时间线与 Buckmaster 声明的时间线有重叠但有微妙差异。<br>
<br>
关于动机：OpenAI 说他们是 9 月 1 日听到“有两个千禧年问题被解决了”的传言后启动评估，传言并非专门针对 Buckmaster 的工作。而 Buckmaster 的声明描述的是：他的工作信息传到 OpenAI 后，OpenAI 才开始在同一条极冷门的技术路线上发力。<br>
<br>
关于交涉：OpenAI 说他们 9 月 6 日完成全部证明和 Lean 验证后，“相信对方也有 Navier-Stokes 的解”，于是主动联系，提出联合发布并承认对方的优先权。但通话后发现 Buckmaster 和 Alpöge 的成果是带外力的 Euler，而非 Navier-Stokes。而 Buckmaster 描述的通话场景是 OpenAI 在信息不对等的情况下施压、要求移除合作者。<br>
<br>
关于数据：OpenAI 在博客和推文中都明确否认访问过用户数据，但加了一句值得注意的话：“虽然可能性不大，但我们无法排除基于他们产品使用而生成的去标识化数据帮助改进了我们的模型”。Buckmaster 在声明中问过这个问题，没得到回答。<br>
<br>
关于学术功劳：OpenAI 推文祝贺 Buckmaster 和 Alpöge 取得了&quot;remarkable mathematical work&quot;，并承认对方在 Euler 问题上的优先权。但声明中没有任何文字提及 Córdoba 和 Martínez-Zoroa 的开创性工作——要知道整个受迫爆破研究计划是他们建立的。<br>
<br>
【Bubeck 回应：指控不实】<br>
<br>
Bubeck 在 X 上发帖，称关于他的指控“虚假且具煽动性”（false and inflammatory），表示自己是按照学术规范参与讨论的，对事态发展表示失望，并承诺次日将给出更详细回应。<br>
<br>
截至目前，Bubeck 尚未对 Buckmaster 声明中的任何具体细节——Codex 数据问题、署名施压、“毁掉你的职业生涯”的说法——作出逐条回应。<br>
<br>
【数学界在等什么】<br>
<br>
Scientific American 的报道标题：“OpenAI 声称数学重大突破，争议缠身。”<br>
<br>
多位数学家指出，虽然 OpenAI 已发布 Lean 代码，但社区尚未完成独立验证。Lean 形式化本身具有极高的可信度，如果代码能通过编译，证明在逻辑上就是正确的，但这仍然需要外部数学家实际运行和检查。<br>
<br>
陶哲轩此前评价 Buckmaster/Alpöge 的工作时说，这些方法“没有原理上的障碍”推进到 Navier-Stokes，但他同时也说，他“不会对有人靠堆大量算力和 AI 来暴力推进这一步感到意外”，只是这种做法并不特别吸引我。在 OpenAI 宣布上万个 Agent 88 小时拿下成果后，回过头来读陶哲轩的话别有深意。<br>
<br>
Clay 数学研究所的规则也值得提醒：即使证明成立，还必须在公认的数学期刊正式发表，并在至少两年的社区审查后才有可能获得千禧年奖。OpenAI 在博客中也表示不打算领取该奖金。<br>
<br>
OpenAI 博客：https://t.co/kzle78SIyl</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/OpenAI/status/2097374640582668336">@OpenAI: We’re sharing a solution to the Navier-Stokes Millennium Prize Problem, one of the deepest pr...</a></h3>
<span class="score-badge" data-tier="high" aria-label="10.0 out of 10">10.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月8日 17:20 UTC · 喜欢 79465 · 转发 13376 · 回复 3641 · 浏览 28455961</p>
<p class="archive-item-content">We’re sharing a solution to the Navier-Stokes Millennium Prize Problem, one of the deepest problems at the frontier of mathematics.<br>
<br>
The proof was produced by a group of agents, using an OpenAI next-generation model significantly more capable than GPT-6 Astra.<br>
<br>
The problem concerns whether the description of smooth three-dimensional fluid motion modeled by the Navier-Stokes equations can break down. It has remained unresolved for roughly 90 years.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2097246086981464088">@op7418: B 站 1 万粉了，真不容易。 https://t.co/djn9l7YCma</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 9月8日 08:50 UTC · 喜欢 91 · 转发 0 · 回复 65 · 浏览 9477</p>
<p class="archive-item-content">B 站 1 万粉了，真不容易。 https://t.co/djn9l7YCma</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2097223647068836166">@dotey: 纽约大学数学家 Tristan Buckmaster 今天发表公开声明，披露了两件事：一是他和合作者借助大语言模型在一个月内攻破了流体力学领域多个重要难题，二是他指控 OpenAI 在得...</a></h3>
<span class="score-badge" data-tier="high" aria-label="9.0 out of 10">9.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月8日 07:20 UTC · 喜欢 647 · 转发 105 · 回复 107 · 浏览 252268</p>
<p class="archive-item-content">纽约大学数学家 Tristan Buckmaster 今天发表公开声明，披露了两件事：一是他和合作者借助大语言模型在一个月内攻破了流体力学领域多个重要难题，二是他指控 OpenAI 在得知他的进展后试图抢先发布成果，并要求将他的合作者从署名中移除，理由是对方在 Anthropic 工作。<br>
<br>
这份声明目前正在数学界和 AI 圈快速传播，涉及学术伦理、AI 能力边界和公司竞争等多个层面。以下是这件事的来龙去脉。<br>
<br>
【数学成果：证明了什么】<br>
<br>
Buckmaster 与合作者 Levent Alpöge 公开了三项证明：不可压缩多孔介质方程、Boussinesq 方程以及三维不可压缩 Euler 方程的有限时间爆破（blowup），均使用了光滑外力（smooth forcing）。他们还认为自己得到了 Navier-Stokes 方程的爆破结果，但该部分的 Lean 形式化验证尚未完成，论文暂不公开。<br>
<br>
翻译成大白话：这些方程描述的是水、空气等流体如何运动。数学家想知道的是，在光滑的初始条件下，流体的速度会不会在有限时间内变成无穷大，也就是&quot;爆破&quot;。这个问题的终极版本就是 Navier-Stokes 存在性与光滑性问题，Clay 数学研究所在 2000 年把它列为七大千禧年难题之一，悬赏一百万美元。<br>
<br>
需要说清楚的是，Buckmaster 和 Alpöge 并没有直接解决那个百万美元的问题。他们证明的是一个相关但限制更多的版本：在加入光滑外力的条件下，方程的解可以爆破。这对应 Clay 问题中 Fefferman 表述的 c 和 d 选项。但这条路径是通向无外力 Euler 方程的重要一步，而无外力版本才是最终目标。<br>
<br>
这项工作并非凭空而来。基础思路来自西班牙数学家 Diego Córdoba 和 Luis Martínez-Zoroa，他们多年来一直在研究带外力的爆破构造，已经在&quot;粗糙外力&quot;条件下取得了成果。Buckmaster 和 Alpöge 所做的是在此基础上推进到光滑外力和 Euler 方程。Buckmaster 在声明中直言：鉴于这一系列工作，他认为 Martínez-Zoroa 配得上 Fields 奖。<br>
<br>
关键结果在 8 月 15 日获得，8 月 22 日通过 Lean（一种形式化证明验证系统）的机器检查。Lean 验证意味着证明没有逻辑漏洞，这不是&quot;信我就行&quot;，而是有机器背书。<br>
<br>
陶哲轩在成果公开后不久就在 Mastodon 上发表评价，称这是&quot;a remarkable achievement&quot;（了不起的成就）。他确认了 Lean 形式化验证的存在，也指出论文确实包含大量 AI 生成的内容，但作者过去几周一直在努力将其改写为可接受的形式。他提到一个关键细节：作者被迫提前发布，原因是&quot;外部事件&quot;，也就是声明中记录的与 OpenAI 的冲突。<br>
<br>
在技术层面，陶哲轩对这条研究路径给出了乐观判断：他认为没有什么原理上的障碍阻止这些方法一路推进到 Navier-Stokes，甚至有&quot;不可忽视的可能性&quot;完全消除外力项。如果后者成立，那就是 Clay 千禧年问题的完整解答。但陶哲轩随即加了一句耐人寻味的话：他不会对有人靠堆算力和 AI 来暴力推进这一步感到意外，但这种做法&quot;并不特别吸引我&quot;——他更感兴趣的是消化证明方法，提取其中的新数学洞见。<br>
<br>
这基本上可以理解为：数学界最具权威的声音认可了成果的实质性，同时含蓄地为&quot;人类+AI 合作&quot;中什么才真正有价值画了一条线。<br>
<br>
【AI 扮演了什么角色】<br>
<br>
Buckmaster 和 Alpöge 在整个过程中大量使用了大语言模型，包括 Anthropic 的 Claude、OpenAI 的 Codex 以及 GPT-5.6 Sol，最近还用了 Astra（后者仅用于论文写作和论证审计）。<br>
<br>
过去一年进展缓慢，两人一直在消化文献、逐步升级前置结果。真正的突破发生在大约一个月前。Buckmaster 坦言，Alpöge 发给他的第一个 LLM 生成的证明是他&quot;读过的最恐怖的东西&quot;。他们花了两周多时间去理解这个证明，并试图将其改写成人类可读的形式。他承认 Euler 方程的论文写作质量很差，甚至用了&quot;AI slop&quot;（AI 生成的垃圾内容）来形容。<br>
<br>
Buckmaster 把这一刻比作国际象棋领域的&quot;深蓝对卡斯帕罗夫&quot;时刻：一个数学家配合 LLM，一个月内完成了原本可能需要数年的工作。他认为这对数学界如何培养学生、分配学术功劳、审稿以及决定什么值得一个人投入毕生精力，都有深远影响。<br>
<br>
【与 OpenAI 的冲突】<br>
<br>
事情从 9 月 3 日开始变味。当时网上已经有传言称&quot;Anthropic 解决了一个重大数学难题&quot;，Alpöge 也收到线报说他们的进展信息已传到 OpenAI 内部。Buckmaster 主动写信给 OpenAI 的一位知名数学家，说明情况并强调这是个人合作，与任何机构无关。<br>
<br>
对方当天回复，表示如果 Buckmaster 愿意透露细节会很有帮助，并提出可以提供算力支持。Buckmaster 提议下周通话，但 OpenAI 方面连续催促提前见面。9 月 6 日（周日），OpenAI 的 Sébastien Bubeck 加入，三人当天下午通了两次电话。<br>
<br>
通话中，Buckmaster 被告知 OpenAI 的一个内部模型已经生成了一份大约 100 页的受迫 Navier-Stokes 方程有限时间爆破证明。Buckmaster 注意到，OpenAI 的技术路线与他和 Alpöge 秘密采用的路线高度重合，而这条路线几乎没有其他人在走。<br>
<br>
声明中描述的通话过程暴露了几个问题。OpenAI 最初声称&quot;极少人工参与&quot;，但随着对话推进（Bubeck 不断收到同事在内部聊天中发来的修正和补充），事实逐渐浮出水面：这是一整个团队在操作，投入了大量算力，先从较容易的问题（包括 Euler）入手，甚至展示给 Buckmaster 的提示词本身也是用 Codex 生成的。<br>
<br>
Buckmaster 追问 OpenAI 是何时开始处理这个问题的。这个问题没有被直接回答，但最终双方确认：第一个提示词是在过去几天内发出的，也就是在 Buckmaster 的工作信息传到 OpenAI 之后。<br>
<br>
Buckmaster 还问了一个关键问题：OpenAI 的模型是否被训练过他们在 Codex 中的会话数据——他和 Alpöge 整个项目期间一直把草稿放在 Codex 里。他被告知模型不会查看用户数据。他再次追问是否用于训练，没有得到回答。<br>
<br>
随后 OpenAI 提出了两个方案：一是 Buckmaster 先发 Euler 结果，OpenAI 第二天发 Navier-Stokes 结果；二是 Buckmaster 独自撰写一篇论文发布 Navier-Stokes 成果，注明系 OpenAI 内部模型所得。Bubeck 两次明确要求将 Alpöge 从署名中移除，说如果不是因为 Alpöge 在 Anthropic 工作，一切会简单得多，还说他在 Anthropic 工作&quot;太烦人了&quot;。OpenAI 还表示，如果他们在 Buckmaster 之后发表，会公开说 Buckmaster 和 Alpöge 配得上 Clay 奖金，称他们是&quot;最接近这个问题的人类&quot;。<br>
<br>
Buckmaster 拒绝了两个方案，并表示如果 OpenAI 按计划发布，他会公开所有经过。对方回应：&quot;你为什么要毁掉自己的职业生涯？&quot; Buckmaster 说自己是学术界的人，反问为什么公开会毁掉职业。回答是：&quot;如果你不希望我友善，那我也可以不友善。&quot;<br>
<br>
之后 Bubeck 给 Alpöge 发短信，提议两人单独谈，并说&quot;我不确定 Tristan 现在是否完全理性&quot;。Alpöge 拒绝并表示应与 Buckmaster 沟通。<br>
<br>
【Buckmaster 自己的界定】<br>
<br>
Buckmaster 在声明末尾明确划了线：他没有看过 OpenAI 的证明，不知道 OpenAI 的模型做了什么或怎么做的，不知道他们的数据是否被使用，也没有指控任何人任何事。他说自己只是在陈述被告知了什么、何时被告知、以及被提议了什么。他这样做是因为&quot;另一种选择是让一连串公告讲述他知道并非事实的故事&quot;。<br>
<br>
他说，如果 OpenAI 的模型确实弥合了通向 Navier-Stokes 的差距，那是一件了不起的事，应该被大声说出来，但要带上完整的历史。<br>
<br>
PDF 地址：https://t.co/jS6A5ZZarS</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2097185692564554109">@dotey: Q1：在和 AI 协作的过程中，有没有一个具体的习惯或方法，对个人成长帮助最大？ 我的经验就一条：先用起来。 只有实践才有真实感悟，我今天讲的开发过程，你不自己做一遍，能带走的东西很有限...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月8日 04:50 UTC · 喜欢 178 · 转发 27 · 回复 69 · 浏览 26924</p>
<p class="archive-item-content">Q1：在和 AI 协作的过程中，有没有一个具体的习惯或方法，对个人成长帮助最大？<br>
<br>
我的经验就一条：先用起来。<br>
<br>
只有实践才有真实感悟，我今天讲的开发过程，你不自己做一遍，能带走的东西很有限。AI 把反馈周期缩到很短：照着这个流程，哪怕不写代码，做一个小工具或 Skill，几小时就有反馈。<br>
<br>
最根本的是建立反馈循环：定义想做的事，AI 帮你做成，你验收；分享出去收反馈；把经验写出来，AI 帮你整素材，输出又倒逼你系统思考。小循环做项目，大循环做分享。循环建起来、越转越快，成长就越来越快。可以理解为把人的成长做成一套 Loop Engineering。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/PandaTalk8/status/2097180109237330332">@PandaTalk8: 年轻的朋友，尽早学会构建自己的反馈回路。 因为真正让人成长的，不是“做了多少事”，而是能否持续知道：我做的事情，究竟有没有产生预期效果。 其实你很努力，也很用心，也坚持学习，但是总是没达...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月8日 04:27 UTC · 喜欢 61 · 转发 4 · 回复 22 · 浏览 36612</p>
<p class="archive-item-content">年轻的朋友，尽早学会构建自己的反馈回路。 <br>
因为真正让人成长的，不是“做了多少事”，而是能否持续知道：我做的事情，究竟有没有产生预期效果。<br>
<br>
其实你很努力，也很用心，也坚持学习，但是总是没达到自己预期的成就。  根本原因就在于没有形成自己的「反馈回路」<br>
---<br>
坐在咖啡不免为自己碌碌无为的前半生感到沮丧。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2097143628842045542">@op7418: 重置来了，朋友们，感觉这几天可以放心蹬</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 9月8日 02:02 UTC · 喜欢 11 · 转发 0 · 回复 40 · 浏览 17831</p>
<p class="archive-item-content">重置来了，朋友们，感觉这几天可以放心蹬</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/amasad/status/2097197172299006423">Amjad Masad: Honored to have the Mayor of London, Sadiq Khan, help us open Replit’s first international of...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Replit 在伦敦开设首个国际办公室，与市长合作推广 AI 技能</p>
<p class="source-line">Follow Builders · X 动态 · Amjad Masad · 9月8日 05:35 UTC · 喜欢 120 · 转发 4 · 回复 19</p>
<p class="archive-item-content">Replit 在伦敦开设首个国际办公室，并与市长合作推动 AI 技能培训。</p>
<p class="archive-item-translation"><span>中文摘要</span>Replit 宣布在伦敦设立首个国际办公室，并与伦敦市长合作，为来自弱势社区的年轻人提供编程和 AI 技能培训。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2097193293532848288">Thibault Sottiaux: Looking at this 28 page deck right now where Codex is keeping track of all the individual lau...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>关于 Codex 跟踪多个发布的宣传性推文</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 9月8日 05:20 UTC · 喜欢 1882 · 转发 53 · 回复 341</p>
<p class="archive-item-content">一条关于 Codex 新发布的宣传性推文，提及团队和 deck，但未提供具体技术信息。</p>
<p class="archive-item-translation"><span>中文摘要</span>这是一条关于 Codex 新发布的宣传性推文，提到团队和 28 页 deck，但缺乏技术细节，内容较为浅显。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/levie/status/2097189559712837770">Aaron Levie: Good reminder here that with rapidly accelerating AI progress, you should likely be building...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Aaron Levie：快速加速的 AI 进步应促使你以指数级愿景构建产品</p>
<p class="source-line">Follow Builders · X 动态 · Aaron Levie · 9月8日 05:05 UTC · 喜欢 101 · 转发 9 · 回复 19</p>
<p class="archive-item-content">提醒开发者应以看待 AI 能力提升数个数量级的愿景来构建产品，专注于那些当前勉强可行但未来可能实现的机会。</p>
<p class="archive-item-translation"><span>中文摘要</span>鉴于 AI 能力的快速进步，构建产品时应设想至少数个数量级的提升或可用 token 量，最佳机会是今日勉强可行但目标远超当前技术限制的领域。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2097174560412246215">Thibault Sottiaux: All reset for everyone. Enjoy the week with Astra. https://t.co/WBM38JotGO</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：为所有人重置。享受与 Astra 的一周。</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 9月8日 04:05 UTC · 喜欢 8803 · 转发 299 · 回复 1273</p>
<p class="archive-item-content">一条关于 Astra 的简短推文，缺乏技术内容，仅为营销性质。</p>
<p class="archive-item-translation"><span>中文摘要</span>这是一条关于 Astra 的营销推文，内容简短，缺乏技术深度。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2097150265044721958">Garry Tan: They shout “billionaires” when actually their cronies straight up loot the public coffers htt...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>加里·谭：他们喊“亿万富翁”，实际上是他们的亲信公然窃取公共资金</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 9月8日 02:29 UTC · 喜欢 126 · 转发 1 · 回复 11</p>
<p class="archive-item-content">Political commentary on billionaires and public corruption, no technical relevance.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条关于政治腐败的推文，与用户关注的技术和 AI 产品无关。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/danshipper/status/2097136523066110240">Dan Shipper: i was looking through my gmail messages from the early 2000s i have incredible news for you 1...</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>翻看旧邮件想起一个名字</p>
<p class="source-line">Follow Builders · X 动态 · Dan Shipper · 9月8日 01:34 UTC · 喜欢 415 · 转发 2 · 回复 23</p>
<p class="archive-item-content">作者翻看早期 Gmail 邮件，向过去的自己提到想出了一个名字，内容无实质价值。</p>
<p class="archive-item-translation"><span>中文摘要</span>一条缺乏技术细节的个人回忆推文，与用户关注领域无关。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2097136075357798679">Guillermo Rauch: Lots of cool stuff shipping this week</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：本周发布很多酷东西</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 9月8日 01:32 UTC · 喜欢 201 · 转发 2 · 回复 29</p>
<p class="archive-item-content">Guillermo Rauch 发布一条缺少详情、仅预告有新品发布的推文。</p>
<p class="archive-item-translation"><span>中文摘要</span>一条缺乏技术细节和具体内容的推文，仅表示本周将有大量新品发布。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2097134278358548658">Guillermo Rauch: Your software factory needs high quality video recording. 𝚊𝚐𝚎𝚗𝚝-𝚋𝚛𝚘𝚠𝚜𝚎𝚛 delivers. We’re shipp...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：你的软件工厂需要高质量视频录制，agent-browser 已支持</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 9月8日 01:25 UTC · 喜欢 1030 · 转发 27 · 回复 37</p>
<p class="archive-item-content">Vercel CEO Guillermo Rauch announces agent-browser now includes high-quality video recording to support software factory review, testing, and QA workflows.</p>
<p class="archive-item-translation"><span>中文摘要</span>Vercel CEO Guillermo Rauch 宣布 agent-browser 新增高质量视频录制功能，用于软件工厂的审查、测试和 QA 流程。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2097133868549816429">Garry Tan: Children need to be teach-yourself-on-YouTube-maxxing https://t.co/1N6fJEHLyK</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Garry Tan：孩子们需要以 YouTube 自学为最大目标</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 9月8日 01:24 UTC · 喜欢 465 · 转发 27 · 回复 43</p>
<p class="archive-item-content">Garry Tan expresses that children should learn by teaching themselves via YouTube.</p>
<p class="archive-item-translation"><span>中文摘要</span>Garry Tan 表示孩子们应该通过 YouTube 自学来最大化学习能力。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2097129408729604237">Peter Yang: Btw @GeminiApp is fantastic for all kinds of music https://t.co/lqJYZv0wMA</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>GeminiApp 音乐功能推荐</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 9月8日 01:06 UTC · 喜欢 5 · 转发 0 · 回复 3</p>
<p class="archive-item-content">一条关于 GeminiApp 音乐功能的简短推荐，缺乏技术深度和相关性。</p>
<p class="archive-item-translation"><span>中文摘要</span>简短的 GeminiApp 音乐功能推荐，无技术细节，与用户兴趣不符。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2097128951604986055">Peter Yang: AI for family videos to remember. It did a pretty great job. https://t.co/Jyi4Iw8c1e</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：用 AI 制作家庭视频以作纪念，效果相当不错</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 9月8日 01:04 UTC · 喜欢 10 · 转发 0 · 回复 5</p>
<p class="archive-item-content">一条关于 AI 生成家庭视频的推文，展示了效果但未提供技术细节。</p>
<p class="archive-item-translation"><span>中文摘要</span>这是一条简短推文，提及 AI 用于创建家庭纪念视频，并称效果良好，但未涉及技术实现或行业见解。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/rauchg/status/2097116011384426516">Guillermo Rauch: ▲ ~/𝚛𝚊𝚞𝚌𝚑𝚐/𝚘𝚜𝚜-𝚐𝚛𝚊𝚗𝚝𝚜/ 𝚕𝚜▐ (v2) I&#x27;m announcing v2 of my open source grants of $1,000USD to 35...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Guillermo Rauch：▲ ~/𝚛𝚊𝚞𝚌𝚑𝚐/𝚘𝚜𝚜-𝚐𝚛𝚊𝚗𝚝𝚜/ 𝚕𝚜▐ (v2) 我宣布我的开源资助计划第二版，向 35 位杰出贡献者提供每人 1000 美元</p>
<p class="source-line">Follow Builders · X 动态 · Guillermo Rauch · 9月8日 00:13 UTC · 喜欢 678 · 转发 33 · 回复 75</p>
<p class="archive-item-content">Guillermo Rauch announces v2 of his open source grants ($1000 each to 35 contributors) across five themes: agent skills/tools, local AI, performance, high-quality foundations, and cool experiments.</p>
<p class="archive-item-translation"><span>中文摘要</span>Guillermo Rauch 宣布其开源资助计划第二版，向 35 位贡献者各提供 1000 美元，主题涵盖代理技能与工具、本地 AI、性能、高质量基础及酷实验。</p>
</article>
</div>
</section>
