# Vim Deleting Shortcuts

```text
x   == dl    " delete char under cursor
X   == dh    " delete char before cursor
D   == d$    " delete to end of line
C   == c$    " change to end of line
s   == cl    " change one character
S   == cc    " change entire line
```

---
# Notes

- `D` and `C` are **inclusive** (`$` motion)
- `S` (`cc`) preserves indentation
- Prefer full forms (`d{motion}`, `c{textobject}`) for composability

---
# Explicit Forms

```text
d$  " delete to end of line
c$  " change to end of line
```

---
