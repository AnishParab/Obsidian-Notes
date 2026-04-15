# Attribute Error

> **AttributeError** occurs when there is no **fallback-value**.

``` python
class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()

cutting.cup = "Small"
print(cutting.cup)   # Small

# del keyword, Attribute Shadowing, No Fall-back value
del cutting.cup
print(cutting.cup)   # AttributeError: Chai object has no attribute cup
```

---
