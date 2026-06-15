# Node.js Docker Runtime

- Isolate Node runtime from host, pin exact version per project

```dockerfile
FROM node:20-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install        # cached layer — only reruns if package.json changes
COPY . .

CMD ["node", "index.js"]
```

```bash
docker build -t project-name .
docker run --rm project-name
```

**Mental model**:
```
Host Node (pacman/mise) → ignored
Docker Image            → defines runtime
Container               → executes project
```

**Dev mode with live reload (bind mount)**:
```bash
docker run -it --rm \
  -v $(pwd):/app \
  -p 3000:3000 \
  node:20-alpine sh
```

- `-v` mounts current dir into container — edit locally, runs in container
- No rebuild needed on code changes

---
