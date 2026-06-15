# Composition via Runtime Constructors

- If a child class has no `__init__`, Python walks up MRO and uses the first `__init__` it finds
- `self.dog_cls` resolves to the subclass's value at runtime — not the parent's

```python
class Dog:
    def __init__(self, name):
        self.name = name

class Labrador(Dog):
    def fetch(self):
        print(f"{self.name} fetches!")

class DogShelter:
    dog_cls = Dog

    def __init__(self):
        self.dog = self.dog_cls("Bruno")  # self.dog_cls resolved at runtime

class FancyShelter(DogShelter):
    dog_cls = Labrador  # no __init__ — uses DogShelter.__init__

fancy = FancyShelter()
# MRO: FancyShelter → DogShelter → object
# DogShelter.__init__ runs
# self.dog_cls = Labrador at runtime
# self.dog = Labrador("Bruno") — not Dog("Bruno")

fancy.dog.fetch()  # Bruno fetches!
```

---
### **What happens step by step**

- `FancyShelter()` called → no `__init__` found → MRO walks up to `DogShelter.__init__`
- Inside `DogShelter.__init__`, `self.dog_cls` → looks up instance → not found → looks up class → finds `Labrador`
- `Labrador("Bruno")` created at runtime — constructor determined dynamically

---
###### Gotcha

- Runtime constructor resolution depends on MRO — always check `__mro__` if behaviour is unexpected
- `self.dog_cls` is looked up on `self` — so subclass override always wins

---
