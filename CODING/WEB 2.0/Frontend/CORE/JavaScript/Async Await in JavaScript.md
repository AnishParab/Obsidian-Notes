# What is `async/await` ?
- A **syntactic sugar** built on top of **Promises**.
- Lets you write async code that **looks synchronous**.
- Makes code **cleaner, easier to read, and debug** compared to `.then()` chains.

---
## `async` Keyword
- Used before a function to make it return a **Promise**.

> Even if you `return` a normal value → it becomes a Promise which is **resolved, pending or rejected**.

``` js
async function greet() {
  return "Hello"; // wrapped in Promise.resolve()
}

greet().then(console.log); // Hello
```

---
## `await` Keyword
- Can only be used **inside async functions**.
- Makes async code **look synchronous**.

> Pauses execution until the Promise **resolves/rejects**.

``` js
function fetchNumber() {
  return new Promise(resolve => setTimeout(() => resolve(42), 1000));
}

async function getNumber() {
  console.log("Fetching...");
  const num = await fetchNumber(); // waits here
  console.log("Got:", num);
}

getNumber();
// Output:
// Fetching...
// Got: 42
```

---
# Async/Await Example with File Reading
``` js
const fs = require("fs");

function anishReadFile() {
  return new Promise((resolve, reject) => {
    fs.readFile("test.txt", "utf8", (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

async function run() {
  try {
    const data = await anishReadFile();   // waits here until resolved
    console.log("File content:", data);
  } catch (err) {
    console.error("Error reading file:", err);
  }
}

run();
```

> Errors are caught with a `try/catch` block → cleaner, more synchronous-looking flow.

---
