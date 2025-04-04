---
title: "nuxi init"
description: Das init-Befehl initialisiert ein frisches Nuxt-Projekt.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/init.ts
    size: xs
---

<!--init-cmd-->
```bash [Terminal]
npx nuxi init [DIR] [--cwd=<Verzeichnis>] [-t, --template] [-f, --force] [--offline] [--preferOffline] [--no-install] [--gitInit] [--shell] [--packageManager]
```
<!--/init-cmd-->

Das `init`-Befehl initialisiert ein frisches Nuxt-Projekt mit [unjs/giget](https://github.com/unjs/giget).

## Argumente

<!--init-args-->
Argument | Beschreibung
--- | ---
`DIR=""` | Projektverzeichnis
<!--/init-args-->

## Optionen

<!--init-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` | `.` | Angabe des Arbeitsverzeichnisses
`-t, --template` |  | Vorlagename
`-f, --force` |  | Überarbeiten bestehendes Verzeichnis
`--offline` |  | Erzwungener Offline-Modus
`--preferOffline` |  | Vorzugsweise Offline-Modus
`--no-install` |  | Abhängigkeiten werden übersprungen
`--gitInit` |  | Git-Repository initialisieren
`--shell` |  | Shell nach der Installation im Projektverzeichnis starten
`--packageManager` |  | Paketmanagerauswahl (npm, pnpm, yarn, bun)
<!--/init-opts-->

## Umgebungsvariablen

- `NUXI_INIT_REGISTRY`: Setzen Sie auf eine benutzerdefinierte Vorlagensammlung. ([mehr erfahren](https://github.com/unjs/giget#custom-registry)).
  - Der Standardregistrierverzeichnis wird aus [nuxt/starter/templates](https://github.com/nuxt/starter/tree/templates/templates) geladen.