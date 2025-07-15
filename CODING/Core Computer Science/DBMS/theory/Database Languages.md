#  Data Definition Language (DDL)
- Used to **define the schema** of the database.
- Specifies:
  - Tables
  - Attributes
  - Constraints (e.g., PK, FK, NOT NULL)

🔸 *Examples:*  
```sql
CREATE TABLE users (...);
ALTER TABLE orders ADD COLUMN status;
```

---
# Data Manipulation Language (DML)
- Used to **modify and query** data.
- Operations:  
    `INSERT`, `DELETE`, `UPDATE`, `SELECT`

---
## Query Language (subset of DML)
- Used to **retrieve data** using queries.

``` sql
SELECT name FROM employees WHERE dept = 'HR';
```

---
# SQL – Structured Query Language
- Combines both:
    - **DDL** → define structure
    - **DML** → manipulate data

``` sql
CREATE TABLE product (...); -- DDL  
INSERT INTO product VALUES (...); -- DML  
```

---
# 🔗 Accessing DB from Application
- Use **APIs** to connect application code to DB.
### Common Interfaces:
- **JDBC** → for Java
- **ODBC** → for C/C++ and others

---
