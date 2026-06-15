**Refer this example**
[[SQL_RDBMS_MySQL_Example_1]]

---
# Pattern Searching / Wildcard

`%` - Any number of characters, including `0` characters.

`_` - Only one character

---
# SQL Query

**Second last letter is `p`**
``` sql
SELECT * FROM Worker WHERE FIRST_NAME LIKE '%p_';
```

---
