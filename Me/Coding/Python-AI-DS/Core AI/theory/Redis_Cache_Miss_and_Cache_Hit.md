# Cache Hit and Miss

- **Cache Hit** — requested data is found in Redis (RAM) → returned immediately, DB not touched
- **Cache Miss** — requested data is NOT in Redis → falls through to the main DB, result then stored in Redis for next time

**Flow:**
```
Request → Redis?
           ├── YES (Hit)  → return data instantly
           └── NO (Miss)  → query DB → store in Redis → return data
```

**Example:**
- User requests product `id=42`
- First request → cache miss → hits PostgreSQL → stores result in Redis
- Every subsequent request → cache hit → never touches PostgreSQL

![[redis2_basics.excalidraw|700]]

**Why it matters:**
- High hit rate = DB is barely touched = system scales massively
- Low hit rate = Redis is just overhead

**Gotcha:**
- **Cache invalidation** — when DB data updates, Redis may still serve stale data
- Most critical (and hardest) problem in caching: _when do you invalidate?_

---
