---
title: "nuxi info"
description: Das `info` Kommando gibt Informationen über den aktuellen oder spezifizierten Nuxt-Projekt an.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/info.ts
    size: xs
---

<!--info-cmd-->
```bash [Terminal]
npx nuxi info [ROOTDIR] [--cwd=<Verzeichnis>]
```
<!--/info-cmd-->

Das `info` Kommando gibt Informationen über den aktuellen oder spezifizierten Nuxt-Projekt an.

## Argumente

<!--info-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Gibt das Arbeitsverzeichnis an (Standardwert: `.`)
<!--/info-args-->

## Optionen

<!--info-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Gibt das Arbeitsverzeichnis an, dies hat Vorrang vor ROOTDIR (Standardwert: `.`)
<!--/info-opts-->