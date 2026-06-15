# Events in Node.js

- `node.js` follows an **Event-Driven** architecture where actions **(events)** trigger specific responses.
- The **EventEmitter** class in the events module is used to handle events in `node.js`.
- Events in `node.js` work little like a publisher-subscriber model where an event is emitted and event listeners **(handlers)** respond to it.

---
# Why use Events ?

- It doesn't choke your CPU.
- Helps in **aysnchronous programming** without **callback hell**.
- Used heavily in real-time applications like chat apps, notifications, and streams.
- Core modules like `fs`, `http` and `stream` use events internally.

---
