# `if` Statement
``` js
let age = 18;

if (age >= 18) {
    console.log("Adult");
}
```
- Runs the block only if the condition is **true**.

---
# `if-else` Statement
``` js
let age = 16;

if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}
```

---
# `if-else if-else` Statement
``` js
let score = 85;

if (score >= 90) {
    console.log("A");
} else if (score >= 80) {
    console.log("B");
} else {
    console.log("C or lower");
}
```

---
# Nested `if` Statement
``` js
let user = "admin";
let loggedIn = true;

if (loggedIn) {
    if (user === "admin") {
        console.log("Welcome Admin");
    }
}
```

---
