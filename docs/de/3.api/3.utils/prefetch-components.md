---
title: 'prefetchComponents'
description: Nuxt bietet Werkzeuge, um die Kontrolle über das Vorabladen von Komponenten zu gewähren.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/preload.ts
    size: xs
---

Das Vorabladen von Komponenten herunterlädt den Code im Hintergrund. Dies basiert auf der Annahme, dass die Komponente wahrscheinlich für die Darstellung verwendet wird. Dadurch kann die Komponente bei Bedarf sofort geladen werden, wenn der Benutzer sie anfordert. Die Komponente wird heruntergeladen und gespeichert, ohne dass der Benutzer explizit danach verlangt.

Verwenden Sie `prefetchComponents`, um individuelle Komponenten, die global in Ihrem Nuxt-App registriert sind, manuell vorabzuladen. Standardmäßig registriert Nuxt diese als asynchrone Komponenten. Sie müssen den Pascal-cased-Namen der Komponente verwenden.

```ts
await prefetchComponents('MyGlobalComponent')

await prefetchComponents(['MyGlobalComponent1', 'MyGlobalComponent2'])
```

::note
Die aktuelle Implementierung verhält sich genauso wie [`preloadComponents`](/docs/api/utils/preload-components), indem sie Komponenten vorab lädt und nicht nur vorablädet, arbeiten wir daran, dieses Verhalten zu verbessern.
::

::note
Auf dem Server hat `prefetchComponents` keine Auswirkungen.
::
