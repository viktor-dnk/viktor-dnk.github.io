---
layout: page
title: Память в камне
subtitle: Памятные места связанные с историческими событиями
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Памятные места связанные с историческими событиями
share-description: На Кубани не мало памятных мест связанных с событиями Великой Отечественной войны 1941-1945 гг., Гражданской войны и другими историческими событиями.
language: ru
keywords: карты, история, география, ономастика
last_modified_at: 2022-01-27 14:00:00 +0300
date: 2022-01-27 14:00:00 +0300
permalink: /toponymy/in-memory/
head-extra: _micro_in-memory.html
---
 На Кубани не мало памятных мест связанных с событиями Великой Отечественной войны 1941-1945 гг., Гражданской войны и другими историческими событиями, которые были отмечены памятными знаками, обелисками, памятниками и другое. И установлены памятные знаки не только в населённых пунктах, но и в горно-лесной зоне. Например: могила советским воинам-авиаторам в долине реки Адегой; памятник подвигу казаков погибших при защите Георгиевского-Липского поста; памятник лётчикам на горе Собер-Баш; памятник на горе Семашхо «Стойкости комсомольской» и так далее. Запечатлена память и в топонимах например гора Батарейная, расположенная на границе Лазаревского и Туапсинского районов.

<div class="posts-list">
  {% assign in-memory = site.toponymy | where: "category", "in-memory" %}
  {% for toponymy in in-memory %}
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
