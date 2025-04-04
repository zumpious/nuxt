---
title: "navigateTo"
description: navigateTo ist ein Hilfsfunktion, die Benutzer programmatisch navigieren lässt.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts
    size: xs
---

## Verwendung

`navigateTo` ist sowohl auf dem Serverseiten- als auch auf dem Clientseiten-Modul verfügbar. Es kann im [Nuxt Kontext](/docs/de/guide/going-further/nuxt-app#der-nuxt-kontext) verwendet werden oder direkt, um Seiten zu navigieren.

::warning
Stellen Sie sicher, dass Sie immer `await` oder `return` auf das Ergebnis von `navigateTo` verwenden, wenn Sie es aufrufen.
::

::note
`navigateTo` kann nicht innerhalb von Nitro-Routen verwendet werden. Um eine Serverseitige Weiterleitung in Nitro-Routen durchzuführen, verwenden Sie stattdessen [`sendRedirect`](https://h3.unjs.io/de/utils/response#sendredirectevent-location-code) anstelle davon.
::

### Innerhalb eines Vue-Komponenten

```vue
<script setup lang="ts">
// 'to' als String übergeben
await navigateTo('/search')

// ... oder als Routenelement
await navigateTo({ path: '/search' })

// ... oder als Routenelement mit Query-Parametern
await navigateTo({
  path: '/search',
  query: {
    page: 1,
    sort: 'asc'
  }
})
</script>
```

### Innerhalb eines Routen-Middlewares

```ts
export default defineNuxtRouteMiddleware((to, from) => {
  if (to.path !== '/search') {
    // Setzt den Redirect-Code auf '301 Moved Permanently'
    return navigateTo('/search', { redirectCode: 301 })
  }
})
```

Wenn `navigateTo` innerhalb eines Routen-Middlewares verwendet wird, muss **das Ergebnis zurückgegeben** werden, um den Middleware-Aufruffluss korrekt zu gewährleisten.

Ein Beispiel, wie eine solche Implementierung **nicht wie erwartet funktioniert**:

```ts
export default defineNuxtRouteMiddleware((to, from) => {
  if (to.path !== '/search') {
    // ❌ Dies funktioniert nicht wie erwartet
    navigateTo('/search', { redirectCode: 301 })
    return
  }
})
```

In diesem Fall wird `navigateTo` ausgeführt, aber nicht zurückgegeben, was zu unerwarteten Verhaltensweisen führen kann.

:read-more{to="/docs/de/guide/directory-structure/middleware"}

### Navigieren zu einer externen URL

Der `external`-Parameter in `navigateTo` beeinflusst, wie URLs navigiert werden:

- **Ohne `external: true`**:
  - Internationale URLs navigieren wie erwartet.
  - Externe URLs werfen einen Fehler aus.

- **Mit `external: true`**:
  - Internationale URLs navigieren mit einer vollständigen Seite Neuladung.
  - Externe URLs navigieren wie erwartet.

#### Beispiel

```vue
<script setup lang="ts">
// Wird ein Fehler werfen;
// die Navigierung zu einer externen URL ist standardmäßig nicht erlaubt
await navigateTo('https://nuxt.com')

// Wird erfolgreich umgeleitet, wenn der `external`-Parameter auf `true` gesetzt ist
await navigateTo('https://nuxt.com', {
  external: true
})
</script>
```

### Öffnen einer Seite in einem neuen Tab

```vue
<script setup lang="ts">
// Öffnet 'https://nuxt.com' in einem neuen Tab
await navigateTo('https://nuxt.com', {
  open: {
    target: '_blank',
    windowFeatures: {
      width: 500,
      height: 500
    }
  }
})
</script>
```

## Typ

```ts
function navigateTo(
  to: RouteLocationRaw | undefined | null,
  options?: NavigateToOptions
): Promise<void | NavigationFailure | false> | false | void | RouteLocationRaw 

interface NavigateToOptions {
  replace?: boolean
  redirectCode?: number
  external?: boolean
  open?: OpenOptions
}

type OpenOptions = {
  target: string
  windowFeatures?: OpenWindowFeatures
}

type OpenWindowFeatures = {
  popup?: boolean
  noopener?: boolean
  noreferrer?: boolean
} & XOR<{ width?: number }, { innerWidth?: number }>
  & XOR<{ height?: number }, { innerHeight?: number }>
  & XOR<{ left?: number }, { screenX?: number }>
  & XOR<{ top?: number }, { screenY?: number }>
```

## Parameter

### `to`

**Typ**: [`RouteLocationRaw`](https://router.vuejs.org/api/de/interfaces/routelocationoptions.html#Interface-RouteLocationOptions) | `undefined` | `null`

**Standardwert**: `'/'`

`to` kann als einfacher String oder als Routenelement übergeben werden, um zur angegebenen URL umgeleitet zu werden. Wenn `undefined` oder `null` übergeben wird, wird standardmäßig zur Startseite umgeleitet.

#### Beispiel

```ts
// Die direkte Übergabe der URL leitet zur Seite '/blog' um
await navigateTo('/blog')

// Mit dem Routenelement wird zur Route mit dem Namen 'blog' umgeleitet
await navigateTo({ name: 'blog' })

// Leitet zur Route 'product' und überträgt dabei ein Parameter (id = 1) mit dem Routenelement.
await navigateTo({ name: 'product', params: { id: 1 } })
```

### `options` (optional)

**Typ**: `NavigateToOptions`

Ein Objekt, das die folgenden Eigenschaften akzeptiert:

- `replace`

  - **Typ**: `boolean`
  - **Standardwert**: `false`
  - Standardmäßig fügt `navigateTo` den angegebenen Pfad in die Instanz des Vue Router auf der Clientseite hinzu.

    Dieses Verhalten kann durch Festlegen von `replace` auf `true` geändert werden, um anzugeben, dass der angegebene Pfad ersetzt werden soll.

- `redirectCode`

  - **Typ**: `number`
  - **Standardwert**: `302`

  - `navigateTo` leitet standardmäßig auf der Serverseite zur angegebenen URL um und setzt den Redirect-Code auf `302 Found` (`302 Found`).

    Dieses Standardverhalten kann durch Angabe eines anderen `redirectCode` geändert werden. Häufig wird `301 Moved Permanently` für permanente Umleitungen verwendet.

- `external`

  - **Typ**: `boolean`
  - **Standardwert**: `false`

  - Erlaubt die Navigierung zu einer externen URL, wenn auf `true` gesetzt. Andernfalls werft `navigateTo` einen Fehler, da die externe Navigation standardmäßig nicht erlaubt ist.

- `open`

  - **Typ**: `OpenOptions`
  - Erlaubt die Navigierung zur URL mithilfe des `open()`-Methode des Fensters. Diese Option ist nur auf der Clientseite gültig und wird auf der Serverseite ignoriert.

    Ein Objekt, das die folgenden Eigenschaften akzeptiert:

  - `target`

    - **Typ**: `string`
    - **Standardwert**: `'_blank'`

    - Eine ohne Leerzeichen enthaltene Zeichenkette, die den Namen des Browsing-Contexts angibt, in den das Ressourcen geladen wird.

  - `windowFeatures`

    - **Typ**: `OpenWindowFeatures`

    - Ein Objekt, das die folgenden Eigenschaften akzeptiert:

      | Eigenschaft | Typ    | Beschreibung |
      |-------------|--------|--------------|
      | `popup`     | `boolean` | Fordert eine minimale Popup-Fensteranforderung an, anstatt ein neues Tab zu öffnen, mit UI-Eigenschaften, die vom Browser entschieden werden. |
      | `width` oder `innerWidth` | `number`  | Gibt die Breite des Inhaltsbereichs (mindestens 100 Pixel) an, einschließlich Scrollbalken. |
      | `height` oder `innerHeight` | `number`  | Gibt die Höhe des Inhaltsbereichs (mindestens 100 Pixel) an, einschließlich Scrollbalken. |
      | `left` oder `screenX`   | `number`  | Legt die horizontale Position des neuen Fensters relativ zum linken Rand des Bildschirms fest. |
      | `top` oder `screenY`   | `number`  | Legt die vertikale Position des neuen Fensters relativ zum oberen Rand des Bildschirms fest. |
      | `noopener`   | `boolean` | Verhindert, dass das neue Fenster über `window.opener` den ursprünglichen Fenster zugreift. |
      | `noreferrer` | `boolean` | Verhindert, dass der Referer-Header gesendet wird und implizit `noopener` aktiviert. |

      Weitere Informationen zu den **windowFeatures**-Eigenschaften finden Sie in der [Dokumentation](https://developer.mozilla.org/en-US/docs/Web/API/Window/open#windowfeatures).