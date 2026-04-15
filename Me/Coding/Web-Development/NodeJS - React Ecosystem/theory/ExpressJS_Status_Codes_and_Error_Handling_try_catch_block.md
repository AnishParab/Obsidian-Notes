# Error Handling Inside Routes

```js
app.post('/tweet', (req, res) => {
  try {
    createTweet()
    res.status(201).send('Tweet Created')
  } catch (err) {
    res.status(500).send('Server Error')
  }
})
```

---
