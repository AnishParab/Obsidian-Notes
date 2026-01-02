# Code
``` python
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    # Default value, hence need not be passed on
    in_stock: bool = True


product1 = Product(id=1, name="Laptop", price=999.99)

product2 = Product(id=2, name="Bag", price=24.33, in_stock=True)

product3 = Product(id=2, name="Bag", price=24.33, in_stock=False)

print(product1)
print(product2)
print(product3)
```

---
