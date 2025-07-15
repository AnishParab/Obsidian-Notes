# Declaring Variables
### `var` (Use for legacy code only)
- Scope ---> Function
- Reassignments ---> Yes
- Redeclarable ---> Yes
- Hoisted ---> Yes (but undefined)
### `let`
- Scope ---> Block
- Reassignments ---> Yes
- Redeclarable ---> No
- Hoisted ---> Temporal Dead Zone applies
### `const`
- Scope ---> Block
- Reassignments ---> No
- Redeclarable ---> No
- Hoisted ---> Temporal Dead Zone applies

---
# Datatypes
Javascript is dynamically typed and uses **type coercion** heavily.
### Primitive Types (Immutable)

| Type      | Example         | Notes                        |
| --------- | --------------- | ---------------------------- |
| Number    | `42`, `3.14`    | All numbers are 64-bit float |
| String    | `"hello"`       | Immutable                    |
| Boolean   | `true`, `false` | Simple logic                 |
| Null      | `null`          | Intentional empty            |
| Undefined | `undefined`     | Uninitialized variable       |
| Symbol    | `Symbol("id")`  | Unique identifiers           |
| BigInt    | `123n`          | For integers > 2⁵³ - 1       |
###  Reference Types (Mutable)

| Type     | Example                              |
| -------- | ------------------------------------ |
| Object   | `{ key: "value" }`                   |
| Array    | `[1, 2, 3]`                          |
| Function | `function() {}`                      |
| Others   | `Date`, `RegExp`, `Map`, `Set`, etc. |

---
