# Nullish Coalescing Operator - `??`

```js
// || triggers on ANY falsy: 0, "", false, null, undefined
let port = userPort || 3000
// problem: if userPort = 0, you wanted 0 but get 3000

// ?? triggers ONLY on null/undefined
let port = userPort ?? 3000
// if userPort = 0, you get 0 ✓
// if userPort = null, you get 3000 ✓
```

> **Rule**: use `??` when `0`, `""`, or `false` are valid values in your logic. Use `||` only when all falsy values should fallback.

---
