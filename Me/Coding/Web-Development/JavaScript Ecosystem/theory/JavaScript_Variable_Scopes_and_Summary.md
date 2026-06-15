# Variable Scopes

> 3 types of scope: global, function, block.

**Scope Summary**

|                | `var`           | `let`     | `const`   |
| -------------- | --------------- | --------- | --------- |
| Global scope   | Yes             | Yes       | Yes       |
| Function scope | Yes             | Yes       | Yes       |
| Block scope    | No              | Yes       | Yes       |
| Hoisted        | Yes (undefined) | Yes (TDZ) | Yes (TDZ) |

---
**Global Scope**
- Declared outside any function or block
- Accessible everywhere

```js
const name = "alice"

function greet() {
  console.log(name)   // accessible
}
```

---
**Function Scope**
- Variables declared inside a function — not accessible outside

```js
function greet() {
  const message = "hello"
  console.log(message)   // works
}
console.log(message)     // ReferenceError
```

---
**Block Scope**
- `let` and `const` are scoped to the nearest `{}`
- `var` ignores block scope — leaks out

```js
if (true) {
  let x = 10
  var y = 20
}
console.log(x)   // ReferenceError — block scoped
console.log(y)   // 20 — var leaks out
```

---
**Lexical Scope (Scope Chain)**
- Inner functions can access outer variables, not vice versa

```js
function outer() {
  const x = 10

  function inner() {
    console.log(x)   // 10 — can access outer scope
  }

  inner()
}
```

> JS walks up the scope chain until it finds the variable or hits global

---
**Closure**
- Function retains access to its outer scope even after outer function returns

```js
function counter() {
  let count = 0
  return function() {
    count++
    console.log(count)
  }
}

const increment = counter()
increment()   // 1
increment()   // 2
increment()   // 3
// count is preserved across calls
```

---
