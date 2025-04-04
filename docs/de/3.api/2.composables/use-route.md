---
title: "useRoute"
description: Das Composable useRoute gibt die aktuelle Route zurück.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts
    size: xs
---

::note
Innerhalb des Templates eines Vue-Komponenten kann die Route mit `$route` zugegriffen werden.
::

## Beispiel

Im folgenden Beispiel rufen wir eine API über [`useFetch`](/docs/api/composables/use-fetch) ab, wobei ein dynamischer Seitenparameter - `slug` - Teil der URL ist.

```html [~/pages/[slug\\].vue]
<script setup lang="ts">
const route = useRoute()
const { data: mountain } = await useFetch(`/api/mountains/${route.params.slug}`)
</script>

<template>
  <div>
    <h1>{{ mountain.title }}</h1>
    <p>{{ mountain.description }}</p>
  </div>
</template>
```

Wenn Sie die Routenquery-Parameter (zum Beispiel `example` in der Pfad `/test?example=true`) zugreifen müssen, können Sie `useRoute().query` anstelle von `useRoute().params` verwenden.

## API

Außer dynamischen Parametern und Query-Parametern bietet `useRoute()` auch die folgenden berechneten Verweise zur aktuellen Route:

- `fullPath`: codierter URL-String, der die aktuelle Route enthält, einschließlich Pfad, Query und Hash
- `hash`: dekodierter Hash-Teil der URL, der mit einem # beginnt
- `query`: Zugriff auf die Routenquery-Parameter
- `matched`: Array normalisierter匹配的文本无法直接翻译，因为它包含了一个未完成的中文句子。正确的句子应该是：“如果需要访问路由查询参数（例如在路径 `/test?example=true` 中的 `example`），则可以使用 `useRoute().query` 而不是 `useRoute().params`。”

以下是完整的德文翻译：

---
title: "useRoute"
description: Das Composable useRoute gibt die aktuelle Route zurück.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts
    size: xs
---

::note
Innerhalb des Templates eines Vue-Komponenten kann die Route mit `$route` zugegriffen werden.
::

## Beispiel

Im folgenden Beispiel rufen wir eine API über [`useFetch`](/docs/api/composables/use-fetch) ab, wobei ein dynamischer Seitenparameter - `slug` - Teil der URL ist.

```html [~/pages/[slug\\].vue]
<script setup lang="ts">
const route = useRoute()
const { data: mountain } = await useFetch(`/api/mountains/${route.params.slug}`)
</script>

<template>
  <div>
    <h1>{{ mountain.title }}</h1>
    <p>{{ mountain.description }}</p>
  </div>
</template>
```

Wenn Sie die Routenquery-Parameter (zum Beispiel `example` in der Pfad `/test?example=true`) zugreifen müssen, können Sie `useRoute().query` anstelle von `useRoute().params` verwenden.

## API

Außer dynamischen Parametern und Query-Parametern bietet `useRoute()` auch die folgenden berechneten Verweise zur aktuellen Route:

- `fullPath`: codierter URL-String, der die aktuelle Route enthält, einschließlich Pfad, Query und Hash
- `hash`: dekodierter Hash-Teil der URL, der mit einem # beginnt
- `query`: Zugriff auf die Routenquery-Parameter
- `matched`: Array normalisierter matched Routes mit der aktuellen Route-Position
- `meta`: benutzerdefinierte Daten, die dem Record angehängt sind
- `name`: eindeutiger Name für das Route-Record
- `path`: codierter Pfad-Teil der URL
- `redirectedFrom`: Route-Position, die versucht wurde zu erreichen, bevor die aktuelle Route-Position erreicht wurde

::note
Browser senden [URL-Fragmente](https://url.spec.whatwg.org/#concept-url-fragment) (zum Beispiel `#foo`) bei Anfragen nicht. Daher können `route.fullPath` im Template verwenden, um Hydrationsprobleme auslösen, da dies den Fragment-Teil auf dem Client enthält, aber nicht auf dem Server.
::

:read-more{icon="i-simple-icons-vuedotjs" to="https://router.vuejs.org/api/#RouteLocationNormalizedLoaded"}