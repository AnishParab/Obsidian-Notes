# Syntax
``` python
{expression for item in iterable if condition}
```

> **NOTE**: `expression` is the object that actually returns something, and for set it stores **unique values**.

---
# Mental Model
> Use when you want to find **unique**.

---
# Example 1
```python
favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

# Create a set to remove duplicates
unique_chai = {chai for chai in favourite_chais}
print(unique_chai)
```

**Output:**
```python
{'Masala Chai', 'Green Tea', 'Lemon Tea', 'Elaichi Chai'}
```
### Explanation:
![[set_comprehension_1.excalidraw|500]]

---
# Example 2
```python
recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

# Flatten all spice lists into a single set of unique spices
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
```

**Output:**
```python
{'clove', 'cardamom', 'ginger', 'black pepper', 'milk'}
```
### Steps:
**Step 1**: Iterate over values of the keys
- `unique_spices = {___ for ingredients in recipes.values()}
**Step 2**: Iterate over each individual value in the list.
- `unique_spices = {___ for ingredients in recipes.values() for spice in ingredients}`
**Step 3**: return value to spice.
- `unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}`
### Explanation:
![[set_comprehension.excalidraw|700]]

---
