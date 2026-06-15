# Redirects

By default curl does **not** follow redirects:
```bash
curl -v http://localhost:3000/old-route
# you'll see 301/302 but curl stops there
```

**Follow redirects with `-L`:**
```bash
curl -L http://localhost:3000/old-route
```

**Limit hops:**
```bash
curl -L --max-redirs 3 http://localhost:3000/old-route
```

**See the full redirect chain:**
```bash
curl -v -L http://localhost:3000/old-route
# each hop shows as a new request/response cycle in -v output
```

---
