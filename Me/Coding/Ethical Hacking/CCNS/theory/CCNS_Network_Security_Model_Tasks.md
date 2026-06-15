# Network Security Model Tasks

- **Design an algorithm** — create a transformation algorithm that the opponent cannot defeat. Security depends on the algorithm being mathematically hard to reverse without the key, e.g. AES, RSA.

- **Generate secret information** — produce the key used by the algorithm. Key size directly impacts security — larger key = exponentially larger search space for brute force. e.g. 128-bit AES key has 2¹²⁸ possible combinations.

- **Develop methods for distribution and sharing** — the algorithm is useless if the key can't be securely shared. Key distribution problem: how do two parties exchange a secret over an untrusted channel? Solved by Diffie-Hellman, PKI, KDC (Kerberos).

- **Specify a protocol** — define the rules both parties follow to use the algorithm and keys correctly. Algorithm + key alone isn't enough — the sequence of steps matters. e.g. TLS specifies exactly how encryption, authentication, and key exchange happen in order.

---
