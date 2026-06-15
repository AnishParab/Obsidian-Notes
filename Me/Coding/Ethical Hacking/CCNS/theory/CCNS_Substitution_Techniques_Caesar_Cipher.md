# Caesar Cipher

- Julius Caesar used it in military communications to prevent enemies from reading intercepted messages. Shift of 3 was his default — simple enough to use in the field without tools.

[[CCNS_Substitution_Techniques_Shift_Cipher]]
> Caesar Cipher is a Shift Cipher with **k=3**

- Simplest known substitution cipher, used by Julius Caesar in military communications
- Shift of 3 was default — simple enough to use in the field without tools
- Each letter replaced by the letter k positions down the alphabet

---
# Letter-to-Number Mapping

| A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |

| N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  |

---
# Algorithm

- Encryption: `C = (p + k) mod 26`
- Decryption: `p = (C - k) mod 26`

---
#### Example — "obsidian" with k=3
| Plaintext | p   | (p+3) mod 26 | Ciphertext |
| --------- | --- | ------------ | ---------- |
| o         | 14  | 17           | R          |
| b         | 1   | 4            | E          |
| s         | 18  | 21           | V          |
| i         | 8   | 11           | L          |
| d         | 3   | 6            | G          |
| i         | 8   | 11           | L          |
| a         | 0   | 3            | D          |
| n         | 13  | 16           | Q          |
**Output:**
`"obsidian"` → `"REVLGLDQ"`

---
# Pros & Cons 
 
**Pros**
- Simple, easy to implement
**Cons**
- Only 25 possible keys → trivially brute-forceable
- Vulnerable to frequency analysis

---
