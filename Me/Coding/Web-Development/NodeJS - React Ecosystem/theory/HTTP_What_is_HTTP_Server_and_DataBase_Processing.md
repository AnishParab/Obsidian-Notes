# HTTP

- **HTTP — HyperText Transfer Protocol**
- Stateless request–response communication model.

```
Client
   │
   │  HTTP Request
   ▼
Server
   │
   │  HTTP Response
   ▼
Client
```

---
# Database Processing (Typical Backend Flow)

## Steps

- **Authenticate** → verify identity.
- **Authorize** → check permissions.
- **Validate** → verify input correctness before DB use.

---
# Request Processing Diagram

```
Client
   │
   │ Request
   ▼
HTTP Server
   │
   ├─ Authenticate
   ├─ Authorize
   ├─ Validate
   │
   ▼
Database
   │
   ▼
HTTP Response → Client
```

---
