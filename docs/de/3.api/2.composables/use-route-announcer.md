---
title: 'useRouteAnnouncer'
description: Dieses Komponentenbeispiel beobachtet Änderungen am Seitentitel und aktualisiert den Anzeigemeldungsnachricht entsprechend.
navigation:
  badge: Neu
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/route-announcer.ts
    size: xs
---

::important
Dieses Komponentenbeispiel ist ab Nuxt v3.12 verfügbar.
::

## Beschreibung

Ein Komponentenbeispiel, das die Änderungen am Seitentitel beobachtet und die Anzeigemeldungsnachricht entsprechend aktualisiert. Es wird von [`<NuxtRouteAnnouncer>`](/docs/api/components/nuxt-route-announcer) verwendet und steuerbar. Es hookt sich in Unheads [`dom:rendered`](https://unhead.unjs.io/docs/typescript/head/api/hooks/dom-rendered) ein, um den Seitentitel zu lesen und als Anzeigemeldungsnachricht festzulegen.

## Parameter

- `politeness`: Legt die Dringlichkeit für die Meldungen von Screenreadern fest: `off` (deaktiviert die Meldung), `polite` (wartet auf Stille) oder `assertive` (unterbricht sofort). (Standardwert: `polite`).

## Eigenschaften

### `message`

- **Typ**: `Ref<string>`
- **Beschreibung**: Die zu ankündigende Nachricht

### `politeness`

- **Typ**: `Ref<string>`
- **Beschreibung**: Dringlichkeitsstufe der Meldung für Screenreadereinrichtungen `off`, `polite` oder `assertive`

## Methoden

### `set(message, politeness = "polite")`

Setzt die zu ankündige Nachricht mit ihrer Dringlichkeitsstufe.

### `polite(message)`

Setzt die Nachricht mit `politeness = "polite"`

### `assertive(message)`

Setzt die Nachricht mit `politeness = "assertive"`

## Beispiel

```vue [pages/index.vue]
<script setup lang="ts">
  const { message, politeness, set, polite, assertive } = useRouteAnnouncer({
    politeness: 'assertive'
  })
</script>
```