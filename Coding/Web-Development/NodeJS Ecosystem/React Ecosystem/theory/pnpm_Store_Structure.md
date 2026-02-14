# pnpm Store Structure

## Global Store

- Single content-addressable store
- Default: `~/.pnpm-store`
- Packages stored by **hash**, not by project

---
## Virtual Store (per project)

- Located in `node_modules/.pnpm/`
- Contains real package directories
- Names include package + version + hash

---
## node_modules Layout

- Top-level `node_modules` has **symlinks only**
- Symlinks point into `.pnpm/`
- Prevents access to undeclared deps

---
## Linking

- **Hard links**: from global store → `.pnpm/`
- **Symlinks**: from `node_modules` → `.pnpm/`

---
## Result

- Single copy per package version
- Strict dependency isolation
- Fast installs

---
