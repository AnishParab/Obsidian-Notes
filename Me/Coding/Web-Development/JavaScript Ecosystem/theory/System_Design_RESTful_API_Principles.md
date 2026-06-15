# Principles of a RESTful API Design
#### 1. HTTP-Based Communication

- All interactions use **HTTP protocol**.
- Resources identified via **URLs**.
- Methods represent actions:
```text
GET → Read
POST → Create
PUT/PATCH → Update
DELETE → Remove
```

---
#### 2. Statelessness

- Server does **not store client session state** in memory.
- Each request contains all required context.
- Persistent data → database, cache store, or token.

**Reason**
- Horizontal scaling
- Server restarts do not break client flow.

---
#### 3. Client–Server Separation

- Client handles UI/UX.
- Server handles business logic + data.
- Communication happens via API calls.

**Goal**
- Independent evolution of frontend and backend.

---
#### 4. Uniform Interface

Consistent resource design:
```text
/users          GET
/users/:id      GET
/users          POST
/users/:id      PATCH
/users/:id      DELETE
```

Rules:
- Use nouns, not verbs.
- Predictable structure.
- Standard HTTP methods.

---
#### 5. Cacheable Responses

- Server responses should define caching behavior.

Examples:
```http
Cache-Control
ETag
Last-Modified
```

Benefits:
- Reduced latency
- Lower server load
- Improved scalability

---
#### 6. Layered System

- Client should not assume direct access to origin server.
- Proxies, gateways, or load balancers may exist.

---
#### 7. Resource-Oriented Design

- API exposes **resources**, not actions.

```text
Correct   → /orders
Incorrect → /createOrder
```

---
#### Core Mental Model

```text
REST = Resource URLs + HTTP Methods + Stateless Requests + Uniform Structure
```

---
