# Why use ?
- Reduces code duplication.
- Split complex tasks.
- Hiding implementation details
- Improve Readability
- Improve Traceability

---
# Code (Reducing Code Duplication)
- You are managing a busy tea stall. You receive many orders and want to print each customer's name along with the type of chai they ordered.
	- Write a function `print_order(name, chai_type)`
	- Call it multiple times for different customers.
``` python
# Parameters are passed here
def print_order(name, chai_type):
	print(f"{name} ordered {chai_type} chai")

# Arguments are passed here
print_order("Aman", "masala")
print_order("Aryan", "ginger")
```

---
# Code (Splitting Complex Tasks)
- You are creating a monthly report for a cafe's sales. Instead of putting all logic in one place, break it down.
	- Write a function `generate_report()` that calls:
		- `fetch_sales()`
		- `filter_valid_orders()`
		- `summarize_data()`
``` python
def fetch_sales():
	print("Fetching the sales data")
	
def filter_valid_sales():
	print("Filtering valid sales")
	
def summarize_data():
	print("Summarizing sales data")

def generate_report():
	fetch_sales()
	filter_valid_sales()
	summarize_data()
	print("Report is ready")
	
generate_report()
```

---
# Code (Hiding Implementation Details)
- You are building a simple app that registers users. You want to separate concerns: getting input, validating it, and saving it.
	- Write `register_user()` that calls:
		- `get_input()`
		- `validate_input()`
		- `save_to_db()`
``` python
def get_input():
	print("Getting user input")
	
def validate_input():
	print("Validating the user info")

def save_to_db():
	print("Saving data to database")
	
def register_user():
	get_input()
	validate_input()
	save_to_db()
	print("User registration complete")
	
register_user()
```

---
# Code (Improve Readability)
- You sell different chai sizes. Instead of writing formulas everywhere, create a function.
	- Write `calculate_bill(cups, price_per_cup)`
	- Return total bill.
	- Use this function for multiple orders.
``` python
def calculate_bill(cups, price_per_cup):
	return cups * price_per_cup
	
my_bill = calculate_bill(3, 15)
print(my_bill)

print("Order for table 2: ", calculate_bill(2, 50))
```

---
# Code (Improve Traceability)
- Your shop adds a 10% VAT on every order. You want this to be consistent and traceable.
	- Write `add_vat(price, vat_rate)`
	- Use it to compute final prices for 3 orders.
``` python
def add_vat(price, vat_rate):
	return price * (100 + vat_rate)/100
	
orders = [100, 150, 200]

for price in orders:
	final_amount = add_vat(price, 10)
	print(f"Original: {price}, Final with VAT: {final_amount}")
```

---
