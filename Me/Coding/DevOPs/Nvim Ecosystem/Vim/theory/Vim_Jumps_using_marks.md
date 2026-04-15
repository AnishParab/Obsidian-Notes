# Vim Jump List Navigation

- Vim maintains a **jump list**: an ordered history of cursor positions created by jump commands.

---
# Navigation Commands

##### `CTRL-O` — Older Position
- Moves **backward** in jump history.

##### `CTRL-I` — Newer Position
- Moves **forward** in jump history.
- Equivalent to `<Tab>`.

---
# Jump History Inspection

##### `:jumps`
- Displays the jump list.
- Most recently used entry is marked with `>`.

---
# Mental Model

- Jump list is **stack-like**, not a single return location.
- toggles between **two most recent positions**.
- `CTRL-O` / `CTRL-I` traverse the **entire history**.

---
# Basic Example

```
33G        " jump to line 33
/^The      " search forward
CTRL-O     " back to line 33
CTRL-O     " back to original position
CTRL-I     " forward to line 33
CTRL-I     " forward to /^The match
```

---
