# Example 1: Delegating Generators with `yield from`
```python
def local_chai():
    yield "Masala chai"
    yield "Ginger chai"

def imported_chai():
    yield "Macha"
    yield "Oolong"

# Delegating the tasks
def full_menu():
    yield from local_chai()
    yield from imported_chai()
```

**Output:**
```text
Masala chai
Ginger chai
Macha
Oolong
```

#### Explanation:
* `yield from` delegates part of the generator’s operations to another generator.
* Helps to keep code modular and avoid nested loops or repeated yield statements.

---
# Example 2: Closing a Generator Gracefully
```python
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")

stall = chai_stall()
print(next(stall))

# Gracefully stop the generator
stall.close()
```

**Output:**
```text
Waiting for chai order
Stall closed, No more chai
```

#### Explanation:
* `next(stall)` starts the generator and reaches the first `yield`.
* `stall.close()` stops the generator and triggers cleanup code in the `except` block.
* Useful for freeing resources or doing final actions when a generator is done.

---
