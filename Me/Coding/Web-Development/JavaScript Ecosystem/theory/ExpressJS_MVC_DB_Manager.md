# `/db`

`book.js`
``` js
exports.BOOKS = [
	{ id: 1, title: 'Book One', author: 'Author One' },
	{ id: 2, title: 'Book Two', author: 'Author Two' },
]
```

---
# `index.js`

``` js
const express = require('express')
const {BOOKS} = require('../db/book')
const router = express.Router()

```

---
