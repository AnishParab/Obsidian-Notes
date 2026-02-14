## Node.js vs Browser APIs

- **JavaScript** = language.
- APIs like `alert`, `fetch`, `document` are **environment-provided**, not part of JS itself.

---
# Example
### `alert`

- `alert()` = **Browser API**.
- Provided by browser runtime.
- Not available in Node.js.

---
# Two Execution Environments

### Browser Environment

Provides:
```
JavaScript
+ DOM API
+ Web APIs (alert, fetch, localStorage, document)
```

Example:
```
alert()
window
document
```

---
### Node.js Environment

Provides:
```
JavaScript
+ Node APIs (fs, http, process)
+ Timers (setTimeout, setInterval)
```

No DOM or UI APIs.

---
# Key Difference

```
JS Language      → same everywhere
Runtime APIs     → depend on environment
```

---
