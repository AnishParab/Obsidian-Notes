# Corepack vs pnpm Store

## Corepack — What It Is

- Manages **package manager binaries**
- Handles **pnpm / yarn versions**
- **Not** a dependency installer

**Invariant**
- Never installs project dependencies

---
## Corepack Responsibilities

- Read `package.json → packageManager`
- Resolve required pnpm version
- Download pnpm binary if missing
- Execute that pnpm version

**Storage**
```
~/.local/share/corepack/
```

- Stores **only binaries**

---
## pnpm Store — What It Is

- Stores **project dependencies**
- Global, content-addressable
- Shared across all projects

**Invariant**
- Packages stored once, linked everywhere

---
## pnpm Store Details

- Stores package contents (by hash)
- Immutable after write

**Storage**
```
~/.pnpm-store
```

(or `~/.local/share/pnpm/store`)

- Corepack never touches this

---
## Execution Flow

```
Shell → pnpm (shim) → Corepack → pnpm (binary)
```

---
## Responsibility Split

**Corepack**
- Version resolution
- Binary management

**pnpm**
- Read `pnpm-lock.yaml`
- Resolve dependency graph
- Fetch from pnpm store
- Create `node_modules` via symlinks

---
# Summary

- Corepack = **pnpm launcher**
- pnpm = **dependency manager**
- Stores are **separate by design**

---
