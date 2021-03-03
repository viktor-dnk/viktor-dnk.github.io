---
layout: page
title: Информация
subtitle: Об этом сайте
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
language: ru
---
<div class="posts-list">
  {% for info in site.info %}
  <article class="post-preview">

    {%- capture thumbnail -%}
      {% if page.thumbnail-img %}
        {{ page.thumbnail-img }}
      {% elsif page.cover-img %}
        {% if page.cover-img.first %}
          {{ page.cover-img[0].first.first }}
        {% else %}
          {{ page.cover-img }}
        {% endif %}
      {% else %}
      {% endif %}
    {% endcapture %}
    {% assign thumbnail=thumbnail | strip %}

    {% if site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="post-image post-image-normal">
      <a href="{{ page.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="page thumbnail">
      </a>
    </div>
    {% endif %}
    {% endif %}

    <a href="{{ page.url | absolute_url }}">
      <h2 class="post-title">{{ page.title }}</h2>

      {% if page.subtitle %}
        <h3 class="post-subtitle">
        {{ page.subtitle }}
        </h3>
      {% endif %}
    </a>

    <p class="post-meta">
      {% assign date_format = site.date_format | default: "%B %-d, %Y" %}
      Дата публикации {{ page.date | date: date_format }}
    </p>

    {% if thumbnail != "" %}
    <div class="post-image post-image-small">
      <a href="{{ page.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="page thumbnail">
      </a>
    </div>
    {% endif %}

    {% unless site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="post-image post-image-short">
      <a href="{{ page.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="page thumbnail">
      </a>
    </div>
    {% endif %}

    <div class="post-entry">
      {{ page.description }}
      <a href="{{ page.url | absolute_url }}" class="post-read-more">[Читать&nbsp;далее]</a>
    </div>
    {% endunless %}

    {% if site.feed_show_tags != false and page.tags.size > 0 %}
    <div class="blog-tags">
      <span>Метки:</span>
      {% for tag in page.tags %}
      <a href="{{ '/tags/' | absolute_url }}#{{- tag -}}">{{- tag -}}</a>
      {% endfor %}
    </div>
    {% endif %}

   </article>
  {% endfor %}
</div>
