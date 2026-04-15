# Foreign Key (FK)

| cust_id | name  | address | contact_no |
| ------- | ----- | ------- | ---------- |
| 1       | Alice | Delhi   | 9876543210 |
| 2       | Bob   | Mumbai  | 9123456789 |

↑ **Customer** (Parent / Referenced table) — PK: `cust_id`

| order_id | timestamp  | delivery_date | **cust_id** |
| -------- | ---------- | ------------- | ----------- |
| 101      | 2024-01-01 | 2024-01-05    | 1           |
| 102      | 2024-01-02 | 2024-01-06    | 2           |

↑ **Order** (Child / Referencing table) — `cust_id` here is FK → references Customer.cust_id

- FK enforces referential integrity — you can't insert an order with a `cust_id` that doesn't exist in Customer

---
