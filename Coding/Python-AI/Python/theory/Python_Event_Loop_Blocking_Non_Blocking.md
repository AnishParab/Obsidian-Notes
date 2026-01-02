# Diagrams
![[event_queue.excalidraw|500]]

---

![Image](https://www.pythontutorial.net/wp-content/uploads/2022/07/python-event-loop.svg)

---

![Image](https://cdn.hackersandslackers.com/2021/04/async_eventloop.jpg)

---

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20250208123836185275/Event-Loop-in-JavaScript.jpg)

---
# Event Loop
**Definition**
- An **event loop** is a core mechanism that continuously checks for and executes **scheduled tasks**, **callbacks**, and **I/O events** without blocking the program.

**Core responsibilities**
- Maintain a queue of **ready callbacks**.
- Monitor **I/O operations** (network, timers, subprocesses).
- Resume **coroutines** when their awaited operation completes.
- Decide _what runs next_ and _when_.

**How it works (high level)**
1. Tasks/coroutines are **registered** with the event loop.
2. A coroutine hits `await` → it **yields control**.
3. The loop runs other ready tasks.
4. When the awaited I/O completes, the loop **schedules the coroutine back**.
5. Loop continues until no tasks remain.

**Key concepts**
- **Coroutine**: `async def` function that can pause with `await`.
- **Task**: A wrapped coroutine scheduled on the event loop.
- **Future**: Placeholder for a result that will be available later.
- **Callback**: A function executed when an event completes.

**Important properties**
- **Single-threaded by default** (concurrency, not parallelism).
- **Non-blocking**: Blocking calls freeze the entire loop.
- Cooperative multitasking: tasks must **yield explicitly** via `await`.

---
# Blocking (Blocks Event Loop)
**What blocks the event loop (bad)**
- `time.sleep()`
- Heavy CPU computation
- Blocking I/O (file reads, sync HTTP)

---
# Non-Blocking (Doesn't Block Event Loop)
**What doesn’t block (good)**
- `await asyncio.sleep()`
- Async network calls
- Async subprocess handling

---
**One-line summary**
> The Python event loop is a scheduler that efficiently runs many I/O-bound tasks by switching between them whenever they’re waiting.

---
