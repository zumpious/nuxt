---
title: 'useAsyncData'
description: useAsyncData bietet Zugriff auf Daten, die asynchron auflösen, in einem SSR-freundlichen Komponens.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts
    size: xs
---

Innerhalb Ihrer Seiten, Komponenten und Plugins können Sie useAsyncData verwenden, um auf Daten zuzugreifen, die asynchron auflösen.

::note
[`useAsyncData`](/docs/api/composables/use-async-data) ist ein Komponens, der direkt im [Nuxt Kontext](/docs/guide/going-further/nuxt-app#das-nuxt-kontext) aufgerufen werden soll. Es gibt reaktive Komponens zurück und verarbeitet Antworten hinzufügend zum Nuxt Payload, sodass sie von Server zu Client übertragen werden können, ohne dass die Daten auf der Clientseite erneut abgerufen werden müssen, wenn die Seite hydriert wird.
::

## Verwendung

```vue [pages/index.vue]
<script setup lang="ts">
const { data, status, error, refresh, clear } = await useAsyncData(
  'berge',
  () => $fetch('https://api.nuxtjs.dev/berge')
)
</script>
```

::warning
Wenn Sie eine benutzerdefinierte useAsyncData-Umwicklungsstruktur verwenden, sollten Sie den Aufruf von `await` innerhalb des Komponens nicht verwenden, da das kann unerwartetes Verhalten verursachen. Bitte folgen Sie [diesem Rezept](/docs/guide/recipes/custom-usefetch#custom-usefetch), um mehr darüber zu erfahren, wie man einen benutzerdefinierten asynchronen Datenabfrage-Fetcher erstellen kann.
::

::note
`data`, `status` und `error` sind Vue Refs und sollten in `<script setup>` mit `.value` zugegriffen werden, während `refresh`/`execute` und `clear` einfache Funktionen sind.
::

### Watch Params

Die eingebaute `watch`-Option ermöglicht es automatisch, den Abfragefunktion neu auszuführen, wenn sich Änderungen feststellen lassen.

```vue [pages/index.vue]
<script setup lang="ts">
const seite = ref(1)
const { data: posts } = await useAsyncData(
  'posts',
  () => $fetch('https://fakeApi.com/posts', {
    params: {
      seite: seite.value
    }
  }), {
    watch: [seite]
  }
)
</script>
```

::warning
[`useAsyncData`](/docs/api/composables/use-async-data) ist eine reservierte Funktionsname, der vom Compiler transformiert wird, daher sollten Sie Ihren eigenen Funktionsnamen nicht als [`useAsyncData`](/docs/api/composables/use-async-data) bezeichnen.
::

:read-more{to="/docs/getting-started/data-fetching#useasyncdata"}

## Parameter

- `key`: ein eindeutiger Schlüssel, um sicherzustellen, dass die Datenabfrage korrekt dupliziert werden kann, wenn Anfragen überlaufen. Wenn Sie keinen Schlüssel angeben, wird für Sie ein eindeutiger Schlüssel basierend auf Dateinamen und Zeilennummer der Instanz von `useAsyncData` generiert.
- `handler`: eine asynchrone Funktion, die einen wahrheitswertigen Wert zurückgeben muss (zum Beispiel sollte sie nicht `undefined` oder `null` sein), oder die Anfrage könnte auf der Clientseite doppelt ausgeführt werden.
::warning
Die `handler`-Funktion sollte **keine Nebeneffekte** haben, um vorhersehbares Verhalten bei SSR und CSR Hydration sicherzustellen. Wenn Sie Nebeneffekte auslösen müssen, verwenden Sie die [`callOnce`](/docs/api/utils/call-once)-Utility, um dies zu tun.
::
- `options`:
  - `server`: ob die Daten auf dem Server abgerufen werden sollen (Standardwert: `true`)
  - `lazy`: ob die asynchrone Funktion nach dem Laden der Route aufgelöst wird, anstatt die Clientseitige Navigation zu blockieren (Standardwert: `false`)
  - `immediate`: wenn auf `false` gesetzt, wird die Anfrage sofort nicht ausgeführt. (Standardwert: `true`)
  - `default`: eine Fabrikfunktion, um den Standardwert von `data` vor der Auflösung der asynchronen Funktion zu setzen - nützlich mit der `lazy: true` oder `immediate: false` Option
  - `transform`: eine Funktion, die verwendet werden kann, um den Ergebniswert der `handler`-Funktion nach der Auflösung zu ändern
  - `getCachedData`: Bereitstellt eine Funktion, die gespeicherte Daten zurückgibt. Ein Rückgabewert von `null` oder `undefined` löst eine Abfrage aus. Standardmäßig ist dies:
    ```ts
    const getDefaultCachedData = (key, nuxtApp) => nuxtApp.isHydrating 
      ? nuxtApp.payload.data[key] 
      : nuxtApp.static.data[key]
    ```
    Dies speichert nur Daten, wenn `experimental.payloadExtraction` in `nuxt.config` aktiviert ist.
  - `pick`: nur die angegebenen Schlüssel aus dem Ergebnis der `handler`-Funktion auswählen
  - `watch`: beobachtbare Quellen automatisch aktualisieren, um die Abfrage zu erneuern
  - `deep`: Daten in einem tiefen Ref-Objekt zurückgeben. Es ist `false` standardmäßig, um eine flache Ref-Objekt für Leistung zu verwenden.
  - `dedupe`: vermeiden, dass die gleiche Schlüssel mehrmals gleichzeitig abgerufen wird (Standardwert: `cancel`). Mögliche Optionen:
    - `cancel` - bestehende Anfragen abbrechen, wenn eine neue Anfrage gestellt wird
    - `defer` - keine neuen Anfragen stellen, wenn eine bestehende Anfrage läuft

::note
Unter der Haube verwendet `lazy: false` `<Suspense>` zur Blockierung der Route-Loading, bevor die Daten abgerufen wurden. Überlegen Sie, `lazy: true` und eine Ladestatusimplementierung zu verwenden, um eine schnellere Benutzererfahrung zu gewährleisten.
::

::read-more{to="/docs/api/composables/use-lazy-async-data"}
Sie können `useLazyAsyncData` verwenden, um das Verhalten von `lazy: true` mit `useAsyncData` zu erreichen.
::

::tip{icon="i-simple-icons-youtube" to="https://www.youtube.com/watch?v=aQPR0xn-MMk" target="_blank"}
Lernen Sie, wie Sie `transform` und `getCachedData` verwenden können, um unnötige API-Aufrufe zu vermeiden und Daten für Besucher auf der Clientseite zu cachen.
::

## Rückgabewerte

- `data`: der Ergebniswert der asynchronen Funktion, die übergeben wurde.
- `refresh`/`execute`: eine Funktion, die verwendet werden kann, um die von der `handler`-Funktion zurückgegebenen Daten zu aktualisieren.
- `error`: ein Fehlerobjekt, wenn die Datenabfrage fehlschlägt.
- `status`: eine Zeichenfolge, die den Status der Datenanfrage angibt:
  - `idle`: wenn die Anfrage noch nicht gestartet wurde, z.B.:
    - wenn `execute` noch nicht aufgerufen wurde und `{ immediate: false }` gesetzt ist
    - wenn HTML auf dem Server gerendert wird und `{ server: false }` gesetzt ist
  - `pending`: die Anfrage läuft
  - `success`: die Anfrage wurde erfolgreich abgeschlossen
  - `error`: die Anfrage ist fehlgeschlagen
- `clear`: eine Funktion, die `data` auf `undefined`, `error` auf `null`, `status` auf `'idle'` und alle aktuell laufenden Anfragen als abgebrochen markiert, setzt.

Standardmäßig wartet Nuxt, bis eine `refresh` abgeschlossen ist, bevor sie erneut ausgeführt werden kann.

::note
Wenn Sie keine Daten auf dem Server abgerufen haben (zum Beispiel mit `server: false`), werden die Daten nicht abgerufen, bis die Hydration abgeschlossen ist. Dies bedeutet, dass selbst wenn Sie auf der Clientseite auf [`useAsyncData`](/docs/api/composables/use-async-data) warten, `data` innerhalb von `<script setup>` immer `null` bleiben kann.
::

## Typ

```ts [Signature]
function useAsyncData<DataT, DataE>(
  handler: (nuxtApp?: NuxtApp) => Promise<DataT>,
  options?: AsyncDataOptions<DataT>
): AsyncData<DataT, DataE>
function useAsyncData<DataT, DataE>(
  key: string,
  handler: (nuxtApp?: NuxtApp) => Promise<DataT>,
  options?: AsyncDataOptions<DataT>
): Promise<AsyncData<DataT, DataE>>

type AsyncDataOptions<DataT> = {
  server?: boolean
  lazy?: boolean
  immediate?: boolean
  deep?: boolean
  dedupe?: 'cancel' | 'defer'
  default?: () => DataT | Ref<DataT> | null
  transform?: (input: DataT) => DataT | Promise<DataT>
  pick?: string[]
  watch?: WatchSource[]
  getCachedData?: (key: string, nuxtApp: NuxtApp) => DataT | undefined
}

type AsyncData<DataT, ErrorT> = {
  data: Ref<DataT | null>
  refresh: (opts?: AsyncDataExecuteOptions) => Promise<void>
  execute: (opts?: AsyncDataExecuteOptions) => Promise<void>
  clear: () => void
  error: Ref<ErrorT | null>
  status: Ref<AsyncDataRequestStatus>
};

interface AsyncDataExecuteOptions {
  dedupe?: 'cancel' | 'defer'
}

type AsyncDataRequestStatus = 'idle' | 'pending' | 'success' | 'error'
```

:read-more{to="/docs/getting-started/data-fetching"}
