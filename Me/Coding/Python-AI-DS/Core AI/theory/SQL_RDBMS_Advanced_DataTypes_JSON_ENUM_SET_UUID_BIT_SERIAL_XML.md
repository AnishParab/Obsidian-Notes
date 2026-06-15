# Advanced Datatypes

#### 1. `JSON`

- Stores structured JSON data
- Useful for semi-structured or dynamic schemas
- Supports JSON querying functions

**Example**
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    profile JSON
);
```

**Insert JSON Data**
```sql
INSERT INTO users VALUES (
    1,
    '{"name": "Ankit", "age": 20}'
);
```

**Access JSON Fields**
```sql
SELECT profile->'$.name' FROM users;
```

---
#### 2. `ENUM`

- Stores one value from a predefined list
- Internally optimized as integers

**Example**
```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    status ENUM('active', 'inactive', 'graduated')
);
```

---
#### 3. `SET`

- Stores multiple values from a predefined list
- Unlike `ENUM`, multiple selections are allowed

**Example**
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    skills SET('python', 'sql', 'java', 'cpp')
);
```

---
#### 4. `UUID`

- Universally unique identifier
- Commonly used in distributed systems

**Example**
```sql
CREATE TABLE users (
    id CHAR(36) PRIMARY KEY
);
```

**Example UUID**
```text
550e8400-e29b-41d4-a716-446655440000
```

---
#### 5. `BIT`

- Stores binary bit values

**Example**
```sql
CREATE TABLE permissions (
    id INT PRIMARY KEY,
    flags BIT(8)
);
```

---
#### 6. `SERIAL`

- Auto-incrementing integer shortcut
- Common in PostgreSQL

Equivalent to:
```sql
BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
```

---
#### 7. `XML`

- Stores XML formatted data
- Supported in some SQL systems

**Example**
```sql
CREATE TABLE documents (
    id INT PRIMARY KEY,
    data XML
);
```

---
