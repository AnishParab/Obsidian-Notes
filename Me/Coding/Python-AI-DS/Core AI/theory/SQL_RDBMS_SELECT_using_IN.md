**Refer this example**
[[SQL_RDBMS_MySQL_Example_1]]

---
# `IN`

- Reduces **OR** conditions.

---
# SQL Query

**All workers who work in `HR`,  `Admin` or `Account`**
``` sql
SELECT * FROM Worker WHERE DEPARTMENT = 'HR' OR DEPARTMENT = 'Admin' OR DEPARTMENT = 'Account';
```

**BETTER WAY**
``` sql
SELECT * FROM Worker WHERE DEPARTMENT IN ('HR', 'Admin', 'Account')
```

---
