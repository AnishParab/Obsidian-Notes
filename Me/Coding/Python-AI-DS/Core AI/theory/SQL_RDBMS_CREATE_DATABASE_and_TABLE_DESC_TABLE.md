> Also Refer : [[SQL_RDBMS_INSERT_VALUES_INTO_and_SELECT_ALL_for_Tables]] for complete **basic workflow**.

---
# Create and Use DB

```sql
CREATE DATABASE IF NOT EXISTS temp;

SHOW DATABASES;

USE temp;
```

---
# Create Table

> NOTE: `PRIMARY KEY` is in capitals.  
> It is a good practice to keep SQL-specific keywords in uppercase.

```sql
CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

SHOW TABLES;

DESC student;
```

---
