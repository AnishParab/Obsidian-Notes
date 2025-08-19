# Datatypes
Javascript is dynamically typed and uses **type coercion** heavily.

---
### Primitive Types (Immutable)

| Type          | Example         | Notes                        |
| ------------- | --------------- | ---------------------------- |
| **Number**    | `42`, `3.14`    | All numbers are 64-bit float |
| **String**    | `"hello"`       | Immutable                    |
| **Boolean**   | `true`, `false` | Simple logic                 |
| **Null**      | `null`          | Intentional empty            |
| **Undefined** | `undefined`     | Uninitialized variable       |
| **Symbol**    | `Symbol("id")`  | Unique identifiers           |
| **BigInt**    | `123n`          | For integers > 2⁵³ - 1       |

---
###  Reference Types (Mutable)

| Object Type       | Description                                                         | Example                                        |
| ----------------- | ------------------------------------------------------------------- | ---------------------------------------------- |
| **Object**        | Generic key–value pairs, created with literals `{}` or constructors | `let obj = { key: 'value' };`                  |
| **Array**         | Ordered list, subclass of Object                                    | `let arr = [1, 2, 3];`                         |
| **Function**      | Callable object, can be declared or as arrow function               | `function greet() {}` or `const fn = () => {}` |
| **Date**          | Date and time representation                                        | `let now = new Date();`                        |
| **RegExp**        | Regular expressions                                                 | `let pattern = /abc/g;`                        |
| **Map / WeakMap** | Key–value pairs; WeakMap keys must be objects                       | `let map = new Map();`                         |
| **Set / WeakSet** | Collections of unique values; WeakSet values must be objects        | `let set = new Set([1,2,3]);`                  |
| **Typed Arrays**  | Binary data views for efficient numeric storage                     | `let buffer = new Uint8Array([1,2,3]);`        |
| **Error Objects** | Represent runtime errors                                            | `throw new Error('Oops');`                     |

---

