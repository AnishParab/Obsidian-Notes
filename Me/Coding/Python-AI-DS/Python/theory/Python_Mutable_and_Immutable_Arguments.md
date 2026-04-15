# Code: Immutable Arguments
``` python
chai = "Ginger chai"

# Parameters 
def prepare_chai(order):
	print("Preparing ", order)

# Arguments
prepare_chai(chai)
# Original value will not change
print(chai)
```

**Output**
``` text
Preparing Ginger chai
Ginger chai
```

---
# Code: Mutable Arguments
``` python
chai = [1,2,3]

print(chai)

def edit_chai(cup):
	cup[1] = 42
	
edit_chai(chai)
print(chai)
```

**Output**
``` text
[1,2,3]
[1,42,3]
[1,42,3]
```

---
