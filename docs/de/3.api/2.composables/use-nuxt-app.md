---
title: 'useNuxtApp'
description: 'Zugriff auf den gemeinsamen Laufzeitkontext der Nuxt-Anwendung.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts
    size: xs
---

`useNuxtApp` ist ein eingebauter Komposable, der einen Weg zur Verwendung des gemeinsamen Laufzeitkontexts der Nuxt-Anwendung bereitstellt. Dieser Kontext wird auch als [Nuxt-Kontext](/docs/de/guide/going-further/nuxt-app#der-nuxt-kontext) bezeichnet und ist sowohl auf dem Client- als auch auf dem Serverseiten verfügbar (aber nicht innerhalb von Nitro-Routen). Er hilft Ihnen dabei, Zugriff auf die Vue-App-Instanz, Laufzeit-Hooks, Laufzeit-Konfigurationsvariablen und interne Zustände wie `ssrContext` und `payload` zu erhalten.

```vue [app.vue]
<script setup lang="ts">
const nuxtApp = useNuxtApp()
</script>
```

Wenn der Laufzeitkontext in Ihrem Bereich nicht verfügbar ist, wirft `useNuxtApp` bei Aufruf eine Ausnahme. Sie können stattdessen `tryUseNuxtApp` für Komposables verwenden, die keine `nuxtApp` benötigen, oder um einfach zu überprüfen, ob der Kontext verfügbar ist, ohne eine Ausnahme zu werfen.

<!--
Hinweis
Standardmäßig ist der gemeinsame Laufzeitkontext von Nuxt unter der Option [`buildId`](/docs/api/nuxt-config#buildid) ange命名原因：由于中文和德文的句子结构和长度差异，直接翻译可能会导致代码块中的语法错误或格式问题。因此，在翻译过程中需要特别注意保持代码块的正确性和完整性。

以下是翻译后的德文Markdown：

---
title: 'useNuxtApp'
description: 'Zugriff auf den gemeinsamen Laufzeitkontext der Nuxt-Anwendung.'
links:
  - label: Quelle
    icon: i-simple-icons-github
    to: https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts
    size: xs
---

`useNuxtApp` ist ein eingebauter Komposable, der einen Weg zur Verwendung des gemeinsamen Laufzeitkontexts der Nuxt-Anwendung bereitstellt. Dieser Kontext wird auch als [Nuxt-Kontext](/docs/de/guide/going-further/nuxt-app#der-nuxt-kontext) bezeichnet und ist sowohl auf dem Client- als auch auf dem Serverseiten verfügbar (aber nicht innerhalb von Nitro-Routen). Er hilft Ihnen dabei, Zugriff auf die Vue-App-Instanz, Laufzeit-Hooks, Laufzeit-Konfigurationsvariablen und interne Zustände wie `ssrContext` und `payload` zu erhalten.

```vue [app.vue]
<script setup lang="ts">
const nuxtApp = useNuxtApp()
</script>
```

Wenn der Laufzeitkontext in Ihrem Bereich nicht verfügbar ist, wirft `useNuxtApp` bei Aufruf eine Ausnahme. Sie können stattdessen `tryUseNuxtApp` für Komposables verwenden, die keine `nuxtApp` benötigen, oder um einfach zu überprüfen, ob der Kontext verfügbar ist, ohne eine Ausnahme zu werfen.

<!--
Hinweis
Standardmäßig ist der gemeinsame Laufzeitkontext von Nuxt unter der Option [`buildId`](/docs/api/nuxt-config#buildid) angegeben. Er ermöglicht die Unterstützung mehrerer Laufzeitkontexte.

## Parameter

- `appName`: eine optionale Anwendungsname. Wenn Sie ihn nicht angeben, wird der Nuxt `buildId`-Option verwendet. Andernfalls muss er mit einem vorhandenen `buildId` übereinstimmen.
-->

## Methoden

### `provide (name, value)`

`nuxtApp` ist ein Laufzeitkontext, den Sie mit [Nuxt Plugins](/docs/de/guide/directory-structure/plugins) erweitern können. Verwenden Sie die `provide` Funktion, um Nuxt Plugins zu erstellen, die Werte und Hilfemethoden in Ihrer Nuxt-Anwendung überall in Komposables und Komponenten verfügbar machen.

Die `provide` Funktion akzeptiert die Parameter `name` und `value`.

```js
const nuxtApp = useNuxtApp()
nuxtApp.provide('hello', (name) => `Hallo ${name}!`)

// Druckt "Hallo name!"
console.log(nuxtApp.$hello('name'))
```

Wie im obigen Beispiel zu sehen, hat `$hello` sich zu einer neuen und benutzerdefinierten Teil des `nuxtApp` Kontextes entwickelt und ist überall verfügbar, wo `nuxtApp` zugänglich ist.

### `hook(name, cb)`

Verfügbare Hooks in `nuxtApp` ermöglichen es Ihnen, die Laufzeiteigenschaften Ihrer Nuxt-Anwendung anzupassen. Sie können Laufzeit-Hooks in Vue.js Komposables und [Nuxt Plugins](/docs/de/guide/directory-structure/plugins) verwenden, um in das Rendering-Lebenszyklus einzubinden.

Die `hook` Funktion ist nützlich, um benutzerdefinierte Logik hinzuzufügen, indem Sie in einem bestimmten Punkt des Rendering-Lebenszyklus eingebunden werden. Die `hook` Funktion wird am häufigsten bei der Erstellung von Nuxt Plugins verwendet.

Siehe [Runtime Hooks](/docs/api/advanced/hooks#app-hooks-runtime) für verfügbare Runtime Hooks, die von Nuxt aufgerufen werden.

```ts [plugins/test.ts]
export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.hook('page:start', () => {
    /* Ihre Code hier */
  })
  nuxtApp.hook('vue:error', (..._args) => {
    console.log('vue:error')
    // if (import.meta.client) {
    //   console.log(..._args)
    // }
  })
})
```

### `callHook(name, ...args)`

`callHook` gibt eine Promise zurück, wenn Sie mit einem der vorhandenen Hooks aufgerufen wird.

```ts
await nuxtApp.callHook('my-plugin:init')
```

## Eigenschaften

`useNuxtApp()` bietet die folgenden Eigenschaften, die Sie verwenden können, um Ihre App zu erweitern und Zustände, Daten und Variablen zu teilen.

### `vueApp`

`vueApp` ist die globale Vue.js [Application-Instanz](https://vuejs.org/api/application.html#application-api), die Sie durch `nuxtApp` zugänglich machen können.

Nützliche Methoden:
- [`component()`](https://vuejs.org/api/application.html#app-component) - Registriert eine globale Komponente, wenn Sie sowohl den Namen als auch die Komponentendefinition übergeben, oder ruft eine bereits registrierte Komponente ab, wenn nur der Name übergeben wird.
- [`directive()`](https://vuejs.org/api/application.html#app-directive) - Registriert eine globale benutzerdefinierte Direktive, wenn Sie sowohl den Namen als auch die Direktivedefinition übergeben, oder ruft eine bereits registrierte Direktive ab, wenn nur der Name übergeben wird [(Beispiel)](/docs/de/guide/directory-structure/plugins#vue-direktiven).
- [`use()`](https://vuejs.org/api/application.html#app-use) - Installiert eine **[Vue.js Plugin](https://vuejs.org/guide/reusability/plugins.html)** [(Beispiel)](/docs/de/guide/directory-structure/plugins#vue-plugins).

:read-more{icon="i-simple-icons-vuedotjs" to="https://vuejs.org/api/application.html#application-api"}

### `ssrContext`

`ssrContext` wird während des Serverseitigen Renderings generiert und ist nur auf dem Serverseiten verfügbar.

Nuxt stellt die folgenden Eigenschaften über `ssrContext` zur Verfügung:
- `url` (String) - Aktuelle Anfrage-URL.
- `event` ([unjs/h3](https://github.com/unjs/h3) Anfrageereignis) - Zugriff auf die Anfrage und Antwort der aktuellen Route.
- `payload` (Objekt) - NuxtApp Payload-Objekt.

### `payload`

`payload` ermöglicht die Übertragung von Daten und Zustandsvariablen vom Serverseiten zum Clientseiten. Die folgenden Schlüssel sind nach dem Übertragen vom Serverseiten auf dem Clientseiten verfügbar:

- `serverRendered` (Boolean) - Gibt an, ob die Antwort serverseitig gerendert wurde.
- `data` (Objekt) - Wenn Sie Daten aus einem API-Endpunkt abrufen, entweder mit [`useFetch`](/docs/api/composables/use-fetch) oder mit [`useAsyncData`](/docs/api/composables/use-async-data), kann das Payload über `payload.data` abgerufen werden. Diese Daten werden gespeichert und helfen Ihnen, um die gleichen Daten in Fällen zu vermeiden, in denen identische Anfragen mehrmals gestellt werden.

  ::code-group
  ```vue [app.vue]
  <script setup lang="ts">
  const { data } = await useAsyncData('count', () => $fetch('/api/count'))
  </script>
  ```
  ```ts [server/api/count.ts]
  export default defineEventHandler(event => {
    return { count: 1 }
  })
  ```
  ::

  Nach dem Abrufen des Wertes von `count` mit [`useAsyncData`](/docs/api/composables/use-async-data) im obigen Beispiel, wenn Sie `payload.data` abrufen, sehen Sie dort `{ count: 1 }` aufgezeichnet.

  Wenn Sie den gleichen `payload.data` von [`ssrcontext`](#ssrcontext) abrufen, können Sie den gleichen Wert auch auf dem Serverseiten abrufen.

- `state` (Objekt) - Wenn Sie mit der [`useState`](/docs/api/composables/use-state) Komposable in Nuxt ein gemeinsames Zustand festlegen, kann dieser Zustand über `payload.state.[name-of-your-state]` abgerufen werden.

  ```ts [plugins/my-plugin.ts]
  export const useColor = () => useState<string>('color', () => 'pink')

  export default defineNuxtPlugin((nuxtApp) => {
    if (import.meta.server) {
      const color = useColor()
    }
  })
  ```

  Es ist auch möglich, mehr fortgeschrittene Typen wie `ref`, `reactive`, `shallowRef`, `shallowReactive` und `NuxtError` zu verwenden.

  Seit [Nuxt v3.4](https://nuxt.com/blog/v3-4#payload-enhancements) ist es möglich, eigene Reducer/Reviver für Typen zu definieren, die von Nuxt nicht unterstützt werden.

  ::tip{icon="i-lucide-video" to="https://www.youtube.com/watch?v=8w6ffRBs8a4" target="_blank"}
  Schauen Sie sich ein Video von Alexander Lichter über die Serienisierung von Payloads an, insbesondere im Hinblick auf Klassen.
  ::

  Im folgenden Beispiel definieren wir ein Reducer (oder Serialisierer) und ein Reviver (oder Deserialisierer) für die [Luxon](https://moment.github.io/luxon/#/) DateTime-Klasse, mithilfe eines Payload Plugins.

  ```ts [plugins/date-time-payload.ts]
  /**
   * Dieser Art von Plugin läuft sehr früh im Nuxt-Lebenszyklus, bevor wir den Payload wiederherstellen.
   * Sie haben keinen Zugriff auf den Router oder andere von Nuxt injizierten Eigenschaften.
   *
   * Beachten Sie, dass der "DateTime" String der Typbezeichner ist und muss
   * sowohl beim Reducer als auch beim Reviver identisch sein.
   */
  export default definePayloadPlugin((nuxtApp) => {
    definePayloadReducer('DateTime', (value) => {
      return value instanceof DateTime && value.toJSON()
    })
    definePayloadReviver('DateTime', (value) => {
      return DateTime.fromISO(value)
    })
  })
  ```

### `isHydrating`

Verwenden Sie `nuxtApp.isHydrating` (Boolean), um zu überprüfen, ob die Nuxt-App auf dem Clientseiten hydriert wird.

```ts [components/nuxt-error-boundary.ts]
export default defineComponent({
  setup (_props, { slots, emit }) {
    const nuxtApp = useNuxtApp()
    onErrorCaptured((err) => {
      if (import.meta.client && !nuxtApp.isHydrating) {
        // ...
      }
    })
  }
})
```

### `runWithContext`

::note
Sie sind wahrscheinlich hier, weil Sie eine "Nuxt-Instanz nicht verfügbar"-Nachricht erhalten haben. Geben Sie diese Methode nur selten bei und melden Sie Beispiele, die Probleme verursachen, damit sie letztendlich am Framework-Ebene gelöst werden können.
::

Die `runWithContext` Methode dient dazu, eine Funktion aufzurufen und ihr einen expliziten Nuxt-Kontext zu geben. Normalerweise wird der Nuxt-Kontext implizit weitergegeben und Sie müssen sich nicht darum kümmern. Allerdings, wenn Sie mit komplexen `async`/`await` Szenarien in Middleware/Plugins arbeiten, können Sie Situationen erleben, in denen die aktuelle Instanz nach einer asynchronen Aufruf unset ist.

```ts [middleware/auth.ts]
export default defineNuxtRouteMiddleware(async (to, from) => {
  const nuxtApp = useNuxtApp()
  let user
  try {
    user = await fetchUser()
    // der Vue/Nuxt-Kompiler verliert den Kontext hier wegen des try/catch Blocks.
  } catch (e) {
    user = null
  }
  if (!user) {
    // legen Sie den richtigen Nuxt-Kontext für unsere `navigateTo`-Aufrufe fest.
    return nuxtApp.runWithContext(() => navigateTo('/auth'))
  }
})
```

#### Verwendung

```js
const result = nuxtApp.runWithContext(() => functionWithContext())
```

- `functionWithContext`: Jede Funktion, die den Kontext der aktuellen Nuxt-Anwendung benötigt. Dieser Kontext wird automatisch korrekt angewendet.

`runWithContext` gibt das zurück, was von `functionWithContext` zurückgegeben wird.

#### Tieferes Verständnis des Kontexts

Das Vue.js Composition API (und Nuxt Composables ähnlich) funktioniert, indem sie auf einen impliziten Kontext abhängen. Während des Lebenszyklus setzt Vue eine temporäre Instanz des aktuellen Komponenten (und Nuxt eine temporäre Instanz von nuxtApp) in einer globalen Variable und löst sie in der gleichen Tick. Bei Serverseitigem Rendering gibt es mehrere Anfragen von verschiedenen Benutzern und nuxtApp läuft in einem gleichen globalen Kontext. Aufgrund dieses Vorgangs setzt Nuxt und Vue diese globale Instanz sofort frei, um eine geteilte Referenz zwischen zwei Benutzern oder Komponenten zu vermeiden.

Was bedeutet das? Das Composition API und Nuxt Composables sind nur während des Lebenszyklus und in der gleichen Tick vor asynchronen Operationen verfügbar:

```js
// --- Vue intern ---
const _vueInstance = null
const getCurrentInstance = () => _vueInstance
// ---

// Vue / Nuxt setzt eine globale Variable, die auf die aktuelle Komponente verweist, in _vueInstance, wenn setup aufgerufen wird.
async function setup() {
  getCurrentInstance() // Arbeitet
  await someAsyncOperation() // Vue löst den Kontext in der gleichen Tick vor asynchroner Operation!
  getCurrentInstance() // null
}
```

Die klassische Lösung dafür ist, die aktuelle Instanz auf der ersten Aufruf in eine lokale Variable wie `const instance = getCurrentInstance()` zu speichern und sie in der nächsten Komposable-Aufruf zu verwenden, aber das Problem ist, dass jede verschachtelte Komposable-Aufruf jetzt explizit die Instanz als Argument akzeptieren muss und nicht auf den impliziten Kontext des Composition-API abhängen darf. Dies ist eine Designbeschränkung mit Composable und kein Problem im Sinne.

Um diese Beschränkung zu überwinden, macht Vue etwas Hintergrundarbeit, wenn unser Anwendungscode kompiliert wird, und restauriert den Kontext nach jeder Aufruf für `<script setup>`:

```js
const __instance = getCurrentInstance() // Generiert durch den Vue-Kompiler
getCurrentInstance() // Arbeitet!
await someAsyncOperation() // Vue löst den Kontext
__restoreInstance(__instance) // Generiert durch den Vue-Kompiler
getCurrentInstance() // Noch immer funktioniert!
```

Für eine bessere Beschreibung dessen, was Vue tatsächlich tut, siehe [unjs/unctx#2 (Kommentar)](https://github.com/unjs/unctx/issues/2#issuecomment-942193723).

#### Lösung

Daher kann `runWithContext` verwendet werden, um den Kontext zu restaurieren, ähnlich wie `<script setup>` funktioniert.

Nuxt intern verwendet [unjs/unctx](https://github.com/unjs/unctx) zum Unterstützung von Composable, die ähnlich wie Vue für Plugins und Middleware sind. Dies ermöglicht Composable wie `navigateTo()` zu funktionieren, ohne direkt `nuxtApp` zu übergeben - bringt die DX und Leistungsvorteile des Composition API auf den gesamten Nuxt-Framework.

Nuxt Composable haben das gleiche Design wie das Vue Composition API und brauchen daher eine ähnliche Lösung, um diesen Transform zu machen. Siehe [unjs/unctx#2](https://github.com/unjs/unctx/issues/2) (Vorschlag), [unjs/unctx#4](https://github.com/unjs/unctx/pull/4) (Transform Implementierung) und [nuxt/framework#3884](https://github.com/nuxt/framework/pull/3884) (Integration in Nuxt).

Vue unterstützt derzeit nur asynchrone Kontext-.Restoration für `<script setup>` für async/await Nutzung. In Nuxt wurde die Transform-Support für `defineNuxtPlugin()` und `defineNuxtRouteMiddleware()` hinzugefügt, was bedeutet, dass wenn Sie sie verwenden, Nuxt sie automatisch mit Kontext-Restoration transformiert.

#### Restliche Probleme

Die `unjs/unctx` Transformation zur automatischen Kontext-.Restoration scheint mit `try/catch` Statements, die `await` enthalten, fehlerhaft zu sein, was letztendlich gelöst werden muss, um die oben empfohlene Workaround-Lösung entfernen zu können.

#### Native Asynchrone Kontexte

Mit einer neuen experimentellen Funktion ist es möglich, native asynchrone Kontexte zu aktivieren, indem man [Node.js `AsyncLocalStorage`](https://nodejs.org/api/async_context.html#class-asynclocalstorage) und neue unctx Unterstützung nutzt, um asynchrone Kontexte **natürlich** für **jede verschachtelte asynchrone Komposable** verfügbar zu machen, ohne eine Transformierung oder manuelle Übertragung/Anrufung mit Kontext zu benötigen.

::tip
Native asynchrone Kontexte funktionieren derzeit in Bun und Node.
::

:read-more{to="/docs/de/guide/going-further/experimental-features#asynccontext"}

## tryUseNuxtApp

Diese Funktion funktioniert genau wie `useNuxtApp`, aber gibt `null` zurück, wenn der Kontext nicht verfügbar ist, anstatt eine Ausnahme zu werfen.

Sie können sie für Komposables verwenden, die keine `nuxtApp` benötigen, oder um einfach zu überprüfen, ob der Kontext verfügbar ist, ohne eine Ausnahme zu werfen.

Beispielverwendung:

```ts [composable.ts]
export function useStandType() {
  // Im Client immer erfolgreich
  if (tryUseNuxtApp()) {
    return useRuntimeConfig().public.STAND_TYPE
  } else {
    return process.env.STAND_TYPE
  }
}
```

<!-- ### Parameter

- `appName`: eine optionale Anwendungsname. Wenn Sie ihn nicht angeben, wird der Nuxt `buildId`-Option verwendet. Andernfalls muss er mit einem vorhandenen `buildId` übereinstimmen. -->