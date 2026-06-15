**Refer this example**
[[Python_OOPS_MRO]]

---
# `super()` with multiple inheritance

- `super()` follows MRO — not just the direct parent

```python
class Dog(Animal):
    def speak(self):
        super().speak()  # calls next in MRO — not necessarily Animal directly
        print("Dog barks")
```

---
###### Gotcha

- `super()` in multiple inheritance chains can be tricky — every class in chain should use `super()`

---
