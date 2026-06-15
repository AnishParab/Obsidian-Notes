# Unary Relations

- A table related to itself.

![[sql_er_unary_relations.excalidraw|300]]

---
# SELF JOIN

- Emulated using `INNER JOIN` and `AS`

``` sql
SELECT e1.id, e1.name, e2.name AS manager
FROM Employee AS e1
INNER JOIN Employee AS e2
ON e1.manager_id = e2.id;
```

---
# Explanation

Example:
- An employee is managed by another employee.
- Both are stored in the same `Employee` table.

Example table:

| id  | name  | manager_id |
| --- | ----- | ---------- |
| 1   | Ankit | NULL       |
| 2   | Rahul | 1          |

Meaning:
- `Rahul` is managed by `Ankit`
So:
```sql
e1 -> employee
e2 -> manager
```

The join:
```sql
ON e1.manager_id = e2.id
```
matches an employee to their manager.

---
