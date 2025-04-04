---
title: 'useRequestEvent'
description: 'Zugriff auf den eingehenden Anfrageereignis mit der Composable useRequestEvent.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts
    size: xs
---

Innerhalb des [Nuxt-Kontexts](/docs/guide/going-further/nuxt-app#der-nuxt-kontext) können Sie `useRequestEvent` verwenden, um auf das eingehende Anfrageereignis zuzugreifen.

```ts
// Das zugrunde liegende Anfrageereignis abrufen
const event = useRequestEvent()

// Die URL abrufen
const url = event?.path
```

::tip
Im Browser wird `useRequestEvent` `undefined` zurückgeben.
::
---