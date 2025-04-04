---
title: 'refreshNuxtData'
description: Aktualisieren aller oder spezifischer asyncData-Instanzen in Nuxt
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts
    size: xs
---

`refreshNuxtData` wird verwendet, um alle oder spezifische `asyncData`-Instanzen neu abzurufen, einschließlich jener von [`useAsyncData`](/docs/api/composables/use-async-data), [`useLazyAsyncData`](/docs/api/composables/use-lazy-async-data), [`useFetch`](/docs/api/composables/use-fetch) und [`useLazyFetch`](/docs/api/composables/use-lazy-fetch).

::note
Wenn Ihr Komponenten durch `<KeepAlive>` gespeichert werden und inaktiv sind, werden die `asyncData`-Instanzen innerhalb der Komponente bis zur Entfernung der Komponente noch einmal abgerufen.
::

## Typ

```ts
refreshNuxtData(keys?: string | string[])
```

## Parameter

* `keys`: Ein einzelner String oder ein Array von Strings als `keys`, die zum Abrufen der Daten verwendet werden. Dieser Parameter ist **optional**. Alle [`useAsyncData`](/docs/api/composables/use-async-data) und [`useFetch`](/docs/api/composables/use-fetch) `keys` werden neu abgerufen, wenn keine expliziten `keys` angegeben sind.

## Rückgabewerte

`refreshNuxtData` gibt eine Promise zurück, die sich auflöst, wenn alle oder spezifische `asyncData`-Instanzen aktualisiert wurden.

## Beispiele

### Alle Daten neu abrufen

Das folgende Beispiel zeigt, wie alle Daten, die mit `useAsyncData` und `useFetch` in einer Nuxt-Anwendung abgerufen werden, neu abgerufen werden.

```vue [pages/some-page.vue]
<script setup lang="ts">
const refreshing = ref(false)

async function refreshAll () {
  refreshing.value = true
  try {
    await refreshNuxtData()
  } finally {
    refreshing.value = false
  }
}
</script>

<template>
  <div>
    <button :disabled="refreshing" @click="refreshAll">
      Alle Daten neu abrufen
    </button>
  </div>
</template>
```

### Spezifische Daten neu abrufen

Das folgende Beispiel zeigt, wie nur die Daten neu abgerufen werden, deren Schlüssel `count` und `user` entsprechen.

```vue [pages/some-page.vue]
<script setup lang="ts">
const refreshing = ref(false)

async function refresh () {
  refreshing.value = true
  try {
    // Du kannst auch ein Array von Schlüsseln übergeben, um mehrere Daten gleichzeitig zu aktualisieren
    await refreshNuxtData(['count', 'user'])
  } finally {
    refreshing.value = false
  }
}
</script>

<template>
  <div v-if="refreshing">
    Laden
  </div>
  <button @click="refresh">Neu abrufen</button>
</template>
```

::note
Wenn Sie Zugriff auf die `asyncData`-Instanz haben, wird empfohlen, ihre `refresh` oder `execute` Methode zu verwenden, um die Daten neu abzurufen.
::

:read-more{to="/docs/getting-started/data-fetching"}
---