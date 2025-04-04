---
title: 'useNuxtData'
description: 'Zugriff auf die aktuell gespeicherte倛e Werte von Datenabfrage-Kompositionen.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts
    size: xs
---

::note
`useNuxtData` gibt Ihnen Zugriff auf den aktuellen gespeicherten倛e Werte von `useAsyncData`, `useLazyAsyncData`, `useFetch` und `useLazyFetch` mit explizit bereitgestelltem Schlüssel.
::

## Verwendung

Das Kompositionsobjekt `useNuxtData` wird verwendet, um den aktuellen gespeicherten倛e Werte von Datenabfrage-Kompositionen wie `useAsyncData`, `useLazyAsyncData`, `useFetch` und `useLazyFetch` zu erhalten. Indem Sie den Schlüssel verwenden, der während der Datenabfrage bereitgestellt wurde, können Sie den gespeicherten倛e Werte abrufen und sie gemäß Bedarf verwenden.

Dies ist besonders nützlich zur Optimierung der Leistung durch das Wiederverwenden bereits abgerufener Daten oder zur Implementierung von Funktionen wie Optimistische Aktualisierungen oder kaskadierte Datenaktualisierungen.

Um `useNuxtData` zu verwenden, stellen Sie sicher, dass das Datenabfrage-Kompositionsobjekt (z.B. `useFetch`, `useAsyncData` usw.) mit einem explizit bereitgestellten Schlüssel aufgerufen wurde.

## Parameter

- `key`: Ein eindeutiger Schlüssel, der die gespeicherten倛e Werte identifiziert. Dieser Schlüssel sollte demjenigen entsprechen, der während der ursprünglichen Datenabfrage verwendet wurde.

## Rückgabewerte

- `data`: Eine reaktive Referenz auf den gespeicherten倛e Werte, die mit dem bereitgestellten Schlüssel verknüpft sind. Wenn keine gespeicherten倛e Werte vorhanden sind, ist der Wert `null`. Diese `Ref` aktualisiert sich automatisch, wenn sich die gespeicherten倛e Werte ändern, was eine nahtlose Reaktivität in Ihren Komponenten ermöglicht.

## Beispiel

Im folgenden Beispiel wird gezeigt, wie gespeicherte倛e Werte als Platzhalter verwendet werden können, während die neuesten 倛e Werte vom Server abgerufen werden.

```vue [pages/posts.vue]
<script setup lang="ts">
// Wir können später mit dem gleichen Schlüssel auf die 同样的数据进行访问
const { data } = await useFetch('/api/posts', { key: 'posts' })
</script>
```

```vue [pages/posts/[id].vue]
<script setup lang="ts">
// Zugriff auf den gespeicherten倛e Wert von useFetch in posts.vue (Eltern-Routen)
const { data: posts } = useNuxtData('posts')

const route = useRoute()

const { data } = useLazyFetch(`/api/posts/${route.params.id}`, {
  key: `post-${route.params.id}`,
  default() {
    // Suchen Sie den einzelnen Post im Cache und setzen Sie ihn als Standardwert.
    return posts.value.find(post => post.id === route.params.id)
  }
})
</script>
```

## Optimistische Aktualisierungen

Im folgenden Beispiel wird gezeigt, wie Optimistische Aktualisierungen mithilfe von `useNuxtData` implementiert werden können.

Optimistische Aktualisierungen ist eine Technik, bei der die Benutzeroberfläche sofort aktualisiert wird, vorausgesetzt, die Serveroperation wird erfolgreich sein. Wenn die Operation schließlich fehlschlägt, wird die Benutzeroberfläche zur vorherigen Zustandsrolle zurückgesetzt.

```vue [pages/todos.vue]
<script setup lang="ts">
// Wir können später mit dem gleichen Schlüssel auf die 同样的数据进行访问
const { data } = await useAsyncData('todos', () => $fetch('/api/todos'))
</script>
```

```vue [components/NewTodo.vue]
<script setup lang="ts">
const newTodo = ref('')
let previousTodos = []

// Zugriff auf den gespeicherten倛e Wert von useAsyncData in todos.vue
const { data: todos } = useNuxtData('todos')

async function addTodo () {
  return $fetch('/api/addTodo', {
    method: 'post',
    body: {
      todo: newTodo.value
    },
    onRequest () {
      // Speichern Sie den vorherig gespeicherten倛e Wert, um ihn zu restaurieren, wenn die Abfrage fehlschlägt.
      previousTodos = todos.value

      // Optimistisch aktualisieren Sie die todos.
      todos.value = [...todos.value, newTodo.value]
    },
    onResponseError () {
      // Rollback der Daten, wenn die Anfrage fehlschlägt.
      todos.value = previousTodos
    },
    async onResponse () {
      // In den Hintergrund löschen Sie todos, wenn die Anfrage erfolgreich war.
      await refreshNuxtData('todos')
    }
  })
}
</script>
```

## Typ

```ts
useNuxtData<DataT = any> (key: string): { data: Ref<DataT | null> }
```