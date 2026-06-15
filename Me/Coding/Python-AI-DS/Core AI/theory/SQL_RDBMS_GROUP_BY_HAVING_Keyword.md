**Refer this example**
[[SQL_RDBMS_MySQL_Example_1]]

---
# `HAVING`

- Just like how, `WHERE` is used to filter from `SELECT`,
- `HAVING` is used to **filter** from `GROUP BY`

> Out of the categories made by `GROUP BY`, we would like to know only particular thing (condition).

---
# SQL Query

**Department and count having more than 2 workers**
``` sql
SELECT DEPARTMENT, COUNT(DEPARTMENT) FROM Worker GROUP BY DEPARTMENT HAVING COUNT(DEPARTMENT) > 2;
```

---
