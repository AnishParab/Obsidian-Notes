``` python
class Dog:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

	def bark(self):
		print("Whoof Whoof)

dog1 = Dog("Ola", "Indian street Dog")
dog1.bark()
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Doug", "Corgi")
do2.bark()
```

---
# Constructor
`__init__()` is the  _constructor_.

---
# `self`
- It refers to current object _(Instance)_  of class.
- It's like, when `dog1 = Dog(something)`, `self = dog1`.

---

