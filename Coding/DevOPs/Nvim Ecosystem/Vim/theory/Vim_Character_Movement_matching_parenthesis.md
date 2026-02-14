# Jump to matching pair

- `%` → jump to matching bracket/paren

Works for:
- `()` parentheses
- `[]` brackets
- `{}` braces

---
# Behavior

- If cursor is on `(` → jumps to matching `)`
- If cursor is on `)` → jumps to matching `(`
- If cursor is **not** on a pair character, `%` searches forward for the next one, then jumps to its match.

---
# Help / Config

- Matching pairs are controlled by:

```vim
:help 'matchpairs'
```

---

