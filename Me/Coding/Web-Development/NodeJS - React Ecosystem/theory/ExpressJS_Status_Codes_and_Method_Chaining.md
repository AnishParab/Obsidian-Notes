# Code

``` js
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

// satus code implementation
app.post('/tweet', (req,res) => {
  res.status(201).send('Tweet Created Success')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```

---
# Basic Method Chaining

```js
res.status(201).send('Created')
```

- `status()` returns `res` → enables chaining.

---
