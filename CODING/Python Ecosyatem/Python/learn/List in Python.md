``` python
tea_varieties = ["Black", "Green", "Oolong", "White"]

print(tea_varieties)
print(tea_varieties[0])

# Slicing and Dicing
tea_varieties[1:3]

for tea in tea_varieties:
	print(tea)

if "Oolong" in tea_varieties:
	print("I have Oolong tea")

tea_varieties.append("Kawa")
tea_varieties.pop()
tea_varieties.remove("Green")
tea_varieties.insert(1, "Green")

# Single Reference
tea_varieties_copy = tea_varieties
# Separate References
tea_varieties_copy_2 = tea_varieties.copy() 
```

---
# List Comprehension
``` python
squared_nums = [x**2 for x in range(10)]

print(squared_nums)
```

---




