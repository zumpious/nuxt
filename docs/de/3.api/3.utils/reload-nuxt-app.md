---
title: 'reloadNuxtApp'
description: reloadNuxtApp wird eine harte Neuladung der Seite durchführen.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/chunk.ts
    size: xs
---

::note
`reloadNuxtApp` wird eine harte Neuladung deiner Anwendung durchführen, indem sie die Seite und ihre Abhängigkeiten erneut vom Server anfordert.
::

Standardmäßig wird auch das aktuelle `State` deiner Anwendung gespeichert (das bedeutet, dass du dieses State mit `useState` erreichen kannst).

::read-more{to="/docs/guide/going-further/experimental-features#restorestate" icon="i-lucide-star"}
Du kannst das experimentelle Wiederherstellen dieses States aktivieren, indem du die Option `experimental.restoreState` in deinem `nuxt.config`-Datei aktivierst.
::

## Typ

```ts
reloadNuxtApp(options?: ReloadNuxtAppOptions)

interface ReloadNuxtAppOptions {
  ttl?: number
  force?: boolean
  path?: string
  persistState?: boolean
}
```

### `options` (optional)

**Typ**: `ReloadNuxtAppOptions`

Ein Objekt, das die folgenden Eigenschaften akzeptiert:

- `path` (optional)

  **Typ**: `string`

  **Standardwert**: `window.location.pathname`

  Die zu neuladende Pfadangabe (standardmäßig der aktuelle Pfad). Wenn dieser von der aktuellen Fensterposition abweicht, wird eine Navigation ausgelöst und ein Eintrag in der Browserhistorie hinzugefügt.

- `ttl` (optional)

  **Typ**: `number`

  **Standardwert**: `10000`

  Die Anzahl der Millisekunden, in denen zukünftige Neuladefordernisse ignoriert werden sollen. Wenn innerhalb dieser Zeit wieder aufgerufen wird, wird `reloadNuxtApp` deine Anwendung nicht neu laden, um Neuladeloopen zu vermeiden.

- `force` (optional)

  **Typ**: `boolean`

  **Standardwert**: `false`

  Diese Option ermöglicht es, die Neuladeloopen-Schutzfunktion komplett zu umgehen und eine Neuladung trotz einer vorherigen Neuladung innerhalb des angegebenen TTL-Zeitraums zu erzwingen.

- `persistState` (optional)

  **Typ**: `boolean`

  **Standardwert**: `false`

  Ob das aktuelle Nuxt-State in sessionStorage gespeichert werden soll (als `nuxt:reload:state`). Standardmäßig hat dies keine Auswirkungen auf die Neuladung, es sei denn, `experimental.restoreState` ist ebenfalls gesetzt oder du handelsweise das State wiederherstellen möchtest.