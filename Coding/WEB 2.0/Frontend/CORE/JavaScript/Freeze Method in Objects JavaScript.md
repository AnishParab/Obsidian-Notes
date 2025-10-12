# `Object.freeze()` — Make Objects Immutable in JS
#####  **Purpose**
`Object.freeze()` **freezes** an object — meaning:
- You cannot **add** new properties
- You cannot **delete** existing ones
- You cannot **modify** property values
- You cannot **reconfigure** properties

> Makes an object **immutable** at the **top level**.

---
# Syntax
``` js
Object.freeze(obj)

```
- Takes an object `obj` and **freezes** it in place.
- Returns the **same object**, now immutable.

---
# Check if Object is Frozen
``` js
Object.isFrozen(user); // true ✅

```

---
# **Shallow Freeze**
- `Object.freeze()` is **shallow** i.e. Nested objects are **not frozen**.

``` js
const config = {
  env: "prod",
  db: {
    host: "localhost",
    port: 5432
  }
};

Object.freeze(config);

config.db.port = 3306; // ✅ This will succeed! (⚠️ Not deeply frozen)
```

---
# **Deep Freeze Utility Function**
``` js
function deepFreeze(obj) {
  Object.freeze(obj);

  for (const key in obj) {
    if (
      typeof obj[key] === 'object' &&
      obj[key] !== null &&
      !Object.isFrozen(obj[key])
    ) {
      deepFreeze(obj[key]);
    }
  }

  return obj;
}

deepFreeze(config);
config.db.port = 3306; // ❌ Now blocked
```

---

