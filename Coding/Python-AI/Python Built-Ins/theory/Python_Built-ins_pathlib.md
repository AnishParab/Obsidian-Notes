# `pathlib`
- **`pathlib`** is a **standard library module** that defines classes representing filesystem paths and exposes path-related operations as **methods on those objects**.

Key definition:
> A `Path` object represents a **location in a filesystem namespace**, not the file itself.

---
# Value-object model
- `Path` is a **pure value object**
- It can represent:
    - existing paths
    - non-existing paths
    - future paths

Creating a `Path`:
``` python
from pathlib import Path
p = Path("data/file.txt")
```

This does **not**:
- check existence
- open files
- touch disk

---
