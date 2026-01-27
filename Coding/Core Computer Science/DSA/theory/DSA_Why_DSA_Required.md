# Data Structures — Core Idea
- A data structure defines **how data is organized, stored, and accessed efficiently**.
- Good structure choice ⇒ faster operations (search, insert, update, delete).

---
# Real-World Mappings

### **1. Undo Functionality**
* Best fit: **Stack**
* Reason: Operations follow **LIFO (Last In, First Out)**.

### **2. Ticket/Seat Booking Systems**
* Best fit: **Graph**
* Reason: Represents connections (routes, seats, dependencies).
* BFS used for shortest paths or exploring availability.

### **3. Music Player “Next/Previous Track” Navigation**
* Best fit: **Linked List**
* Circular or doubly linked lists allow:
  * Move to next song
  * Move to previous song
  * Loop playlist

### **4. E-Commerce Category Browsing**
* Best fit: **Tree**
  * Root → main category
  * Internal nodes → sub-categories
  * Leaves → final products

### **5. Student Reports (Insert/Delete/Search Heavy Workloads)**
* Frequent **insert/delete** → **Linked List** (O(1) insert/delete with pointer updates)
* Frequent **search** → **Array** (supports indexing, binary search with sorted data)

---
