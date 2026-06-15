# Timeouts

```bash
# TCP connection timeout — how long to wait to establish connection
curl --connect-timeout 5 http://localhost:3000/books

# total time limit — entire request + response must finish within this
curl -m 10 http://localhost:3000/books

# both together (always do this in scripts)
curl --connect-timeout 5 -m 10 http://localhost:3000/books
```

Difference:
- `--connect-timeout` — fails fast if server is unreachable
- `-m` — kills the request if it takes too long overall (slow server, huge response)

---
# Retries

```bash
# retry up to 3 times on failure
curl --retry 3 http://localhost:3000/books

# wait 2 seconds between retries
curl --retry 3 --retry-delay 2 http://localhost:3000/books

# retry on all errors including HTTP 5xx
curl --retry 3 --retry-all-errors http://localhost:3000/books
```

> Gotcha — `--retry` only retries on network failures by default, not HTTP errors like 500. You need `--retry-all-errors` for that.

---
**All together for scripts:**

```bash
curl --connect-timeout 5 \
     -m 10 \
     --retry 3 \
     --retry-delay 2 \
     --retry-all-errors \
     -s \
     http://localhost:3000/books
```

---
