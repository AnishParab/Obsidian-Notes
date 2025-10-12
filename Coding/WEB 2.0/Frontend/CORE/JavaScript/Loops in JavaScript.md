# Why use loops?
- To **repeat a block of code** multiple times.
- Helps avoid code duplication.

---
# `for` Loop
- Used when you know how many times to run.
``` js
for (let i = 0; i < 5; i++) {
  console.log(i); // 0,1,2,3,4
}
```
- `for (initialization; condition; increment/decrement) { ... }`

---
# `while` Loop
- Used when the number of iterations is **unknown**.
- Runs **as long as condition is true**.
``` js
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
```

---
# `do...while` Loop
- Similar to `while`, but **executes at least once** (condition checked later).
``` js
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 5);
```

---
