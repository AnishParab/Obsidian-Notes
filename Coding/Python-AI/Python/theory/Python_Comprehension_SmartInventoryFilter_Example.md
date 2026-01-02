# Problem Statement
**Smart Inventory Filter**
- You are building a **Smart Inventory Filter** for a retail store.  

**Tasks:**
1. Process a list of product dictionaries, where each product has name, price, and category.
2. Use different types of comprehensions to:
    - Extract names of products priced below ₹500 using **list comprehension**.
    - Extract all **unique categories** using **set comprehension**.
    - Create a **name-to-price mapping** using **dictionary comprehension**.
    - Generate a list of **discounted prices** using a **generator expression** and convert it to a list.
3. Return all four outputs as a tuple.

---
# Code
``` python
"""
items: A list of dictionaries, each representing a product with keys:
    - "name": str
    - "price": int
    - "category": str

Returns:
    - List of names of affordable products (price < 500)
    - Set of unique categories
    - Dictionary of product name to price mapping
    - Generator expression converted to list of prices after applying 10% discount
"""


def filter_inventory():
    items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]

    # List comprehension
    affordable_products = [item["name"] for item in items if item["price"] < 500]
    print("Affordable products are ", affordable_products)

    # Set comprehension
    unique_categories = {item["category"] for item in items}
    print("Unique catgories ", unique_categories)

    # Dictionary comprehension
    products_and_prices = {item["name"]: item["price"] for item in items}
    print("Product and its price ", products_and_prices)

    # Generator comprehension
    # 10% discount
    discounted_prices = list(map(int, (item["price"] * 0.9 for item in items)))
    print("Discounted prices ", discounted_prices)


filter_inventory()
```

---
