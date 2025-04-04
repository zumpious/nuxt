---
title: 'useRuntimeConfig'
description: 'Zugriff auf Laufzeit-Konfigurationsvariablen mit dem Composable useRuntimeConfig.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts
    size: xs
---

## Verwendung

```vue [app.vue]
<script setup lang="ts">
const config = useRuntimeConfig()
</script>
```

```ts [server/api/foo.ts]
export default defineEventHandler((event) => {
  const config = useRuntimeConfig(event)
})
```

:read-more{to="/docs/de/guide/going-further/runtime-config"}

## Definieren von Laufzeit-Konfigurationen

Das folgende Beispiel zeigt, wie man eine öffentliche API-Basis-URL und einen geheimen API-Token definiert, der nur auf dem Server zugänglich ist.

Wir sollten immer `runtimeConfig`-Variablen innerhalb von `nuxt.config` definieren.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  runtimeConfig: {
    // Geheime Schlüssel sind nur auf dem Server verfügbar
    apiSecret: '123',

    // Öffentliche Schlüssel, die dem Client zugänglich sind
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || '/api'
    }
  }
})
```

::note
Variablen, die auf dem Server zugänglich sein müssen, werden direkt innerhalb von `runtimeConfig` hinzugefügt. Variablen, die sowohl auf dem Client als auch auf dem Server zugänglich sein müssen, werden in `runtimeConfig.public` definiert.
::

:read-more{to="/docs/de/guide/going-further/runtime-config"}

## Zugreifen auf Laufzeit-Konfigurationen

Um auf Laufzeit-Konfigurationen zuzugreifen, können wir den Composable `useRuntimeConfig()` verwenden:

```ts [server/api/test.ts]
export default defineEventHandler((event) => {
  const config = useRuntimeConfig(event)

  // Zugriff auf öffentliche Variablen
  const result = await $fetch(`/test`, {
    baseURL: config.public.apiBase,
    headers: {
      // Zugriff auf einen geheimen Schlüssel (nur auf dem Server verfügbar)
      Authorization: `Bearer ${config.apiSecret}`
    }
  })
  return result
}
```

In diesem Beispiel ist `apiBase` im `public` Namespace definiert, sodass es sowohl auf dem Server als auch auf dem Client universell zugänglich ist, während `apiSecret` **nur auf dem Server verfügbar** ist.

## Umgebungsvariablen

Es ist möglich, Laufzeit-Konfigurationswerte mithilfe einer passenden Umgebungsvariablen zu aktualisieren, deren Name mit `NUXT_` präfixiert ist.

:read-more{to="/docs/de/guide/going-further/runtime-config"}

### Verwenden des `.env` Datei

Wir können die Umgebungsvariablen in der `.env` Datei festlegen, um sie während der **Entwicklung** und **Build/Generierung** zugänglich zu machen.

```ini [.env]
NUXT_PUBLIC_API_BASE = "https://api.localhost:5555"
NUXT_API_SECRET = "123"
```

::note
Jede Umgebungsvariable, die in der `.env` Datei festgelegt wird, wird während der **Entwicklung** und **Build/Generierung** im Nuxt-App über `process.env` zugegriffen.
::

::warning
In der **Produktionslaufzeit** sollten Sie Plattform-Umgebungsvariablen verwenden und `.env` wird nicht verwendet.
::

:read-more{to="/docs/de/guide/directory-structure/env"}

## `app` Namespace

Nuxt verwendet den `app` Namespace für Laufzeit-Konfigurationen, der Schlüssel wie `baseURL` und `cdnURL` enthält. Sie können diese Werte bei Laufzeit durch Festlegen von Umgebungsvariablen anpassen.

::note
Dies ist ein reservierter Namespace. Sie sollten keine zusätzlichen Schlüssel innerhalb von `app` einführen.
::

### `app.baseURL`

Standardmäßig ist `baseURL` auf `'/'` gesetzt.

Allerdings kann `baseURL` durch Festlegen der `NUXT_APP_BASE_URL` als Umgebungsvariable bei Laufzeit aktualisiert werden.

Dann können Sie diesen neuen Basis-URL über `config.app.baseURL` zugreifen:

```ts [/plugins/my-plugin.ts]
export default defineNuxtPlugin((NuxtApp) => {
  const config = useRuntimeConfig()

  // Universeller Zugriff auf baseURL
  const baseURL = config.app.baseURL
})
```

### `app.cdnURL`

Das folgende Beispiel zeigt, wie man eine benutzerdefinierte CDN-URL definiert und über `useRuntimeConfig()` zugreift.

Sie können eine benutzerdefinierte CDN-URL für das Servieren von statischen Assets in `.output/public` mithilfe der `NUXT_APP_CDN_URL` Umgebungsvariable verwenden.

Und dann können Sie die neue CDN-URL über `config.app.cdnURL` zugreifen.

```ts [server/api/foo.ts]
export default defineEventHandler((event) => {
  const config = useRuntimeConfig(event)

  // Universeller Zugriff auf cdnURL
  const cdnURL = config.app.cdnURL
})
```

:read-more{to="/docs/de/guide/going-further/runtime-config"}