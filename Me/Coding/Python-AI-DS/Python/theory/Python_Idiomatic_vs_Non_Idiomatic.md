# Idiomatic Python

- Idiomatic = code written in Python’s natural style (common patterns + best practices).

## Characteristics
- readable
- simple
- uses built-ins
- follows conventions (PEP 8)

---
# Examples

### 1) emptiness check
Non-idiomatic:
```python
if len(items) != 0:
    print("Items exist")
````

Idiomatic:
```python
if items:
    print("Items exist")
```

### 2) iteration
Non-idiomatic:
```python
for i in range(0, len(nums)):
    print(nums[i])
```

Idiomatic:
```python
for num in nums:
    print(num)
```

### 3) boolean check
Non-idiomatic:
```python
flag = True
if flag == True:
    run()
```

Idiomatic:
```python
if flag:
    run()
```

---
# Common patterns

- truthy/falsy: `if data:`
- swap: `a, b = b, a`

- list comprehension:
```python
squares = [x*x for x in range(5)]
```

- context manager:
```python
with open("file.txt") as f:
    data = f.read()
```

---

> “There should be one—and preferably only one—obvious way to do it.” — Zen of Python

---
