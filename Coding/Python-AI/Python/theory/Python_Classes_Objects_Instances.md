# What is OOPS ?
- It is a paradigm of programming.
- It is a style of writing code.

---
> **NOTE**: Always name your classes like this: `ClassName`

---
# Syntax
``` python
# Class
class Chai:
	pass
	
class ChaiTime:
	pass

# Reference to the Class
print(type(Chai))
# OR
lemon_tea = Chai
print(lemon_tea)

print()

# Object creation, requires `()`
ginger_tea = Chai()

print(type(ginger_tea))

print()

print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
```

**Output**:
``` text
<class 'type'>
<class 'type'>

<class '__main__.Chai'>

True
False
```

---
### Key Point
> In reality, a class is actually an **object**.
> Although the output shows `<class 'type'>`, it is actually an **object**.

---
