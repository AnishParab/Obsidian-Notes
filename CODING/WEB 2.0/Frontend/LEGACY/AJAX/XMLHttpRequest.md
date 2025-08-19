# `XMLHttpRequest`
- **JavaScript objects** used to make AJAX requests.
Basic Flow
``` js
const xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.example.com/data");

xhr.onload = () => console.log(xhr.responseText);

xhr.send();
```

---
# Basic Workflow
``` text
1. Create the object          → new XMLHttpRequest()
2. Configure it               → .open(method, url, async)
3. Send the request           → .send()
4. Listen for response        → .onreadystatechange or .onload
```

---
# Ready States
The `XMLHttpRequest` object has `readyState` from 0 to 4:

| Value | State              | Meaning                                                                     |
| ----- | ------------------ | --------------------------------------------------------------------------- |
| `0`   | `UNSENT`           | `xhr` object is created, but `.open()` hasn't been called yet.              |
| `1`   | `OPENED`           | `.open()` has been called — request is configured but not sent yet.         |
| `2`   | `HEADERS_RECEIVED` | `.send()` has been called, and the response headers + status are available. |
| `3`   | `LOADING`          | The browser is **receiving data** (often in chunks) from the server.        |
| `4`   | `DONE`             | The request is complete and the full **response is ready**. ✅               |

You’ll often use this to check if the request completed successfully.

---
# Why use Fetch API now?
It is modern, promise-based and also has a cleaner syntax.

---





















