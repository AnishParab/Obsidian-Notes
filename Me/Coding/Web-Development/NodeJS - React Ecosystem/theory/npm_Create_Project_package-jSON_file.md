# Why `package.json`

- Defines project metadata.
- Marks a directory as an `npm` package.
- Allows dependency management, scripts, and module configuration.

---
# Make your Project a Package using `npm`

## Step 1 — Initialize at Project Root

Create `package.json`:

```bash
mkdir project
cd project

## Now
npm init
## OR
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
  "homepage": "https://github.com/anishparab/hello-world#readme",
  "repository": {
    "type": "git",
    "url": "https://github.com/anishparab/hello-world.git"
  },
  "bugs": {
    "url": "https://github.com/anishparab/hello-world/issues"
  },
  "keywords": [
    "nodejs",
    "backend",
    "production"
  ],
  "engines": {
    "node": ">=20"
  },
  "files": [
    "index.js",
    "lib/"
  ],
  "scripts": {
    "start": "node index.js",
    "dev": "node --watch index.js",
    "test": "node --test"
  }
}
```

---
