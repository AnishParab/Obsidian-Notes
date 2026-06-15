# Dockerfile

- A Dockerfile is a script of instructions to build a Docker image
- Each instruction = a new layer stacked on top of the previous

---
**Step 1 — App setup**
- Create your app (e.g. `npm create vite@latest`)
- Write your source files as normal

**Step 2 — React + nginx mental model**
- In production: React build is served via nginx — user never hits Node directly
- nginx acts as the proxy/web server; user always interacts with nginx
- In dev (this example): we skip nginx, serve via Vite's dev server instead
![[docker_react_nginx.excalidraw|200]]

**Step 3 — `Dockerfile`**
``` text
FROM node:22-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev"]
```

**Step 4 — Build image**
``` bash
docker build -t vite-test .
```

**Step 5 — Run container**
``` bash
docker run -p 5173:5173 vite-test
```
- `-p 5173:5173` maps host port → container port
- Vite binds to `localhost` by default → unreachable from outside the container

**Step 6 — Fix: expose Vite to all interfaces**
- Edit `vite.config.js`:
```js
export default defineConfig({
  server: {
    host: "0.0.0.0",
    port: 5173,
  },
})
```
- `0.0.0.0` = listen on all network interfaces, not just localhost

**Step 7 — Rebuild (images are immutable)**
- Config change → must rebuild the image
- Tag as version 2 (or overwrite — Docker reuses cached layers where possible):
``` bash
docker build -t vite-test:2 .
```

**Step 8 — Run updated image**
```
docker run -p 5173:5173 vite-test:2
```

---
# Potential Optimizations

![[Pasted image 20260517144431.png]]
- Key insight from the visual: `COPY package*.json` + `RUN npm install` are intentionally split from `COPY . .` — so that `node_modules` layer gets cached and doesn't reinstall on every source file change. Changing `App.jsx` only invalidates Layer 5 onwards, not the heavy Layer 4. This is the first optimization pattern you'll hit in the next (optimized) version.

---
