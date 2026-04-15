# `index.js`

``` js
const app = require('./app')
const PORT = 3000

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`)
})
```

---
# `app.js`

``` js
const express = require('express')
const booksRoutes = require('./routes/books.routes.js')

const app = express()

app.use(express.json())

app.use('/books', booksRoutes)

module.exports = app
```

---
# Refer :

[[Express_Book_Store_API_Models_Controllers_and_Routes_basic_code]]

---
