# Redis Use-Cases

![[redis_use_cases.excalidraw|700]]

- **Cache** — store frequently read DB results in RAM; reduces DB load drastically
- **Session Store** — store user session data (login state, tokens); fast access, easy expiry via TTL
- **OTP Store** — store OTPs with a TTL (e.g. 5 mins); auto-expires without any cleanup job
- **Rate Limiting** — track request counts per user/IP using atomic increment; block if threshold exceeded
- **Job Queue** — push jobs into a Redis list; workers pop and process; lightweight alternative to RabbitMQ/Kafka for simple queues

---
**Gotcha:**
- All of these exploit the same 2 properties: **speed** (RAM) + **TTL** (auto-expiry)
- OTP and session use cases are essentially the same pattern — store temporarily, expire automatically

---
