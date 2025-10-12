# WebSocket Code
``` ts
import WebSocket, { WebSocketServer } from 'ws';
import http from 'http';

// HTTP Logic
const server = http.createServer(function(request: any, response: any) {
    console.log((new Date()) + ' Received request for ' + request.url);
    response.end("hi there");
});

const wss = new WebSocketServer({ server });

// WebSocket Logic
wss.on('connection', function connection(ws) {
  // Event Registers
  ws.on('error', console.error);

  ws.on('message', function message(data, isBinary) {
    // Server Connects to Every Client
    wss.clients.forEach(function each(client) {
      if (client.readyState === WebSocket.OPEN) {
        client.send(data, { binary: isBinary });
      }
    });
  });

  // Simple Send Message
  ws.send('Hello! Message From Server!!');
});

server.listen(8080, function() {
    console.log((new Date()) + ' Server is listening on port 8080');
});
```

---
