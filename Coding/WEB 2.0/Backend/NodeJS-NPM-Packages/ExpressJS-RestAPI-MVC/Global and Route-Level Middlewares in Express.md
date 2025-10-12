# Global Middlewares
``` js
// Middlewares
app.use(express.json());

// Middleware to log into a file
app.use(function(req, res, next) {
  const log = `[${Date.now()}] ${req.method} ${req.path}`;
  fs.appendFileSync('logs.txt', log, 'utf-8');
  next();
});
```

---
# Route-Level Middlewares
``` js
function loggerMiddleware(req, res, next) {
  const log = `[${Date.now()}] ${req.method} ${req.path}`;
  fs.appendFileSync('logs.txt', log, 'utf-8');
  next();
};

function customMiddleware(req, res, next) {
  console.log('I am a custom middleware');
  next();
};

// This is a global middleware
app.use(loggerMiddleware);

// This is a route-level middleware
app.get('/books/:id', customMiddleware, (req, res) => {
	console.lod(req.headers);  
});
```

---
# Difference in Route-level Middleware
- The main difference is `next()` of the `customMiddleware()` invokes the function in the route instead of the next middleware.

---
# You can also chain the Route-Level Middlewares
``` js
app.get('/books/:id', customMiddleware, loggerMiddleware, (req, res) => {
	console.lod(req.headers);  
});
```

---
> Hence the function inside a route is also technically a middleware without next function since the request-response cycle should eventually be terminated.

---
