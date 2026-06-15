# Polymorphism

- Same interface, different behaviour depending on the object.

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Duck:
    def speak(self):
        print("Quack!")

animals = [Dog(), Cat(), Duck()]

for animal in animals:
    animal.speak()  # each object responds differently to the same call
```

Output:
```
Woof!
Meow!
Quack!
```

- Same method name `speak()` — different behaviour per object
- Calling code doesn't care what type the object is

---
###### Gotcha

- Python doesn't enforce interface — if `speak()` is missing → `AttributeError` at runtime
- Use `ABC` + `@abstractmethod` to enforce the interface at class definition time

---
