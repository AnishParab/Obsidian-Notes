# Sets (Mutable)
- A **set** is an **unordered**, **mutable**, and **unique** collection of elements.
- It is commonly used for **membership tests**, **eliminating duplicates**, and **set operations** like union, intersection, and difference.

---
### **Example**
```python
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# Union
all_spices = essential_spices | optional_spices

# Intersection
common_spices = essential_spices & optional_spices

# Difference
only_in_essential = essential_spices - optional_spices

print(f"All spices: {all_spices}")
print(f"Common spices: {common_spices}")
print(f"Only in essential spices: {only_in_essential}")

# Membership test
print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")
```

**Output:**
```
All spices: {'cardamom', 'ginger', 'cinnamon', 'cloves', 'black pepper'}
Common spices: {'ginger'}
Only in essential spices: {'cardamom', 'cinnamon'}
Is 'cloves' in essential spices? False
```

---
# **Key Properties:**
* No duplicate elements.
* Elements must be **hashable** (immutable types like `int`, `str`, `tuple`).
* Supports mathematical set operations.
* Mutable → can add or remove elements using `.add()` and `.remove()`.

---
