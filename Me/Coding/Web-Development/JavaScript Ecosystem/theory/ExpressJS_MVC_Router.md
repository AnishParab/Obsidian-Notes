# `routes` folder

- `book.routes.js`
``` js
const express = require('express')

const router = express.Router()

// Get all books
// books route is managed in index.js
router.get('/', (req,res) => {
	return res.json(books)
})

// Get book by ID
router.get('/:id', customMiddleware, loggerMiddleware, (req,res) => {
  const id = parseInt(req.params.id)
  const book = books.find((e) => e.id === id) //SELECT * from books where id = {id}

  if (isNaN(id)) return res.status(400).json({ error: `id must be of type number`})

  if (!book) return res.status(404).json({ error: `Book with ${id} does not exist`})

  return res.json(book)
})

module.exports = router
```

---
# `index.js`

``` js
const express = require('express')

const bookRouter = require('./routes/book.routes')

// Any request that starts with books, will move the bookRouter
app.use('/books', bookRouter)
```

---
