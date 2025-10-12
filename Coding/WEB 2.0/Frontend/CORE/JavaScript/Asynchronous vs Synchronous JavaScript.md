# Synchronous
- Code runs **line by line**, in sequence.
- Each operation must **finish before the next one starts**.
- Can cause **blocking** if a task takes long.
``` js
console.log("Start");
console.log("Middle");
console.log("End");

// Output:
// Start
// Middle
// End
```

---
# Asynchronous
- Code does **not wait** for a task to complete.
- Long tasks (like fetching data) run in the background.
- Uses **callbacks, promises, async/await** to handle results later.
``` js
console.log("Start");

setTimeout(() => {
  console.log("Async Task Done!");
}, 1000);

console.log("End");

// Output:
// Start
// End
// Async Task Done!
```

---
