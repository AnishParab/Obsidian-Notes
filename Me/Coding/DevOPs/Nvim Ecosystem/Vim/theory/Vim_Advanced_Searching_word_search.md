# Search Whole Words

### Problem
- `/the` matches `the` **and** `there`

### Word boundary markers
- `\<` → start of word
- `\>` → end of word

---
# Search examples

- Match words ending with `the`:
```vim
/the\>
```

- Match whole word `the` only:
```vim
/\<the\>
```

(does not match `there`, `soothe`)

---
