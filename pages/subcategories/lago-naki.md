---
layout: page
title: Нагорье Лагонаки
subtitle: Топонимы вокруг Лагонакского нагорья
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Топонимика Лагонаки
share-description: Под названием Лагонаки понимается нагорье, горный узел обшей площадью около 700 км². Это природное образование принято так называть с 1984 г.
language: ru
keywords: карты, история, география, ономастика, Лагонаки, нагорье
last_modified_at: 2022-01-26 14:00:00 +0300
date: 2022-01-14 16:00:00
permalink: /toponymy/lago-naki/
head-extra: [etc/_micro_lago-naki.html, etc/_aboutme.html, etc/ads.html]
footer-extra: [etc/ads-footer.html]
---
Под названием **Лагонаки** понимается нагорье, горный узел обшей площадью около 700 км². Это природное образование принято так называть с 1984 г., обосновал и доказал это Сергей Павлович Лозовой. Нагорье объединяет в себе ряд плато, хребтов, долин рек, вершин. В административном отношении нагорье находится в Республике Адыгея (Майкопский район) и Краснодарском крае (Апшеронский и Хостинский районы). Большая часть Лагонакского нагорья, входит в состав территории ФГУ Кавказский заповедник и называется - Лагонакский биосферный полигон.

<div class="posts-list">
  {% assign lago-naki = site.toponymy | where: "category", "lago-naki" %}
  {% for toponymy in lago-naki %}
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
