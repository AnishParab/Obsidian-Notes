# Inheritance v/s Composition
- **Inheritance** allows directly inheriting the properties of the `BaseClass`.
- **Composition** allows using the properties of the `BaseClass` using a **reference**.

---
# Code
```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Prepare {self.type} chai....")


# Inheritance
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


# Composition
class ChaiShop:
    # Creating a reference
    chai_cls = BaseChai

    def __init__(self):
        # Creating an object using the reference
        self.chai = self.chai_cls("Regular")

    def serve(self):
        # You have access to properties of BaseChai
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


# Inheritance + Composition
class FancyChaiShop(ChaiShop):
    # Override chai_cls of ChaiShop with a Specialised chai class
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()

# shop - Inheritance accesses
print(shop.chai)
print(shop.chai_cls)
shop.serve()

# fancy - Inheritance accesses
print(fancy.chai_cls)
print(fancy.chai)
fancy.serve()

# shop - Composition accesses
# shop.chai_cls.prepare() -> Will give you argument missing for parameter self
shop.chai.prepare()

# fancy - Composition accesses
# fancy.chai_cls.add_spices() -> Will give you argument missing for parameter self



# Runtime Constructors
# chai_cls in FancyChaiShop is overridden and does not have a Constructor
# Hence it creates a Constructor of the Inherited class
# Hence chai is accessible
# The constructor is created at runtime
fancy.chai.add_spices()
```

**Output:**
```text
<__main__.BaseChai object at 0x7f4bbd178ad0>
<class '__main__.BaseChai'>
Serving Regular chai in the shop
Prepare Regular chai....
<class '__main__.MasalaChai'>
<__main__.MasalaChai object at 0x7f4bbd178d70>
Serving Regular chai in the shop
Prepare Regular chai....
Prepare Regular chai....
Adding cardamom, ginger, cloves.
```

> Hence, if you don't have a constructor, it will be automatically made at the time of execution behind the scenes.

---
