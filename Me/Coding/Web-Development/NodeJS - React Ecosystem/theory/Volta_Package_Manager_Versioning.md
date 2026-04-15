# Purpose

- Pin package manager versions at project level.
- Ensure deterministic installs and script execution.
- Volta ensures compatible versions.

---
# Pin Versions to Project

> Inside project:

```bash
volta pin npm@10
volta pin yarn@1
volta pin pnpm@9
```

Updates `package.json`:
```json
"volta": {
  "node": "20.x.x",
  "npm": "10.x.x",
  "yarn": "1.x.x",
  "pnpm": "9.x.x"
}
```

---
# Supported Tools

Volta can manage:
```
node
npm
yarn
pnpm
npx
corepack-enabled tools
```

Any CLI installed through Volta inherits pinned runtime.

---
# Verify Active Versions

```bash
npm -v
yarn -v
pnpm -v
which npm
```

Expected:
```
~/.volta/bin/...
```

---
# Execution Model

```
Command issued
      ↓
Volta shim
      ↓
Pinned tool version executes
```

---
