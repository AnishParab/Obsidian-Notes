# Referential Integrity Constraints

| cust_id | name  |
| ------- | ----- |
| 1       | Alice |
| 2       | Bob   |

↑ **Customer** (Parent) — PK: `cust_id`

| order_id | cust_id |
| -------- | ------- |
| 101      | 1       |
| 102      | 2       |

↑ **Order** (Child) — FK: `cust_id`

---
## Insert Constraint

- You cannot insert a child row with a FK value that doesn't exist in parent

```
INSERT INTO Order VALUES (103, 99);  -- REJECTED
```

↑ `cust_id = 99` doesn't exist in Customer — violates referential integrity

---
## Delete Constraint

- You cannot delete a parent row if a child row is still referencing it

```
DELETE FROM Customer WHERE cust_id = 1;  -- REJECTED by default
```

↑ Order 101 still references `cust_id = 1` — DB blocks the delete

---
### 3 ways to handle this:

##### **ON DELETE CASCADE**
- Deleting parent automatically deletes all referencing child rows
- `DELETE Customer(cust_id=1)` → Order 101 also gets deleted automatically
- Use when child rows are meaningless without the parent (orders without a customer)

##### **ON DELETE SET NULL**
- Deleting parent sets FK in child rows to NULL
- `DELETE Customer(cust_id=1)` → Order 101's `cust_id` becomes NULL

| order_id | cust_id |
| -------- | ------- |
| 101      | NULL    |
| 102      | 2       |

- FK **can** be NULL — it means "no parent assigned"
- Use when child record should be preserved even after parent is gone (e.g. anonymous orders)

##### **ON DELETE RESTRICT / NO ACTION**

- Default behavior — blocks the delete entirely if any child references it

---
