``` js
import express from 'express';
import fs from 'node:fs';
const app = express();
const PORT = 8000;

// In memory database since we don't have a database
const books = [
  { id: 1, title: 'Book One', author: 'Author One' },
  { id: 2, title: 'Book Two', author: 'Author Two' },
];

// Middlewares
app.use(express.json());

// Middleware to log into a file
app.use(function(req, res, next) {
  const log = `[${Date.now()}] ${req.method} ${req.path}`;
  fs.appendFileSync('logs.txt', log, 'utf-8');
  next();
});

app.use(function(req,res,next){
	const log = `[${Date.now()}] ${req.method} ${req.path}`;
});

app.get('/books', (req, res) => {
  res.setHeader('x-asp', 'anish parab');
  return res.json(books); // Array will be coverted to JSON
});

// Dynamic Routing
app.get('/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const book = books.find((e) => e.id === id);

  // Bad Request
  if (isNaN(id))
    return res.status(400).json({ error: `Id must be of type number` });

  // ID does not exist
  if (!book) return res.status(404).json({ error: `Book with id ${id} does not exist` });

  return res.json(book);
});

app.post('/books', (req, res) => {
  // NOTE: req.body requires the express.json() middleware
  const { title, author } = req.body;

  if (!title || title === '') return res.status(400).json({ error: 'title is required' });
  if (!author || author === '') return res.status(400).json({ error: 'author is required' });

  const id = books.length + 1;

  const book = { id, title, author };
  books.push(book);

  return res.status(201).json({ message: 'Book created successfully', id });
});

app.delete('/books/:id', (req, res) => {
  const id = parseInt(req.params.id);

  if (isNaN(id))
    return res.status(400).json({ error: `id must be of type number` });

  const indexToDelete = books.findIndex(e => e.id === id);

  if (indexToDelete < 0)
    return res.status(404).json({ error: `Book with id ${id} does not exist` });

  books.splice(indexToDelete, 1);

  return res.status(200).json({ message: 'Book deleted' });
});

app.listen(PORT, () => console.log(`Server is running on PORT 8000`));
```

---
