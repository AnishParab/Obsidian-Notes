> Unlike `.catch()`, we can use `try/catch` blocks for cleaner error handling for `async/await`.

--- 
# Syntax

``` js
async function fetchData() {
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.error("Error:", err);
  }
}
```

---
