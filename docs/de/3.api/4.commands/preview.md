---
title: "nuxi Vorschau"
description: Der Befehl `vorschau` startet einen Server, um Ihre Nuxt-Anwendung nach dem Build-Befehl zu vorspielen. Der Befehl `start` ist ein Alias für `vorschau`. Wenn Sie Ihre Anwendung in der Produktion ausführen, finden Sie weitere Informationen im Abschnitt [Bereitstellung](/docs/getting-started/deployment).

links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/preview.ts
    size: xs
---

<!--vorschau-cmd-->
```bash [Terminal]
npx nuxi vorschau [ROOTDIR] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--envName] [--dotenv] [-p, --port]
```
<!--/vorschau-cmd-->

Der `vorschau` Befehl startet einen Server, um Ihre Nuxt-Anwendung nach dem Ausführen des `build` Befehls zu vorspielen. Der Befehl `start` ist ein Alias für `vorschau`. Wenn Sie Ihre Anwendung in der Produktion ausführen, finden Sie weitere Informationen im Abschnitt [Bereitstellung](/docs/getting-started/deployment).

## Argumente

<!--vorschau-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Gibt das Arbeitsverzeichnis an (Standardwert: `.`)
<!--/vorschau-args-->

## Optionen

<!--vorschau-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Gibt das Arbeitsverzeichnis an, dies hat Vorrang vor ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm|info|detailliert>` |  | Gibt den Build-Level an
`--envName` |  | Die Umgebung, die verwendet wird, um Konfigurationsüberschreitungen aufzulösen (Standard ist `produktion` beim Build und `entwicklung` beim Start des Entwicklungs-Servers)
`--dotenv` |  | Pfad zum `.env`-Datei, die geladen werden soll, relativ zum Arbeitsverzeichnis
`-p, --port` |  | Port, an dem angehört wird (Standardwert: `NUXT_PORT \|\| NITRO_PORT \|\| PORT`)
<!--/vorschau-opts-->

Dieser Befehl setzt `process.env.NODE_ENV` auf `produktion`. Um diese Einstellung zu überschreiben, definieren Sie `NODE_ENV` in einer `.env`-Datei oder als Kommandozeilenargument.

::note
Aus Praktiken Gründen wird in Vorschau-Modus Ihr [`.env`](/docs/guide/directory-structure/env)-Datei in `process.env` geladen. (Allerdings müssen Sie in der Produktion sicherstellen, dass Ihre Umgebungsvariablen manuell gesetzt sind.)
::