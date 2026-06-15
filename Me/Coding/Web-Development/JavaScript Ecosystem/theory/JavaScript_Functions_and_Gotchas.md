# JavaScript Functions

**Declaration**
```js
// function declaration — hoisted
function add(a, b) {
  return a + b
}

// function expression — not hoisted
const add = function(a, b) {
  return a + b
}

// arrow function
const add = (a, b) => a + b

// arrow — single param, no parens needed
const double = x => x * 2

// arrow — no params
const greet = () => "hello"
```

---
**Default Parameters**
```js
function greet(name = "Guest") {
  return `Hello ${name}`
}
greet()           // "Hello Guest"
greet("alice")    // "Hello Alice"
```

---
**Rest Parameters**
```js
function sum(...nums) {
  return nums.reduce((acc, n) => acc + n, 0)
}
sum(1, 2, 3, 4)   // 10
```

---
**Arguments object (CJS only)**
```js
function log() {
  console.log(arguments)   // array-like object of all args
}
// not available in arrow functions
```

---
**Spread in function call**
```js
const nums = [1, 2, 3]
console.log(Math.max(...nums))   // 3
```

---
**Higher Order Functions**
```js
// function that takes a function
function apply(fn, value) {
  return fn(value)
}
apply(x => x * 2, 5)   // 10

// function that returns a function
function multiplier(factor) {
  return n => n * factor
}
const triple = multiplier(3)
triple(5)   // 15
```

---
**IIFE (Immediately Invoked Function Expression)**
```js
(function() {
  console.log("runs immediately")
})()

// arrow version
(() => console.log("runs immediately"))()
```

---
**Pure vs Impure**
```js
// pure — same input, same output, no side effects
const add = (a, b) => a + b

// impure — modifies external state
let count = 0
const increment = () => count++
```

---
# Gotchas:

- Arrow functions have no `this`, `arguments`, or `prototype`
- Function declarations are hoisted, expressions are not
- `return` without a value returns `undefined`
- Arrow functions cannot be used as constructors (`new` throws)

---
