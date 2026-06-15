# Polymorphism with inheritance

```python
class Dog:
    def speak(self):
        print("Woof!")

class Labrador(Dog):
    def speak(self):
        print("Woof Woof!")  # overrides parent

class GoldenRetriever(Dog):
    def speak(self):
        print("Bark!")

dogs = [Dog(), Labrador(), GoldenRetriever()]

for dog in dogs:
    dog.speak()
# Woof!
# Woof Woof!
# Bark!
```

---
