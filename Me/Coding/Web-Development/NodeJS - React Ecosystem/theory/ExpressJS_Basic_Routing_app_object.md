# Routing

- _Routing_ refers to determining how an application responds to a client request to a particular endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).

- Syntax
``` js
app.METHOD(PATH, HANDLER_FUNC)
```

---
# Code

``` js
const express = require('express')
const app = express()
const port = 3000

// home route
app.get('/', (req, res) => {
  res.send('Hello World!')
})

// contact-us route
app.get('/contact-us', (req,res) => {
  res.send('You can contact me at my email address')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```

**Output**:
> `/` -> Home Route
> `/contact-us` -> Contact-us Route

---
