# `REPLACE INTO`

- Data already present -> then behaves as `REPLACE`
- Data not present -> then behaves as `INSERT`

> Inserts a new row or replaces an existing row if a duplicate `PRIMARY KEY` or `UNIQUE` value exists.

- Existing row is deleted and replaced with the new row.

``` sql
REPLACE INTO Worker (
    WORKER_ID,
    FIRST_NAME,
    SALARY
)
VALUES (
    1,
    'Ankit',
    90000
);
```

---
