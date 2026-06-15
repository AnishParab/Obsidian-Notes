**Refer this example**
[[SQL_RDBMS_MySQL_Example_1]]

---
# `GROUP BY`

- All unique values.

---
# Aggregation Functions

- `COUNT`
- `SUM`
- `AVG`
- `MIN`
- `MAX`

> If no aggregation functions are used, `GROUP BY` acts like `DISTINCT`.

---
# SQL Query

**Number of employees working in different department**
``` sql
SELECT DEPARTMENT, COUNT(DEPARTMENT) FROM Worker GROUP BY DEPARTMENT;
```

---
