# Monoalphabetic Decryption

##### Attack Type
- **Frequency Analysis Attack** on Monoalphabetic Cipher
- Exploits the fact that cipher preserves frequency of original alphabet

##### Concept
- Every language has known letter frequencies
- e.g. 'E' is most frequent in English (~12.7%)
- Most frequent ciphertext letter → most likely maps to 'E'
- Iteratively guess mappings until plaintext emerges
![[Pasted image 20260613135633.png]]

---
# Example

**Ciphertext:**
`UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZ`
`VUEPHZMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSX`
`EPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ`
##### Step 1: Count frequency of each ciphertext letter
| Letter | Freq% | Letter | Freq% |
| ------ | ----- | ------ | ----- |
| P      | 13.33 | E      | 5.00  |
| Z      | 11.67 | V      | 4.17  |
| S      | 8.33  | X      | 4.17  |
| U      | 8.33  | F      | 3.33  |
| O      | 7.50  | W      | 3.33  |
| M      | 6.67  | T      | 2.50  |
| H      | 5.83  | A      | 1.67  |
| D      | 5.00  | B      | 1.67  |
##### Step 2: Map high frequency cipher letters to English frequencies
- P (13.33%) → E (most frequent in English)
- Z (11.67%) → T (second most frequent)
- S, U → A, O (next most frequent)
##### Step 3: Iteratively guess and refine
- Ciphertext: `GZGEWVGRNCP`
- Trial mappings refined row by row until plaintext reads correctly

| CT  | G   | Z   | G   | E   | W   | V   | G   | R   | N   | C   | P   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PT  | E   | X   | E   | C   | U   | T   | E   | P   | L   | A   | N   |

##### Result
- `GZGEWVGRNCP` → **EXECUTEPLAN**

---
# Key Insight

- No key needed — just English letter frequency table
- Long ciphertext = more accurate frequency analysis
- Countermeasure: homophones (multiple cipher letters per plaintext letter)

---
