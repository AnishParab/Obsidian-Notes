# Python Type Annotations/Hints

> Special Syntax that allow declaring the *type* of a variable.

> By declaring *types* for your variables, editors and tools can give you better support.

---
# Code example

``` python
first_name: str, last_name: str
```

``` python
def get_full_name(first_name: str, last_name: str):
	full_name = first_name.title() + " " + last_name.title()
	return full_name
	
print(get_full_name("john", "doe"))
```

---
# Advantages

> Because the editor knows the types of the variables, you don't only get completion, you also get error checks.

**Example**: Now you know that you have to fix it, convert `age` to a string with `str(age)`:
``` python
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age
```

---
