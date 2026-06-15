# `-v` Flag 

```bash
curl -v http://localhost:3000/books
```

> Lines with `>` = what curl sent. Lines with `<` = what server replied. `*` = curl internals (connection, TLS, etc).


---
### Output

**DNS + Connection**
```
* Host localhost:3000 was resolved.
* IPv6: ::1  /  IPv4: 127.0.0.1
* Trying [::1]:3000...
* Established connection... from ::1 port 57824
```
- curl resolved `localhost` to both IPv6 (`::1`) and IPv4 (`127.0.0.1`)
- It tried IPv6 first — that's system preference, not curl's choice
- Your local port `57824` is ephemeral — OS assigns it randomly for this connection

**Request curl sent (`>`)**
```
> GET /books HTTP/1.1
> Host: localhost:3000
> User-Agent: curl/8.19.0
> Accept: */*
```
- `HTTP/1.x` — not HTTP/2, because localhost doesn't negotiate it
- `Accept: */*` — curl doesn't care what format comes back, accepts anything
- These are the default headers curl adds automatically

**Response from Express (`<`)**
```
< X-Powered-By: Express        # remove this in production — leaks stack info
< Content-Type: application/json; charset=utf-8
< Content-Length: 101
< ETag: W/"65-..."              # fingerprint for caching
< Connection: keep-alive        # TCP connection stays open (timeout=5s)
```

**Connection**
```
* Connection #0 to host localhost:3000 left intact
```
Not closed — kept alive for potential reuse within 5 seconds.

---
