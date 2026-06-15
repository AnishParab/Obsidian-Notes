# Node v/s Browser APIs

- JavaScript = language
- APIs = environment-provided, not part of JS itself.

```
Browser = JS + DOM + Web APIs (alert, fetch, document, localStorage)
Node.js = JS + Node APIs (fs, http, process) + Timers
```

- `alert()`, `window`, `document` → browser only
- `fs`, `process`, `http` → Node only
- `setTimeout`, `fetch` → both (fetch added to Node in v18)

> Rule: same language, different APIs depending on runtime.

---
**Why does `require` work only in `node.js` and not in `vanilla-js` ?**
- [[NodeJS_Wrapper_Function_Introduction]]

---
