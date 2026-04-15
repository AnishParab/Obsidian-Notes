# Properties of Table

- **Distinct relation name** — no two tables can have the same name in a schema
- **Atomic cell values** — each value is indivisible

| cust_id | name  | phone                  |
| ------- | ----- | ---------------------- |
| 1       | Alice | 9876543210, 9123456789 |

↑ violates atomicity — phone has multiple values. Fix: separate table or separate columns.

- **Unique attribute names** — two columns in the same table can't share a name
- **No duplicate tuples** — no two rows can be identical across all attributes
- **No order significance** — row 1 vs row 5 means nothing; column order means nothing

---
