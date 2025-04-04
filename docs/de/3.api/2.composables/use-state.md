---
title: "useState"
description: Das useState-Komponenten erstellt ein reaktives und SSR-freundliches gemeinsames State.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/state.ts
    size: xs
---

## Verwendung

```ts
// Erstellt ein reaktives State mit Standardwert
const count = useState('counter', () => Math.round(Math.random() * 100))
```

:read-more{to="/docs/getting-started/state-management"}

::important
Da die Daten innerhalb von `useState` serialisiert werden, ist es wichtig, dass sie nichts enthalten, was nicht serialisiert werden kann, wie z.B. Klassen, Funktionen oder Symbole.
::

::warning
`useState` ist eine reservierte Funktionsname, der vom Compiler transformiert wird, daher sollten Sie Ihre eigene Funktion nicht `useState` heißen.
::

::tip{icon="i-lucide-video" to="https://www.youtube.com/watch?v=mv0WcBABcIk" target="_blank"}
Schauen Sie sich einen Video von Alexander Lichter an, in dem er erklärt, wann und warum man `useState()` verwenden sollte.
::

## Verwenden von `shallowRef`

Wenn Sie Ihr State nicht tief reaktiv haben möchten, können Sie `useState` mit [`shallowRef`](https://vuejs.org/api/reactivity-advanced.html#shallowref) kombinieren. Dies kann die Leistung verbessern, wenn Ihr State große Objekte und Arrays enthält.

```ts
const state = useState('my-shallow-state', () => shallowRef({ deep: 'not reactive' }))
// isShallow(state) === true
```

## Typ

```ts
useState<T>(init?: () => T | Ref<T>): Ref<T>
useState<T>(key: string, init?: () => T | Ref<T>): Ref<T>
```

- `key`: Ein eindeutiger Schlüssel, der sicherstellt, dass die Datenabfrage korrekt dedupliziert wird. Wenn Sie keinen Schlüssel angeben, wird Ihnen ein eindeutiger Schlüssel basierend auf Datei- und Zeilennummer von [`useState`](/docs/api/composables/use-state) generiert.
- `init`: Eine Funktion, die den Anfangswert für das State bereitstellt, wenn es nicht initialisiert wurde. Diese Funktion kann auch ein `Ref` zurückgeben.
- `T`: (nur TypeScript) Gibt den Typ des States an
::