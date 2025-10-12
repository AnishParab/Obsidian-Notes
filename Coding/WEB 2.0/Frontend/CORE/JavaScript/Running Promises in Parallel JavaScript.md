> If multiple Promises are independent, use `Promise.all()` instead of awaiting them one by one.

---
# Example
``` js
async function runParallel() {
  const [user, posts] = await Promise.all([
    fetch("/user/1").then(r => r.json()),
    fetch("/posts").then(r => r.json())
  ]);
  console.log(user, posts);
}
```

---
