---
layout: default
title: AI 资讯雷达
body_class: home-page
---

{% assign zh_posts = site.posts | where: "lang", "zh" %}
{% assign latest_post = zh_posts | first %}

<section class="daily-digest" aria-labelledby="daily-digest-title">
  <header class="section-heading">
    <div>
      <p class="eyebrow">DAILY BRIEF</p>
      <h2 id="daily-digest-title">每日速递</h2>
      {% if latest_post %}
        <p class="latest-date">{{ latest_post.date | date: "%Y 年 %m 月 %d 日" }}</p>
      {% endif %}
    </div>
    <a class="history-link" href="{{ '/archive/' | relative_url }}">
      <span>查看历史日报</span>
      <svg aria-hidden="true" viewBox="0 0 20 20"><path d="M7.5 4.5 13 10l-5.5 5.5"/></svg>
    </a>
  </header>

  {% if latest_post %}
    {% assign latest_body = latest_post.content | split: '</h1>' | last %}
    {% assign latest_body = latest_body | replace: '<h3', '<h4' | replace: '</h3>', '</h4>' %}
    {% assign latest_body = latest_body | replace: '<h2', '<h3' | replace: '</h2>', '</h3>' %}
    <article class="latest-digest-content">
      {{ latest_body }}
    </article>
  {% else %}
    <div class="empty-state">今天的日报还在生成中，请稍后再来。</div>
  {% endif %}
</section>
