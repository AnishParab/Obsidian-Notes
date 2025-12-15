# Tuples in Python **(Immutable)**
- Tuples are **immutable** (cannot be changed after creation).
- Defined using parentheses `()`.

---
# Creating a Tuple

```python
masala_spices = ("cardamom", "cloves", "cinnamon")
```

---
# Tuple Unpacking

- You can assign tuple elements to variables in one line.

```python
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")
```

**Output:**

```
Main masala spices: cardamom, cloves, cinnamon
```

---
# Multiple Assignment

```python
ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cardamom_ratio}")
```

### Swapping Variables

```python
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Swapped ratio → G: {ginger_ratio}, C: {cardamom_ratio}")
```

---
# Membership Test

- Check if an item exists in a tuple using `in`.

```python
print("ginger" in masala_spices)    # False
print("cinnamon" in masala_spices)  # True
print("Cinnamon" in masala_spices)  # False (case-sensitive)
```

---
## Tuple Characteristics

| Feature                     | Description                       |
| --------------------------- | --------------------------------- |
| Immutable                   | Cannot be modified once created   |
| Ordered                     | Elements maintain insertion order |
| Allow duplicates            | Yes                               |
| Can contain different types | Example: `(1, "chai", 3.14)`      |

---
## Useful Tuple Operations

| Operation     | Example                       | Output                                                                 |
| ------------- | ----------------------------- | ---------------------------------------------------------------------- |
| `len()`       | `len(masala_spices)`          | `3`                                                                    |
| Indexing      | `masala_spices[0]`            | `cardamom`                                                             |
| Slicing       | `masala_spices[0:2]`          | `('cardamom', 'cloves')`                                               |
| Concatenation | `masala_spices + ("nutmeg",)` | `('cardamom', 'cloves', 'cinnamon', 'nutmeg')`                         |
| Repetition    | `masala_spices * 2`           | `('cardamom', 'cloves', 'cinnamon', 'cardamom', 'cloves', 'cinnamon')` |

---
