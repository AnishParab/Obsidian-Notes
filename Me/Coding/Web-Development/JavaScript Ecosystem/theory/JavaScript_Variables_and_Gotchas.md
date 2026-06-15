# JavaScript Variables

- `var`, `let`, `const`

---
**Redeclaration**
``` js
var x = 1
var x = 2      // fine

let y = 1
let y = 2      // SyntaxError

const z = 1
const z = 2    // SyntaxError
```

---
**Reassignment**
``` js
var x = 1
x = 2          // fine

let y = 1
y = 2          // fine

const z = 1
z = 2          // TypeError
```

---
**Block Scope**
``` js
if (true) {
  var a = 1
  let b = 2
  const c = 3
}
console.log(a)   // 1 — leaks out
console.log(b)   // ReferenceError
console.log(c)   // ReferenceError
```

---
**Hoisting**
``` js
console.log(a)   // undefined — hoisted, initialized as undefined
var a = 5

console.log(b)   // ReferenceError — TDZ
let b = 5

console.log(c)   // ReferenceError — TDZ
const c = 5
```

---
**`const` with objects**
``` js
const obj = { a: 1 }
obj.a = 99         // fine — mutating contents
obj = {}           // TypeError — reassigning binding

const arr = [1, 2]
arr.push(3)        // fine — [1, 2, 3]
arr = []           // TypeError
```

---
**Loop gotcha**
``` js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100)
}
// 3 3 3 — single shared i

for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100)
}
// 0 1 2 — new i per iteration
```

---
