# Docker Containers

- A container is a **runtime instance** of a Docker image
- Adds a thin writable layer on top of the image's read-only layers — all runtime changes go here
- Shares the host kernel — no guest OS overhead
- Multiple containers can run from the same image simultaneously

---
**Isolation**
- Each container gets its own:
    - Filesystem (via image layers + writable layer)
    - Network stack (own IP, ports)
    - Process namespace (can't see host PIDs or other containers)
    - Resource limits (CPU, memory via cgroups)
- Containers don't interfere with each other or the host by default

---
**Ephemeral**
- Containers are temporary by design — writable layer is destroyed on `docker rm`
- Anything written inside the container (logs, DB files, uploads) is lost unless persisted via a **volume**
- Advantage: clean slate every run — no state drift between deployments
- Disadvantage: stateful apps (databases) need explicit volume mounts to survive restarts

---
**Portable**
- Container packages app + all dependencies — behaves identically across dev, staging, prod
- No "works on my machine" — environment is baked into the image the container runs from
- Runs on any host with Docker installed regardless of underlying OS or cloud provider

---
**Gotchas**
- Container stops when PID 1 exits — if your entrypoint process dies, the container dies
- Stopped containers still exist on disk until `docker rm` — use `--rm` flag to auto-clean on exit
- Writable layer is not for storage — it's slow compared to volumes and dies with the container

---
