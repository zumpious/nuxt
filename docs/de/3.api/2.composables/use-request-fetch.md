---
title: 'useRequestFetch'
description: 'Forwarde die Request-Kontext und Header für Serverseitige Fetch-Anfragen mit dem Composable useRequestFetch.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts
    size: xs
---

Sie können `useRequestFetch` verwenden, um die Request-Kontext und Header bei der Ausführung von Serverseitigen Fetch-Anfragen weiterzuleiten.

Wenn Sie eine Clientseitige Fetch-Anfrage ausführen, sendet der Browser automatisch die notwendigen Headers.
Bei der Ausführung einer Anfrage während des Serverseitigen Renderings müssen wir jedoch die Headers manuell weiterleiten, aus Sicherheitsgründen.

::note
Headers, die **nicht weitergeleitet** werden sollen, **werden nicht in der Anfrage enthalten** sein. Diese Headers beinhalten z.B.:
`transfer-encoding`, `connection`, `keep-alive`, `upgrade`, `expect`, `host`, `accept`
::

::tip
Der Composable [`useFetch`](/docs/api/composables/use-fetch) verwendet `useRequestFetch` unter der Haube, um die Request-Kontext und Header automatisch weiterzuleiten.
::

::code-group

```vue [pages/index.vue]
<script setup lang="ts">
// Dies wird die Headers des Benutzers an den `/api/cookies` Event Handler weiterleiten
// Ergebnis: { cookies: { foo: 'bar' } }
const requestFetch = useRequestFetch()
const { data: forwarded } = await useAsyncData(() => requestFetch('/api/cookies'))

// Dies wird nichts weiterleiten
// Ergebnis: { cookies: {} }
const { data: notForwarded } = await useAsyncData(() => $fetch('/api/cookies')) 
</script>
```

```ts [server/api/cookies.ts]
export default defineEventHandler((event) => {
  const cookies = parseCookies(event)

  return { cookies }
})
```

::

::tip
Im Browser während der Clientseitigen Navigation wird `useRequestFetch` genau so wie das reguläre [`$fetch`](/docs/api/utils/dollarfetch) verhalten.
::


Bitte beachten Sie, dass die Übersetzung der Dokumentationstexte in den Links und Codebeispielen korrekt beibehalten wurde, während der Rest des Textes ins Deutsche übersetzt wurde.