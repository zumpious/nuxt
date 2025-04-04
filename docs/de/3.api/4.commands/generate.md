---
title: "nuxi generate"
description: Vorbereitet jede Route der Anwendung und speichert den Ergebniscode als einfache HTML-Dateien ab.
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/generate.ts
    size: xs
---

<!--generate-cmd-->
```bash [Terminal]
npx nuxi generate [ROOTDIR] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--preset] [--dotenv] [--envName]
```
<!--/generate-cmd-->

Der Befehl `generate` vorbereitet jede Route deiner Anwendung und speichert den Ergebniscode als einfache HTML-Dateien ab, die du auf jeder statischen Hosting-Dienststellung bereitstellen kannst. Der Befehl startet den Befehl `nuxi build` mit dem Argument `prerender` gesetzt auf `true`.

## Argumente

<!--generate-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Gibt das Arbeitsverzeichnis an (Standardwert: `.`)
<!--/generate-args-->

## Optionen

<!--generate-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Gibt das Arbeitsverzeichnis an, dies hat Vorrang über ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm|info|detailliert>` |  | Gibt den Build-Level des Protokolls an
`--preset` |  | Nitro Server-Voreinstellung
`--dotenv` |  | Pfad zur `.env`-Datei zum Laden, relativ zum Arbeitsverzeichnis
`--envName` |  | Das Umgebungsprofil, das verwendet wird, um Konfigurationsüberschreitungen zu lösen (Standard ist `produktion` beim Build und `entwicklung` beim Start des Entwicklungs-servers)
<!--/generate-opts-->

::read-more{to="/docs/getting-started/deployment#static-hosting"}
Weitere Informationen zur Vorabrenderung und statischer Hosting-Dienststellung finden Sie hier.
::