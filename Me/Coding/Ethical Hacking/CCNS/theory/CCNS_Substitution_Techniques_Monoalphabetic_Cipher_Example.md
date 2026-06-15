# Example

- Encrypt the plaintext "Attack postponed to tomorrow and do not use our secret paper until further info"
- Secret key: "The quick brown fox jumps over the lazy dog."
- Note: Ignore the second and latter occurrence of alphabets in the key

---
##### Key Derivation
- Key: "The quick brown fox jumps over the lazy dog" (pangram — all 26 letters)
- Remove duplicates, keep first occurrence order:
- `T H E Q U I C K B R O W N F X J M P S V L A Z Y D G`

##### Cipher Alphabet
| Plain  | a   | b   | c   | d   | e   | f   | g   | h   | i   | j   | k   | l   | m   | n   | o   | p   | q   | r   | s   | t   | u   | v   | w   | x   | y   | z   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cipher | T   | H   | E   | Q   | U   | I   | C   | K   | B   | R   | O   | W   | N   | F   | X   | J   | M   | P   | S   | V   | L   | A   | Z   | Y   | D   | G   |

##### Encryption
Plaintext: `attack postponed to tomorrow and do not use our secret paper until further info`

| p   | l   | a   | i   | n   | t   | e   | x   | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a   | t   | t   | a   | c   | k   | p   | o   | s   |
| T   | V   | V   | T   | E   | O   | J   | X   | S   |

| t   | p   | o   | n   | e   | d   | t   | o   | t   | o   | m   | o   | r   | r   | o   | w   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V   | J   | X   | F   | U   | Q   | V   | X   | V   | X   | N   | X   | P   | P   | X   | Z   |

| a   | n   | d   | d   | o   | n   | o   | t   | u   | s   | e   | o   | u   | r   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T   | F   | Q   | Q   | X   | F   | X   | V   | L   | S   | U   | X   | L   | P   |

| s   | e   | c   | r   | e   | t   | p   | a   | p   | e   | r   | u   | n   | t   | i   | l   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S   | U   | E   | P   | U   | V   | J   | T   | J   | U   | P   | L   | F   | V   | B   | W   |

| f   | u   | r   | t   | h   | e   | r   | i   | n   | f   | o   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I   | L   | P   | V   | K   | U   | P   | B   | F   | I   | X   |

#### Ciphertext
`THHTEQ UICHUIKBR HI HIOIWWIN TKR RI KIH FCB IFW CBEWBH UTUBW FKHXJ XKUI`

---
