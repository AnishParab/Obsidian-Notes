**Refer this example**
[[SQL_RDBMS_MySQL_Example_1]]

---
# Good Practices - `PRIMARY KEY`

```sql
WORKER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT
```

- Use `INT` for fast indexing and searchability
- Use `NOT NULL` since a primary key cannot be empty
- Use `AUTO_INCREMENT` for automatic unique ID generation
- Keep the primary key simple and stable

---
> **NOTE**: An attribute can be `PK` and `FK` *both* in a table.

---
