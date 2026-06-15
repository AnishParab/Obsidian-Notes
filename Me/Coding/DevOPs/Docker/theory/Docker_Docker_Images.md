# Docker Images

- A Docker image is a read-only, standalone, executable package containing everything needed to run an app:
    - Application code
    - Runtime (Python, Node, JVM, etc.)
    - Libraries and dependencies
    - Environment variables
    - Config files
- Images are **templates** — containers are running instances of images
- Stored locally via `docker pull` or built via `Dockerfile`

---
**Layered architecture**
- Images are built layer by layer — each instruction in a `Dockerfile` adds a new layer
- Layers are cached — unchanged layers are reused on rebuild (faster builds)
- Layers are shared across images — if two images share a base (`ubuntu`), that layer is stored once on disk
- Final image = stacked, read-only layers merged via union filesystem

---
**Immutability**
- Once built, an image layer cannot be changed
- Advantage: guaranteed consistency — same image behaves identically everywhere
- Disadvantage: stateful data (databases, uploads) cannot live inside an image — it's lost when the container is removed
- Solution: **volumes** — mount external storage into the container for persistent data

---
**Portability**
- An image built on your Arch machine runs on any Linux host, any cloud provider, any CI runner
- The registry (Docker Hub, GHCR, ECR) is the distribution mechanism — push once, pull anywhere

---
**Gotchas**
- Every `RUN`, `COPY`, `ADD` in a Dockerfile = a new layer — unnecessary layers bloat image size
- A container adds a thin writable layer on top of the image — writes go there, not into the image itself
- `docker commit` can snapshot a container into an image, but it's bad practice — use `Dockerfile` instead for reproducibility

---
