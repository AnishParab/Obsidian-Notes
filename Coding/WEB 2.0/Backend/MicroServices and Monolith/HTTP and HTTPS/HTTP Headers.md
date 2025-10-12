# What ?
- Used to send meta data about a resource or a HTTP message.
- Describe's the behavior of the client or the server.
- It contains text information stored in key-value pairs, and they are included in every HTTP request and response.
- These headers communicate core information, such as what browser the client is using and what data is being requested.

---
# HTTP Request (from client → server) ? **(GET)**
``` http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
```

---
# HTTP Response (from server → client)
``` http
HTTP/1.1 200 OK
Date: Mon, 15 Sep 2025 12:00:00 GMT
Server: Apache/2.4.41 (Ubuntu)
Content-Type: text/html; charset=UTF-8
Content-Length: 1256
Cache-Control: max-age=3600
```

---
