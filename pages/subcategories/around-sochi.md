---
layout: page
title: Большой Сочи и топонимика вокруг
subtitle: Топонимика Большого Сочи и его окрестностей
cover-img: ["/img/example-logos/main-cover.jpg" : "Генеральная карта Кавказского края, изданная в 1858 г."]
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Топонимика вокруг Сочи
share-description: Город-курорт Сочи входит в состав Краснодарского края, разделён на 4 внутригородских района - Адлерский, Лазаревский, Хостинский и Центральный.
language: ru
keywords: карты, история, география, ономастика, Сочи
last_modified_at: 2023-05-10 19:00:00 +0300
date: 2022-01-14 16:00:00
permalink: /toponymy/around-sochi/
head-extra: [amp_link.html, etc/_aboutme.html, ads/ads.html, etc/_micro_around-sochi.html]
footer-extra: [ads/ads-footer.html]
---
Муниципальное образование городской округ город-курорт Сочи входит в состав Краснодарского края, разделён на 4 внутригородских района: Адлерский, Лазаревский, Хостинский и Центральный (собственно город Сочи). Является единственным в России городом расположенном в субтропиках. Городской округ расположился вдоль Чёрного моря от реки Шепси до реки Псоу на участке протяжённостью ~106 км. Город-курорт Сочи ещё называют **Большой Сочи**, а также «Курортной столицей», «Летней столицей» или «Южной столицей» России. Город известен и тем, что более 80% всей его территории расположено в особо охраняемых природных территориях Кавказского государственного заповедника и Сочинского национального парка.

<div class="posts-list">
  {% assign around-sochi = site.toponymy | where: "category", "around-sochi" %}
  {% for toponymy in around-sochi %}
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
                        {% if forloop.index == 10 %}
                        {% include ads/ads-cat-2.html %}
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
