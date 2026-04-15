# How this code makes it Non-Blocking
- The **event loop runs in the main thread**.
- `check_stock()` is submitted to a **worker thread** managed by `ThreadPoolExecutor`.
- `time.sleep(3)` blocks **only that worker thread**, not the event loop.
- `await` suspends the coroutine while the thread works.
- When the thread finishes, the event loop resumes the coroutine with the result.

---
# Code
``` python
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def check_stock(item):
    """
    Synchronous, blocking function.
    - Uses time.sleep()
    - NOT asyncio-aware
    - Must NOT run directly on the event loop
    """
    print(f"Checking {item} in store...")
    time.sleep(3)  # Blocks the current thread
    return f"{item} stock: 42"


async def main():
    # Get reference to the currently running event loop
    loop = asyncio.get_running_loop()

    # ThreadPoolExecutor:
    # - Manages a pool of worker threads
    # - Used for blocking I/O or legacy sync code
    with ThreadPoolExecutor() as pool:

        # run_in_executor:
        # - Submits `check_stock` to the thread pool
        # - Immediately returns control to the event loop
        # - Event loop stays responsive
        # - Returns an awaitable (Future)
        result = await loop.run_in_executor(
            pool,              # Executor (thread pool)
            check_stock,       # Blocking function
            "Masala Chai"      # Function argument
        )

        # This line executes AFTER the background thread finishes
        print(result)


# Creates event loop
# Runs main() coroutine
# Cleans up loop after completion
asyncio.run(main())
```

---
