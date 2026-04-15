# Key Constraints

- PK must be **unique** and **not NULL**
- CK must also be unique and not NULL
- Ensures no two tuples are identical on key attributes

| cust_id | name  |
| ------- | ----- |
| 1       | Alice |
| 1       | Bob   |

↑ violates key constraint — duplicate `cust_id`

---
