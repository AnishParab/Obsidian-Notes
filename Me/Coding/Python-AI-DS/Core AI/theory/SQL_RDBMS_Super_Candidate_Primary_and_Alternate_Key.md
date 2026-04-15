# Setup — example table:

| cust_id | name  | email           | contact_no |
| ------- | ----- | --------------- | ---------- |
| 1       | Alice | alice@email.com | 9876543210 |
| 2       | Bob   | bob@email.com   | 9123456789 |
| 3       | Alice | xy@email.com    | 9000000000 |

---
# Super Key (SK)

- Any combination of attributes that uniquely identifies a tuple
- `{cust_id}`, `{email}`, `{contact_no}`, `{cust_id, email}`, `{name, contact_no}` — all valid SKs
- `{name}` alone is NOT a SK — two Alices exist

---
# Candidate Key (CK)

- Minimal SK — no redundant attribute
- From above: `{cust_id}`, `{email}`, `{contact_no}` are CKs
- `{cust_id, email}` is NOT a CK — removing `email` still uniquely identifies
- CK values must never be NULL

---
# Primary Key (PK)

- One CK chosen to be the main identifier — prefer fewest attributes
- `{cust_id}` is the PK here

---
# Alternate Key (AK)

- AK = CK − PK
- `{email}` and `{contact_no}` are AKs

---
