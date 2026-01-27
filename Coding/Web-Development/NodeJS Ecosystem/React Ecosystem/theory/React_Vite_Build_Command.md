# `build` Command
## Purpose
- Produces a **production-ready, static artifact** from source code.
- Transforms development code into **optimized browser-consumable files**.

---
## What Happens (High-Level)
When you run:
```bash
pnpm build
```

the script typically executes:
```bash
vite build
```

Vite then:
- Resolves the full dependency graph
- Transpiles JSX and modern JavaScript
- Bundles modules into static assets
- Minifies and optimizes output
- Hashes filenames for cache safety

---
## Output
- Generated files are written to:
```
dist/
```
- These files are **static** and can be served by any web server.

---
# Key Invariant
> After `build`, no Node.js or pnpm is required to run the app — only a static file server.

---
