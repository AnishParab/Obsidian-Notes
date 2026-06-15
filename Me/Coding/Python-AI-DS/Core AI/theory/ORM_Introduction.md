# ORM Introduction

- ORM (Object-Relational Mapper) = maps database tables to code objects
- Query the DB using your language instead of raw SQL
- Each table → class, each row → instance, each column → property

```js
// Raw SQL
SELECT * FROM users WHERE id = 1

// ORM equivalent (Prisma)
await prisma.user.findUnique({ where: { id: 1 } })
```

- Handles: queries, relationships, migrations, connection pooling
- Trade-off: abstraction hides SQL — can generate inefficient queries
- Popular JS ORMs: Prisma, TypeORM, Sequelize, Drizzle

---
