---
layout: page
title: Информация
subtitle: Об этом сайте
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Об авторе, информация, контакты
share-description: Информация о сайте Заметки географа. Контакты. Условия использования. Связь с автором. Дорога не кончается!!!
last_modified_at: 2022-01-14 10:00:00 +0300
language: ru
keywords: информация, контакты
permalink: /info/
head-extra: [etc/_aboutme.html, etc/ads.html]
footer-extra: [etc/ads-footer.html]
---
<div class="posts-list">
  {% for info in site.info %}
  <article class="post-preview">

    {%- capture thumbnail -%}
      {% if info.thumbnail-img %}
        {{ info.thumbnail-img }}
      {% elsif info.cover-img %}
        {% if info.cover-img.first %}
          {{ info.cover-img[0].first.first }}
        {% else %}
          {{ info.cover-img }}
        {% endif %}
      {% else %}
      {% endif %}
    {% endcapture %}
    {% assign thumbnail=thumbnail | strip %}

    {% if site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="post-image post-image-normal">
      <a href="{{ info.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="page thumbnail">
      </a>
    </div>
    {% endif %}
    {% endif %}

    <a href="{{ info.url | absolute_url }}">
      <h2 class="post-title">{{ info.title }}</h2>

      {% if info.subtitle %}
        <h3 class="post-subtitle">
        {{ info.subtitle }}
        </h3>
      {% endif %}
    </a>

    <p class="post-meta">
      {% assign date_format = site.date_format | default: "%B %-d, %Y" %}
      Дата публикации {{ info.date | date: date_format }}
    </p>

    {% if thumbnail != "" %}
    <div class="post-image post-image-small">
      <a href="{{ info.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="page thumbnail">
      </a>
    </div>
    {% endif %}

    {% unless site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="post-image post-image-short">
      <a href="{{ info.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="page thumbnail">
      </a>
    </div>
    {% endif %}

    <div class="post-entry">
      {{ info.description }}
      <a href="{{ info.url | absolute_url }}" class="post-read-more">[Читать&nbsp;далее]</a>
    </div>
    {% endunless %}

    {% if site.feed_show_tags != false and info.tags.size > 0 %}
    <div class="blog-tags">
      <span>Метки:</span>
      {% for tag in info.tags %}
      <a href="{{ '/tags/' | absolute_url }}#{{- tag -}}">{{- tag -}}</a>
      {% endfor %}
    </div>
    {% endif %}

   </article>
  {% endfor %}
</div>
