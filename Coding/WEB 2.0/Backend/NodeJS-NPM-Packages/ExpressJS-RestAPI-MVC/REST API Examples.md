# Getting User Information
#### Request
``` http
GET /users/{id}
Host: example.com
```
#### Response
``` json
{
	"id": 1,
	"name": "Saitej",
	"email": "saitej@gmail.com"
}
```

---
# Creating New User
#### Request
``` http
POST /users
Host: example.com
Content-Type: application/json

{
	"name": "Anish",
	"email": "anish@gmail.com"
}
```
#### Response
``` http
{
	"id": 2,
	"name": "Anish",
	"email": "anish@gmail.com"
}
```

---
# Updating User Information
#### Request
``` http
PUT /users/{id}
Host: example.com
Content-Type: application/json

{
	"name": "Sona",
	"email": "sona@gmail.com"
}
```
#### Response
``` http
{
	"id": 2,
	"name": "Sona",
	"email": "sona@gmail.com"
}
```

---
# Deleting a User
#### Request
``` http
DELETE /users/{id}
Host: example.com
```
#### Response
``` http
{
	"message": "User deleted successfully"
}
```

---
