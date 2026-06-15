# Remove Images

- Removes one or more images from local storage
``` bash
docker rmi <image_id or name:tag>
```
- or
``` bash
docker image rm <image_id or name:tag>
```

---
# Variations

| Command                             | What it does                                   |
| ----------------------------------- | ---------------------------------------------- |
| `docker rmi <id>`                   | Remove one image                               |
| `docker rmi <id1> <id2>`            | Remove multiple images                         |
| `docker rmi -f <id>`                | Force remove even if a container references it |
| `docker rmi $(docker images -q)`    | Remove all images                              |
| `docker rmi -f $(docker images -q)` | Force remove all images                        |
| `docker image prune`                | Remove all dangling images                     |
| `docker image prune -a`             | Remove all unused images (not just dangling)   |

---
**Gotchas**
- Can't remove an image if a container (even stopped) is using it — `docker rm` the container first, or use `-f`
- `-f` doesn't actually delete the image if a running container uses it — it just untags it. The layers stay until the container is gone.
- `docker image prune -a` removes **all** images not referenced by any container — including ones you might want to keep. Be deliberate.
- Shared layers between images are not duplicated on disk — removing one image doesn't free as much space as `SIZE` suggests if layers are shared

---
