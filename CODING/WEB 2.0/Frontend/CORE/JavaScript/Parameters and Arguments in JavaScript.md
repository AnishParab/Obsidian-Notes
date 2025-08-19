# Parameters and Arguments
- Parameters → placeholders in function definition.
- Arguments → actual values passed.
``` js
function add(a, b) {
  return a + b;
}

add(2, 3); // 5
```

---
# Default Parameters
- Provide fallback values.
``` js
function greet(name = "Guest") {
  return `Hello, ${name}`;
}
console.log(greet()); // Hello, Guest
```

---
# Rest Parameters
- Collects multiple arguments into an array.
``` js
function sum(...nums) {
  return nums.reduce((a, b) => a + b, 0);
}
console.log(sum(1, 2, 3, 4)); // 10
```

---

