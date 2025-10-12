# Filtering and Sorting Data
#### Request
``` http
GET /users?age=25&sort=name
Host: example.com
```
#### Response
``` http
[
	{
		"id": 3,
		"name": "Saitya"
		"age": 24
	},
	
	{
		"id": 4,
		"name": "Sona",
		"age": 25
	}
]
```

---
# Pagination
#### Request
``` http
GET /users?page=2&limit=10
Host: example.com
```
#### Response
``` http
{
	"total": 50,
	"page": 2,
	"limit": 10,
	"data": [
		// Array of users
	]
}
```
- The query parameters page=2 and limit=10 specify the page number and the number of items per page.

---
