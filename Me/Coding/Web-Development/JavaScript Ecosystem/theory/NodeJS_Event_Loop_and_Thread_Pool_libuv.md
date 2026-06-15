# Event Loop and Thread Pool

![[event_loop_and_thread_pool_in_nodeJS.excalidraw|700]]

---
# Event Loop

- Single-threaded JS execution model.
- Schedules:
    - callbacks
    - timers
    - promise microtasks
    - network I/O readiness
- Handles **non-blocking OS async events**.
- Blocking code freezes the event loop.

---
# Thread Pool (`libuv`)

- Background worker threads (default: 4).
- Used when OS async APIs are unavailable.

**Offloaded Work:**
- `fs` operations
- DNS (non-native)
- `crypto`
- `zlib`
- native addons

---
# Key Points

- Event loop ≠ blocking handler.
- Thread pool ≠ all async work.
- CPU-heavy JS runs on main thread unless moved to worker threads.

---
