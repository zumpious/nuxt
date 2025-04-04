---
title: "nuxi Modul"
description: "Suchen und Module in Ihre Nuxt-Anwendung mit der Befehlszeile hinzufügen."
links:
  - label: Quellcode
    icon: i-simple-icons-github
    to: https://github.com/nuxt/cli/blob/main/packages/nuxi/src/commands/module/
    size: xs
---

Nuxi bietet einige Werkzeuge an, um [Nuxt-Module](/modules) problemlos zu verwalten.

## nuxi Modul hinzufügen

<!--module-add-cmd-->
```bash [Terminal]
npx nuxi module add <MODULENAME> [--cwd=<Verzeichnis>] [--logLevel=<stumm|info|detailliert>] [--skipInstall] [--skipConfig] [--dev]
```
<!--/module-add-cmd-->

<!--module-add-args-->
Argument | Beschreibung
--- | ---
`MODULENAME` | Modulname
<!--/module-add-args-->

<!--module-add-opts-->
Option | Standard | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` | `.` | Angabe des Arbeitsverzeichnisses
`--logLevel=<stumm\|info\|detailliert>` |  | Angabe des Build-Level
`--skipInstall` |  | npm install überspringen
`--skipConfig` |  | nuxt.config.ts Aktualisierung überspringen
`--dev` |  | Modul als Entwicklungsabhängigkeit installieren
<!--/module-add-opts-->

Der Befehl ermöglicht es Ihnen, [Nuxt-Module](/modules) in Ihrer Anwendung ohne manuelle Arbeit zu installieren.

Wenn Sie den Befehl ausführen, wird das folgende vorgenommen:

- Das Modul als Abhängigkeit mit Ihrem Paketmanager installieren
- Es in Ihrem [package.json](/docs/guide/directory-structure/package) hinzufügen
- Ihr [`nuxt.config`](/docs/guide/directory-structure/nuxt-config) aktualisieren

**Beispiel:**

Das Installieren des [`Pinia`](/modules/pinia) Moduls

```bash [Terminal]
npx nuxi module add pinia
```

## nuxi Modul suchen

<!--module-search-cmd-->
```bash [Terminal]
npx nuxi module search <QUERY> [--cwd=<Verzeichnis>] [--nuxtVersion=<2|3>]
```
<!--/module-search-cmd-->

### Argumente

<!--module-search-args-->
Argument | Beschreibung
--- | ---
`QUERY` | Suchbegriffe
<!--/module-search-args-->

### Optionen

<!--module-search-opts-->
Option | Standard | Beschreibung
--- | --- | ---
`--cwd=<Verzeichnis>` | `.` | Angabe des Arbeitsverzeichnisses
`--nuxtVersion=<2\|3>` |  | Filtern nach Nuxt-Version und nur kompatibele Module auflisten (standardmäßig automatisch erkannt)
<!--/module-search-opts-->

Der Befehl sucht nach Nuxt-Modulen, die Ihren Suchbegriff erfüllen und mit Ihrer Nuxt-Version kompatibel sind.

**Beispiel:**

```bash [Terminal]
npx nuxi module search pinia
```