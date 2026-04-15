# Word Movement (Vim)

### Basic word motions
- `w` → forward to **start of next word**
- `b` → backward to **start of previous word**
- `e` → forward to **end of current/next word**
- `ge` → backward to **end of previous word**

### Counts
Prefix a number to repeat the motion:
- `3w` → move forward 3 words
- `2b` → move backward 2 words
- `2e` → move forward to end of 2nd word
- `2ge` → move backward to end of 2nd previous word

---
# Notes / Behavior

- If cursor is already at the start of a word, `w` goes to the **start of the next word** (not the same word).
- `w` can cross lines: at end of line, it moves to the first word of the next line.
- Word boundaries include punctuation (`.`, `-`, `)`, etc.).
- Word definition can be changed via:
```vim
:help 'iskeyword'
```

Reset keyword behavior for standard examples:
```vim
:set iskeyword&
```

---
# WORD motions (whitespace-separated)

Uppercase motions treat **whitespace-separated chunks** as units (punctuation included).
- `W` → forward to start of next WORD
- `B` → backward to start of previous WORD
- `E` → forward to end of WORD
- `gE` → backward to end of WORD

---
