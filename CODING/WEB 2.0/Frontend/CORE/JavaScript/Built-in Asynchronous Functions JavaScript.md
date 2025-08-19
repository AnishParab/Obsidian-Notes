# JavaScript and Web API Functions
## Timers API
- **`setTimeout(fn, delay)`** → run once after delay.
- **`setInterval(fn, delay)`** → run repeatedly after delay.
- **`clearTimeout(id)` / `clearInterval(id)`** → cancel timers.
``` js
const id = setInterval(() => console.log("Tick"), 1000);
setTimeout(() => clearInterval(id), 5000);
```

---
## Networking API
- **`fetch(url)`** → returns a **Promise**, used for HTTP requests.
- (Older) **`XMLHttpRequest`** → callback-based HTTP requests.
``` js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(res => res.json())
  .then(data => console.log(data));
```

---
## File & Storage APIs
- **`FileReader`** → read files asynchronously.
- **`localStorage` / `indexedDB`** → async data storage (IndexedDB is promise-like).
``` js
const reader = new FileReader();
reader.onload = () => console.log(reader.result);
reader.readAsText(new Blob(["Hello!"]));
```

---
## Browser/DOM APIs
- **`addEventListener(event, handler)`** → handlers run asynchronously when events occur.
``` js
document.addEventListener("click", () => {
  console.log("Clicked!");
});
```

---
## Microtasks & Promises
- **`Promise`** → async placeholder value.
- **`queueMicrotask(fn)`** → schedule function in microtask queue (runs before next macrotask).
``` js
queueMicrotask(() => console.log("Microtask"));
Promise.resolve().then(() => console.log("Promise resolved"));
```

---
## Other Web APIs (Asynchronous by Nature)
- **`WebSockets`** (`new WebSocket(url)`) → real-time communication.
- **`Geolocation.getCurrentPosition()`** → async location access.
- **`requestAnimationFrame(fn)`** → async UI updates (per animation frame).
- **`Web Workers`** → background threads for heavy tasks.
- **`Notification API`** → async notifications.

---
