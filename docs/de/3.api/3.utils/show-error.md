---
title: 'showError'
description: Nuxt bietet eine schnelle und einfache Möglichkeit, eine vollbildige Fehlerseite anzuzeigen, falls erforderlich.
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/error.ts
    size: xs
---

Innerhalb des [Nuxt-Kontexts](/docs/guide/going-further/nuxt-app#der-nuxt-kontext) kannst du `showError` verwenden, um einen Fehler anzuzeigen.

**Parameter:**

- `error`: `string | Error | Partial<{ cause, data, message, name, stack, statusCode, statusMessage }>`
  
```ts
showError("😱 Ohne, ein Fehler ist aufgetreten.")
showError({
  statusCode: 404,
  statusMessage: "Seite nicht gefunden"
})
```

Der Fehler wird im Zustand mit der Komponente `useError()` gesetzt, um eine reaktive und SSR-freundliche gemeinsame Fehlerzustandsvariable für Komponenten zu erstellen.

::tip
`showError` ruft das `app:error` Hook auf.
::

:read-more{to="/docs/getting-started/error-handling"}
---