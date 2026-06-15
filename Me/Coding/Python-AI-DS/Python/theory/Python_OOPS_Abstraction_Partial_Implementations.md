**Pre-requisite**
[[Python_OOPS_Abstraction]]

---
# Partial Implementation

``` python
class Labrador(Dog):
    def speak(self):
        print("Woof!")
    # fetch not implemented

d = Labrador()  # TypeError — fetch is still abstract
```

---
# Abstract class with concrete methods

``` python
class Dog(ABC):
    @abstractmethod
    def speak(self):
        pass

    def breathe(self):           # concrete method — not abstract
        print("Breathing...")
```

- Abstract class can have both abstract and concrete methods
- Concrete methods are **inherited as-is**

---
###### Gotcha

- `ABC` + `@abstractmethod` both required for enforcement
- Forget either → Python lets you instantiate silently
- Abstract class can have `__init__` — runs when child calls `super().__init__()`

---
