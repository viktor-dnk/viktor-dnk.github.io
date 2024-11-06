---
layout: page
title: Топонимика Краснодарского края и Республики Адыгея
subtitle: Очерки по топонимике Кубани
cover-img: ["/img/example-logos/main-cover.jpg" : "Генеральная карта Кавказского края, изданная в 1858 г."]
share-img: /img/example-logos/main-cover4x3.jpg
share-title: Топонимика Кубани. Тайны названий.
share-description: Даже самое удачное толкование истории слова может быть пересмотрено, как только найдутся новые данные. Ничего страшного в этом нет
language: ru
keywords: карты, история, география, ономастика
last_modified_at: 2023-10-24 11:50:00 +0300
date: 2021-01-02 16:00
head-extra: [amp_link.html, etc/_aboutme.html,  ads/ads.html]
footer-extra: [ads/ads-footer.html]
permalink: /toponymy/
---
_«Даже самое удачное толкование истории слова может быть пересмотрено, как только найдутся новые данные. Ничего страшного в этом нет» (Л.В. Успенский, 1960 г.)_

Видимо, многие задумывались, что означают географические названия? **Топонимика** (от греческих слов _topos_ — «место» и _onyma_ — «имя, название», то есть «имя места») раздел ономастики, изучающий историю происхождения географических названий: населённых пунктов, морей, рек, озёр, гор и др. Термин географическое название, является синонимом слова топоним. **Ономастика** (от греческого _onomastikys_ — «искусство давать имена») наука, изучающая имена собственные всех типов и их происхождение.
Изучение происхождения топонимов – дело не из простых, и иногда попытки объяснить многие из них носят случайный характер. Но как правило, перевод топонимов требует учёта многих факторов, в том числе географических, исторических и языковых особенностей, а также использования максимального количества различных карт и литературы. Для выявления истории происхождения некоторых топонимов, приходится проводить камеральные исследования, которые «превращаются» в очерки. Помогает решать непростые вопросы топонимики **историческая география** — дисциплина, изучающая конкретную географию прошлого той или иной территории.

<div class="posts-list">
  {% for toponymy in site.toponymy reversed %}
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
                    {% if forloop.index == 15 %}
                    {% include ads/ads-cat-2.html %}
                    {% endif %}
                    {% if forloop.index == 30 %}
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
