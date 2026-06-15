# Duck Typing

- Python doesn't care about the type — only whether the method exists
- "If it walks like a duck and quacks like a duck, it's a duck"
- No inheritance required — if the method exists, it works

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Robot:
    def speak(self):
        print("Beep boop!")

# Robot has nothing to do with Dog or Cat
# Python only checks if speak() exists at runtime
animals = [Dog(), Cat(), Robot()]
for a in animals:
    a.speak()
# Woof!
# Meow!
# Beep boop!
```

**Why this works**
- Python uses dynamic dispatch — method lookup happens at runtime, not compile time
- No type checking, no interface enforcement — just "does this object have this method?"

---
###### Gotcha

- Method missing → `AttributeError` at runtime — no compile-time safety
- Use `ABC` + `@abstractmethod` to enforce the interface if safety is needed
- `hasattr(obj, "speak")` to check before calling if type is uncertain

---
