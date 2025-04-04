---
title: "nuxi analyze"
description: "Analysiere den Produktionsbundle oder deinen Nuxt-Anwendung."
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/analyze.ts
    size: xs
---

<!--analyze-cmd-->
```bash [Terminal]
npx nuxi analyze [ROOTDIR] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--dotenv] [--name=<name>] [--no-serve]
```
<!--/analyze-cmd-->

Der Befehl `analyze` baut Nuxt und analysiert den Produktionsbundle (experimentell).

## Argumente

<!--analyze-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Angibt das Arbeitsverzeichnis (Standardwert: `.`)
<!--/analyze-args-->

## Optionen

<!--analyze-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Angibt das Arbeitsverzeichnis an, dies hat Vorrang vor ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm|info|detailliert>` |  | Angibt den Build-Level der Protokollierung
`--dotenv` |  | Pfad zum `.env`-Datei, die geladen werden soll, relativ zum Rootverzeichnis
`--name=<name>` | `default` | Name der Analyse
`--no-serve` |  | Überspringt das Bereitstellen der Analyseergebnisse
<!--/analyze-opts-->

::note
Dieser Befehl setzt `process.env.NODE_ENV` auf `production`.
::