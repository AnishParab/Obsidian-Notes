# CommonJS

Setup — `package.json`:
```json
{ "type": "commonjs" }
```

Importing:
```js
// built-in
const fs = require('node:fs')
const path = require('node:path')

// third-party
const express = require('express')

// custom — relative path, extension optional in CJS
const math = require('./math')
const utils = require('../utils/helper')
```

Exporting:
```js
// single export
module.exports = function add(a, b) { return a + b }

// multiple exports
module.exports = { add, subtract, multiply }

// named individually
exports.add = (a, b) => a + b
exports.subtract = (a, b) => a - b
```

Importing exports:
```js
// default export
const add = require('./math')

// multiple exports
const { add, subtract } = require('./math')
```

---
# Gotchas:

- `require` is synchronous
- Module is cached after first load — same object returned on subsequent requires
- `exports` is shorthand for `module.exports` — never reassign `exports` directly, use `module.exports`
- `__dirname` and `__filename` available natively

---
