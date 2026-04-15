# Code

``` js
const express = require('express')
const app = express()
const port = 3000

app.use(express.json())

// In-memory DB
const books = [
  { id: 1, title: 'Book One', author: 'Author One'},
  { id: 2, title: 'Book Two', author: 'Author Two'},
]

// Get all books
app.get('/books', (req,res) => {
  res.json(books)
})

// Get book by ID
app.get('/books/:id', (req,res) => {
  const id = parseInt(req.params.id)
  const book = books.find((e) => e.id === id) //SELECT * from books where id = {id}

  if (isNaN(id)) return res.status(400).json({ error: `id must be of type number`})

  if (!book) return res.status(404).json({ error: `Book with ${id} does not exist`})

  return res.json(book)
})

// Add books
app.post('/books', (req,res) => {
  const { title, author } = req.body
  
  if (!title || title === '') return res.status(400).json({ error: 'title is required' })
  if (!author || author === '') return res.status(400).json({ error: 'author is required' })

  id = books.length + 1

  const book = { id: id, title, author}
  books.push(book)

  return res.status(201).json({ message: 'Book created success', id: id})
})

// Delete book
app.delete('/books/:id', (req,res) => {
  const id = parseInt(req.params.id)

  if (isNaN(id)) return res.status(400).json({ error: 'ID must be of type number' })

  const indexToDelete = books.findIndex((e) => e.id === id)

  if (indexToDelete < 0) return res.status(404).json({ error: `Book with ${id} does ot exist` })

  books.splice(indexToDelete, 1)

  return res.status(200).json({ message: 'book deleted' })
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```

**Test** :
``` bash

```

---
