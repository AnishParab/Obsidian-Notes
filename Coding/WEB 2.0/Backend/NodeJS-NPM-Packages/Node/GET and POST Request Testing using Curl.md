# GET
- By default, `curl` sends a **GET** request.

---
# POST
- To send a POST with form data:
``` bash
curl -X POST -d "username=asp&password=secret" https://httpbin.org/post

```

- To POST JSON:
``` bash
curl -X POST -H "Content-Type: application/json" \
-d '{"username": "asp", "role": "engineer"}' \
https://httpbin.org/post
```

---
