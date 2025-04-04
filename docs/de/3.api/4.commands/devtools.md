---
title: "nuxi devtools"
description: Das Kommando devtools ermöglicht es Ihnen, Nuxt DevTools pro Projekt zu aktivieren oder deaktivieren.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/devtools.ts
    size: xs
---

<!--devtools-cmd-->
```bash [Terminal]
npx nuxi devtools <BETRÄGE> [WURZELVERZEICHNIS] [--cwd=<verzeichnis>]
```
<!--/devtools-cmd-->

Das Ausführen von `nuxi devtools enable` installiert Nuxt DevTools global und aktiviert es auch im spezifischen Projekt, das Sie verwenden. Es wird als Vorlieben auf Ihrem Benutzerebeneigenen `.nuxtrc` gespeichert. Wenn Sie die Unterstützung für DevTools für ein bestimmtes Projekt entfernen möchten, können Sie `nuxi devtools disable` ausführen.

## Argumente

<!--devtools-args-->
Argument | Beschreibung
--- | ---
`BETRÄGE` | Auszuführendes Kommando (Möglichkeiten: <enable\|disable>)
`WURZELVERZEICHNIS="."` | Angibt das Arbeitsverzeichnis (Standardwert: `.`)
<!--/devtools-args-->

## Optionen

<!--devtools-opts-->
Option | Standard | Beschreibung
--- | --- | ---
`--cwd=<verzeichnis>` |  | Angibt das Arbeitsverzeichnis an, dies hat Vorrang über WURZELVERZEICHNIS (Standardwert: `.`)
<!--/devtools-opts-->

::read-more{icon="i-simple-icons-nuxtdotjs" to="https://devtools.nuxt.com" target="\_blank"}
Weitere Informationen zu den **Nuxt DevTools** finden Sie hier.
::