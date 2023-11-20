---
layout: page
title: Ономастика горных вершин, перевалов и пр.
subtitle: Оронимы Кубани и Адыгеи
cover-img: ["/img/example-logos/main-cover.jpg" : "Генеральная карта Кавказского края, изданная в 1858 г."]
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Оронимы Кубани и Адыгеи
share-description: Раздел топонимики, который изучает названия вершин, горных систем, скал, перевалов, хребтов, называется оронимика, что с греческого означает «горы имя».
language: ru
keywords: карты, история, география, ономастика, ороним
last_modified_at: 2023-05-10 19:00:00 +0300
date: 2022-01-14 16:00:00
permalink: /toponymy/mountains/
head-extra: [amp_link.html, etc/_aboutme.html, ads/ads.html, etc/_micro_mountains.html]
footer-extra: [ads/ads-footer.html]
---
Наука изучающая имена собственные всех типов и их происхождение называется **ономастика** (от греческого onomastikys - «искусство давать имена»). **Топонимика** (от греческих слов topos - «место» и onyma - «имя, название», то есть «имя места») раздел ономастики, изучающий историю происхождения географических названий. Раздел топонимики, который изучает названия вершин, горных систем, скал, перевалов, нагорий, равнин, ущелий, долин, хребтов, называется **оронимика**, что с греческого буквально означает «горы имя». К оронимам относят географические названия всех положительных (гора, скала и другое) и отрицательных (ущелье, долина и другое) форм рельефа, независимо от их размера.

<div class="posts-list">
  {% assign mountains = site.toponymy | where: "category", "mountains" %}
  {% for toponymy in mountains %}
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

                        {% if forloop.index == 5 %}
                        {% include ads/ads-cat-1.html %}
                        {% endif %}
                        {% if forloop.index == 16 %}
                        {% include ads/ads-cat-2.html %}
                        {% endif %}
                        {% if forloop.index == 28 %}
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
