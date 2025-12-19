# Truthy & Falsy in Python
- Python converts values to `True` or `False` using `bool()`
- This behavior is called **truthiness**

---
# Rules
- **Falsy values** → `False`
    - `0`, `0.0`
    - `None`
    - `False`
    - Empty collections: `""`, `[]`, `{}`, `()`
	
- **Truthy values** → `True`
    - Any non-zero number
    - Any non-empty collection or string
    - Most objects

---
# Example Code
```python
milk_present = 0
print(bool(milk_present))   # False

chai_present = 12
print(bool(chai_present))   # True
```

---
# Key Insight
- `0` means **absence**
- Non-zero values mean **presence**
- Used heavily in conditions:

```python
if chai_present:
    serve_chai()
```

---
### Why It Matters
- Cleaner condition checks
- Fewer explicit comparisons
- Idiomatic Python code

---
