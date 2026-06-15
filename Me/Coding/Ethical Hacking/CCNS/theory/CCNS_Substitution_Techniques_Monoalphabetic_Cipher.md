# Monoalphabetic Cipher

- Single cipher alphabet used for entire message
- Cipher line is any permutation of the 26 alphabetic characters

---
# Permutation

- Ordered sequence of all elements of a set S, each appearing exactly once
- S = {a, b, c} → 6 permutations: abc, acb, bac, bca, cab, cba
- For 26 letters → 26! possible keys ≈ 4 × 10²⁶

---
#### Example
| Plaintext  | N   | e   | s   | o   |
| ---------- | --- | --- | --- | --- |
| Ciphertext | D   | U   | L   | A   |
![[Pasted image 20260613135606.png]]

- No uniform shift — each letter maps arbitrarily
- 4 letter word "Neso" → 4! = 24 possible mappings for those 4 letters

---
# Pros & Cons

**Pros**
- 26! possible keys → eliminates brute force
- Better than Caesar Cipher in key space
**Cons**
- Reflects frequency data of original alphabet
- Prone to frequency analysis — e.g. 'E' is most common in English
- Guessing attack possible using English letter frequency
- Countermeasure: homophones — multiple cipher substitutes for a single plaintext letter

---
