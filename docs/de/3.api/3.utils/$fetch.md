---
title: "$fetch"
description: Nuxt verwendet `ofetch`, um den globalen Hilfesatz `$fetch` für die Ausführung von HTTP-Anfragen verfügbar zu machen.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/entry.ts
    size: xs
---

Nuxt verwendet [ofetch](https://github.com/unjs/ofetch) zum Exponieren des `$fetch`-Hilfesatzes global, damit Sie in Ihrem Vue-App oder API-Pfade HTTP-Anfragen ausführen können.

::tip{icon="i-lucide-rocket"}
Während der Serverseitigen Darstellung wird eine Aufruf `$fetch` zur Abruf Ihrer internen [API-Pfade](/docs/de/guide/directory-structure/server) direkt die zugehörige Funktion aufrufen (das Emulieren einer Anfrage), **erhaltend eine zusätzliche API-Aufruf**.
::

::note{color="blue" icon="i-lucide-info"}
Verwenden Sie `$fetch` in Komponenten ohne Verpackung mit [`useAsyncData`](/docs/de/api/composables/use-async-data), wird das Abrufen der Daten zweimal ausgeführt: einmal auf dem Server und dann erneut auf der Clientseite während der Hydratation, da `$fetch` das Serverzustand nicht an den Client überträgt. Daher wird die Abfrage auf beiden Seiten ausgeführt, da der Client die Daten erneut abrufen muss.
::

## Verwendung

Wir empfehlen, entweder [`useFetch`](/docs/de/api/composables/use-fetch) oder [`useAsyncData`](/docs/de/api/composables/use-async-data) + `$fetch` zu verwenden, um das Duplikat der Datenabfrage zu vermeiden, wenn Sie die Komponentendaten abrufen.

```vue [app.vue]
<script setup lang="ts">
// Während der SSR werden die Daten zweimal abgerufen, einmal auf dem Server und einmal auf der Clientseite.
const dataTwice = await $fetch('/api/item')

// Während der SSR werden die Daten nur auf der Serverseite abgerufen und an den Client übertragen.
const { data } = await useAsyncData('item', () => $fetch('/api/item'))

// Sie können auch `useFetch` als Kürzel für `useAsyncData` + `$fetch` verwenden.
const { data } = await useFetch('/api/item')
</script>
```

:read-more{to="/docs/de/getting-started/data-fetching"}

Sie können `$fetch` in beliebigen Methoden verwenden, die nur auf der Clientseite ausgeführt werden.

```vue [pages/contact.vue]
<script setup lang="ts">
async function contactForm() {
  await $fetch('/api/contact', {
    method: 'POST',
    body: { hello: 'world' }
  })
}
</script>

<template>
  <button @click="contactForm">Kontaktieren</button>
</template>
```

::tip
`$fetch` ist die bevorzugte Methode zur Ausführung von HTTP-Aufrufen in Nuxt anstelle von [@nuxt/http](https://github.com/nuxt/http) und [@nuxtjs/axios](https://github.com/nuxt-community/axios-module), die für Nuxt 2 entwickelt wurden.
::

::note
Wenn Sie `$fetch` verwenden, um einen (externen) HTTPS-URL mit einem selbstsignierten Zertifikat in der Entwicklung aufzurufen, müssen Sie `NODE_TLS_REJECT_UNAUTHORIZED=0` in Ihrer Umgebung festlegen.
::

### Übergeben von Headers und Cookies

Wenn wir `$fetch` im Browser aufrufen, werden Benutzerheaders wie `cookie` direkt an die API gesendet.

Allerdings während der Serverseitigen Darstellung, aufgrund von Sicherheitsrisiken wie **Server-Side Request Forgery (SSRF)** oder **Authentication Misuse**, wird `$fetch` keine Benutzer-Cookies übermitteln und Cookies aus der Antwort der Abfrage nicht weiterleiten.

::code-group

```vue [pages/index.vue]
<script setup lang="ts">
// Dies wird während der SSR keine Headers oder Cookies weiterleiten
const { data } = await useAsyncData(() => $fetch('/api/cookies'))
</script>
```

```ts [server/api/cookies.ts]
export default defineEventHandler((event) => {
  const foo = getCookie(event, 'foo')
  // ... Führen Sie etwas mit dem Cookie aus
})
```
::

Wenn Sie auf dem Server Cookies und Headers weiterleiten müssen, müssen Sie sie manuell übermitteln:

```vue [pages/index.vue]
<script setup lang="ts">
// Dies wird die Benutzer-Header und Cookies an `/api/cookies` weiterleiten
const requestFetch = useRequestFetch()
const { data } = await useAsyncData(() => requestFetch('/api/cookies'))
</script>
```

Allerdings, wenn Sie `useFetch` mit einer relativen URL auf dem Server aufrufen, verwendet Nuxt [`useRequestFetch`](/docs/de/api/composables/use-request-fetch) zum Proxyieren von Headers und Cookies (mit Ausnahme von Headers, die nicht weitergeleitet werden sollen, wie `host`).
::