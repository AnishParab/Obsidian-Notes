# `next()`

> `next()` is used to **manually fetch** each yield values for **each execution pause**, until **stop iteration**.

> It triggers a **yield**.

---
# Function with List vs Generator:
```python
# Returns full list at once
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# Yields one at a time (generator)
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()

print(chai)

print(next(chai))  # Cup 1
print(next(chai))  # Cup 2
print(next(chai))  # Cup 3
print(next(chai))  # Raises StopIteration
```

**Output:**
```text
<generator object get_chai_generator at 0x7fcfcbd46800>

Cup 1
Cup 2
Cup 3
Traceback (most recent call last):
  ...
StopIteration
```

---
# Key Takeaways:
- `yield` turns a function into a generator.
- Once a generator is exhausted, `StopIteration` is raised.
- Use `next()` to manually fetch values or loop through with `for`.

---
