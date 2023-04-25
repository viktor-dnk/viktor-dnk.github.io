﻿/*! head.load - v1.0.3 */
!function(e,t){var n,a=e.document,r=[],o={},u={},l="async"in a.createElement("script")||"MozAppearance"in a.documentElement.style||e.opera,c=e.head_conf&&e.head_conf.head||"head",i=e[c]=e[c]||function(){i.ready.apply(null,arguments)},s=1,d=2,f=3,p=4;function y(){}function m(e,t){if(e){"object"==typeof e&&(e=[].slice.call(e));for(var n=0,a=e.length;n<a;n++)t.call(e,e[n],n)}}function h(e,n){var a=Object.prototype.toString.call(n).slice(8,-1);return n!==t&&null!==n&&a===e}function v(e){return h("Function",e)}function g(e){return h("Array",e)}function T(e){(e=e||y)._done||(e(),e._done=1)}function E(e){var t,n,a,r,o={};if("object"==typeof e)for(var l in e)e[l]&&(o={name:l,url:e[l]});else o={name:(t=e,n=t.split("/"),a=n[n.length-1],r=a.indexOf("?"),-1!==r?a.substring(0,r):a),url:e};var c=u[o.name];return c&&c.url===o.url?c:(u[o.name]=o,o)}function L(e){for(var t in e=e||u)if(e.hasOwnProperty(t)&&e[t].state!==p)return!1;return!0}function b(e,n){e.state===t&&(e.state=s,e.onpreload=[],j({url:e.url,type:"cache"},(function(){!function(e){e.state=d,m(e.onpreload,(function(e){e.call()}))}(e)})))}function S(e,t){t=t||y,e.state!==p?e.state!==f?e.state!==s?(e.state=f,j(e,(function(){e.state=p,t(),m(o[e.name],(function(e){T(e)})),n&&L()&&m(o.ALL,(function(e){T(e)}))}))):e.onpreload.push((function(){S(e,t)})):i.ready(e.name,t):t()}function j(t,n){function r(t){t=t||e.event,u.onload=u.onreadystatechange=u.onerror=null,n()}function o(r){("load"===(r=r||e.event).type||/loaded|complete/.test(u.readyState)&&(!a.documentMode||a.documentMode<9))&&(e.clearTimeout(t.errorTimeout),e.clearTimeout(t.cssTimeout),u.onload=u.onreadystatechange=u.onerror=null,n())}var u,l,c;n=n||y,"css"===(l=t.url,(c=(l=l||"").split("?")[0].split("."))[c.length-1].toLowerCase())?((u=a.createElement("link")).type="text/"+(t.type||"css"),u.rel="stylesheet",u.href=t.url,t.cssRetries=0,t.cssTimeout=e.setTimeout((function n(){if(t.state!==p&&t.cssRetries<=20){for(var r=0,l=a.styleSheets.length;r<l;r++)if(a.styleSheets[r].href===u.href)return void o({type:"load"});t.cssRetries++,t.cssTimeout=e.setTimeout(n,250)}}),500)):((u=a.createElement("script")).type="text/"+(t.type||"javascript"),u.src=t.url),u.onload=u.onreadystatechange=o,u.onerror=r,u.async=!1,u.defer=!1,t.errorTimeout=e.setTimeout((function(){r({type:"timeout"})}),7e3);var i=a.head||a.getElementsByTagName("head")[0];i.insertBefore(u,i.lastChild)}function A(){if(!a.body)return e.clearTimeout(i.readyTimeout),void(i.readyTimeout=e.setTimeout(A,50));n||(n=!0,function(){for(var e=a.getElementsByTagName("script"),t=0,n=e.length;t<n;t++){var r=e[t].getAttribute("data-headjs-load");if(r)return void i.load(r)}}(),m(r,(function(e){T(e)})))}function M(){a.addEventListener?(a.removeEventListener("DOMContentLoaded",M,!1),A()):"complete"===a.readyState&&(a.detachEvent("onreadystatechange",M),A())}if("complete"===a.readyState)A();else if(a.addEventListener)a.addEventListener("DOMContentLoaded",M,!1),e.addEventListener("load",A,!1);else{a.attachEvent("onreadystatechange",M),e.attachEvent("onload",A);var O=!1;try{O=!e.frameElement&&a.documentElement}catch(e){}O&&O.doScroll&&function t(){if(!n){try{O.doScroll("left")}catch(n){return e.clearTimeout(i.readyTimeout),void(i.readyTimeout=e.setTimeout(t,50))}A()}}()}i.load=i.js=l?function(){var e=arguments,t=e[e.length-1],n={};return v(t)||(t=null),g(e[0])?(e[0].push(t),i.load.apply(null,e[0]),i):(m(e,(function(e,a){e!==t&&(e=E(e),n[e.name]=e)})),m(e,(function(e,a){e!==t&&S(e=E(e),(function(){L(n)&&T(t)}))})),i)}:function(){var e=arguments,t=e[e.length-1],n=[].slice.call(e,1),a=n[0];return v(t)||(t=null),g(e[0])?(e[0].push(t),i.load.apply(null,e[0]),i):(a?(m(n,(function(e){!v(e)&&e&&b(E(e))})),S(E(e[0]),v(a)?a:function(){i.load.apply(null,n)})):S(E(e[0])),i)},i.test=function(e,t,n,a){var r="object"==typeof e?e:{test:e,success:!!t&&(g(t)?t:[t]),failure:!!n&&(g(n)?n:[n]),callback:a||y},o=!!r.test;return o&&r.success?(r.success.push(r.callback),i.load.apply(null,r.success)):!o&&r.failure?(r.failure.push(r.callback),i.load.apply(null,r.failure)):a(),i},i.ready=function(e,t){if(e===a)return n?T(t):r.push(t),i;if(v(e)&&(t=e,e="ALL"),g(e)){var l={};return m(e,(function(e){l[e]=u[e],i.ready(e,(function(){L(l)&&T(t)}))})),i}if("string"!=typeof e||!v(t))return i;var c=u[e];if(c&&c.state===p||"ALL"===e&&L()&&n)return T(t),i;var s=o[e];return s?s.push(t):s=o[e]=[t],i},i.ready(a,(function(){L()&&m(o.ALL,(function(e){T(e)})),i.feature&&i.feature("domloaded",!0)}))}(window);