---
title: useHead
description: useHead personalisiert die Kopfzeigenschaften von einzelnen Seiten Ihres Nuxt-Anwendungsprogramms.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/unjs/unhead/blob/main/packages/vue/src/composables.ts
    size: xs
---

Der Kompositionsfunktion [`useHead`](/docs/api/composables/use-head) ermöglicht es Ihnen, Ihre Kopfzeichen in einem programmgesteuerten und reaktiven Modus zu verwalten, unterstützt durch [Unhead](https://unhead.unjs.io). Wenn die Daten von einem Benutzer oder einer anderen unvertrauenswürdigen Quelle stammen, empfehlen wir Ihnen, sich auch mit der Kompositionsfunktion [`useHeadSafe`](/docs/api/composables/use-head-safe) auszuweisen.

:read-more{to="/docs/getting-started/seo-meta"}

## Typ

```ts
useHead(meta: MaybeComputedRef<MetaObject>): void
```

Unten sind die nicht-reactiven Typen für [`useHead`](/docs/api/composables/use-head) aufgeführt.

```ts
interface MetaObject {
  title?: string
  titleTemplate?: string | ((title?: string) => string)
  base?: Base
  link?: Link[]
  meta?: Meta[]
  style?: Style[]
  script?: Script[]
  noscript?: Noscript[]
  htmlAttrs?: HtmlAttributes
  bodyAttrs?: BodyAttributes
}
```

Siehe [@unhead/vue](https://github.com/unjs/unhead/blob/main/packages/vue/src/types/schema.ts) für detaillierte Typen.

::note
Die Eigenschaften von `useHead` können dynamisch sein und akzeptieren `ref`, `computed` und `reactive` Eigenschaften. Der `meta` Parameter kann auch eine Funktion akzeptieren, die ein Objekt zurückgibt, um das gesamte Objekt reaktiv zu machen.
::

## Parameter

### `meta`

**Typ**: `MetaObject`

Ein Objekt, das die folgenden Kopfmetadaten akzeptiert:

- `meta`: Jedes Element im Array wird zu einem neu erstellten `<meta>`-Tag gemappt, wobei die Objekteigenschaften auf die entsprechenden Attribute gemappt werden.
  - **Typ**: `Array<Record<string, any>>`
- `link`: Jedes Element im Array wird zu einem neu erstellten `<link>`-Tag gemappt, wobei die Objekteigenschaften auf die entsprechenden Attribute gemappt werden.
  - **Typ**: `Array<Record<string, any>>`
- `style`: Jedes Element im Array wird zu einem neu erstellten `<style>`-Tag gemappt, wobei die Objekteigenschaften auf die entsprechenden Attribute gemappt werden.
  - **Typ**: `Array<Record<string, any>>`
- `script`: Jedes Element im Array wird zu einem neu erstellten `<script>`-Tag gemappt, wobei die Objekteigenschaften auf die entsprechenden Attribute gemappt werden.
  - **Typ**: `Array<Record<string, any>>`
- `noscript`: Jedes Element im Array wird zu einem neu erstellten `<noscript>`-Tag gemappt, wobei die Objekteigenschaften auf die entsprechenden Attribute gemappt werden.
  - **Typ**: `Array<Record<string, any>>`
- `titleTemplate`: Konfiguriert einen dynamischen Vorlage, um die Seitentitel individuell anzupassen.
  - **Typ**: `string` | `((title: string) => string)`
- `title`: Setzt einen statischen Seitentitel für eine individuelle Seite.
  - **Typ**: `string`
- `bodyAttrs`: Setzt Attribute des `<body>`-Tags. Jede Objekteigenschaft wird auf das entsprechende Attribut gemappt.
  - **Typ**: `Record<string, any>`
- `htmlAttrs`: Setzt Attribute des `<html>`-Tags. Jede Objekteigenschaft wird auf das entsprechende Attribut gemappt.
  - **Typ**: `Record<string, any>`
```