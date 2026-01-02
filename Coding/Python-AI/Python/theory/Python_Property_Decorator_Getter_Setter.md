# Getter and Setter
- **Getters and setters** are methods used to **control access to an object’s internal data** while keeping attribute-style access.
### Getter
A **getter** retrieves the value of an internal attribute.
- Implemented using `@property`
- Called **implicitly** when the attribute is accessed
- Can compute or modify the returned value
### Setter
A **setter** updates the internal attribute.
- Defined using `@<property>.setter`
- Called **implicitly** when assigning to the attribute
- Commonly used for validation or constraints

---
# Code
``` python
class TeaLeaf:
    def __init__(self, age):
        # Conventionally treated as "internal" attribute (not truly private)
        self._age = age

    # Property getter: accessed like an attribute, not a method
    @property
    def age(self):
        # Computed / controlled access to internal state
        return self._age + 2

    # Property setter: validates before updating internal state
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")


leaf = TeaLeaf(2)

# Accessing the property (getter is called implicitly)
print(leaf.age)

# Updating the property (setter is called implicitly)
leaf.age = 4
print(leaf.age)

# Invalid update triggers validation error
leaf.age = 6
print(leaf.age)
```

**Output**:
``` text
4
6
ValueError
```

---
