# Install Node via Volta

```bash
volta install node@20
```

Effect:
- Installs Node.
- Creates Volta shims in PATH.

---
# Pin Version to Project

Inside project:
```bash
volta pin node@20
```

Updates `package.json`:
```json
"volta": {
  "node": "20.x.x"
}
```

Purpose:
- Declares required runtime.

---
#  Verify Active Runtime

```bash
node -v
which node
```

Expected:
```
~/.volta/bin/node
```

---
