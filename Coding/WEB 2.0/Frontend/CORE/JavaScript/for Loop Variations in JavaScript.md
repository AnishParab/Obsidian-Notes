# `for...in` Loop
- Iterates over **keys (properties)** of an object.
``` js
const person = { name: "Alex", age: 22 };
for (let key in person) {
  console.log(key, person[key]);
}
// name Alex
// age 22
```

---
# `for...of` Loop
- Iterates over **values** of iterables (arrays, strings, maps, sets).
``` js
const nums = [10, 20, 30];
for (let num of nums) {
  console.log(num);
}
// 10, 20, 30
```

---
# `forEach()`
- `Array.prototype.forEach()`
- `map()`, `filter()`, `reduce()`

> These aren’t "loops" syntactically, but they **replace loops** in functional style.

``` js
const nums = [1, 2, 3];
nums.forEach(n => console.log(n)); // forEach loop
```

---
