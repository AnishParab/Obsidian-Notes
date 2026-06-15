# Key Value Store

- Redis stores all data as **key-value pairs**
- Key = unique string identifier
- Value = the actual data (can be multiple data types)

**Basic syntax:**
```
SET <key> <value>
GET <key>
DEL <key>
```

**Example:**
```
SET user:1:name "Alice"
GET user:1:name  -- returns "Alice"
```

**Key naming convention:**
- Use `:` as separator for namespacing
- `user:1:name`, `otp:user123`, `session:abc123`
- Keeps keys organized and collision-free

**Value data types:**
- `String` — plain text, numbers, serialized JSON
- `List` — ordered list of strings (job queues)
- `Set` — unordered unique strings
- `Sorted Set` — set with scores (leaderboards)
- `Hash` — field-value pairs inside one key (user object)

![[redis_value_storing.excalidraw|700]]

**Gotcha:**
- Keys are case-sensitive — `User:1` ≠ `user:1`
- No nested keys — Redis is flat; nesting is simulated via naming convention (`user:1:address:city`)

---
