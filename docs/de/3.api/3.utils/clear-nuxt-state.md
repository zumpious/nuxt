---
title: 'clearNuxtState'
description: Lösche den gespeicherten Zustand von useState.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/state.ts
    size: xs
---

::note
Diese Methode ist nützlich, wenn Sie den Zustand von `useState` ungültig machen möchten.
::

## Typ

```ts
clearNuxtState (keys?: string | string[] | ((key: string) => boolean)): void
```

## Parameter

- `keys`: Ein oder eine Array von Schlüsseln, die im[`useState`](/docs/api/composables/use-state) verwendet werden, um deren gespeicherten Zustand zu löschen. Wenn keine Schlüssel angegeben sind, wird **alle Zustände** ungültig gemacht.