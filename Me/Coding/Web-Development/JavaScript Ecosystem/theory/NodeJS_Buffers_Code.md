# Code 1 - `.alloc()`

``` js
const { Buffer } = require('node:buffer')

const buf = Buffer.alloc(4)
console.log(buf)
console.log(buf[1])
```

**Output**:
``` text
<Buffer 00 00 00 00>
0
```

---
# Code 2 - `.from` and `.toString()`

``` js
const { Buffer } = require('node:buffer')

const buf = Buffer.from('Hello chai')
console.log(buf)
console.log(buf.toString())
```

**Output**:
``` text
<Buffer 48 65 6c 6c 6f 20 63 68 61 69>
Hello chai
```

---
# Code 3 - `.write()`

``` js
const { Buffer } = require('node:buffer')

const buf = Buffer.alloc(10)
buf.write('Hello')
console.log(buf.toString())
```

**Output**:
``` text
Hello
```

---
# Code 5 -  `utf-8`

``` js
const { Buffer } = require('node:buffer')

const buf = Buffer.from("Chai aur Code")
buf.write(buf.toString())
console.log(buf.toString("utf8", 0, 4))
```

**Output**:
``` text
Chai
```

---
# Code 5 - Changing Characters

``` js
const { Buffer } = require('node:buffer')

const buf = Buffer.from("Chai")
console.log(buf.toString())

buf[0] = 0x4A
console.log(buf.toString())
```

**Output**:
``` text
Chai
Jhai
```

---
# Code 6 - `.concat()` and `.length`

``` js
const { Buffer } = require('node:buffer')

const buf1 = Buffer.from("Chai aur")
const buf2 = Buffer.from(" Code")

const merged = Buffer.concat([buf1, buf2])
console.log(merged.toString())

console.log(merged.length)
```

**Output**:
``` text
Chai aur Code
13
```

---
