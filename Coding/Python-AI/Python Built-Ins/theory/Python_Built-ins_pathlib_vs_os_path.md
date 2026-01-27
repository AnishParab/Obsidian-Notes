# `os.path`
- Python originally represented filesystem paths as strings.
- Manipulation relied on `os.path` functions layered on top of strings.
#### Issues
- **Lack of structure**
    - A path string carries no semantics (file vs directory, absolute vs relative).
- **OS-dependent behavior**
    - Separator differences (`/` vs `\`) leak into logic.
	- Cannot handle **PosixPath** and **WindowsPath**.
- **Error-prone composition**
    - Manual joins, slicing, suffix handling.
- **Poor abstraction boundary**
    - String operations mixed with filesystem I/O logic.

---
# Why `pathlib`
#### Design goal of `pathlib`

> Provide a **typed, object-oriented, immutable representation** of filesystem paths with a clean separation between:

- path _description_
- filesystem _effects_

---
# Summary

| Aspect           | `os.path`      | `pathlib`           |
| ---------------- | -------------- | ------------------- |
| Data model       | Strings        | Typed objects       |
| Composition      | Function calls | Operators / methods |
| Semantics        | Implicit       | Explicit            |
| Testability      | Lower          | Higher              |
| Modern usage<br> | Legacy         | Preferred           |
|                  |                |                     |

---
