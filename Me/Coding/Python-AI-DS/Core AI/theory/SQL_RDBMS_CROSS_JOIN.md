# `CROSS JOIN`

- Returns all possible row combinations from both tables.

**Example**
- `Table_1` → 5 rows
- `Table_2` → 10 rows
- Result → `5 × 10 = 50` rows

```sql
SELECT *
FROM Table_1
CROSS JOIN Table_2;
```

> Produces the Cartesian product of both tables.

> Rarely used in production.

---
