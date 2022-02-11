---
layout: page
title: Поиск
subtitle: Работает поиск по сайту от Yandex
language: ru
cover-img: /img/example-logos/main-cover.jpg
share-title: Поиск по сайту
share-description: На сайте исправно работает поиск по сайту. Поиск производится по всем статьям за всё время их публикации.
share-img: /img/example-logos/main-cover4x3.jpg
keywords: поиск, search, яндекс
head-extra: _search.html
last_modified_at: 2022-01-14 10:00:00 +0300
date: 2021-10-09 16:00
---

{% capture google_search_site %}{{ site.url }}{{ site.baseurl }}/{% endcapture %}
<script language="Javascript" type="text/javascript">
	function google_search() {
		var query = document.getElementById("google-search").value;
		window.open("https://www.google.com/search?q=" + query + "+site:" + "{{ google_search_site | cgi_escape }}");
	}
</script>

<form id="search" onsubmit="google_search(); return false;">
	<input type="text" id="google-search" placeholder="{{ site.data.language.enter_search_term }}">
</form>
<noscript>
	Search <a href="https://www.google.com/search?q=site:{{ google_search_site | cgi_escape }}" target="_blank">Google</a> for:
	<pre><code>search-term site:{{ google_search_site }}</code></pre>
</noscript>
