# Types of Modules (Node.js)
### Built-in Modules

- Provided by Node.js runtime.
- No installation required.

Examples:
```
fs
path
http
os
```

Import:
```js
import fs from "fs";
```

---
### Third-Party Modules

- External packages from npm registry.
- Installed via package manager.

Example:
```bash
npm install express
```

Import:
```js
import express from "express";
```

---
### Custom / Internal Modules

- Files created within the project.
- Used to organize application code.

Example:
```js
import helper from "./helper.js";
```

---
