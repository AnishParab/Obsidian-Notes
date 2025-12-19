# Dictionary in Python **(Mutable)**
- Allows named-based indexing.
``` python
# dictionary
chai_order = dict(type="Masala chai", size="large", sugar=2)
print(f"Chai order: {chai_order}")

# Adding elements
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# Printing single element
print(f"Recipe base: {chai_recipe['base']}")

# Delete
print(f"Recipe base: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe base: {chai_recipe}")

# Membership test
print(f"Is sugar in the order? {'sugar' in chai_order}")

# dictionery 2nd way, redifining
chai_order = {"type": "Ginger chai", "size": "Medium", "sugar": 1}

# key value pairs
print(f"Order details (keys): {chai_order.keys()}")  # returns an array
print(f"Order details (values): {chai_order.values()}")  # returns an array
print(
    f"Order details (items): {chai_order.items()}"
)  # returns an array of tuples of key value pairs

# Method: popitem
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")
print(f"{chai_order}")

# Method: update
extra_spices = {"cardmom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

# Throws an error if value is not present
chai_size = chai_order["size"]
print(f"Chai size is {chai_size}")

# Safer way to get values with no errors
customer_note = chai_order.get("note", "NO note")
print(f"Customer note is {customer_note}")
```

---
- All the things like union, complement etc you learnt in sets can be applied here also.

---
