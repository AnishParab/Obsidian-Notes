# Optional Chaining
``` js
let user = { profile: { name: "Alice" } };

if (user?.profile?.name === "Alice") {
    console.log("Hello Alice");
}
```

- Prevents errors if a property is `undefined` or `null`.

---
