# Detached Mode

- Runs a container in the background — terminal is freed immediately, container keeps running
``` bash
docker run -d <image>
```

---
# Variations

| Command                              | What it does                               |
| ------------------------------------ | ------------------------------------------ |
| `docker run -d <image>`              | Run container in background                |
| `docker run -d --name myapp <image>` | Run detached with a name                   |
| `docker run -d -p 8080:80 <image>`   | Detached + port mapping                    |
| `docker attach <id>`                 | Re-attach terminal to a detached container |
| `docker logs <id>`                   | View stdout of detached container          |
| `docker logs -f <id>`                | Follow logs in real time (like `tail -f`)  |
| `docker logs --tail 50 <id>`         | Last 50 lines of logs                      |
| `docker logs --since 10m <id>`       | Logs from last 10 minutes                  |

---
# Foreground vs Detached

|                | Foreground (default) | Detached `-d`                      |
| -------------- | -------------------- | ---------------------------------- |
| Terminal       | Blocked              | Freed                              |
| Stdout         | Printed live         | Captured, view via `docker logs`   |
| Stop on Ctrl+C | Yes                  | No                                 |
| Use case       | Debugging            | Production / long-running services |

---
**Gotchas**
- `docker attach` attaches to the container's PID 1 stdin/stdout — `Ctrl+C` here will **stop** the container, not just detach. Use `Ctrl+P Ctrl+Q` to detach safely.
- If the container exits immediately in detached mode, `docker logs <id>` is your only window into what went wrong
- `-d` and `--rm` can be combined — container cleans itself up after it stops: `docker run -d --rm <image>`

---
