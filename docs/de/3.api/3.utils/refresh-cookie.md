---
title: "refreshCookie"
description: "Manuelle Aktualisierung von useCookie-Werten, wenn ein Cookie geändert wurde"
navigation:
  badge: Neu
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/cookie.ts
    size: xs
---

::important
Diese Funktion ist ab [Nuxt v3.10](/blog/v3-10) verfügbar.
::

## Zweck

Die `refreshCookie`-Funktion dient dazu, den Cookie-Wert, der durch `useCookie` zurückgegeben wird, manuell zu aktualisieren.

Dies ist nützlich, um den `useCookie`-Ref zu aktualisieren, wenn wir wissen, dass der neue Cookie-Wert im Browser gesetzt wurde.

## Verwendung

```vue [app.vue]
<script setup lang="ts">
const tokenCookie = useCookie('token')

const login = async (username, password) => {
  const token = await $fetch('/api/token', { ... }) // Setzt den `token` Cookie auf Antwort
  refreshCookie('token')
}

const loggedIn = computed(() => !!tokenCookie.value)
</script>
```

::note{to="/docs/de/guide/going-further/experimental-features#cookiestore"}
Sie können das experimentelle `cookieStore`-Option aktivieren, um `useCookie`-Werte automatisch zu aktualisieren, wenn sich der Cookie im Browser ändert.
::

## Typ

```ts
refreshCookie(name: string): void
```