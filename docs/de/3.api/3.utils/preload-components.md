---
title: 'preloadComponents'
description: Nuxt bietet Werkzeuge, um die Vorladung von Komponenten zu steuern.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/preload.ts
    size: xs
---

Komponenten vorladen lädt Komponenten, die Ihre Seite sehr bald benötigen, frühzeitig bei der Rendering-Lebenszyklusphase. Dies stellt sicher, dass sie früher verfügbar sind und weniger wahrscheinlich das Rendering der Seite blockieren, was die Leistung verbessert.

Verwenden Sie `preloadComponents`, um individuelle Komponenten manuell vorzuladen, die in Ihrem Nuxt-App global registriert wurden. Standardmäßig registriert Nuxt diese als asynchrone Komponenten. Sie müssen den Pascal-cased-Namen der Komponente verwenden.

```js
await preloadComponents('MyGlobalComponent')

await preloadComponents(['MyGlobalComponent1', 'MyGlobalComponent2'])
```

::note
Auf dem Server hat `preloadComponents` keine Auswirkungen.
::
---