# Encapsulation

- Encapsulation = bundling data + methods together, then controlling access to that data
- Solves two problems:
    - _Organisation:_ data and behaviour live together in one unit
    - _Security:_ not everything inside should be accessible outside

---
# The three tools of encapsulation in Python

### **1. Access modifiers**

- Control who can access what

```python
class Dog:
    def __init__(self, name, age):
        self.name = name        # public
        self._age = age         # protected
        self.__strength = "High" # private
```

---
### **2. Getters and setters via `@property`**

- Controlled read/write access with validation

```python
class Dog:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

d = Dog(3)
print(d.age)  # 3 — getter
d.age = 5     # setter
d.age = -1    # ValueError
```

---
### **3. `__slots__`**

- Restrict which attributes an instance can have

```python
class Dog:
    __slots__ = ['name', 'age']

d = Dog()
d.name = "Bruno"   # works
d.color = "Brown"  # AttributeError
```

---
# Full example

```python
class Dog:
    __slots__ = ['_name', '_age']

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    def describe(self):
        print(f"{self._name} is {self._age} years old")

d = Dog("Bruno", 3)
print(d.name)   # Bruno — getter
print(d.age)    # 3 — getter
d.age = 5       # setter
d.name = "Max"  # AttributeError — no setter
d.color = "Brown"  # AttributeError — not in __slots__
```

---
###### Gotcha

- Python has no true private — convention + `@property` is the closest you get
- `__slots__` + `@property` together give the strongest encapsulation Python can offer natively

---
