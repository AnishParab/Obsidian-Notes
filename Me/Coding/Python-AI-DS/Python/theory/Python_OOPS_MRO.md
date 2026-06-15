# MRO (Multiple Resolution Order)

- **Method Resolution Order (MRO)** defines the **order in which Python searches for methods and attributes** in a class hierarchy, especially when **multiple inheritance** is involved.
- In multiple inheritance, the same method may appear in more than one parent class.  
- MRO provides a **deterministic and consistent rule** to decide **which implementation is used**.

> Python follows a strict left-to-right, depth-first order — C3 linearization algorithm
> Determines which method gets called when multiple parents define the same method

---
# **The Diamond problem**

![[mro.excalidraw|300]]

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class DogCat(Dog, Cat):  # inherits from both
    pass

d = DogCat()
d.speak()  # Which speak() gets called?
```

**Python follows MRO**
``` bash
Labrador → Dog → Animal → object
```

**Checking MRO**
```python
print(DogCat.__mro__)
# (<class 'DogCat'>, <class 'Dog'>, <class 'Cat'>, <class 'Animal'>, <class 'object'>)

d.speak()  # Dog barks — Dog comes before Cat in MRO
```

**Hence**
```python
DogCat.__mro__        # tuple
DogCat.mro()          # list
```

---
###### Gotcha

- Order of parents in class definition matters — `DogCat(Dog, Cat)` vs `DogCat(Cat, Dog)` gives different MRO
- Always check `__mro__` when debugging unexpected method calls

---
