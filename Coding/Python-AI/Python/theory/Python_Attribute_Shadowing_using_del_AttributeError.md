# Attribute Shadowing
``` python
class Chai:
    # Attributes
    temperature = "Hot"
    strength = "Strong"


# Creating a Reference to the class
cutting = Chai()
print(cutting.temperature)

print()

# Checking Namespace
cutting.temperature = "mild"
print("After changing ", cutting.temperature)
print("Direct look into the class ", Chai.temperature)

print()

# del keyword, Attribute Shadowing, Use Fall-back value
del cutting.temperature
print("After deleting ", cutting.temperature)
```

**Output**:
``` text
Hot

After changing  mild
Direct look into the class  Hot

After deleting  Hot
```
### Key Points
- Use `del` keyword for **Attribute Shadowing**.
- It uses the **fallback-value** after using `del`.
- If there is no _fallback-value_, an **AttributeError** occurs.

---
# Attribute Error
- **AttributeError** occurs when there is no **fallback-value**.
``` python
class Chai:
    # Attributes
    temperature = "Hot"
    strength = "Strong"


# Creating a Reference to the class
cutting = Chai()

# Creating a run-time attribute
cutting.cup = "small"
print("Cup size ", cutting.cup)

print()

# del keyword, Attribute Shadowing, No Fall-back value
del cutting.cup
print("After deleting Cup size is ", cutting.cup)
```

**Output**:
``` text
Cup size small

AttributeError: 'Chai' object has no attribute 'cup'
```

---
