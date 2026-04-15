# NOTE

- Below given examples are **Synchronous** in nature
- Refer
[[NodeJS_Synchronous_and_Asynchronous_Code]]
> for **Asynchronous** codes.

---
# File System Module in Node.js

> **NOTE:** `node:fs` has been recently added in newer versions of `node.js` that explicitly tells that `fs` is a built-in module.

``` js
const fs = require('node:fs')

console.log(fs)
```

---
# Code to Read and Write files

``` js
const fs = require('node:fs')

const content = fs.readFileSync('notes.txt', 'utf-8')

console.log(content)

// Always overwrites the content
fs.writeFileSync('copy.txt', 'I want to write this', 'utf-8')

// Don't overwrite the content
fs.appendFileSync('copy.txt', content, 'utf-8')
```

---
# Create and Remove Directories

``` js
const fs = require('node:fs')

fs.mkdirSync('games')

fs.mkdirSync('games/xyz/a', { recursive: true })

fs.rmdirSync('games/xyz/a')
```

---
# Delete Files

``` js
const fs = require('node:fs')

fs.writeFileSync('copy.txt', 'To be deleted later', 'utf-8')

fs.unlinkSync('copy.txt')
```

---
