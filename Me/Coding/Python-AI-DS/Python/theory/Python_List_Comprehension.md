# Syntax
``` python
[expression for items in iterable if condition]
```

> **NOTE**: `expression` is the object that actually returns something

---
# Example: List Comprehension

```python
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

# Filter only the teas that contain the word "Iced"
iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)
```

**Output:**
```text
['Iced Lemon Tea', 'Iced Peach Tea']
```
### Steps:
**Step 1**:
- `[___ for tea in menu]`
**Step 2**:
- `[___ for tea in menu if "Iced" in tea]`
**Step 3**:
- `[tea for tea in menu if "Iced" in tea]`
### Explanation:
![[list_comprehension.excalidraw|500]]

---

