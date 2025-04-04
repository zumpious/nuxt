---
title: 'abortNavigation'
description: 'abortNavigation ist eine Hilfsfunktion, die die Navigation verhindert und bei Bedarf einen Fehler wirft.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts
    size: xs
---

::warning
`abortNavigation` kann nur innerhalb eines [Route Middleware Handlers](/docs/de/guide/directory-structure/middleware) verwendet werden.
::

## Typ

```ts
abortNavigation(err?: Error | string): false
```

## Parameter

### `err`

- **Typ**: [`Error`](https://developer.mozilla.org/pl/docs/Web/JavaScript/Reference/Global_Objects/Error) | `string`

  Optionaler Fehler, der durch `abortNavigation` geworfen wird.

## Beispiele

Im folgenden Beispiel wird gezeigt, wie man `abortNavigation` in einem Route Middleware Handler verwenden kann, um unbefugten Zugriff auf eine Route zu verhindern:

```ts [middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const user = useState('user')

  if (!user.value.isAuthorized) {
    return abortNavigation()
  }

  if (to.path !== '/edit-post') {
    return navigateTo('/edit-post')
  }
})
```

### `err` als String

Sie können den Fehler als String übergeben:

```ts [middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const user = useState('user')

  if (!user.value.isAuthorized) {
    return abortNavigation('Insufficient permissions.')
  }
})
```

### `err` als Fehlerobjekt

Sie können den Fehler als ein [`Error`](https://developer.mozilla.org/pl/docs/Web/JavaScript/Reference/Global_Objects/Error) Objekt übergeben, z.B. das in einem `catch`-Block gefangen wurde:

```ts [middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  try {
    /* code that might throw an error */
  } catch (err) {
    return abortNavigation(err)
  }
})
```