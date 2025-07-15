---

---
#  Abstraction in DBMS
- DBMS hides **complex details** from users via **abstraction**.
- Different users see **different views** of the same data.
####  Example
- **Logistics Department**:
  - Views: product IDs, stock levels, warehouse locations.
- **Marketing Department**:
  - Views: product names, sales data, customer demographics.

---

#  Three-Schema Architecture (ANSI-SPARC Model)
A model to **separate user views from physical storage**.  
It has 3 levels:

---
## Physical Level (Lowest)
- **How data is actually stored**.
- Uses low-level data structures.
- Focuses on:
  - File structures
  - Indexes
  - Compression
  - Encryption

*Example:*  
> Table rows stored as B+ Trees on SSDs, compressed with LZ4, and encrypted using AES-256.

---
## Logical / Conceptual Level (Middle)
- **What data is stored**, and **relationships** between them.
- Defines:
  - Tables
  - Columns
  - Constraints
  - Relationships

- Provides **Physical Data Independence** (schema can change without affecting users).

*Example:*  
> "Customer" table has `customer_id`, `name`, and `phone_number`.  
> "Orders" table has `order_id`, `customer_id`, and `total_price`.

---
## External / View Level (Top)
- **What the user sees** (customized views of data).
- Each user/application can have a **personalized view**.
- Hides unnecessary details.

*Example:*  
> A **Sales Analyst** sees only customer names and total purchases.  
> A **Finance Team** sees invoices and payment status.

---
# Summary

| Level    | Purpose                       | Example                     |
| -------- | ----------------------------- | --------------------------- |
| Physical | Data storage details          | B+ Trees, File blocks       |
| Logical  | Database schema and relations | Tables, Foreign Keys        |
| External | User-specific views           | Marketing sees `sales_data` |

---

