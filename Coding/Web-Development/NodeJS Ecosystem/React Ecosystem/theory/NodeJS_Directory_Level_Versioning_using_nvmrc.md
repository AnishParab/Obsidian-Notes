# NOTE

> This approach is only possible if Node.js and npm was installed using `nvm` and not globally using `pacman`.

---
# Purpose

- Pins **Node runtime version** at project level.
- Ensures consistent execution across environments.

---
# Steps
### Create Project

```bash
mkdir project-name
cd project-name
```

---
### Declare Node Version

```bash
echo "20" > .nvmrc
```

- File contains only the version string.

---
### Activate Version

```bash
nvm use
```

Behavior:
- Reads `.nvmrc`
- Switches active Node via PATH.

If version not installed:
```bash
nvm install
```

---
### Verify

```bash
node -v
which node
```

Expected path:
```
~/.nvm/versions/node/...
```

---
### Structure

```
project-name/
 ├── .nvmrc
 └── package.json
```

---
