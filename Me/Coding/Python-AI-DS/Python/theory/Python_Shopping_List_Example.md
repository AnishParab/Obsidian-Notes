# Problem Statement
**Shopping List**
You’re building a shopping list feature in a grocery app. You need to support various list operations such as adding items, removing them, merging with others, and handling user inputs from text.

**Tasks:**
- Create a grocery list named my_cart with the items: "apples", "bananas", and "milk"
- Print the grocery list.
- Add "bread" to the end of the list.
- Print the updated grocery list.
- Insert "ketchup" at the beginning of the list.
- Print the updated grocery list.
- Remove "bananas" from the list.
- Print the updated grocery list.
- Remove the last item from the list and store it in a variable named removed_item.
- Print the value of removed_item.
- Extend the grocery list by adding "rice" and "butter".
- Print the updated grocery list.
- Sort the grocery list in alphabetical order.
- Print the updated grocery list.
- Reverse the order of the grocery list.
- Print the updated grocery list.
- Concatenate the grocery list with another list containing "juice" and "jam".
- Print the resulting list.
- Duplicate the grocery list twice.
- Print the resulting list.
- Define a string with the value "tomato cucumber spinach" and convert it into a list.
- Print the converted list.

---
# Code
``` python
my_cart = ["apples", "bananas", "milk"]
print(f"Grocery list: {my_cart}")

my_cart.append("bread")
print(f"Grocery list: {my_cart}")

my_cart.insert(0, "ketchup")
print(f"Grocery list: {my_cart}")

my_cart.remove("bananas")
print(f"Grocery list: {my_cart}")

removed_item = my_cart.pop()
print(f"Removed item: {removed_item}")

extend_grocery_list = ["rice", "butter"]
my_cart.extend(extend_grocery_list)
print(f"Grocery list: {my_cart}")

my_cart.sort()
print(f"Grocery list: {my_cart}")

my_cart.reverse()
print(f"Grocery list: {my_cart}")

# Concatenate a list
concatenate_list = ["juice", "jam"]
print(f"Grocery list: {my_cart + concatenate_list}")

my_cart = my_cart * 2
print(f"Grocery list: {my_cart}")

# String to list COnversion
conversion = "tomato cucumber spinach"
print(f"{conversion.split()}")
```

---
