# Why not use raw `XMLHttpRequest`
- Verbose Syntax
- Callback Hell (`onreadystatechange`)
- No promises (built-in)
- No error catching like `try...catch`

---
# jQuery AJAX
-  Simple syntax like `$.ajax()`, `$.get()`, `$.post()`
-  Legacy now, but still in use.

---
# Axios
-  Based on Promises
-  Works in both **browser** and **Node.js**
-  Better error handling
-  Interceptors, CSRF handling, etc.

---
# Fetch API
-  Native in all browsers
-  Promise-based (like Axios)
-  Needs manual JSON parsing and error handling

---
#  Which one should you care about?

| Use Case                   | Suggestion                      |
| -------------------------- | ------------------------------- |
| Learning core principles   | Use `XMLHttpRequest` ✅          |
| Want Promises + modern JS  | Use `fetch()`                   |
| Real projects (React, Vue) | Use `Axios`                     |
| Legacy projects            | Might still use `jQuery.ajax()` |
