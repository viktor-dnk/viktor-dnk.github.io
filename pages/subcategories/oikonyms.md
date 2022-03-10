---
layout: page
title: Населённые пункты Кубани
subtitle: Ойконимы Краснодарского Края и Республики Адыгея
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Топонимика населённых пунктов Кубани и Адыгеи
share-description: Одно из направлений топонимики занимается изучением собственных названий населенных пунктов (городов, посёлков, сёл, станиц, хуторов) называется ойконимия.
language: ru
keywords: карты, история, география, ономастика, ойконим
last_modified_at: 2022-01-26 14:00:00 +0300
date: 2022-01-14 16:00:00
permalink: /toponymy/oikonyms/
head-extra: [etc/_micro_oikonyms.html, etc/_aboutme.html]
---
На Земле всё имеет свой адрес, своё название. Для человека этот адрес начинается с места рождения, то есть с родины, поэтому каждый человек должен знать его и уметь объяснить его значение. Одно из направлений топонимики занимается изучением собственных названий населённых пунктов (аулов, городов, посёлков, сёл, станиц, хуторов) называется **ойконимия**, термин образован от греческого слова буквально означающего «дома имя».

В 1774 г. османская крепость Копыл стала Российской, и с приходом русских войск в 1777 г. стала резиденцией командующего Кубанским корпусом. В 1865 г. у крепости основывается станица, которая впоследствии превратилась в город Славянск-на-Кубани, так как на Кубани основан. Город можно считать и первым на Кубани административным центром, так как здесь ещё в 1777 г. была учреждена резиденция командующего Кубанским корпусом.

<div class="posts-list">
  {% assign oikonyms = site.toponymy | where: "category", "oikonyms" %}
  {% for toponymy in oikonyms %}
  <article class="post-preview">

  <!--    {%- capture thumbnail -%}
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
      {% if thumbnail != "" %} -->
      <div class="post-image post-image-normal">
        <a href="{{ toponymy.url | absolute_url }}" aria-label="Thumbnail">
          <img src="{{ toponymy.url | absolute_url | replace:'.ru/','.ru/img/' | append: 'thumb.jpg' }}" alt="{{ toponymy.thumbnail-caption }}" title="{{ toponymy.thumbnail-caption }}">
        </a>
      </div>
  <!--    {% endif %}
      {% endif %} -->

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
        <img src="{{ toponymy.url | absolute_url | replace:'.ru/','.ru/img/' | append: 'thumb.jpg' }}" alt="{{ toponymy.thumbnail-caption }}" title="{{ toponymy.thumbnail-caption }}">
      </a>
    </div>
    {% endif %}

    {% unless site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="post-image post-image-short">
      <a href="{{ toponymy.url | absolute_url }}" aria-label="Thumbnail">
        <img src="{{ toponymy.url | absolute_url | replace:'.ru/','.ru/img/' | append: 'thumb.jpg' }}" alt="{{ toponymy.thumbnail-caption }}" title="{{ toponymy.thumbnail-caption }}">
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
