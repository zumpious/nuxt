---
title: 'useLazyFetch'
description: Dieser Wrapper um `useFetch` führt die Navigierung sofort aus.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/fetch.ts
    size: xs
---

## Beschreibung

Standardmäßig blockiert `useFetch` (`/docs/api/composables/use-fetch`) die Navigierung, bis der asynchrone Handler aufgelöst ist. `useLazyFetch` bietet einen Wrapper um `useFetch`, der die Navigierung vor der Auflösung des Handlers durch Festlegen der Option `lazy` auf `true` auslöst.

::note
`useLazyFetch` hat die gleiche Signatur wie `useFetch` (`/docs/api/composables/use-fetch`).
::

::note
Das Warten auf `useLazyFetch` in diesem Modus stellt sicher, dass die Anfrage initialisiert wird. Bei clientseitiger Navigierung kann die Daten nicht unmittelbar verfügbar sein, und Sie sollten im App die Ausstehende Zustand verwalten.
::

:read-more{to="/docs/api/composables/use-fetch"}

## Beispiel

```vue [pages/index.vue]
<script setup lang="ts">
/* Die Navigierung erfolgt bevor das Abrufen abgeschlossen ist.
 * Behandeln Sie den 'pending' und 'error'-Zustand direkt in Ihrem Komponenten-Template
 */
const { status, data: posts } = await useLazyFetch('/api/posts')
watch(posts, (newPosts) => {
  // Da posts möglicherweise null beginnt, haben Sie zunächst keinen Zugriff
  // auf seine Inhalte, aber Sie können ihn beobachten.
})
</script>

<template>
  <div v-if="status === 'pending'">
    Lade ...
  </div>
  <div v-else>
    <div v-for="post in posts">
      <!-- Führen Sie etwas aus -->
    </div>
  </div>
</template>
```

::note
`useLazyFetch` ist eine reservierte Funktionsnamen, der vom Compiler transformiert wird, daher sollten Sie Ihre eigene Funktion nicht `useLazyFetch` nennen.
::

:read-more{to="/docs/getting-started/data-fetching"}