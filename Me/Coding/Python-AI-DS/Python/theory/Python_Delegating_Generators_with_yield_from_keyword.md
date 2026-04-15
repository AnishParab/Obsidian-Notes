# `yield from`

>  * `yield from` delegates part of the generator’s operations to **another generator**.

---
# Code: Delegating Generators with `yield from`
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
	
for chai in full_menu():
    print(chai)
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
