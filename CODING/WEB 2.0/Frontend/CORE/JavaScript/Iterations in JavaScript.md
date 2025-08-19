# Iteration Methods
``` js
let numbers = [1, 2, 3, 4];

numbers.forEach(n => console.log(n)); // Executes for each element

let doubled = numbers.map(n => n * 2); // [2, 4, 6, 8]

let evens = numbers.filter(n => n % 2 === 0); // [2, 4]

let sum = numbers.reduce((acc, cur) => acc + cur, 0); // 10

numbers.every(n => n > 0); // true
numbers.some(n => n > 3);  // true

```

---
