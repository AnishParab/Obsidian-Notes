# Vim Named Marks (`a–z`)

- A **named mark** is a user-defined cursor position stored by Vim and identified by a lowercase letter (`a–z`).

---
# Creating Marks

#### `m{letter}`

- Sets a mark at the **current cursor position**.
- Example:
```
ma
```
- Sets mark `a`.

---
# Jumping to Marks

##### `` `{mark} ``
- Jumps to the **exact cursor position** (line + column).

##### `' {mark}`
- Jumps to the **start of the line** containing the mark.
- Column information is discarded.

---
# Practical Use Pattern

##### Two-Point Navigation
```
ms    " mark start
me    " mark end
's    " jump to start line
''    " jump back
'e    " jump to end line
```

- Common convention: `s` = start, `e` = end (not special, just mnemonic).

---
# Listing Marks

##### `:marks`
- Displays all active marks.
- Includes user-defined and special marks.

---
# Special Marks (Implicit)

- `'` — position before last jump
- `"` — cursor position when file was last edited
- `[` — start of last change
- `]` — end of last change

---
# Common Misconceptions

- Marks are **not visible** in the buffer.
- Marks are **file-local**, not global.
- Lowercase marks differ from uppercase (global) mark

---
