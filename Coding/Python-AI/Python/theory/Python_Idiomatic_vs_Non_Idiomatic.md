# Idiomatic Python Code
- **Idiomatic Python** means writing code that follows Python’s natural style and best practices—code that _looks right_ to experienced Python developers.

---
# Core Characteristics
- Clear and readable
- Simple and expressive
- Uses Python’s built-in features
- Follows community conventions (PEP 8)

---
# Example 1

**Non-idiomatic**
```python
if len(items) != 0:
    print("Items exist")
```

**Idiomatic**
```python
if items:
    print("Items exist")
```

---
# Example 2

**Non-idiomatic**
```python
for i in range(0, len(nums)):
    print(nums[i])
```

**Idiomatic**
```python
for num in nums:
    print(num)
```

---
# Example 3

**Non-idiomatic**
```python
flag = True
if flag == True:
    run()
```

**Idiomatic**
```python
if flag:
    run()
```

---
# Common Idiomatic Patterns
- Truthy / falsy checks: `if data:`
- Multiple assignment: `a, b = b, a`
- List comprehensions:
```python
squares = [x*x for x in range(5)]
```
- Context managers:
```python
with open("file.txt") as f:
    data = f.read()
```

---
# Guiding Principle

> **“There should be one—and preferably only one—obvious way to do it.”**  
> — _The Zen of Python_

- Idiomatic code prioritizes **clarity over cleverness**.

---
