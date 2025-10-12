# GET Request
``` js
app.get('/', (req,res) => {
	res.send("Get Request")
});
```

---
# POST Request
``` js
app.post('/items', (req,res) => {
	res.send("Post Request")
});
```

---
# PUT Request
``` js
app.put('/items:id', (req,res) => {
	res.send("Put Request")
});
```

---
# DELETE Request
``` js
app.delete('/items:id', (req,res) => {
	res.send("Delete Request")
});
```

---
