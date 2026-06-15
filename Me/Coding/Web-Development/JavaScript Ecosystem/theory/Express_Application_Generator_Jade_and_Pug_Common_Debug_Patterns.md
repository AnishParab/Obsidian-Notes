# Why this matters

When debugging legacy SSR code, the real difficulty is identifying **which layer is failing**:

```text
Routing vs Rendering vs Layout vs Static
```

A short checklist file prevents scanning the entire project.

---
# Suggested Contents

Layered debugging order:

```text
1. Does route call res.render()?
2. Is view engine configured?
3. Does template exist in views/?
4. Does layout inheritance match block names?
5. Are static assets expected from public/ instead of views/?
```

Common misconceptions to include:
- `res.send()` bypasses Pug completely.
- `.pug` extension should not be used in `res.render()`.
- Static middleware runs before rendering.

---
