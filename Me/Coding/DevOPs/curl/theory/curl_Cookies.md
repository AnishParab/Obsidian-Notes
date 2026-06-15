# Sending a cookie

```bash
curl -b "session=abc123" http://localhost:3000/books
# multiple
curl -b "session=abc123; theme=dark" http://localhost:3000/books
```

**Save cookies from response to file**
```bash
curl -c cookies.txt http://localhost:3000/login
```

**Load cookies from file + save updated cookies back**
```bash
curl -b cookies.txt -c cookies.txt http://localhost:3000/books
```

Always use both `-b` and `-c` together for stateful sessions — `-b` sends, `-c` saves.

---
# Real-world flow — login + authenticated request:

```bash
# 1. login — server sets cookie
curl -c cookies.txt \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"secret"}' \
  http://localhost:3000/login

# 2. use cookie on protected route
curl -b cookies.txt http://localhost:3000/dashboard
```

**Inspect the cookie file:**
```bash
cat cookies.txt
```

> Netscape format — you'll see domain, path, expiry, name, value.

---
