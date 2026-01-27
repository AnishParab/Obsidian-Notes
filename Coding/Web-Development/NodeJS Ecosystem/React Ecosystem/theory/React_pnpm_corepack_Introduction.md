# Purpose
- Manages **package manager binaries** (pnpm, yarn)
- Ensures **per-project pnpm version pinning**
- Acts as a **dispatcher**, not a package installer

Key invariant:
> Corepack never installs project dependencies.

---
# What it handles
- Reads `package.json → packageManager`
- Resolves the required pnpm version
- Downloads that pnpm binary if missing
- Executes the correct pnpm version
### Storage directory
Corepack stores **only package manager binaries**:
```
~/.local/share/corepack/
```
(Exact path may vary by OS, but scope is the same.)

---
# pnpm-store
### Purpose
- Stores **npm packages** (project dependencies)
- Uses a **content-addressable, global store**
- Shared safely across all pnpm projects

Key invariant:
> Packages are stored once and linked, never duplicated.
### What it stores
- Package tarball contents
- Indexed by content hash
- Immutable once written
### Storage directory
Default pnpm store location:
```
~/.pnpm-store
```

(or `~/.local/share/pnpm/store` depending on setup)
> Corepack never touches this directory.

---
# Project-Level Flow
### Execution Chain
```
Shell → pnpm (shim)
```

```
pnpm (shim) → Corepack
```

---
# Corepack Responsibilities
- Reads `package.json`
- Resolves required pnpm version
- Downloads pnpm binary if needed
- Executes that pnpm binary

---
# pnpm Responsibilities
- Reads `pnpm-lock.yaml`
- Resolves exact dependency graph
- Fetches packages from pnpm store
- Creates project-local `node_modules` via symlinks

---
