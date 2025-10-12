- Optimized, dependency-free bcrypt implementation in **pure JavaScript** with full **TypeScript** support.

---
# Why Use `bcryptjs`?
- **No native dependencies** — works everywhere.
- Fully compatible with C++ `bcrypt` binding.
- Uses **salting** and **adaptive hashing** to mitigate:
    - Rainbow table attacks
    - Brute-force attacks
- Max input length: **72 bytes** (UTF-8 chars may consume more than 1 byte).
- Use `bcrypt.truncates(password)` to check if a password exceeds 72 bytes.

---
