---
layout: page
title: Топонимика
subtitle: Очерки по топонимике Кубани
cover-img: /img/example-logos/main-cover.jpg
language: ru
---
_«Даже самое удачное толкование истории слова может быть пересмотрено, как только найдутся новые данные. Ничего страшного в этом нет» (Л.В. Успенский, 1960 г.)_

Видимо, многие задумывались, что означают географические названия?  **Топонимика** (от греческих слов _topos_ - «место» и _onyma_ - «имя, название», то есть «имя места») раздел ономастики, изучающий историю происхождения географических названий: населенных пунктов, морей, рек, озер, гор и др. Термин географическое название, является синонимом слова топоним. **Ономастика** (от греческого _onomastikys_ - «искусство давать имена») наука, изучающая имена собственные всех типов и их происхождение.
Изучение происхождения топонимов – дело не из простых, и иногда попытки объяснить многие из них носят случайный характер. Но как правило, перевод топонимов требует учета многих факторов, в том числе географических, исторических и языковых особенностей, а также использования максимального количества различных карт и литературы. Для выявления истории происхождения некоторых топонимов, приходится проводить камеральные исследования, которые «превращаются» в очерки. Помогает решать непростые вопросы топонимики **историческая география** — дисциплина, изучающая конкретную географию прошлого той или иной территории.

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
    {% assign yesReadTime = number | append: " минут на прочтение" %}
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
