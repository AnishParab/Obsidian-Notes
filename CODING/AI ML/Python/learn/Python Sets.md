``` python
# Creating a set
numbers = {1, 2, 3, 4, 5}

# Adding elements
numbers.add(6)

# Removing elements
numbers.remove(3)

# Sets are unordered and do not allow duplicates
numbers.add(6)  # No effect as 6 is already in the set

# Looping through a set
for num in numbers:
    print(num)
```