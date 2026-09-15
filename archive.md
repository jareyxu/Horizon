---
layout: default
title: 历史日报
permalink: /archive/
body_class: archive-page
---

{% assign zh_posts = site.posts | where: "lang", "zh" %}

<header class="archive-heading">
  <p class="eyebrow">ARCHIVE</p>
  <h1>历史日报</h1>
  <p>按日期回看过去的 AI 资讯速递。</p>
</header>

<nav class="digest-archive" aria-label="历史日报">
  {% for post in zh_posts offset:1 %}
    <a class="digest-archive-item" href="{{ post.url | relative_url }}">
      <span>{{ post.date | date: "%Y 年 %m 月 %d 日" }}</span>
      <svg aria-hidden="true" viewBox="0 0 20 20"><path d="M7.5 4.5 13 10l-5.5 5.5"/></svg>
    </a>
  {% else %}
    <p class="empty-state">还没有历史日报。</p>
  {% endfor %}
</nav>
