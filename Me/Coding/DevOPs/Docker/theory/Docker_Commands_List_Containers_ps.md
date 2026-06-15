# List Containers

- Lists containers
``` bash
docker ps
```

---
# Variations

| Flag                                      | What it does                       |
| ----------------------------------------- | ---------------------------------- |
| `docker ps`                               | Running containers only            |
| `docker ps -a`                            | All containers (running + stopped) |
| `docker ps -q`                            | Only container IDs (running)       |
| `docker ps -aq`                           | All container IDs                  |
| `docker ps -s`                            | Show disk size per container       |
| `docker ps -n 3`                          | Last 3 created containers          |
| `docker ps -l`                            | Last created container             |
| `docker ps --no-trunc`                    | Full output, no truncation         |
| `docker ps -f status=exited`              | Filter by status                   |
| `docker ps -f name=myapp`                 | Filter by name                     |
| `docker ps --format "{{.ID}} {{.Names}}"` | Custom output format               |

---
# Useful combos

- Stop all running containers
``` bash
docker stop $(docker ps -q)
```

- Remove all stopped containers
``` bash
docker rm $(docker ps -aq)
```

---
