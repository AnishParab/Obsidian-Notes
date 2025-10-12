# What is Routing
- _Routing_ refers to determining how an application responds to a client request to a particular endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).

---
# Structure of a Route
``` js
app.METHOD(PATH, HANDLER)
```
- `app` is an instance of `express`.
- `METHOD` is an [HTTP request method](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods), in lowercase.
- `PATH` is a path on the server.
- `HANDLER` is the function executed when the route is matched.

---
# Respond with `Hello World!` on the homepage:

``` js
app.get('/', (req, res) => {
  res.send('Hello World!')
})
```

---
# Respond to POST request on the root route (`/`), the application’s home page:

``` js
app.post('/', (req, res) => {
  res.send('Got a POST request')
})
```

---
# Respond to a PUT request to the `/user` route:

``` js
app.put('/user', (req, res) => {
  res.send('Got a PUT request at /user')
})
```

---
# Respond to a DELETE request to the `/user` route:

``` js
app.delete('/user', (req, res) => {
  res.send('Got a DELETE request at /user')
})
```

---
