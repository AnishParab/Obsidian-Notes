# ES Module

Setup — `package.json`:
```json
{ "type": "module" }
```

Importing:
```js
// built-in
import fs from 'node:fs'
import { readFile, writeFile } from 'node:fs'

// third-party
import express from 'express'

// custom — .js extension required
import math from './math.js'
import { add, subtract } from '../utils/helper.js'
```

Exporting:
```js
// default export
export default function add(a, b) { return a + b }

// named exports
export const add = (a, b) => a + b
export const subtract = (a, b) => a - b

// export at bottom
const add = (a, b) => a + b
const subtract = (a, b) => a - b
export { add, subtract }
```

Importing exports:
```js
// default
import add from './math.js'

// named
import { add, subtract } from './math.js'

// both
import add, { subtract } from './math.js'

// all as namespace
import * as math from './math.js'
```

Dynamic import (lazy load):
```js
const module = await import('./math.js')
```

---
# Gotchas:

- `.js` extension mandatory in import paths
- Loading is asynchronous
- Top-level `await` supported
- `__dirname` and `__filename` not available — replace with:

```js
import { fileURLToPath } from 'node:url'
import { dirname } from 'node:path'
const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)
```

---
