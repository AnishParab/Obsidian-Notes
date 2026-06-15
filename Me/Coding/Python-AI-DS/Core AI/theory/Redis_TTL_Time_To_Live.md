# Time To Live (TTL)

- **TTL (Time To Live)** = expiry timer set on a key — Redis auto-deletes it when timer hits 0
- Without TTL, key lives forever (until manually deleted or Redis restarts without persistence)

**Example:**
```
SET otp:user123 "4521" EX 300   -- expires in 300 seconds (5 mins)
```
- After 5 mins → key is gone automatically, no cleanup job needed

**Commands:**
- `EX <seconds>` — set TTL in seconds at creation
- `EXPIRE <key> <seconds>` — set/update TTL on existing key
- `TTL <key>` — check remaining time (returns -1 if no TTL, -2 if key doesn't exist)
- `PERSIST <key>` — remove TTL, make key permanent

**Why it matters:**
- OTPs, sessions, rate limit windows, cache entries — all need auto-expiry
- Offloads expiry logic from application code to Redis itself

**Gotcha:**
- TTL is not guaranteed to the millisecond — Redis uses lazy expiry + periodic cleanup
- Lazy expiry: key is checked and deleted only when accessed
- Periodic cleanup: Redis scans a random sample of keys every 100ms to delete expired ones

![[redis_value_storing.excalidraw|700]]

---
