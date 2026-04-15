# Composite Key

- PK made of 2+ attributes
- Example: in an `Enrollment` table with no single unique column:

| student_id | course_id | grade |
| ---------- | --------- | ----- |
| 1          | CS101     | A     |
| 1          | CS102     | B     |
| 2          | CS101     | A     |

- PK = `{student_id, course_id}` — neither alone is unique

---
# Compound Key

- Composite key where both/all attributes are FKs
- Same `Enrollment` table — `student_id` is FK → Student, `course_id` is FK → Course
- PK `{student_id, course_id}` is a compound key

---
