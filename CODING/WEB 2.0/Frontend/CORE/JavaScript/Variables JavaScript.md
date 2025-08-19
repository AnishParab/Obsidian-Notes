# What are Variables?
- **Variables** are **named memory locations** used to **store**, **reference**, and **manipulate** data during program execution.
### Key Concepts
- **Human-readable identifiers** to access memory locations.
- Store different types of data:
    - `number`, `string`, `boolean`, `object`, `array`, `function`, etc.
- Allow **data reuse**, **dynamic updates**, and **maintainability**.
- Abstract low-level memory management — you don’t handle memory addresses directly.

---
# Declaring Variables in JavaScript
- JavaScript provides **three keywords** to declare variables: `var`, `let`, and `const`.

---
## `var` — **Legacy (Function Scoped)**
### Characteristics
- Function-scoped (not block-scoped)
- Reassignable
- Redeclarable
- Hoisted to top of scope and initialized as `undefined`

``` js
function demoVar() {
  var x = 10;
  if (true) {
    var x = 20; // Same x!
    console.log(x); // 20
  }
  console.log(x); // 20 (still the same)
}
demoVar();
```

---
## `let` — **Modern (Block Scoped)**
### Characteristics
- Block-scoped (`{ }`)
- Reassignable
- Not redeclarable within the same scope
- Hoisted, but not initialized (Temporal Dead Zone applies).

``` js
function demoLet() {
  let y = 10;
  if (true) {
    let y = 20; // Different y (scoped to block)
    console.log(y); // 20
  }
  console.log(y); // 10
}
demoLet();
```

---
## `const` — **Constant (Block Scoped)**
### Characteristics
- Block-scoped
- Not reassignable
- Not redeclarable
- Hoisted, but not initialized (Temporal Dead Zone)

``` js
function demoConst() {
  const z = 100;
  // z = 200; // ❌ Error: Assignment to constant variable

  const person = { name: "Alice" };
  person.name = "Bob"; // ✅ Allowed (object reference is constant, but properties can change)
  console.log(person.name); // Bob
}
demoConst();
```

---
# Variable Naming Conventions in JavaScript
### Valid Rules
- Must begin with a **letter**, **underscore `_`**, or **dollar sign `$`**
- Subsequent characters can include digits `0-9`
- **Case-sensitive**: `score` and `Score` are different
- Cannot use **reserved keywords** like `let`, `var`, `class`, etc.
### Recommended Style (CamelCase)
| Style                  | Example               | Purpose                            |
| ---------------------- | --------------------- | ---------------------------------- |
| `camelCase`            | `userName`, `isValid` | **Preferred in JavaScript**        |
| snake_case             | `user_name`           | ⚠️ Not idiomatic in JS             |
| kebab-case             | `user-name`           | ❌ Invalid for variables            |
| `PascalCase`           | `UserProfile`         | **For class names / constructors** |
| `SCREAMING_SNAKE_CASE` | `USER_ID`             | **For Constants**                  |

### Avoid
- Starting names with numbers (e.g., `1value`)
- Using symbols (except `_`, `$`)
- Single-character names (unless in small scopes like loops)
- Non-descriptive names like `a`, `temp`, `data` (unless appropriate)

---
