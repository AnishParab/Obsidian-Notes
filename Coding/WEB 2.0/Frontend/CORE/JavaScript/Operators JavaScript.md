# Arithmetic Operators

| Operator  | Description                     | Example                           |
| --------- | ------------------------------- | --------------------------------- |
| `+`       | Addition / string concatenation | `5 + 2 // 7`, `'a' + 'b' // "ab"` |
| `-`       | Subtraction                     | `5 - 2 // 3`                      |
| `*`       | Multiplication                  | `5 * 2 // 10`                     |
| `/`       | Division                        | `5 / 2 // 2.5`                    |
| `%`       | Remainder (modulus)             | `5 % 2 // 1`                      |
| `**`      | Exponentiation                  | `2 ** 3 // 8`                     |
| Unary `+` | Converts to number              | `+"5" // 5`                       |
| Unary `-` | Negates number                  | `-3 // -3`                        |

---
# Assignment Operators

| Operator | Description                   | Example             |
| -------- | ----------------------------- | ------------------- |
| `=`      | Assign                        | `x = 5`             |
| `+=`     | Add & assign                  | `x += 3`            |
| `-=`     | Subtract & assign             | `x -= 2`            |
| `*=`     | Multiply & assign             | `x *= 2`            |
| `/=`     | Divide & assign               | `x /= 2`            |
| `%=`     | Modulo & assign               | `x %= 2`            |
| `**=`    | Power & assign                | `x **= 3`           |
| `<<=`    | Left shift & assign           | `x <<= 1`           |
| `>>=`    | Sign-propagating right shift  | `x >>= 1`           |
| `>>>=`   | Zero-fill right shift         | `x >>>= 1`          |
| `&=`     | Bitwise AND & assign          | `x &= 3`            |
| `        | =`                            | Bitwise OR & assign |
| `^=`     | Bitwise XOR & assign          | `x ^= 2`            |
| `&&=`    | Logical AND assignment        | `x &&= y`           |
| `        |                               | =`                  |
| `??=`    | Nullish coalescing assignment | `x ??= y`           |

---
# Comparison Operators

| Operator | Description                     | Example              |
| -------- | ------------------------------- | -------------------- |
| `==`     | Equal (type-converting)         | `'5' == 5 // true`   |
| `!=`     | Not equal (type-converting)     | `'5' != 5 // false`  |
| `===`    | Strict equal (no type coercion) | `'5' === 5 // false` |
| `!==`    | Strict not equal                | `'5' !== 5 // true`  |
| `>`      | Greater than                    | `5 > 3`              |
| `<`      | Less than                       | `3 < 5`              |
| `>=`     | Greater than or equal           | `5 >= 5`             |
| `<=`     | Less than or equal              | `3 <= 5`             |

---
# Logical Operators

| Operator | Description                         | Example                          |
| -------- | ----------------------------------- | -------------------------------- |
| `&&`     | Logical AND                         | `true && false // false`         |
| `        |                                     | `                                |
| `!`      | Logical NOT                         | `!true // false`                 |
| `??`     | Nullish coalescing (null/undefined) | `null ?? 'default' // "default"` |

---
# Bitwise Operators (operate on 32-bit signed integers)

| Operator | Description                    | Example        |
| -------- | ------------------------------ | -------------- |
| `&`      | AND                            | `5 & 3 // 1`   |
| `        | `                              | OR             |
| `^`      | XOR                            | `5 ^ 3 // 6`   |
| `~`      | NOT                            | `~5 // -6`     |
| `<<`     | Left shift                     | `5 << 1 // 10` |
| `>>`     | Right shift (sign-propagating) | `5 >> 1 // 2`  |
| `>>>`    | Unsigned right shift           | `5 >>> 1 // 2` |

---
# String Operators
- Only `+` and `+=` are overloaded for string concatenation.
``` js
'Hello' + ' World' // "Hello World"

```

---
# Conditional (Ternary) Operator
``` js
let result = (age >= 18) ? 'Adult' : 'Minor';

```

---
# typeof Operator
``` js
typeof 'abc'; // "string"

```

---
# delete Operator
- Removes a property from an object.
``` js
delete obj.key;

```

---
# in Operator
- Checks if a property exists in an object.
``` js
'length' in []; // true

```

---
# instanceof Operator
- Checks if object is instance of a constructor.
``` js
arr instanceof Array; // true

```

---
# void Operator
- Evaluates an expression and returns `undefined`.
``` js
void 0; // undefined

```

---
# Spread (`...`) and Rest (`...`)
``` js
let arr2 = [...arr1];
function sum(...nums) {}
```

---
# Optional Chaining (`?.`)
```js
user?.address?.city;

```

---
