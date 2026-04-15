# HTTP Methods

- HTTP methods define the **intended action** to be performed on a resource.
- Semantics matter for caching, idempotency, and REST design.

---
# Core Methods

### `GET`

- Retrieve resource.
- **Safe** and **idempotent**.
- No request body (by convention).
- Should not mutate server state.

---
### `POST`

- Create or trigger processing.
- **Not idempotent**.
- Used when server generates resource ID or performs an action.

---
### `PUT`

- Replace entire resource.
- **Idempotent**.
- Same request repeated → same result.

---
### `PATCH`

- Partial update of resource.
- Not strictly idempotent (depends on implementation).

---

### `DELETE`

- Remove resource.
- Usually idempotent (deleting twice → same end state).

---
# Less Common Methods

### `HEAD`

- Same as `GET` but returns headers only.
- Used for metadata checks.

### `OPTIONS`

- Returns supported methods.
- Used in CORS preflight.

---
# Notes

- **Safe** = does not modify server state.
- **Idempotent** = repeated calls produce same final state.
- Misusing POST for updates breaks caching and API semantics.

---
