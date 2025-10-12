# Code
``` js
app.use('/books', (req, res, next) => {
  console.log('Middleware 1 for /books');
  next();
});

app.use('/books', (req, res, next) => {
  console.log('Middleware 2 for /books');
  next();
});

app.get('/books', (req, res) => {
  res.send('Final handler for /books');
});

```

#### Output:
``` bash
Middleware 1 for /books
Middleware 2 for /books
Final handler for /books
```

---
# Code
``` js
app.use('/books', (req, res, next) => {
  console.log('Only middleware for /books');
  next();
});
```

#### Output:
``` bash
Only middleware for /books
```

> …and then the client gets a **404 response** because nothing else matched after `next()`.

---
# Hence
That’s why a path-level middleware almost always either:
- Ends the cycle with a response (`res.send()`, `res.json()`, etc.), or
- Forwards control to a **downstream route handler**.

---
