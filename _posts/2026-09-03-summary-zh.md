---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
lang: zh
---

> 从 60 条内容中筛选出 12 条重要资讯。

---

1. [谷歌发布 Gemini 3.8 Flash 及网络安全专用版 Flash Cyber](#item-1) ⭐️ 8.6/10
2. [Claude Fable 5.1：科学基准大幅提升，鹈鹕测试表现亮眼](#item-2) ⭐️ 8.3/10
3. [Meta 发布 Muse Spark 1.3，低价登顶 DeepSWE 基准](#item-3) ⭐️ 8.0/10
4. [报告：三个网站炮制 21.5 万“最佳软件”页面，Perplexity 引用](#item-4) ⭐️ 8.0/10
5. [Paint.NET 作者透露：Claude 编写了面向 WINE 的 Direct2D 重写](#item-5) ⭐️ 8.0/10
6. [World Labs 发布新世界模型 Atlas：一张图生成完整 3D 场景](#item-6) ⭐️ 8.0/10
7. [Qwen3.8-Max-0902 登顶 Code Arena WebDev，以 $5/MToken 领跑 Pareto 前沿](#item-7) ⭐️ 7.7/10
8. [Cursor 推出 Self-Hosted Machines，让云智能体在企业自有机器上执行](#item-8) ⭐️ 7.67/10
9. [Anthropic 发布电商 Agent 架构指南并开源 commerce-agents 参考实现](#item-9) ⭐️ 7.58/10
10. [英伟达接近以 129 亿美元收购 Hugging Face](#item-10) ⭐️ 7.3/10
11. [Claude 为 Cowork 和 Claude Code 新增后台操作电脑能力](#item-11) ⭐️ 7.03/10
12. [OpenAI API 现 GPT-6 'Astra' 踪迹：404 状态码泄露](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemini 3.8 Flash 及网络安全专用版 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 8.6/10

谷歌发布了 Gemini 3.8 Flash，这是 3.7 Flash 的升级版本，速度更快、能力更强；同时还推出了专门用于自主发现软件漏洞并生成可用补丁的 Gemini 3.8 Flash Cyber 变体。该模型在软件工程、智能体任务和特定领域多步推理方面均有显著提升。 早期基准测试显示，Gemini 3.8 Flash 在 Artificial Analysis 上获得 59 分的智能评分，与 Opus 5 等更大的旗舰模型不相上下——这对一个低成本的"Flash"型号来说非常惊人。其速度、低价和强大的 HTML/JavaScript 生成能力相结合，使其对 AI 开发者工具和智能体工作流极具吸引力。 该模型支持可自定义的思考强度级别（高、中、低），以平衡质量、成本和延迟，并保留了 Gemini 对音频和视频的多模态输入支持——这是与 OpenAI 和 Anthropic 旗舰模型的重要差异。Simon Willison 报告称，仅用约 1.8 美分和 13 秒就生成了一个精美的 HTML/JavaScript 作品，但他也指出低思考级别相比 3.7 可能有所退步。

hackernews · bratao · 9月2日 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49537553) · 4 个来源

**核验**: 多源印证

**背景**: Gemini Flash 是 Google DeepMind 面向高吞吐、低延迟场景推出的轻量级、高性价比模型系列。新的 3.8 Flash 版本在 3.7 Flash 基础上，针对软件工程、智能体知识工作流和特定领域推理进行了改进。Flash Cyber 变体专为网络安全设计，可自主识别漏洞并生成补丁。谷歌还展示了该模型的编码能力：在 Google Antigravity 中仅用一条提示词就构建了一个完整可玩的 DOS 风格谷歌地图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3.8 Flash and 3.8 Flash Cyber - The Keyword</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://cybersecuritynews.com/gemini-3-8-flash-cyber/">Google Launches Gemini 3.8 Flash Cyber to Identify and Auto ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极：Simon Willison 强调了其在 HTML/JavaScript 生成方面出色的速度与成本比（1.8 美分、13 秒），另一位评论者指出它在 DeepSwe 基准测试中排名第一、击败 Opus 5，还有用户报告在旅行规划应用中的实际表现优异。一些用户称赞 Gemini 的多模态音频/视频输入和低价适合媒体分析，不过 Willison 也指出低思考强度级别相比 3.7 可能有所退步。

**标签**: `#Gemini`, `#AI models`, `#Google DeepMind`, `#AI developer tools`, `#LLM release`

---

<a id="item-2"></a>
## [Claude Fable 5.1：科学基准大幅提升，鹈鹕测试表现亮眼](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/) ⭐️ 8.3/10

Anthropic 发布了 Claude Fable 5.1（以及 Mythos 5.1），宣称其在编程、知识工作和长期问题求解方面树立了新标准。在全新的 Terminal-Bench-Science 0.1 基准上，Fable 5.1 取得 52.6% 的成绩，高于 Fable 5 的 24.7%、Opus 5 的 29.0% 和 GPT-5.6 Sol 的 22.4%；Simon Willison 还在全部五个推理等级上测试了它的鹈鹕绘图能力。 这是一次重要的 Claude 版本发布，其最显著的提升出现在科学研究基准上，表明 Anthropic 正发力面向科学工作流的 AI 智能体。Willison 的鹈鹕实测为模型的指令遵循和代码生成质量提供了独立、可核查的验证，而不只是依赖厂商的基准宣传。 Fable 5.1 提供五个推理等级——low、medium、high、xhigh 和 max——并且无法完全关闭推理。在 Willison 的测试中，low 和 medium 设置下模型似乎跳过了鹈鹕提示词的推理（没有推理文本，输出 token 分别约为 1,998 和 1,977），而 high 设置使用了 2,612 个 token、耗时 29.6 秒、花费 13.087 美分；其他基准相比科学基准的大幅跃升只有小幅改进。

rss · Simon Willison · 9月1日 23:57 · 2 个来源

**核验**: 多源印证

**背景**: “鹈鹕基准”（pelican benchmark）是 Simon Willison 推广的一个非正式测试，要求大语言模型生成一只骑自行车的鹈鹕的 SVG 图片，以此具体、可核查地比较模型的指令遵循、视觉构图和代码生成能力。Terminal-Bench-Science 是一个全新的持续演进基准，于 8 月 27 日首次公布，用于评估 AI 智能体在生命科学、物理科学、地球科学和数学等领域中由专家策划的研究工作流上的表现，首批包含 70 个任务。Willison 此前曾指出，鹈鹕基准与模型整体质量的相关性随时间有所减弱，但他仍认为在同一模型家族内、以及不同推理强度设置之间进行比较是有价值的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.terminal-bench-science.ai/announcement">Terminal-Bench-Science 0.1</a></li>
<li><a href="https://github.com/harbor-framework/terminal-bench-science">GitHub - harbor-framework/terminal-bench-science: Terminal-Bench-Science: Evaluating AI agents on research workflows across scientific domains · GitHub</a></li>
<li><a href="https://gigazine.net/gsc_news/en/20250609-llms-pelicans-on-bicycles/">Here's what happens when you run the AI benchmark 'Draw a Pelican ...</a></li>

</ul>
</details>

**标签**: `#Claude Fable 5.1`, `#Anthropic`, `#AI benchmarks`, `#LLM evaluation`, `#AI coding`

---

<a id="item-3"></a>
## [Meta 发布 Muse Spark 1.3，低价登顶 DeepSWE 基准](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta 发布了 Muse Spark 1.3，这是一款低成本的编程与智能体 AI 模型，据称在 DeepSWE 基准上取得了迄今最高分（75.4）。该模型已在 Claude Code 和 Simon Willison 的 llm 命令行工具等开发者工具中开始测试。 此次发布增强了低成本 AI 编程助手这一档位，为开发者在日常智能体任务中提供了比前沿模型更便宜的选择。其 DeepSWE 最高分以及对现有工具链的兼容性，可能加剧模型提供商之间的价格竞争。 Muse Spark 1.3 增加了面向高难度推理与智能体任务的 max reasoning 能力，并提升了真实场景可用性，能够跟踪上下文和先前结果、处理混乱或冲突的输入。社区测试中，一次请求约花费 4.23 美分、耗时 38 秒，生成结果被认为优于 Muse Spark 1.2。

hackernews · bvaldivielso · 9月2日 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49541256)

**核验**: 多源印证

**背景**: Muse Spark 是 Meta 超级智能实验室（Meta Superintelligence Labs）开发的大语言模型，于 2026 年 4 月首次亮相，并在 2026 年 7 月以 Muse Spark 1.1 版本发布。DeepSWE 是 Datacurve 推出的防数据污染编程基准，用 91 个代码库中 113 个原创、长周期软件工程任务（覆盖 TypeScript、Go、Python、JavaScript 和 Rust）来评估模型。llm 是一个流行的开源命令行工具，可在终端中调用多种大语言模型；Claude Code 则是一种编程智能体工具，可配置指向不同的模型端点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-spark-1-3">Introducing Muse Spark 1.3 | Meta AI Research</a></li>
<li><a href="https://deepswe.datacurve.ai/">DeepSWE measures frontier coding agents on original, long-horizon...</a></li>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/llm: Access large language models from the ...</a></li>

</ul>
</details>

**社区讨论**: 评论者反应热烈：有人通过 llm 进行了廉价且快速的测试，认为 1.3 的输出明显优于 1.2；还有人指出 DeepSWE 75.4 是迄今最高分，短暂超过了 Gemini 3.8 Flash。一位使用过 Spark 1.2 的开发者称赞其价格低廉、配合度高，另一位则询问是否应让 Claude Code 指向 Muse Spark 端点，并征求对编程智能体工具的看法。还有评论者称赞 Meta，同时讽刺地说这一发布“几乎”让他们忘记了 Meta 因儿童社交媒体成瘾面临的 180 亿美元诉讼。

**标签**: `#AI agents`, `#AI developer tools`, `#coding models`, `#Muse Spark`, `#benchmarks`

---

<a id="item-4"></a>
## [报告：三个网站炮制 21.5 万“最佳软件”页面，Perplexity 引用](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

Trellner 的一份新调查报告发现，仅三个网站就通过程序化方式生成了 215,128 个“最佳软件”榜单页面，而 Perplexity 等 AI 搜索引擎经常在回答中引用这些页面。报告揭露了低质量、AI 生成的 SEO 垃圾内容如何成为 AI 推荐的主要来源之一。 这件事很重要，因为 AI 搜索引擎本应提供可信来源，却越来越多地引用机器生成的垃圾内容，导致回答质量下降并削弱用户信任。这也标志着新一轮军备竞赛：内容农场正在专门针对 AI 问答引擎而非传统搜索引擎进行优化。 报告指出，这三个网站通过程序化 SEO 模板大规模生成“最佳软件”列表页，合计 215,128 个页面。Perplexity 对这些页面的引用说明，AI 问答引擎会继承开放网络中的偏见和垃圾内容；报告还警告，这类人为制造的来源很难被用户察觉。

hackernews · jakobgreenfeld · 9月2日 13:59 · [社区讨论](https://news.ycombinator.com/item?id=49536375)

**核验**: 多源印证

**背景**: 程序化 SEO（programmatic SEO）是一种利用模板和数据自动批量生成大量网页、以覆盖大量搜索关键词的技术。Perplexity 是一款 AI 问答搜索引擎，它结合大语言模型与实时网络搜索来合成回答，并标注引用来源。这份报告揭示了一个日益严重的问题：当 AI 生成的内容充斥网络时，AI 搜索引擎可能会引用其他 AI 生成的页面，形成污染推荐结果的反馈循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perplexity_AI">Perplexity AI</a></li>
<li><a href="https://www.semrush.com/blog/programmatic-seo/">What Is Programmatic SEO? Examples + How to Do It</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为 AI 模型缺乏对来源的怀疑精神。有用户指出，LLM 倾向于偏爱自己生成的内容，并举例说 Claude 和 Codex 可复现地表现出这种偏好；另一位用户则描述了 LLM 自信地推荐一个并不存在的“Foobar 广场”并附上生动细节。还有人观察到 Perplexity 为追求速度导致结果质量下降，并指出智能体引用的对比页面往往是其中一家被比较公司发布的 AI 生成 AEO 内容。

**标签**: `#AI search`, `#SEO spam`, `#Perplexity`, `#LLM-generated content`, `#AI recommendations`

---

<a id="item-5"></a>
## [Paint.NET 作者透露：Claude 编写了面向 WINE 的 Direct2D 重写](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

在 2026 年 9 月的一篇论坛帖子中，Paint.NET 作者 Rick Brewster 透露，Anthropic 的 Claude 从零编写了一个洁净室逆向工程的 Direct2D 重写版本，使 Paint.NET 可以通过 /wine 参数在 WINE 上运行。这段约 18 万行、位于 PaintDotNet.Windows.Direct2D1.Managed.dll 的代码未经彻底审查，被形容为“vibe coding”（氛围编程）产物。 这是一个标志性的真实案例：AI 编程代理生成了大规模、可运行的系统级重实现，而人类维护者表示没有 AI 这件事根本不可能发生。它既展示了 AI 生成代码在雄心勃勃项目上的潜力，也凸显了发布数十万行未经审查代码的严重风险。 Brewster 表示他不得不“盯梢”Claude 的资源管理问题，包括修复引用计数对象缺失的 COM AddRef() 调用，并多次否决糟糕的设计或架构决策。他也称赞 Claude 逆向推导出 Direct2D 内置效果库所需公式的能力，同时指出 Paint.NET 其余代码约 70 万行、是他 20 多年工作的成果。

rss · Simon Willison · 9月2日 05:50

**核验**: 多源印证

**背景**: WINE 是一个兼容层，通过重新实现 Windows API 让 Windows 应用能在 Linux 等操作系统上运行。Direct2D 是 Windows 的 2D 图形渲染 API，而 WINE 对它的支持不完整，长期以来阻碍了 Paint.NET 的运行。洁净室逆向工程（clean-room reverse engineering）指依据规格说明重新创建设计、而不复制原始代码，有助于避免侵犯版权。“Vibe coding”（氛围编程）一词由 Andrej Karpathy 推广，指引导、测试和反馈 AI 生成的代码，而非手动逐行编写。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clean-room_reverse_engineering">Clean-room reverse engineering</a></li>
<li><a href="https://github.com/resources/articles/what-is-vibe-coding">What Is Vibe Coding? - GitHub</a></li>

</ul>
</details>

**标签**: `#AI coding`, `#Claude`, `#WINE`, `#Direct2D`, `#vibe coding`

---

<a id="item-6"></a>
## [World Labs 发布新世界模型 Atlas：一张图生成完整 3D 场景](https://x.com/op7418/status/2094988419722248397) ⭐️ 8.0/10

李飞飞创立的 World Labs 发布了新一代世界模型 Atlas，只需一张或几张图片就能构建完整的 3D 空间场景。它支持像素级精确相机控制的视频生成（最长 1 分钟、1440p）、通过点云和 3D 高斯泼溅进行 3D 场景重建，以及子弹时间等时空仿真。 Atlas 将生成式 AI 从 2D 图像与视频合成推进到可持久、可漫游的 3D 世界，可能重塑影视制作、游戏、机器人训练和空间计算等领域。它还能重建真实场景并模拟时间演变，进一步印证了世界模型作为具身智能发展路径的价值。 Atlas 将每张输入图像锚定在共享空间上下文中的具体 3D 位置，再继续生成未见内容，同时保持场景一致性。其 3D 重建效果据称超过了专门针对 3D 高斯泼溅优化的模型，还能把普通手机拍摄的视频重新取景为子弹时间效果。

twitter · 歸藏(guizang.ai) · 9月2日 03:18

**核验**: 多源印证

**背景**: 世界模型（world model）是一种学习物理世界运行规律的神经网络，能够根据图像、视频等输入数据预测和模拟未来状态。3D 高斯泼溅（3D Gaussian Splatting）是一种光栅化技术，可从少量 2D 图像实时渲染逼真的 3D 场景，是新视角合成的重要表示方法。Atlas 将两者结合，以图片为空间锚点，生成一致、可漫游的 3D 场景与视频。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/gaussian-splatting">Introduction to 3D Gaussian Splatting - Hugging Face</a></li>

</ul>
</details>

**标签**: `#world model`, `#3D generation`, `#computer vision`, `#generative AI`, `#World Labs`

---

<a id="item-7"></a>
## [Qwen3.8-Max-0902 登顶 Code Arena WebDev，以 $5/MToken 领跑 Pareto 前沿](https://x.com/Alibaba_Qwen/status/2094982928371794077) ⭐️ 7.7/10

阿里巴巴通义千问发布 Qwen3.8-Max-0902，该模型在 Code Arena WebDev 排行榜上以 1,691 分首次亮相即登顶总榜第一。该模型现已可在 QwenCloud 试用，混合定价为 $5/MToken，成为 Pareto 前沿上得分最高的模型。 此次发布为开发者提供了一个价格极具竞争力的前沿级编程模型，巩固了通义千问在 AI 开发者工具市场中的地位。这也表明开源权重实验室能够在质量和成本效率上与顶级闭源模型同台竞争。 该模型在 Code Arena WebDev 上取得 1,691 分，该基准测试评估需要多步推理和工具调用的智能体前端编码工作流。$5/MToken 为按每百万 token 报价的混合价格，这是 API 定价的标准单位；模型现已在 QwenCloud 开放试用。

aihot · X：通义千问 / Qwen (@Alibaba_Qwen) · 9月2日 02:57 · [中文阅读](https://aihot.virxact.com/items/cmtjimzgx083zrobvekm2zmje)

**核验**: 多源印证

**背景**: Code Arena WebDev 是一个公开排行榜，根据前端 Web 开发任务（包括需要多步推理和工具调用的智能体编码工作流）对 AI 模型进行排名。在 AI 模型经济学中，Pareto 前沿指这样一组模型：不存在更便宜的模型能达到同等或更高的智能水平；在最近一次快照中，351 个定价 LLM 中只有 13 个位于该前沿上。Token 定价通常以每百万 token（MToken）为单位报价，输入和输出 token 分别计价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arena.ai/leaderboard/code/webdev/">Code Arena WebDev leaderboard</a></li>
<li><a href="https://artificialcuriositylabs.ai/posts/pareto-frontier-is-the-model-market-map/">The Pareto Frontier Is the Model Market Map | Artificial Curiosity Labs</a></li>
<li><a href="https://www.solvimon.com/glossary/ai-token-pricing">What is AI Token Pricing? | Solvimon Glossary</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#AI model release`, `#Code Arena`, `#benchmark`, `#AI pricing`

---

<a id="item-8"></a>
## [Cursor 推出 Self-Hosted Machines，让云智能体在企业自有机器上执行](https://cursor.com/blog/self-hosted-machines) ⭐️ 7.67/10

Cursor 于 2026 年 3 月 25 日发布 Self-Hosted Machines，让云智能体的工具执行迁移到企业自有网络内的机器上运行。智能体的推理、规划与循环仍留在 Cursor 云端，worker 通过出站 HTTPS 连接与本地机器对接，Cursor 不会主动连入企业网络。 这一功能解决了企业采用 AI 智能体的主要障碍——数据安全与代码保密问题，让代码、构建产物和密钥全部留在客户自有基础设施内。它增强了 Cursor 在 AI 开发者工具市场的竞争力，并可能加速自主编码智能体在企业中的大规模落地。 Self-Hosted Machines 支持自动扩缩容、休眠以及沙箱合作伙伴，专为智能体并行自主处理大量软件任务而设计。其架构将工具执行（本地）与推理规划（云端）分离，仅通过 worker 的出站 HTTPS 连接通信，企业无需开放入站端口。

aihot · Cursor Blog · 9月2日 12:00 · [中文阅读](https://aihot.virxact.com/items/cmtkffuf503cbrobqkwhimxmp)

**核验**: 多源印证

**背景**: 云智能体是能够自主完成软件开发任务的 AI 系统，例如编辑代码、运行构建、执行测试等。企业此前对采用这类智能体持谨慎态度，因为代码和密钥可能离开自有网络；Self-Hosted Machines 通过在内部基础设施上运行工具执行、同时把基于大模型的推理留在云端，解决了这一安全顾虑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/blog/self-hosted-cloud-agents">Run cloud agents in your own infrastructure · Cursor</a></li>
<li><a href="https://cursor.com/changelog/03-25-26">Self-hosted Cloud Agents · Cursor</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/cursor-self-hosted-machines-move-agents-on-prem">Cursor self-hosted machines move agents on-prem | StartupHub.ai</a></li>

</ul>
</details>

**标签**: `#Cursor`, `#AI Agents`, `#Enterprise AI`, `#Self-Hosted`, `#AI Developer Tools`

---

<a id="item-9"></a>
## [Anthropic 发布电商 Agent 架构指南并开源 commerce-agents 参考实现](https://claude.com/blog/the-anatomy-of-effective-commerce-agents) ⭐️ 7.58/10

Anthropic 发布了一份电商 Agent 构建指南，内容基于与零售、旅游、电信等团队的生产落地经验。同时，Anthropic 开源了 anthropics/commerce-agents 仓库，其中包含基于 Claude 构建的购物与商家 Agent 参考实现。 这为开发者提供了一套经过生产验证的电商 Agent 架构，而非停留在推测性的设计模式。开源参考实现降低了上手门槛，为零售、旅游、电信和娱乐等场景提供了可直接借鉴的起点。 推荐架构是让单个 Claude 在标准 Agent 循环中配合技能（skills）与工具运行，而不是按领域拆分成多个子智能体。commerce-agents 仓库包含零售、电商、电信和娱乐等场景的示例，指南还采用了 Anthropic 的 Agent Skills 格式来提供可组合的能力。

aihot · Claude：Blog（网页） · 9月2日 17:01 · [中文阅读](https://aihot.virxact.com/items/cmtkcffah018zrog0zokk6s30)

**核验**: 多源印证

**背景**: Agent 循环（agent loop）是 AI Agent 反复执行的“感知-规划-行动-观察”周期，直到达成目标为止，其本质是 LLM 与记忆、规划、工具使用的结合。Agent Skills 是 Anthropic 推出的开放格式，用于为 Agent 提供程序性知识与能力，类似于给新员工准备的入职指南；开发者可以用可组合的技能来定制 Agent，而无需为每个场景单独构建专用 Agent。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/commerce-agents">GitHub - anthropics/commerce-agents: Reference blueprint for building shopping and merchant agents with Claude. Examples in retail, commerce, telecom, and entertainment included. · GitHub</a></li>
<li><a href="https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills">Equipping agents for the real world with Agent Skills \ Anthropic</a></li>
<li><a href="https://atlan.com/know/ai-agent/what-is-an-agent-loop/">The AI Agent Loop: Architecture and Failure Modes [2026]</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Anthropic`, `#Agent Architecture`, `#Open Source`, `#E-commerce`

---

<a id="item-10"></a>
## [英伟达接近以 129 亿美元收购 Hugging Face](https://x.com/rohanpaul_ai/status/2094975190468010368) ⭐️ 7.3/10

据彭博社报道，英伟达正接近以约 129 亿美元收购 Hugging Face，交易总额可能达到约 140 亿美元。双方尚未达成最终协议，条款仍可能变动。 若交易完成，这将成为规模最大的 AI 并购之一，使英伟达深入掌控开源 AI 生态与开发者工具链。这可能重塑模型分发方式，以及开发者获取 AI 基础设施的途径。 据报道，这一价格约为 Hugging Face 在 2023 年融资轮中 45 亿美元估值的 2.9 倍，相当于其约 1.5 亿美元年化收入的 86 倍。英伟达还在讨论在交易中加入 10 亿美元的员工留任方案。

aihot · X：Rohan Paul (@rohanpaul_ai) · 9月2日 02:26 · [中文阅读](https://aihot.virxact.com/items/cmtjhy5ze07gorobv62fpf0wi)

**核验**: 多源印证

**背景**: Hugging Face 是一家总部位于纽约的公司，以开源 Transformers 库和庞大的社区平台闻名，开发者可在该平台分享和部署机器学习模型。英伟达是用于训练和运行 AI 模型的 GPU 的主要供应商，并一直在向软件和开发者平台扩张。收购将把英伟达的硬件生态与 Hugging Face 广泛使用的模型中心和工具结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/hugging-face">What is Hugging Face? - IBM</a></li>
<li><a href="https://365datascience.com/trending/what-is-hugging-face/">What is Hugging Face? A Beginners Guide – 365 Data Science</a></li>

</ul>
</details>

**社区讨论**: X 上的讨论简短而积极，有用户称这对 Hugging Face 来说是“一笔巨大的交易”。相关帖子还强调了报道中的估值倍数和可能达 10 亿美元的留任方案，反映出人们对交易财务条款的关注。

**标签**: `#Nvidia`, `#Hugging Face`, `#AI 并购`, `#开源 AI`, `#AI 开发者工具`

---

<a id="item-11"></a>
## [Claude 为 Cowork 和 Claude Code 新增后台操作电脑能力](https://x.com/claudeai/status/2095226833293685100) ⭐️ 7.03/10

Anthropic 官方宣布，Claude Cowork 和 Claude Code 现已支持在后台操作电脑。用户把任务交给 Claude 后，它可以像人一样点击、输入和打开应用，而用户可以同时去做其他事情。 这标志着 Anthropic 的 computer use 能力从 API 测试版扩展到终端用户智能体产品，实现了异步、无需监督的桌面自动化。对希望委托多步骤任务并节省时间的知识工作者和开发者来说意义重大。 Cowork 是 Anthropic 面向非技术任务的 macOS 智能体，可读取和编辑文件、整理桌面、从截图生成电子表格等。Claude Code 是面向开发者的智能编码工具，能理解代码库、编辑文件并运行命令；本次公告为这两款产品都增加了后台操作能力。

aihot · X：Claude (@claudeai) · 9月2日 19:06 · [中文阅读](https://aihot.virxact.com/items/cmtkh71ky017vrolly7trswyx)

**核验**: 多源印证

**背景**: Anthropic 于 2024 年随 Claude 3.5 Sonnet 首次推出 "computer use" 测试版，让开发者能够通过 API 构建操作电脑的智能体。Cowork 和 Claude Code 是 Anthropic 面向终端用户的智能体产品：Cowork 面向办公和个人任务，Claude Code 面向软件开发。后台操作意味着智能体可以在用户转向其他活动时继续完成被委托的任务，从而实现异步委托。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork">Get started with Claude Cowork | Anthropic Help Center</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.anthropic.com/news/3-5-models-and-computer-use">Introducing computer use , a new Claude 3.5 Sonnet, and Claude...</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI Agents`, `#Computer Use`, `#Automation`, `#Product Launch`

---

<a id="item-12"></a>
## [OpenAI API 现 GPT-6 'Astra' 踪迹：404 状态码泄露](https://x.com/synthwavedd/status/2095184148981842161) ⭐️ 7.0/10

一条推文称，OpenAI Responses API 上已暂存模型标识符 'gpt-6-astra'，请求该名称会返回 404 Not Found，而不存在的名称则返回 400 错误。OpenAI 尚未官方确认该模型，但已知的 '5.6 Cyber' 标识符也呈现相同的 404 模式。 这是 OpenAI 正在准备代号为 'Astra' 的 GPT-6 模型变体的强烈早期信号，能让开发者和 AI 社区提前开始集成与测试。这也展示了一种通过公共 API 状态码差异来发现未发布模型名称的实用检测技巧。 该检测方法利用 Responses API 对已暂存或已知模型标识符（如 'gpt-6-astra' 和 '5.6 Cyber'）返回 404，而对乱写的标识符返回 400 的差异。据报道，AWS Bedrock API 中也有类似现象，曾用于在 'Fable 5.1' 发布前一天发现该模型。

twitter · leo 🐾 · 9月2日 16:16

**核验**: 多源印证

**背景**: OpenAI Responses API 于 2025 年 3 月 11 日发布，是 OpenAI 用于生成模型回复的最先进接口，支持文本和图像输入及文本输出，并可创建有状态的交互。模型标识符（slug）是开发者在 API 请求中用来选择模型的名称，提供商通常会在正式发布前将即将推出的模型暂存到后端系统中。因此，404 与 400 响应的差异可以揭示被保留的模型名称。Amazon Bedrock 是 AWS 的托管服务，用于通过 API 访问基础模型，这解释了为何 Bedrock API 中也存在类似的检测模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://grokipedia.com/page/OpenAI_Responses_API">OpenAI Responses API</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/Welcome.html">Welcome - Amazon Bedrock</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#Responses API`, `#AI models`, `#API detection`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="12"><span>其他追踪推文</span><span class="archive-tab-count">12</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="11"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">11</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2095291379559580154">@dotey: Google 今天发布了 Gemini 3.8 Flash，同时推出的还有一个专门用于网络安全的变体 3.8 Flash Cyber。 Google 最近这个发布节奏很有意思。7 月底发...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 23:22 UTC · 喜欢 3 · 转发 1 · 回复 3 · 浏览 4663</p>
<p class="archive-item-content">Google 今天发布了 Gemini 3.8 Flash，同时推出的还有一个专门用于网络安全的变体 3.8 Flash Cyber。<br>
<br>
Google 最近这个发布节奏很有意思。7 月底发 3.6 Flash，8 月中发 3.7 Flash，今天又发 3.8 Flash，间隔都只有大约三周。而与此同时，今年 6 月本该发布的 Gemini 3.5 Pro 至今没有出现。Google 在 Flash 这条线上疯狂迭代，但更高端的 Pro 系列迟迟没有动静。<br>
<br>
再加上 8 月初 DeepMind 经历了一轮震荡，创始人兼 CEO Demis Hassabis 从日常管理退出，转任 DeepMind 主席和 Alphabet 首席科学家，首席科学家 Jeff Dean 也离职创业。新任 SVP Koray Kavukcuoglu 接管了 Gemini 的开发。这种背景下连续推 Flash，不知道是不是某种程度上的刷存在感。<br>
<br>
回到模型本身。<br>
<br>
3.8 Flash 和 3.7 Flash 一样的价格，每百万输入 Token 0.75 美元，每百万输出 Token 3.75 美元。<br>
<br>
注意这个价格是促销价，2026 年底到期后翻倍变成 1.5 和 7.5 美元。<br>
<br>
跑分上，3.8 Flash 在 DeepSWE v1.1（一个衡量模型自主解决复杂工程问题能力的评测）上拿到 73.7%，仅比 Claude Opus 5 的 74% 低 0.3 个百分点，超过了 GPT-5.6 Sol 的 72.7%、Claude Sonnet 5 的 53.8%，以及上代 3.7 Flash 的 65.3%。<br>
<br>
至于为什么评分高，Google 自己的解释是 3.8 Flash “works harder”，遇到复杂任务会多想几步、多调用几次工具，代价是消耗更多 Token。<br>
<br>
另一个跑分细节：3.8 Flash 在 Gray Swan 提示词注入（prompt injection）评测中被攻破的概率只有 5.5%，对比 DeepSeek V4 Pro 的 60.1%、Grok 4.6 的 51.8%。也就是说，用 3.8 Flash 做 AI Agent 被恶意指令劫持的风险要低得多。<br>
<br>
跟着 Gemini 3.8 Flash 一起发布的还有 3.8 Flash Cyber，这是一个专门为网络安全防御训练的模型，只通过 Google 新推出的 Fairwind Program 向经审核的政府机构、关键基础设施运营商和安全研究人员开放，目前全球有 650 多个合作伙伴。普通开发者用不了。<br>
<br>
Google 把这个模型的能力框定在安全防御上，强调它擅长找漏洞和修漏洞，而非攻击利用。在 CyberGym 漏洞发现评测中，3.8 Flash Cyber 拿到 86.2%；在覆盖 20 种编程语言的内部评测中，漏洞发现成功率超过 70%。在 CWE-Bench 自动修补评测中，它以 47.2% 的 pass@1 逼近了前沿模型的 47.8%，但成本低得多。<br>
<br>
一些实际应用案例：<br>
Chrome 安全团队发现 3.8 Flash Cyber 比最好的商用大模型多修复了 2.6 倍的 Chrome 漏洞；<br>
安全公司 Wiz 的内部渗透测试中，它的召回率高出 7.5% 到 9.7%，成本却低了 2.3 到 5.2 倍；<br>
Google Cloud 漏洞研究团队用它在不到两小时内发现了一个关键漏洞，这类漏洞通常需要数月的人工研究。<br>
<br>
3.8 Flash 已经可以通过 Gemini API、Google AI Studio、Android Studio、Antigravity 等渠道使用，Google AI Pro 和 Ultra 订阅用户在 Gemini App 中也能用上。企业版通过 Gemini Enterprise 接入。Cyber 版需要申请 Fairwind Program。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2095282572016095352">@dotey: 如果你想试试 Fable 指挥 GPT 5.6 干活，可以试试这个 Plugin。 我没有试这种模式是因为我直接让 Fable 指挥 Opus 更简单直接，没必要折腾。 如果你用 Fab...</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 22:47 UTC · 喜欢 12 · 转发 2 · 回复 3 · 浏览 5395</p>
<p class="archive-item-content">如果你想试试 Fable 指挥 GPT 5.6 干活，可以试试这个 Plugin。<br>
<br>
我没有试这种模式是因为我直接让 Fable 指挥 Opus 更简单直接，没必要折腾。<br>
<br>
如果你用 Fable API 而不是订阅的话这应该是一种不错的模式。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2095277585500410302">@dotey: 用 Fable 指挥其他 Agent 效果很好是因为它给 的指令很详细，基本上不会出什么岔子 https://t.co/72Lvxzpneh</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 22:27 UTC · 喜欢 44 · 转发 2 · 回复 3 · 浏览 7745</p>
<p class="archive-item-content">用 Fable 指挥其他 Agent 效果很好是因为它给 <br>
 的指令很详细，基本上不会出什么岔子 https://t.co/72Lvxzpneh</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2095216535119843747">@dotey: 看起来 gpt-6-astra 要发了</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 18:25 UTC · 喜欢 29 · 转发 0 · 回复 10 · 浏览 12571</p>
<p class="archive-item-content">看起来 gpt-6-astra 要发了</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/dotey/status/2095214013693243806">@dotey: 基本上你只要让 Fable 指挥其他 Agent 干活，这两个进度条就能持平。 大部分任务你选 Fable + High（或者 Medium，千万别 Max 及以上），然后后面加一句： &gt; 注...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 18:15 UTC · 喜欢 194 · 转发 28 · 回复 20 · 浏览 31501</p>
<p class="archive-item-content">基本上你只要让 Fable 指挥其他 Agent 干活，这两个进度条就能持平。<br>
<br>
大部分任务你选 Fable + High（或者 Medium，千万别 Max 及以上），然后后面加一句：<br>
&gt; 注意你的主要任务是分析、编排和验证，具体任务尽可能交给 subagent（Opus 或 Sonnet）去执行。自己只做需求澄清、方案拆解、任务分发和结果验收，实现类工作（读大量代码、写代码、跑测试、批量修改）一律用 Agent 工具派给 subagent 执行。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/daniel_mac8/status/2095206393682780672">@daniel_mac8: Fable 5.1 orchestrates GPT-5.6 Luna agents. Via the &#x27;fable-advisor&#x27; plugin for Claude Code. 1...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 17:45 UTC · 喜欢 365 · 转发 16 · 回复 30 · 浏览 36989</p>
<p class="archive-item-content">Fable 5.1 orchestrates GPT-5.6 Luna agents.<br>
<br>
Via the &#x27;fable-advisor&#x27; plugin for Claude Code.<br>
<br>
1. Fable 5.1 orchestrates<br>
2. GPT-5.6 Luna implements<br>
3. Fable 5.1 reviews<br>
<br>
Think of it like in-context distillation: give Luna the intelligence of Fable 5.1 at a fraction the cost.</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/OfficialLoganK/status/2095175881690173885">@OfficialLoganK: Introducing Gemini 3.8 Flash, another jump in Gemini&#x27;s agentic + coding capabilities, and our...</a></h3>
<span class="score-badge" data-tier="good" aria-label="7.0 out of 10">7.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 15:43 UTC · 喜欢 9339 · 转发 693 · 回复 667 · 浏览 952200</p>
<p class="archive-item-content">Introducing Gemini 3.8 Flash, another jump in Gemini&#x27;s agentic + coding capabilities, and our 3rd updated Flash model in only 6 weeks...<br>
<br>
This model has been a ton of fun to work with, excited to see what you all think! https://t.co/Cj07lCBtp8</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/latepostnews/status/2095142540660093315">@latepostnews: 晚点独家丨月之暗面向港交所秘密交表，正式启动 IPO 《晚点 LatePost》独家获悉，月之暗面（Kimi）已于本周以保密形式向港交所递交 A1 文件，正式启动港股 IPO 流程。A1...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 13:31 UTC · 喜欢 15 · 转发 2 · 回复 1 · 浏览 18460</p>
<p class="archive-item-content">晚点独家丨月之暗面向港交所秘密交表，正式启动 IPO<br>
<br>
《晚点 LatePost》独家获悉，月之暗面（Kimi）已于本周以保密形式向港交所递交 A1 文件，正式启动港股 IPO 流程。A1 是企业申请在港交所上市时提交的正式申请表之一。<br>
<br>
Kimi 方面回应上述消息称：“对于市场传闻不予置评，目前暂无可以披露的信息。”<br>
<br>
同时据我们了解，Kimi 也正在以 500 亿美元的投前估值推进新一轮融资。这很有可能是 Kimi IPO 前的最后一轮融资。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/wquguru/status/2095114755879190638">@wquguru: 另一个 Claude Code token 管理技巧：看 /usage 时，把周度总消耗和 Fable 周度消耗两条进度条尽量对齐。 Fable 更贵、更聪明，但是额度只有总额度的 50...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @dotey · 9月2日 11:40 UTC · 喜欢 14 · 转发 2 · 回复 4 · 浏览 34257</p>
<p class="archive-item-content">另一个 Claude Code token 管理技巧：看 /usage 时，把周度总消耗和 Fable 周度消耗两条进度条尽量对齐。<br>
<br>
Fable 更贵、更聪明，但是额度只有总额度的 50%，很容易出现两种失衡：<br>
<br>
Fable 条已经 70%，总用量才 40%，智力额度见底，后面只能强行降智<br>
总用量 70%，Fable 才 20%，便宜模型烧得太猛，最强模型的窗口反而被浪费了<br>
<br>
对齐也不必机械对半，找一个自己感觉比较良好的比例，而是让周额度和 Fable 额度大致成比例下降即可，一些性价比高的落地做法：<br>
<br>
主会话用 Fable 做判断、架构、拆任务、复盘；执行、检索、改文件、跑测试丢给  Opus 子代理。<br>
<br>
任务切换就 /clear，长任务中途 /compact。<br>
<br>
每天看几次进度条，Fable 超前就减少 Fable 使用强度；总进度条超前就多把一些关键决策交回 Fable。<br>
<br>
实测下来，这种节奏能让智力密度和额度一起走到重置日，达到一个最佳的状态。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2095032036427993361">@op7418: 前几天跟李继刚、橘子和雅婷一起聊了聊最近关注的一些事情和想法</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 9月2日 06:12 UTC · 喜欢 157 · 转发 30 · 回复 75 · 浏览 44911</p>
<p class="archive-item-content">前几天跟李继刚、橘子和雅婷一起聊了聊最近关注的一些事情和想法</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/yilunAIyyds/status/2095030491519111230">@yilunAIyyds: 请来继刚、歸藏、橘子对谈，几个思考： 1. 让 AI 真正落地的不是产品，是服务 2. 企业 AI 转型，只需要搞定 5% 的人 3. 越土的行业，AI 越吃香 4. 卖 Skill 给...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 9月2日 06:06 UTC · 喜欢 179 · 转发 33 · 回复 9 · 浏览 64744</p>
<p class="archive-item-content">请来继刚、歸藏、橘子对谈，几个思考：<br>
1. 让 AI 真正落地的不是产品，是服务<br>
2. 企业 AI 转型，只需要搞定 5% 的人<br>
3. 越土的行业，AI 越吃香<br>
4. 卖 Skill 给个人用户，是个伪生意<br>
5. 别人的 Skill 再厉害，也进不了你的工作流<br>
6. 下一张社交网络，一半节点不是人<br>
<br>
#aicoding #易论 AI #归藏 #colaOS #李继刚</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/op7418/status/2094996310743306407">@op7418: 昨晚 Claude 发布了 Fable 5.1 和 Mythos 5.1，两者的权重相同。 输入输出价格和 Fable 5 一样，缓存价格降了 75%。 官方的说法是，按 token 计...</a></h3>
<span class="score-badge" data-tier="good" aria-label="8.0 out of 10">8.0</span>
</div>
<p class="source-line">Twitter/X · @op7418 · 9月2日 03:50 UTC · 喜欢 41 · 转发 0 · 回复 68 · 浏览 19760</p>
<p class="archive-item-content">昨晚 Claude 发布了 Fable 5.1 和 Mythos 5.1，两者的权重相同。<br>
<br>
输入输出价格和 Fable 5 一样，缓存价格降了 75%。<br>
<br>
官方的说法是，按 token 计费的话，典型负载大约会便宜 25%，重度 Agent 负载大概会便宜 45%。<br>
<br>
但时间线上全在说 Fable 5.1 的订阅额度消耗得非常快，可能 20 分钟、半小时整个额度就用光了。<br>
<br>
而且这模型还有一些更严重的问题：<br>
<br>
不支持强制的 tool choice，更早的模型读不了它的 thinking block，导致不能中途换模型，改历史消息会让 thinking 失效。<br>
<br>
输出带有不可见的文本水印（这个之前聊过，非常恶心，会导致生成的文案质量变差）<br>
<br>
Artificial Analysis 帮 Anthropic 做预发布测评的反馈显示：即使缓存降价 75%，Fable 5.1 Max 跑完任务的实际开销依然比 Fable 5 Max 贵 20%，因为它的输出 token 大约是 Fable 5 的 1.7 倍。<br>
<br>
看起来还是挺拉胯的，反而更贵了，再加上隐形文本水印以及无法切换模型这些问题。<br>
<br>
是不是意味着一旦它触发了安全护栏，你切到 Opus 5，缓存就直接失效掉了，随后调用成本跟着大幅上涨？</p>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/levie/status/2095024699441119612">Aaron Levie: AI for cyber is about to go vertical. The models increasingly becoming insanely good at findi...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Aaron Levie：AI 网络安全即将垂直起飞</p>
<p class="source-line">Follow Builders · X 动态 · Aaron Levie · 9月2日 05:43 UTC · 喜欢 47 · 转发 5 · 回复 14</p>
<p class="archive-item-content">Aaron Levie argues that AI models are becoming highly effective at finding and exploiting vulnerabilities, making AI-driven triage and automated fixes with human oversight essential, and boosting demand for security roles.</p>
<p class="archive-item-translation"><span>中文摘要</span>Aaron Levie 认为，AI 模型在发现和利用漏洞方面正变得极其出色，企业只能依靠 AI 配合人工监督来分流和自动修复，安全岗位的需求也将因此大增。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2095002897859912044">Nikunj Kothari: Terrifying.. also just the start of how leaks like this are going to get way worse 😭 https://...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari：太可怕了……这也只是这类泄露会变得更糟的开始 😭 https://...</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 9月2日 04:16 UTC · 喜欢 3 · 转发 0 · 回复 0</p>
<p class="archive-item-content">A vague tweet expressing alarm that leaks will get worse, with no technical details or context.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条含糊的推文，表达对泄露问题将变得更糟的担忧，但缺乏技术细节和上下文。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2094999513627025757">Zara Zhang: I wish every city was in Tokyo https://t.co/j1ppDGCx7p</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang：我希望每个城市都在东京</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 9月2日 04:03 UTC · 喜欢 37 · 转发 2 · 回复 7</p>
<p class="archive-item-content">Zara Zhang expresses a wish that every city were in Tokyo, with a link to an unspecified post.</p>
<p class="archive-item-translation"><span>中文摘要</span>Zara Zhang 表达了一个愿望，希望每个城市都在东京，并附上了一个链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2094999358525821099">Peter Yang: fwiw I dislike having alot of random skills installed. I&#x27;m at a point where I only have about...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：顺便说一句，我不喜欢安装很多随机技能，目前只保留大约十几个（大部分是我自己的）</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 9月2日 04:02 UTC · 喜欢 28 · 转发 0 · 回复 9</p>
<p class="archive-item-content">Peter Yang 建议 AI 代理用户不要安装太多随机技能，只保留自己常用的十几个，并保持技能简短、定期删除不用的。</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 建议 AI 代理用户尽量少装随机技能，只保留自己常用的十几个，并保持技能尽可能简短、定期删除不用的。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2094995775952740795">Peter Yang: While I&#x27;m cleaning up my AI skills I have a question for the experts here. Sometimes I end up...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：在我清理 AI 技能时，想请教这里的专家。有时我会陷入……</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 9月2日 03:48 UTC · 喜欢 102 · 转发 2 · 回复 33</p>
<p class="archive-item-content">Peter Yang asks experts how to prevent AI skills from overfitting and drifting when iteratively updating them based on a single manual correction thread.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 提出了一个 AI 技能维护中的常见问题：反复通过 AI 手动迭代修正后，再让 AI 更新技能以实现一次性成功，容易导致技能过拟合和漂移，并询问解决方案。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/petergyang/status/2094987791566622971">Peter Yang: If you&#x27;re trying out Fable 5.1 I highly recommend running: /claude-api prompt-audit on your s...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Yang：如果你在试用 Fable 5.1，我强烈建议运行：/claude-api prompt-audit</p>
<p class="source-line">Follow Builders · X 动态 · Peter Yang · 9月2日 03:16 UTC · 喜欢 1514 · 转发 71 · 回复 38</p>
<p class="archive-item-content">Peter Yang recommends running /claude-api prompt-audit in Fable 5.1 to find redundant rules and clean up skills for newer models.</p>
<p class="archive-item-translation"><span>中文摘要</span>Peter Yang 推荐在 Fable 5.1 中对技能运行 /claude-api prompt-audit，以清理冗余规则并适配最新模型。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/realmadhuguru/status/2094973690576576675">Madhu Guru: Great example of the immense opportunity enterprises have if they build their own post traini...</a></h3>
<span class="score-badge" data-tier="low" aria-label="4.0 out of 10">4.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Madhu Guru：企业构建自有后训练系统的巨大机遇的绝佳范例</p>
<p class="source-line">Follow Builders · X 动态 · Madhu Guru · 9月2日 02:20 UTC · 喜欢 53 · 转发 1 · 回复 0</p>
<p class="archive-item-content">Author highlights Shopify&#x27;s ML team as a great example of the opportunity for enterprises to build their own post-training systems, evals, and data flywheels.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者以 Shopify 的机器学习团队为例，指出企业构建自有后训练系统、评估体系和数据飞轮蕴含巨大机遇。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/trq212/status/2094945951865520458">Thariq: it’s a very good model, I spent a lot of time diving into it- longer write up coming but try...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.0 out of 10">5.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thariq：这是一个非常好的模型，我花了很多时间深入研究——更长的文章即将发布，但请先试试……</p>
<p class="source-line">Follow Builders · X 动态 · Thariq · 9月2日 00:30 UTC · 喜欢 1414 · 转发 50 · 回复 128</p>
<p class="archive-item-content">The author praises a model and recommends using lower reasoning effort for tasks with fewer edge cases, noting that switching effort no longer breaks prompt caching.</p>
<p class="archive-item-translation"><span>中文摘要</span>作者称赞该模型，并建议在验证需求较低或边界情况较少的任务上使用较低推理强度，同时指出切换推理强度不再破坏提示缓存。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2094943457769099520">Zara Zhang: Since when did this type of website design become in vogue? https://t.co/Cwnz0MhMhz</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang：这种网站设计是从什么时候开始流行的？</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 9月2日 00:20 UTC · 喜欢 109 · 转发 1 · 回复 47</p>
<p class="archive-item-content">A vague tweet questioning when a certain website design style became popular, lacking technical detail or actionable insight.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条关于某种网站设计风格何时开始流行的模糊推文，缺乏技术细节和可执行信息。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/danshipper/status/2094942644497457527">Dan Shipper: remember when we used to have to type out low level code like this? https://t.co/h30xZEfRle</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Dan Shipper：还记得我们以前得这样输入底层代码吗？</p>
<p class="source-line">Follow Builders · X 动态 · Dan Shipper · 9月2日 00:17 UTC · 喜欢 56 · 转发 0 · 回复 15</p>
<p class="archive-item-content">Dan Shipper nostalgically remarks about having to type out low-level code, linking to an unspecified example.</p>
<p class="archive-item-translation"><span>中文摘要</span>Dan Shipper 发推怀念过去需要手动输入底层代码的日子，并附上一个未说明的链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2094939684015317363">Thibault Sottiaux: Bullish</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：看涨</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 9月2日 00:05 UTC · 喜欢 5162 · 转发 120 · 回复 880</p>
<p class="archive-item-content">A brief post expressing optimism (&#x27;Bullish&#x27;) with no technical details or context.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条仅表达乐观情绪（“看涨”）的简短帖子，没有技术细节或背景信息。</p>
</article>
</div>
</section>
