# Example (Attribute Shadowing)
``` python
class Chai:
	temperature = "hot"
	strength = "Strong"
	
cutting = Chai
print(cutting.temperature)

cutting.temperature = "Mild"
# For cutting object
print("After changing ",cutting.temperature)
# For Class
print("Direct look into the class ", Chai.temperature)

# Fall-back to class property value
del cutting.temperature
print("After del: ", cutting.temperature) # Prints hot instead of mild

cutting.cup = "small"
print("cup size is ", cutting.cup)

# Attribute error since there is no fallback
del cutting.cup
print("cup size after deletion is ", cutting.cup)
```

**Output**:
``` text
hot

After changing Mild
Direct look into the class hot

After del: hot

cup size is small

Attribute error
```

---
