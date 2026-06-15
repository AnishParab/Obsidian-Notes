# JavaScript Loops

**for**
```js
for (let i = 0; i < 5; i++) {
  console.log(i)   // 0 1 2 3 4
}
```

---
**while**
```js
let i = 0
while (i < 5) {
  console.log(i)   // 0 1 2 3 4
  i++
}
```

---
**do...while**
```js
let i = 0
do {
  console.log(i)   // runs at least once even if condition is false
  i++
} while (i < 5)
```

---
**for...of** — iterate over iterables (arrays, strings, maps, sets)
```js
const nums = [1, 2, 3]
for (const num of nums) {
  console.log(num)   // 1 2 3
}
```

---
**for...in** — iterate over object keys
```js
const user = { name: "alice", age: 25 }
for (const key in user) {
  console.log(key, user[key])   // name alice, age 25
}
```

---
**Loop control (break and continue)**
```js
// break — exit loop entirely
for (let i = 0; i < 5; i++) {
  if (i === 3) break
  console.log(i)   // 0 1 2
}

// continue — skip current iteration
for (let i = 0; i < 5; i++) {
  if (i === 3) continue
  console.log(i)   // 0 1 2 4
}
```

---
# Gotchas:

- `for...in` on arrays — avoid, iterates keys as strings (`"0"`, `"1"`) and may include prototype properties
- `for...of` on objects — throws error, objects are not iterable by default
- `var` in loops — use `let` always (scope gotcha covered in [[JavaScript_Variables_and_Gotchas]])

---
