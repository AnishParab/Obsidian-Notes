- In lists, indexes are your keys.
- In dictionary, you give your custom keys.

---
# Methods
``` python
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

chai_types["Masala"]
chai_types["Gingery"]

chai_types["Green"] = "Fresh"

for chai in chai_types:
	print(chai, chai_types[chai])

for key, value in chai_types.items():
	print(key, value)

if "Masala" in chai_types:
	print("I have masala")

print(len(chai_types))

chai_types["Earl Grey": "Citrus"]

chai_types.pop("Ginger")

chai_types.popitem()

del chai_types["Green"]

chai_types_copy = chai_types.copy()
```

---
# Nested
``` python
tea_shop = {
"chai": {"Masala": "Spicy", "Ginger": "Zesty"},
"Tea" : {"Green": "Mild", "Black": "Strong"},
}
```

---
# Comprehension
``` python
squared_num = {x:x**2 for x in range(6)}

print(squared_num)
```

---








