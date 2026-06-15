# `localhost` — Notes

- `localhost` = hostname that resolves to **loopback interface**.
- Refers to **the same machine** initiating the request.

```
localhost → 127.0.0.1 (IPv4)
localhost → ::1       (IPv6)
```

---
# Why it Exists

- Enables local networking without external network access.
- OS routes packets internally via loopback device (`lo`).

---
# Key Properties

- Never leaves the host.
- No router, DNS, or internet required.
- Used for development servers, testing, IPC over TCP.

---
# Mental Model

```
Client → localhost → OS loopback → Server (same machine)
```

---
# Common Misconceptions

- `localhost` ≠ internet server.
- Binding to `localhost` restricts access to local machine only.
- `0.0.0.0` is not localhost; it binds to all interfaces.

---
# Typical Usage

```
http://localhost:3000
http://127.0.0.1:8080
```

---
