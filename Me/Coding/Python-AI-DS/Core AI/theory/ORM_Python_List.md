# ORM Python Ecosystem

**Relational (SQL)**

| ORM          | Notes                                              |
| ------------ | -------------------------------------------------- |
| SQLAlchemy   | Most powerful, Core + ORM modes, industry standard |
| Django ORM   | Django-only, not standalone                        |
| SQLModel     | SQLAlchemy + Pydantic, FastAPI-friendly            |
| Peewee       | Lightweight, simple syntax                         |
| Tortoise ORM | Async, FastAPI-friendly                            |

---
**Document (MongoDB)**

| ODM         | Notes                                   |
| ----------- | --------------------------------------- |
| MongoEngine | ORM-style, mature                       |
| Beanie      | Async, Pydantic-based, FastAPI-friendly |
| Motor       | Async MongoDB driver, low-level         |

---
**Redis**

| ODM      | Notes                      |
| -------- | -------------------------- |
| Redis-OM | Object mapping for Redis   |
| redis-py | Official client, low-level |

---
**Other**

| ORM               | DB            | Notes                    |
| ----------------- | ------------- | ------------------------ |
| Cassandra Driver  | Cassandra     | Official, no ORM layer   |
| Elasticsearch-DSL | Elasticsearch | Query builder + ORM-like |

---
