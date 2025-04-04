---
title: 'useHydration'
description: 'Bietet volle Kontrolle über den Hydrationszyklus, um Daten vom Server zu setzen und abzurufen.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/hydrate.ts
    size: xs
---

::note
Dies ist ein fortgeschrittenes Komponentenfunktionalität und wird hauptsächlich von Nuxt-Modulen verwendet.
::

::note
`useHydration` ist so konzipiert, um die Zustandsynchronisierung und -wiederherstellung während der SSR (Server-Side Rendering) **zu gewährleisten**. Wenn Sie einen global reaktiven Zustand in Nuxt erstellen möchten, der SSR-freundlich ist, ist `useState` die empfohlene Wahl.
::

`useHydration` ist eine eingebaute Komponentenfunktionalität, die eine Möglichkeit bietet, Daten auf dem Serverseiten jedes Mal zu setzen, wenn eine neue HTTP-Anfrage gestellt wird, und diese Daten auf der Clientseite abzurufen. So ermöglicht `useHydration` Ihnen, den Hydrationszyklus vollständig zu steuern.

Die von der `get`-Funktion auf dem Server zurückgegebenen Daten werden unter dem eindeutigen Schlüssel im `nuxtApp.payload` gespeichert, der als erster Parameter von `useHydration` übergeben wird. Während des Hydrationsprozesses werden diese Daten dann auf der Clientseite abgerufen, um unnötige Berechnungen oder API-Aufrufe zu vermeiden.

`useHydration()` kann innerhalb von Komponentenfunktionalitäten, Plugins und Komponenten verwendet werden.

## Verwendung

::code-group

```ts [Ohne useHydration]
export default defineNuxtPlugin((nuxtApp) => {
  const myStore = new MyStore()

  if (import.meta.server) {
    nuxt.hooks.hook('app:rendered', () => {
      nuxtApp.payload.myStoreState = myStore.getState()
    })
  }

  if (import.meta.client) {
    nuxt.hooks.hook('app:created', () => {
      myStore.setState(nuxtApp.payload.myStoreState)
    })
  }
})
```

```ts [Mit useHydration]
export default defineNuxtPlugin((nuxtApp) => {
  const myStore = new MyStore()

  useHydration(
    'myStoreState', 
    () => myStore.getState(), 
    (data) => myStore.setState(data)
  )
})
```
::

## Typ

```ts [Signatur]
useHydration <T> (key: string, get: () => T, set: (value: T) => void) => void
```

## Parameter

- `key`: Ein eindeutiger Schlüssel, der das Datenobjekt in Ihrer Nuxt-Anwendung identifiziert.
- `get`: Eine Funktion, die **nur auf dem Server** ausgeführt wird (wird bei der SSR-Bereitstellung aufgerufen), um den Anfangswert festzulegen.
- `set`: Eine Funktion, die **nur auf dem Client** ausgeführt wird (wird beim Erstellen der ursprünglichen Vue-Instanz aufgerufen), um die Daten abzurufen.