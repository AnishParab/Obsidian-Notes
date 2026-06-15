# Request Anatomy

**1. Method + URL**
```bash
curl -X POST http://localhost:3000/books
#     ^        ^         ^        ^
#   method   scheme     host     path
```

URL breakdown:
```
http://localhost:3000/books?sort=asc
^      ^         ^    ^     ^
scheme host      port path  query string
```

---
**2. Headers** Metadata about the request. curl sends some by default, you add the rest.

```bash
curl -v http://localhost:3000/books
# Default headers curl sends automatically:
# Host, User-Agent, Accept
```

Adding custom headers:
```bash
curl http://localhost:3000/books \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer mytoken" \
  -H "X-Custom-Header: whatever"
```

---
**3. Body** Only relevant for POST/PUT/PATCH. GET/DELETE have no body.

```bash
curl -X POST http://localhost:3000/books \
  -H "Content-Type: application/json" \
  -d '{"title": "Dune", "author": "Herbert"}'
#    ^
#    body
```

- Gotcha — `-d` without `Content-Type` sends as `application/x-www-form-urlencoded` by default, not JSON. Always set the header explicitly.

---
