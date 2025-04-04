---
title: "useResponseHeader"
description: "Verwenden Sie useResponseHeader, um einen Server-Antwortheader zu setzen."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts
    size: xs
---

::important
Diese Komponente ist ab Nuxt v3.14 verfügbar.
::

Sie können den eingebaute [`useResponseHeader`](/docs/api/composables/use-response-header) Komponentenmäßigen zu verwenden, um einen Server-Antwortheader innerhalb Ihrer Seiten, Komponenten und Plugins zu setzen.

```ts
// Ein benutzerdefinierter Antwortheader setzen
const header = useResponseHeader('X-My-Header');
header.value = 'my-value';
```

## Beispiel

Wir können `useResponseHeader` verwenden, um einen Antwortheader auf einer pro-Seite Basis einfach zu setzen.

```vue [pages/test.vue]
<script setup>
// pages/test.vue
const header = useResponseHeader('X-My-Header');
header.value = 'my-value';
</script>

<template>
  <h1>Testseite mit benutzerdefiniertem Header</h1>
  <p>Die Antwort vom Server für diese "/test" Seite wird einen benutzerdefinierten "X-My-Header" Header haben.</p>
</template>
```

Wir können `useResponseHeader` z.B. in Nuxt [Middleware](/docs/guide/directory-structure/middleware) verwenden, um einen Antwortheader für alle Seiten zu setzen.

```ts [middleware/my-header-middleware.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const header = useResponseHeader('X-My-Always-Header');
  header.value = `Ich bin immer hier!`;
});
```