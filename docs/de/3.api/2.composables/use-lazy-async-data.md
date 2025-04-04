---
title: useLazyAsyncData
description: Dieser Wrapper um `useAsyncData` startet die Navigation sofort.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts
    size: xs
---

## Beschreibung

Standardmäßig blockiert `useAsyncData` (`/docs/api/composables/use-async-data`) die Navigation, bis der asynchrone Handler aufgelöst ist. `useLazyAsyncData` bietet einen Wrapper um `useAsyncData`, der die Navigation vor der Auflösung des Handlers durch Festlegen der Option `lazy` auf `true` startet.

::note
`useLazyAsyncData` hat die gleiche Signatur wie `useAsyncData` (`/docs/api/composables/use-async-data`).
::

:read-more{to="/docs/api/composables/use-async-data"}

## Beispiel

```vue [pages/index.vue]
<script setup lang="ts">
/* Die Navigation wird bevor das Abrufen abgeschlossen ist.
   Bearbeiten Sie direkt im Template die 'pending' und 'error' Zustände
*/
const { status, data: count } = await useLazyAsyncData('count', () => $fetch('/api/count'))

watch(count, (newCount) => {
  // Da count möglicherweise null beginnt, haben Sie nicht sofort Zugriff
  // auf seine Inhalte, aber Sie können es beobachten.
})
</script>

<template>
  <div>
    {{ status === 'pending' ? 'Laden...' : count }}
  </div>
</template>
```

::warning
`useLazyAsyncData` ist eine reservierte Funktionsnamen, die vom Compiler transformiert wird, daher sollten Sie Ihre eigene Funktion nicht `useLazyAsyncData` nennen.
::

:read-more{to="/docs/getting-started/data-fetching"}