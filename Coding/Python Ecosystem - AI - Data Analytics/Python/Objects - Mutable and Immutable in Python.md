# Objects
> Everything is an object in python.

Each object has it's own **identity**, **type** and **value**.

---
# Mutability
- **Mutable** ---> It is changeable.
- **Immutable** ---> It is not changeable.

- Never check mutability with **value**, instead check it with **identity**.

---
# Immutable Code
``` python
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Initial sugar: {sugar_amount}")
```

![[python_mutability.excalidraw|500]]

> Hence `sugar_amount` is **immutable**, since value changes but it's identity doesn't.

> What changes is the **reference**.

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

``` bash
Initial spice mix: set()
Initial spice mix id: 139750398252800
After spice mix: {'Cardamom', 'Ginger'}
After spice mix id: 139750398252800
```

> The `id` remains same but the value is changed.

---

> **Basically, if the memory address is changeable then it is mutable.**

---
