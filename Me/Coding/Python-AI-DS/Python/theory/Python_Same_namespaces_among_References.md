# Same namespaces for references

``` python
class Chai:
    origin = "India"

Chai.is_hot = False
masala = Chai

print(masala.is_hot)  # False
print(Chai.is_hot)    # False                                

masala.is_wet = True

print(masala.is_wet)  # True
print(Chai.is_wet)    # Also True which it adds to Chai also

masala.is_hot = True
print(masala.is_hot)  # True
print(Chai.is_hot)    # Also True and hence no divergence

masala.origin = "USA"
print(masala.origin)  # USA
print(Chai.origin)    # Also USA
```

> Hence, `Chai` and `masala` are the same **namespaces (blueprints)**.

> This means `masala` just points to `Chai`.

---
