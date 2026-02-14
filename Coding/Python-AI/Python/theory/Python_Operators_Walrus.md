# Statement vs Expression

- `x = 5` → statement (assignment)
- `3 + 3` → expression (returns a value)

---
# Walrus operator (`:=`)

## Without walrus
```python
value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible, remainder is {remainder}")
````

---
## With walrus

> Avoids separate assignment before condition

- Example 1
```python
value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")
```

- Example 2
```python
available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size:\n").lower()) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")
```

- Example 3
```python
flavors = ["masala", "ginger", "lemon", "mint"]
print("Available flavors:", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You chose {flavor} chai")
```

---
