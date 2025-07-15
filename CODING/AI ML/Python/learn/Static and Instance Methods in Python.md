# Instance Methods
- The default method in Python.
- Uses `self` as first argument.
- Instance needed.

---
# Static Methods
- Doesn't take `self` or `cls` as the _first argument_.
- Use `@staticmethod` as decorator.
- No instance needed.

``` python
class BankAccount:
	MIN_BALANCE = 100

# Instance Method
	def __init__(self, owner, balance=0):
		self.owner = owner
		self._balance = balance

# Instance Method
	def deposit(self, amount):
		if amount>0:
			self._balance += amount
			print(f"{self.owner}'s new balance: ${self.balance}")
		else:
			print("Deposit amount must be positive.")

# Static method
	@staticmethod
	def is_valid_interest_rate(rate):
		return 0<= rate <=5

account = BankAccount("Alice", 500)
account.deposit(200)

# Using Static Method
# No instance needed for static methods
print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))
```

---
