---
title: "nuxi aktualisieren"
description: Das Upgrade-Befehl aktualisiert Nuxt auf die neueste Version.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/upgrade.ts
    size: xs
---

<!--upgrade-cmd-->
```bash [Terminal]
npx nuxi upgrade [ROOTDIR] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--dedupe] [-f, --force] [-ch, --channel=<stabil|nachtlich>]
```
<!--/upgrade-cmd-->

Das `upgrade`-Befehl aktualisiert Nuxt auf die neueste Version.

## Argumente

<!--upgrade-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Gibt das Arbeitsverzeichnis an (Standardwert: `.`)
<!--/upgrade-args-->

## Optionen

<!--upgrade-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Gibt das Arbeitsverzeichnis an, dies hat Vorrang vor ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm\|info\|detailliert>` |  | Gibt den Build-Level an
`--dedupe` |  | Entfernt Duplikate, erstellt aber kein neues Lockfile
`-f, --force` |  | Führt eine Upgrade-Aktion durch, um das Lockfile und node_modules zu aktualisieren
`-ch, --channel=<stabil\|nachtlich>` | `stabil` | Gibt eine Kanalversion an, von der installiert wird (Standardwert: stabil)
<!--/upgrade-opts-->