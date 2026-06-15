# Remove Containers

- Removes one or more stopped containers from disk
``` bash
docker rm <container_id or name>
```

---
**Variations**

| Command                      | What it does                                  |
| ---------------------------- | --------------------------------------------- |
| `docker rm <id>`             | Remove one container                          |
| `docker rm <id1> <id2>`      | Remove multiple containers                    |
| `docker rm $(docker ps -aq)` | Remove all stopped containers                 |
| `docker rm -f <id>`          | Force remove a running container (skips stop) |
| `docker rm -v <id>`          | Remove container + its anonymous volumes      |
| `docker rm -fv <id>`         | Force remove + anonymous volumes              |

---
**Related**

| Command                  | What it does                                                      |
| ------------------------ | ----------------------------------------------------------------- |
| `docker rm`              | Remove containers                                                 |
| `docker rmi`             | Remove images                                                     |
| `docker volume rm`       | Remove volumes                                                    |
| `docker system prune`    | Remove all stopped containers + dangling images + unused networks |
| `docker container prune` | Remove all stopped containers only                                |

---
**Gotchas**
- Can't `docker rm` a running container without `-f` — stop it first or use `-f`
- `-v` only removes **anonymous** volumes — named volumes are left untouched
- `docker system prune` is aggressive — it also nukes unused networks and dangling images, not just containers. Add `-a` and it removes all unused images too.

---
