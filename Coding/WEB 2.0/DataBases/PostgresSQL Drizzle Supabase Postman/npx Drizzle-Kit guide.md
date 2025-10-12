# Generate a Migration
- Compare schema vs migration history → outputs SQL.
``` bash
npx drizzle-kit generate

```
- This will create a new file in `./drizzle/YYYYMMDDHHMM_migration.sql`.

---
# Apply Migrations
- Run all pending migrations on your DB.
``` bash
npx drizzle-kit migrate

```
- After this, your DB schema matches your Drizzle schema.

---
# Reset migrations (wipe + rebuild)
- Drops everything, then re-applies migrations:
``` bash
npx drizzle-kit migrate reset

```
- ⚠️ This destroys data — use for dev/testing only.

---
# Push schema directly
- Instead of generating migrations, directly apply schema changes.
``` bash
npx drizzle-kit push

```
- This is like Prisma’s `db push`. Useful in dev, but avoid in prod (migrations are safer).

---
# Introspect existing DB
- Generate Drizzle schema from an existing database.
``` bash
npx drizzle-kit introspect

```
- It’ll spit out `.ts` files describing your tables.

---
# Studio (visualizer)
- Spin up a UI to explore your DB & schema.
``` bash
npx drizzle-kit studio

```
- This gives you a browser UI with tables, queries, etc.

---
# **Typical Workflow**
- Change your schema file (add table/column).
- Generate migration:
``` bash
npx drizzle-kit generate

```
- Apply migration:
``` bash
npx drizzle-kit migrate

```
- Restart your Node app:
``` bash
node index.js

```

---
