# Data Models
- Used to **design** the database at the **logical level**.
- Provide the **framework** to represent:
  - Data
  - Relationships
  - Semantics
  - Constraints

> A data model defines **how data is connected** and **how it can be accessed**.

---
# Purpose
- Define **structure** of data.
- Support **data consistency rules**.
- Provide a **standard way to design** databases.

---
# Common Data Models

## ER Model (Entity-Relationship)
- Uses **entities**, **attributes**, and **relationships**.
- Good for **conceptual database design**.

🔸 *Example:*  
> `Student` entity has `name`, `roll`, and relates to `Course`.

---
## Relational Model
- Data is stored in **tables (relations)**.
- Based on **set theory and first-order logic**.

🔸 *Example:*  
> Table: `Employees(id, name, dept_id)`

---
## Object-Oriented Model
- Data + behavior are stored as **objects**.
- Supports **inheritance**, **encapsulation**, etc.

🔸 *Example:*  
> `class Employee` with fields and methods, stored in DB.

---
## Object-Relational Model
- Combines **Relational + OOP** features.
- Supports **complex data types**, **inheritance**, etc.

🔸 *Example:*  
> PostgreSQL allows custom object types in relational tables.

---
# Summary

| Model             | Key Feature                   |
| ----------------- | ----------------------------- |
| ER Model          | High-level, conceptual design |
| Relational Model  | Tables, rows, columns         |
| Object-Oriented   | Data as objects with methods  |
| Object-Relational | Mix of tables and objects     |

---
