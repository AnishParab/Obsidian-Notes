# Examples of an ORM
- **Python to Postgres** → SQLAlchemy
- **JavaScript/TypeScript to Postgres** → Drizzle
- **JavaScript/TypeScript to MongoDB** -> Mongoose

- **Prisma** ---> JavaScript to Many types of Databases.

---
# What is an ORM?
- **Object Relation Mapping**.
- It is a piece of software designed to translate between the data representations used by databases and those used in object-oriented programming. 
- It’s like a translator between the world of **objects in code** (classes, methods, attributes) and the world of **rows in a relational database** (tables, columns, queries).

---
# Example
- Instead of writing raw SQL queries like:
``` sql
SELECT * FROM users WHERE id = 1;

```

- you’d interact with your database in your programming language, like:
``` python
user = User.objects.get(id=1)

```

---
# Why ORMs Exist
- Programming languages are **object-oriented** (Python, Java, C#, etc.).
- Databases are **relational** (tables, foreign keys).
- ORMs bridge this mismatch (sometimes called the “object-relational impedance mismatch”).

---
