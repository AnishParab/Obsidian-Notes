# Methods

- A method is a function defined inside a class. Three types exist — each serves a different purpose.
	1. **Instance method**
	2. **Class method**
	3. **Static method**

---
# Quick comparison

| Type     | Decorator       | First arg | Accesses         |
| -------- | --------------- | --------- | ---------------- |
| Instance | none            | `self`    | instance + class |
| Class    | `@classmethod`  | `cls`     | class only       |
| Static   | `@staticmethod` | none      | neither          |

---
# Method with `No Arguments` and `Decorators`

``` python
class Chai:
    def brew():
        print("Brewing chai...")


tea1 = Chai
tea1.brew()   # This works fine but no use

tea2 = Chai()
tea2.brew()   # TypeError: Should take self argument
```

---
### Reason why we need `self`

**When you call `tea2.brew()`:**
- `tea2` is an instance
- Python finds `brew` in `Chai.__dict__`
- Python wraps it as a **bound method** — automatically passes `tea2` as the first argument
- `brew()` has no parameters → `TypeError: brew() takes 0 positional arguments but 1 was given`

**When you call `tea1.brew()`:**
- `tea1` is the class itself — not an instance
- Python finds `brew` directly in `Chai.__dict__`
- No binding happens — called as a plain function
- `brew()` has no parameters, nothing is passed → works fine, but useless

---
