# Shift Cipher

- Generalized form of Caesar Cipher

> Caesar Cipher is a Shift Cipher with **k=3**

- Any shift value k from 0-25 is valid

---
# Algorithm

- Encryption: `C = (p + k) mod 26`
- Decryption: `p = (C - k) mod 26`

---
#### Example — "cryptography" with k=4
| Plaintext | p   | (p+4) mod 26 | Ciphertext |
| --------- | --- | ------------ | ---------- |
| c         | 2   | 6            | G          |
| r         | 17  | 21           | V          |
| y         | 24  | 2            | C          |
| p         | 15  | 19           | T          |
| t         | 19  | 23           | X          |
| o         | 14  | 18           | S          |
| g         | 6   | 10           | K          |
| r         | 17  | 21           | V          |
| a         | 0   | 4            | E          |
| p         | 15  | 19           | T          |
| h         | 7   | 11           | L          |
| y         | 24  | 2            | C          |
**Output:**
`"cryptography"` → `"GVCTXSKVEPTLC"`

---
#### Example — "Hello" with k=0
- k=0 → no shift → ciphertext = plaintext
- **"Hello" → "HELLO"**
- Demonstrates why k=0 is useless

---
