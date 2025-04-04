---
title: 'defineRouteRegeln'
description: 'Definieren Sie Route-Regeln für hybrides Rendering auf der Seite Ebene.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/pages/runtime/composables.ts
    size: xs
---

::read-more{to="/docs/de/handleiding/weitergehen/experimentale-merkmale#inline-routeregeln" icon="i-lucide-star"}
Diese Funktion ist experimentell und um sie zu verwenden, müssen Sie die Option `experimental.inlineRouteRegeln` in Ihrem `nuxt.config` aktivieren.
::

## Verwendung

```vue [pages/index.vue]
<script setup lang="ts">
defineRouteRules({
  prerender: true
})
</script>

<template>
  <h1>Hello world!</h1>
</template>
```

Wird übersetzt zu:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  routeRules: {
    '/': { prerender: true }
  }
})
```

::note
Wenn Sie [`nuxt build`](/docs/de/api/befehle/build) ausführen, wird die Startseite im `.output/public/index.html` vorab gerendert und statisch angeboten.
::

## Hinweise

- Eine Regel, die in `~/pages/foo/bar.vue` definiert ist, wird auf Anfragen nach `/foo/bar` angewendet.
- Eine Regel in `~/pages/foo/[id].vue` wird auf Anfragen nach `/foo/**` angewendet.

Für mehr Kontrolle, z.B. wenn Sie eine benutzerdefinierte `path` oder `alias` in der Seiten-[`definePageMeta`](/docs/de/api/utils/define-page-meta) festgelegt haben, sollten Sie `routeRules` direkt in Ihrem `nuxt.config` setzen.

::read-more{to="/docs/de/handleiding/konzepte/rendering#hybrides-rendering" icon="i-lucide-medal"}
Lesen Sie mehr über die `routeRules`.
::