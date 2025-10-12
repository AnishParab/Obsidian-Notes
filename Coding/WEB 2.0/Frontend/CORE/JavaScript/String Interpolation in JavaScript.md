# What ?
- **String interpolation** in JavaScript means embedding variables or expressions directly into a string, usually using **template literals** (backticks `` ` ``) instead of quotes.

---
# Syntax
``` js
let name = "Alex";
let age = 25;

console.log(`My name is ${name} and I am ${age} years old.`);
// Output: My name is Alex and I am 25 years old.
```

---
# Use-Case in  Expressions
``` js
let a = 5, b = 3;
console.log(`Sum: ${a + b}`);
// Output: Sum: 8
```

---
# Use-Case in Functions
``` js
function greet(user) {
  return `Hello, ${user}!`;
}

console.log(`${greet("Alex")}, welcome!`);
// Output: Hello, Alex!, welcome!
```

---
# Multi-Line Support
``` js
let multiLine = `
This is line one.
This is line two.
`;
console.log(multiLine);
```

---
