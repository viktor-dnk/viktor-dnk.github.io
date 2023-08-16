---
layout: page
title: Побережье Чёрного и Азовского морей
subtitle: Топонимика на морском побережье Кубани
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Топонимы Черноморского и Азовского побережья Кубани
share-description: «Морские ворота юга России», как и «Балтийское окно в Европу» начал возводить Петр I. В Таганрогском заливе в 1698 г. была основана военно-морская база.
language: ru
keywords: карты, история, география, ономастика, Чёрное море, Азвоское море
last_modified_at: 2023-05-10 19:00:00 +0300
date: 2022-01-14 16:00:00
permalink: /toponymy/sea-coast/
head-extra: [etc/_micro_sea-coast.html, etc/_aboutme.html,  ads/ads.html]
footer-extra: [ads/ads-footer.html]
---
«Морские ворота юга России», как и «Балтийское окно в Европу» начал возводить ещё император Пётр I. На северном берегу Таганрогского залива Азовского моря в 1698 г. была основана им первая военно-морская база России. Императрица Екатерина II завершила дело начатое Петром, она вернула земли Тьмутараканского княжества России, отторгнутые Византией, а затем захваченные Османской империей. Краснодарский край омывается с северо-запада Азовским и с юго-запада Чёрным морями, которые соединены Керченским проливом и удалении всего на 32 км. Они позволяют России выходить в Мировой океан, что имеет важное военно-стратегическое и экономическое значение.

<div class="posts-list">
  {% assign sea-coast = site.toponymy | where: "category", "sea-coast" %}
  {% for toponymy in sea-coast %}
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

                        {% if forloop.index == 4 %}
                        {% include ads/ads-cat-1.html %}
                        {% endif %}
                        {% if forloop.index == 11 %}
                        {% include ads/ads-cat-2.html %}
                        {% endif %}
                        {% if forloop.index == 20 %}
                        {% include ads/ads-cat-3.html %}
                        {% endif %}

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
