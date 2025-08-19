# Previous Code
``` js
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
	res.send("Get Request")
});

app.post('/items', (req, res) => {
	res.json({ x: 1, y: 2, z: 3 })
});

app.put('/items/:id', (req, res) => {
	res.send("Put Request")
});

app.delete('/items/:id', (req, res) => {
	res.send("Delete Request")
});

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`)
})
```

---
# Above code using **Chaining**
``` js
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
	res.send("Get Request")
}).post('/items', (req, res) => {
	res.json({ x: 1, y: 2, z: 3 })
}).put('/items/:id', (req, res) => {
	res.send("Put Request")
}).delete('/items/:id', (req, res) => {
	res.send("Delete Request")
});

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`)
})
```

---
