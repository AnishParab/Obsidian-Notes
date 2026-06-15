# Multiple Inheritance

- Python allows a class to inherit from more than one parent.

```python
class Swimmer:
    def swim(self):
        print("Swimming!")

class Runner:
    def run(self):
        print("Running!")

class Labrador(Swimmer, Runner):
    pass

d = Labrador()
d.swim()  # Swimming!
d.run()   # Running!
```

---
