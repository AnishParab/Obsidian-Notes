# Route-Level Middlewares

``` js
function loggerMiddleware(req, res, next) {
	const log = `\n[${Date.now()}] ${req.method} ${req.path}`
	fs.appendFileSync('logs.txt', log, 'utf-8')
	next()
}

// Get book by ID
app.get('/books/:id', loggerMiddleware, (req,res) => {
  const id = parseInt(req.params.id)
  const book = books.find((e) => e.id === id) //SELECT * from books where id = {id}

  if (isNaN(id)) return res.status(400).json({ error: `id must be of type number`})

  if (!book) return res.status(404).json({ error: `Book with ${id} does not exist`})

  return res.json(book)
})
```

**Sequence** :
``` text
loggerMiddleware ----> (req,res) body
```

---
