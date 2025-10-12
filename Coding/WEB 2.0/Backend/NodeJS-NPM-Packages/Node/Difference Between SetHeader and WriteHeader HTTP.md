# `setHeader(name, value)`
- **Purpose:** Sets (or overwrites) a single HTTP header field **before** the response is sent.
- **Usage:** You can call it multiple times before the response is committed. Each call changes the headers that will eventually be sent.
- **Behavior:** Does **not** send the response headers immediately, it just queues them.
``` js
res.setHeader('Content-Type', 'application/json');
res.setHeader('X-Powered-By', 'Coffee and Rust');
```

---
# `writeHead(statusCode, headers)`
- **Purpose:** Sends the **status line** (like `HTTP/1.1 200 OK`) and the headers to the client immediately.
- **Usage:** This is the point of no return: once called, you can’t change or add headers with `setHeader()`.
- **Behavior:** Can take both a status code and an object of headers.
``` js
res.writeHead(200, {
  'Content-Type': 'application/json',
  'X-Powered-By': 'Coffee and Rust'
});
```

---
