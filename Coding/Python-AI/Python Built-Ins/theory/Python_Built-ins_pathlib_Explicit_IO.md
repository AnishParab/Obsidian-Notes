# Filesystem boundary (explicit I/O)
- Methods that **touch disk**:
``` python
p.exists()
p.is_file()
p.is_dir()
p.iterdir()
p.read_text()
p.write_bytes()
```

Key principle:
> Filesystem state can change between calls.

Failure mode:
``` python
if p.exists():
    p.read_text()   # can still fail
```

Correct reasoning:
- Existence checks are advisory, not guarantees.

---
