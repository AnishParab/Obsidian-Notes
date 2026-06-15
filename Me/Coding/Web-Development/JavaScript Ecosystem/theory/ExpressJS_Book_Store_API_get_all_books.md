# `models/books.store.js`

``` js
exports.getAll = () => books
```

---
# `controllers/books.controllers.js`

``` js
exports.getAllBooks = (req,res) => {
	res.json(store.getAll())
}
```

---
# `routes/books.routes.js`

``` js
router.get('/', booksController.getAllBooks)
```

---
