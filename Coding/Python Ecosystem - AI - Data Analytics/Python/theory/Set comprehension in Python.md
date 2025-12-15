# Example: Set Comprehension
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
- `{chai for chai in favourite_chais}` removes duplicates by converting the list to a set.

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

### Explanation:

- The nested comprehension `{spice for ingredients in recipes.values() for spice in ingredients}`:
    - First loops over each list of ingredients in the `recipes` dictionary.
    - Then loops over each spice in those lists.
    - Adds each spice to the set, resulting in a collection of unique spices.

---
