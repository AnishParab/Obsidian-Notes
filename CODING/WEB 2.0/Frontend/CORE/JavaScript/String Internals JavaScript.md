> JS strings are **UTF-16 encoded**.

- `.length` counts UTF-16 code units, not actual characters for emojis or some symbols:

---
# Example
``` js
'😀'.length // 2 (because surrogate pairs)

```

- Instead Use :
``` js
[... '😀'].length // 1 (spread into array of graphemes)

```

---

---
