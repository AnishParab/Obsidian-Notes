# Slicing

Format: `string[start:end:step]`

```python
print(chai_type[0:6])   # Output: Ginger
print(chai_type[:6])    # Same as above
print(chai_type[7:11])  # Output: chai
print(chai_type[-4:])   # Output: chai
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