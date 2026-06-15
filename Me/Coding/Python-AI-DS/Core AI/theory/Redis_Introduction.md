# Redis Introduction

- **Redis** = Remote Dictionary Server
- *In-memory data store* — data lives in RAM, not on disk
- RAM access vs disk access = orders of magnitude faster
- Used as: cache, message broker, session store, leaderboard backend

**Why in-memory matters:**
- Disk I/O is the bottleneck in traditional DBs
- Redis eliminates that — reads/writes happen at memory speed (~100k–1M ops/sec)

**Gotcha:**
- RAM is volatile — if Redis crashes without persistence configured, data is lost
- Redis has optional persistence (RDB snapshots, AOF logging) but that's a tradeoff

![[redis_basics.excalidraw|700]]

---
---

- Reduce Read Pressure
- Store Temp data which expires
- Shared counter - Likes, page views, etc
- Handle background jobs like queues -> notifications, email, report generation

---
# Stuff like Redis

- Redis
- KeyDB - drop in alternative to redis
- dragonflydb
- Valkey
- memcached
- upstash - Only a platform for Redis, QStash, Vector etc.

---
