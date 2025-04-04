---
title: 'useRequestURL'
description: 'Zugriff auf den eingehenden Anfrage-URL mit der Composable useRequestURL.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/url.ts
    size: xs
---

`useRequestURL` ist ein Hilfsfunktion, die eine [URL-Objekt](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) zurückgibt, das sowohl auf dem Server- als auch auf dem Clientseiten funktioniert.

::important
Wenn Sie [Hybrid Rendering](/docs/de/guide/concepts/rendering#hybrid-rendering) mit Cache-Strategien verwenden, werden alle eingehenden Anfrageheaders, wenn die Antworten über die [Nitro-Cacheschicht](https://nitro.unjs.io/de/guide/cache) gehandhabt werden, ignoriert (was bedeutet, dass `useRequestURL` für den `host` `localhost` zurückgibt).

Sie können die Option [`cache.varies`](https://nitro.unjs.io/de/guide/cache#options) definieren, um Header zu spezifizieren, die bei der Caching und Bereitstellung der Antworten berücksichtigt werden sollen, wie z.B. `host` und `x-forwarded-host` für Mehrmietumgebungen.
::

::code-group

```vue [pages/about.vue]
<script setup lang="ts">
const url = useRequestURL()
</script>

<template>
  <p>URL ist: {{ url }}</p>
  <p>Pfad ist: {{ url.pathname }}</p>
</template>
```

```html [Ergebnis im Entwicklungsmodus]
<p>URL ist: http://localhost:3000/about</p>
<p>Pfad ist: /about</p>
```

::

::tip{icon="i-simple-icons-mdnwebdocs" to="https://developer.mozilla.org/en-US/docs/Web/API/URL#instance_properties" target="_blank"}
Lesen Sie mehr über die Instanz Eigenschaften von URL auf der Dokumentation von MDN.
::


Bitte beachten Sie, dass die URLs nicht übersetzt wurden, da sie unverändert bleiben sollten.