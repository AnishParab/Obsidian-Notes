# Node.js Installation — 2 Approaches

## 1) System Install (`pacman`)

- Installs Node system-wide.
- Single global version.
- Managed by OS updates.

Use when:
- One runtime for entire machine.
- Server or stable environment.

---
### 2) User Install (`nvm` + `.nvmrc`)

- Installs Node per user.
- Supports multiple versions.
- `.nvmrc` declares project runtime.

Use when:

- Development workflows.
- Different projects need different Node versions.

---
# **Key Difference**

```
pacman → system runtime
nvm    → user-level version manager
```

---
