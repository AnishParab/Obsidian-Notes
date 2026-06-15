# Browser - Inspect

- Access: `F12` or `Ctrl+Shift+I` or right-click → Inspect

---
# Tabs:

| Tab         | Purpose                                           |
| ----------- | ------------------------------------------------- |
| Elements    | Live DOM tree + CSS editor                        |
| Console     | JS REPL + logs + errors                           |
| Sources     | JS files + breakpoint debugger                    |
| Network     | HTTP requests, responses, timing                  |
| Performance | Runtime profiling, FPS, bottlenecks               |
| Memory      | Heap snapshots, memory leaks                      |
| Application | localStorage, cookies, IndexedDB, service workers |
| Lighthouse  | Performance + SEO + accessibility audit           |

---
# Key features:

**Elements tab**
- Click any element → inspect/edit HTML and CSS live
- `$0` in console → references currently selected element
- Force element state: right-click → Force state → `:hover`, `:focus`, etc.

**Network tab**
- See every HTTP request the page makes
- Filter by type: XHR, Fetch, JS, CSS, IMG
- Click request → see headers, payload, response, timing
- Throttle network speed to simulate slow connections

**Sources tab**
- Set breakpoints by clicking line numbers
- Step through JS execution
- Watch variables, call stack, scope

**Console shortcuts**
```js
$0        // last selected DOM element
$("div")  // querySelector shorthand
$$("div") // querySelectorAll shorthand
$_        // last evaluated expression
```

---
