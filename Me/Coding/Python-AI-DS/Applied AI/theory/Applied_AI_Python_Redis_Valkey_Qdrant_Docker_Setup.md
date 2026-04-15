# Two Options
- **Redis** - Their open-source license was revoked.
- **Valkey** - _Drop-in replacement_ for Redis which means anything you write will be compatible with _Redis_.

---
# Valkey Setup
- Since it is an RAG, you also need a vector dB setup such as **qdrant**.
`docker-compose.yml`
``` yaml
services:
  qdrant:
    image: qdrant/qdrant
    ports:
      - 6333:6333

  valkey:
    image: valkey/valkey
    ports:
      - 6379:6379
```

---
