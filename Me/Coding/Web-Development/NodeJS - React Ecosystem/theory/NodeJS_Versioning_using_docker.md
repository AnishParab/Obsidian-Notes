# Purpose

- Isolate Node runtime from host system.
- Pin exact Node version per project.
- Avoid dependency on global `pacman` install.

---
# Steps
## 1) Create `Dockerfile`

```dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

CMD ["node", "index.js"]
```

**Key Ideas**
- `node:20-alpine` → pinned runtime.
- `WORKDIR` → container project root.
- Install deps before copying source for caching.

---
## 2) Build Image

```bash
docker build -t project-name .
```

Effect:
```
Docker Image = Project + Node Runtime
```

---
## 3) Run Container

```bash
docker run --rm project-name
```

Runs using Node version defined in image, not host.

---
## 4) Development Mode (Bind Mount)

```bash
docker run -it --rm \
  -v $(pwd):/app \
  -p 3000:3000 \
  node:20-alpine \
  sh
```

Purpose:
- Live code editing.
- No rebuild required.

---
## 5) Project Structure

```
project/
 ├── Dockerfile
 ├── package.json
 ├── package-lock.json
 └── src/
```

---
## 6) Mental Model

```
Host Node (pacman) → ignored
Docker Image       → defines runtime
Container          → executes project
```

---
