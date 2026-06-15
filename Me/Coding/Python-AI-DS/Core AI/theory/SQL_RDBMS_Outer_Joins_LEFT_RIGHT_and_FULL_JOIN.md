# `LEFT JOIN`

![[Left_join_sql_rdbms.excalidraw|300]]


``` sql
SELCET c.*, o.* FROM Customer as c LEFT JOIN Orders as o ON c.id = o.cust_id;
```

---
# `RIGHT JOIN`

![[Me/Coding/Python-AI-DS/Core AI/excalidraw/right_join_sql.excalidraw|300]]

``` sql
SELCET c.*, o.* FROM Customer as c RIGHT JOIN Orders as o ON c.id = o.cust_id;
```

---
# Full JOIN using `UNION`

![[full_join_sql.excalidraw|300]]

- Emulated in MySQL using `LEFT` and `RIGHT JOIN` - `UNION`

``` sql
SELECT c.*, o.*
FROM Customer AS c
LEFT JOIN Orders AS o
ON c.id = o.cust_id

UNION

SELECT c.*, o.*
FROM Customer AS c
RIGHT JOIN Orders AS o
ON c.id = o.cust_id;
```

---
