---
title: useHeadSafe
description: Die empfohlene Methode zur Bereitstellung von Kopfdaten mit Benutzereingaben.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/unjs/unhead/blob/main/packages/vue/src/composables.ts
    size: xs
---

Das Komponentenwrapper `useHeadSafe` ist ein Wrapper um das Komponentenwrapper [`useHead`](/docs/api/composables/use-head), das die Eingaben auf sicherer Werte beschränkt.

## Verwendung

Sie können alle gleichen Werte wie bei [`useHead`](/docs/api/composables/use-head) übergeben.

```ts
useHeadSafe({
  script: [
    { id: 'xss-script', innerHTML: 'alert("xss")' }
  ],
  meta: [
    { 'http-equiv': 'refresh', content: '0;javascript:alert(1)' }
  ]
})
// Wird sicher generiert
// <script id="xss-script"></script>
// <meta content="0;javascript:alert(1)">
```

::read-more{to="https://unhead.unjs.io/docs/typescript/head/api/composables/use-head-safe" target="_blank"}
Weitere Informationen finden Sie im Dokumentationswerk der `Unhead`.
::

## Typ

```ts
useHeadSafe(input: MaybeComputedRef<HeadSafe>): void
```

Die Liste der erlaubten Werte ist:

```ts
const WhitelistAttributes = {
  htmlAttrs: ['class', 'style', 'lang', 'dir'],
  bodyAttrs: ['class', 'style'],
  meta: ['name', 'property', 'charset', 'content', 'media'],
  noscript: ['textContent'],
  style: ['media', 'textContent', 'nonce', 'title', 'blocking'],
  script: ['type', 'textContent', 'nonce', 'blocking'],
  link: ['color', 'crossorigin', 'fetchpriority', 'href', 'hreflang', 'imagesrcset', 'imagesizes', 'integrity', 'media', 'referrerpolicy', 'rel', 'sizes', 'type'],
}
```

Weitere detaillierte Typen finden Sie unter [@unhead/vue](https://github.com/unjs/unhead/blob/main/packages/vue/src/types/safeSchema.ts).
---