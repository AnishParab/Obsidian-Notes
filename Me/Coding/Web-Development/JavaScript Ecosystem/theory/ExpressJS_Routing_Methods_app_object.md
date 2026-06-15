# Notes

- Many methods listed (`LOCK`, `MKCOL`, `REPORT`, etc.) originate from **WebDAV extensions**, not core HTTP semantics.
- Express exposes handlers for these methods because Node’s HTTP layer treats method names generically; support does not imply ecosystem-wide usage.
- Common REST APIs typically use only: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.

---
# Express Routing Methods

- `app` is an Express Object.
- **Syntax**:
``` js
app.METHOD(path, callback [,callback ...])
```
- **Safe**: Does not modify server state by definition (GET, HEAD, OPTIONS, TRACE).
- **Idempotent**: Repeating the request produces the same effect (PUT, DELETE, etc.).

| Method        | Purpose                                          | Safe | Idempotent  | Typical Use Case                       |
| ------------- | ------------------------------------------------ | ---- | ----------- | -------------------------------------- |
| `GET`         | Retrieve resource representation                 | Yes  | Yes         | Fetch data                             |
| `POST`        | Create subordinate resource / trigger processing | No   | No          | Create entity, submit form             |
| `PUT`         | Replace entire resource                          | No   | Yes         | Full update                            |
| `PATCH`       | Partial modification of resource                 | No   | Usually No  | Partial update                         |
| `DELETE`      | Remove resource                                  | No   | Yes         | Delete entity                          |
| `HEAD`        | Same as GET but without response body            | Yes  | Yes         | Metadata checks                        |
| `OPTIONS`     | Discover server capabilities                     | Yes  | Yes         | CORS preflight                         |
| `TRACE`       | Diagnostic loopback request                      | Yes  | Yes         | Debugging proxies                      |
| `COPY`        | Duplicate resource                               | No   | Usually Yes | WebDAV operations                      |
| `MOVE`        | Move resource to new URI                         | No   | Yes         | WebDAV file systems                    |
| `LOCK`        | Lock resource for editing                        | No   | No          | Collaborative editing (WebDAV)         |
| `UNLOCK`      | Remove lock from resource                        | No   | Yes         | WebDAV workflows                       |
| `MKCOL`       | Create collection (directory)                    | No   | Yes         | WebDAV directory creation              |
| `MKACTIVITY`  | Create versioning activity                       | No   | Yes         | WebDAV version control                 |
| `MERGE`       | Merge changes into resource                      | No   | No          | Versioned resources                    |
| `CHECKOUT`    | Checkout resource for editing                    | No   | No          | Version control (WebDAV)               |
| `SEARCH`      | Server-side search query                         | Yes  | Yes         | Queryable resources                    |
| `M-SEARCH`    | Multicast search request                         | Yes  | Yes         | Discovery protocols                    |
| `NOTIFY`      | Send event notification                          | No   | No          | Event systems                          |
| `SUBSCRIBE`   | Register for notifications                       | No   | No          | Event subscription                     |
| `UNSUBSCRIBE` | Cancel subscription                              | No   | Yes         | Event systems                          |
| `PURGE`       | Remove cached resource                           | No   | Yes         | Cache invalidation (CDN/reverse proxy) |
| `REPORT`      | Retrieve structured info                         | Yes  | Yes         | WebDAV reporting                       |

---
