---
title: "onPrehydrate"
description: "Verwenden Sie onPrehydrate, um einen Callback auf dem Client sofort vor der Hydratierung der Seite durch Nuxt auszuführen."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts
    size: xs
---

::important
Diese Komponente ist ab Nuxt v3.12 verfügbar.
::

`onPrehydrate` ist ein Lebenszyklus-Hook, der es Ihnen ermöglicht, einen Callback auf dem Client sofort vor der Hydratierung der Seite durch Nuxt auszuführen.

::note
Dies ist eine fortgeschrittene Hilfsmittel und sollte mit Vorsicht verwendet werden. Zum Beispiel manipulieren [`nuxt-time`](https://github.com/danielroe/nuxt-time/pull/251) und [`@nuxtjs/color-mode`](https://github.com/nuxt-modules/color-mode/blob/main/src/script.js) den DOM, um Hydrations-Unstimmigkeiten zu vermeiden.
::

## Verwendung

`onPrehydrate` kann direkt im Setup-Funktion einer Vue-Komponente (zum Beispiel in `<script setup>`) oder in einem Plugin aufgerufen werden. Es wird nur dann wirksam, wenn es auf dem Server aufgerufen wird, und es wird nicht in Ihrer Client-Build enthalten sein.

## Parameter

- `callback`: Eine Funktion, die in der HTML-Datei kodiert und eingebunden wird. Sie sollte keine externen Abhängigkeiten (wie automatische Imports) oder Verweise auf Variablen außerhalb des Callbacks haben. Die Callback-Funktion wird vor der Initialisierung des Nuxt-Runtime ausgeführt, sodass sie auf das Nuxt oder Vue-Kontext nicht angewiesen sein sollte.

## Beispiel

```vue twoslash [app.vue]
<script setup lang="ts">
declare const window: Window
// ---cut---
// onPrehydrate wird sichergestellt, dass er vor der Hydratierung von Nuxt ausgeführt wird
onPrehydrate(() => {
  console.log(window)
})

// Solange es nur ein Wurzelelement hat, können Sie den Elementzugriff nutzen
onPrehydrate((el) => {
  console.log(el.outerHTML)
  // <div data-v-inspector="app.vue:15:3" data-prehydrate-id=":b3qlvSiBeH:"> Hi there </div>
})

// Für sehr fortschrittliche Anwendungen (zum Beispiel ohne ein einzelnes Wurzelelement) können Sie `data-prehydrate-id` selbst zugreifen/ändern
const prehydrateId = onPrehydrate((el) => {})
</script>

<template>
  <div>
    Hi there
  </div>
</template>
```

Bitte beachten Sie, dass der Inhalt der Codeblöcke und Links unverändert bleibt.