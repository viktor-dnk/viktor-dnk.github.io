---
layout: page
title: Топонимика
subtitle: Очерки по топонимике Кубани
cover-img: /img/example-logos/main-cover.jpg
language: ru
---
<div class="toponymy-list">
  {% for toponymy in site.toponymy %}
  <article class="toponymy-preview">

    {%- capture thumbnail -%}
      {% if toponymy.thumbnail-img %}
        {{ toponymy.thumbnail-img }}
      {% elsif toponymy.cover-img %}
        {% if toponymy.cover-img.first %}
          {{ toponymy.cover-img[0].first.first }}
        {% else %}
          {{ toponymy.cover-img }}
        {% endif %}
      {% else %}
      {% endif %}
    {% endcapture %}
    {% assign thumbnail=thumbnail | strip %}

    {% if site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="toponymy-image toponymy-image-normal">
      <a href="{{ toponymy.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="toponymy thumbnail">
      </a>
    </div>
    {% endif %}
    {% endif %}

    <a href="{{ toponymy.url | absolute_url }}">
      <h2 class="toponymy-title">{{ toponymy.title }}</h2>

      {% if toponymy.subtitle %}
        <h3 class="toponymy-subtitle">
        {{ toponymy.subtitle }}
        </h3>
      {% endif %}
    </a>

    <p class="toponymy-meta">
      {% assign date_format = site.date_format | default: "%B %-d, %Y" %}
      Дата публикации {{ toponymy.date | date: date_format }}
    </p>

    {% if thumbnail != "" %}
    <div class="toponymy-image toponymy-image-small">
      <a href="{{ toponymy.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="toponymy thumbnail">
      </a>
    </div>
    {% endif %}

    {% unless site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="toponymy-image toponymy-image-short">
      <a href="{{ toponymy.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="toponymy thumbnail">
      </a>
    </div>
    {% endif %}

    <div class="toponymy-entry">
      {{ toponymy.description }}
      <a href="{{ toponymy.url | absolute_url }}" class="toponymy-read-more">[Читать&nbsp;далее]</a>
    </div>
    {% endunless %}

    {% if site.feed_show_tags != false and toponymy.tags.size > 0 %}
    <div class="blog-tags">
      <span>Метки:</span>
      {% for tag in toponymy.tags %}
      <a href="{{ '/tags' | absolute_url }}#{{- tag -}}">{{- tag -}}</a>
      {% endfor %}
    </div>
    {% endif %}

   </article>
  {% endfor %}
</div>