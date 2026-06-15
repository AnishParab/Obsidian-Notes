# When to use which

|              | Inheritance   | Composition                |
| ------------ | ------------- | -------------------------- |
| Relationship | is-a          | has-a                      |
| Coupling     | Tight         | Loose                      |
| Flexibility  | Less          | More                       |
| Reusability  | Via hierarchy | Via plugging in components |

---
# Why composition is often preferred

- Inheritance creates tight coupling — change in parent breaks child
- Composition is modular — swap components without touching the rest

```python
class ElectricEngine:
    def start(self):
        print("Electric engine started silently!")

class Car:
    def __init__(self, engine):  # inject engine — loose coupling
        self.engine = engine

c1 = Car(Engine())
c2 = Car(ElectricEngine())

c1.start()  # Engine started!
c2.start()  # Electric engine started silently!
```

---
###### Gotcha

- Don't use inheritance just for code reuse — use it only for genuine is-a relationships
- Favour composition over inheritance — standard principle in LLD and design patterns

---
