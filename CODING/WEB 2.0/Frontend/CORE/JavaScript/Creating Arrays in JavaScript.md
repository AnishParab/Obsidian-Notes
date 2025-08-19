# Preferred Syntax
``` js
let arr = [10, 20, 30];

```

---
# Array Constructor
``` js
let arr = new Array(10, 20, 30); // [10, 20, 30]
let emptyArr = new Array(5);     // Creates an array with length 5, all empty slots
```

- `Array.of()`
``` js
let arr = Array.of(5); // [5] — avoids the constructor ambiguity

```

- `Array.from()`
``` js
let arr = Array.from("hello"); // ['h', 'e', 'l', 'l', 'o']

```

---
