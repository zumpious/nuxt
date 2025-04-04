---
title: 'clearNuxtData'
description: Löscht gespeicherte Daten, den Fehlerzustand und ausstehende Promises von useAsyncData und useFetch.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts
    size: xs
---

::note
Diese Methode ist nützlich, wenn Sie die Datensuchung für eine andere Seite ungültig machen möchten.
::

## Typ

```ts
clearNuxtData (keys?: string | string[] | ((key: string) => boolean)): void
```

## Parameter

* `keys`: Ein oder ein Array von Schlüsseln, die in [`useAsyncData`](/docs/api/composables/use-async-data) verwendet werden, um deren gespeicherte Daten zu löschen. Wenn keine Schlüssel angegeben sind, wird **alle Daten** ungültig gemacht.