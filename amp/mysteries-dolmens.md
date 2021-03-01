---
layout: amp
title: Тайны тысячелетних дольменов Кубани
subtitle: Публикация посвящена памятникам археологии — дольменам Западного Кавказа
cover-img: /img/example-logos/main-cover.jpg
share-img: /img/example-logos/main-cover4x3.jpg
language: ru
last_modified_at: 2021-02-24 02:30:00 +0300
date: 2021-02-23 15:00
---
{: .box-note}
## <br><br><br>Тайны тысячелетних дольменов Кубани

Путешествуя по Кубани на автомобиле или пешком с рюкзаком, отдыхая на Чёрном море и совершая экскурсии, гости нашего края, да и сами кубанцы, посещают уникальные памятники археологии — дольмены. После знакомства с ними у многих возникают различные вопросы, на которые зачастую трудно ответить однозначно по объективным причинам. В этой публикации автор, используя данные начиная с ХIХ в. до последних открытий археологов и исследователей древностей Кубани в ХХI в., делает попытку найти правдивые ответы на множество вопросов о загадочной культуре строителей дольменов Западного Кавказа.

<div class="mysteries-dolmenss-list">
  {% for mysteries-dolmens in site.mysteries-dolmens %}
  <article class="mysteries-dolmens-preview">

    {%- capture thumbnail -%}
      {% if mysteries-dolmens.thumbnail-img %}
        {{ mysteries-dolmens.thumbnail-img }}
      {% elsif mysteries-dolmens.cover-img %}
        {% if mysteries-dolmens.cover-img.first %}
          {{ mysteries-dolmens.cover-img[0].first.first }}
        {% else %}
          {{ mysteries-dolmens.cover-img }}
        {% endif %}
      {% else %}
      {% endif %}
    {% endcapture %}
    {% assign thumbnail=thumbnail | strip %}

    {% if site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="mysteries-dolmens-image mysteries-dolmens-image-normal">
      <a href="{{ mysteries-dolmens.url | absolute_url }}" aria-label="Thumbnail">
        <amp-img src="{{ thumbnail | absolute_url }}" alt="mysteries-dolmens thumbnail" layout="intrinsic" width="220" height="220"></amp-img>
      </a>
    </div>
    {% endif %}
    {% endif %}

    <a href="{{ mysteries-dolmens.url | absolute_url }}">
      <h2 class="mysteries-dolmens-title">{{ mysteries-dolmens.title }}</h2>

      {% if mysteries-dolmens.subtitle %}
        <h3 class="mysteries-dolmens-subtitle">
        {{ mysteries-dolmens.subtitle }}
        </h3>
      {% endif %}
    </a>

    <p class="mysteries-dolmens-meta">
      {% assign date_format = site.date_format | default: "%B %-d, %Y" %}
      Дата публикации {{ mysteries-dolmens.date | date: date_format }}
    </p>

    {% if thumbnail != "" %}
    <div class="mysteries-dolmens-image mysteries-dolmens-image-small">
      <a href="{{ mysteries-dolmens.url | absolute_url }}" aria-label="Thumbnail">
        <amp-img src="{{ thumbnail | absolute_url }}" alt="mysteries-dolmens thumbnail" layout="intrinsic" width="220" height="220"></amp-img>
      </a>
    </div>
    {% endif %}

    {% unless site.feed_show_excerpt == false %}
    {% if thumbnail != "" %}
    <div class="mysteries-dolmens-image mysteries-dolmens-image-short">
      <a href="{{ mysteries-dolmens.url | absolute_url }}" aria-label="Thumbnail">
        <amp-img src="{{ thumbnail | absolute_url }}" alt="mysteries-dolmens thumbnail" layout="intrinsic" width="220" height="220"></amp-img>
      </a>
    </div>
    {% endif %}

    <div class="mysteries-dolmens-entry">
      {{ mysteries-dolmens.description }}
      <a href="{{ mysteries-dolmens.url | absolute_url }}" class="mysteries-dolmens-read-more">[Читать&nbsp;далее]</a>
    </div>
    {% endunless %}

    {% if site.feed_show_tags != false and mysteries-dolmens.tags.size > 0 %}
    <div class="blog-tags">
      <span>Метки:</span>
      {% for tag in mysteries-dolmens.tags %}
      <a href="{{ '/tags/' | absolute_url }}#{{- tag -}}">{{- tag -}}</a>
      {% endfor %}
    </div>
    {% endif %}

   </article>
  {% endfor %}
</div>
