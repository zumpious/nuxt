---
title: "defineNuxtRouteMiddleware"
description: "Erstelle benannte Routen Middleware mit der Helper-Funktion defineNuxtRouteMiddleware."
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts
    size: xs
---

Routen Middleware werden im Verzeichnis [`middleware/`](/docs/de/guide/directory-structure/middleware) Ihres Nuxt-Anwendungsverzeichnisses gespeichert (es sei denn, Sie haben dies anderes konfiguriert [hier](/docs/de/api/nuxt-config#middleware)).

## Typ

```ts
defineNuxtRouteMiddleware(middleware: RouteMiddleware) => RouteMiddleware

interface RouteMiddleware {
  (to: RouteLocationNormalized, from: RouteLocationNormalized): ReturnType<NavigationGuard>
}
```

## Parameter

### `middleware`

- **Typ**: `RouteMiddleware`

Eine Funktion, die zwei Vue Router Routenobjekte als Parameter nimmt: das nächste Routenziel `to` als erstes und das aktuelle Routenziel `from` als zweites.

Weitere Informationen zu den verfügbaren Eigenschaften von `RouteLocationNormalized` finden Sie in den **[Vue Router Dokumentationen](https://router.vuejs.org/api/#RouteLocationNormalized)**.

## Beispiele

### Fehlertextseite anzeigen

Sie können Routen Middleware verwenden, um Fehler zu werfen und hilfreiche Fehlermeldungen anzuzeigen:

```ts [middleware/error.ts]
export default defineNuxtRouteMiddleware((to) => {
  if (to.params.id === '1') {
    throw createError({ statusCode: 404, statusMessage: 'Seite nicht gefunden' })
  }
})
```

Die obige Routen Middleware wird den Benutzer zur benutzerdefinierten Fehlerseite umleiten, die in der `~/error.vue`-Datei definiert ist, und zeigt die Fehlermeldung und den Code an, der vom Middleware übergeben wurde.

### Umleitung

Verwenden Sie die Komponente [`useState`](/docs/de/api/composables/use-state) in Kombination mit der `navigateTo`-Hilfsfunktion innerhalb der Routen Middleware, um Benutzer aufgrund ihrer Authentifizierungszustände auf andere Routen umzuleiten:

```ts [middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const auth = useState('auth')

  if (!auth.value.isAuthenticated) {
    return navigateTo('/login')
  }

  if (to.path !== '/dashboard') {
    return navigateTo('/dashboard')
  }
})
```

Beide Hilfsfunktionen [navigateTo](/docs/de/api/utils/navigate-to) und [abortNavigation](/docs/de/api/utils/abort-navigation) sind global verfügbar und können innerhalb von `defineNuxtRouteMiddleware` verwendet werden.
---