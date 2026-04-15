# Refer

[[Express_Book_Store_API_Basic_Codes]]

---
# `models/books.store.js`

``` js
const books = [
  { id: 1, title: 'Book One', author: 'Author One'},
  { id: 2, title: 'Book Two', author: 'Author Two'}
]

let nextId = 3
```

---
# `controllers/books.controllers.js`

``` js
const store = require('../models/books.store.js')
```

---
# `routes/books.routes.js`

``` js
const router = require('express').Router()
const booksController = require('../controllers/books.controller.js')

module.exports = router
```

---
