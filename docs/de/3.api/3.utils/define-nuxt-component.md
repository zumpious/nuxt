---
title: "defineNuxtComponent"
description: defineNuxtComponent() ist eine Hilfsfunktion zur Definition von typesicher Vue-Components mit der Options-API.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/component.ts
    size: xs
---

::note
`defineNuxtComponent()` ist eine Hilfsfunktion zur Definition von typesicher Vue-Components mithilfe der Options-API, ähnlich wie die Funktion [`defineComponent()`](https://vuejs.org/api/general.html#definecomponent). Der Wrapper von `defineNuxtComponent()` bietet auch Unterstützung für die Optionen `asyncData` und `head`.
::

::note
Die Verwendung von `<script setup lang="ts">` ist die empfohlene Art, Vue-Components in Nuxt zu deklarieren.
::

:read-more{to=/docs/getting-started/data-fetching}

## `asyncData()`

Wenn Sie `setup()` in Ihrem App nicht verwenden möchten, können Sie den `asyncData()`-Methodenaufruf in Ihrer Komponentendefinition verwenden:

```vue [pages/index.vue]
<script lang="ts">
export default defineNuxtComponent({
  async asyncData() {
    return {
      data: {
        grüße: 'hallo Welt!'
      }
    }
  },
})
</script>
```

## `head()`

Wenn Sie `setup()` in Ihrem App nicht verwenden möchten, können Sie den `head()`-Methodenaufruf in Ihrer Komponentendefinition verwenden:

```vue [pages/index.vue]
<script lang="ts">
export default defineNuxtComponent({
  head(nuxtApp) {
    return {
      title: 'Mein Site'
    }
  },
})
</script>
```