# Example: Inheritance and Composition in Python

```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

# Inheritance
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")

# Composition
class ChaiShop:
	# Creating a Reference
    chai_cls = BaseChai

    def __init__(self):
		# Creating an object using the reference
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

# Composition + Inheritance
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai  # Override with a specialized chai class

shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()

# Access method unique to MasalaChai
fancy.chai.add_spices()
# MasalaChai inherits `BaseChai.__init__` because it does not define its own. FancyChaiShop overrides `chai_cls`, so ChaiShop ends up instantiating `MasalaChai` instead of `BaseChai`.
```

**Output:**

```text
Serving Regular chai in the shop
Preparing Regular chai...

Serving Masala chai in the shop
Preparing Masala chai...

Adding cardamom, ginger, cloves.
```

---

### Explanation:

#### 1. **Inheritance**

* `MasalaChai` inherits from `BaseChai`, meaning it reuses the base `prepare()` method and adds its own (`add_spices()`).
* This demonstrates **code reuse and extension** — `MasalaChai` *is a* `BaseChai`.

#### 2. **Composition**

* `ChaiShop` uses a `chai_cls` to create a `chai` object inside itself.
* This means the shop *has a* chai — not *is a* chai.
* Composition allows flexible behavior by **injecting** different chai classes (`BaseChai`, `MasalaChai`, etc.) without modifying the `ChaiShop` code.

#### 3. **Polymorphism in Action**

* `FancyChaiShop` inherits from `ChaiShop` but overrides `chai_cls` with `MasalaChai`.
* When `fancy.serve()` is called, it automatically uses the `MasalaChai` version, showing dynamic behavior at runtime.

---

**In short:**

* **Inheritance** → “Is a” relationship (`MasalaChai` *is a* `BaseChai`).
* **Composition** → “Has a” relationship (`ChaiShop` *has a* `Chai`).
* Together, they provide flexibility, reusability, and cleaner code design.

---
