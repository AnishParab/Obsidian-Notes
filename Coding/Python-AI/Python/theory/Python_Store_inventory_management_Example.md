# Problem Statement
**Managing Store Inventory**
You’re managing product categories for a retail store. Your task is to identify:
- Which products are available in which branches
- What products are common
- What products are missing in each branch
- And which products should not be altered using frozenset

**Tasks:**
- Create a set branch_a_products with the items: "bread", "milk", "butter", "jam"
- Create another set branch_b_products with the items: "bread", "cheese", "butter", "ketchup"
- Print both sets.
- Find and print the union of both branches’ products.
- Find and print the intersection of both branches’ products.
- Find and print the products that are in branch_a_products but not in branch_b_products.
- Check whether "ketchup" is available in branch_a_products and print the result.
- Define a frozenset called essential_items with values: "milk", "bread", "ketchup".
- Print the frozenset.

---
# Code
``` python
branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

print(f"A products: {branch_a_products}")
print(f"B products: {branch_b_products}")

union_set = branch_a_products | branch_b_products
print(f"Union: {union_set}")

intersection_set = branch_a_products & branch_b_products
print(f"Intersection: {intersection_set}")

complement_set = branch_a_products - branch_b_products
print(f"Complement: {complement_set}")

print(f"Is 'ketchup' in branch A products? {'ketchup' in branch_a_products}")

essential_items = frozenset({"milk", "bread", "ketchup"})
print(f"Essential items: {essential_items}")
```

---
