# Features

| Feature        | **CommonJS (CJS)**             | **ES Modules (ESM)**                           |
| -------------- | ------------------------------ | ---------------------------------------------- |
| File Extension | `.js`                          | `.mjs` or `"type": "module"` in `package.json` |
| Syntax         | `require()` & `module.exports` | `import` & `export`                            |
| Used In        | Node.js (default before v13)   | Browser & modern Node.js (v13+)                |
| Execution      | Synchronously                  | Asynchronously                                 |

---
# Difference

| Topic            | **CommonJS**           | **ES Modules**               |
| ---------------- | ---------------------- | ---------------------------- |
| Default in Node? | ✅ Yes (before v13)     | ✅ Yes (after v14.8+)         |
| Exports syntax   | `module.exports = ...` | `export default / export {}` |
| Imports syntax   | `require()`            | `import ... from ...`        |
| Top-level await  | ❌ Not supported        | ✅ Supported                  |
| File loading     | Synchronous            | Asynchronous                 |

---
# CommonJS Example
``` js
// utils.js
function greet(name) {
  return `Hello, ${name}`;
}
module.exports = greet;

// app.js
const greet = require('./utils');
console.log(greet('Arch User'));
```

---
# ESM **(ECMAScript / ES6 Modules)** Example
``` js
// utils.mjs
export function greet(name) {
  return `Hello, ${name}`;
}
```

``` js
// app.mjs
import { greet } from './utils.mjs';
console.log(greet('NeoVim User'));
```

---
# Example
`commonJS`
``` js
exports.getAllBooks = function(req, res) {
  res.setHeader('x-asp', 'anish parab');
  return res.json(BOOKS); // Array will be coverted to JSON
};
```

`ejs`
``` js
export const getAllBooks = (req, res) => {
  res.setHeader('x-asp', 'anish parab');
  return res.json(BOOKS); // Array will be coverted to JSON
};
```

---
