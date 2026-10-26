---
layout: default
title: 自媒体选题信息源与平台接入调研
---

# 自媒体选题信息源与平台接入调研

调研日期：2026-10-20。目标是及时发现 AI 趋势、实用玩法、视觉创意和适合个人观点解读的新闻。

## 已配置的 17 个新增来源

RSS：The Rundown AI、Ben's Bites、One Useful Thing、爱范儿、小众软件、Google 官方博客、ElevenLabs Blog、OpenAI News、少数派。

公开网页：AIBase 中文、Future Tools、Theoretically Media、ChatGPT Release Notes、Anthropic News、Runway News、Canva Newsroom、即梦官网功能监测。

每个新增 RSS 来源最多返回 8 条近期候选；综合媒体和 Google 博客先做 AI 主题关键词过滤。公开网页最多读取 6–8 个文章链接。进入现有评分与去重流程，不承诺每天每个来源都有新文章。One Useful Thing 等观点来源并非日报，少数派 Feed 只有最近一批文章，可能没有命中 AI 主题。

ChatGPT 更新日志普通 HTTP 请求实测 403；Canva 有时返回挑战页面，或文章结构无法提取日期，属于待解决来源，不能算稳定接通。小众软件 RSS 在本机读取成功，但 VPS 实测 403，需要后续解决访问差异。配置保留有限次数的普通请求和日志诊断，不绕过验证码或登录要求。Runway 页面可读，本次列表中可识别文章早于最近 30 天。即梦为官网内容变化监测：首次建立基线不推送旧功能，后续变化标注“待核实”，观察时间不等于产品发布时间。它不等于整个即梦探索社区已接入。

Future Tools 列表使用小时相对时间，记录 `date_precision=relative`；正式发布时间优先由原始来源核验。没有可识别发布时间的普通文章不会被当成当天新闻。

不消耗模型或 X 配额的检查：

```sh
uv run python -m scripts.check_creator_sources --days 7
```

检查输出区分读取成功、部分文章不可用、接口不可用与零近期内容；临时存储官网监测基线，不改生产状态。

## X 候选账号

这是按选题用途整理的观察名单，不是按粉丝量或近期互动数据计算的排行榜。当前没有给所有候选调用付费接口抓取近期样本，因此不能宣称谁“最好”。

| 账号 | 用途 | 建议 |
|---|---|---|
| [Tim Simmons @TheoMediaAI](https://x.com/TheoMediaAI) | AI 影视工具实测、制作方法和局限 | 重点候选；作者网站和 YouTube 可补充 |
| [Matt Wolfe @mreflow](https://x.com/mreflow) | 新工具、产品体验、新闻整理 | 重点候选；Future Tools 已补充同作者内容 |
| [Rowan Cheung @rowancheung](https://x.com/rowancheung) | 大众 AI 新闻、产品功能与应用案例 | 重点候选；The Rundown RSS 已接入 |
| [Ethan Mollick @emollick](https://x.com/emollick) | AI 对工作、教育和个人能力的影响 | 观点解读候选；One Useful Thing 已接入 |
| [Min Choi @minchoi](https://x.com/minchoi) | 视觉效果、有趣案例、应用合集 | 发现线索；回到案例原作者核验，区分赞助与实测 |

Tim 的[官网](https://theoreticallymedia.com/)结构化资料链接到 @TheoMediaAI；[Matt 官网](https://mattwolfe.com/)、[The Rundown](https://www.therundown.ai/)、[Ethan 自述](https://www.oneusefulthing.org/about)用于交叉核对作者定位。

当前 Twitter135 采集关闭，账号列表为空；Follow Builders 对共享 Feed 中的账号统一处理。以后若启用专门追踪，应按账号数和轮询频率核算请求预算，并计入 ID 解析和人工测试请求。通过作者博客补充覆盖不等于已抓到其全部 X 帖子。

## 视频与社交平台获取方法

| 平台 | 可用方法 | 具体限制与建议 |
|---|---|---|
| YouTube | 官方频道 Atom Feed；Data API 查询 uploads 播放列表 | 可获取标题、简介、链接、时间；API 需要项目密钥。公开更新不等于有权获取任意视频字幕 |
| B站 | RSSHub UP 主视频/动态路由；有授权的开放平台接口 | RSSHub 路由可能需要 Cookie，存在风控维护；官方开放平台主要面向授权账号，不是任意 UP 主全站搜索 |
| 小红书 | 授权数据服务；本机登录浏览器的人工辅助采集 | 未核实通用官方笔记搜索 API；公开电商开放平台不能等同内容搜索接口。需要账号会话或供应商密钥 |
| 抖音 | 官方授权账号 API；第三方数据服务 | 官方 video.list 要作者授权，不能直接追踪所有博主；第三方服务需要实测、费用预算 |
| 视频号 | 经验证的数据服务、用户分享链接与登录会话的人工辅助整理 | 本次未核实可长期用于任意博主订阅的公开官方接口；不能用微信公众号 API 代替视频号 |

### 原始技术依据

- [YouTube 官方频道 Feed / Push](https://developers.google.com/youtube/data/guides/push_notifications)：频道发布、标题和简介变化通知。
- [YouTube playlistItems.list](https://developers.google.com/youtube/data/reference/rest/v3/playlistItems/list)：uploads 列表，每次 1 quota unit。
- [YouTube captions.download](https://developers.google.com/youtube/data/reference/rest/v3/captions/download)：要求用户具有视频编辑权限，不是任意字幕下载 API。
- [B站开放平台](https://open.bilibili.com/doc)：账号和稿件授权；[RSSHub B站路由源码](https://github.com/DIYgod/RSSHub/tree/master/lib/routes/bilibili)。
- [抖音授权账号视频列表](https://open.douyin.com/platform/resource/docs/openapi/video-management/douyin/search-video/account-video-list/)：video.list scope，需要用户授权。
- [小红书开放平台](https://open.xiaohongshu.com/)：当前公开入口主要为店铺、电商与授权应用。
- [MediaCrawler 项目](https://github.com/NanmiCoder/MediaCrawler)提供小红书、抖音、B站等采集实现，但[当前许可证](https://github.com/NanmiCoder/MediaCrawler/blob/main/LICENSE)限制非商业学习用途，未用于本项目生产环境。
- 第三方 TikHub 文档列有[小红书作者笔记列表](https://docs.tikhub.io/420136396e0)与[抖音作者视频列表](https://docs.tikhub.io/186826223e0)。这是供应商接口能力声明，本次未购买或实测；未据此承诺其视频号覆盖能力。

优先顺序：先稳定运行公开 RSS/网页，再接 YouTube 频道元数据；B站少量 UP 主做试点；小红书/抖音选择可验证的数据服务或本机辅助工作流。视频号先保持分享链接整理，直到找到并实测可用供应商。VPS 仅约 1GB 内存，暂不在上面额外部署多个常驻浏览器或本地转写模型。
