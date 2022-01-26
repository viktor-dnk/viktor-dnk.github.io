---
layout: page
title: Город Краснодар и его окрестности
subtitle: топонимы вокруг столицы Кубани
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Топонимы возле Краснодара
share-description: Муниципальное образование город Краснодар расположено в центральной части Краснодарского края на правом берегу реки Кубань. Его территория составляет 841 км².
language: ru
keywords: карты, история, география, ономастика
last_modified_at: 2022-01-26 14:00:00 +0300
date: 2022-01-14 16:00:00
permalink: /toponymy/around-krasnodar/
head-extra: _micro_around-krasnodar.html
---
Муниципальное образование город Краснодар расположено в центральной части Краснодарского края на правом берегу реки Кубань. Его территория составляет 841 км². Через южную окраину города проходит 45 параллель северной широты. В 60-х годах ХIХ в. здесь проживало до 10 тыс. чел., тогда он назывался Екатеринодар. В 1880 г., в городе проживала 28 тыс. чел., а в 1901 г. числилось 68 тыс. чел. В 1920 г. Екатеринодар переименован в Краснодар. По данным 2021 г. всего в Краснодаре численность населения в границах городского округа (со входящими в его состав сельскими населёнными пунктами) составляет 1 038 000 человек.

<div class="posts-list">
  {% assign around-krasnodar = site.toponymy | where: "category", "around-krasnodar" %}
  {% for toponymy in around-krasnodar %}
  <article class="post-preview">

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
    <div class="post-image post-image-normal">
      <a href="{{ toponymy.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="{{ toponymy.thumbnail-caption }}" title="{{ toponymy.thumbnail-caption }}">
      </a>
    </div>
    {% endif %}
    {% endif %}

    <a title="{{ toponymy.share-title }}" href="{{ toponymy.url | absolute_url }}">
      <h2 class="post-title">{{ toponymy.title }}</h2>

      {% if toponymy.subtitle %}
        <h3 class="post-subtitle">
        {{ toponymy.subtitle }}
        </h3>
      {% endif %}
    </a>

    <p class="post-meta">
      {% assign date_format = site.date_format | default: "%B %-d, %Y" %}
      Дата публикации {{ toponymy.date | date: date_format }}
    </p>

    {% if thumbnail != "" %}
    <div class="post-image post-image-small">
      <a href="{{ toponymy.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="{{ toponymy.thumbnail-caption }}" title="{{ toponymy.thumbnail-caption }}">
      </a>
    </div>
    {% endif %}

    {% unless site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="post-image post-image-short">
      <a href="{{ toponymy.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ thumbnail | absolute_url }}" alt="{{ toponymy.thumbnail-caption }}" title="{{ toponymy.thumbnail-caption }}">
      </a>
    </div>
    {% endif %}

    <div class="post-entry">
      {{ toponymy.description }}
      <a title="{{ toponymy.share-title }}" href="{{ toponymy.url | absolute_url }}" class="post-read-more">[Читать&nbsp;далее]</a>
    </div>
    {% endunless %}

    {% if site.feed_show_tags != false and toponymy.tags.size > 0 %}
    <div class="blog-tags">
      <span>Метки:</span>
      {% for tag in toponymy.tags %}
      <a href="{{ '/tags/' | absolute_url }}#{{- tag -}}">{{- tag -}}</a>
      {% endfor %}
    </div>
    {% endif %}

   </article>
  {% endfor %}
</div>
