# 1. `print("")`
- You pass a **plain string literal**.
- It prints exactly the content of the string.

Example:
```python
print("")      # prints an empty line
print("abc")   # prints: abc
```

---
# 2. `print(f"")`
- You pass an **f-string**, which is a formatted string literal.
- Inside an f-string, expressions in `{}` are evaluated before printing.

```python
x = 5
print(f"x = {x}")  # prints: x = 5
```

If the f-string has no expressions, it behaves like a normal string:
```python
print(f"hello")  # same as print("hello")
```

---
# 3. `print(variable)`
- Prints the value of the variable using **standard string conversion**.

```python
x = 10
print(x)     # prints: 10
```

---
# 4. `print("a", "b", "c")`
- Prints multiple arguments separated by a space (default `sep=" "`).

```python
print("a", "b", "c")    # prints: a b c
```

---
# 5. `print(..., sep=..., end=...)`
- Controls separators and line endings.

```python
print("a", "b", "c", sep="-")   # a-b-c
print("hello", end="")          # no trailing newline
```

---
# 6. `print()` (no arguments)
Prints a blank line.

---
