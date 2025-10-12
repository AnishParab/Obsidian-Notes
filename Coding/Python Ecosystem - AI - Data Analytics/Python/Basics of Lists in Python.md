- It is a **mutable** data type.

---
# Code and common List methods
``` python
ingredients = ["water", "milk", "black tea"]

# Append method
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

# Remove method
ingredients.remove("water")
print(f"ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

# Extend method
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

# Insert method
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

# Pop method
last_added = chai.ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")

# Reverse method
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

# Sort method
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

# Maximum and minimum in a list
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Maximum sugar level: {min(sugar_levels)}")
```

- Index starts with `0`.

---
