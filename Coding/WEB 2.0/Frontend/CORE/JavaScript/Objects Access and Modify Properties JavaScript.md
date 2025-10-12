# Accessing Properties
``` js
console.log(user.name);      // "Alice" ✅ Dot notation
console.log(user["age"]);    // 25 ✅ Bracket notation

let prop = "isAdmin";
console.log(user[prop]);     // true ✅ Dynamic access
```

---
# Modifying Properties
``` js
user.age = 30;               // ✅ Modify
user.city = "Delhi";         // ✅ Add new property
delete user.isAdmin;         // ✅ Delete property
```

---
