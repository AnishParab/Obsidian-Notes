- Always returns the same output for the same input.
- Has no _side effects_ (eg:- no logging, no DB access, no modifying global state).
- It does not depend on any state or variables that are outside of its scope.

---
# When to use pure functions

| Use Case                         | Should Be Pure? |
| -------------------------------- | --------------- |
| Business logic                   | ✅ Yes           |
| Mathematical computations        | ✅ Yes           |
| Formatting / parsing             | ✅ Yes           |
| Interacting with DB, files, etc. | ❌ No            |
| Sending network requests<br>     | ❌ No            |

---

