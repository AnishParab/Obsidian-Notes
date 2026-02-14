# Volta — Introduction

- **Volta** = JavaScript toolchain manager.
- Manages **Node**, **npm**, **yarn**, **pnpm** versions per project.
- Uses **project configuration**, not shell switching.

---
# Core Idea

```
package.json → declares runtime
Volta        → enforces pinned versions automatically
```

No manual `nvm use`.

---
# Key Properties

- User-level install (no root).
- Deterministic execution.
- Works in non-interactive shells and CI.
- Avoids PATH mutation per session.

---
# How It Differs

| Tool   | Mechanism                        |
| ------ | -------------------------------- |
| nvm    | Shell-based version switching    |
| pacman | System-wide runtime              |
| Volta  | Project-pinned runtime execution |

---
# Mental Model

```
Command executed
      ↓
Volta shim intercepts
      ↓
Correct Node version runs
```

---
