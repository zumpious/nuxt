---
title: 'nuxi dev'
description: Das `dev` Kommando startet einen Entwicklungsserver mit Hot-Module-Austausch unter [http://localhost:3000](http://localhost:3000)
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/dev.ts
    size: xs
---

<!--dev-cmd-->
```bash [Terminal]
npx nuxi dev [ROOTDIR] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--dotenv] [--envName] [--no-clear] [--no-fork] [-p, --port] [-h, --host] [--clipboard] [-o, --open] [--https] [--publicURL] [--qr] [--public] [--tunnel] [--sslCert] [--sslKey]
```
<!--/dev-cmd-->

Das `dev` Kommando startet einen Entwicklungsserver mit Hot-Module-Austausch unter [http://localhost:3000](http://localhost:3000)

## Argumente

<!--dev-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Angibt das Arbeitsverzeichnis (Standardwert: `.`)
<!--/dev-args-->

## Optionen

<!--dev-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` |  | Angibt das Arbeitsverzeichnis an, dies hat Vorrang vor ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm\|info\|detailliert>` |  | Angibt den Build-Level der Protokollierung
`--dotenv` |  | Pfad zum `.env`-Datei, die geladen werden soll, relativ zum Wurzelverzeichnis
`--envName` |  | Die Umgebung, die verwendet wird, um Konfigurationsüberschreitungen aufzulösen (Standard ist `produktion` beim Builden und `entwicklung` beim Starten des Entwicklungsservers)
`--no-clear` |  | Deaktiviert das Löschen des Konsole bei Neustart
`--no-fork` |  | Deaktiviert das Fork-Modus
`-p, --port` |  | Port, an dem angehört wird (Standardwert: `NUXT_PORT \|\| NITRO_PORT \|\| PORT \|\| nuxtOptions.devServer.port`)
`-h, --host` |  | Host, an dem angehört wird (Standardwert: `NUXT_HOST \|\| NITRO_HOST \|\| HOST \|\| nuxtOptions._layers?.[0]?.devServer?.host`)
`--clipboard` | `false` | URL in die Zwischenablage kopieren
`-o, --open` | `false` | URL im Browser öffnen
`--https` |  | HTTPS aktivieren
`--publicURL` |  | Anzeigebare öffentliche URL (für QR-Code verwendet)
`--qr` |  | Wenn verfügbar, Anzeige des QR-Codes für die öffentliche URL
`--public` |  | An alle Netzwerkinterfaces hören
`--tunnel` |  | Tunnel mithilfe von https://github.com/unjs/untun öffnen
`--sslCert` |  | (VERALTET) Verwenden Sie stattdessen `--https.cert`.
`--sslKey` |  | (VERALTET) Verwenden Sie stattdessen `--https.key`.
<!--/dev-opts-->

Der Port und der Host können auch über die Umgebungsvariablen `NUXT_PORT`, `PORT`, `NUXT_HOST` oder `HOST` gesetzt werden.

Darüber hinaus können die oben genannten Optionen `nuxi` an `listen` weitergegeben werden, z.B. `--no-qr` um den QR-Code des Entwicklungsservers zu deaktivieren. Sie finden die Liste der `listen` Optionen in den [unjs/listhen](https://github.com/unjs/listhen) Dokumentationen.

Dieses Kommando setzt `process.env.NODE_ENV` auf `entwicklung`.

::note
Wenn Sie in der Entwicklung einen selbstsignierten Zertifikat verwenden, müssen Sie `NODE_TLS_REJECT_UNAUTHORIZED=0` in Ihrer Umgebung setzen.
::