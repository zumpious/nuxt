---
title: "nuxi build"
description: "Bau dein Nuxt-Anwendungsprojekt."
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/build.ts
    size: xs
---

<!--build-cmd-->
```bash [Terminal]
npx nuxi build [ROOTDIR] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--prerender] [--preset] [--dotenv] [--envName]
```
<!--/build-cmd-->

Das `build`-Kommando erstellt eine `.output`-Verzeichnis mit deinem Anwendungscode, dem Server und den Abhängigkeiten, die für die Produktion bereitgestellt werden.

## Argumente

<!--build-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Gibt das Arbeitsverzeichnis an (Standardwert: `.`)
<!--/build-args-->

## Optionen

<!--build-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Gibt das Arbeitsverzeichnis an, dies hat Vorrang vor ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm|info|detailliert>` |  | Gibt den Build-Level an
`--prerender` |  | Bau Nuxt und rendere statische Routen vorab
`--preset` |  | Nitro-Server-Preset
`--dotenv` |  | Pfad zum `.env`-Datei, relativ zum Arbeitsverzeichnis
`--envName` |  | Das Umgebungsprofil, das verwendet wird, um Konfigurationsüberschreitungen aufzulösen (Standard ist `produktion` beim Bau und `entwicklung` beim Starten des Entwicklungs-servers)
<!--/build-opts-->

::note
Dieses Kommando setzt `process.env.NODE_ENV` auf `produktion`.
::

::note
`--prerender` setzt `preset` immer auf `static`
::