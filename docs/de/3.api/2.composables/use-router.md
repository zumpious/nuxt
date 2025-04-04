---
title: "useRouter"
description: "Das useRouter-Komponenten gibt das Router-Instanz zurück."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts
    size: xs
---

```vue [pages/index.vue]
<script setup lang="ts">
const router = useRouter()
</script>
```

Wenn Sie den Router nur im Template benötigen, verwenden Sie `$router`:

```vue [pages/index.vue]
<template>
  <button @click="$router.back()">Zurück</button>
</template>
```

Wenn Sie eine `pages/` Verzeichnis haben, ist `useRouter` im Verhalten identisch zu dem, das von `vue-router` bereitgestellt wird.

::read-more{icon="i-simple-icons-vuedotjs" to="https://router.vuejs.org/api/interfaces/Router.html#Properties-currentRoute" target="_blank"}
Lesen Sie die Dokumentation zum `Router`-Interface in der `vue-router`-Dokumentation.
::

## Grundlegende Manipulation

- [`addRoute()`](https://router.vuejs.org/api/interfaces/Router.html#addRoute): Fügt ein neues Routenobjekt zur Router-Instanz hinzu. Der Parameter `parentName` kann verwendet werden, um ein neues Routenobjekt als Kind eines bestehenden Routenschemas hinzuzufügen.
- [`removeRoute()`](https://router.vuejs.org/api/interfaces/Router.html#removeRoute): Entfernt ein bestehendes Routenobjekt über seinen Namen.
- [`getRoutes()`](https://router.vuejs.org/api/interfaces/Router.html#getRoutes): Gibt eine vollständige Liste aller Routenobjekte zurück.
- [`hasRoute()`](https://router.vuejs.org/api/interfaces/Router.html#hasRoute): Prüft, ob ein Routenobjekt mit einem bestimmten Namen existiert.
- [`resolve()`](https://router.vuejs.org/api/interfaces/Router.html#resolve): Gibt die normalisierte Version einer Routenposition zurück. Inkludiert auch eine `href`-Eigenschaft, die den aktuellen Pfad enthält.

```ts [Beispiel]
const router = useRouter()

router.addRoute({ name: 'home', path: '/home', component: Home })
router.removeRoute('home')
router.getRoutes()
router.hasRoute('home')
router.resolve({ name: 'home' })
```

::note
`router.addRoute()` fügt Routendetails in eine Liste von Routen hinzu und ist nützlich, wenn man Nuxt-Plugins erstellt. `router.push()`, andererseits, startet sofort eine neue Navigation und ist nützlich in Seiten, Vue-Komponenten und Komponenten.
::

## Basierend auf History-API

- [`back()`](https://router.vuejs.org/api/interfaces/Router.html#back): Gehe in die Vergangenheit zurück, sofern möglich, gleichbedeutend mit `router.go(-1)`.
- [`forward()`](https://router.vuejs.org/api/interfaces/Router.html#forward): Gehe in die Zukunft vorwärts, sofern möglich, gleichbedeutend mit `router.go(1)`.
- [`go()`](https://router.vuejs.org/api/interfaces/Router.html#go): Bewege sich durch die Geschichte vorwärts oder rückwärts, ohne die hierarchischen Einschränkungen, die in `router.back()` und `router.forward()` angewendet werden.
- [`push()`](https://router.vuejs.org/api/interfaces/Router.html#push): Programmgesteuertes Navigieren zu einer neuen URL durch Hinzufügen einer neuen Eintrag in die Historie. **Es wird empfohlen, stattdessen `navigateTo` zu verwenden.**
- [`replace()`](https://router.vuejs.org/api/interfaces/Router.html#replace): Programmgesteuertes Navigieren zu einer neuen URL durch Ersetzen des aktuellen Eintrags in der Historie. **Es wird empfohlen, stattdessen `navigateTo` zu verwenden.**

```ts [Beispiel]
const router = useRouter()

router.back()
router.forward()
router.go(3)
router.push({ path: "/home" })
router.replace({ hash: "#bio" })
```

::read-more{icon="i-simple-icons-mdnwebdocs" to="https://developer.mozilla.org/en-US/docs/Web/API/History" target="_blank"}
Weitere Informationen zur Browser-History-API.
::

## Navigation-Gardinen

Das `useRouter`-Komponenten bietet die Hilfsmethoden `afterEach`, `beforeEach` und `beforeResolve`, die als Navigation-Gardinen fungieren.

Allerdings hat Nuxt das Konzept von **Route-Middleware**, das die Implementierung von Navigation-Gardinen vereinfacht und eine bessere Benutzererfahrung bietet.

::read-more{to="/docs/guide/directory-structure/middleware"}

## Versprechen und Fehlerbehandlung

- [`isReady()`](https://router.vuejs.org/api/interfaces/Router.html#isReady): Gibt ein Versprechen zurück, das sich löst, wenn der Router die initiale Navigation abgeschlossen hat.
- [`onError`](https://router.vuejs.org/api/interfaces/Router.html#onError): Fügt einen Fehlerbehandler hinzu, der jedes Mal aufgerufen wird, wenn während der Navigation ein nicht gefangener Fehler auftritt.

::read-more{icon="i-simple-icons-vuedotjs" to="https://router.vuejs.org/api/interfaces/Router.html#Methods" title="Vue Router-Dokumentation" target="_blank"}

## Universal Router-Instanz

Wenn Sie kein `pages/` Verzeichnis haben, gibt `useRouter` ([/docs/api/composables/use-router](/docs/api/composables/use-router)) eine universelle Router-Instanz zurück, die ähnliche Hilfsmethoden bereitstellt, aber beachten Sie, dass nicht alle Funktionen möglicherweise unterstützt werden oder genau so funktionieren wie bei `vue-router`.