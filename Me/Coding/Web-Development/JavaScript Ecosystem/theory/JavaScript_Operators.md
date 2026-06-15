# JavaScript Operators

``` js
// Arithmetic
let a = 10 + 3   // 13
let b = 10 - 3   // 7
let c = 10 * 3   // 30
let d = 10 / 3   // 3.333
let e = 10 % 3   // 1   — remainder
let f = 10 ** 3  // 1000 — exponentiation

// Assignment
let x = 10
x += 5   // 15
x -= 3   // 12
x *= 2   // 24
x /= 4   // 6
x %= 4   // 2
x **= 3  // 8

// Unary - post and pre
let y = 10
console.log(++y)   // 11
console.log(y++)   // 11 - then becomes 12
console.log(y--)   // 12 - then becomes 11
console.log(--y)   // 10

// Comparison
console.log(1 == "1")    // true  — coerces type
console.log(1 === "1")   // false — strict, no coercion
console.log(1 != "1")    // false
console.log(1 !== "1")   // true
console.log(5 > 3)       // true
console.log(5 >= 5)      // true

// Logical
console.log(true && false)   // false - AND
console.log(true || false)   // true - OR
console.log(!true)           // false - NOT
console.log(null ?? "default")      // "default" — null/undefined only
console.log(0 ?? "default")         // 0 — 0 is not null/undefined
console.log(0 || "default")         // "default" — 0 is falsy, || triggers

// Ternary
let age = 20
let status = age >= 18 ? "adult" : "minor"   // "adult"

// Type
console.log(typeof 42)          // "number"
console.log(typeof "hello")     // "string"
console.log(typeof null)        // "object" — historical bug
console.log([] instanceof Array) // true

// Bitwise
console.log(5 & 3)    // 1
console.log(5 | 3)    // 7
console.log(5 ^ 3)    // 6
console.log(~5)        // -6
console.log(5 << 1)   // 10
console.log(5 >> 1)   // 2

// Optional chaining
const user = { address: { city: "Nashik" } }
console.log(user?.address?.city)   // "Nashik"
console.log(user?.phone?.number)   // undefined — no error

const arr = [1, 2, 3]
console.log(arr?.[0])              // 1

const fn = null
console.log(fn?.())                // undefined — no error
```

---
# Gotchas

- `==` coerces: `0 == false // true`, `"" == false // true` — avoid
- `||` fallback triggers on any falsy (`0`, `""`, `false`) — use `??` if `0` or `""` are valid values

**Refer this**
[[JavaScript_Type_Coercion_Truthy_and_Falsy_Values]]

---
