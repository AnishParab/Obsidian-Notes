# What is Express.js ?

- **Express.js** = minimal web framework for Node.js.
- Provides structured abstraction over the native `http` module.
- Designed for building **HTTP servers and APIs**.

> Mental Model
```
Node.js http module → Low-level primitives
Express.js         → Structured layer on top
```

---
# Why Express Exists

- Native Node.js `http` is low-level:
    - Manual routing
    - Manual header handling
    - Boilerplate request parsing
- Express introduces:
    - Routing system
    - Middleware pipeline
    - Request/Response helpers

---
# Core Concepts

| Concept         | Meaning                        |
| --------------- | ------------------------------ |
| Routing         | Map URL → handler              |
| Middleware      | Functions executed in sequence |
| Request Object  | Incoming HTTP data             |
| Response Object | Outgoing server reply          |

---
# What Express Is NOT

- Not a full framework (no ORM, auth, frontend).
- Not a replacement for Node.js.
- Not required to build servers — only simplifies.

---
# Common Applications

- REST APIs
- Backend services
- Microservices
- Web servers

---
