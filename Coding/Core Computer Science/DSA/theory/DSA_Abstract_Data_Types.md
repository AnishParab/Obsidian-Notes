# Abstract Data Types (ADT)
### Definition
An **Abstract Data Type (ADT)** is a _logical specification_ of a data structure defined by:
- **What data it stores**
- **What operations are permitted**
- **What each operation guarantees**

An ADT **does not specify**:
- How data is represented in memory
- How operations are implemented

This separation is intentional.

---
### Why ADTs Exist (Before How)
The primary purpose of an ADT is **abstraction**:
- Decouple _usage_ from _implementation_
- Enable reasoning about correctness independent of performance choices
- Allow multiple implementations with identical behavior

This supports:
- Modularity
- Replaceability
- Formal verification of behavior

---
### Canonical Examples

#### 1. List ADT
**Intent**: Ordered collection with positional access.
**Operations (semantic level)**:
- `insert(position, element)`
- `remove(position)`
- `replace(position, element)`
- `get(position)`

#### 2. Stack ADT
**Intent**: Last-In–First-Out (LIFO) access discipline.
**Operations**:
- `push(x)` → add element to top
- `pop()` → remove and return top element
- `peek()` → return top without removing

#### 3. Queue ADT
**Intent**: First-In–First-Out (FIFO) access discipline.
**Operations**:
- `enqueue(x)` → insert at rear
- `dequeue()` → remove from front

---
