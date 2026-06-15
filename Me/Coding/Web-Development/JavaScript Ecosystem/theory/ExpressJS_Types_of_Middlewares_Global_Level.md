# Global Middlewares

- These middlewares run everytime.

---
# Code

``` js
app.use(function (req, res, next) {
	console.log('I am Middleware A')
	next()
})

app.use(function (req, res, next) {
	console.log('I am Middleware B')
	next()
})
```

**Output**:
``` bash
Http server is running on PORT 8000
I am Middleware A
I am Middleware B 
```

---
