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
app.get('/', (req, res) => {
  res.send('Search for "/books" route');
});

app.use('/books', bookRouter);

app.listen(PORT, () => console.log(`Server is running on PORT 8000`));
```

---
# `.env`
``` text
DATABASE_URL=postgres://postgres:admin@localhost:5432/book-store
```

---
# `docker-compose.yml`
``` yml
services:
  postgres:
    image: postgres:17.4
    ports:
      - 5432:5432
    environment:
      POSTGRES_DB: book-store
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: admin
```

---
# `drizzle.config.js`
``` js
import 'dotenv/config';
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  dialect: 'postgresql',
  out: './drizzle',
  schema: './models/index.js',
  dbCredentials: {
    url: process.env.DATABASE_URL,
  },
});
```

---
# `drizzle/`
- Manually, nothing was created inside this directory.

---
# `db/index.js`
``` js
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/node-postgres';

// postgres://<username>:<password>@<host>:<port>/<db_name>
export const db = drizzle(process.env.DATABASE_URL);
```

---
# `routes/book.route.js`
``` js
import express from 'express';

import * as controller from '../controllers/book.controller.js';

const router = express.Router();

router.get('/', controller.getAllBooks);

// Dynamic Routing
router.get('/:id', controller.getBookById);

router.post('/', controller.createBook);

router.delete('/:id', controller.deleteBookById);

export default router;
```

---
# `models/book.model.js`
``` js
import { pgTable, uuid, varchar, text } from "drizzle-orm/pg-core";
import { authorsTable } from "./author.model.js";

export const booksTable = pgTable("books", {
  id: uuid("id").primaryKey().defaultRandom(),
  title: varchar("title", { length: 100 }).notNull(),
  description: text("description"),
  authorId: uuid("author_id")
    .references(() => authorsTable.id)
    .notNull(),
});

// NOTE: These kind of relations are not possible in MongoDB
```

---
# `models/author.model.js`
``` js
import { pgTable, uuid, varchar, text } from "drizzle-orm/pg-core";

export const authorsTable = pgTable('authors', {
  id: uuid().primaryKey().defaultRandom(),
  firstName: varchar({ lenght: 55 }).notNull(),
  lastName: varchar({ lenght: 55 }),
  email: varchar({ length: 255 }).notNull().unique(),
});
```

---
# `models/index.js`
``` js
import { booksTable } from "./book.model";
import { authorsTable } from "./author.model";

export { booksTable, authorsTable };
```

---
# `controllers/book.controller.js`
``` js
import { booksTable } from "../models/book.model.js";
import { db } from "../db/index.js";
import { eq } from "drizzle-orm";

export const getAllBooks = async function(req, res) {
  const books = await db.select().from(booksTable);
  return res.json(books); // Array will be coverted to JSON
};

export const getBookById = async function(req, res) {
  const id = req.params.id;
  const [book] = await db.select().from(booksTable).where((table) => eq(table.id, id)).limit(1);

  // Bad Request
  if (isNaN(id))
    return res.status(400).json({ error: `Id must be of type number` });

  // ID does not exist
  if (!book) return res.status(404).json({ error: `Book with id ${id} does not exist` });

  return res.json(book);
};

export const createBook = async function(req, res) {
  const { title, authorId, description } = req.body;

  if (!title || title === '') return res.status(400).json({ error: 'title is required' });

  const [result] = await db.insert(booksTable).values({
    title,
    authorId,
    description,
  }).returning({
    id: booksTable.id,
  }).onConflictDoNothing();

  return res.status(201).json({ message: 'Book created successfully', id: result.id });
};

export const deleteBookById = async function(req, res) {
  const id = req.params.id;

  await db.delete().from(booksTable).where(eq(booksTable.id, id)).limit(1);

  return res.status(200).json({ message: 'Book deleted' });
};
```

---
