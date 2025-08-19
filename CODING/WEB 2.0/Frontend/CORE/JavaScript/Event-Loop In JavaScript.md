 > **[Visualize Event-Loop here](http://latentflip.com/loupe/)**

---
#  Why Event-Loop ?
- JavaScript is **single-threaded** (one call stack).
- But browsers/Node.js provide **Web APIs** (timers, fetch, etc.) to handle async tasks.
- The **Event Loop** coordinates between **Call Stack**, **Web APIs**, and **Queues**.

---
# Key Components
### 1. **Call Stack**
- Place where JS executes code **line by line**.
- Functions are pushed when called, popped when finished.

### 2. **Web APIs (Browser/Node APIs)**
- Provided by environment (not JS itself).
- Example: `setTimeout`, `fetch`, DOM events.
- Async tasks are handed over to Web APIs.

### 3. **Callback Queue (Macrotask Queue)**
- Holds callbacks from Web APIs (timers, events, etc.).
- Examples: `setTimeout`, `setInterval`, I/O.

### 4. **Microtask Queue**
- Higher priority than Callback Queue.
- Holds **Promises** and `queueMicrotask`.
- Runs immediately after the current call stack is empty.

### 5. **Event Loop**
- Continuously checks:
    - Is Call Stack empty?
    - If yes → move tasks from Microtask Queue first.
    - Then → move tasks from Callback Queue.

---
# Example Flow
``` js
console.log("Start");

setTimeout(() => console.log("Timeout"), 0);

Promise.resolve().then(() => console.log("Promise"));

console.log("End");
```

**Execution Order:**
1. `Start` (stack → logs immediately)
2. `End` (stack → logs immediately)
3. `Promise` (microtask queue runs before macrotask)
4. `Timeout` (macrotask queue runs after microtasks)

---
