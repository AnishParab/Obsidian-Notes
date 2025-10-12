# Steps
``` bash
npm init -y

npm i @types/node
```

---
# Code
``` js
import http from 'http';

const server = http.createServer(function(req, res) {
  console.log(`Incoming request: ${req.method} ${req.url}`);
  console.log(req.headers);
  res.writeHead(200);
  res.end('Thanks for visiting my server');
});

server.listen(8000, function() {
  console.log(`HTTP server is up and running on port 8000`);
});
```

---
> Run the code using `node index.js`
 **Halt** the server using `Ctrl c`

---
# Explanation
- `req` ---> This object contains what the user wants.
- `res` ---> Server returns a response object.

---
# `res.end`
- This submits a text response.

---
