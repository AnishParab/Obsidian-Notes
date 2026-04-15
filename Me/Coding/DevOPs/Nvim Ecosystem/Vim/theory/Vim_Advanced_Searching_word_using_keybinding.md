# Searching for a word in the text

- Position the cursor on the word and use the `*` command.
- Vim will grab the word under the cursor and use it as the search string.

---
# Searching Backwards

- Use `#`.

---
# `*` / `#` behavior

- `*` → search forward for **whole word** under cursor **(start-of-word marker)**
- `#` → search backward for **whole word** under cursor **(end-of-word marker)**
- `g*` / `g#` → search partial matches (not whole-word only)

---
