``` python
from pydantic import BaseModel, field_validator, model_validator, computed_field # type: validator

class User(BaseModel):
	username: str

	@field_validator('username')
	# cls is whole class, v is value which is username
	def username_length(cls, v):
		if len(v) < 4:
			raise ValueError("Username must be at least 4 characters")
		return v

class SignupData(BaseModel):
	password: str
	confirm_password: str

	# after makes sure everything runs after custom validations
	
	@model_validator(mode='after') 
	def password_match(cls, values):
		if values.password != values.confirm_password:
			raise ValueError("password do not match")
		return values

class Product(BaseModel):
	price: float
	quantity: int

	@computed_field
	@property
	def total_price(self) -> float:
		return self.price * self.quantity
```

---
# Assignment
``` python
from pydantic import BaseModel, Field, computed_field # type: ignore

# TODO: Create Booking Model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also add computed field: total_amount = nights * rate_per_night

class Booking(BaseModel):
	user_id: int
	room_id: int
	nights: int = Field(
		...
		ge=1	
		)
	rate_per_night: float

	@computed_field
	@property
	def total_amount(self) -> float
		return self.nights * self.rate_per_night
```

---









