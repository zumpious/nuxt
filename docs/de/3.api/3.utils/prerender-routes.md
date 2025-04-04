---
title: 'prerenderRoutes'
description: prerenderRoutes weist Nitro darauf hin, eine zusätzliche Route vorab zu rendern.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts
    size: xs
---

Während des Vorabrenderings können Sie Nitro dazu hinweisen, zusätzliche Pfade vorab zu rendern, auch wenn ihre URLs im HTML der generierten Seite nicht angezeigt werden.

::important
`prerenderRoutes` kann nur innerhalb des [Nuxt-Kontexts](/docs/guide/going-further/nuxt-app#the-nuxt-context) aufgerufen werden.
::

::note
`prerenderRoutes` muss während des Vorabrenderings ausgeführt werden. Wenn `prerenderRoutes` in dynamischen Seiten/Routen verwendet wird, die nicht vorab gerendert werden, wird es nicht ausgeführt.
::

```js
const route = useRoute()

prerenderRoutes('/')
prerenderRoutes(['/', '/about'])
```

::note
Im Browser oder außerhalb des Vorabrenderings hat `prerenderRoutes` keine Auswirkungen.
::

Sie können sogar API-Routen vorab rendern, was besonders für vollständig statisch generierte Seiten (SSG) nützlich ist, da Sie dann Daten mit `$fetch` abrufen können, als ob ein Server verfügbar wäre!

```js
prerenderRoutes('/api/content/article/name-of-article')

// Später im App
const articleContent = await $fetch('/api/content/article/name-of-article', {
  responseType: 'json',
})
```

::warning
Vorab gerenderte API-Routen in der Produktion können je nach dem Provider, zu dem Sie bereitgestellt werden, nicht die erwarteten Antwortheaders zurückgeben. Zum Beispiel könnte eine JSON-Antwort mit einem `application/octet-stream` Content-Type serviert werden.
Setzen Sie immer `responseType` manuell, wenn Sie vorab gerenderte API-Routen abrufen.
::
---