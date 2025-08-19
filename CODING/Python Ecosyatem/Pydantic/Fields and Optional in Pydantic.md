# Optional
``` python
from pydantic import BaseModel # type: ignore
from typing import List, Dict, Optional

class Cart(BaseModel):
	user_id: int
	items: List[str]
	quantities: Dict[str, int]

class BlogPost(BaseModel):
	title: str
	content: str
	image_url: Optional[str] = None
```

---
# Fields
``` python
from pydantic import BaseModel, Field # type: ignore
from typing import Optional

# TODO: Create Employee Model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)

class Employee(BaseModel):
	employee_id: int
	employee_name: str = Field(
		..., # This means it is required field
		min_length=3, 
		max_length=50,
		description="Employee Name", # For better error messages
		example="Anish Parab" # How to fill this field
		)
	department: Optional[str] = 'General'
	salary: float = Field(
		...,
		ge=10000 # Greater Then
		)
	
```

---








