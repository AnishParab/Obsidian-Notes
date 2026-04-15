# Surrogate Key

You have two separate tables:

| student_id | name  | college  |
| ---------- | ----- | -------- |
| 1          | Alice | MIT      |
| 2          | Bob   | Stanford |

| employee_id | name  | company   |
| ----------- | ----- | --------- |
| 1           | Carol | Google    |
| 2           | Alice | Microsoft |

- Now you merge them into a single `Person` table. Problem: both tables have their own IDs starting from 1 — they clash. Neither is a reliable PK anymore.

- Solution — generate a new surrogate key:

| person_id | name  | type     | original_id |
| --------- | ----- | -------- | ----------- |
| 101       | Alice | Student  | 1           |
| 102       | Bob   | Student  | 2           |
| 103       | Carol | Employee | 1           |
| 104       | Alice | Employee | 2           |

- `person_id` is the surrogate key — auto-generated, no real-world meaning
- Solves the ID clash problem cleanly
- `original_id` kept optionally for traceability, but it's not the PK

---
