# Stop Containers

- Gracefully stops a running container (sends `SIGTERM`, then `SIGKILL` after timeout)
``` bash
docker stop <container_id or name>
```

---
# Variations

| Command                       | What it does                            |
| ----------------------------- | --------------------------------------- |
| `docker stop <id>`            | Stop one container                      |
| `docker stop <id1> <id2>`     | Stop multiple containers                |
| `docker stop $(docker ps -q)` | Stop all running containers             |
| `docker stop -t 5 <id>`       | Wait 5s before SIGKILL (default is 10s) |
| `docker stop -t 0 <id>`       | Immediate SIGKILL, no grace period      |

---
# Related commands

| Command          | Difference                                       |
| ---------------- | ------------------------------------------------ |
| `docker stop`    | SIGTERM → waits → SIGKILL. Clean shutdown.       |
| `docker kill`    | SIGKILL immediately. No grace period.            |
| `docker pause`   | Freezes the container (SIGSTOP), doesn't stop it |
| `docker restart` | stop + start in one command                      |

---
**Gotchas**
- `docker stop` gives the process a chance to handle shutdown (flush buffers, close DB connections) — prefer it over `docker kill`
- If the app ignores `SIGTERM`, it will just hang until the timeout then get killed anyway — tune `-t` accordingly
- Stopped containers still exist on disk — use `docker rm` to remove them

---
