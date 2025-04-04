---
title: 'definePageMeta'
description: 'Definieren Sie Metadaten für Ihre Seitenkomponenten.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/pages/runtime/composables.ts
    size: xs
---

`definePageMeta` ist ein Compiler-Makro, das Sie verwenden können, um Metadaten für Ihre **Seiten**-Komponenten im Verzeichnis [`pages/`](/docs/de/guide/directory-structure/pages) zu definieren (es sei denn, dies wurde anderesweise konfiguriert, siehe [nuxt.config#pages](/docs/de/api/nuxt-config#pages)). Auf diese Weise können Sie benutzerdefinierte Metadaten für jede statische oder dynamische Route Ihres Nuxt-Anwendungsprojekts festlegen.

```vue [pages/some-page.vue]
<script setup lang="ts">
definePageMeta({
  layout: 'default'
})
</script>
```

:read-more{to="/docs/de/guide/directory-structure/pages/#page-metadata"}

## Typ

```ts
definePageMeta(meta: PageMeta) => void

interface PageMeta {
  validate?: (route: RouteLocationNormalized) => boolean | Promise<boolean> | Partial<NuxtError> | Promise<Partial<NuxtError>>
  redirect?: RouteRecordRedirectOption
  name?: string
  path?: string
  props?: RouteRecordRaw['props']
  alias?: string | string[]
  pageTransition?: boolean | TransitionProps
  layoutTransition?: boolean | TransitionProps
  viewTransition?: boolean | 'always'
  key?: false | string | ((route: RouteLocationNormalizedLoaded) => string)
  keepalive?: boolean | KeepAliveProps
  layout?: false | LayoutKey | Ref<LayoutKey> | ComputedRef<LayoutKey>
  middleware?: MiddlewareKey | NavigationGuard | Array<MiddlewareKey | NavigationGuard>
  scrollToTop?: boolean | ((to: RouteLocationNormalizedLoaded, from: RouteLocationNormalizedLoaded) => boolean)
  [key: string]: unknown
}
```

## Parameter

### `meta`

- **Typ**: `PageMeta`

  Ein Objekt, das die folgenden Seitenmetadaten akzeptiert:

  **`name`**

  - **Typ**: `string`

    Sie können einen Namen für die Route dieser Seite definieren. Standardmäßig wird der Name basierend auf dem Pfad im Verzeichnis [`pages/`](/docs/de/guide/directory-structure/pages) generiert.

  **`path`**

  - **Typ**: `string`

    Sie können eine [benutzerdefinierte reguläre Ausdrucksform](#benutzerdefinierte-reguläre-ausdrucksform) definieren, wenn Sie eine komplexere Muster haben als das Dateiname.

  **`props`**
  
  - **Typ**: [`RouteRecordRaw['props']`](https://router.vuejs.org/de/guide/essentials/passing-props)

    Erlaubt den Zugriff auf die Route `params` als Props, die an die Seitenkomponente übergeben werden.

  **`alias`**

  - **Typ**: `string | string[]`

    Alias für das Record. Erlaubt die Definition zusätzlicher Pfade, die wie eine Kopie des Records verhalten. Erlaubt es, Pfad-Kürzel wie `/users/:id` und `/u/:id` zu haben. Alle Werte von `alias` und `path` müssen die gleichen Params teilen.

  **`keepalive`**

  - **Typ**: `boolean` | [`KeepAliveProps`](https://vuejs.org/de/api/built-in-components.html#keepalive)

    Setzen Sie auf `true`, wenn Sie die Zustände der Seite bei Änderungen der Route beibehalten möchten, oder verwenden Sie die [`KeepAliveProps`](https://vuejs.org/de/api/built-in-components.html#keepalive) für eine feingranuläre Kontrolle.

  **`key`**

  - **Typ**: `false` | `string` | `((route: RouteLocationNormalizedLoaded) => string)`

    Legen Sie den `key`-Wert fest, wenn Sie mehr Kontrolle über das Erneuern des `<NuxtPage>`-Components benötigen.

  **`layout`**

  - **Typ**: `false` | `LayoutKey` | `Ref<LayoutKey>` | `ComputedRef<LayoutKey>`

    Legen Sie einen statischen oder dynamischen Namen des Layouts für jede Route fest. Dies kann auf `false` gesetzt werden, um den Standardlayout abzuschalten.

  **`layoutTransition`**

  - **Typ**: `boolean` | [`TransitionProps`](https://vuejs.org/de/api/built-in-components.html#transition)

    Legen Sie den Namen des Transitions für das aktuelle Layout fest. Sie können auch diesen Wert auf `false` setzen, um den Layout-Transition abzuschalten.

  **`middleware`**

  - **Typ**: `MiddlewareKey` | [`NavigationGuard`](https://router.vuejs.org/de/api/interfaces/NavigationGuard.html#navigationguard) | `Array<MiddlewareKey | NavigationGuard>`

    Definieren Sie anonyme oder benannte Middleware direkt innerhalb von `definePageMeta`. Erfahren Sie mehr über [Route Middleware](/docs/de/guide/directory-structure/middleware).

  **`pageTransition`**

  - **Typ**: `boolean` | [`TransitionProps`](https://vuejs.org/de/api/built-in-components.html#transition)

    Legen Sie den Namen des Transitions für die aktuelle Seite fest. Sie können auch diesen Wert auf `false` setzen, um die Seite-Transition abzuschalten.

  **`viewTransition`**

  - **Typ**: `boolean | 'always'`

    **Experimentelles Feature, nur verfügbar, wenn in Ihrem `nuxt.config`-File aktiviert ist**</br>
    Aktivieren oder deaktivieren Sie View Transitions für die aktuelle Seite.
    Wenn auf `true` gesetzt, wird Nuxt keine Transition anwenden, wenn der Benutzer-Browser `prefers-reduced-motion: reduce` entspricht (empfohlen). Wenn auf `always` gesetzt, wird Nuxt immer die Transition anwenden.

  **`redirect`**

  - **Typ**: [`RouteRecordRedirectOption`](https://router.vuejs.org/de/guide/essentials/redirect-and-alias.html#redirect-and-alias)

    Zu welcher Route umleiten, wenn die Route direkt übereinstimmt. Die Umleitung findet vor jeder Navigation-Guard statt und löst eine neue Navigation mit dem neuen Zielort aus.

  **`validate`**

  - **Typ**: `(route: RouteLocationNormalized) => boolean | Promise<boolean> | Partial<NuxtError> | Promise<Partial<NuxtError>>`

    Überprüfen Sie, ob eine gegebene Route gültig ist, um diese Seite darzustellen. Gibt `true` zurück, wenn sie gültig ist, oder `false`, wenn nicht. Wenn keine andere Übereinstimmung gefunden werden kann, bedeutet dies eine 404. Sie können auch direkt ein Objekt mit `statusCode`/`statusMessage` zurückgeben, um sofort mit einer Fehlerantwort zu antworten (andere Übereinstimmungen werden nicht überprüft).

  **`scrollToTop`**

  - **Typ**: `boolean | (to: RouteLocationNormalized, from: RouteLocationNormalized) => boolean`

    Weisen Sie an, ob Nuxt vor der Darstellung der Seite nach oben scrollen soll oder nicht. Wenn Sie die Standardscrollverhalten von Nuxt überschreiben möchten, können Sie dies in `~/app/router.options.ts` (siehe [Benutzerdefinierte Routing](/docs/de/guide/recipes/custom-routing#using-approuteroptions)) tun.

  **`[key: string]`**

  - **Typ**: `any`

    Neben den oben genannten Eigenschaften können Sie auch **benutzerdefinierte** Metadaten festlegen. Sie möchten dies möglicherweise in einem typsicheren Weise durch [Erweitern des Typs des `meta`-Objekts](/docs/de/guide/directory-structure/pages/#typing-custom-metadata).

## Beispiele

### Basiskonfiguration

Das unten stehende Beispiel zeigt:

- wie `key` eine Funktion sein kann, die einen Wert zurückgibt;
- wie die `keepalive`-Eigenschaft sicherstellt, dass das `<modal>`-Component nicht zwischengespeichert wird, wenn zwischen mehreren Komponenten gewechselt wird;
- wie `pageType` als benutzerdefinierte Eigenschaft hinzugefügt wird:

```vue [pages/some-page.vue]
<script setup lang="ts">
definePageMeta({
  key: (route) => route.fullPath,

  keepalive: {
    exclude: ['modal']
  },

  pageType: 'Checkout'
})
</script>
```

### Definieren von Middleware

Das unten stehende Beispiel zeigt, wie Middleware mithilfe einer `function` direkt innerhalb von `definePageMeta` definiert werden kann oder als `string` festgelegt wird, die auf den Dateinamen der Middleware in dem `middleware/` Verzeichnis zugeordnet ist:

```vue [pages/some-page.vue]
<script setup lang="ts">
definePageMeta({
  // Middleware als Funktion definieren
  middleware: [
    function (to, from) {
      const auth = useState('auth')

      if (!auth.value.authenticated) {
          return navigateTo('/login')
      }

      if (to.path !== '/checkout') {
        return navigateTo('/checkout')
      }
    }
  ],

  // ... oder als String
  middleware: 'auth'

  // ... oder mehrere Strings
  middleware: ['auth', 'another-named-middleware']
})
</script>
```

### Verwenden einer benutzerdefinierten regulären Ausdrucksform

Eine benutzerdefinierte reguläre Ausdrucksform ist eine gute Möglichkeit, Konflikte zwischen überschneidenden Routen zu lösen, zum Beispiel:

Die beiden Routen "/test-category" und "/1234-post" passen sowohl zur Seite `[postId]-[postSlug].vue` als auch zur Seite `[categorySlug].vue`.

Um sicherzustellen, dass wir nur Zahlen (`\d+`) für `postId` in der `[postId]-[postSlug]`-Route haben, können wir den folgenden Code in der `[postId]-[postSlug].vue`-Datei hinzufügen:

```vue [pages/[postId\\]-[postSlug\\].vue]
<script setup lang="ts">
definePageMeta({
  path: '/:postId(\\d+)-:postSlug' 
})
</script>
```

Weitere Beispiele finden Sie unter [Vue Router's Matching Syntax](https://router.vuejs.org/de/guide/essentials/route-matching-syntax.html).

### Definieren eines Layouts

Sie können das Layout definieren, das sich auf den Dateinamen des Layouts bezieht (standardmäßig im Verzeichnis [`layouts/`](/docs/de/guide/directory-structure/layouts)). Sie können auch das Layout deaktivieren, indem Sie `layout` auf `false` setzen:

```vue [pages/some-page.vue]
<script setup lang="ts">
definePageMeta({
  // benutzerdefiniertes Layout festlegen
  layout: 'admin'

  // ... oder das Standardlayout deaktivieren
  layout: false
})
</script>
```