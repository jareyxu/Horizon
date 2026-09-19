---
layout: default
title: AI 资讯雷达
body_class: home-page
---

{% assign zh_posts = site.posts | where: "lang", "zh" %}
{% assign latest_post = zh_posts | first %}

{% if latest_post %}
  {% assign source_body = latest_post.content | split: '</h1>' | last %}
  {% assign summary_html = source_body | split: '<blockquote>' | last | split: '</blockquote>' | first %}
  {% assign summary_plain = summary_html | strip_html | strip %}
  {% assign total_count = summary_plain | split: '从 ' | last | split: ' 条' | first | strip %}
  {% assign selected_count = summary_plain | split: '筛选出 ' | last | split: ' 条' | first | strip %}
  {% assign body_parts = source_body | split: '<ol>' %}
  {% assign toc_chunk = body_parts[1] %}
  {% assign toc_inner = toc_chunk | split: '</ol>' | first %}
  {% assign detail_body = source_body | replace: '<h3', '<h4' | replace: '</h3>', '</h4>' %}
  {% assign detail_body = detail_body | replace: '<h2', '<h3' | replace: '</h2>', '</h3>' %}
  {% assign weekday = latest_post.date | date: '%w' %}
  {% case weekday %}
    {% when '0' %}{% assign weekday_zh = '星期日' %}
    {% when '1' %}{% assign weekday_zh = '星期一' %}
    {% when '2' %}{% assign weekday_zh = '星期二' %}
    {% when '3' %}{% assign weekday_zh = '星期三' %}
    {% when '4' %}{% assign weekday_zh = '星期四' %}
    {% when '5' %}{% assign weekday_zh = '星期五' %}
    {% when '6' %}{% assign weekday_zh = '星期六' %}
  {% endcase %}
{% endif %}

<section class="radar-hero" aria-labelledby="daily-digest-title">
  <div class="radar-hero-copy">
    <p class="eyebrow">DAILY BRIEF</p>
    <h2 id="daily-digest-title">每日<span>速递</span></h2>
    <p class="hero-subtitle">聚焦全球 AI 动态，洞察值得关注的技术、产品与行业进展。</p>
    {% if latest_post %}
      <div class="hero-date">
        <svg aria-hidden="true" viewBox="0 0 24 24"><path d="M7 3v3m10-3v3M4.5 9.5h15M6 5h12a2 2 0 0 1 2 2v12H4V7a2 2 0 0 1 2-2Z"/></svg>
        <time datetime="{{ latest_post.date | date: '%Y-%m-%d' }}">{{ latest_post.date | date: "%Y 年 %m 月 %d 日" }}</time>
        <span>{{ weekday_zh }}</span>
        <span class="hero-date-note">每天早上 06:00 更新</span>
      </div>
    {% endif %}
  </div>

  <div class="radar-visual" aria-hidden="true">
    <svg viewBox="0 0 620 300" role="presentation">
      <defs>
        <linearGradient id="radar-globe" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#d9ecff"/>
          <stop offset=".5" stop-color="#7cb7ff"/>
          <stop offset="1" stop-color="#176ff2"/>
        </linearGradient>
        <linearGradient id="radar-card" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#fff" stop-opacity=".86"/>
          <stop offset="1" stop-color="#d8eaff" stop-opacity=".42"/>
        </linearGradient>
        <filter id="radar-shadow" x="-50%" y="-50%" width="200%" height="200%">
          <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#1268db" flood-opacity=".18"/>
        </filter>
      </defs>
      <g transform="translate(390 145)" filter="url(#radar-shadow)">
        <circle r="102" fill="url(#radar-globe)" opacity=".82"/>
        <ellipse rx="102" ry="38" fill="none" stroke="#fff" stroke-opacity=".72"/>
        <ellipse rx="47" ry="102" fill="none" stroke="#fff" stroke-opacity=".5"/>
        <path d="M-88-48c37 16 139 16 176 0M-94 47c44-18 144-18 188 0" fill="none" stroke="#fff" stroke-opacity=".48"/>
        <ellipse rx="168" ry="66" fill="none" stroke="#398cff" stroke-opacity=".45" transform="rotate(-10)"/>
        <circle cx="-146" cy="10" r="6" fill="#0ea5e9"/>
        <circle cx="151" cy="-31" r="5" fill="#0ea5e9"/>
        <circle cx="65" cy="-90" r="4" fill="#fff"/>
      </g>
      <g class="radar-glass-card" transform="translate(125 62) rotate(-5)" filter="url(#radar-shadow)">
        <rect width="142" height="178" rx="20" fill="url(#radar-card)" stroke="#fff" stroke-opacity=".9"/>
        <text x="24" y="68" fill="#1268e8" font-size="42" font-weight="750">AI</text>
        <text x="24" y="96" fill="#31517c" font-size="14" font-weight="600">更快 · 更深 · 更广</text>
        <path d="M24 124h72M24 137h50" stroke="#6ea8ef" stroke-width="4" stroke-linecap="round" opacity=".65"/>
      </g>
      <g class="radar-labels" fill="#174e9d" font-size="13" font-weight="650">
        <g transform="translate(330 38)"><rect width="70" height="32" rx="16" fill="#fff" fill-opacity=".9"/><text x="21" y="21">技术</text></g>
        <g transform="translate(496 81)"><rect width="70" height="32" rx="16" fill="#fff" fill-opacity=".9"/><text x="21" y="21">产品</text></g>
        <g transform="translate(485 210)"><rect width="70" height="32" rx="16" fill="#fff" fill-opacity=".9"/><text x="21" y="21">行业</text></g>
        <g transform="translate(319 229)"><rect width="70" height="32" rx="16" fill="#fff" fill-opacity=".9"/><text x="21" y="21">趋势</text></g>
      </g>
    </svg>
  </div>
