---
title: 'nuxi Reinigung'
description: 'Entfernt häufig erzeugte Nuxt-Dateien und Caches.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/cleanup.ts
    size: xs
---

<!--cleanup-cmd-->
```bash [Terminal]
npx nuxi cleanup [ROOTDIR] [--cwd=<Verzeichnis>]
```
<!--/cleanup-cmd-->

Der Befehl `cleanup` entfernt häufig erzeugte Nuxt-Dateien und Caches, einschließlich:

- `.nuxt`
- `.output`
- `node_modules/.vite`
- `node_modules/.cache`

## Argumente

<!--cleanup-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Gibt das Arbeitsverzeichnis an (Standardwert: `.`)
<!--/cleanup-args-->

## Optionen

<!--cleanup-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Gibt das Arbeitsverzeichnis an, dies hat Vorrang über ROOTDIR (Standardwert: `.`)
<!--/cleanup-opts-->