---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 29 条内容中筛选出 6 条重要资讯。

---

1. [AI 新超能力：专注与执行](#item-1) ⭐️ 8.0/10
2. [在 8 美元 ESP32-S3 上运行 2890 万参数大语言模型](#item-2) ⭐️ 7.9/10
3. [Claude Opus 5 系统提示词完整泄露，135027 字符，约 3.4 万 token](#item-3) ⭐️ 7.75/10
4. [AI 代币灰色市场转售经济内幕](#item-4) ⭐️ 7.0/10
5. [调查揭露 LLM 代币转售市场](#item-5) ⭐️ 7.0/10
6. [双向语音交互漏洞已修复](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 新超能力：专注与执行](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and) ⭐️ 8.0/10

Rick Manelius 发表了一篇文章，分析了 AI 工具如何帮助开发者专注并执行项目，同时警告过度依赖 AI 会导致大量相似且不兼容的初级软件泛滥。 这一分析揭示了 AI 在软件开发中的双刃剑效应：虽然它提升了个人的生产力和专注力，但有可能导致浅薄且不兼容的实现方式泛滥，从而损害软件的长期多样性和质量。 文章的警告在社区评论中得到印证，评论描述了这样一种趋势：每个问题都被视为用 AI 只需'几个小时'就能解决，导致大量相似但不兼容的项目。此外，一些评论者指出 AI 能处理项目的前 99%，但在最后 1%上遇到困难，从而留下大量接近完成的工作积压。

hackernews · mooreds · 7月26日 13:13 · [社区讨论](https://news.ycombinator.com/item?id=49057877)

**核验**: 已核对原文

**背景**: AI 驱动的编程助手（如 GitHub Copilot、Cursor 等）迅速普及，使开发者能够以前所未有的速度生成代码、修复配置问题并探索想法。这可以大幅降低认知负荷，帮助开发者专注于更高层次的目标。然而，一个日益增长的担忧是，过度依赖这些工具会导致软件同质化，许多开发者产出相似且初级的实现，彼此不兼容，可能抑制创新并带来维护挑战。

**社区讨论**: 社区讨论反映了 nuanced 的观点：许多开发者赞赏 AI 减少了倦怠感并支持了副项目，但大家强烈认同文章关于相似且不兼容的初级软件泛滥的警告。评论者如 cgearhart 描述了'又一个...'的时代，而 staticvar 指出 AI 能处理 99%但无法完成最后 1%，导致大量接近完成的项目。其他如 crucialfelix 和 bigyax 则报告了使用 AI 管理工作流程并保持轻松参与的积极体验。

**标签**: `#AI agents`, `#developer tools`, `#automation`, `#software development`, `#productivity`

---

<a id="item-2"></a>
## [在 8 美元 ESP32-S3 上运行 2890 万参数大语言模型](https://github.com/slvDev/esp32-ai) ⭐️ 7.9/10

开发者 slvDev 成功在 ESP32-S3 微控制器上运行了一个 2890 万参数的大语言模型，完全在设备本地运行，无需连接服务器，生成速度达到每秒 9.5 个 token。 这一突破表明，大语言模型可以在极低成本的硬件上部署，为物联网和嵌入式系统实现离线 AI 推理开辟了可能性，无需依赖云 API 或互联网连接。 该模型利用 Google 的 Per-Layer Embeddings 技术，将其 2890 万参数中的大部分存储在闪存中，每次 token 仅从 2500 万参数的查找表中读取约 450 字节。它在 ESP32-S3 上以端到端 9.5 tok/s 的速度运行，该芯片拥有 512KB SRAM、8MB PSRAM 和 16MB 闪存。

aihot · Hacker News 热门（buzzing.cc 中文翻译） · 7月26日 03:54 · [中文阅读](https://aihot.virxact.com/items/cms1ao381037kro0wqp7mg4x3)

**核验**: 多源印证

**背景**: ESP32-S3 是一种常用于物联网设备的低成本微控制器，其快速内存（SRAM）仅有 512KB。在此类设备上运行大语言模型极具挑战性，因为模型通常需要将所有参数放入快速内存。Per-Layer Embeddings 技术最初来自 Google 的 Gemma 模型，它将庞大的嵌入表存储在慢速闪存中，推理时仅加载必要的行，从而大幅降低内存需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://startupfortune.com/a-developer-ran-a-language-model-on-an-8-chip-and-quietly-broke-the-cloud-ai-model-for-iot/">A developer ran a language model on an $8 chip and quietly broke the cloud AI model for IoT - Startup Fortune</a></li>
<li><a href="https://www.waveshare.com/wiki/ESP32-S3-Zero">ESP 32 - S 3 -Zero - Waveshare Wiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Edge Computing`, `#LLM`, `#Microcontroller`, `#Open Source`

---

<a id="item-3"></a>
## [Claude Opus 5 系统提示词完整泄露，135027 字符，约 3.4 万 token](https://www.ithome.com/0/981/688.htm) ⭐️ 7.75/10

开发者 Eversmile1 在 GitHub 上公开了 Claude Opus 5 的完整系统提示词，包含 135027 字符（约 3.4 万 token），包括 30 个工具的 JSON schema、严格的版权规则和跨会话记忆系统。 此次泄露揭示了领先 AI 模型系统提示词的技术细节，包括工具架构和记忆系统，对开发者极具价值，有助于推动 AI 产品设计和代理技术的创新。 系统提示词共 1511 行，最长的部分是记忆文件系统，采用基于标签的系统和严格的隐私规则。它还包含一个 'recommend_claude_apps' 工具用于推广 Anthropic 自家产品，以及一个对第三方服务限制严格的 'suggest_connectors' 工具。

aihot · IT之家（RSS） · 7月26日 05:33 · [中文阅读](https://aihot.virxact.com/items/cms1dpz52040tro0w3c4a9c8p)

**核验**: 多源印证

**背景**: 系统提示词是给 AI 模型的基础指令集，用于指导其在交互中的行为，通常对最终用户不可见。JSON Schema 是一种声明性语言，用于注释和验证 JSON 文档，确保工具输入输出符合预期格式。跨会话记忆允许 AI 记住之前对话的信息，从而实现更个性化和上下文感知的交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://json-schema.org/overview/what-is-jsonschema">JSON Schema - What is JSON Schema ?</a></li>
<li><a href="https://auto-post.io/blog/agents-evolve-with-cross-session-memory">Cross - Session Memory : How AI Agents Evolve</a></li>
<li><a href="https://www.promptlayer.com/glossary/system-prompt/">What is a System prompt? | PromptLayer</a></li>

</ul>
</details>

**标签**: `#Claude Opus 5`, `#system prompt`, `#AI developer tools`, `#leak`, `#AI agents`

---

<a id="item-4"></a>
## [AI 代币灰色市场转售经济内幕](https://vectoral.com/blog/token-relay-market) ⭐️ 7.0/10

一项详细调查揭示了一个蓬勃发展的灰色市场转售经济，转售商通过利用被盗的 API 密钥、计费系统滥用和欺诈手段，以官方价格 94-98%的折扣提供前沿 AI 模型的访问权限。 这种欺诈手段威胁着 OpenAI 和 Anthropic 等 AI 公司的收入模式，可能迫使它们取消免费试用并加强安全措施。同时，它也凸显了如何通过非官方渠道规避中国等地区的访问限制。 转售市场通过一个四层供应链运作，涉及虚拟卡商户、账户池、退款套利和代理渠道。这些平台运营联盟计划和客户支持，看起来像合法的 SaaS 企业。

hackernews · mlenhard · 7月26日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49058993)

**核验**: 多源印证

**背景**: AI 代币转售服务是代理主要 AI 提供商的 API 请求的灰色市场平台，主要服务于无法直接访问的中国大陆用户。转售商汇集被盗或欺诈获取的 API 密钥，并以大幅折扣转售访问权限。该生态系统已变得相当复杂，一些平台提供结构化的 B2B 级访问和每日赠品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vectoral.com/blog/token-relay-market">An Inside Look at the Relay Market Powering Token Resellers and Fraud</a></li>
<li><a href="https://daily.dev/posts/an-inside-look-at-the-relay-market-powering-token-resellers-and-fraud-njahgl92o">An Inside Look at the Relay Market Powering Token...</a></li>
<li><a href="https://fortune.com/2026/05/07/stripe/">Stripe CEO says a wave of token theft is wreaking havoc on the AI economy</a></li>

</ul>
</details>

**社区讨论**: 评论者将其与早期的广告欺诈市场和云信用滥用相提并论，指出同样的套利动态已存在数十年。一些人分享了竞争对手通过折扣代币获得不公平优势的个人经历，而另一些人则讨论了为代理代币制定无懈可击的订阅合同的难度。

**标签**: `#AI tokens`, `#fraud`, `#relay market`, `#API abuse`, `#cloud credits`

---

<a id="item-5"></a>
## [调查揭露 LLM 代币转售市场](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 7.0/10

Matt Lenhard 的调查揭露了一个市场，通过代理服务滥用免费试用、未受保护的支持机器人和被盗凭证，以折扣价转售 LLM 代币。 这项调查揭示了一个利用 LLM API 漏洞的繁荣地下经济，给开发者和供应商带来重大的安全和财务风险，他们可能面临意外成本和数据泄露。 转售者使用开源 API 代理工具（如 one-api 和 new-api）在汇集凭证之间负载均衡请求，而买家包括寻求廉价代币、绕过地理限制以及进行模型蒸馏的用户。

rss · Simon Willison · 7月26日 19:30

**核验**: 多源印证

**背景**: one-api 和 new-api 是开源项目，为各种 LLM 提供商提供统一的 API 网关，允许用户高效管理多个 API 密钥和路由请求。虽然设计用于合法用途，但它们可能被转售者利用，从免费试用、被盗密钥或退款中汇集凭证。调查表明，这个转售市场主要活跃在中国，买家通过这些代理访问折扣代币。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/songquanpeng/one-api">GitHub - songquanpeng/one-api: LLM API 管理 & 分发系统，支持 Open... API统一管控平台：new-api、one-api、Grok2API、Quotio、UniAPI、MetA... new-api: 基于oneapi二次开发 - Gitee New API - The Foundation of Your AI Universe One-API vs New-API：2026年开源LLM网关怎么选？部署踩坑 + 商业方案... One API vs New API (2026):开源 Token 中转站对比 | 支流科技</a></li>
<li><a href="https://blog.csdn.net/lonelymanontheway/article/details/158704894">API统一管控平台：new-api、one-api、Grok2API、Quotio、UniAPI、MetA...</a></li>

</ul>
</details>

**标签**: `#AI API`, `#token reselling`, `#fraud`, `#open source proxy`, `#LLM ecosystem`

---

<a id="item-6"></a>
## [双向语音交互漏洞已修复](https://x.com/thsottiaux/status/2081254182502465981) ⭐️ 7.0/10

开发者 Thibault Sottiaux 宣布，已修复计算机无法响应语音输入的漏洞，从而实现了与计算机的双向语音通信。 这一更新对 AI 代理和开发者工具意义重大，因为它通过语音实现了更自然的人机交互。它可能带来更直观的界面和多种应用中的免提操作。 该公告缺乏关于实现方式或相关产品的具体技术细节。推文中包含一个链接指向更多信息，但公告本身未提供细节。

follow_builders · Thibault Sottiaux · 7月26日 05:43

**核验**: 已核对原文

**背景**: 传统上，与计算机的语音交互是单向的：用户可以发出命令，但计算机不会进行对话。近年来 AI 的进步，特别是大型语言模型，使双向语音交互成为可能，让计算机能够理解上下文并自然回应。此次漏洞修复很可能利用了这些 AI 能力，以实现更具对话性的界面。

**标签**: `#AI agents`, `#voice interaction`, `#product launch`, `#developer tools`, `#human-computer interaction`

---

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多追踪内容</h2>
<p class="archive-intro">以下内容已于今日成功抓取，但未进入上方主列表。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-tracked-x" aria-controls="archive-panel-tracked-x" aria-selected="true" tabindex="0" data-archive-tab="tracked-x" data-count="0"><span>其他追踪推文</span><span class="archive-tab-count">0</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="11"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">11</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-tracked-x" aria-labelledby="archive-tab-tracked-x" data-archive-panel="tracked-x">
<h3 class="archive-panel-title">其他追踪推文</h3>
<p class="archive-empty">今天该来源没有其他未入选内容。</p>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2081267611132641787">Nikunj Kothari: em dash lover &amp;amp; savior can’t explain how to successfully type an em dash on their keyboar...</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari: 破折号爱好者和救星却记不住如何不查资料就打出破折号</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 7月26日 06:37 UTC · 喜欢 1 · 转发 0 · 回复 1</p>
<p class="archive-item-content">A tweet noting that em dash enthusiasts often forget how to type the symbol.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文指出，热爱破折号的人常常忘记如何打出这个符号。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2081234705287086195">Garry Tan: PS This is a shitpost</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Garry Tan: 附注：这是一个垃圾帖子</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 7月26日 04:26 UTC · 喜欢 35 · 转发 0 · 回复 9</p>
<p class="archive-item-content">A shitpost from Garry Tan with no substantive content.</p>
<p class="archive-item-translation"><span>中文摘要</span>来自 Garry Tan 的一个无实质内容的垃圾帖子。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2081229262452097169">Thibault Sottiaux: Game changer when used from mobile. Available in the ChatGPT app already. https://t.co/egAqFV...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：在手机上使用时是游戏规则改变者。已在 ChatGPT 应用中可用。</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月26日 04:04 UTC · 喜欢 901 · 转发 27 · 回复 112</p>
<p class="archive-item-content">A tweet claiming a game-changing feature for mobile use in the ChatGPT app, but lacking technical details.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文声称 ChatGPT 应用在手机上使用时具有颠覆性功能，但缺乏技术细节。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2081223709755650054">Zara Zhang: AI-native companies have a culture akin to an open-source community</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang: AI 原生公司的文化类似于开源社区</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 7月26日 03:42 UTC · 喜欢 31 · 转发 2 · 回复 14</p>
<p class="archive-item-content">Zara Zhang observes that AI-native companies share a culture similar to open-source communities.</p>
<p class="archive-item-translation"><span>中文摘要</span>Zara Zhang 观察到，AI 原生公司的文化与开源社区相似。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2081223316547977529">Garry Tan: My dad was cheering real loud from the stands Dad stop you’re embarrassing me https://t.co/4K...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Garry Tan: 我爸爸在看台上大声欢呼，爸爸别这样，你让我难为情了</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 7月26日 03:41 UTC · 喜欢 562 · 转发 8 · 回复 38</p>
<p class="archive-item-content">Garry Tan tweets about his dad cheering loudly at a sports event, causing embarrassment.</p>
<p class="archive-item-translation"><span>中文摘要</span>Garry Tan 发推文说他的爸爸在体育赛事中大声欢呼，让他感到尴尬。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/garrytan/status/2081222788090830946">Garry Tan: We should prioritize people and a vibrant community and more housing far far far more than so...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.0 out of 10">1.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Garry Tan: 我们应该优先考虑人、充满活力的社区和更多的住房，远远超过某个人的观点</p>
<p class="source-line">Follow Builders · X 动态 · Garry Tan · 7月26日 03:39 UTC · 喜欢 184 · 转发 5 · 回复 19</p>
<p class="archive-item-content">Garry Tan argues for prioritizing people, community, and housing over individual opinions.</p>
<p class="archive-item-translation"><span>中文摘要</span>Garry Tan 认为，相比于个人的观点，我们更应该优先考虑人、社区和住房。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/amasad/status/2081210562881716339">Amjad Masad: tfw when last nights edible finally kicks in https://t.co/k8QkUUo7go</a></h3>
<span class="score-badge" data-tier="low" aria-label="0.0 out of 10">0.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Amjad Masad: 昨晚的食用品终于生效时的感觉</p>
<p class="source-line">Follow Builders · X 动态 · Amjad Masad · 7月26日 02:50 UTC · 喜欢 84 · 转发 1 · 回复 10</p>
<p class="archive-item-content">Amjad Masad tweets about an edible kicking in, with no substantive content.</p>
<p class="archive-item-translation"><span>中文摘要</span>Amjad Masad 发推文说昨晚的食用品终于起效了，内容无实质信息。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/zarazhangrui/status/2081200367480738098">Zara Zhang: What do you do when you’re waiting for AI output? https://t.co/74RH0Od3nR</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Zara Zhang: 当你在等待 AI 输出时，你会做什么？</p>
<p class="source-line">Follow Builders · X 动态 · Zara Zhang · 7月26日 02:10 UTC · 喜欢 42 · 转发 1 · 回复 54</p>
<p class="archive-item-content">A tweet posing a question about how developers spend their time while waiting for AI model outputs, sparking discussion on workflow optimization.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文提出了一个问题：开发者在等待 AI 模型输出时如何利用时间，引发了关于工作流优化的讨论。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2081198608293187635">Thibault Sottiaux: ChatGPT Work officially has overtaken Codex in number of active users. Way to go.</a></h3>
<span class="score-badge" data-tier="mid" aria-label="6.0 out of 10">6.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：ChatGPT Work 在活跃用户数上正式超越 Codex。干得漂亮。</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 7月26日 02:03 UTC · 喜欢 3485 · 转发 85 · 回复 453</p>
<p class="archive-item-content">ChatGPT Work has surpassed Codex in active users, indicating a shift in AI coding tool adoption.</p>
<p class="archive-item-translation"><span>中文摘要</span>ChatGPT Work 在活跃用户数量上已超过 Codex，标志着 AI 编码工具偏好的转变。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2081195994499133820">Nan Yu: The real reason we don’t have a true SoftwareFactory https://t.co/ZTH4DZJtzm</a></h3>
<span class="score-badge" data-tier="low" aria-label="3.0 out of 10">3.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nan Yu: 我们没有一个真正的软件工厂的真正原因</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 7月26日 01:52 UTC · 喜欢 11 · 转发 0 · 回复 1</p>
<p class="archive-item-content">Nan Yu tweets about the real reason we don&#x27;t have a true SoftwareFactory, linking to an article.</p>
<p class="archive-item-translation"><span>中文摘要</span>Nan Yu 发推文讨论我们没有一个真正的软件工厂的真正原因，并附上了一篇文章链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thenanyu/status/2081187979024797858">Nan Yu: If you can make a SoftwareFactory, then you can make a SoftwareFactoryFactory</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.0 out of 10">2.0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>如果你能制造一个软件工厂，那么你就能制造一个软件工厂工厂</p>
<p class="source-line">Follow Builders · X 动态 · Nan Yu · 7月26日 01:20 UTC · 喜欢 10 · 转发 0 · 回复 4</p>
<p class="archive-item-content">A tweet stating that if you can build a SoftwareFactory, you can build a SoftwareFactoryFactory, implying a recursive or meta-approach to software creation.</p>
<p class="archive-item-translation"><span>中文摘要</span>一条推文指出，如果你能构建一个软件工厂，那么你就能构建一个软件工厂工厂，暗示了软件创建的递归或元方法。</p>
</article>
</div>
</section>
