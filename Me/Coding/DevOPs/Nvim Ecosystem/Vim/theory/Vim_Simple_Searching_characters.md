# Search forward

- `/` → search forward

Example:
```vim
/include
```

### Next / Previous match
- `n` → next occurrence (same direction)
- `N` → previous occurrence (opposite direction)

---
# Search backward

- `?` → search backward

Example:
```vim
?include
```

---
# Ex-command search (jump to Nth match on a line)

```vim
:4/the
```

- Jumps to the **4th** match of `the` in the current line.

---
