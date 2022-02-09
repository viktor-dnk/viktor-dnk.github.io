---
layout: page
title: Дополнительная информация
subtitle: Из истории дольменов Западного Кавказа © В.Н. Ковешников
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Дополнительная информация
language: ru
keywords: карты, история, география, ономастика
last_modified_at: 2022-01-21 10:00:00 +0300
date: 2022-01-14 16:00:00
permalink: /mysteries-dolmens/info/
---
Дольмены Западного Кавказа очень разнообразны

<div class="posts-list">
  {% assign info = site.mysteries-dolmens | where: "category", "info" %}
  {% for mysteries-dolmens in info %}
  <article class="post-preview">

  <!--    {%- capture thumbnail -%}
        {% if mysteries-dolmens.thumbnail-img %}
          {{ mysteries-dolmens.thumbnail-img }}
        {% elsif mysteries-dolmens.cover-img %}
          {% if mysteries-dolmens.cover-img.first %}
            {{ mysteries-dolmens.cover-img[0].first.first }}
          {% else %}
            {{ mysteries-dolmens.cover-img }}
          {% endif %}
        {% else %}
        {% endif %}
      {% endcapture %}
      {% assign thumbnail=thumbnail | strip %}

      {% if site.feed_show_excerpt == false %}
      {% if thumbnail != "" %} -->
      <div class="post-image post-image-normal">
        <a href="{{ mysteries-dolmens.url | absolute_url }}" aria-label="Thumbnail">
          <img src="{{ mysteries-dolmens.url | absolute_url | replace:'.ru/','.ru/img/' | append: 'thumb.jpg' }}" alt="{{ mysteries-dolmens.thumbnail-caption }}" title="{{ mysteries-dolmens.thumbnail-caption }}">
        </a>
      </div>
  <!--    {% endif %}
      {% endif %} -->

    <a title="{{ mysteries-dolmens.share-title }}" href="{{ mysteries-dolmens.url | absolute_url }}">
      <h2 class="post-title">{{ mysteries-dolmens.title }}</h2>

      {% if mysteries-dolmens.subtitle %}
        <h3 class="post-subtitle">
        {{ mysteries-dolmens.subtitle }}
        </h3>
      {% endif %}
    </a>

    <p class="post-meta">
      {% assign date_format = site.date_format | default: "%B %-d, %Y" %}
      Дата публикации {{ mysteries-dolmens.date | date: date_format }}
    </p>

    {% if thumbnail != "" %}
    <div class="post-image post-image-small">
      <a href="{{ mysteries-dolmens.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ mysteries-dolmens.url | absolute_url | replace:'.ru/','.ru/img/' | append: 'thumb.jpg' }} alt="{{ mysteries-dolmens.thumbnail-caption }}" title="{{ mysteries-dolmens.thumbnail-caption }}">
      </a>
    </div>
    {% endif %}

    {% unless site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="post-image post-image-short">
      <a href="{{ mysteries-dolmens.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ mysteries-dolmens.url | absolute_url | replace:'.ru/','.ru/img/' | append: 'thumb.jpg' }} alt="{{ mysteries-dolmens.thumbnail-caption }}" title="{{ mysteries-dolmens.thumbnail-caption }}">
      </a>
    </div>
    {% endif %}

    <div class="post-entry">
      {{ mysteries-dolmens.description }}
      <a title="{{ mysteries-dolmens.share-title }}" href="{{ mysteries-dolmens.url | absolute_url }}" class="post-read-more">[Читать&nbsp;далее]</a>
    </div>
    {% endunless %}

    {% if site.feed_show_tags != false and mysteries-dolmens.tags.size > 0 %}
    <div class="blog-tags">
      <span>Метки:</span>
      {% for tag in mysteries-dolmens.tags %}
      <a href="{{ '/tags/' | absolute_url }}#{{- tag -}}">{{- tag -}}</a>
      {% endfor %}
    </div>
    {% endif %}

   </article>
  {% endfor %}
</div>
