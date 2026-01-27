# `Path`

```python
from pathlib import Path

p = Path("data/audio.wav")
```

**What happens internally**
- Stores path components as structured parts
- Normalizes separators for the current OS
- Does **not** touch the filesystem

**What does NOT happen**
- No stat call
- No existence check
- No permission check

This is intentional. `Path` is a _descriptor_, not an accessor.

---
# Path composition (core operation)
```python
base = Path("data")
p = base / "raw" / "input.wav"
```

### Why `/` works
- `Path.__truediv__` is overloaded
- Returns a **new Path**
- Enforces correct separator rules

Equivalent, but less readable:
```python
Path("data", "raw", "input.wav")
```

### Failure mode
```python
Path("/abs") / "/other"
```

Result:

```python
Path("/other")
```

Reason:

- Absolute paths discard the left operand
    
- This is by design, not a bug
    

---

## 3. Relative vs absolute paths

```python
Path("a/b").is_absolute()     # False
Path("/a/b").is_absolute()   # True
```

Conversion:

```python
p = Path("a/b")
p.absolute()   # cwd + "a/b" (no resolution)
p.resolve()    # resolves symlinks, may fail
```

### Failure mode of `resolve()`

- Raises if parent directories do not exist
    
- Unsafe for speculative paths
    

---

## 4. Structural introspection (zero I/O)

```python
p = Path("/home/asp/audio.wav")

p.name        # audio.wav
p.stem        # audio
p.suffix      # .wav
p.suffixes    # ['.wav']
p.parent      # /home/asp
p.parents     # iterable of ancestors
```

These are **pure transformations**.

---

## 5. Filesystem boundary: existence & type

```python
p.exists()
p.is_file()
p.is_dir()
```

### Critical misconception

> `exists()` makes future operations safe

False.

```python
if p.exists():
    p.read_text()   # can still fail
```

Reason:

- TOCTOU race (time-of-check vs time-of-use)
    

Correct model:

- Treat filesystem as adversarial
    
- Handle exceptions
    

---

## 6. Reading and writing files

### Text

```python
p.write_text("hello", encoding="utf-8")
data = p.read_text(encoding="utf-8")
```

### Binary

```python
p.write_bytes(b"\x00\x01")
data = p.read_bytes()
```

### Failure modes

- Missing parent directories
    
- Permission denied
    
- Partial writes (on crash)
    

---

## 7. Directory creation

```python
Path("data/raw").mkdir(parents=True, exist_ok=True)
```

Parameters:

- `parents=True` → create intermediate dirs
    
- `exist_ok=True` → suppress error if exists
    

Failure mode:

- Race conditions under concurrency
    

---

## 8. Directory traversal

```python
for p in Path("data").iterdir():
    print(p)
```

### Pattern matching

```python
Path("data").glob("*.wav")
Path("data").rglob("*.wav")
```

Returns:

- Lazy iterators of `Path` objects
    

Failure mode:

- Symlink loops in `rglob`
    

---

## 9. Renaming and moving

```python
p.rename("new.wav")
p.replace("new.wav")
```

Difference:

- `rename()` may fail across filesystems
    
- `replace()` overwrites if target exists
    

Use `replace()` for atomic updates when possible.

---

## 10. Deletion

```python
p.unlink()   # file
p.rmdir()    # empty directory
```

Failure mode:

- `rmdir()` fails if directory not empty
    

---

## 11. Permissions and metadata

```python
stat = p.stat()
stat.st_size
stat.st_mtime
```

This is a direct syscall boundary.

---

## 12. Interop with legacy APIs

```python
open(Path("file.txt"))
os.listdir(Path("."))
```

Convert only when forced:

```python
str(p)
```

---

## 13. Secure path handling (important)

### Directory traversal defense

```python
base = Path("/safe/root")
candidate = (base / user_input).resolve()

if not candidate.is_relative_to(base):
    raise SecurityError
```

Prevents:

```
../../etc/passwd
```

---

## 14. Path lifecycle pattern (recommended)

```python
out = Path("out/data.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("payload")
```

Clear phases:

1. Describe path
    
2. Ensure container exists
    
3. Perform I/O
    
4. Handle failure
    

---

## 15. When `Path` is the wrong tool

- URLs → `urllib`
    
- In-memory file abstractions
    
- Virtual FS layers
    
- High-frequency hot loops
    

---

## 16. Stable summary

- `Path` is **pure until I/O**
    
- Composition is explicit and safe
    
- Filesystem state is unreliable
    
- Exceptions are the correctness mechanism
    

---

### Next step (recommended)

- Atomic writes with temp files
    
- `Path` in ML / DSP pipelines
    
- Testing filesystem code with `tmp_path` (pytest)
    

Say which one to proceed with.