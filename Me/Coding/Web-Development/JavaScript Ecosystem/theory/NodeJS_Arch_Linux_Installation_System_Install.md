# Using (`pacman`)

- Installs Node system-wide.
- Single global version.
- Managed by OS updates.

```bash
# via pacman (stable)
sudo pacman -S nodejs npm

# verify
node -v
npm -v
```

---
# Using `mise`

*manage `python` and `node.js`, both using `mise`*
```bash
mise use --global node@lts
```

- This is the better path since you're already managing Python with mise. Keeps Node versioned and isolated.

---
