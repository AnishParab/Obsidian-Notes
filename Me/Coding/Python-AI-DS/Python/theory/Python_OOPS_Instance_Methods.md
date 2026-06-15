# Instance Methods

- Most common.
- Receives `self` - has access to instance and class data
- No decorators

> `self` gives access to both instance `__dict__` and class `__dict__`

``` python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Bruno")
d.bark()  # Bruno says Woof!
```

---
**Under the Hood**
``` python
d.bark()            # syntactic sugar
Dog.bark(d)         # what Python actually does — passes d as self
```

---
# NOTE: Instance methods can modify state

``` python
class Dog:
    def __init__(self, name):
        self.name = name
        self.is_sitting = False

    def sit(self):
        self.is_sitting = True
        print(f"{self.name} is now sitting")

    def stand(self):
        self.is_sitting = False
        print(f"{self.name} is now standing")

d = Dog("Bruno")
d.sit()    # Bruno is now sitting
d.stand()  # Bruno is now standing
```

---
