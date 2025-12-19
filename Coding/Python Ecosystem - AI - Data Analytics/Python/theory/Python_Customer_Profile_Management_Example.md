# Problem Statement
**Customer Profile Management**
You are building a customer profile manager for a CRM (Customer Relationship Management) system. You need to store and manipulate customer data using Python dictionaries.

**Tasks:**
- Create a dictionary named customer with the following fields:
    - "name": "John Doe"
    - "age": 32
    - "city": "New York"
- Print the dictionary.
- Add "email" and "phone" to the dictionary.
- Print the updated dictionary.
- Print the customer’s "name" and "city" values.
- Check whether the key "email" exists in the dictionary and print the result.
- Delete the "age" field from the dictionary.
- Print the updated dictionary.
- Print all dictionary keys, values, and items.
- Remove and print the last inserted key-value pair.
- Use .get() to access the key "membership" (which doesn’t exist).
- Print the result.
- Update the dictionary with a new field "address" set to "221B Baker Street".
- Print the final dictionary.

---
# Code
``` python
customer = {"name": "John Doe", "age": 32, "city": "New York"}

print(f"Customer: {customer}")

customer["email"] = "jd@gmail.com"
customer["phone"] = "6969696969"

print(f"Customer: {customer}")

print(f"Customer name: {customer['name']}")
print(f"Customer city: {customer['city']}")

print(f"Is 'email' in customer? {'email' in customer}")

del customer["age"]
print(f"Customer: {customer}")

print(f"Keys: {customer.keys()}")
print(f"Values: {customer.values()}")
print(f"Items: {customer.items()}")

last_item = customer.popitem()
print(f"{last_item} was popped.")
print(f"Hence Customer: {customer}")

membership = customer.get("membership", "No membership")
print(f"{membership}")

customer["address"] = "221B Baker Street"
print(f"Customer: {customer}")
```

---
