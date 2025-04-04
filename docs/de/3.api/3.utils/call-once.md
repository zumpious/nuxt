---
title: "callOnce"
description: "Führt eine gegebene Funktion oder einen Codeausschnitt bei der SSR oder CSR nur einmal aus."
navigation:
  badge: Neu
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/once.ts
    size: xs
---

::important
Diese Hilfsmittel sind ab [Nuxt v3.9](/blog/v3-9) verfügbar.
::

## Zweck

Die `callOnce` Funktion ist darauf ausgelegt, eine gegebene Funktion oder einen Codeausschnitt nur einmal während der Ausführung auszuführen:
- Serverseitige Erstellung, aber nicht die Hydratation
- Clientseitige Navigation

Dies ist nützlich für Code, der nur einmal ausgeführt werden sollte, wie zum Beispiel das Protokollieren eines Ereignisses oder das Einrichten eines globalen Zustands.

## Verwendung

Der Standardmodus von `callOnce` ist es, den Code nur einmal auszuführen. Zum Beispiel wird der Code, wenn er auf dem Server ausgeführt wird, auf dem Client nicht wiederholt ausgeführt. Er wird auch nicht wiederholt ausgeführt, wenn Sie `callOnce` mehrmals auf dem Client aufrufen, zum Beispiel indem Sie zurück zu dieser Seite navigieren.

```vue [app.vue]
<script setup lang="ts">
const websiteConfig = useState('config')

await callOnce(async () => {
  console.log('Dies wird nur einmal protokolliert')
  websiteConfig.value = await $fetch('https://my-cms.com/api/website-config')
})
</script>
```

Es ist auch möglich, den Code bei jeder Navigation auszuführen, ohne dabei eine doppelte Server/Client-Last zu verursachen. Dafür kann der Modus `navigation` verwendet werden:

```vue [app.vue]
<script setup lang="ts">
const websiteConfig = useState('config')

await callOnce(async () => {
  console.log('Dies wird nur einmal protokolliert und dann bei jeder clientseitigen Navigation')
  websiteConfig.value = await $fetch('https://my-cms.com/api/website-config')
}, { mode: 'navigation' })
</script>
```

::important
Der Modus `navigation` ist ab [Nuxt v3.15](/blog/v3-15) verfügbar.
::

::tip{to="/docs/de/getting-started/state-management#verwendung-mit-pinia"}
`callOnce` ist nützlich in Kombination mit dem [Pinia Modul](/modules/pinia), um Store-Aktionen aufzurufen.
::

:read-more{to="/docs/de/getting-started/state-management"}

::warning
Achten Sie darauf, dass `callOnce` nichts zurückgibt. Wenn Sie Daten abrufen möchten, sollten Sie stattdessen [`useAsyncData`](/docs/de/api/composables/use-async-data) oder [`useFetch`](/docs/de/api/composables/use-fetch) verwenden.
::

::note
`callOnce` ist ein Komposable, der direkt in einer Setup-Funktion, einem Plugin oder einem Routen-Middleware aufgerufen werden sollte, da es Daten zum Nuxt-Payload hinzufügen muss, um die Funktion beim Hydratieren des Clients nicht wiederzurufen.
::

## Typ

```ts
callOnce (key?: string, fn?: (() => any | Promise<any>), options?: CallOnceOptions): Promise<void>
callOnce(fn?: (() => any | Promise<any>), options?: CallOnceOptions): Promise<void>

type CallOnceOptions = {
  /**
   * Ausführungsmodus für die callOnce-Funktion
   * @default 'render'
   */
  mode?: 'navigation' | 'render'
}
```

## Parameter

- `key`: Eine eindeutige Schlüssel, der sicherstellt, dass der Code nur einmal ausgeführt wird. Wenn Sie keinen Schlüssel angeben, wird ein eindeutiger Schlüssel basierend auf der Datei und Zeilennummer der Instanz von `callOnce` für Sie generiert.
- `fn`: Die Funktion, die einmal ausgeführt werden soll. Diese Funktion kann auch einen `Promise` und einen Wert zurückgeben.
- `options`: Legt den Modus fest, entweder zur Wiederholung bei Navigation (`navigation`) oder nur einmal im Lebenszyklus der Anwendung (`render`). Der Standardwert ist `render`.
  - `render`: Führt einmal während der Initialisierung aus (entweder SSR oder CSR) - Standardmodus
  - `navigation`: Führt einmal während der Initialisierung und einmal pro weiteren clientseitigen Navigationen aus