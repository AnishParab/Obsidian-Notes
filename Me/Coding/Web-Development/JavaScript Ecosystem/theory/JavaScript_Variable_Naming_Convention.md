# JavaScript Variable Naming Conventions

**Rules (enforced by JS engine):**
- Must start with letter, `_`, or `$` — not a number
- No spaces, no special characters except `_` and `$`
- Case-sensitive — `name` and `Name` are different
- Cannot use reserved keywords (`let`, `class`, `return`, etc.)

```js
// valid
let userName
let _private
let $element
let user1

// invalid
let 1user      // SyntaxError
let user-name  // SyntaxError
let let        // SyntaxError
```

---
**Conventions (enforced by team/style):**

| Case            | Usage                 | Example                    |
| --------------- | --------------------- | -------------------------- |
| camelCase       | variables, functions  | `userName`, `getUserData`  |
| PascalCase      | classes, components   | `UserProfile`, `AppRouter` |
| SCREAMING_SNAKE | constants             | `MAX_RETRIES`, `API_URL`   |
| `_prefix`       | private/internal      | `_internalState`           |
| `$prefix`       | DOM elements / jQuery | `$button`                  |

```js
// variables + functions
let userName = "alice"
function getUserData() {}

// classes
class UserProfile {}

// constants
const MAX_RETRIES = 3
const API_URL = "https://api.example.com"

// private convention
class Counter {
  _count = 0       // signals internal — not truly private
  #count = 0       // truly private (ES2022 class field)
}
```

> Gotcha — JS has no enforced private outside `#`. `_` is just a convention signal.

---
