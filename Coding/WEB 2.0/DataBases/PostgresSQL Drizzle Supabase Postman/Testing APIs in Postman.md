# **Testing APIs**
- Add **Tests** under a request (JavaScript snippets).
- Example test:
``` bash
pm.test("Status code is 200", () => {
  pm.response.to.have.status(200);
});

pm.test("Response has userId", () => {
  const json = pm.response.json();
  pm.expect(json).to.have.property("userId");
});
```

- Tests can check response status, time, body, headers.

---
