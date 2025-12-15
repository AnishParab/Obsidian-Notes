# Number Types **(Immutable Data Types)**

1. **Integers (`int`)** – Whole numbers, positive or negative.  
    _Examples:_ `10`, `-5`, `0`
	
2. **Booleans (`bool`)** – Logical values representing truth.  
    _Values:_ `True`, `False`
	
3. **Floating-Point (`float`)** – Numbers with decimal points.  
    _Examples:_ `3.14`, `-0.5`, `2.0`0
	
4. **Complex Numbers (`complex`)** – Combine real and imaginary parts.  
    _Examples:_ `2 + 3j`, `-1j`, `4 - 2j`

---
# Arithmetic Operators

| Operator | Description              | Example  | Output |
| -------- | ------------------------ | -------- | ------ |
| `+`      | Addition                 | `2 + 3`  | `5`    |
| `-`      | Subtraction              | `5 - 2`  | `3`    |
| `*`      | Multiplication           | `4 * 3`  | `12`   |
| `/`      | Division (float result)  | `5 / 2`  | `2.5`  |
| `//`     | Floor division (integer) | `5 // 2` | `2`    |
| `%`      | Modulus (remainder)      | `5 % 2`  | `1`    |
| `**`     | Exponentiation (power)   | `2 ** 3` | `8`    |

---
# Logical Operators

| Operator | Description                          | Example               | Output  |
| -------- | ------------------------------------ | --------------------- | ------- |
| `and`    | True if **both** conditions are true | `(5 > 2) and (3 < 4)` | `True`  |
| `or`     | True if **either** condition is true | `(5 < 2) or (3 < 4)`  | `True`  |
| `not`    | Inverts the Boolean value            | `not (5 > 2)`         | `False` |

---
# Comparison Operators

| Operator | Description              | Example  | Output |
| -------- | ------------------------ | -------- | ------ |
| `==`     | Equal to                 | `3 == 3` | `True` |
| `!=`     | Not equal to             | `3 != 4` | `True` |
| `>`      | Greater than             | `5 > 3`  | `True` |
| `<`      | Less than                | `2 < 4`  | `True` |
| `>=`     | Greater than or equal to | `5 >= 5` | `True` |
| `<=`     | Less than or equal to    | `3 <= 5` | `True` |

---
# Bitwise Operators

- Operate on binary representations of integers.

| Operator | Description               | Example  | Binary Example | Output |
| -------- | ------------------------- | -------- | -------------- | ------ |
| `&`      | Bitwise AND               | `5 & 3`  | `101 & 011`    | `1`    |
| ` \| `   | Bitwise OR                | `5 \| 3` | `101 \| 011`   | `7`    |
| `^`      | Bitwise XOR               | `5 ^ 3`  | `101 ^ 011`    | `6`    |
| `~`      | Bitwise NOT (invert)      | `~5`     | `~0101`        | `-6`   |
| `<<`     | Left shift (×2 per step)  | `5 << 1` | `101 → 1010`   | `10`   |
| `>>`     | Right shift (÷2 per step) | `5 >> 1` | `101 → 10`     | `2`    |

---
