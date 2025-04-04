---
title: 'preloadRouteComponents'
description: preloadRouteComponents ermöglicht es Ihnen, einzelne Seiten in Ihrem Nuxt-App manuell vorab zu laden.
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/preload.ts
    size: xs
---

Vorbeladen werden die Komponenten einer gegebenen Route, die der Benutzer zukünftig navigieren könnte. Dies stellt sicher, dass die Komponenten früher verfügbar sind und weniger wahrscheinlich den Navigationsschritt blockieren, was die Leistung verbessert.

::tip{icon="i-lucide-rocket"}
Nuxt vorab lädt bereits die notwendigen Routen automatisch, wenn Sie den `NuxtLink`-Komponenten verwenden.
::

:read-more{to="/docs/api/components/nuxt-link"}

## Beispiel

Lade eine Route beim Verwenden von `navigateTo` vor.

```ts
// wir warten nicht auf diese asynchrone Funktion, um das Blockieren des Renderings zu vermeiden
// die Setup-Funktion dieser Komponente
preloadRouteComponents('/dashboard')

const submit = async () => {
  const results = await $fetch('/api/authentication')

  if (results.token) {
    await navigateTo('/dashboard')
  }
}
```

:read-more{to="/docs/api/utils/navigate-to"}

::note
Auf dem Server hat `preloadRouteComponents` keine Auswirkungen.
::
---