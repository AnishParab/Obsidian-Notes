# Difference

| Feature           | **Callback**              | **Synchronous**               | **Promises (Async/Await)**            |
| ----------------- | ------------------------- | ----------------------------- | ------------------------------------- |
| 🧵 Blocking?      | ❌ Non-blocking            | ✅ Blocking                    | ❌ Non-blocking                        |
| ⌛ Execution       | Asynchronous              | Synchronous                   | Asynchronous                          |
| 🧠 Readability    | ❌ Callback hell if nested | ✅ Easy to understand          | ✅ Clean & readable with `async/await` |
| 💣 Error Handling | `if(err)` or try/catch    | try/catch                     | `.catch()` or try/catch with `await`  |
| ✅ Use Case        | Low-level async logic     | Quick scripts / startup tasks | Modern async flows / clean code       |

---
# Examples
### Callback
``` js
const fs = require('fs');

fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) console.error(err);
  else console.log(data);
});
```

## Synchronous
``` js
const data = fs.readFileSync('file.txt', 'utf8');
console.log(data); // Blocks further execution until done
```

## Promise / Async-Await
``` js
const fs = require('fs/promises');

async function readFile() {
  try {
    const data = await fs.readFile('file.txt', 'utf8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
readFile();
```

---
# When to Use ? 
| Situation                    | Best Choice            |
| ---------------------------- | ---------------------- |
| Performance-critical servers | Promises / Async       |
| Startup/init scripts         | Synchronous            |
| Simple async logic           | Callbacks / Promises   |
| Clean scalable async logic   | Promises (async/await) |

---
