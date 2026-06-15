**Refer this example**
[[SQL_RDBMS_MySQL_Example_1]]

---
# `ON DELETE CASCADE`

- Used with `FOREIGN KEY`
- Automatically deletes child rows when the parent row is deleted
- Maintains referential integrity

**Example**
```sql
FOREIGN KEY (WORKER_REF_ID)
    REFERENCES Worker(WORKER_ID)
    ON DELETE CASCADE
```

**Effect**
- If a worker is deleted from `Worker`
- Related rows in `Bonus` or `Title` are also deleted automatically

---
# `REFERENCES`

- Links a column to the `PRIMARY KEY` of another table
- Creates a relationship between tables

**Meaning**
- `WORKER_REF_ID` refers to `WORKER_ID` in the `Worker` table
- Prevents invalid references

---
