---
title: 'nuxi build-module'
description: 'Nuxt-Befehl, um Ihren Nuxt-Modul vor der Veröffentlichung zu kompilieren.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/module-builder/blob/main/src/cli.ts
    size: xs
---

<!--build-module-cmd-->
```bash [Terminal]
npx nuxi build-module [ROOTDIR] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--build] [--stub] [--sourcemap] [--prepare]
```
<!--/build-module-cmd-->

Der Befehl `build-module` führt `@nuxt/module-builder` aus, um eine `dist`-Verzeichnis innerhalb Ihres `rootDir` zu generieren, das den vollständigen Build für Ihren **nuxt-Modul** enthält.

## Argumente

<!--build-module-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Angibt das Arbeitsverzeichnis (Standardwert: `.`)
<!--/build-module-args-->

## Optionen

<!--build-module-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Angibt das Arbeitsverzeichnis an, dies hat Vorrang über ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm|info|detailliert>` |  | Bestimmt den Build-Level
`--build` | `false` | Modul für die Veröffentlichung kompilieren
`--stub` | `false` | Stubs für Entwicklung generieren anstelle des tatsächlichen Builds
`--sourcemap` | `false` | Quelltextmappen generieren
`--prepare` | `false` | Modul für lokale Entwicklung vorbereiten
<!--/build-module-opts-->

::read-more{to="https://github.com/nuxt/module-builder" icon="i-simple-icons-github" target="\_blank"}
Mehr Informationen zu `@nuxt/module-builder` finden Sie hier.
::