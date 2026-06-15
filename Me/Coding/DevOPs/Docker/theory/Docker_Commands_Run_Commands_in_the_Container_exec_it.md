# Run Commands in the Container

- Opens an interactive shell inside a running container
``` bash
docker exec -it <container_id or name> <command>
```

---
# Flags

| Flag  | Meaning                                   |
| ----- | ----------------------------------------- |
| `-i`  | Keep stdin open (interactive)             |
| `-t`  | Allocate a pseudo-TTY (terminal emulator) |
| `-it` | Both — needed together for a usable shell |

---
# Common usage

| Command                                  | What it does                                |
| ---------------------------------------- | ------------------------------------------- |
| `docker exec -it <id> bash`              | Open bash shell inside container            |
| `docker exec -it <id> sh`                | Open sh (for Alpine-based images — no bash) |
| `docker exec -it <id> python3`           | Drop into Python REPL inside container      |
| `docker exec -it <id> mysql -u root -p`  | Open MySQL CLI inside container             |
| `docker exec -d <id> <cmd>`              | Run command in background inside container  |
| `docker exec -it -e VAR=value <id> bash` | Inject env variable for the session         |
| `docker exec -it -u root <id> bash`      | Enter as root regardless of container user  |

---
**Gotchas**
- Container must be **running** — `exec` doesn't start stopped containers. Use `docker start <id>` first.
- `bash` may not exist in minimal images (Alpine uses `sh` by default) — try `sh` if `bash` fails
- Changes made inside `exec` shell are to the **running container's writable layer** — they're lost when the container is removed unless committed or mounted via a volume
- `exec` spawns a **new process** inside the container — it doesn't attach to PID 1. Exiting the shell doesn't stop the container.

---
