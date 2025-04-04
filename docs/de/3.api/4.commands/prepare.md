---
title: 'nuxi vorbereiten'
description: Das Befehl `vorbereiten` erstellt eine `.nuxt` Verzeichnis in Ihrer Anwendung und generiert Typen. Dies kann in einer CI-Umgebung oder als `postinstall` Befehl in Ihrem `package.json` ([/docs/guide/directory-structure/package]) nützlich sein.

links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/prepare.ts
    size: xs
---

<!--prepare-cmd-->
```bash [Terminal]
npx nuxi vorbereiten [ROOTDIR] [--dotenv] [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--envName]
```
<!--/prepare-cmd-->

Der Befehl `vorbereiten` erstellt ein Verzeichnis [.nuxt](/docs/de/guide/directory-structure/nuxt) in Ihrer Anwendung und generiert Typen. Dies kann in einer CI-Umgebung oder als `postinstall` Befehl in Ihrem `package.json` ([/docs/de/guide/directory-structure/package]) nützlich sein.

## Argumente

<!--prepare-args-->
Argument | Beschreibung
--- | ---
`ROOTDIR="."` | Angibt das Arbeitsverzeichnis (Standardwert: `.`)
<!--/prepare-args-->

## Optionen

<!--prepare-opts-->
Option | Standardwert | Beschreibung
--- | --- | ---
`--dotenv` |  | Pfad zu einem `.env`-Datei, die geladen werden soll, relativ zum Wurzelverzeichnis
`--cwd=<Verzeichnis>` |  | Angibt das Arbeitsverzeichnis an, dies hat Vorrang über ROOTDIR (Standardwert: `.`)
`--logLevel=<stumm|info|detailliert>` |  | Angibt den Build-Level der Protokollierung
`--envName` |  | Die Umgebung, die verwendet wird, um Konfigurationsüberschreitungen aufzulösen (Standard ist `produktion` beim Builden und `entwicklung` beim Starten des Entwicklungsservers)
<!--/prepare-opts-->