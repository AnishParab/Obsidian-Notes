# Replacing

```text
r{char}
```

- Replaces **character under cursor**
- Stays in **Normal mode**
- **Not an operator**

Equivalent effect to `cl` / `s`, but without Insert mode.

---
# Example

```text
rT   rt   rw
```

Each replaces the current character with the given one.

---
# Count Behavior

```text
[count] + r{char}
```

- Replaces **count characters** with the **same character**

Example:

```text
5rx
```

Replaces 5 characters with `x`.

---
# Line Break Replacement

```text
r<Enter>
```

- Deletes one character
- Inserts a **newline**

With count:

```text
4r<Enter>
```

- Deletes 4 characters
- Inserts **one** line break

---
# Key Properties

- No operator–motion grammar
- Count applies only to **characters replaced**
- Always exits immediately (no `<Esc>`)

---
