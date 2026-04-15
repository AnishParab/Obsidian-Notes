# Domain Integrity Constraints

- Restricts the **data type** and **valid value range** of an attribute
- Every value inserted must belong to the defined domain

| cust_id | name  | age |
| ------- | ----- | --- |
| 1       | Alice | -5  |

↑ violates domain constraint — age can't be negative. Domain: `INT, age > 0`

---
