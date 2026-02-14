# Data Structures — Core Idea

- Data structure = **how data is organized, stored, accessed**
- Good choice ⇒ faster **search / insert / update / delete**

---
# Real-World Mappings

### 1. Undo

- **Stack**
- **LIFO**

---
### 2. Ticket/Seat Booking

- **Graph**
- Models **connections**
- **BFS** for shortest path / availability search

---
### 3. Music Player Next/Previous

- **Linked List**
- **Doubly / Circular**
    - next / previous
    - loop playlist

---
### 4. E-Commerce Categories

- **Tree**
    - root: main category
    - internal: sub-categories
    - leaves: products

---
### 5. Student Reports (Heavy Insert/Delete/Search)

- insert/delete heavy → **Linked List** (O(1) pointer updates)
- search heavy → **Array** (indexing, binary search if sorted)

---
