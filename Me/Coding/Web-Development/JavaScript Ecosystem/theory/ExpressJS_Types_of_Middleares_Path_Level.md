# Code

- Always runs if the path matches regardless of the type of request (GET, POST, etc).

``` js
app.use('/books', (req, res, next) => {})
```

---
