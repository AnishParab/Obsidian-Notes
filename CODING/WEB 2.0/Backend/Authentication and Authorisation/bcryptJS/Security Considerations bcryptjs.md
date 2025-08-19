# Security Considerations
- **Adaptive Hashing**: Iteration count can increase over time for better security.
- **Input Truncation**: Only first 72 bytes of password are hashed.
- **Output Hash Length**: Always 60 characters.
- **Crypto Fallback**: Uses secure random if `crypto` is unavailable.

---