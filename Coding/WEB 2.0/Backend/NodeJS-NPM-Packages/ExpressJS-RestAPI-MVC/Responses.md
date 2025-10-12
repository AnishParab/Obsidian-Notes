# `sendFile` Request
``` js
app.get('/', (req,res) => {
	res.sendFile('./dummy.html',
	{root:__dirname});
});
```

---
# `json` Request
``` js
app.post('/', (req,res) => {
	res.json({x:1, y:2, z:3})
})
```

---
