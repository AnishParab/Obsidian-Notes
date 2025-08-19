# What is a Function ?
- A **block of code** that performs a specific task.
- Can be **reused** many times.
- Helps with **modularity** and **clean code**.

---
# `return` Statement
- Ends function execution.
- Sends value back.
- Without `return`, function returns `undefined`.

---
# Function Declaration
- Traditional way of defining functions.

> Hoisted (can be called **before** definition).

``` js
function greet(name) {
  return `Hello, ${name}`;
}

console.log(greet("Alex")); // Hello, Alex
```

---
# Function Expression
- Store function in a variable.

> Not hoisted (must be defined before use).

``` js
const greet = function(name) {
  return `Hello, ${name}`;
};
```

---
# Arrow Functions
- Shorter syntax, commonly used.
- Lexical `this` (does **not** bind its own `this`).
- Great for callbacks.

``` js
const greet = (name) => `Hello, ${name}`;

```

---
