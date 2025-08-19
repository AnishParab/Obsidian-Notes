# Operator Overloading
``` txt
>>> 'chai' + 'code'
>>> 'chaicode'
```

---
# String Slicing
``` python
name = "Anish"

# name[stating_index(inclusive) : End_index(exclusive) : hop]
name[0:4:2]
```

---
# String Methods
``` python
chai = "Masala Chai"

# Lower Case
print(chai.lower())

# Upper Case
print(chai.upper())

name = "    Anish"
# Strip 
print(name.strip())

# Replace
print(chai.replace("Masala", "Lemon"))

address = "Kurtarkar, Nagari, Santa, Cruz"
# Split and retrun a List
print(address.split(", "))
# Find something
print(address.find("Santa"))
print(address.find("Ponda"))

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))

# Join a list as a String
chai_variety = ["Lemon", "Masala", "Ginger"]
print("".join(chai_variety))

# Length of a String
print(len(chai))

# Print Charaters
for letter in chai:
	print(letter)

chai = "He said, \"Masala chai is awesome\" "
# Use raw string instead
chai = r"Masala\nChai"
print(chai)

# Is Keyword Present?
chai = "Masala Chai"
print("Masala" in chai)
```

---







