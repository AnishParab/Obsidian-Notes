# Core Mental Model
- **async def** → defines a _coroutine_ (not executed immediately)
- **await** → _yields control_ to the event loop
- **event loop** → runs coroutines, switches between them when they `await`
- **asyncio.sleep** → non-blocking pause (suspends coroutine, not thread)
- **time.sleep** → blocks the thread (kills concurrency)

---
# Code 1: `await` vs blocking sleep
```python
import asyncio


async def brew_chai():
    print("Brewing chai...")

    # Non-blocking sleep:
    # - Coroutine is suspended
    # - Event loop is free to run OTHER coroutines
    await asyncio.sleep(2)

    print("Chai is ready.")


# Creates an event loop
# Schedules brew_chai() as a task
# Runs until the coroutine completes
asyncio.run(brew_chai())
```

### What actually happens
1. `brew_chai()` starts execution.
2. Hits `await asyncio.sleep(2)`
3. Coroutine **pauses**, control returns to the event loop.
4. After 2 seconds, coroutine is **resumed**.
5. Execution completes.

---
# Why `time.sleep()` is dangerous in async code
```python
import time
import asyncio

async def bad_example():
    print("Start")
    time.sleep(2)  # ❌ Blocks the entire event loop
    print("End")
```

- Event loop is frozen
- No other coroutine can run
- Async advantage is lost

---
# Code 2: True concurrency with `asyncio.gather`
```python
import asyncio


async def brew(name):
    print(f"Brewing {name}...")

    # All brew() coroutines pause here together
    await asyncio.sleep(2)

    print(f"{name} is ready.")


async def main():
    # asyncio.gather:
    # - Schedules ALL coroutines on the SAME event loop
    # - Runs them concurrently
    # - Waits until ALL complete
    await asyncio.gather(
        brew("Masala"),
        brew("Green"),
        brew("Ginger"),
    )


asyncio.run(main())
```

### Timeline (important)
```
t = 0s  → All 3 coroutines start
t = 0s  → All hit await asyncio.sleep(2)
t = 2s  → All resume
```

### Critical insight
- Total time ≈ **2 seconds**
- NOT 2 + 2 + 2
- This is **concurrency**, not parallelism

---
# Code 3: Async I/O with `aiohttp`
```python
import asyncio
import aiohttp


async def fetch_url(session, url):
    # Non-blocking HTTP request
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


async def main():
    # Three identical URLs (simulating multiple requests)
    urls = ["https://httpbin.org/delay/2"] * 3

    # ClientSession should be shared
    async with aiohttp.ClientSession() as session:

        # Create coroutine objects (NOT executed yet)
        tasks = [fetch_url(session, url) for url in urls]

        # *tasks expands to: t1, t2, t3
        # All are scheduled on the same event loop
        await asyncio.gather(*tasks)


asyncio.run(main())
```

### What happens under the hood
- Requests are **sent almost immediately**
- While waiting for network I/O:
    - Coroutine yields control
    - Event loop runs others
- When responses arrive:
    - Corresponding coroutine resumes

### Why async shines here
- Network I/O is slow
- CPU waits → async fills that wait with useful work

---
# Important Distinctions

### Async ≠ Parallel

| Concept  | Meaning                  |
| -------- | ------------------------ |
| Async    | Cooperative multitasking |
| Parallel | Multiple CPU cores       |

Async uses **one thread**, parallel uses **many cores**.

---
# Coroutine Lifecycle

```text
async def func():     # definition
func()                # coroutine object
await func()          # execution
```

- Calling does **not** run it
- `await` or scheduling runs it

---
# `asyncio.gather` vs sequential await

❌ Sequential (slow)
```python
await brew("Masala")
await brew("Green")
await brew("Ginger")
```

✅ Concurrent
```python
await asyncio.gather(
    brew("Masala"),
    brew("Green"),
    brew("Ginger"),
)
```

---
# When to use asyncio
✅ Network I/O  
✅ File I/O (async-supported libs)  
✅ APIs, scraping, microservices  
❌ CPU-heavy computation (use multiprocessing)

---
# One-line Cheatsheet
- **async def** → coroutine
- **await** → yield control
- **event loop** → scheduler
- **asyncio.sleep** → non-blocking
- **time.sleep** → blocking
- **gather** → concurrency

---
