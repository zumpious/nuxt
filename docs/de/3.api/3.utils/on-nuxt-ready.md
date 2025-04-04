---
title: "onNuxtReady"
description: Die Composable `onNuxtReady` ermöglicht es, einen Callback auszuführen, nachdem Ihre Anwendung initialisiert wurde.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ready.ts
    size: xs
---

::important
`onNuxtReady` läuft nur auf der Client-Seite. :br
Es ist ideal für den Ausführung von Code, der die Anfängerrendition Ihrer Anwendung nicht blockieren sollte.
::

```ts [plugins/ready.client.ts]
export default defineNuxtPlugin(() => {
  onNuxtReady(async () => {
    const myAnalyticsLibrary = await import('my-big-analytics-library')
    // etwas mit myAnalyticsLibrary tun
  })
})
```

Es ist „sicher“, diesen Code auch nach der Initialisierung Ihrer Anwendung auszuführen. In diesem Fall wird der Code in der nächsten leeren Callback-Iteration ausgeführt.