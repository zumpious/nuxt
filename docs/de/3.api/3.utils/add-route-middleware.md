---
title: 'addRouteMiddleware'
description: 'addRouteMiddleware() ist eine Hilfsfunktion, um Middleware dynamisch in Ihrer Anwendung hinzuzufügen.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts
    size: xs
---

::note
Route Middleware sind Navigationsgardien, die im Verzeichnis der[`middleware/`](/docs/de/guide/directory-structure/middleware) Ihres Nuxt-Projekts gespeichert werden (lessen Sie es [anderenfalls einstellen](/docs/de/api/nuxt-config#middleware)).
::

## Typ

```ts
function addRouteMiddleware (name: string, middleware: RouteMiddleware, options?: AddRouteMiddlewareOptions): void
function addRouteMiddleware (middleware: RouteMiddleware): void

interface AddRouteMiddlewareOptions {
  global?: boolean
}
```

## Parameter

### `name`

- **Typ:** `string` | `RouteMiddleware`

Kann entweder eine Zeichenkette oder eine Funktion vom Typ `RouteMiddleware` sein. Die Funktion nimmt den nächsten Routenziel `to` als erstes Argument und das aktuelle Routenziel `from` als zweites Argument entgegen, beide sind Vue-Routerelemente.

Weitere Informationen zu verfügbaren Eigenschaften von [Routenelementen](/docs/de/api/composables/use-route).

### `middleware`

- **Typ:** `RouteMiddleware`

Das zweite Argument ist eine Funktion vom Typ `RouteMiddleware`. Gleich wie oben, bietet sie `to` und `from` Routenelemente. Es wird optional, wenn das erste Argument in `addRouteMiddleware()` bereits als Funktion übergeben wird.

### `options`

- **Typ:** `AddRouteMiddlewareOptions`

Ein optionales `options`-Argument ermöglicht es, den Wert von `global` auf `true` zu setzen, um anzugeben, ob das Routen Middleware global ist (Standardwert ist `false`).

## Beispiele

### Benannte Route Middleware

Benannte Route Middleware werden definiert, indem eine Zeichenkette als erstes Argument und eine Funktion als zweites Argument übergeben wird:

```ts [plugins/my-plugin.ts]
export default defineNuxtPlugin(() => {
  addRouteMiddleware('named-middleware', () => {
    console.log('named middleware added in Nuxt plugin')
  })
})
```

Wenn sie in einem Plugin definiert werden, überschreibt sie jegliche vorhandenen Middleware mit demselben Namen im `middleware/` Verzeichnis.

### Globale Route Middleware

Globale Route Middleware können in zwei Weisen definiert werden:

- Übergeben Sie eine Funktion direkt als erstes Argument ohne einen Namen. Sie wird automatisch als globale Middleware behandelt und bei jeder Routenänderung angewendet.

  ```ts [plugins/my-plugin.ts]
  export default defineNuxtPlugin(() => {
    addRouteMiddleware((to, from) => {
      console.log('anonymous global middleware that runs on every route change')
    })
  })
  ```

- Setzen Sie ein optionales drittes Argument `{ global: true }`, um anzugeben, ob die Routen Middleware global ist.

  ```ts [plugins/my-plugin.ts]
  export default defineNuxtPlugin(() => {
    addRouteMiddleware('global-middleware', (to, from) => {
        console.log('global middleware that runs on every route change')
      },
      { global: true }
    )
  })
  ```
```