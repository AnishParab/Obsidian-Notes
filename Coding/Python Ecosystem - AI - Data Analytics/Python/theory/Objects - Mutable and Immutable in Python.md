# Objects
> Everything is an object in python.

## `IVT`

Each object has:
- **Identity** → Unique address in memory (`id()`)
- **Type** → The kind of object (`type()`)
- **Value** → The actual data stored

#### Code
``` python
x = 10
print(id(x))      # identity
print(type(x))    # type
print(x)          # value
```

#### Output
``` text
22405776
<class 'int'>
2
```

---
# Mutability
- **Mutable:** Changeable object (e.g., list, dict, set)
- **Immutable:** Unchangeable object (e.g., int, float, str, tuple)

> Mutability is determined by **identity**, not by value.

---
# Immutable Code
``` python
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Initial sugar: {sugar_amount}")
```

![[python_mutability.excalidraw|500]]

---
## Proof
``` python
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Initial sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")
```

``` bash
Initial sugar: 2
Initial sugar: 12
ID of 2: 22405776
ID of 12: 22406096
```

**OR**
``` python
x = 4
print("Initial: ", x)

print("ID before: ", id(x))

x = 20
print("After: ", x)

print("ID after: ", id(x))
```

``` text
Initial:  4
ID before:  22405840
After:  20
ID after:  22406352
```

> Even though the value changed, the object reference changed too.
> **The identity (`id`) differs → Immutable**
> Hence this proves that the reference changes.

---
# Mutable Code
``` python
spice_mix = set()
print(f"Initial spice mix: {spice_mix}")
print(f"Initial spice mix id: {id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("Cardamom")

print(f"After spice mix: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")
```

## Output
``` bash
Initial spice mix: set()
Initial spice mix id: 139750398252800
After spice mix: {'Cardamom', 'Ginger'}
After spice mix id: 139750398252800
```

> The `id` remains same but the value is changed.
> **The identity remains the same → Mutable**

---
# Summary

> **If the memory address stays constant, the object is immutable**.

---
