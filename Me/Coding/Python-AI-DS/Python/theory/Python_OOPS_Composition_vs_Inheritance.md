**Pre-requisites**
[[LLD_UML_Structural_Diagrams_Class_Diagram]]

---
# Composition v/s Inheritance

Two ways to build relationships between classes.

---
# Inheritance — **is-a relationship**

- `Labrador` is-a `Dog`
- Child gets everything from parent

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

class Labrador(Dog):
    def fetch(self):
        print(f"{self.name} fetches the ball!")
```

---
# Composition — **has-a relationship**

- `Dog` has-a `Engine` → wrong
- `Car` has-a `Engine` → correct
- One class contains another class as an attribute

```python
class Engine:
    def start(self):
        print("Engine started!")

    def stop(self):
        print("Engine stopped!")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def start(self):
        self.engine.start()

c = Car()
c.start()  # Engine started!
```

---
