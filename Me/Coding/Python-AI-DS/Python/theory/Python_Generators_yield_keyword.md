# Why Generators?
- Use less memory (no full list stored).
- Lazy evaluation (values produced on demand).
- Useful when results don't need to be stored all at once.

> **NOTE**: You always use a `for` loop to print values from a geneartor function.

---
# Using `yield` to Build Generators

> Yield just **pauses execution** and waits for a **new value** for the generator instance alone.

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
### Exaplanation
![[decorators.excalidraw|500]]

---
