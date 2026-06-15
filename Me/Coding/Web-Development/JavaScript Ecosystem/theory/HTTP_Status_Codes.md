# HTTP Status Codes — Notes

- **HTTP Status Code** = numeric response sent by server indicating **result of a request**.
- Returned in **response line**:  
    `HTTP/1.1 200 OK`
- Purpose:
    - Communicate outcome
    - Enable client decision logic (retry, redirect, auth, cache)

---
# Status Code Classes

## `1xx` — Informational

- Request received, processing continues.
- Rarely used in typical web apps.

Common:
- `100 Continue` — client may send body.
- `101 Switching Protocols` — protocol upgrade (e.g., WebSocket).

---
## `2xx` — Success

Meaning: **Request was valid and processed**.

- `200 OK` — standard success.
- `201 Created` — new resource created.
- `202 Accepted` — async processing.
- `204 No Content` — success with empty body.
Notes:
- `200` ≠ resource created.
- `204` useful for idempotent updates.

---
## `3xx` — Redirection

Client must perform another action (usually new request).

- `301 Moved Permanently` — permanent redirect (cacheable).
- `302 Found` — temporary redirect.
- `304 Not Modified` — caching optimization.
Key concept:
- Used heavily by caching layers and CDNs.
Failure mode:
- Redirect loops → infinite client requests.

---
## `4xx` — Client Errors

Meaning: **Request invalid or unauthorized**.

##### Authentication / Authorization
- `401 Unauthorized` — authentication required.
- `403 Forbidden` — authenticated but not allowed.

Common misconception:
- `401` is not “permission denied”; it means **missing/invalid auth**.
##### Resource Issues
- `404 Not Found` — resource missing.
- `410 Gone` — permanently removed.
##### Validation / Request Issues
- `400 Bad Request` — malformed input.
- `409 Conflict` — state conflict.
- `422 Unprocessable Entity` — semantic validation error.
- `429 Too Many Requests` — rate limiting.
Design guideline:
- Prefer precise codes over generic `400`.

---
## `5xx` — Server Errors

Meaning: **Server failed after valid request**.

- `500 Internal Server Error` — unknown failure.
- `501 Not Implemented` — feature unsupported.
- `502 Bad Gateway` — upstream failure.
- `503 Service Unavailable` — temporary overload/maintenance.
- `504 Gateway Timeout` — upstream timeout.
Systems insight:
- Often originates from reverse proxies (NGINX, load balancers).

---
# Mental Model (Server Perspective)

```
Request arrives
    ↓
Validation?
    ├── fail → 4xx
    └── pass
          ↓
Processing success?
    ├── yes → 2xx
    ├── redirect logic → 3xx
    └── internal failure → 5xx
```

---
# Idempotency + Status Codes

| Method | Typical Success |
| ------ | --------------- |
| GET    | 200             |
| POST   | 201 / 200       |
| PUT    | 200 / 204       |
| PATCH  | 200             |
| DELETE | 204             |

Edge case:
- DELETE may return `404` if resource already removed — design choice.

---
# Caching Implications

- `200`, `301`, `304` commonly cacheable.
- `401`, `403`, `500` typically non-cacheable.
- Incorrect caching headers + status codes → stale data bugs.

---
# Common Engineering Mistakes

- Returning `200` for failures (breaks observability).
- Using `500` for validation errors.
- Confusing `401` vs `403`.
- Overusing `302` instead of `301`.
- Ignoring `429` for rate limiting systems.

---
# Common Status Code

```
200 OK
201 Created
204 No Content
301 Moved Permanently
304 Not Modified
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Unprocessable Entity
429 Too Many Requests
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

---
