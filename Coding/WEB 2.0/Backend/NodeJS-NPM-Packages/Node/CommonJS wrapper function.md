# Code
``` js
(function(exports, require, module, __filename, __dirname) {
  // Your module code
});
```

---
# What ? 
It wraps every `.js` file in Node to:
- Provide access to `require`, `module.exports`, etc.
- Keep variables scoped to the module (not global)
- Allow modular backend JavaScript

---
# What this is NOT:
- It **does NOT convert anything**
- It is **NOT related to EJS**
- It is **NOT used for HTML rendering or templating**
- It does **NOT turn JS into HTML**

---
