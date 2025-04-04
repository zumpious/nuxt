---
title: "useError"
description: useError Composable gibt den globalen Nuxt-Fehler zurück, der bearbeitet wird.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/error.ts
    size: xs
---

Die Composable gibt den globalen Nuxt-Fehler zurück, der bearbeitet wird und er ist sowohl auf dem Client als auch auf dem Server verfügbar.

```ts
const error = useError()
```

`useError` setzt einen Fehler im State und erstellt eine reaktive sowie SSR-freundliche globale Nuxt-Fehlerübersicht über Komponenten hinweg.

Nuxt-Fehler haben folgende Eigenschaften:

```ts
interface {
  // HTTP-Antwort-Statuscode
  statusCode: number
  // HTTP-Antwort-Statusmeldung
  statusMessage: string
  // Fehlermeldung
  message: string
}
```

:read-more{to="/docs/getting-started/error-handling"}
