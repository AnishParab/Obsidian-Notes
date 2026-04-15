# Corepack

``` bash
sudo pacman -S corepack
```

You must already have:
- **Node.js installed** (preferably via `nvm`, `fnm`, or `asdf`)
- **Corepack enabled**

```bash
corepack enable
```

This ensures:
- No global pnpm binaries
- Per-project pnpm version control

``` bash
pnpm -v
```

---
