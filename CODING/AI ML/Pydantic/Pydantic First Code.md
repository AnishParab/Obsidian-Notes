# First Model
``` python
from pydantic import BaseModel # type: ignore

class User(BaseModel):
	id: int
	name: str
	is_active: bool

input_data = {'id': 101, 'name': "ChaiCode", 'is_active': True}

user = User(**input_data)
print(user)
```

---
# Assignment
``` python
from pydantic import BaseModel

# TODO: Create product model with id, name, price, in_stock

class Product(BaseModel):
	id : int
	name : str
	price: float
	in_stock: bool = True  # Default value
```

---
