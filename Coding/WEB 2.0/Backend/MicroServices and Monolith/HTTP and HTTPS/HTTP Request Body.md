# What ?
- The body of a request is the part that contains the 'body' of information the request is transferring.
- The body of an HTTP request contains any information being submitted to the web server, such as a username and password, or any other data entered into a form.

---
> A `GET` request usually has no body, while `POST`, `PUT`, or `PATCH` requests almost always do.

---
# Content-Type
- The **Content-Type** header in the request tells the server how to interpret the body (e.g. `application/json`, `multipart/form-data`, `text/plain`).

---
# Example : Sending JSON data in a POST request
``` http
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 48

{
  "username": "asp",
  "password": "secret123"
}
```

---
# Example : Form Submission
``` http
POST /signup HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 43

username=asp&email=asp%40mail.com&age=25
```

---
