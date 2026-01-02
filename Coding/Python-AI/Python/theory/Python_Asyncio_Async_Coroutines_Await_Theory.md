# Asyncio
- Python’s **asynchronous event-driven framework**
- Manages task scheduling via an **event loop**
- Enables concurrency without threads or processes
- Best for **I/O-bound** workloads

---
# Async
- Declares a function as **asynchronous**
- Returns a **coroutine object** when called
- Does not execute immediately
``` python
async def func():
    pass
```

---
# Coroutine
- A **suspendable function**
- Can pause execution and resume later
- Cooperates with the event loop
- Core unit of async concurrency
``` python
fetch_url(session, url)  # coroutine object
```

---
# Await
- Suspends the current coroutine
- Hands control back to the event loop
- Allows other coroutines to run during wait time
- Used only inside `async` functions
``` python
await asyncio.gather(*tasks)
```

---
