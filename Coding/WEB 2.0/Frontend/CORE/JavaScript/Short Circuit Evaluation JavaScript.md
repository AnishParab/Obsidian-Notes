# Short-Circuit Evaluation
``` js
let isLoggedIn = true;
isLoggedIn && console.log("Welcome!"); // Executes only if true

let name = null;
let displayName = name || "Guest"; // "Guest"
```

---
