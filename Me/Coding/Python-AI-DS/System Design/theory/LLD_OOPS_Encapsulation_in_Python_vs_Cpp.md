# Encapsulation in Python v/s Cpp

> Same concept, different enforcement — C++ is strict, Python trusts the developer

---
# Access Modifiers

| C++         | Python             |                           |
| ----------- | ------------------ | ------------------------- |
| Public      | `public:` block    | `field` (default)         |
| Protected   | `protected:` block | `_field` (convention)     |
| Private     | `private:` block   | `__field` (name mangling) |
| Enforcement | Compiler error     | Convention only           |

---
# Private field access

- C++: `myCar->currentSpeed = 500` → compile error if `private`
- Python: `my_car.__current_speed = 500` → silently creates a _new_ attribute, doesn't touch the real one
- Python real field: `my_car._SportsCar__current_speed = 500` → works, nothing blocks it

---
# Getters and Setters

| C++           | Python                          |                                    |
| ------------- | ------------------------------- | ---------------------------------- |
| Getter        | `int getSpeed()`                | `@property`                        |
| Setter        | `void setTyreCompany(string v)` | `@field.setter`                    |
| Access syntax | `myCar->getSpeed()`             | `my_car.speed` (like an attribute) |

- Python `@property` is cleaner — caller doesn't know or care if it's a method or field

---
# Constructor

| C++            | Python                          |                                    |
| -------------- | ------------------------------- | ---------------------------------- |
| Definition     | `SportsCar(string b, string m)` | `def __init__(self, brand, model)` |
| Self-reference | `this->field`                   | `self.field`                       |

---
# Destructor

- C++: `~SportsCar()` — must manually clean up, especially with `new`/`delete`
- Python: `__del__` exists but GC handles memory — almost never needed

---
# The core difference

- C++ encapsulation is a hard guarantee — compiler enforces it
- Python encapsulation is a social contract — nothing physically stops violation
- Python philosophy: "we're all consenting adults here"

---
