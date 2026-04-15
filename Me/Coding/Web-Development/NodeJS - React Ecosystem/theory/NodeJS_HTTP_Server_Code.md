# Code

``` js
const http = require('node:http')

const server = http.createServer(function(req, res) {
  console.log('I got an incoming request')

  res.writeHead(200, { 'Content-Type': 'application/json' })
  res.end('Thanks for visiting my server')
})

server.listen(8000, function() {
  console.log(`HTTP Server is up and running on port 8000. Click here : http://localhost:8000`)
})
```

---
