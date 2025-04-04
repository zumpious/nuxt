---
title: "usePreviewMode"
description: "Verwenden Sie usePreviewMode, um den Vorschau-Modus in Nuxt zu überprüfen und zu steuern."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/preview.ts
    size: xs
---

# `usePreviewMode`

Der Vorschau-Modus ermöglicht es Ihnen, wie Ihre Änderungen auf einer Live-Seite angezeigt werden würden, ohne sie den Benutzern zu offenbaren.

Sie können die eingebaute `usePreviewMode` Komponente verwenden, um den Vorschauzustand in Nuxt abzurufen und zu steuern. Wenn die Komponente den Vorschau-Modus erkennt, wird automatisch jedes erforderliche Update für [`useAsyncData`](/docs/api/composables/use-async-data) und [`useFetch`](/docs/api/composables/use-fetch) zur Wiedergabe des Vorschauinhalts erzwungen.

```js
const { enabled, state } = usePreviewMode()
```

## Optionen

### Benutzerdefinierte `enable`-Prüfung

Sie können eine benutzerdefinierte Methode zum Aktivieren des Vorschau-Modus angeben. Standardmäßig wird die `usePreviewMode` Komponente aktiviert, wenn der `preview`-Parameter in der URL gleich `true` ist (z.B. `http://localhost:3000?preview=true`). Sie können die `usePreviewMode` in eine benutzerdefinierte Komponente einpacken, um Optionen konsistent überall zu halten und Fehler zu vermeiden.

```js
export function useMyPreviewMode () {
  return usePreviewMode({
    shouldEnable: () => {
      return !!route.query.customPreview
    }
  });
}
```

### Ändern des Standardzustands

Die `usePreviewMode` Komponente versucht, den Wert des `token`-Parameters aus der URL im Zustand zu speichern. Sie können diesen Zustand ändern, und er wird für alle Aufrufe von [`usePreviewMode`](/docs/api/composables/use-preview-mode) verfügbar sein.

```js
const data1 = ref('data1')

const { enabled, state } = usePreviewMode({
  getState: (currentState) => {
    return { data1, data2: 'data2' }
  }
})
```

::note
Die `getState`-Funktion fügt die zurückgegebenen Werte dem aktuellen Zustand hinzu, achten Sie daher darauf, nicht zufällig wichtigen Zustand zu überschreiben.
::

### Anpassen der `onEnable` und `onDisable`-Callbacks

Standardmäßig wird, wenn `usePreviewMode` aktiviert wird, `refreshNuxtData()` aufgerufen, um alle Daten vom Server neu abzurufen.

Wenn der Vorschau-Modus deaktiviert wird, wird das Modul einen Callback hinzufügen, der nach einer folgenden Routen-Navigation `refreshNuxtData()` aufruft.

Sie können benutzerdefinierte Callbacks angeben, indem Sie eigene Funktionen für die `onEnable` und `onDisable`-Optionen bereitstellen.

```js
const { enabled, state } = usePreviewMode({
  onEnable: () => {
    console.log('Vorschau-Modus wurde aktiviert')
  },
  onDisable: () => {
    console.log('Vorschau-Modus wurde deaktiviert')
  }
})
```

## Beispiel

Das folgende Beispiel erstellt eine Seite, bei der ein Teil des Inhalts nur im Vorschau-Modus angezeigt wird.

```vue [pages/some-page.vue]
<script setup>
const { enabled, state } = usePreviewMode()

const { data } = await useFetch('/api/preview', {
  query: {
    apiKey: state.token
  }
})
</script>

<template>
  <div>
    Einige Basisinhalte
    <p v-if="enabled">
      Nur Vorschau-Inhalt: {{ state.token }}
      <br>
      <button @click="enabled = false">
        Vorschau-Modus deaktivieren
      </button>
    </p>
  </div>
</template>
```

Jetzt können Sie Ihr Projekt generieren und starten:

```bash [Terminal]
npx nuxi generate
npx nuxi preview
```

Dann können Sie Ihren Vorschau-Modus durch Hinzufügen des Query-Params `preview` an die Seite sehen, die Sie anzeigen möchten:

```js
?preview=true
```

::note
`usePreviewMode` sollte lokal mit `nuxi generate` und dann `nuxi preview` getestet werden, nicht mit `nuxi dev`. (Der [Vorschau-Befehl](/docs/api/commands/preview) ist nicht mit dem Vorschau-Modus verbunden.)
::
---