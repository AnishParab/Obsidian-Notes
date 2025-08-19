# Queues using Lists
``` python
# Queue implementation using lists
queue = []

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
print(queue.pop(0))  # Output: 10
print(queue.pop(0))  # Output: 20
```

# Using collections.deque
``` python
from collections import deque

# Queue implementation using deque
queue = deque()

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
print(queue.popleft())  # Output: 10
print(queue.popleft())  # Output: 20
```