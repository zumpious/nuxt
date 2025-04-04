---
title: 'useCookie'
description: useCookie ist ein SSR-freundlicher Composable zum Lesen und Schreiben von Cookies.
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/cookie.ts
    size: xs
---

Innerhalb deiner Seiten, Komponenten und Plugins kannst du `useCookie` verwenden, einen SSR-freundlichen Composable zum Lesen und Schreiben von Cookies.

```ts
const cookie = useCookie(name, options)
```

::note
`useCookie` funktioniert nur im [Nuxt Kontext](/docs/guide/going-further/nuxt-app#the-nuxt-context).
::

::tip
Der `useCookie` Ref wird automatisch den Cookie-Wert in JSON serialisieren und deserialisieren.
::

## Beispiel

Das folgende Beispiel erstellt einen Cookie namens `counter`. Wenn der Cookie nicht existiert, wird er mit einem zufälligen Wert initialisiert. Sobald wir den Wert von `counter` ändern, wird der Cookie entsprechend aktualisiert.

```vue [app.vue]
<script setup lang="ts">
const counter = useCookie('counter')

counter.value = counter.value || Math.round(Math.random() * 1000)
</script>

<template>
  <div>
    <h1>Counter: {{ counter || '-' }}</h1>
    <button @click="counter = null">reset</button>
    <button @click="counter--">-</button>
    <button @click="counter++">+</button>
  </div>
</template>
```

:link-example{to="/docs/examples/advanced/use-cookie"}

::note
Manuell `useCookie` Werte aktualisieren, wenn ein Cookie geändert wurde, mit [`refreshCookie`](/docs/api/utils/refresh-cookie).
::

## Optionen

Der Cookie Composable akzeptiert mehrere Optionen, die das Verhalten von Cookies ändern lassen.

Die meisten Optionen werden direkt an das [cookie](https://github.com/jshttp/cookie) Paket übergeben.

### `maxAge` / `expires`

Verwende diese Optionen, um die Ablaufzeit des Cookies zu setzen.

`maxAge`: Gibt den `number` (in Sekunden) als Wert für die [`Max-Age Set-Cookie` Eigenschaft](https://tools.ietf.org/html/rfc6265#section-5.2.2) an. Der angegebene Wert wird abgerundet. Standardmäßig ist keine maximale Ablaufzeit festgelegt.

`expires`: Gibt den `Date` Objekt als Wert für die [`Expires Set-Cookie` Eigenschaft](https://tools.ietf.org/html/rfc6265#section-5.2.1) an. Standardmäßig ist keine Ablaufzeit festgelegt. Die meisten Clients betrachten dies als "nicht-persönliches Cookie" und löschen es bei Bedingungen wie das Beenden eines Webbrowserprogramms.

::note
Die [Spezifikation des Cookie-Speichermodells](https://tools.ietf.org/html/rfc6265#section-5.3) besagt, dass, wenn sowohl `expires` und `maxAge` festgelegt sind, `maxAge` Vorrang hat, aber nicht alle Clients dies befolgen. Wenn beide festgelegt sind, sollten sie auf denselben Zeitpunkt zeigen!
::

::note
Wenn weder `expires` noch `maxAge` festgelegt sind, ist der Cookie session-basiert und wird beim Schließen des Browsers entfernt.
::

### `httpOnly`

Gibt den `boolean` Wert für die [`HttpOnly Set-Cookie` Eigenschaft](https://tools.ietf.org/html/rfc6265#section-5.2.6) an. Wenn wahr, wird die `HttpOnly` Eigenschaft gesetzt; andernfalls nicht. Standardmäßig ist die `HttpOnly` Eigenschaft nicht gesetzt.

::warning
Sei vorsichtig, wenn du dies auf `true` setzt, da konformen Clients den Cookie in `document.cookie` nicht sehen lassen.
::

### `secure`

Gibt den `boolean` Wert für die [`Secure Set-Cookie` Eigenschaft](https://tools.ietf.org/html/rfc6265#section-5.2.5) an. Wenn wahr, wird die `Secure` Eigenschaft gesetzt; andernfalls nicht. Standardmäßig ist die `Secure` Eigenschaft nicht gesetzt.

::warning
Sei vorsichtig, wenn du dies auf `true` setzt, da konforme Clients den Cookie in Zukunft nicht an den Server senden, wenn der Browser keine HTTPS-Verbindung hat. Dies kann Hydration-Fehler verursachen.
::

### `partitioned`

Gibt den `boolean` Wert für die [`Partitioned Set-Cookie`](https://datatracker.ietf.org/doc/html/draft-cutler-httpbis-partitioned-cookies#section-2.1) Eigenschaft an. Wenn wahr, wird die `Partitioned` Eigenschaft gesetzt, andernfalls nicht. Standardmäßig ist die `Partitioned` Eigenschaft nicht gesetzt.

::note
Dies ist eine Eigenschaft, die noch nicht vollständig standardisiert ist und sich in der Zukunft ändern könnte.
Dies bedeutet auch, dass viele Clients diese Eigenschaft möglicherweise ignorieren, bis sie sie verstehen.

Weitere Informationen findest du in der [Vorschlag](https://github.com/privacycg/CHIPS).
::

### `domain`

Gibt den Wert für die [`Domain Set-Cookie` Eigenschaft](https://tools.ietf.org/html/rfc6265#section-5.2.3) an. Standardmäßig ist kein Domain festgelegt, und die meisten Clients betrachten den Cookie nur für den aktuellen Domain.

### `path`

Gibt den Wert für die [`Path Set-Cookie` Eigenschaft](https://tools.ietf.org/html/rfc6265#section-5.2.4) an. Standardmäßig wird der Pfad als ["Standardpfad"](https://tools.ietf.org/html/rfc6265#section-5.1.4) betrachtet.

### `sameSite`

Gibt den `boolean` oder `string` Wert für die [`SameSite Set-Cookie` Eigenschaft](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-03#section-4.1.2.7) an.

- `true` setzt die `SameSite` Eigenschaft auf `Strict` für strenges Same-Site-Enforcement.
- `false` setzt die `SameSite` Eigenschaft nicht.
- `'lax'` setzt die `SameSite` Eigenschaft auf `Lax` für laxes Same-Site-Enforcement.
- `'none'` setzt die `SameSite` Eigenschaft auf `None` für explizites Cross-Site-Cookie.
- `'strict'` setzt die `SameSite` Eigenschaft auf `Strict` für strenges Same-Site-Enforcement.

Weitere Informationen zu den verschiedenen Enforcements finden Sie in der [Spezifikation](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-03#section-4.1.2.7).

### `encode`

Gibt eine Funktion an, die verwendet wird, um den Cookie-Wert zu kodieren. Da der Wert eines Cookies eine begrenzte Zeichensatz hat (und muss eine einfache Zeichenkette sein), kann diese Funktion den Wert in eine Zeichenkette kodieren, die für einen Cookie-Wert geeignet ist.

Die Standard-Kodierungsfunktion ist `JSON.stringify` + `encodeURIComponent`.

### `decode`

Gibt eine Funktion an, die verwendet wird, um den Cookie-Wert zu dekodieren. Da der Wert eines Cookies eine begrenzte Zeichensatz hat (und muss eine einfache Zeichenkette sein), kann diese Funktion einen vorher kodierten Cookie-Wert in eine JavaScript-Zeichenkette oder andere Objekte dekodieren.

Die Standard-Dekodierungsfunktion ist `decodeURIComponent` + [destr](https://github.com/unjs/destr).

::note
Wenn eine Ausnahme in dieser Funktion geworfen wird, wird der ursprüngliche, nicht-dekodierte Cookie-Wert als Cookie-Wert zurückgegeben.
::

### `default`

Gibt eine Funktion an, die den Standardwert des Cookies zurückgibt. Die Funktion kann auch einen `Ref` zurückgeben.

### `readonly`

Erlaubt das Zugreifen auf einen Cookie-Wert ohne die Möglichkeit, ihn zu ändern.

### `watch`

Gibt den `boolean` oder `string` Wert für [watch](https://vuejs.org/api/reactivity-core.html#watch) des Cookie-Ref-Datums an.

- `true` - Wird das Cookie-Ref-Datum und seine verschachtelten Eigenschaften beobachtet (Standard).
- `shallow` - Wird nur das Cookie-Ref-Datum und seine oberflächlichen Eigenschaften beobachtet.
- `false` - Wird das Cookie-Ref-Datum nicht beobachtet.

::note
Manuell `useCookie` Werte aktualisieren, wenn ein Cookie geändert wurde, mit [`refreshCookie`](/docs/api/utils/refresh-cookie).
::

**Beispiel 1:**

```vue
<script setup lang="ts">
const user = useCookie(
  'userInfo',
  {
    default: () => ({ score: -1 }),
    watch: false
  }
)

if (user.value && user.value !== null) {
  user.value.score++; // userInfo Cookie wird mit diesem Änderung nicht aktualisiert
}
</script>

<template>
  <div>User score: {{ user?.score }}</div>
</template>
```

**Beispiel 2:**

```vue
<script setup lang="ts">
const list = useCookie(
  'list',
  {
    default: () => [],
    watch: 'shallow'
  }
)

function add() {
  list.value?.push(Math.round(Math.random() * 1000))
  // list Cookie wird mit diesem Änderung nicht aktualisiert
}

function save() {
  if (list.value && list.value !== null) {
    list.value = [...list.value]
    // list Cookie wird mit diesem Änderung aktualisiert
  }
}
</script>

<template>
  <div>
    <h1>List</h1>
    <pre>{{ list }}</pre>
    <button @click="add">Add</button>
    <button @click="save">Save</button>
  </div>
</template>
```

## Cookies in API-Routen

Du kannst `getCookie` und `setCookie` aus dem [`h3`](https://github.com/unjs/h3) Paket verwenden, um Cookies in Server API Routen zu setzen.

```ts [server/api/counter.ts]
export default defineEventHandler(event => {
  // Lese Counter Cookie
  let counter = getCookie(event, 'counter') || 0

  // Erhöhe Counter Cookie um 1
  setCookie(event, 'counter', ++counter)

  // Senden einer JSON Antwort
  return { counter }
})
```

:link-example{to="/docs/examples/advanced/use-cookie"}
