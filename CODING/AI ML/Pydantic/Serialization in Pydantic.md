# What is Serialization
It is the process of converting an object, data structure, or state into a format that can be stored (in a file or memory buffer) or transmitted (over a network) and reconstructed later.

---
#  Why Serialization?
Serialization is essential for:
1. **Data Persistence**: Storing objects in databases or files.
2. **Communication**: Sending complex data over a network (e.g., in APIs).
3. **Caching**: Saving the state for quick access later.
4. **Inter-process communication** (IPC) or **Remote Procedure Calls** (RPC).

---
# Pydantic Specific
It converts **model** into **JSON or Dict**.

---
# Code
``` python
from pydantic import BaseModel, ConfigDict # type: ignore
from typing import List
from datetime import datetime

class Address(BaseModel):
	street: str
	city: str
	zip_code: str

class User(BaseModel):
	id: int
	name: str
	email: str
	is_active: bool = True
	createdAt: datetime
	address: Address
	tags: List[str] = []

	# Modify any formats
	model_config = ConfigDict(
		json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
	)

# Create a user Instance
user = User(
	id = 1,
	name = "Anish",
	email = "anish@gmail.com",
	created_at = datetime(2024, 3, 15, 14, 30)
	address = Address(
		street = "something",
		city = "Jaipur",
		zip_code = "001144",
	)
	tags = ["premium", "subscriber"],
)

# Using model_dump() -> Dict
python_dict = user.model_dump()
print(python_dict)

print("\n=============================================\n")

# Using model_dump_json() -> JSON
json_str = user.model_dump_json()
print(json_str)
```

---
