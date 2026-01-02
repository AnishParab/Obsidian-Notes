# Code
``` python
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


# Model compositin: User contains a reference of Address model
# Hierarchical Data Structure
class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(street="123 something", city="Jaipur", postal_code="100001")

user = User(id=1, name="Anish", address=address)

user_data = {
    "id": 1,
    "name": "Anish",
    "address": {"street": "321 something", "city": "Goa", "postal_code": "403401"},
}

user2 = User(**user_data)

print(user)

print()

print(user2)
```

---
