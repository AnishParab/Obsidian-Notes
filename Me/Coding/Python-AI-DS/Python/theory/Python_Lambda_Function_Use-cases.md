# Key rules
- Can have **any number of arguments**
- Must contain **exactly one expression**
- Automatically returns the expression result
- **No statements** (`if`, `for`, `while`, `return`, `print`, etc.)
- Used for **short, simple logic**

---
# Examples
#### Single argument
```python
square = lambda x: x * x
```
#### Multiple arguments
```python
add = lambda a, b: a + b
```
#### With conditional (ternary) expression
```python
max_value = lambda a, b: a if a > b else b
```
#### No arguments
```python
greet = lambda: "Hello"
```

---
# Common usage patterns
#### With `map()`
```python
numbers = [1, 2, 3]
squares = list(map(lambda x: x * x, numbers))
```
#### With `filter()`
```python
evens = list(filter(lambda x: x % 2 == 0, numbers))
```
#### With `sorted()`
```python
students = [("Amit", 85), ("Riya", 92)]
students_sorted = sorted(students, key=lambda x: x[1])
```

---
# When **not** to use lambda
- Logic spans multiple lines
- Needs error handling
- Requires readability or reuse

---
