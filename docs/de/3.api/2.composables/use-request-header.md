---
title: "useRequestHeader"
description: "Verwenden Sie useRequestHeader, um auf einen bestimmten eingehenden Anforderungsheader zuzugreifen."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts
    size: xs
---

Sie können den eingebauten [`useRequestHeader`](/docs/api/composables/use-request-header)-Komponentenfunktionen verwenden, um in Ihren Seiten, Komponenten und Plugins auf jeden eingehenden Anforderungsheader zuzugreifen.

```ts
// Den Authorization-Anforderungsheader abrufen
const authorization = useRequestHeader('authorization')
```

::tip
Im Browser wird `useRequestHeader` `undefined` zurückgeben.
::

## Beispiel

Mit `useRequestHeader` können wir einfach feststellen, ob ein Benutzer autorisiert ist oder nicht.

Das folgende Beispiel liest den `authorization`-Anforderungsheader, um zu überprüfen, ob eine Person auf ein eingeschränktes Ressource zugreifen kann.

```ts [middleware/authorized-only.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  if (!useRequestHeader('authorization')) {
    return navigateTo('/not-authorized')
  }
})
```