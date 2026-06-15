# Class Creation Internals

- When Python sees a `class` block, it goes through 3 steps internally

**Example class**
```python
class Dog:
    species = "Canis lupus"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} barks!")
```

---
# Step 1 — Collect the namespace

- Python executes the class body as a block of code
- Everything defined inside gets collected into a dictionary

**proof**
``` python
print(Dog.__dict__)
```
**Output**
```python
{
    "species": "Canis lupus",
    "__init__": <function>,
    "bark": <function>
}
```

---
# Step 2 — Call `type()`

- Python calls `type(name, bases, namespace)` to create the class object

- These two are equivalent:
```python
# Normal syntax
class Dog:
    species = "Canis lupus"
    def bark(self): print("Woof")

# What Python does internally
def bark(self): print("Woof")
Dog = type("Dog", (object,), {"species": "Canis lupus", "bark": bark})
```

- `bases` determines inheritance — `type()` uses it to build MRO
```python
Animal = type("Animal", (), {})
Dog = type("Dog", (Animal,), {})
issubclass(Dog, Animal)  # True
```

---
# Step 3 — Bind the name

- Result of `type()` assigned to `Dog` in current scope

**Instance creation:**
```python
d = Dog("Bruno")

print(d.__dict__)
```
**Output:**
``` bash
{'name': 'Bruno'}
```

Now,
```
Global Namespace
┌─────────┐
│ Dog ────┼──► <class Dog>
└─────────┘
```
- You're not calling `__init__` directly — you're calling the class object
- `Dog.__call__("Bruno")` is triggered internally
```
Dog("Bruno")
     │
     ▼
Dog.__call__()
     │
     ├──► Dog.__new__(Dog)   — allocates memory, creates empty instance
     │         │
     │         ▼
     │    obj.__dict__ = {}  — empty, no attributes yet
     │
     └──► Dog.__init__(obj, "Bruno")
               │
               ▼
          obj.__dict__ = {'name': 'Bruno'}
               │
               ▼
               d
```

---
### **Method lookup — `d.bark()`**

```
d.bark()
   │
   ▼
Step 1: look in d.__dict__     → bark not found
   │
   ▼
Step 2: look in Dog.__dict__   → bark found as plain function
   │
   ▼
Step 3: descriptor protocol wraps it as bound method
        bark.__get__(d, Dog)
   │
   ▼
bound_bark() = Dog.bark(d)     → d passed as self automatically
```

---
# Complete mental model

```
type  → creates → classes
class → creates → instances
functions → become bound methods when accessed through instances
```

```
Class Definition
      │
      ▼
namespace dict collected
      │
      ▼
type(name, bases, namespace)
      │
      ▼
<class Dog> created
      │
      ▼
Dog("Bruno") called
      │
      ▼
Dog.__call__()
      │
      ├──► __new__()  → empty instance
      └──► __init__() → populated instance
                │
                ▼
                d
```

---
