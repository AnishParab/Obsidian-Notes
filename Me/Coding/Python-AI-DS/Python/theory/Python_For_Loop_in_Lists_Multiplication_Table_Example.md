# Problem Statement
**Generate Multiplication Table**
- You are developing a feature in an educational app that displays multiplication tables.  

**Tasks:**
1. Write a function named multiplication_table that takes a single integer argument number.
2. Using a for loop and range(), generate the multiplication table for number from 1 to 10.
3. Return a **list of strings** in the following format:
    "number x i = result"
    (Example: "3 x 4 = 12")

---
# Code
``` python
def multiplication_table(number: int):
    table = []
    for i in range(1, 11):
        result = number * i
        table.append(f"{number} * {i} = {result}")
    return table


number = input("Enter the number you want a multiplication table for.\n")
number = int(number)

table = multiplication_table(number)
print(table)
```

---
