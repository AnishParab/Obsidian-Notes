##### This is the python way of `getters` and `setters`.
``` python
class User:
	def __init__(self, username, email, password)
		self.username = username
		self._email = email
		self.password = password

# This is a getter property
	@property
	def email(self):
		return self._email

# This is a setter property
	@email.setter
	def email(self, new_email):
		if "@" in new_email:
			self._email = new_email


user1 = User("anish", "anish@gmail.com", "123")

# Using setter
user1.email = "this is not an email"

# Using getter
print(user1.email)
```

---
