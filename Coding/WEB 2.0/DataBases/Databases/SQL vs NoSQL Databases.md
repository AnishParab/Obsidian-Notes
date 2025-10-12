# SQL
- Also called as **Relational Databases**.
- Structured Data.
> Rules are enforced on the database Layer.
- Postgres, MySQL are some examples.

---
# NoSQL
- Also called as **Non-Relational Databases**.
- Non-Structural Data.
> Rules are enforced on the Application Layer.
- MongoDB is an example.
- **Data Format**: `key : value`

---
# Example
## NoSQL
``` json
{
  "users": {
    "id": "A",
    "gender": "m",
    "name": "A",
    "friends": ["B", "C", "Z"]
  }
}
```
- Stores data as documents (JSON-like).
- Embedded arrays/objects for relationships (e.g., `friends` list).
- **No fixed schema** → flexible structure.

---
## SQL
- **One-to-Many** or **Many-to-Many** handled via separate relation tables (e.g., `Friends`).
- Schema enforces **consistency** and **structure**.

---
- User Schema

| id  | name | email | password | profileImage |
| --- | ---- | ----- | -------- | ------------ |
| A   | ...  | ...   | ...      | ...          |
| B   | ...  | ...   | ...      | ...          |
| C   | ...  | ...   | ...      | ...<br>      |

---
- Friends Schema (Many to Many Relationship)

| user_first | user_second |
| ---------- | ----------- |
| A          | B           |
| A          | C           |

---
## Key Difference
- **NoSQL (MongoDB)**
    - Schema-less
    - Stores relationships directly in documents (embedded arrays).
    - Flexible but may duplicate data.
- **SQL (PostgreSQL/MySQL)**
    - Schema-based
    - Relationships via joins and foreign keys.
    - Structured, consistent, but stricter.

---