# `Bcrypt`
**Bcrypt** is a **password-hashing function** based on the **_Blowfish cipher_**. It’s specially designed to be:
- **Slow and adaptive**, making brute-force attacks inefficient
- Resistant to **rainbow tables** by incorporating a unique **salt**
- Adjustable over time using **cost factor (rounds)** to remain secure as hardware gets faster

---
# bcryptjs vs Bcrypt (C++ Binding)

| Feature            | `bcryptjs`                                   | `bcrypt` (native)                             |
| ------------------ | -------------------------------------------- | --------------------------------------------- |
| **Language**       | Pure **JavaScript**                          | Native **C++ addon** for Node.js              |
| **Speed**          | Slower (~30% or more)                        | Much faster                                   |
| **Platform**       | Works **everywhere**, even **browsers**      | Only works in **Node.js**, needs native build |
| **Security**       | Secure if rounds are high enough             | Secure and faster                             |
| **Dependencies**   | Zero-deps                                    | Requires native compile tools                 |
| **Use in Browser** | Yes (CDN / Webpack etc.)                     | No                                            |
| **Best For**       | Maximum portability (e.g., serverless, edge) | Production Node apps needing speed            |

---
# Summary
| Term             | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| **Bcrypt**       | The original C-based cryptographic hashing function           |
| **bcrypt (npm)** | Fast native binding for Node.js (requires build tools)        |
| **bcryptjs**     | Pure JavaScript version — slower but portable, no native deps |

---
# NOTE

> Refer [[Realistic Use-Cases for Bcrypt and bcryptjs]] for more understanding.

---
