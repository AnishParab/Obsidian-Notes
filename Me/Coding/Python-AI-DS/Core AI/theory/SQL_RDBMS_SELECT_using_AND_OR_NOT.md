
**Refer this example**
[[SQL_RDBMS_MySQL_Example_1]]

---
# SQL Query

`OR` - **All workers who work in `HR`,  `Admin` or `Account`**
``` sql
SELECT * FROM Worker WHERE DEPARTMENT = 'HR' OR DEPARTMENT = 'Admin' OR DEPARTMENT = 'Account';
```

`AND` - **All workers who work in both `HR` and `Admin`**
``` sql
SELECT * FROM Worker WHERE DEPARTMENT = 'HR' AND DEPARTMENT = 'Admin';
```

`NOT` - **All workers who are not in `HR` and `Admin`**
``` sql
SELECT * FROM Worker WHERE DEPARTMENT NOT IN ('HR', 'Admin');
```

---
