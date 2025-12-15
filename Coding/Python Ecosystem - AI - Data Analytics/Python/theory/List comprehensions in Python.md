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

### Explanation:

* `tea for tea in menu` iterates through each item in the list.
* `if "Iced" in tea` filters items that contain the word `"Iced"`.
* The result is a new list containing only iced teas.

---

