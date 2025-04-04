---
title: "clearError"
description: "Das clearError-Komponentenrätsel löscht alle behandelten Fehler."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/error.ts
    size: xs
---

Innerhalb Ihrer Seiten, Komponenten und Plugins können Sie `clearError` verwenden, um alle Fehler zu löschen und den Benutzer zurückschicken.

**Parameter:**

- `options?: { redirect?: string }`

Sie können eine optionale Pfadangabe für einen Schaltungswechsel bereitstellen (zum Beispiel, wenn Sie zu einer sicheren Seite navigieren möchten).

```js
// Ohne Schaltungswechsel
clearError()

// Mit Schaltungswechsel
clearError({ redirect: '/homepage' })
```

Fehler werden im Zustand mit der Funktion [`useError()`](/docs/api/composables/use-error) gesetzt. Das clearError-Komponentenrätsel setzt diesen Zustand zurück und ruft das `app:error:cleared` Hook mit den bereitgestellten Optionen auf.

:read-more{to="/docs/getting-started/error-handling"}
---