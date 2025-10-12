# `package.json`
``` json
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node --watch index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "module",
  "dependencies": {
    "@types/node": "^24.5.2",
    "express": "^5.1.0"
  }
}
```

---
# Semantic Versioning
- Syntax: X1.X2.X3 ---> **Bits**
- X1 ---> Major Version
- X2 ---> Minor Version
- X3 ---> Patch Version

---
# Patch Version
- Incremented for backward-compatible bug fixes.
- These updates address issues without adding new functionality or breaking anything.
- For instance, 1.2.3 to 1.2.4 signals a bug fix that doesn't affect compatibility.

---
# Minor Version
- Incremented when new functionality is added in a backward-compatible way.
- This means that existing code should continue to work, but new features are available.
- For example, 1.2.0 to 1.3.0 suggests that new features are introduced without breaking compatibility.

----
# Major Version
- Incremented when there are incompatible API changes.
- These changes may break existing functionality or require modifications in dependent code.
- For example, 1.0.0 to 2.0.0 indicates a significant change that may require users to update their code.

---


---
