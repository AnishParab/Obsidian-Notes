# Playfair Cipher

- aka Wheatstone-Playfair Cipher
- Invented 1854 by Charles Wheatstone, promoted by Lord Playfair
- First literal digram substitution technique
- Manual symmetric encryption

## Step 1: Build 5×5 Matrix (keyword: MONARCHY)
- Write keyword letters, no duplicates
- Fill remaining alphabet in order
- I/J share one cell (25 cells only)

|     | 1   | 2   | 3   | 4   | 5   |
| --- | --- | --- | --- | --- | --- |
| 1   | M   | O   | N   | A   | R   |
| 2   | C   | H   | Y   | B   | D   |
| 3   | E   | F   | G   | I/J | K   |
| 4   | L   | P   | Q   | S   | T   |
| 5   | U   | V   | W   | X   | Z   |

## Step 2: Create Digrams
- Split plaintext into pairs of 2
- Same letter in a pair → insert filler X
- Odd length → append X

| Plaintext    | Digrams           |
| ------------ | ----------------- |
| attack       | AT TA CK          |
| balloon      | BA LX LO ON       |
| neso academy | NE SO AC AD EM YX |

## Step 3: Encryption Rules
- **Same row** → shift right, wrap around
- **Same column** → shift down, wrap around
- **Rectangle** → each letter takes the column of the other

## Step 4: Encrypt "attack" → AT TA CK

### Rules
- **Same row** → shift right, wrap
- **Same column** → shift down, wrap
- **Rectangle** → swap to each other's column

### Matrix reference
| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | M | O | N | **A** | **R** |
| 2 | C | H | Y | B | D |
| 3 | E | F | G | I/J | K |
| 4 | L | P | Q | **S** | **T** |
| 5 | U | V | W | X | Z |

### Digram AT
- A(row1,col4), T(row4,col5) → Rectangle
- A → (row1,col5) → **R**
- T → (row4,col4) → **S**
- `AT → RS`

### Digram TA
- T(row4,col5), A(row1,col4) → Rectangle
- T → (row4,col4) → **S**
- A → (row1,col5) → **R**
- `TA → SR`

### Digram CK
- C(row2,col1), K(row3,col5) → Rectangle
- C → (row2,col5) → **D**
- K → (row3,col1) → **E**
- `CK → DE`

### Result
`attack → RSSRDE`

---
