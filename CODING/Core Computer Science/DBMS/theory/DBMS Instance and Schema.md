# Instance of Database
- The **snapshot** of data at a particular moment.
- It **changes frequently** as data is inserted, updated, or deleted.

🔸 *Example:*  
> Current records in the `students` table right now  
> (`id: 1, name: "Aman"`)

---
#  Database Schema
- **Blueprint/Structure** of the database.
- Describes how data is **organized** and how the **relationships** are defined.

Includes:
- **Attributes** of tables  
  > e.g., `name VARCHAR(255)`, `age INT`
- **Constraints**  
  > e.g., `PRIMARY KEY`, `NOT NULL`, `UNIQUE`
- **Relationships**  
  > e.g., `FOREIGN KEY`, `One-to-Many`

### Levels of Schema:
1. **Physical Schema** – storage details  
2. **Logical Schema** – table structures & relations  
3. **View Schema** – user-specific views

---

# 🔁 Summary

| Concept  | Description                       | Changes Frequently |
| -------- | --------------------------------- | ------------------ |
| Instance | Actual data in the database now   | ✅ Yes              |
| Schema   | Structural design of the database | ❌ No               |

---
