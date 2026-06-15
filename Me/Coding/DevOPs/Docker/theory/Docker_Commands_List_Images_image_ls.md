# List Images

- Lists all locally available images
``` bash
docker images
```
- or
``` bash
docker image ls
```

---
# Variations

| Command                                                       | What it does                                  |
| ------------------------------------------------------------- | --------------------------------------------- |
| `docker images`                                               | List all local images                         |
| `docker images -a`                                            | Include intermediate (dangling) layers        |
| `docker images -q`                                            | Image IDs only                                |
| `docker images --no-trunc`                                    | Full image ID, no truncation                  |
| `docker images -f dangling=true`                              | Only dangling images (untagged, unreferenced) |
| `docker images -f reference=ubuntu`                           | Filter by image name                          |
| `docker images --format "{{.Repository}} {{.Tag}} {{.Size}}"` | Custom output                                 |

---
# Output columns

| Column       | Meaning                           |
| ------------ | --------------------------------- |
| `REPOSITORY` | Image name                        |
| `TAG`        | Version label (default: `latest`) |
| `IMAGE ID`   | Unique hash (truncated)           |
| `CREATED`    | When the image was built          |
| `SIZE`       | Uncompressed size on disk         |

---
**Gotchas**
- `latest` tag is just a convention — it doesn't guarantee it's actually the newest version. Always check.
- Dangling images (`<none>:<none>`) are leftover layers from rebuilds — they waste disk, clean with `docker image prune`
- `SIZE` shown is uncompressed — actual pull size from registry is smaller due to compression and shared layers

---
