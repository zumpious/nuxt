---
title: 'setPageLayout'
description: setPageLayout ermöglicht es Ihnen, die Layoutstruktur einer Seite dynamisch zu ändern.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts
    size: xs
---

::important
`setPageLayout` ermöglicht es Ihnen, die Layoutstruktur einer Seite dynamisch zu ändern. Es basiert auf dem Zugriff auf den Nuxt-Kontext und kann daher nur innerhalb des [Nuxt-Kontexts](/docs/de/guide/going-further/nuxt-app#der-nuxt-kontext) aufgerufen werden.
::

```ts [middleware/custom-layout.ts]
export default defineNuxtRouteMiddleware((to) => {
  // Setze das Layout auf der Seite, auf die du navigierst
  setPageLayout('other')
})
```

::note
Wenn Sie das Layout dynamisch auf der Serverseite festlegen, müssen Sie dies vor der Darstellung durch Vue (d.h., innerhalb eines Plugins oder eines Routen-Middlewares) tun, um eine Hydrationsungleichheit zu vermeiden.
::
```