---
title: "nuxi add"
description: "Erstellt eine Entität in Ihrer Nuxt-Anwendung."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/add.ts
    size: xs
---

<!--add-cmd-->
```bash [Terminal]
npx nuxi add <TEMPLATE> <NAME> [--cwd=<Verzeichnis>] [--logLevel=<schweissig|info|detailliert>] [--force]
```
<!--/add-cmd-->

### Argumente

<!--add-args-->
Argument | Beschreibung
--- | ---
`TEMPLATE` | Spezifizieren Sie welche Vorlage generiert werden soll (Möglichkeiten: <api\|plugin\|komponente\|komponierbar\|middleware\|layout\|seite\|schicht>)
`NAME` | Spezifizieren Sie den Namen des generierten Dateien
<!--/add-args-->

### Optionen

<!--add-opts-->
Option | Standard | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` | `.` | Spezifizieren Sie das Arbeitsverzeichnis
`--logLevel=<schweissig\|info\|detailliert>` |  | Spezifizieren Sie den Build-Level der Protokollierung
`--force` | `false` | Überprüfen Sie Datei überschreiben, wenn sie bereits existiert
<!--/add-opts-->

**Modifikatoren:**

Einige Vorlagen unterstützen zusätzliche Modifikator-Schalter, um einen Suffix (wie `.client` oder `.get`) zu ihrem Namen hinzuzufügen.

```bash [Terminal]
# Erstellt `/plugins/sockets.client.ts`
npx nuxi add plugin sockets --client
```

## `nuxi add komponente`

* Modifikator-Schalter: `--mode client|server` oder `--client` oder `--server`

```bash [Terminal]
# Erstellt `components/TheHeader.vue`
npx nuxi add komponente TheHeader
```

## `nuxi add komponierbar`

```bash [Terminal]
# Erstellt `composables/foo.ts`
npx nuxi add komponierbar foo
```

## `nuxi add layout`

```bash [Terminal]
# Erstellt `layouts/custom.vue`
npx nuxi add layout custom
```

## `nuxi add plugin`

* Modifikator-Schalter: `--mode client|server` oder `--client` oder `--server`

```bash [Terminal]
# Erstellt `plugins/analytics.ts`
npx nuxi add plugin analytics
```

## `nuxi add seite`

```bash [Terminal]
# Erstellt `pages/about.vue`
npx nuxi add seite about
```

```bash [Terminal]
# Erstellt `pages/category/[id].vue`
npx nuxi add seite "category/[id]"
```

## `nuxi add middleware`

* Modifikator-Schalter: `--global`

```bash [Terminal]
# Erstellt `middleware/auth.ts`
npx nuxi add middleware auth
```

## `nuxi add api`

* Modifikator-Schalter: `--method` (kann `connect`, `delete`, `get`, `head`, `options`, `patch`, `post`, `put` oder `trace` akzeptieren) oder alternativ können Sie direkt `--get`, `--post`, usw. verwenden.

```bash [Terminal]
# Erstellt `server/api/hello.ts`
npx nuxi add api hello
```

## `nuxi add schicht`

```bash [Terminal]
# Erstellt `layers/subscribe/nuxt.config.ts`
npx nuxi add schicht subscribe
```