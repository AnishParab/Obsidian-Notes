# Example: Infinite Generator
```python
def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(3):
    print(next(refill))

for _ in range(6):
    print(next(user2))
```

**Output:**
```text
Refill #1
Refill #2
Refill #3
Refill #1
Refill #2
Refill #3
Refill #4
Refill #5
Refill #6
```

---
# Notes:
* `infinite_chai()` is an infinite generator; it never runs out of values.
* Each generator instance keeps its own internal `count`.
* Useful for streams, simulations, or when you can't predict an end condition.

---
