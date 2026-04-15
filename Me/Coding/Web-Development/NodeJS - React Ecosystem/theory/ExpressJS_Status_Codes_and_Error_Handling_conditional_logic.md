# Conditional Status Logic

```js
app.get('/user/:id', (req, res) => {
  const user = findUser(req.params.id)

  if (!user) {
    return res.status(404).send('User not found')
  }

  res.status(200).json(user)
})
```

**Pattern**
- Early return avoids multiple responses.

---
