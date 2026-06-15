# `INNER JOIN`

![[sql_inner_joins.excalidraw|300]]

> Returns only the rows where matching values exist in both tables for the given key.

---
# Syntax

``` sql
SELECT column-list FROM table1 INNER JOIN table2 ON condition1 INNER JOIN table3 ON condition2
```

---
# SQL Query

``` sql
SELECT c.*, o.* FROM CUSTOMER AS c INNER JOIN Orders AS o ON c.id = o.cust_id;
```

---
