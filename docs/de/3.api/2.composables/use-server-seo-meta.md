---
title: 'useServerSeoMeta'
description: Das Composable `useServerSeoMeta` ermöglicht es Ihnen, die SEO-Meta-Tags Ihres Sites als flaches Objekt zu definieren mit vollständiger TypeScript-Unterstützung.
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/unjs/unhead/blob/main/packages/vue/src/composables.ts
    size: xs
---

Genau wie bei der [`useSeoMeta`](/docs/api/composables/use-seo-meta) kann das Composable `useServerSeoMeta` Ihre SEO-Meta-Tags als flaches Objekt mit vollständiger TypeScript-Unterstützung definieren.

:read-more{to="/docs/api/composables/use-seo-meta"}

Im meisten Fällen ist die Metadaten nicht reaktiv, da Roboter nur den Initial-Load scannen. Daher empfehlen wir, das Composable [`useServerSeoMeta`](/docs/api/composables/use-server-seo-meta) als leistungsorientierte Hilfsmittel zu verwenden, das auf dem Client nichts tut (oder einen `head`-Objekt zurückgibt).

```vue [app.vue]
<script setup lang="ts">
useServerSeoMeta({
  robots: 'index, follow'
})
</script>
```

Die Parameter sind genau wie bei der [`useSeoMeta`](/docs/api/composables/use-seo-meta) identisch.

:read-more{to="/docs/getting-started/seo-meta"}
---