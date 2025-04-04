---
title: 'updateAppConfig'
description: 'Aktualisieren des App Configs laufzeitweise.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/config.ts
    size: xs
---

::note
Aktualisiert das `app.config` ([/docs/guide/directory-structure/app-config](/docs/guide/directory-structure/app-config)) mithilfe von tiefem Zuweisung. Bestehende (verkettete) Eigenschaften werden beibehalten.
::

## Verwendung

```js
const appConfig = useAppConfig() // { foo: 'bar' }

const newAppConfig = { foo: 'baz' }

updateAppConfig(newAppConfig)

console.log(appConfig) // { foo: 'baz' }
```

:read-more{to="/docs/guide/directory-structure/app-config"}