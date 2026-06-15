# Example 1

``` python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Labrador(Dog):
    pass

d = Labrador()
d.speak()
```

**MRO**
``` bash
Labrador → Dog → Animal → object
```

**Output**
- Finds `speak()` in `Dog` first and stops there
``` bash
Dog barks
```

---
# Example 2

``` python
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")

class C(A):
    def hello(self):
        print("C")

class D(B, C):
    pass

d = D()
d.hello()  # B — why?
```

**MRO**
``` bash
D → B → C → A → object
```

**Output**
- Finds `hello()` in `B` first and stops there
``` bash
B
```

---
###### Gotcha

- Order of parents in definition matters — `D(B, C)` vs `D(C, B)` gives different MRO
- Always check `__mro__` when debugging unexpected method calls

---
