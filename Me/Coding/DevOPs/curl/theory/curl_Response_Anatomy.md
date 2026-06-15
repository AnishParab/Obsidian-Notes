# Response Anatomy

Every HTTP response has 3 parts: **status line**, **headers**, **body**.

---
**1. Status Line**

```
HTTP/1.1 200 OK
^        ^   ^
protocol code reason
```

Status code ranges:
```
1xx — Informational  (request received, continuing)
2xx — Success        (200 OK, 201 Created, 204 No Content)
3xx — Redirect       (301 Moved, 302 Found, 304 Not Modified)
4xx — Client error   (400 Bad Request, 401 Unauthorized, 404 Not Found)
5xx — Server error   (500 Internal Server Error, 503 Unavailable)
```

---
**2. Headers**

```
Content-Type: application/json    # format of the body
Content-Length: 42                # byte size of body
ETag: W/"2a-..."                  # fingerprint for caching
Location: /books/3                # where new resource lives (POST response)
Connection: keep-alive            # TCP connection behavior
```

---
**3. Body** The actual payload. Could be JSON, HTML, plain text, binary.

---
**Useful flags for inspecting responses:**

```bash
# headers only, no body
curl -I http://localhost:3000/books

# headers + body together
curl -i http://localhost:3000/books

# body only, no progress bar (default)
curl -s http://localhost:3000/books

# save body to file
curl -o response.json http://localhost:3000/books

# see just the status code
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/books
```

---
