# Promise Chaining
``` js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(res => res.json())
  .then(data => console.log("Post:", data))
  .catch(err => console.error(err));
```

---
# Utility Methods
- `Promise.all([p1, p2])` → wait for all to finish.
- `Promise.race([p1, p2])` → first one to finish wins.
- `Promise.allSettled([p1, p2])` → wait for all (whether resolved or rejected).
- `Promise.any([p1, p2])` → first one to succeed.

---
