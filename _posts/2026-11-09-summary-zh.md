---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> 从 20 条内容中筛选出 0 条重要资讯。

今天没有足够合适的精选选题，可在下方全部资讯中自行挑选。

<hr class="archive-divider">
<section class="archive-tabs" data-archive-tabs>
<h2>更多资讯，供你自行挑选</h2>
<p class="archive-intro">以下内容已成功抓取，因评分、数量限制或同题合并未进入精选。AI 判断仅供参考，你可以继续阅读并自行挑选；各来源切换是全部列表的子集。</p>
<div class="archive-tablist" role="tablist" aria-label="更多追踪内容来源" hidden>
<button type="button" role="tab" id="archive-tab-all" aria-controls="archive-panel-all" aria-selected="true" tabindex="0" data-archive-tab="all" data-count="20"><span>全部未入选</span><span class="archive-tab-count">20</span></button>
<button type="button" role="tab" id="archive-tab-follow-builders" aria-controls="archive-panel-follow-builders" aria-selected="false" tabindex="-1" data-archive-tab="follow-builders" data-count="8"><span>其他 Follow Builders 资讯</span><span class="archive-tab-count">8</span></button>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-all" aria-labelledby="archive-tab-all" data-archive-panel="all">
<h3 class="archive-panel-title">全部未入选</h3>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/">parse_number() 作为 SQLite 扩展：C 与 Rust 实现对比</a></h3><span class="score-badge" data-tier="low">2.2</span></div>
<p class="archive-original-title">parse_number() as a SQLite extension: C vs Rust</p><p class="source-line">Simon Willison · 11-08 22:26 UTC</p>
<p class="archive-item-content">文章对比了用 C 和 Rust 为 SQLite 编写 parse_number() 扩展的实现方式。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：这是面向开发者的 SQLite 扩展编程对比，普通用户难以直接使用，标题层面也不涉及 AI 消费级功能。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>Research:<br>parse_number() as a SQLite extension: C vs Rust<br>I was out walking the dog when I got curious about how easy/difficult it would be to write a SQLite C extension that adds a<br>parse_number()<br>function for turning strings like<br>-$1,234.56<br>or<br>&#x27;12.5%&#x27;<br>into numeric values that could be summed and sorted.<br>I fired up regular Claude chat (Opus 5.5)<br>and prompted<br>:<br>I&#x27;m thinking about a SQLite custom function &#x27;parse_number(value)&#x27; that strips &#x27;,&#x27;, &#x27;$&#x27;, &#x27;£&#x27; and &#x27;%&#x27;, handles a leading &#x27;-&#x27;, and returns &#x27;NULL&#x27; for anything it can’t parse<br>Explore the difference between building this as a SQLite extension in C v.s. in Rust - I want to compare performance and code complexity and size of the resulting<br>.so<br>(or whatever) file<br>This gave me a solid starting point - the Rust extension was 321 KB (using<br>Rusqlite<br>) and 298 KB (using<br>sqlite-loadable-rs<br>), while the C extension was 14 KB. But the Rust extension was faster!<br>Turns out that&#x27;s because the Rust equivalent of C&#x27;s<br>strtod<br>is &quot;twice as fast&quot;. So I prompted:<br>Try writing your own C function for parsing text into a decimal number that catches up to or beats the Rust implementation<br>And it did:<br>Net cost per row over 2 million rows, lower is better:<br>first C<br>new C<br>rusqlite<br>sqlite-loadable<br>Mixed data<br>67 ns<br>19 ns<br>46 ns<br>41 ns<br>Integers only<br>25 ns<br>16 ns<br>36 ns<br>32 ns<br>Decimals only<br>106 ns<br>18 ns<br>55 ns<br>47 ns<br>Finally, I had it rewrite the prototype as a research report to match the others in<br>simonw/research<br>by prompting this:<br>Clone simonw/research from GitHub and turn your above investigation into a research report as seen in that repository - you can give me a zip file to download that contains your new folder<br>Here&#x27;s<br>the resulting report<br>.<br>Tags:<br>c<br>,<br>research<br>,<br>sqlite<br>,<br>rust<br>,<br>claude</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors">英伟达董事会正在调查黄仁勋</a></h3><span class="score-badge" data-tier="low">3.7</span></div>
<p class="archive-original-title">Nvidia Board of Directors Is Investigating Jensen Huang</p><p class="source-line">vincentchau · 11-08 20:26 UTC</p>
<p class="archive-item-content">英伟达董事会发布声明称正在调查CEO黄仁勋，但标题未说明具体事由。</p>
<p class="archive-assessment">AI 判断：这是公司治理层面的突发消息，与普通人使用AI无直接关系，且来源信息有限，难以做成实用教程或可靠解读。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[nrmitchi]: The title on this is just extremely misleading. Nvidia is doing an investigation of Jensen Huang  being targeted in an intelligence operation ; ie, an investigation of something  that happened to him . The title implies that Jensen Huang is the target of Nvidia&#x27;s investigation.<br><br>[enlyth]: Also reported by Bloomberg: &quot;Nvidia Board to Probe Spying Case After CEO Admits Infidelity&quot;  https://www.bloomberg.com/news/articles/2026-11-08/nvidia-bo...   https://archive.is/VfRdl<br><br>[aigalaxiome]: China targets everyone of consequence, of course they targeted Jensen.<br>This may be a &#x27;game of thrones&#x27; nefarious move by hostile foreign or domestic parties who want to wrest defacto control, perhaps angle to put their puppet in control, or otherwise leverage Nvidia by taking down its Founder and CEO.<br>It is completely unproven and should not be assumed that Jensen nor Nvidia took part in anything untoward at all. Historically, Jensen doesn&#x27;t do stupid. So whether you like him o...<br><br>[zugi]: There&#x27;s no explanation of whether he got sextorted, or what the plan was to get sensitive information from him. Or was the plan just to publicly humiliate him in hopes he&#x27;d get replaced by someone less capable?<br><br>[baxtr]: They say any man can be seduced by one of these three: money, drugs or sex. Or as Charlie Munger put it:  There are only three ways a smart person can go broke: Liquor, ladies, and leverage.“</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://sergeykuhne.com/blog/fighting-ai-brain-fry">我是如何对抗“AI 烧脑”的</a></h3><span class="score-badge" data-tier="low">4.6</span></div>
<p class="archive-original-title">How I Fight AI Brain Fry</p><p class="source-line">kyunez · 11-08 19:37 UTC</p>
<p class="archive-item-content">作者分享自己在高强度使用 AI 后应对注意力涣散和思维疲劳的个人方法。</p>
<p class="archive-assessment">AI 判断：这属于个人经验分享；其中缺少可核实的操作步骤、具体工具和直观演示，对普通观众的实用性有限。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[eterm]: I&#x27;ve learned that rather than juggle too much, I just accept that I&#x27;m still more productive than ever before, even if I&#x27;m &quot;idle&quot;, it&#x27;s important to take time to have a break and to recharge, refresh and reflect. So I limit myself to at most 2 or 3 things at once, and if all of those are in long running sessions, well so be it, I know I&#x27;ll be deep back in it soon. But it&#x27;s tempting to start &quot;just one more session&quot;, especially something like get...<br><br>[sollewitt]: This only solves part of the problem, the other half is: ok so you have 3 chats going, at some point you realize you have 3 &gt;10k line CLs to review, on top of code your colleagues are asking you to review. Every review I’ve ever done I’ve found overfitting and brittle solutions and things tacked on instead of integrated so I refuse to give up on code reviews, but those are my real bottleneck, and having three is so much worse than one because my context and understanding is diluted and a b...<br><br>[docheinestages]: Why start several threads in parallel to begin with? If waiting is an issue, maybe you should break that one task into multiple steps. That would only produce more output at a lower quality. Nothing has changed about the human thinking capacity. Focus on one thing and get it done.<br><br>[hetspookjee]: I’ve tried this kind of format too but it didn’t stick for me as i  was missing the rich context the sessions were able to provide for me. Specifically the lack of diagrams and other nice formatting that is possible in HTML files. I  also tried linear as a broker in between for a while but it just blew up and became too tedious to navigate and ran out of sync fast. Also expensive on token overhead. Currently what I task it to do is have one or multiple agent threads tied to a project work it ...<br><br>[silcoon]: I think the problem is context switching. &quot;I can work on three different tasks at once thanks to AI&quot; seems really empowering, but in reality, it&#x27;s impossible to focus deeply on one task if your thought process is constantly interrupted every few minutes. Every time I find myself idling in front of a screen, I feel the need to find something else to do, a distraction to fill those 54s before the agent sends a notification that needs my attention. This isn&#x27;t healthy, and it&amp;...</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://mailroute.net/blog/outlook-rejecting-email-without-dmarc">Outlook.com Is Quietly Rejecting Email from Domains Without DMARC</a></h3><span class="score-badge" data-tier="low">0</span></div>
<p class="source-line">xmddmx · 11-08 19:20 UTC</p>
<p class="archive-item-content">Outlook.com Is Quietly Rejecting Email from Domains Without DMARC</p>
<p class="archive-assessment">AI 判断：前置规则过滤：HN 标题及已抓取内容未命中 AI 主题</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[Neikius]: Outlook.com is also rejecting mail based on blocklists that are not public and you essentialy cannot get yourself out. My VPS provider is pretty much entirely blocked and their regular blocklist process says we are golden so nothing to unblock. Outlook.com and similar are an anathema to email. This is why they tell you not to run a mail server . On the other hand rejecting domains without dmarc is fine. Just not happy it is silent.<br><br>[codethief]: Outlook.com has quietly dropped[0] emails from certain domains/IPs for years, even with SPF/DKIM/DMARC all properly set up and no history of spam. As someone who&#x27;s administering their own mail server, Outlook has been the bane of my existence. [0]: As in: They accepted the email just fine (according to the logs) but it still didn&#x27;t end up in the recipient&#x27;s mailbox.<br><br>[stephbook]: Sounds like something every mail sender should have done already. Good for Microsoft customers and I don&#x27;t care one bit for the lazy people who have to late-patch now.<br><br>[dwm]: They&#x27;re not rejecting them quietly.  They&#x27;re sending 5xx permanent delivery failures.<br><br>[klodolph]: I set up DMARC on my personal domain so long ago I can&#x27;t even remember when I did it. 10 years+? I had kinda assumed that a lot of providers would start rejecting domains without DMARC support. I&#x27;m surprised it&#x27;s happening this late.</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://duxlabs.dev/">Dux: Free, open-source Wayland desktop shell with file manager and theming</a></h3><span class="score-badge" data-tier="low">0</span></div>
<p class="source-line">indigodaddy · 11-08 19:08 UTC</p>
<p class="archive-item-content">Dux: Free, open-source Wayland desktop shell with file manager and theming</p>
<p class="archive-assessment">AI 判断：前置规则过滤：HN 标题及已抓取内容未命中 AI 主题</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[shortformblog]: Been using this for close to a year (wrote about it here when it was still called Dank Material Shell:  https://tedium.co/2026/01/29/niri-danklinux-scrolling-window... ); it is endlessly slick, and I think good enough to help mainstream Niri. It also just added official support for atomic distros like Bazzite; it was previously kind of an annoying gap given the popularity of those distros.<br><br>[jeffnash]: I was confused for a second, but turns out DMS rebranded the &#x27;Dank&#x27; to &#x27;Dux&#x27; a few weeks ago [1]. I&#x27;ve been running DMS + Niri for nearly a year now with no intentions of switching anytime soon. Given how often I&#x27;ve historically changed shells/DEs, this is the ricing equivalent to settling down, getting married, and having kids. [1]  https://duxlabs.dev/blog/v2-0-release<br><br>[nylonstrung]: DMS is extremely solid but at this point is becoming more all-encompassing than I honestly want I&#x27;ve been wanting to try Noctalia with this River-based multi-paradigm compositor (which supports DMS)  https://github.com/greenm01/triad<br><br>[darkwi11ow]: https://wiki.xfce.org/releng/wayland_roadmap <br>My most anticipated development roadmap these days.<br><br>[mariocesar]: I use it daily. There was a learning curve since I was used to GNOME Shell, but Niri and the ability to build my own widgets with QML ended up being the killer features for me. I&#x27;ve built several custom widgets and small apps, and I&#x27;m happy with my workflow</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers">高盛正撤回其银行家和交易员使用的 Claude Code</a></h3><span class="score-badge" data-tier="low">3.85</span></div>
<p class="archive-original-title">Goldman Sachs is pulling Claude Code from its bankers and traders</p><p class="source-line">TheWiggles · 11-08 18:16 UTC</p>
<p class="archive-item-content">据报道，高盛正在停止让内部银行家和交易员使用 Claude Code，这一企业级调整引发外界对金融机构 AI 落地的关注。</p>
<p class="archive-assessment">AI 判断：这是企业内部工具调整的消息，普通人难以亲自使用或复现，实用价值和画面感有限，更适合作为行业观察而非教程选题。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[lukebuehler]: People are giving all kinds of explanations here why Goldman is doing this, but they are not addressing what the article (implicitly) says: operating coding agents on the primary machines of finance professionals runs directly into the lethal trifecta. It&#x27;s as simple as that. You cannot have semi-unattended agents running on the same workstations that have access to client/trade/prop information and email client, and internet, and internal networks, it&#x27;s too dangerous--a m...<br><br>[legitster]: At our org they have been clawing back Claude access because of chronic billing overages. Budgets are tight and consumption billing models are being stamped down on everywhere. Anthropic sales can not offer us any sort of normalized billing rate. Gemini is swooping in because they offer flat consistent billing and handle overages through throttling access to higher models. For 90% of the non-engineering org the experience is near enough it makes no difference.<br><br>[steveBK123]: Regardless of tech tool, non-tech writing POCs they try to force tech to get into production is a timeless story.  LLM just allows people to get there faster, with less knowledge of coding.. which leads to the actual problem I think. Banks have a ton of legal/compliance/reglatory/reputational concerns about application access/entitleements, data privacy, data licensing, granular data entitlements, data access (auditable).. approval chains (auditable), as well as actual fin...<br><br>[cactca]: The most interesting part of this announcement is the timing. GS is leading Anthropic&#x27;s IPO, what motivated them to announce this a few weeks before trading starts?<br><br>[fancyfredbot]: Goldman is very unlikely to have decided proactively to cut off traders access, and it&#x27;s much more likely there was an operational loss. What kind of loss? I don&#x27;t know but consider: 1) Claude Code is only being taken away from traders. 2) Only traders have permission to send orders to the market and book client trades. 3) Claude code would probably have been running as the trader, under their account with minimal review. If you run a coding agent in that environment it&#x27;s only ...</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="http://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html">写作作为思考工具</a></h3><span class="score-badge" data-tier="low">3.8</span></div>
<p class="archive-original-title">Writing as a thinking tool</p><p class="source-line">jruohonen · 11-08 10:41 UTC</p>
<p class="archive-item-content">一篇博客文章讨论写作如何作为思考工具，帮助人理清思路并深化理解。</p>
<p class="archive-assessment">AI 判断：这是关于写作与思维方法的个人随笔，没有可演示的 AI 新功能、价格或使用限制，对普通人的直接实用价值有限。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[billypilgrim]: When I had started my PhD, I thought the writing part of a paper was just the last thing I needed to do to summarize my results, like a boring epilogue to the more exciting science. What surprised me was how much of the scientific process relied on my ability to convey my ideas to someone else. And to be able to do that you need clarity of mind, you need to have worked through multiple drafts to be able to get to your point as efficiently and clearly as possible. So many times I only discover...<br><br>[GarnetFloride]: I have seen the same thing happen in multiple domains. You may have identified a problem to solve, but the act of solving it, by writing it down, by writing a program, building a tool, making a device, or even carving from stone. As you work on it the problem becomes more clear and seems to tell you what the actual shape of the problem is and you have to adapt your solution to that actual problem, even if it ignores certain aspects of the original idea. Writing it down and trying to clarify i...<br><br>[drewbeck]: This is true for designing, too. I see a lot of people saying Figma is dead because you can prototype directly; for novel UX problems the act of designing — of putting ideas together, assembling a component, even getting good data into a design — is where a lot of my thinking and insights develop. The brain work plus the craft work, the tight loop between thinking and creating is so critical for me and I haven’t found nearly the same feeling when prompting. In writing and designing I think we...<br><br>[lilerjee]: Writing code (Programming) is a thinking tool too. When you are writing code manually, actually you are thinking about what you are doing, what you will build actually, what are your or users&#x27; real requirements, etc.<br><br>[hoppp]: Most of my projects are born out of scribbles on paper, system diagrams with boxes and little arrows to try to describe the system I want to build or my thought process written down like in this post. When I get it on paper and everything feels right I start creating the codebase but I have to get it down first, feels like I remember it more after I save my thoughts to external paper storage.</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://github.com/synchopate/llama-modchip">Llama-modchip：在64GB内存、无GPU的机器上运行284B参数的DeepSeek</a></h3><span class="score-badge" data-tier="low">3.15</span></div>
<p class="archive-original-title">Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU</p><p class="source-line">joshcsimmons · 11-08 10:22 UTC</p>
<p class="archive-item-content">一个GitHub项目演示如何在仅64GB内存、不使用GPU的情况下运行284B参数的DeepSeek大模型。</p>
<p class="archive-assessment">AI 判断：这属于底层推理与部署技巧，普通用户难以复现，实用性和受众相关性都低。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[kennywinker]: The floor for a functional local AI system keeps getting lower, dispite ram and GPU prices continuing to go up. An E5 workstation with lots of threads, $300 of RAM and at least $100 of GPU gets you something that can do &gt;100tok/s+ prompt processing, and ~20tok/s output with Qwen3.8-flash-next:IQ3_S. Toss a $500 GPU in there, and it goes from barely usable to pleasingly performant. For less than $800 you have something that holds its own with where the SOTA was less than a year ag...<br><br>[armcat]: Something to keep in mind with aggressive quantisation, is that it&#x27;s been empirically proven [1] that (1) quantisation has non-linear performance behaviour, and (2) generally the peak size-to-performance ratio occurs at 4-bit; anything lower and you will see significant reduction in performance. Also, I&#x27;ve been playing with speech models for the past 2 years, and for me anything below 8-bit is a huge drop in quality; so quantisation for LLMs and for other bespoke modality models, is...<br><br>[antirez]: To put this on perspective, consider that with 128GB of unified RAM it can run even  fast :  https://x.com/antirez/status/2119392658661749175 <br>Like, coding-agent acceptably fast. See later in the reply for the prefill at ~300 t/s but can go even faster for larger prefills.<br><br>[aappleby]: Stupid question, but does this AI-generated repo actually _do_ anything? Comparing it on Nemotron, it runs just about the same as plain old llama.cpp on the cpu (except prefill seems much faster). I don&#x27;t see an option to set up DeepSeek in &quot;modchip setup&quot;, so I haven&#x27;t tested that one yet. Edit: this is on a Ryzen 7945hx 16-core Zen 4 + 96 gb DDR5.<br><br>[boredatoms]: The quantization is probably the  most  important thing to know and its not clear at all from the dense word salad</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://www.lorekit.io/blog/open-agent-memory-format">智能体记忆需要一个 OpenTelemetry 时刻</a></h3><span class="score-badge" data-tier="low">1.95</span></div>
<p class="archive-original-title">Agent memory needs its OpenTelemetry moment</p><p class="source-line">mthines · 11-08 08:40 UTC</p>
<p class="archive-item-content">Lorekit 提出为智能体记忆制定统一开放格式，借鉴 OpenTelemetry 的标准化思路，让不同 AI 智能体的记忆数据可以互通。</p>
<p class="archive-assessment">AI 判断：这是面向开发者的记忆格式标准倡议，普通用户难以直接使用或感知，属于技术类选题。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[armchairhacker]: Is this a significant problem? It seems like there are 15 solutions to every AI “text format” problem, but all are merely structure over feeding the AI informal English, structure which I believe the “transformer” model is specifically able to strip to a common form (which is how training it on the entire internet worked). AI does benefit from learning to use skills, and being instructed with  good  structures (like “save [specific important kind of detail] in memories” and “plan before imple...<br><br>[speedping]: Entire blog post reeks of LLM. <br>If there was an adequately reliable way of detecting LLM text i&#x27;d build a browser extension that would just filter it out altogether.<br><br>[Fordec]: On the general premise, I agree. But I don&#x27;t think that moment is today, not yet anyway. I don&#x27;t think we understand the right way to approach context and memory yet or how long they should last for, never mind standardizing on an abstraction prematurely that ends up being like SOAP or SGML.<br><br>[lmeyerov]: Premature optimization imo I&#x27;m happy with the otel LLM extensions, and would rather this to be a meta protocol vs actual protocol/standard: 1. Harness memory rapidly evolves approach across the full stack, from data storage &amp; rep to overall concept. Arguably we are in an early primitive era because text is being used instead of semantic vectors etc. 2. Even something as basic like a knowledge graph has a wide diversity of approaches. 3. Similar to REST APIs, what I would argue f...<br><br>[baalimago]: Do we really need this..? What LLMs do well is interpret natural language. So it&#x27;s a sponge for whatever format is used in a specific project: a predefined format is not really needed. Besides, do we really want memory of user A&#x27;s agents to co-exist with memory of user B? Not really. So the argument for collaboration and sharing is quite slim, at least for coding agents. The repository specific context can be encoded into a docs/ or architecture/ directory, just like it&amp;#x...</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://x.com/thsottiaux/status/2119305294291612140">Thibault Sottiaux：推出 Pro 50 会有意义吗？大家怎么看？https://t.co/WZi6KGXFc9</a></h3><span class="score-badge" data-tier="low">2.65</span></div>
<p class="archive-original-title">Thibault Sottiaux: Would a Pro 50 make sense? Wdyt? https://t.co/WZi6KGXFc9</p><p class="source-line">Thibault Sottiaux · 11-08 05:45 UTC</p>
<p class="archive-item-content">Thibault Sottiaux 发推询问是否值得推出 Pro 50 方案，征求大家的意见。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：这仅是标题层面的开放式征求意见，缺少具体功能、价格与演示信息，普通人无法据此实际使用或判断。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>Would a Pro 50 make sense? Wdyt? https://t.co/WZi6KGXFc9</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://x.com/thsottiaux/status/2119296267545419987">Thibault Sottiaux：看到一些误解，但所有 Pro 套餐都没有 5 小时限制，并提供以下用量……</a></h3><span class="score-badge" data-tier="mid">5.6</span></div>
<p class="archive-original-title">Thibault Sottiaux: Saw some confusions, but all Pro plans have no 5-hour limits, and give the following usage co...</p><p class="source-line">Thibault Sottiaux · 11-08 05:09 UTC</p>
<p class="archive-item-content">相关人士澄清所有 Pro 套餐均无 5 小时使用限制，并提及后续用量安排。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：标题仅是套餐规则澄清且内容不完整；普通人可直接受益，但缺少可演示的视觉素材和完整事实。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>Saw some confusions, but all Pro plans have no 5-hour limits, and give the following usage compared to Plus.<br><br>✅ Pro 100 = 10X<br>✅ Pro 200 = 20X<br>✅ Pro 500 = 50X, access to ultrafast</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://www.ifanr.com/1688364?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=">被年轻人遗忘的磁带，正在 AI 时代闷声发大财</a></h3><span class="score-badge" data-tier="low">4.5</span></div>
<p class="archive-original-title">被年轻人遗忘的磁带，正在 AI 时代闷声发大财 原</p><p class="source-line">爱范儿 · 11-08 03:35 UTC</p>
<p class="archive-item-content">一篇标题称磁带在 AI 时代重新获得商机的文章，但仅凭标题无法确认其具体 AI 用途与事实依据。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：标题有反差感，但只有标题、缺少可核实的 AI 用法或数据，暂不宜作为教程或实用选题。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>磁带在 AI 时代迎来了第二春。<br>#欢迎关注爱范儿官方微信公众号：爱范儿（微信号：ifanr），更多精彩内容第一时间为您奉上。</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://caleb.software/posts/claude-to-pi.html">告别 Claude，转向 Pi</a></h3><span class="score-badge" data-tier="low">4.45</span></div>
<p class="archive-original-title">Goodbye Claude, hello Pi</p><p class="source-line">karagenit · 11-08 03:11 UTC</p>
<p class="archive-item-content">一位开发者撰文讲述自己从 Claude 切换到 Pi 的使用体验与理由。</p>
<p class="archive-assessment">AI 判断：这是开发者的个人工具选择分享，普通用户可参考，但缺少可亲手演示的具体功能对比。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>--- Top Comments ---<br><br>[bottlepalm]: I used to use ChatGPT/Claude in the TUI up until like 3 months ago, but my usage of LLMs has exploded - many sessions across many projects. I feel like I outgrew the TUI and now I&#x27;m using ChatGPT/Claude desktop. VS Code has become a code review tool and place where I manage git if need be. The GUI is less verbose with the nitty gritty hidden in expandable sections, which makes history easier and cleaner to scroll through, also no scrolling bugs, rich text is easier to read with...<br><br>[leobuskin]: Pi is a good harness (I finally gave it a try w/ abliterated GLM), but not with Anthropic subscription, and there are multiple reasons to avoid alternative harnesses with their models in general (imho): 1. Potential ban due to ToS violation; 2. It doesn&#x27;t follow all Anthropic&#x27;s communication mechanisms out-of-the-box, they heavily use custom headers, hidden flags, and undocumented API features that affect models&#x27; behavior; 3. Compact is better in CC (significantly); 4. Cac...<br><br>[zmmmmm]: Comments seem filled with generic fandom for Pi or other harnesses / multiplexers. The actual post seems incoherent. They had a bunch of problems with Claude, most in features Pi does not even support in the first place. They don&#x27;t like &quot;instability&quot; aka rapid pace of development, ignoring Pi is just as if not more rapid. They passively assume an ecosystem of plugins is going to be more stable. I&#x27;m a big fan of Pi and believe everyone should use it or similar open har...<br><br>[real_faxenoff]: I became interested in how the harness works internally so I could try to implement my own small AI agent in a business project. And I realized that right now, most of the model’s efficiency lies precisely in the harness. And that there’s a whole complicated world inside it, one that will soon become more complex than the models themselves. All my experiments using third-party harnesses for code-writing agents showed that if a model is used in a non-native harness, it sometimes burns through ...<br><br>[gvkhna]: Pi is without contest the best harness. Because it’s yours, the total control is the only way to move from driving agents to orchestrating them. My interruptions and frustration with llms has gone down a cliff. It’s amazing to see what just a few lines of system prompt really can do to keep agents doing the correct thing much more often.</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://x.com/steipete/status/2119264334627090514">Peter Steinberger：Asahi 项目的核心就是把封闭受限的东西开放出来，并补充……</a></h3><span class="score-badge" data-tier="low">2.3</span></div>
<p class="archive-original-title">Peter Steinberger: The Asahi project was all about taking something closed and restricted and opening it up. Add...</p><p class="source-line">Peter Steinberger · 11-08 03:02 UTC</p>
<p class="archive-item-content">Peter Steinberger 在推文中表示，Asahi 项目的意义在于把原本封闭受限的东西开放出来，并对此做了补充说明。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：仅凭标题看，这是关于开源与封闭生态的个人观点，缺少普通人可直接使用的功能或可演示细节，判断依据仅为标题。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>The Asahi project was all about taking something closed and restricted and opening it up.<br><br>Adding new restrictions that make it harder for other projects to build on that is not the way. And that AI rejection is just silly. https://t.co/fT4O4wieQm</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://x.com/swyx/status/2119242830707311005">Swyx：受 @dexhorthy、@CompleteSkeptic 等人启发的贴纸游戏</a></h3><span class="score-badge" data-tier="low">2.3</span></div>
<p class="archive-original-title">Swyx: sticker game inspired by @dexhorthy @CompleteSkeptic et al https://t.co/NWvVRZ71uW https://t....</p><p class="source-line">Swyx · 11-08 01:37 UTC</p>
<p class="archive-item-content">Swyx 分享了一个受多位网友启发的贴纸游戏，并附上链接。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：标题信息有限，只提到贴纸游戏和灵感来源，缺少可核实的玩法与普通人的实际用途。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>sticker game inspired by @dexhorthy @CompleteSkeptic et al https://t.co/NWvVRZ71uW https://t.co/QHmHu3ZSFG</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://x.com/nikunj/status/2119229917019971879">Nikunj Kothari：下周三11月11日中午，下一位嘉宾是 @danielrupawalla，@ArcanumLabs_ 联合创始人……</a></h3><span class="score-badge" data-tier="low">1.9</span></div>
<p class="archive-original-title">Nikunj Kothari: Next guest up is @danielrupawalla, cofounder of @ArcanumLabs_ next Wednesday, Nov 11th at noo...</p><p class="source-line">Nikunj Kothari · 11-08 00:46 UTC</p>
<p class="archive-item-content">这是一则访谈预告：Nikunj Kothari 将于11月11日中午对话 Arcanum Labs 联合创始人 Daniel Rupawalla。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：标题仅为访谈预告，未提供可演示的AI功能或普通人可用信息，实用性与受众相关性均低。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>Next guest up is @danielrupawalla, cofounder of @ArcanumLabs_ next Wednesday, Nov 11th at noon. <br><br>For this session, we&#x27;ll be chatting about all things data (what the labs are buying, who is selling, how do i get into this business, will this market even last..)<br><br>Format:<br>&gt; 60 minute sessions (IRL only) in SF<br>&gt; For the first 45 mins, I get to ask the guest spicy questions about their expertise<br>&gt; For the last 15 mins, they get to ask me anything they want to learn about venture<br>&gt; All off the record, chatham house rules<br>&gt; Open to 10-12 guests who listen in and can ask some of their own questions<br><br>Register here if you want to join, and subscribe to the Luma for future guests: https://t.co/esETUKhcm7</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://simonwillison.net/2026/Nov/7/link-rel-next/">datasette #3046：不要向 Firefox 的 HTML 页面发送 link: rel=next HTTP 头</a></h3><span class="score-badge" data-tier="low">1.25</span></div>
<p class="archive-original-title">datasette #3046: Don&#x27;t serve link: rel=next HTTP headers to Firefox for HTML pages</p><p class="source-line">Simon Willison · 11-07 23:57 UTC</p>
<p class="archive-item-content">该条目记录 datasette 的一个修复：针对 HTML 页面，不再向 Firefox 发送 link: rel=next HTTP 头。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：这是开发工具的数据集项目补丁，仅涉及 HTTP 头兼容性，普通用户没有可用的教程或可视化演示。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>datasette #3046: Don&#x27;t serve link: rel=next HTTP headers to Firefox for HTML pages<br>I was looking at the Firefox network panel today when I noticed that requests to a Datasette table page were triggering an<br>HTTP prefetch<br>to the next page of rows in that table.<br>This was happening because Datasette pages serve an HTTP<br>link<br>header like this:<br>link: &lt;https://latest.datasette.io/fixtures/compound_three_primary_keys?_next=a%2Cd%2Cv&gt;; rel=&quot;next&quot;<br>This is bad. A tiny fraction of the visitors to one of those pages will click the &quot;next&quot; link, which means their browser is fetching unnecessary data and the Datasette server is having to render an entire page that then gets thrown away.<br>I dug in and learned that Firefox has<br>an issue<br>that has been open for 24 years about this behavior...<br>And one of the early comments on that issue links to<br>my blog post from 2002<br>complaining about this feature. I hadn&#x27;t just forgotten that I had written about it, I had forgotten the feature entirely!<br>Tags:<br>firefox<br>,<br>html<br>,<br>mozilla<br>,<br>datasette</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://x.com/amasad/status/2119217304953053419">Amjad Masad：更好的一课</a></h3><span class="score-badge" data-tier="low">2.05</span></div>
<p class="archive-original-title">Amjad Masad: The Better Lesson: https://t.co/662AivSigr</p><p class="source-line">Amjad Masad · 11-07 23:55 UTC</p>
<p class="archive-item-content">仅从标题看，Amjad Masad 分享了一条题为“更好的一课”的内容，具体所指尚未说明。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：标题过于抽象，缺少可核实的 AI 功能、教程或新闻信息，难以支撑面向普通人的实用选题。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>The Better Lesson: https://t.co/662AivSigr</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://x.com/swyx/status/2119210618976944259">Swyx：https://t.co/ydo8JgYDXr</a></h3><span class="score-badge" data-tier="low">0</span></div>
<p class="archive-original-title">Swyx: https://t.co/ydo8JgYDXr</p><p class="source-line">Swyx · 11-07 23:29 UTC</p>
<p class="archive-item-content">Swyx 发布了一条只含短链接的推文，标题未提供任何可核实的具体内容。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：仅凭标题只有一个短链接，无法判断主题、可用性或真实性，属于信息不足的预告式内容。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>https://t.co/ydo8JgYDXr</p></details>
</article>
<article class="archive-item candidate-item">
<div class="archive-item-heading"><h3><a href="https://x.com/swyx/status/2119210582654210255">Swyx：刚到场……业界最好的周边礼物玩法，你们下周有得期待了 https://t.c...</a></h3><span class="score-badge" data-tier="low">1.75</span></div>
<p class="archive-original-title">Swyx: just arrived… best swag game in the business. u guys are in for a treat next week https://t.c...</p><p class="source-line">Swyx · 11-07 23:29 UTC</p>
<p class="archive-item-content">Swyx 发推称刚抵达现场，并预告下周将带来业界最好的周边礼物玩法。</p>
<p class="archive-assessment">AI 判断：标题初筛（未依据正文）：标题只提到周边礼物和下周预告，没有具体 AI 功能或可用信息，属于信息不足的悬念式发文，难以做成实用选题。</p>
<details class="archive-original"><summary>展开原始摘录</summary><p>just arrived… best swag game in the business. u guys are in for a treat next week https://t.co/4tppCNnBWf https://t.co/uBruvPBba5</p></details>
</article>
</div>
<div class="archive-panel" role="tabpanel" id="archive-panel-follow-builders" aria-labelledby="archive-tab-follow-builders" data-archive-panel="follow-builders">
<h3 class="archive-panel-title">其他 Follow Builders 资讯</h3>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2119305294291612140">Thibault Sottiaux: Would a Pro 50 make sense? Wdyt? https://t.co/WZi6KGXFc9</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.65 out of 10">2.65</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：推出 Pro 50 会有意义吗？大家怎么看？https://t.co/WZi6KGXFc9</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 11月8日 05:45 UTC · 喜欢 1369 · 转发 58 · 回复 855</p>
<p class="archive-item-content">Thibault Sottiaux 发推询问是否值得推出 Pro 50 方案，征求大家的意见。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/thsottiaux/status/2119296267545419987">Thibault Sottiaux: Saw some confusions, but all Pro plans have no 5-hour limits, and give the following usage co...</a></h3>
<span class="score-badge" data-tier="mid" aria-label="5.6 out of 10">5.6</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Thibault Sottiaux：看到一些误解，但所有 Pro 套餐都没有 5 小时限制，并提供以下用量……</p>
<p class="source-line">Follow Builders · X 动态 · Thibault Sottiaux · 11月8日 05:09 UTC · 喜欢 2756 · 转发 86 · 回复 650</p>
<p class="archive-item-content">相关人士澄清所有 Pro 套餐均无 5 小时使用限制，并提及后续用量安排。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/steipete/status/2119264334627090514">Peter Steinberger: The Asahi project was all about taking something closed and restricted and opening it up. Add...</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.3 out of 10">2.3</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Peter Steinberger：Asahi 项目的核心就是把封闭受限的东西开放出来，并补充……</p>
<p class="source-line">Follow Builders · X 动态 · Peter Steinberger · 11月8日 03:02 UTC · 喜欢 1053 · 转发 44 · 回复 85</p>
<p class="archive-item-content">Peter Steinberger 在推文中表示，Asahi 项目的意义在于把原本封闭受限的东西开放出来，并对此做了补充说明。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2119242830707311005">Swyx: sticker game inspired by @dexhorthy @CompleteSkeptic et al https://t.co/NWvVRZ71uW https://t....</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.3 out of 10">2.3</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：受 @dexhorthy、@CompleteSkeptic 等人启发的贴纸游戏</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 11月8日 01:37 UTC · 喜欢 74 · 转发 0 · 回复 9</p>
<p class="archive-item-content">Swyx 分享了一个受多位网友启发的贴纸游戏，并附上链接。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/nikunj/status/2119229917019971879">Nikunj Kothari: Next guest up is @danielrupawalla, cofounder of @ArcanumLabs_ next Wednesday, Nov 11th at noo...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.9 out of 10">1.9</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Nikunj Kothari：下周三 11 月 11 日中午，下一位嘉宾是 @danielrupawalla，@ArcanumLabs_ 联合创始人……</p>
<p class="source-line">Follow Builders · X 动态 · Nikunj Kothari · 11月8日 00:46 UTC · 喜欢 13 · 转发 1 · 回复 3</p>
<p class="archive-item-content">这是一则访谈预告：Nikunj Kothari 将于 11 月 11 日中午对话 Arcanum Labs 联合创始人 Daniel Rupawalla。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/amasad/status/2119217304953053419">Amjad Masad: The Better Lesson: https://t.co/662AivSigr</a></h3>
<span class="score-badge" data-tier="low" aria-label="2.05 out of 10">2.05</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Amjad Masad：更好的一课</p>
<p class="source-line">Follow Builders · X 动态 · Amjad Masad · 11月7日 23:55 UTC · 喜欢 255 · 转发 12 · 回复 37</p>
<p class="archive-item-content">仅从标题看，Amjad Masad 分享了一条题为“更好的一课”的内容，具体所指尚未说明。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2119210618976944259">Swyx: https://t.co/ydo8JgYDXr</a></h3>
<span class="score-badge" data-tier="low" aria-label="0 out of 10">0</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：https://t.co/ydo8JgYDXr</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 11月7日 23:29 UTC · 喜欢 1 · 转发 0 · 回复 0</p>
<p class="archive-item-content">Swyx 发布了一条只含短链接的推文，标题未提供任何可核实的具体内容。</p>
</article>
<article class="archive-item">
<div class="archive-item-heading">
<h3><a href="https://x.com/swyx/status/2119210582654210255">Swyx: just arrived… best swag game in the business. u guys are in for a treat next week https://t.c...</a></h3>
<span class="score-badge" data-tier="low" aria-label="1.75 out of 10">1.75</span>
</div>
<p class="archive-item-translation archive-title-translation"><span>中文标题</span>Swyx：刚到场……业界最好的周边礼物玩法，你们下周有得期待了 https://t.c...</p>
<p class="source-line">Follow Builders · X 动态 · Swyx · 11月7日 23:29 UTC · 喜欢 92 · 转发 2 · 回复 18</p>
<p class="archive-item-content">Swyx 发推称刚抵达现场，并预告下周将带来业界最好的周边礼物玩法。</p>
</article>
</div>
</section>
