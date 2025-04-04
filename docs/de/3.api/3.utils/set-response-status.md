---
title: 'setResponseStatus'
description: setResponseStatus legt den statusCode (und optional den statusMessage) der Antwort fest.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts
    size: xs
---

Nuxt bietet Composables und Werkzeuge für eine erste Klasse Server-Side-Rendering Unterstützung.

`setResponseStatus` legt den statusCode (und optional den statusMessage) der Antwort fest.

::important
`setResponseStatus` kann nur im [Nuxt Kontext](/docs/guide/going-further/nuxt-app#der-nuxt-kontext) aufgerufen werden.
::

```js
const event = useRequestEvent()

// event wird im Browser undefiniert sein
if (event) {
  // Setze den Statuscode auf 404 für eine benutzerdefinierte 404 Seite
  setResponseStatus(event, 404)

  // Setze den statusMessage ebenfalls
  setResponseStatus(event, 404, 'Seite nicht gefunden')
}
```

::note
Im Browser hat `setResponseStatus` keine Auswirkungen.
::

:read-more{to="/docs/getting-started/error-handling"}
---