# Special Array-Like Objects
- DOM NodeLists, `arguments` object — **not real arrays**, but can be converted:
``` js
Array.from(arguments);
[...document.querySelectorAll("div")];

```

---
