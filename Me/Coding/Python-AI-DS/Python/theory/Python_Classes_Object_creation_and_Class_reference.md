# Classes and Objects

- OOP = paradigm of writing code around objects

> Class = blueprint, Object = **instance** of that class

---
# Creating a Class

> Class Naming Convention: `UpperCamelCase`

``` python
class Chai:
	pass
	
class ChaiTime:
	pass
```

---
# Class reference v/s Object creation

``` python
# Reference to a class - no ()
lemon_tea = Chai
# Similar to:
# print(Chai)

# Object creation - () required
ginger_tea = Chai()
```

---
# Type checks

``` python
type(Chai)                    # <class 'type'> — class is itself an object

type(lemon_tea)               # <class 'type'>

type(ginger_tea)              # <class '__main__.Chai'>

type(ginger_tea) is Chai      # True

type(ginger_tea) is ChaiTime  # False
```

---
