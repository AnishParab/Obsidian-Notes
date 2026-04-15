# Self Arguments: Implicit, Explicit Passing and **Missing Self**

``` python
class Chaicup:
	size = 150 # ml

	def describe(self):
		return f"A {self.size}ml chai cup"

cup = Chaicup()
print(cup.describe()) # Implicitly passes cup as self

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two)) # Explicitly passing instance as self

print(Chaicup.describe()) # Missing self
```

**Output**:
``` text
A 150ml cup of chai

A 100ml cup of chai

TypeError: Chaicup.describe() missing 1 required positional argument: 'self'
```

---
# Explanation:

* `self` refers to the instance on which a method is called.
* `cup.describe()` is equivalent to `Chaicup.describe(cup)`.
* When calling `describe()` without any instance, Python raises an error because `self` is not provided.

> Hence **Objects** can run **methods** only when *self* is passed.
> And
> **References** can run **methods** without *self*.

---
# For Objects to Run Methods *without*  `self`

- Refer this:
[[Python_staticmethod_Decorator]]

---
