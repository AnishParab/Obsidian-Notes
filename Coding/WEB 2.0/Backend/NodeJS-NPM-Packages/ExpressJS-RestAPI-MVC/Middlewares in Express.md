# Code
``` js
app.use((req,res,next) => {
	console.log('I am a middleware');
	next();
});
```

---
- `next()` ---> This calls the next middleware or else its halts the code.

---
