# Vim Search Patterns — Simple Regex

- Vim search uses **regular expressions** to describe text patterns.  

---
# Line Anchors

##### `^` — Beginning of Line
- Matches only at column 0.
- `^include` → matches `include` **only if it starts the line**.

##### `$` — End of Line
- Matches only at line end.
- `was$` → matches `was` **only if it ends the line**.

##### Combined
- `^the$` → matches a line consisting **exactly** of `the`.
- Whitespace is significant:
    - `the` ≠ `the`

---
# Any Single Character

##### `.` — Dot
- Matches **any single existing character** (except newline).
- `c.m` → matches `c` + any char + `m`
    - Examples: `cam`, `c9m`, `c_m`

---
# Literal vs Special Characters

##### Escaping Special Characters
- Special characters have meaning in regex.
- To match them literally, **escape with `\`**.

##### Example
- `ter.` → matches `ter` + any character
- `ter\.` → matches literal `ter.` only

---
