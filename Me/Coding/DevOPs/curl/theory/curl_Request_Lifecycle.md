# `curl` Request Lifecycle

**1. DNS Resolution** `localhost` → resolves to `127.0.0.1` (loopback). For a real domain, curl asks your DNS server for the IP.

**2. TCP Handshake** curl opens a TCP connection to `127.0.0.1:3000`. Three-way handshake (SYN → SYN-ACK → ACK). This is just establishing the pipe.

**3. HTTP Request sent** Over that TCP connection, curl sends plain text:
```
GET /users HTTP/1.1
Host: localhost:3000
User-Agent: curl/8.19.0
Accept: */*
```

**4. Server processes, sends response**
```
HTTP/1.1 200 OK
Content-Type: application/json
...
[body]
```

**5. Connection closes** (or stays alive for reuse)

---
