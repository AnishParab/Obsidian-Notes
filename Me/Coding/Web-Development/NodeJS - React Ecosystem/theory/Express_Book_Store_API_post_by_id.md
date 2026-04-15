# `models/books.store.js`

``` js
let nextId = 3

exports.create = ({ title, author }) => {
	const newBook = {
		id: nextId++,
		title,
		author
	}
	
	books.push(newBook)
	return newBook
}
```

---
# `controllers/books.controllers.js`

``` js
exports.createBook = (req, res) => {
	const { title, author } = req.body
	
	if {
		typeof title !== 'string' ||
		typeof author !== 'string' ||
		!title.trim() ||
		!author.trim()
	} {
		return res.status(400).json({
			error: 'Invalid payload: title and author required'
		})
	}
	
	const book = store.create({
		title: title.trim(),
		author: author.trim()
	})
	
	res.status(201).location(`/books/${book.id}`).json(book)
}
```

---
# `routes/books.routes.js`

``` js
router.post('/', booksController.createBook)
```

---
