# Abstract Data Types (ADT)

## Definition

An **ADT** = _logical specification_ of a type:
- **Data it stores**
- **Allowed operations**
- **Guarantees** of operations

An ADT **does not define**:
- memory representation
- implementation details

---
# Why ADTs Exist

Purpose: **abstraction**
- separate **usage** from **implementation**
- reason about **correctness** independent of performance
- allow multiple implementations with same behavior

Enables:
- modularity
- replaceability
- formal verification

---
# Canonical Examples

### List ADT

**Intent**: ordered collection with positional access  
**Operations**:
- `insert(pos, x)`
- `remove(pos)`
- `replace(pos, x)`
- `get(pos)`

---
### Stack ADT

**Intent**: **LIFO**  
**Operations**:
- `push(x)`
- `pop()`
- `peek()`

---
### Queue ADT

**Intent**: **FIFO**  
**Operations**:

- `enqueue(x)`
- `dequeue()`

---
