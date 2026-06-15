**Refer this example**
[[SQL_RDBMS_MySQL_Example_1]]

---
# `ADD` new Column

``` sql
ALTER TABLE Worker ADD AGE INT NOT NULL DEFAULT 0;

DESC Worker;
```

---
# Better Approach to add AGE

``` sql
CREATE TABLE Customer (
	DATE_OF_BIRTH DATE
);

SELECT TIMESTAMP(YEAR, DATE_OF_BIRTH, CURDATE()) AS AGE FROM Customer;

DESC Worker;
```

- **Prduction Techniques**: Because AGE is derived data.

---
