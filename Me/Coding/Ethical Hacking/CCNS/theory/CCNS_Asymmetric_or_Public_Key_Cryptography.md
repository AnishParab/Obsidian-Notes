# Asymmetric / Public Key Cryptography

- Different keys used for encryption and decryption
- **Public key** — shared openly, used to encrypt
- **Private key** — kept secret, used to decrypt
- Also called public key cryptography

---
# Characteristics

- Slower — computationally expensive
- Solves the key distribution problem
- Public key can be freely distributed without compromising security
- Only the private key holder can decrypt

---
# How It Works

- Sender encrypts with recipient's public key
- Only recipient's private key can decrypt
- Private key never leaves the owner

---
# Use Cases

- Secure key exchange, e.g. TLS handshake
- Digital signatures — sign with private key, verify with public key
- Authentication

---
# Examples

- RSA, Diffie-Hellman, ECC

---
# Weakness

- Computationally slow — not suitable for large data
- In practice: asymmetric used to exchange a symmetric key, symmetric used for bulk data (hybrid approach)

---
