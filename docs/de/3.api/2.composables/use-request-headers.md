---
title: "useRequestHeaders"
description: "Verwenden Sie useRequestHeaders, um die eingehenden Anforderungsheader zu accessed."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts
    size: xs
---

Sie können den eingebauten [`useRequestHeaders`](/docs/api/composables/use-request-headers) Komponenten zu verwenden, um die eingehenden Anforderungsheader innerhalb Ihrer Seiten, Komponenten und Plugins zu accessen.

```js
// Alle Anforderungsheader abrufen
const headers = useRequestHeaders()

// Nur den Cookie-Anforderungsheader abrufen
const headers = useRequestHeaders(['cookie'])
```

::tip
Im Browser wird `useRequestHeaders` ein leeres Objekt zurückgeben.
::

## Beispiel

Wir können `useRequestHeaders` verwenden, um den `authorization`-Anforderungsheader der ursprünglichen Anfrage während der SSR an jede zukünftige interne Anfrage zu proxyieren.

Das folgende Beispiel fügt den `authorization`-Anforderungsheader einer isomorphen `$fetch`-Aufruf hinzu.

```vue [pages/some-page.vue]
<script setup lang="ts">
const { data } = await useFetch('/api/confidential', {
  headers: useRequestHeaders(['authorization'])
})
</script>
```