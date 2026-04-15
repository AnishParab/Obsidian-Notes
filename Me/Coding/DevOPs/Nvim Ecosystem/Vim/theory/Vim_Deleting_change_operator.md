# Change Operator (`c`) — Minimal Notes

```text
c{motion|textobject}
```

- Deletes the range
- Enters **Insert mode**

Equivalent to:
```text
d{motion} + i
```

(except one case below)

---
# Example

```text
c2wbe<Esc>
```

- `c` → change operator
- `2w` → delete two words
- `be` → insert text
- `<Esc>` → Normal mode

---
# Exception (`cw`)

```text
cw == ce   (not c + w)
```

- Does **not** delete trailing space
- Historical Vi behavior
- Only inconsistency in `c` operator

---
# Recommendation

- Prefer text objects for clarity:
    

```text
ciw   " change inner word
caw   " change word + space
```

---
