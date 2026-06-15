# Sending custom headers

```bash
# single header
curl -H "X-Custom-Header: value" http://localhost:3000/books

# multiple headers
curl -H "X-Request-ID: abc123" \
     -H "X-Client-Version: 1.0" \
     http://localhost:3000/books
```

**Overriding default headers**
```bash
# override User-Agent
curl -H "User-Agent: myapp/1.0" http://localhost:3000/books

# override Accept
curl -H "Accept: application/json" http://localhost:3000/books
```

---
# Auth headers

```bash
# Basic auth — sends base64(user:pass) in header
curl -u username:password http://localhost:3000/books
# equivalent to:
curl -H "Authorization: Basic dXNlcjpwYXNz" http://localhost:3000/books

# Bearer token (JWT)
curl -H "Authorization: Bearer eyJhbGci..." http://localhost:3000/books

# API key in header
curl -H "X-API-Key: mysecretkey" http://localhost:3000/books

# API key as query param (worse — shows in logs)
curl "http://localhost:3000/books?api_key=mysecretkey"
```

---
