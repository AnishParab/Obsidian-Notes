# Data vs Information

## What is Data?
- Collection of raw **bits and bytes**.
- No inherent meaning or significance.
- Example: `101010`, `42`, `John`.

---
## What is Information?
- **Processed and interpreted** data.
- Has **meaning**.
- Enables **decision making**.
- Example: `John scored 42 in Math.`

---
#  Types of Data
- **Qualitative**: Descriptive (e.g., colors, names).
- **Quantitative**: Numerical (e.g., age, height).

---
#  Database
- An **electronic storage** of structured data.
- Example: A table of students with names, IDs, and grades.

---
#  DBMS (Database Management System)
- A set of **programs/software** to:
  - Access
  - Add
  - Update
  - Delete data
- Examples: PostgreSQL, MySQL, SQLite.

---
#  DBMS vs File System

## File System Disadvantages

### 1. Data Redundancy and Inconsistency
- **Redundancy**: Same data stored multiple times.
- **Inconsistency**: Updates in one file not reflected in others.
- 🔸 *Example:* Address updated in one file but not in another.

### 2. Difficulty in Accessing Data
- Complex logic needed to search or retrieve.
- 🔸 *Example:* Need to write a program to find all students with >80% marks.

### 3. Data Isolation
- Data scattered across multiple files in various formats.
- 🔸 *Example:* Student info in one file, marks in another—hard to join them.

### 4. Integrity Problem
- No central rules to enforce valid data.
- 🔸 *Example:* Negative marks or invalid roll numbers.

### 5. Atomicity Problem
- Difficult to ensure **complete** execution or **rollback** on failure.
- 🔸 *Example:* Half of the money is debited but not credited.

### 6. Concurrent Access Anomalies
- Simultaneous access leads to inconsistent state.
- 🔸 *Example:* Two people editing the same file simultaneously.

### 7. Security Problems
- Limited control over access and user rights.
- 🔸 *Example:* Any user can read sensitive salary data.

---
