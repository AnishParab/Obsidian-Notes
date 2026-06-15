# Why `package.json`

- Defines project metadata.
- Marks a directory as an `npm` package.
- Allows dependency management, scripts, and module configuration.

---
# Make your Project a Package using `npm`

Create `package.json`:
```bash
mkdir project
cd project

## Now
npm init
## BETTER
npm init -y
```

> **NOTE** : Production-Standard
``` bash
entry point: (index.js)
```

---
## Example `package.json` - Production Level

```json
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "Production-ready Node.js application",
  "license": "MIT",
  "author": "Anish Parab",
  "type": "commonjs",
  "main": "index.js",
  "engines": { "node": ">=20" },
  "scripts": {
    "start": "node index.js",
    "dev": "node --watch index.js",
    "test": "node --test"
  },
  "files": ["index.js", "lib/"],
  "repository": { "type": "git", "url": "https://github.com/anishparab/hello-world.git" },
  "bugs": { "url": "https://github.com/anishparab/hello-world/issues" },
  "homepage": "https://github.com/anishparab/hello-world#readme",
  "keywords": ["nodejs", "backend"]
}
```

---
