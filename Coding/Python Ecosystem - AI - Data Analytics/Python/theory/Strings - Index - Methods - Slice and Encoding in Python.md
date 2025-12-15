# Strings in Python **(Immutable)**
- Strings are **immutable** (cannot be changed after creation).
- Defined using single (`'`), double (`"`), or triple quotes (`'''` / `"""`).

---
# Creating a String

```python
chai_type = "Ginger chai"
```

---
# Indexing
- Indexing starts at **0**.
- Each character has a unique position.

| Character | Index |
| --------- | ----- |
| G         | 0     |
| i         | 1     |
| n         | 2     |
| g         | 3     |
| e         | 4     |
| r         | 5     |
|           | 6     |
| c         | 7     |
| h         | 8     |
| a         | 9     |
| i         | 10    |

### Access by Index

```python
print(chai_type[0])  # Output: G
print(chai_type[-1]) # Output: i
```

`-1` refers to the **last character**.

---
# Slicing

Format: `string[start:end:step]`

```python
print(chai_type[0:6])   # Output: Ginger
print(chai_type[:6])    # Same as above
print(chai_type[7:11])  # Output: chai
print(chai_type[0:6:2]) # Output: Gne (every 2nd character)
```

- **Start** index is inclusive.
- **End** index is exclusive.
- **Step** controls the stride between indices.

---
# Reverse a String

```python
print(chai_type[::-1])  # Output: iahc regniG
```

---
# String Methods

| Method           | Description               | Example                    | Output               |
| ---------------- | ------------------------- | -------------------------- | -------------------- |
| `.upper()`       | Converts to uppercase     | `"chai".upper()`           | `CHAI`               |
| `.lower()`       | Converts to lowercase     | `"ChAi".lower()`           | `chai`               |
| `.title()`       | Capitalizes each word     | `"ginger chai".title()`    | `Ginger Chai`        |
| `.replace(a, b)` | Replace text              | `"chai".replace("i", "y")` | `chay`               |
| `.split()`       | Split into list by spaces | `"ginger chai".split()`    | `['ginger', 'chai']` |
| `.strip()`       | Remove whitespace         | `" chai ".strip()`         | `chai`               |
| `.find()`        | Find substring index      | `"ginger".find("g")`       | `0`                  |

---
# Encoding and Decoding

Used for handling text data in different formats (e.g., UTF-8).

```python
label_text = "Any language string"
encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
```

| Variable        | Type    | Example Output           |
| --------------- | ------- | ------------------------ |
| `encoded_label` | `bytes` | `b'Any language string'` |
| `decoded_label` | `str`   | `Any language string`    |

---
