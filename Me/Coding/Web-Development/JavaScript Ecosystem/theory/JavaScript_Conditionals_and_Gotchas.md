# JavaScript Conditionals

**if / else if / else**
```js
let age = 20

if (age < 13) {
  console.log("child")
} else if (age < 18) {
  console.log("teen")
} else {
  console.log("adult")
}
```

---
**Ternary**
```js
let status = age >= 18 ? "adult" : "minor"

// nested (avoid — unreadable)
let grade = score >= 90 ? "A" : score >= 80 ? "B" : "C"
```

---
**switch**
```js
let day = "Mon"

switch (day) {
  case "Mon":
  case "Tue":
    console.log("weekday")
    break
  case "Sat":
  case "Sun":
    console.log("weekend")
    break
  default:
    console.log("unknown")
}
```

---
**Nullish coalescing (`??`)**
```js
let name = null
console.log(name ?? "Guest")   // "Guest" — only triggers on
							   // null/undefined
							   
console.log(0 ?? "Guest")      // 0 — 0 is not null/undefined
```

---
**Optional chaining with condition**
```js
let user = null
console.log(user?.name ?? "Guest")   // "Guest" — no error
```

---
**Short circuit evaluation**
```js
// && — runs right side only if left is truthy
isLoggedIn && loadDashboard()

// || — runs right side only if left is falsy
let name = username || "Guest"
```

---
# Gotchas:

- `switch` uses `===` internally — no type coercion
- Missing `break` → fallthrough to next case
- `??` vs `||` — use `??` when `0` or `""` are valid values

---
