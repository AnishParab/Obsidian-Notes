# Vector DataBase
- **PineCone** - Hosted Managed Service
- **WeaviateDB** - OpenSource
- **ChromaDB** - OpenSource
- **pgvector** - OpenSource
- **QdrantDB** - OpenSource and Lightweight _(Pronounced as Quadrant)_

---
# QdrantDB Local Docker Setup
- Create `docker-compose.yml`
``` yaml
services:
  vector-db:
    image: qdrant/qdrant
    ports:
      - 6333:6333
```

- Now write the command:
``` bash
docker compose up
```

- Now run it in detached mode:
``` bash
docker compose up -d
```

- Check if the docker container is running:
``` bash
docker ps -a
```

---
