---
title: "nuxi typecheck"
description: Der `typecheck` Befehl führt `vue-tsc` aus, um die Typen in Ihrem App durchzuchecken.
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/typecheck.ts
    size: xs
---

<!--typecheck-cmd-->
```bash [Terminal]
npx nuxi typecheck [ROOTDIR] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>]
```
<!--/typecheck-cmd-->

Der `typecheck` Befehl führt den [`vue-tsc`](https://github.com/vuejs/language-tools/tree/master/packages/tsc) aus, um die Typen in Ihrem App durchzuchecken.

## Argumente

<!--typecheck-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Gibt das Arbeitsverzeichnis an (Standardwert: `.`)
<!--/typecheck-args-->

## Optionen

<!--typecheck-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Gibt das Arbeitsverzeichnis an, dies hat Vorrang vor ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm\|info\|detailliert>` |  | Gibt den Build-Level des Protokollierungsniveaus an
<!--/typecheck-opts-->

::note
Dieser Befehl setzt `process.env.NODE_ENV` auf `production`. Um dieses zu überschreiben, definieren Sie `NODE_ENV` in einer [`.env`](/docs/de/guide/directory-structure/env) Datei oder als Kommandozeilenargument.
::

::read-more{to="/docs/de/docs/guide/concepts/typescript#type-checking"}
Weitere Informationen zur Aktivierung der Typenprüfung bei der Erstellung oder beim Entwickeln finden Sie hier.
::