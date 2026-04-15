# Attribute Shadowing

``` python
class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)   # Hot

# Namespace Revision
cutting.temperature = "Mild"
print(cutting.temperature)   # Mild
print(Chai.temperature)      # Hot

# del keyword, Attribute Shadowing, Use Fall-back value
del cutting.temperature
print(cutting.temperature)   # Hot and not Mild
```

**Key Points**
- Use `del` keyword for **Attribute Shadowing**.
- It uses the **fallback-value** after using `del`.
- If there is no _fallback-value_, an **AttributeError** occurs.

---
