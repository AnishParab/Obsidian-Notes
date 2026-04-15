# E.F. Codd's 12 Rules

> Proposed by **E.F. Codd** (inventor of the relational model) to define what a truly relational DBMS must satisfy
> No commercial RDBMS fully satisfies all 12 — they're a benchmark, not a checklist

---
# Rule 0 (Foundation Rule):

- The system must manage data using only its relational capabilities — no backdoor non-relational access

---
# Rules 1–12:

1. **Information Rule** — all data stored in tables (relations), nothing else
2. **Guaranteed Access Rule** — every value accessible via: table name + primary key + column name
3. **Systematic Treatment of NULL** — NULLs handled uniformly (unknown/missing, not zero or empty string)
4. **Active Online Catalog** — schema (metadata) stored in tables too, queryable via SQL
5. **Comprehensive Data Sublanguage** — must have at least one language supporting DDL, DML, constraints, transactions
6. **View Updating Rule** — all theoretically updatable views must be updatable by the system
7. **High-Level Insert, Update, Delete** — set-level operations, not just row-by-row
8. **Physical Data Independence** — changing physical storage doesn't break applications
9. **Logical Data Independence** — changing logical schema (tables) doesn't break applications
10. **Integrity Independence** — integrity constraints stored in catalog, not in application code
11. **Distribution Independence** — works the same whether data is distributed or not
12. **Non-Subversion Rule** — no lower-level access method can bypass integrity rules

---
# Gotcha:

- Rule 3 (NULL) is one of the most violated/debated — NULL behavior in SQL is notoriously inconsistent
- Logical data independence (Rule 9) is the hardest to achieve in practice

---
