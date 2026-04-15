# Problem Statement

> Simple Bill Splitter

Write a python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
- Total bill: Rs 1200
- People: Aman, Aryan, Akanksha
- Each person owes: Rs 400

Final output:
- Aman owes Rs 400
- Neha owes Rs 400
- Ravi owes Rs 400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box

---
# Code

``` python
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

num_people = int(input("How many people are there in the group?\n"))

names = []

for i in range(num_people):
    name = input(f"Enter the name of person #{i+1}\n").strip()
    names.append(name)

total_bill = get_float("Enter the bill amount in number only.\n")

share = round(total_bill / num_people, 2)

print("\n" + "*" * 40)
print(f"Total bill: {total_bill}")
print(f"Each person owes {share}")

for name in names:
    print(f"{name} owes {share} rupees")

print("\n" + "*" * 40)
```

---
