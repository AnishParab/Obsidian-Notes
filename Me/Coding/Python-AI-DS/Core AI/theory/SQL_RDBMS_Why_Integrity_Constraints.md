# Why Integrity Constraints ?

- CRUD operations without rules = risk of corrupting the DB
- Integrity constraints are guardrails — enforce consistency automatically at the DB level, not the application level
- Goal: DB must always reflect a valid, consistent state regardless of what operation was performed

**Gotcha:**
- Putting integrity logic only in application code is dangerous — direct DB access (migrations, scripts, other services) bypasses it entirely
- Constraints enforced at DB level = always guaranteed

---
