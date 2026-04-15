# Installing Dependencies using `npm`

## Pre-requisite

- [[npm_Create_Project_package-jSON_file]]

---
## Install a Dependency

```bash
npm install @types/node
```

---
# Result

- Adds package to `node_modules/`
- Updates `package.json` → `dependencies`
- Updates / creates `package-lock.json`

---
# Notes

- Installs from npm registry.
- Version resolved using semver rules.
- Local install (default) scopes dependency to the project.

---
