# Composition via Class Reference

- Composition via class reference = storing the class itself as an attribute, not an instance
- Allows swapping the class at subclass level without touching `__init__`

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} barks!")

class DogShelter:
    dog_cls = Dog  # storing the class itself — not an instance

    def __init__(self):
        self.dog = self.dog_cls("Bruno")  # instance created here

    def show(self):
        self.dog.bark()

shelter = DogShelter()
shelter.show()  # Bruno barks!
```

- `dog_cls` is a class reference — `DogShelter.dog_cls` is `Dog` itself
- `self.dog` is the actual instance — created using that reference

---
# **Swapping via subclass**

```python
class Labrador(Dog):
    def fetch(self):
        print(f"{self.name} fetches!")

class FancyShelter(DogShelter):
    dog_cls = Labrador  # swap — no __init__ needed

fancy = FancyShelter()
fancy.show()          # Bruno barks!
fancy.dog.fetch()     # Bruno fetches!
```

- Override `dog_cls` in subclass — behaviour changes without touching `__init__`

---
