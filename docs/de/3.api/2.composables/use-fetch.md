---
title: 'useFetch'
description: 'Lade Daten von einer API-Endpunkt mit einem SSR-freundlichen Komposablen.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/fetch.ts
    size: xs
---

Dieser Komposablen bietet eine praktische Verpackung umgegangen von [`useAsyncData`](/docs/api/composables/use-async-data) und [`$fetch`](/docs/api/utils/dollarfetch).
Er generiert automatisch eine Schlüssel basierend auf URL und Abfrageoptionen, bietet Typhinweise für Anforderungs-URL basierend auf Server-Routen und schließt API-Antwort-Typen ab.

::note
`useFetch` ist ein Komposablen, der direkt in einer Setup-Funktion, Plugin oder Route-Middleware aufgerufen werden soll. Er gibt reaktive Komposablen zurück und verarbeitet die Hinzufügung von Antworten zum Nuxt-Payload, damit sie vom Server zum Client übertragen werden können, ohne dass die Daten beim Hydratieren der Seite neu geladen werden müssen.
::

## Verwendung

```vue [pages/modules.vue]
<script setup lang="ts">
const { data, status, error, refresh, clear } = await useFetch('/api/modules', {
  pick: ['title']
})
</script>
```

::warning
Wenn Sie eine benutzerdefinierte `useFetch`-Verpackung verwenden, sollten Sie die Funktion nicht in einem Komposablen erwartet werden, da das kann unerwartetes Verhalten verursachen. Bitte folgen Sie [diesem Rezept](/docs/guide/recipes/custom-usefetch#custom-usefetch) für weitere Informationen zur Erstellung eines benutzerdefinierten asynchronen Datensuchers.
::

::note
`data`, `status` und `error` sind Vue-Refs, und sie sollten mit `.value` zugegriffen werden, wenn sie im `<script setup>` verwendet werden, während `refresh`/`execute` und `clear` einfache Funktionen sind.
::

Mit der `query`-Option können Sie Suchparameter Ihrer Anfrage hinzufügen. Diese Option wird von [unjs/ofetch](https://github.com/unjs/ofetch) erweitert und verwendet [unjs/ufo](https://github.com/unjs/ufo) um die URL zu erstellen. Objekte werden automatisch kodifiziert.

```ts
const param1 = ref('value1')
const { data, status, error, refresh } = await useFetch('/api/modules', {
  query: { param1, param2: 'value2' }
})
```

Das obige Beispiel führt zu `https://api.nuxt.com/modules?param1=value1&param2=value2`.

Sie können auch [Interceptoren](https://github.com/unjs/ofetch#%EF%B8%8F-interceptors) verwenden:

```ts
const { data, status, error, refresh, clear } = await useFetch('/api/auth/login', {
  onRequest({ request, options }) {
    // Setze die Anforderungsheader
    // beachte, dass dies auf ofetch >= 1.4.0 angewiesen ist - du musst möglicherweise deinen Lockfile aktualisieren
    options.headers.set('Authorization', '...')
  },
  onRequestError({ request, options, error }) {
    // Verarbeite die Anforderungsfehler
  },
  onResponse({ request, response, options }) {
    // Verarbeite die Antwortdaten
    localStorage.setItem('token', response._data.token)
  },
  onResponseError({ request, response, options }) {
    // Verarbeite die Antwortfehler
  }
})
```

::warning
`useFetch` ist eine reservierte Funktion, die vom Compiler transformiert wird, daher sollten Sie Ihre eigene Funktion nicht `useFetch` heißen.
::

::warning
Wenn Sie das `data`-Variable aus einer `useFetch`-Rückgabe destrukturiert haben und es sich um eine Zeichenkette handelt und nicht um ein JSON-geparstes Objekt, stellen Sie sicher, dass Ihr Komponenten-Import keine Importanweisung wie `import { useFetch } from '@vueuse/core'` enthält.
::

::tip{icon="i-lucide-video" to="https://www.youtube.com/watch?v=njsGVmcWviY" target="_blank"}
Schauen Sie sich den Video von Alexander Lichter an, um `useFetch` falsch zu verwenden zu vermeiden!
::

:link-example{to="/docs/examples/advanced/use-custom-fetch-composable"}

:read-more{to="/docs/getting-started/data-fetching"}

:link-example{to="/docs/examples/features/data-fetching"}

## Parameter

- `URL`: Die URL, die abgerufen werden soll.
- `Options` (erweitert von [unjs/ofetch](https://github.com/unjs/ofetch) Optionen & [AsyncDataOptions](/docs/api/composables/use-async-data#params)):
  - `method`: Anforderungsverfahren.
  - `query`: Fügt Suchparameter zur URL hinzu, indem [ufo](https://github.com/unjs/ufo) verwendet wird.
  - `params`: Alias für `query`
  - `body`: Anforderungsbody - automatisch kodifiziert (wenn ein Objekt übergeben wird).
  - `headers`: Anforderungsheader.
  - `baseURL`: Basis-URL für die Anfrage.
  - `timeout`: Millisekunden, nach denen die Anfrage automatisch abgebrochen wird.
  - `cache`: Behandelt Cache-Kontrolle gemäß [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/fetch#cache)
    - Du kannst einen Boolean übergeben, um den Cache zu deaktivieren, oder einer der folgenden Werte: `default`, `no-store`, `reload`, `no-cache`, `force-cache`, und `only-if-cached`.

::note
Alle Abfrageoptionen können mit einem `computed` oder `ref` Wert gegeben werden. Diese werden beobachtet und neue Anfragen werden automatisch mit jeder neuen Werte durchgeführt, wenn sie aktualisiert werden.
::

- `Options` (von [`useAsyncData`](/docs/api/composables/use-async-data)):
  - `key`: ein eindeutiger Schlüssel, um sicherzustellen, dass die Datenabfrage korrekt de-dupliziert werden kann, wenn nicht angegeben, wird er auf Basis von URL und Abfrageoptionen automatisch generiert.
  - `server`: ob die Daten auf dem Server abgerufen werden sollen (Standardwert: `true`).
  - `lazy`: ob die asynchrone Funktion nach dem Laden der Route aufgelöst werden soll, anstatt die clientseitige Navigation zu blockieren (Standardwert: `false`).
  - `immediate`: wenn auf `false` gesetzt, wird die Anfrage sofort nicht ausgeführt. (Standardwert: `true`).
  - `default`: eine Fabrikfunktion, um den Standardwert von `data` vor der Auflösung der asynchronen Funktion festzulegen - nützlich mit der `lazy: true` oder `immediate: false` Option.
  - `transform`: eine Funktion, die verwendet werden kann, um den Ergebniswert der `handler`-Funktion nach der Auflösung zu verändern.
  - `getCachedData`: Bereitstelle eine Funktion, die gespeicherte Daten zurückgibt. Ein `null` oder `undefined` Rückgabewert löst eine neue Abfrage aus. Standardmäßig ist dies:
    ```ts
    const getDefaultCachedData = (key, nuxtApp) => nuxtApp.isHydrating 
      ? nuxtApp.payload.data[key] 
      : nuxtApp.static.data[key]
    ```
    Dies speichert Daten nur, wenn `experimental.payloadExtraction` in `nuxt.config` aktiviert ist.
  - `pick`: wähle nur die angegebenen Schlüssel aus diesem Array aus der `handler`-Funktion.
  - `watch`: beobachte eine Reihe von reaktiven Quellen und aktualisiere den Abfrageergebnis automatisch, wenn sie sich ändern. Abfrageoptionen und URL werden standardmäßig beobachtet. Du kannst komplett ignorierte reaktive Quellen durch `watch: false` ausschließen. Zusammen mit `immediate: false` ermöglicht dies eine vollständig manuelle `useFetch`. (Du kannst [hier](/docs/getting-started/data-fetching#watch) ein Beispiel sehen, wie `watch` verwendet wird.)
  - `deep`: gib die Daten in einem tiefen Ref-Objekt zurück. Es ist `false` standardmäßig, um die Leistung zu verbessern und die Daten in einem flachen Ref-Objekt zurückzugeben.
  - `dedupe`: vermeide das Abrufen derselben Schlüssel mehr als einmal gleichzeitig (Standardwert: `cancel`). Mögliche Optionen:
    - `cancel` - stelle bestehende Anfragen ab, wenn eine neue gemacht wird
    - `defer` - mache keine neuen Anfragen, wenn eine bestehende Anfrage läuft

::note
Wenn Sie eine Funktion oder `ref` als `url`-Parameter übergeben oder Funktionen als Argumente an den `options`-Parameter übergeben, dann wird die `useFetch`-Aufruf nicht mit anderen `useFetch`-Aufrufen in Ihrem Codebase übereinstimmen, selbst wenn die Optionen äquivalent erscheinen. Wenn Sie eine Übereinstimmung erzwingen möchten, können Sie Ihren eigenen Schlüssel in `options` übergeben.
::

::note
Wenn Sie `useFetch` verwenden, um eine (externe) HTTPS-URL mit einem selbstsignierten Zertifikat in der Entwicklung aufzurufen, müssen Sie `NODE_TLS_REJECT_UNAUTHORIZED=0` in Ihrer Umgebung setzen.
::

::tip{icon="i-simple-icons-youtube" to="https://www.youtube.com/watch?v=aQPR0xn-MMk" target="_blank"}
Lernen Sie, wie Sie `transform` und `getCachedData` verwenden, um unnötige API-Anfragen zu vermeiden und Daten für Besucher auf dem Client zu cachen.
::

## Rückgabewerte

- `data`: der Ergebniswert der asynchronen Funktion, die übergeben wurde.
- `refresh`/`execute`: eine Funktion, die verwendet werden kann, um die von der `handler`-Funktion zurückgegebenen Daten zu aktualisieren.
- `error`: ein Fehlerobjekt, wenn die Datenabfrage fehlschlägt.
- `status`: eine Zeichenkette, die den Status der Datenanfrage angibt:
  - `idle`: wenn die Anfrage noch nicht gestartet wurde, z.B.:
    - wenn `execute` noch nicht aufgerufen wurde und `{ immediate: false }` gesetzt ist
    - wenn HTML auf dem Server gerendert wird und `{ server: false }` gesetzt ist
  - `pending`: die Anfrage läuft
  - `success`: die Anfrage wurde erfolgreich abgeschlossen
  - `error`: die Anfrage ist fehlgeschlagen
- `clear`: eine Funktion, die `data` auf `undefined`, `error` auf `null`, `status` auf `'idle'` setzt und alle laufenden Anfragen als abgebrochen markiert.

Standardmäßig wartet Nuxt, bis eine `refresh` abgeschlossen ist, bevor sie erneut ausgeführt werden kann.

::note
Wenn Sie Daten auf dem Server nicht abgerufen haben (z.B. mit `server: false`), werden die Daten erst nach der Hydratierung abgerufen. Das bedeutet, dass `data` innerhalb von `<script setup>` immer `null` bleibt, selbst wenn Sie `useFetch` auf dem Client erwartet.
::

## Typ

```ts [Signature]
function useFetch<DataT, ErrorT>(
  url: string | Request | Ref<string | Request> | (() => string | Request),
  options?: UseFetchOptions<DataT>
): Promise<AsyncData<DataT, ErrorT>>

type UseFetchOptions<DataT> = {
  key?: string
  method?: string
  query?: SearchParams
  params?: SearchParams
  body?: RequestInit['body'] | Record<string, any>
  headers?: Record<string, string> | [key: string, value: string][] | Headers
  baseURL?: string
  server?: boolean
  lazy?: boolean
  immediate?: boolean
  getCachedData?: (key: string, nuxtApp: NuxtApp) => DataT | undefined
  deep?: boolean
  dedupe?: 'cancel' | 'defer'
  default?: () => DataT
  transform?: (input: DataT) => DataT | Promise<DataT>
  pick?: string[]
  watch?: WatchSource[] | false
}

type AsyncData<DataT, ErrorT> = {
  data: Ref<DataT | null>
  refresh: (opts?: AsyncDataExecuteOptions) => Promise<void>
  execute: (opts?: AsyncDataExecuteOptions) => Promise<void>
  clear: () => void
  error: Ref<ErrorT | null>
  status: Ref<AsyncDataRequestStatus>
}

interface AsyncDataExecuteOptions {
  dedupe?: 'cancel' | 'defer'
}

type AsyncDataRequestStatus = 'idle' | 'pending' | 'success' | 'error'
```