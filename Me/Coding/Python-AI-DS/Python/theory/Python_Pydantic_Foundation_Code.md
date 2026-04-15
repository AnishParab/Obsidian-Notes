# Code: Pydantic

> We get automatic validations now.
	- For example: If `101` passed as string will be converted to `int`.

``` python
from pydantic import BaseModel


class User(BaseModel):
	# Type Annotations
    id: int
    name: str
    is_active: bool


input_data = {"id": 101, "name": "ChaiCode", "is_active": True}

# Model Initiation
# Unpacking the dictionary so that it won't be used as one value
user = User(**input_data)

print(user)
```

---
