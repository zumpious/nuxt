---
title: 'useSeoMeta'
description: Das Composable `useSeoMeta` ermöglicht es Ihnen, die SEO-Meta-Tags Ihres Sites als flaches Objekt zu definieren, mit vollem TypeScript-Unterstützung.
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/unjs/unhead/blob/main/packages/vue/src/composables.ts
    size: xs
---

Dies hilft Ihnen dabei, häufige Fehler zu vermeiden, wie z.B. das Verwenden von `name` anstelle von `property`, sowie Tippfehler - mit über 100 vollständig typisierten Meta-Tags.

::important
Dies ist die empfohlene Methode zur Hinzufügung von Meta-Tags zu Ihrem Site, da es XSS-sicher ist und volle TypeScript-Unterstützung bietet.
::

:read-more{to="/docs/de/getting-started/seo-meta"}

## Verwendung

```vue [app.vue]
<script setup lang="ts">
useSeoMeta({
  title: 'Mein wunderbares Site',
  ogTitle: 'Mein wunderbares Site',
  description: 'Dies ist mein wunderbares Site, erzählen Sie mir alles darüber.',
  ogDescription: 'Dies ist mein wunderbares Site, erzählen Sie mir alles darüber.',
  ogImage: 'https://example.com/bild.png',
  twitterCard: 'summary_large_image',
})
</script>
```

Wenn Sie reaktive Tags einfügen, sollten Sie den berechneten Getter-Syntax (`() => value`) verwenden:

```vue [app.vue]
<script setup lang="ts">
const title = ref('Mein Titel')

useSeoMeta({
  title,
  description: () => `Dies ist eine Beschreibung für die Seite ${title.value}`
})
</script>
```

## Parameter

Es gibt über 100 Parameter. Siehe die [vollständige Liste der Parameter im Quellcode](https://github.com/harlan-zw/zhead/blob/main/packages/zhead/src/metaFlat.ts#L1035).

:read-more{to="/docs/de/getting-started/seo-meta"}

## Leistung

Im meisten Fällen müssen SEO-Meta-Tags nicht reaktiv sein, da Roboter von Suchmaschinen hauptsächlich die Anfangsladung des Seitenkörpers scannen.

Für bessere Leistung können Sie Ihre Aufrufe von `useSeoMeta` in eine Server-nur-Bedingung einwickeln, wenn die Meta-Tags nicht reaktiv sein müssen:

```vue [app.vue]
<script setup lang="ts">
if (import.meta.server) {
  // Diese Meta-Tags werden nur während der Serverseitigen Darstellung hinzugefügt
  useSeoMeta({
    robots: 'index, follow',
    description: 'Statische Beschreibung, die keine Reaktivität benötigt',
    ogImage: 'https://example.com/bild.png',
    // weitere statische Meta-Tags...
  })
}

const dynamischerTitel = ref('Mein Titel')
// Nennen Sie nur reaktive Meta-Tags außerhalb der Bedingung, wenn erforderlich
useSeoMeta({
  title: () => dynamischerTitel.value,
  ogTitle: () => dynamischerTitel.value,
})
</script>
```

Dies wurde früher mit dem Composable `useServerSeoMeta` verwendet, aber es wurde in diesem Ansatz deprecierter.
::