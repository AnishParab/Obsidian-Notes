# Versioning using `mise`

- Manage `node.js`, `python` and other runtimes in one tool with **`.mise.toml`**

```toml
# .mise.toml — project-level Node version
[tools]
node = "20"
```

```bash
mise use node@20    # sets version for current project
mise use --global node@lts  # sets global default
```

---
