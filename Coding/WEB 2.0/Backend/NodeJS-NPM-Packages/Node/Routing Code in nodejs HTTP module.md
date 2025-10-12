# Code
``` js
import http from 'http';

const server = http.createServer(function(req, res) {
  switch (req.url) {
    case '/':
      res.writeHead(200);
      return res.end(`Homepage`);

    case '/contact-us':
      res.writeHead(200);
      return res.end(`Contact me at aishparab3.25@gmail.com`);

    case '/about':
      res.writeHead(200);
      return res.end(`I am a Software Engineer`);

    default:
      res.writeHead(404);
      return res.end("You are lost");
  }
});

server.listen(8000, () => console.log(`Server is running on PORT: 8000`));
```

---
