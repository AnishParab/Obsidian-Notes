# `models/books.store.js`

``` js
exports.getByID = (id) => {
	return books.find(book => book.id === id) || null
}
```

---
# `controllers/books.controllers.js`

``` js
exports.getBookById = (req,res) => {
	const id = Number(req.params.id)
	
	if (!Number.isInteger(id)) {
		return res.status(400).json({ error: 'Invalid book id' })
	}
	
	const book = store.getById(id)
	
	if (!book) {
		return res.status(404).json({ error: 'Book not found' })
	}
	
	res.json(book)
}
```

---
# `routes/books.routes.js`

``` js
router.get('/:id', booksController.getBookById)
```

---
