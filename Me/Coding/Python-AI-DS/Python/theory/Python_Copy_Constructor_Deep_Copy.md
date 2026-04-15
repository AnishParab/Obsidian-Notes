**Pre-requisite**
[[Python_Copy_Constructor_Shallow_Copy]]

---
# Deep Copy

- Copies the object AND all nested objects — fully independent

```python
tea3 = copy.deepcopy(tea1)

tea3.flavor = "Kawa"
tea3.ingredients.append("cardamom")

print(tea1.flavor)       # Ginger
print(tea1.ingredients)  # unaffected — fully independent copy
# ["water", "milk", "ginger", "lemon"]

print(tea3.flavor)       # Kawa
print(tea3.ingredients)  # ["water", "milk", "ginger", "lemon", "cardmom"]
```

---
