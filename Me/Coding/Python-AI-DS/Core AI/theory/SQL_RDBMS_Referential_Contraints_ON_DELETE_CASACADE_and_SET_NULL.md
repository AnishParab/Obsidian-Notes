# Pre-requisites

[[SQL_RDBMS_Referential_Integrity_Constraints]]

---
# `ON DELETE CASCADE` - for Insert constraint

> Deletes child rows automatically when the parent row is deleted.

``` sql
CREATE TABLE Department (
    ID INT PRIMARY KEY
);

CREATE TABLE Employee (
    ID INT PRIMARY KEY,
    DEPT_ID INT,
    FOREIGN KEY (DEPT_ID)
        REFERENCES Department(ID)
        ON DELETE CASCADE
);
```

``` sql
DELETE FROM Department WHERE ID = 1;
```

- Related rows in `Employee` are also deleted.

---
# `ON DELETE SET NULL` - for Delete constraint

> Sets foreign key values to `NULL` when the parent row is deleted.

``` sql
CREATE TABLE Department (
    ID INT PRIMARY KEY
);

CREATE TABLE Employee (
    ID INT PRIMARY KEY,
    DEPT_ID INT,
    FOREIGN KEY (DEPT_ID)
        REFERENCES Department(ID)
        ON DELETE SET NULL
);
```

``` sql
DELETE FROM Department WHERE ID = 1;
```

- `DEPT_ID` becomes `NULL` in `Employee`.

---
