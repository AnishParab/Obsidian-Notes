> Reference of the website is in [[Postgres Drizzle Setup First Steps and TS Setup]]

---
# Step 1 : Create `docker-compose.yml`
[[Setting up Postgres with Docker for Local Development]]

---
# Step 2:
- Create `drizzle` folder.
- Create `drizzle.config.js` file.
- `npm init` for `package.json` file.

---
# Step 3:
``` bash
npm i drizzle-orm pg
```

---
# Step 4: `db/index.js`
``` js
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/node-postgres';

// postgres://<username>:<password>@<host>:<port>/<db_name>
export const db = drizzle("postgres://postgres:admin@localhost:5432/mydb");
```
- The postgres URL is setup in `docker-compose.yml`

---
# Step 5: `drizzle/schema.js`
``` js
import { pgTable, integer, varchar } from "drizzle-orm/pg-core";

// Name of the Table is users
export const usersTable = pgTable('users', {
  id: integer().primaryKey(),
  name: varchar({ length: 255 }).notNull(),
  email: varchar({ length: 255 }).notNull().unique()
});
```

---
# Step 6: Install
``` bash
npm i -D drizzle-kit 
```

---
# Step 7: `drizzle.config.js`
``` js
import 'dotenv/config';
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  dialect: 'postgresql',
  out: './drizzle',
  schema: './drizzle/schema.js',
  dbCredentials: {
    url: 'postgres://postgres:admin@localhost:5432/mydb',
  },
});
```

---
# Step 8: Applying changes to the database
- This reads `drizzle.config.js`
``` bash
npx drizzle-kit push
```

---
# Step 9: Check Everything on a UI
``` bash
npx drizzle-kit studio
```

---
# `index.js`
``` js
import 'dotenv/config';
import { db } from "./db/index.js";
import { usersTable } from "./drizzle/schema.js";

async function getAllUsers() {
  const users = await db.select().from(usersTable)
  console.log(`Users in DB`, users);
  return users;
};

async function createUser({ id, name, email }) {
  await db.insert(usersTable).values({
    id,
    name,
    email,
  }).onConflictDoNothing();
};

createUser({ id: 1, name: 'Anish', email: 'anish@example.com' });

getAllUsers();
```

---
# Step 11: `.env`
``` bash
npm i dotenv
```

``` txt
DATABASE_URL=postgres://postgres:admin@localhost:5432/mydb
```
- Now replace the **URL** from the rest of your codebase with `process.env.DATABASE_URL`

---
# Step 12: TypeScript and LSP support ?
``` bash
npm i -D tsx @types/pg
```

And follow : 
[Postgres Drizzle](https://orm.drizzle.team/)

---
