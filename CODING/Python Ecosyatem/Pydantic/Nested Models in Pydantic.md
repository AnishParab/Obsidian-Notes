# Referencing & Forward Referencing
``` python
from typing import List, Optional
from pydantic import BaseModel #type: ignore

class Address(BaseModel):
	street: str
	city: str
	postal_code: str

class User(BaseModel):
	id: int
	name: str
	address: Address # Reference a class

class Comment(BaseModel):
	id: int
	content: str
	replies: Optional[List['Comment']] = None # This is called as self referencing (Forward Referencing)

Comment.model_rebuild() # Necessary for Forward Referencing

address = Address(
	street = "123 something",
	city = "Goa",
	postal_code = "10001",
)

user = User(
	id = 1,
	name: "Anish",
	address = address,
)

comment = Comment(
	id = 1,
	content = "First Comment"
	replies = [
		Comment(id=2, content="Reply 1"),
		Comment(id=3, content="Reply 2")
	]
)
```

---
# Assignment
``` python
from pydantic import BaseModel #type: ignore
from typing import List

# TODO: Create Course model
# Each course has modules
# Each module has lessons

class Lessoni(BaseModel):
	lesson_id: int
	topic: str

class Module(BaseModel):
	module_id: int
	module_name: str
	lessons: List[lesson]

class Course(BaseModel):
	course_id: int
	title: str
	modules: List[Module]
```

---