</section>

{% if latest_post %}
  <section class="digest-dashboard" aria-label="今日 AI 资讯概览" data-dashboard>
    <div class="digest-ranking-card">
      <header class="digest-card-header">
        <div class="digest-summary-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M7 3h8l4 4v14H5V3h2Zm7 0v5h5M8 12h8M8 16h6"/></svg>
        </div>
        <div class="digest-summary-text">{{ summary_html }}</div>
        <a class="history-link" href="{{ '/archive/' | relative_url }}">
          <span>查看历史日报</span>
          <svg aria-hidden="true" viewBox="0 0 20 20"><path d="M7.5 4.5 13 10l-5.5 5.5"/></svg>
        </a>
      </header>

      <ol class="digest-ranking" data-dashboard-ranking>
        {{ toc_inner }}
      </ol>
    </div>

    <aside class="dashboard-aside" aria-label="今日数据">
      <section class="overview-card" aria-labelledby="overview-title">
        <header class="aside-card-title">
          <svg aria-hidden="true" viewBox="0 0 24 24"><path d="M5 20V10m7 10V4m7 16v-7"/></svg>
          <h3 id="overview-title">AI 行业今日概览</h3>
        </header>
        <div class="stat-grid">
          <div class="stat-item stat-blue"><span class="stat-icon" aria-hidden="true">◎</span><strong>{{ total_count }}</strong><small>今日全网资讯</small></div>
          <div class="stat-item stat-amber"><span class="stat-icon" aria-hidden="true">★</span><strong>{{ selected_count }}</strong><small>精选重要资讯</small></div>
          <div class="stat-item stat-violet"><span class="stat-icon" aria-hidden="true">◆</span><strong data-dashboard-highest>—</strong><small>今日最高评分</small></div>
          <div class="stat-item stat-green"><span class="stat-icon" aria-hidden="true">↗</span><strong data-dashboard-average>—</strong><small>平均关注评分</small></div>
        </div>
      </section>

      <section class="trend-card" aria-labelledby="trend-title">
        <div class="aside-card-title trend-heading">
          <div>
            <p class="eyebrow">7 DAY SIGNAL</p>
            <h3 id="trend-title">一周精选趋势</h3>
          </div>
          <span>篇数</span>
        </div>
        {% assign recent_posts = zh_posts | slice: 0, 7 | reverse %}
        <ol class="mini-trend" data-digest-trend>
          {% for post in recent_posts %}
            {% assign post_summary = post.content | split: '<blockquote>' | last | split: '</blockquote>' | first | strip_html | strip %}
            {% assign post_selected = post_summary | split: '筛选出 ' | last | split: ' 条' | first | strip %}
            <li data-count="{{ post_selected }}">
              <span class="trend-value">{{ post_selected }}</span>
              <span class="trend-track"><span class="trend-bar"></span></span>
              <time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%m/%d' }}</time>
            </li>
          {% endfor %}
        </ol>
      </section>

      <blockquote class="radar-quote">
        <svg aria-hidden="true" viewBox="0 0 32 24"><path d="M0 24V13C0 4 5 0 13 0v6c-4 0-6 2-6 6h6v12H0Zm19 0V13c0-9 5-13 13-13v6c-4 0-6 2-6 6h6v12H19Z"/></svg>
        <p>在信息的洪流中，为你留下真正值得关注的信号。</p>
      </blockquote>

      <a class="rss-card" href="{{ '/feed-zh.xml' | relative_url }}">
        <span class="rss-card-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 11.5a7.5 7.5 0 0 1 7.5 7.5M5 5a14 14 0 0 1 14 14M6 19a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"/></svg></span>
        <span><strong>每日 AI 资讯，准时送达</strong><small>通过 RSS 获取最新精选内容</small></span>
        <svg class="rss-card-arrow" aria-hidden="true" viewBox="0 0 20 20"><path d="M7.5 4.5 13 10l-5.5 5.5"/></svg>
      </a>
    </aside>
  </section>

  <section class="daily-details" aria-labelledby="daily-details-title">
    <header class="details-heading">
      <div>
        <p class="eyebrow">FULL REPORT</p>
        <h2 id="daily-details-title">今日详情</h2>
      </div>
      <p>包含摘要、背景、核验信息与参考来源。</p>
    </header>
    <article class="latest-digest-content">
      {{ detail_body }}
    </article>
  </section>
{% else %}
  <div class="empty-state">今天的日报还在生成中，请稍后再来。</div>
{% endif %}
