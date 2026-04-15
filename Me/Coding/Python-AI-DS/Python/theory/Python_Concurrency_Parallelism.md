# Diagram
![[concurrency_and_parallelism.excalidraw|500]]

---
# Concurrency vs Parallelism

### Concurrency
**Definition**
- Handling **multiple tasks** by switching between them.
- Tasks make progress **independently**, but not necessarily at the same time.
**Key Characteristics**
- Focus on **task coordination and responsiveness**
- Often used with threads, async/await, event loops
- Works even on **single-core** systems
**Pros**
- System stays responsive during slow I/O
- One blocked task doesn’t stop others
- Efficient for I/O-bound workloads such as disk read/write, web requests.
**Cons**
- Difficult to reason about execution order
- Risk of race conditions and deadlocks
- Does not guarantee performance speedup
**Example**
- Web server handling many client requests using async I/O

---
### Parallelism
**Definition**
- Executing **multiple tasks simultaneously**.
- Requires **multiple CPU cores** or processors.
**Key Characteristics**
- Focus on **performance and speed**
- Tasks are split into independent sub-tasks
- Uses multiprocessing, GPU computing, SIMD, etc.
**Pros**
- True execution speedup
- Fully utilizes multi-core hardware
- Ideal for CPU-intensive workloads
**Cons**
- **Straggler problem:** if one parallel task is slow or lazy, synchronization points can stall the entire process
- Higher overhead for coordination and data sharing
- Poor efficiency if tasks are uneven or dependent
**Example**
- Training a model using multiple CPU cores or GPUs

---
# Core Difference (One Line)
- **Concurrency**: dealing with many tasks at once
- **Parallelism**: doing many tasks at the same time

---
