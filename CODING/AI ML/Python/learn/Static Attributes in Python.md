# Static (Class) Attributes
- A static attribute (sometimes called a class attribute) is an attribute that belongs to the class itself, not to any specific instance of the class.
- Shared across all instances of that class.

``` python
class User:
	user_count = 0

	def __init__(self, username, email):
		self.username = username # instance attribute
		self.email = email # instance attribute
		User.user_count += 1 # static attribute

	def display_user(self):
		print(f"Username: {self.username}, Email: {self.email}")

user1 = User("anish", "anish@gmail.com")
user2 = User("bala", "bala@gmail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)
```

Output:
``` bash
2
2
2
```

---
