# `index.js`
``` js
import express from 'express';

import bookRouter from './routes/book.route.js';

import { loggerMiddleware } from './middlewares/logger.js';

const app = express();
const PORT = 8000;

// Middlewares
app.use(express.json());
app.use(loggerMiddleware);

// Routes
app.use('/books', bookRouter);

app.listen(PORT, () => console.log(`Server is running on PORT 8000`));
```

---
# `routes/book.route.js`
``` js
import express from 'express';

import { BOOKS } from '../db/book.js';

const router = express.Router();

router.get('/', (req, res) => {
  res.setHeader('x-asp', 'anish parab');
  return res.json(BOOKS); // Array will be coverted to JSON
});

// Dynamic Routing
router.get('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const book = BOOKS.find((e) => e.id === id);

  // Bad Request
  if (isNaN(id))
    return res.status(400).json({ error: `Id must be of type number` });

  // ID does not exist
  if (!book) return res.status(404).json({ error: `Book with id ${id} does not exist` });

  return res.json(book);
});

router.post('/', (req, res) => {
  // NOTE: req.body requires the express.json() middleware
  const { title, author } = req.body;

  if (!title || title === '') return res.status(400).json({ error: 'title is required' });
  if (!author || author === '') return res.status(400).json({ error: 'author is required' });

  const id = BOOKS.length + 1;

  const book = { id, title, author };
  BOOKS.push(book);

  return res.status(201).json({ message: 'Book created successfully', id });
});

router.delete('/:id', (req, res) => {
  const id = parseInt(req.params.id);

  if (isNaN(id))
    return res.status(400).json({ error: `id must be of type number` });

  const indexToDelete = BOOKS.findIndex(e => e.id === id);

  if (indexToDelete < 0)
    return res.status(404).json({ error: `Book with id ${id} does not exist` });

  BOOKS.splice(indexToDelete, 1);

  return res.status(200).json({ message: 'Book deleted' });
});

export default router;
```

---
# `middlewares/logger.js`
``` js
import fs from 'node:fs';

// Middleware to log into a file
export const loggerMiddleware = function(req, res, next) {
  const log = `[${Date.now()}] ${req.method} ${req.path}`;
  fs.appendFileSync('logs.txt', log, 'utf-8');
  next();
};
```

---
# `db/book.js`
``` js
// In memory database since we don't have a database
export const BOOKS = [
  { id: 1, title: 'Book One', author: 'Author One' },
  { id: 2, title: 'Book Two', author: 'Author Two' },
];
```

---
