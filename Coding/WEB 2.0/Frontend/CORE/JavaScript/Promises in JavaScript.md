# What is a Promise ?
- A **special object** that represents the result of an async operation (pending now, value later).
- Provides a cleaner way to handle async code than callbacks.
- Helps avoid **callback hell** by chaining with `.then()`.
- It’s a **built-in abstraction** over async completion.

---
# States of a Promise
- **Pending** → initial state.
- **Fulfilled** → operation completed successfully (`resolve`).
- **Rejected** → operation failed (`reject`).

---
# Syntax
``` js
const promise = new Promise((resolve, reject) => {
  // async work
  if (success) {
    resolve("Task done!");
  } else {
    reject("Something went wrong");
  }
});

promise
  .then(result => console.log(result))   // runs on resolve
  .catch(error => console.error(error))  // runs on reject
  .finally(() => console.log("Always runs"));
```

---
# Example: File Reading (Node.js)
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

function onDone(data) {
  console.log("File content:", data);
}

anishReadFile().then(onDone).catch(console.error);
```

> Here the **Promise** comes **Synchronously** 
> But
> The **data** comes **Asynchronously**

---
