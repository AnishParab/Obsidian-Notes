# Accessing Base Class
- **Code Duplication**
- **Explicit call**
- **super()**

---
# Code Duplication
``` python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


class GingerChai(Chai):
    # Code Duplication
    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level
```

---
# Explicit call
``` python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# Code Duplication
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# --- OR ---


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # Explicit call
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level
```

---
# `super()` **(Usual Method)**
``` python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# Code Duplication
# class GingerChai(Chai):
#     # Code Duplication
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level


# --- OR ---


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # super()
        super().__init__(type_, strength)
        self.spice_level = spice_level
```

---
