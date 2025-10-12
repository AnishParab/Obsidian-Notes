- Tuples are **mutable**.

---
# Code 1
``` python
masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")
```

---
# Code 2
``` python
ginger_ratio, cardamom_ration = 2, 1

print(f"Ratio is G: {ginger_ratio} and C: {cardamom_ratio})
```

### Swap the variables
``` python
ginger_ratio, cardamon_ration = cardamom_ratio, ginger_ratio
```

---
# Membership
- Checking the availability using the keyword `in`.
``` python
print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")

print(f"Is cinnamom in masala spices ? {'cinnamom' in masala_spices}")

print(f"Is Cinnamom in masala spices ? {'Cinnamom' in masala_spices}")
```

#### Output:
``` bash
False
True
False
```

---
