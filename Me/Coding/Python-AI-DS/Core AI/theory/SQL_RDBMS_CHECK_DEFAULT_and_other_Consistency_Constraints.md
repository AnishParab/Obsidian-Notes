# Consistency Constraints

- Rules used to maintain valid and consistent data in a table.

---
# `CHECK`

- Ensures values satisfy a specific condition.

```sql
CREATE TABLE Account (
    BALANCE INT,
    CONSTRAINT ACCOUNT_BALANCE_CHECK
    CHECK (BALANCE > 1000)
);
```

---
# `NOT NULL`

- Prevents `NULL` values in a column.

```sql
NAME VARCHAR(255) NOT NULL
```

---
# `UNIQUE`

- Prevents duplicate values.

```sql
EMAIL VARCHAR(255) UNIQUE
```

---
# `PRIMARY KEY`

- Uniquely identifies each row.

```sql
ID INT PRIMARY KEY
```

---
# `FOREIGN KEY`

- Maintains relationships between tables.

```sql
FOREIGN KEY (WORKER_REF_ID)
REFERENCES Worker(WORKER_ID)
```

---
# `DEFAULT`

- Assigns a default value if none is provided.

```sql
STATUS VARCHAR(20) DEFAULT 'ACTIVE'
```

---
# `AUTO_INCREMENT`

- Automatically generates sequential numeric values.

```sql
ID INT AUTO_INCREMENT
```

---
