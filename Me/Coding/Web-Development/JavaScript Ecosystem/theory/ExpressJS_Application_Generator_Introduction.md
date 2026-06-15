# Express.js — Application Generator

- `express-generator` is a **project scaffolding tool**.
- It generates a predefined folder structure and boilerplate code.
- It does **not** change Express runtime behavior.

Key idea:
```
Generator = File Structure Template
Express    = Runtime Framework
```

Common misconception:
- Using the generator is not required to build Express apps.

---
# Why It Exists

Primary goals:
- Standardize project layout.
- Separate application logic from server bootstrap.
- Provide SSR-ready structure with views.

Debug relevance:
- Many legacy Express projects use this layout.
- Understanding the structure helps locate bugs quickly.

---
# Core Insight

The generator encodes one opinionated architecture:
```
Server Runtime (bin)
Application Wiring (app.js)
Routing Layer (routes)
Rendering Layer (views)
Static Layer (public)
```

Understanding this separation is sufficient to navigate and debug most generator-based Express projects.

---
