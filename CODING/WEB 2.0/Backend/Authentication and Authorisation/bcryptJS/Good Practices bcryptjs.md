# Good Practices
- Always **check input length**: `bcrypt.truncates(password)`
- Prefer **async methods** in production (non-blocking)
- Use **10–12 rounds** for most apps; increase for higher security needs
- Don't store plaintext passwords — always hash and salt

---
