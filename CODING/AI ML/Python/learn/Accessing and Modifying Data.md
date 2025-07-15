# Traditional Approach
##### Make the data private and use getters and setters.
This allows to modify and access the data in a controlled way.
``` python
class User:
	def __init__(self, username, email, password):
		self.username = username
		self._email = email # protected
		self.password = password

# This is a getter
	def get_email(self):
		return self._email

# This is a setter
	def set_email(self, new_email):
		self._email = new_email

	def clean_email(self):
		return self._email.lower().strip()

user1 = User("Anish", "anishparab3.25@gmail.com", "hello_world")

# Don't do this
# print(user1._email)

# using getter
print(user1.get_email())

# using setter
user1.set_email("hellothere@gmail.com")

print(user1.clean_email())
```
##### Programmers should follow the _Consenting Adults_ philosophy.

---
