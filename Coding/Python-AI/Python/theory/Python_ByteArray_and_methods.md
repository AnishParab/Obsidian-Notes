# `bytearray` (Mutable Byte Sequence in Python)

## What is `bytearray`?
- `bytearray` represents a **mutable sequence of bytes**.
- Unlike `bytes`, its contents **can be changed after creation**.
- Commonly used for **binary data manipulation**, buffers, and low-level I/O.

---
## Syntax

```python
bytearray(source=b"", encoding=None, errors="strict")
```

### Common sources
- `bytes` object
- Iterable of integers (`0–255`)
- String (requires `encoding`)

---
# Basic Example

```python
raw_spice_data = bytearray(b"Cinnamon")
raw_spice_data[0:5] = b"Card"
print(raw_spice_data)
```

**Output**
```
bytearray(b'Cardmon')
```

### Explanation
- `b"Cinnamon"` → immutable `bytes`
- `bytearray(...)` → mutable byte sequence
- Slice assignment **modifies the data in place**

⚠️ Note:  
`bytearray.replace()` **returns a new bytearray**; it does _not_ modify in-place.  
Slice assignment is the correct way to mutate content.

---
# Mutability Demonstration
```python
data = bytearray(b"ABC")
data[1] = ord("Z")
print(data)
```

**Output**
```
bytearray(b'AZC')
```

---
## `bytes` vs `bytearray`

| Feature          | `bytes`           | `bytearray`           |
| ---------------- | ----------------- | --------------------- |
| Mutability       | ❌ Immutable       | ✅ Mutable             |
| Index assignment | ❌ Not allowed     | ✅ Allowed             |
| Use case         | Fixed binary data | Editable binary data  |
| Example          | `b"Hello"`        | `bytearray(b"Hello")` |

---
# Supported Operations

### Concatenation (`+`)
```python
bytearray(b"Hi") + bytearray(b"!")
```

### Repetition (`*`)
```python
bytearray(b"A") * 3
```

### Append / Extend
```python
data.append(65)        # 'A'
data.extend(b"BC")
```

---
# Important Characteristics
- Each element is an **integer (0–255)**
- Behaves like a **mutable list of bytes**
- Efficient for:
    - network packets
    - file buffers
    - binary protocol parsing
    - memory-efficient data updates

---
# When to use `bytearray`
Use `bytearray` when:
- You need to **modify binary data**
- Performance matters for repeated updates
- Working with low-level I/O or buffers

Use `bytes` when:
- Data should remain immutable
- Hashability is required (dict keys, sets)

---
# One-line summary

> **`bytearray` is to `bytes` what `list` is to `tuple`.**

If you want, I can:
- add memory layout explanation
- compare `bytearray` with `array('b')` and `memoryview`
- show real networking or file I/O examples

---
