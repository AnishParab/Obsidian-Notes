# Why Generators?
- Use less memory (no full list stored).
- Lazy evaluation (values produced on demand).
- Useful when results don't need to be stored all at once.

---
# Using `yield` to Build Generators
```python
def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

for cup in stall:
    print(cup)
```

**Output:**
```text
Cup 1: Masala Chai
Cup 2: Ginger Chai
Cup 3: Elaichi Chai
```

---
# Function with List vs Generator:
```python
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]  # Returns full list at once

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"  # Yields one at a time (generator)

chai = get_chai_gen()

print(next(chai))  # Cup 1
print(next(chai))  # Cup 2
print(next(chai))  # Cup 3
print(next(chai))  # Raises StopIteration
```

**Output:**

```text
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
