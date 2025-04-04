---
title: 'createError'
description: Erstelle ein Fehlerobjekt mit zusätzlichen Metadaten.
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/error.ts
    size: xs
---

Du kannst diese Funktion verwenden, um ein Fehlerobjekt mit zusätzlichen Metadaten zu erstellen. Es ist in beiden Teilen deines Apps, dem Vue und dem Nitro Teil, nutzbar und soll geworfen werden.

## Parameter

- `err`: `string | { cause, data, message, name, stack, statusCode, statusMessage, fatal }`

Du kannst entweder einen String oder ein Objekt an die `createError` Funktion übergeben. Wenn du einen String übergeben, wird dieser als Fehler `message` verwendet, und der `statusCode` fällt standardmäßig auf `500`. Wenn du ein Objekt übergeben, kannst du mehrere Eigenschaften des Fehlers festlegen, wie z.B. `statusCode`, `message` und andere Fehler-Eigenschaften.

## In Vue-App

Wenn du einen Fehler mit `createError` werfst:

- auf dem Server wird eine vollbildige Fehlerseite ausgelöst, die du mit `clearError` löschen kannst.
- auf dem Client wird ein nicht-fataler Fehler ausgelöst, den du verarbeiten musst. Wenn du eine vollbildige Fehlerseite auslösen möchtest, kannst du dies durch Festlegen von `fatal: true` erreichen.

### Beispiel

```vue [pages/movies/[slug\\].vue]
<script setup lang="ts">
const route = useRoute()
const { data } = await useFetch(`/api/movies/${route.params.slug}`)
if (!data.value) {
  throw createError({ statusCode: 404, statusMessage: 'Seite nicht gefunden' })
}
</script>
```

## In API-Routen

Verwende `createError`, um Fehlerbehandlung in Server-API-Routen auszulösen.

### Beispiel

```ts [server/api/error.ts]
export default eventHandler(() => {
  throw createError({
    statusCode: 404,
    statusMessage: 'Seite nicht gefunden'
  })
})
```

In API-Routen wird empfohlen, `createError` mit einem Objekt und einer kurzen `statusMessage` zu verwenden, da diese auf dem Client zugänglich ist. Andernfalls wird ein `message`, der an einer API-Route an `createError` übergeben wird, nicht zum Client weitergeleitet. Alternativ kannst du die `data`-Eigenschaft verwenden, um Daten an den Client zurückzugeben. In jedem Fall solltest du immer darauf achten, dynamischen Benutzereingaben nicht in der Nachricht zu verwenden, um potenzielle Sicherheitsprobleme zu vermeiden.

:read-more{to="/docs/getting-started/error-handling"}
---