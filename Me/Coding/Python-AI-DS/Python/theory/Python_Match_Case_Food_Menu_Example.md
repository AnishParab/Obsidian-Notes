# Problem Statement
**Food Menu Selector**
- You’re creating a menu price lookup system for a digital food ordering app using the match-case statement.  

**Tasks:**
1. Define a function get_item_price that takes a string input item.
2. Use match-case to return the following based on the item name:
    - "pizza" → "Price: 30 bucks"
    - "burger" → "Price: 15 bucks"
    - "pasta" → "Price: 20 bucks"
    - "salad" → "Price: 10 bucks"
    - Any other item → "Item not available"
3. Make sure the item check is **case-insensitive** (e.g., “BURGER” or “burger” should both match).

---
# Code
``` python
def get_item_price(item: str):
    match item:
        case "pizza":
            print("Price is 30 bucks")
        case "burger":
            print("Price is 15 bucks")
        case "pasta":
            print("Price is 20 bucks")
        case "salad":
            print("Price is 10 bucks")
        case _:
            print("Item not available")


item = input("Enter your preferred item (pizza/burger/pasta/salad).\n").lower()

get_item_price(item)
```

---
