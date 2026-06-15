# JSON Responses

```js
const express = require('express')
const app = express()

app.post('/books', (req,res) => {
	const { title, author } = req.body
	
	return res.status(200).json({ message: 'Book created success' })
})

app.use(express.json())
```

- Automatically sets `Content-Type: application/json`.

---
