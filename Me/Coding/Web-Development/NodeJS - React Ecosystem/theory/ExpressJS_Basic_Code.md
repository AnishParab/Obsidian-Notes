# Code

- Typically, `index.js`
``` js
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello Friend')
})

app.listen(port, () => {
  console.log(`Example app listening on port http://localhost:${port}`)
})
```

---
# Explanation

> This app starts a server and listens on port 3000 for connections. The app responds with “Hello World!” for requests to the root URL (`/`) or _route_. For every other path, it will respond with a **404 Not Found**.

---
