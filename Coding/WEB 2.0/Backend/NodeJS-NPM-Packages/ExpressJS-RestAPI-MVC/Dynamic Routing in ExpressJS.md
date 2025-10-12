> Use `:` for dynamic routing.

---
# Syntax
``` js
app.get('/books/:xyz', (req, res) => {
  const id = req.params.xyz;
});
```

---
