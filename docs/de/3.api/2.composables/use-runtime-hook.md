---
title: useRuntimeHook
description: Registriert ein Laufzeit-Hook in einer Nuxt-Anwendung und stellt sicher, dass es ordnungsgemäß abgebrochen wird, wenn der Scope zerstört wird.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/runtime-hook.ts
    size: xs
---

::important
Diese Komponente ist ab Nuxt v3.14 verfügbar.
::

```ts [Signature]
function useRuntimeHook<THookName extends keyof RuntimeNuxtHooks>(
  name: THookName,
  fn: RuntimeNuxtHooks[THookName] extends HookCallback ? RuntimeNuxtHooks[THookName] : never
): void
```

## Verwendung

### Parameter

- `name`: Der Name des zu registrierenden Laufzeit-Hooks. Siehe die vollständige Liste der [Laufzeit-Nuxt-Hooks hier](/docs/api/advanced/hooks#app-hooks-runtime).
- `fn`: Die Callback-Funktion, die ausgeführt wird, wenn der Hook ausgelöst wird. Die Funktionssignatur variiert je nach Hook-Name.

### Rückgabewert

Die Komponente gibt keinen Wert zurück, aber sie löst den Hook automatisch ab, wenn das Scope des Komponenten-Scopes zerstört wird.

## Beispiel

```vue twoslash [pages/index.vue]
<script setup lang="ts">
// Registriere einen Hook, der jedes Mal ausgeführt wird, wenn eine Verknüpfung vorab geladen wird, aber dieser wird automatisch bereinigt (und nicht erneut aufgerufen) sein, wenn das Komponenten-Scope zerstört wird
useRuntimeHook('link:prefetch', (link) => {
  console.log('Vorab-Laden von', link)
})
</script>
```