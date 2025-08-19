# `.length`
``` js
let arr = [1, 2, 3];
console.log(arr.length); // 3

arr.length = 1; // Truncates array → [1]

```

---
# Sparse Arrays
``` js
let arr = [];
arr[5] = 42;
console.log(arr.length); // 6
console.log(arr); // [empty × 5, 42]
```

> **Avoid sparse arrays** — they break engine optimizations.

---
