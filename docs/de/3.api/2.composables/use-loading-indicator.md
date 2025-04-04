---
title: 'useLoadingIndicator'
description: Diese Komponente gibt Ihnen Zugriff auf den Ladezustand der App-Seite.
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/loading-indicator.ts
    size: xs
---

## Beschreibung

Eine Komponente, die den Ladezustand der Seite zurückgibt. Wird von [`<NuxtLoadingIndicator>`](/docs/api/components/nuxt-loading-indicator) verwendet und steuerbar. Sie hookt sich in [`page:loading:start`](/docs/api/advanced/hooks#app-hooks-runtime) und [`page:loading:end`](/docs/api/advanced/hooks#app-hooks-runtime) ein, um seinen Zustand zu ändern.

## Parameter

- `duration`: Ladebalkendauer in Millisekunden (Standardwert `2000`).
- `throttle`: Verzögert das Erscheinen und Verschwinden, in Millisekunden (Standardwert `200`).
- `estimatedProgress`: Standardmäßig reduziert Nuxt sich bei Annäherung an 100%. Sie können eine benutzerdefinierte Funktion zur Anpassung des Fortschritts bereitstellen, die eine Funktion ist, die die Ladebalkendauer (oben) und die verstrichene Zeit erhält. Sie sollte einen Wert zwischen 0 und 100 zurückgeben.

## Eigenschaften

### `isLoading`

- **Typ**: `Ref<boolean>`
- **Beschreibung**: Der Ladezustand

### `error`

- **Typ**: `Ref<boolean>`
- **Beschreibung**: Der Fehlerzustand

### `progress`

- **Typ**: `Ref<number>`
- **Beschreibung**: Der Fortschrittszustand. Von `0` bis `100`.

## Methoden

### `start()`

Setzt `isLoading` auf `true` und beginnt damit, den `progress`-Wert zu erhöhen. `start` akzeptiert eine Option `{ force: true }`, um die Intervalle zu überspringen und den Ladezustand sofort zu zeigen.

### `set()`

Setzt den `progress`-Wert auf einen bestimmten Wert. `set` akzeptiert eine Option `{ force: true }`, um die Intervalle zu überspringen und den Ladezustand sofort zu zeigen.

### `finish()`

Setzt den `progress`-Wert auf `100`, stoppt alle Timer und Intervalle, dann setzt den Ladezustand `500` ms später zurück. `finish` akzeptiert eine Option `{ force: true }`, um die Intervalle vor dem Zurücksetzen des Zustands zu überspringen, und `{ error: true }`, um die Farbe des Ladebalkens zu ändern und den Fehlerzustand auf `true` zu setzen.

### `clear()`

Wird von `finish()` verwendet. Löscht alle Timer und Intervalle, die von der Komponente verwendet werden.

## Beispiel

```vue
<script setup lang="ts">
  const { progress, isLoading, start, finish, clear } = useLoadingIndicator({
    duration: 2000,
    throttle: 200,
    // Dies ist die Standardmethode, wie der Fortschritt berechnet wird
    estimatedProgress: (duration, elapsed) => (2 / Math.PI * 100) * Math.atan(elapsed / duration * 100 / 50)
  })
</script>
```

```vue
<script setup lang="ts">
  const { start, set } = useLoadingIndicator()
  // Gleichbedeutend mit set(0, { force: true })
  // Setze den Fortschritt auf 0 und zeige den Ladezustand sofort an
  start({ force: true })
</script>
```