# **Operator Overloading**

Operator overloading lets built-in operators behave differently depending on operand types.
For example, `+` can add numbers, concatenate strings, or merge lists.

### **Example 1: List Concatenation (`+`)**

```python
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")
```

**Output:**

```
Liquid mix: ['water', 'milk', 'ginger']
```

**Explanation:**
The `+` operator merges two lists into one.
This is an example of **operator overloading**, where `+` performs **concatenation** instead of arithmetic addition.

---

### **Example 2: List Repetition (`*`)**

```python
strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")
```

**Output:**

```
Strong brew: ['black tea', 'water', 'black tea', 'water', 'black tea', 'water']
```

**Explanation:**
The `*` operator repeats the list elements `n` times.
Here, multiplying by `3` repeats the list three times.

---
# **Bytearray (Mutable Byte Sequence)**

A `bytearray` is a **mutable** sequence of bytes.
It allows modification of binary data, unlike `bytes` (which are immutable).

### **Syntax**

```python
bytearray([source[, encoding[, errors]]])
```

### **Example**

```python
raw_spice_data = bytearray(b"Cinnamon")
raw_spice_data = raw_spice_data.replace(b"Cinna", b"Card")
print(f"Bytes: {raw_spice_data}")
```

**Output:**

```
Bytes: bytearray(b'Cardmon')
```

**Explanation:**

* `b"Cinnamon"` is a bytes literal.
* `bytearray()` converts it into a mutable byte sequence.
* `.replace()` modifies the byte content in-place.

---

## **Key Points**

| Feature          | Description                   | Mutable | Example                       |
| ---------------- | ----------------------------- | ------- | ----------------------------- |
| `bytes`          | Immutable sequence of bytes   | ❌       | `b"Hello"`                    |
| `bytearray`      | Mutable sequence of bytes     | ✅       | `bytearray(b"Hello")`         |
| `+` (Overloaded) | Concatenates lists or strings | —       | `[1, 2] + [3] → [1, 2, 3]`    |
| `*` (Overloaded) | Repeats lists or strings      | —       | `["a"] * 3 → ["a", "a", "a"]` |

---
