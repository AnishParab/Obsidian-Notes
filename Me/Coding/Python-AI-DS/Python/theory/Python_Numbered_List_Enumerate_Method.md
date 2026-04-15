# Problem
You are creating a tea menu board. Each item must be numbered.
- Use `enumerate()` to print menu items with numbers.

---
# Enumerate
- **Enumerate** returns a **numbered list**.

---
# Code
```python
menu = ["Green", "Lemon", "Spiced", "Mint"]

for m in menu:
	print(f"Menu item is {m}")
	
x = list(enumerate(menu))
print(x)
# Output
# [(0, 'Green'), (1, 'Lemon'), (2. 'Spiced'), (3, 'Mint')]

y = list(enumerate(menu, start=1))
print(y)
# Output
# [(1, 'Green'), (2, 'Lemon'), (3. 'Spiced'), (4, 'Mint')]

for idx, item in enumerate(menu, start=1):
	print(f"{idx} : {item} chai")
# Ouput
# 1 : Green chai
# 2 : Lemon chai
# 3 : Spiced chai
# 4 : Mint chai
```

---
