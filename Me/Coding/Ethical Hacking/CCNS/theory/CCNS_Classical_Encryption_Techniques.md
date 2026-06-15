# Classical Encryption Techniques

- Oldest forms of encryption, now obsolete
- Basis for understanding modern cryptography
- Two fundamental operations: substitution and transposition
- Can be combined for stronger encryption (product cipher)

---
# Substitution Techniques

- Letters replaced by other letters, numbers, or symbols
- Character identity changes, position stays same

- Letters are replaced with new characters

| Plaintext  | a   | b   | c   | d   | e   |
| ---------- | --- | --- | --- | --- | --- |
| Ciphertext | D   | E   | F   | G   | H   |

- New characters can be introduced
- Vulnerable to frequency analysis — letter frequencies preserved
##### Types
- **Caesar Cipher** — shift each letter by fixed value, e.g. shift 3: A→D, B→E
- **Monoalphabetic Cipher** — each letter maps to a fixed different letter, arbitrary substitution
- **Playfair Cipher** — encrypts digrams (pairs of letters) using a 5×5 key matrix
- **Hill Cipher** — uses matrix multiplication with a key matrix, encrypts blocks of letters
- **Polyalphabetic Cipher** — uses multiple substitution alphabets, e.g. Vigenère cipher, harder to frequency analyze
- **One-Time Pad** — key is random, as long as message, used once → unconditionally secure

---
# Transposition Techniques

- Only position of characters changes, identity stays same
- Applies permutations to plaintext letters
- More effective with longer plaintext
- Vulnerable to anagramming if pattern is detected

- Just letters are re-arranged

| Plaintext  | H   | E   | L   | L   | O   |
| ---------- | --- | --- | --- | --- | --- |
| Ciphertext | O   | L   | L   | E   | H   |
##### Types
- **Rail Fence** — plaintext written in zigzag across rails, read off row by row
- **Row Column Transposition** — plaintext written in rows, columns reordered by a key

---
# Substitution vs Transposition

|                 | Substitution       | Transposition          |
| --------------- | ------------------ | ---------------------- |
| What changes    | Character identity | Character position     |
| What stays same | Position           | Identity               |
| Vulnerability   | Frequency analysis | Anagramming            |
| Example         | Caesar, Playfair   | Rail Fence, Row Column |

---
