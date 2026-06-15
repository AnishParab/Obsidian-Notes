# MD5 (Message Digest Algorithm 5)

> MD5 is a cryptographic hash function that accepts a message of arbitrary length and produces a fixed 128-bit message digest.

- Developed by Ronald Rivest
- Defined in RFC 1321
- Produces:
```text
Message
    ↓
MD5
    ↓
128-bit Digest
```

- Widely used for integrity checking
- Cryptographically broken today due to collision attacks

---
# Purpose of MD5

Input:
```text
Any length message
```
Output:
```text
128-bit fixed digest
```
Example:
```text
HELLO
```
↓
```text
8B1A9953C4611296A827ABF8C47804D7
```
Small change:
```text
HELLo
```
↓
Completely different digest.
This is called the:
```text
Avalanche Effect
```

---
# Properties of MD5

##### Preimage Resistance
Given:
```text
Digest
```
Finding original message should be infeasible.
##### Second Preimage Resistance
Given:
```text
M
```
Finding another:
```text
M'
```
with same digest should be infeasible.
##### Collision Resistance
Finding:
```text
M1 ≠ M2
```
such that:
```text
MD5(M1) = MD5(M2)
```
should be infeasible.

---
# MD5 Overview

```text
Message
↓
Padding
↓
Append Length
↓
Initialize Buffers
↓
Process 512-bit Blocks
↓
128-bit Digest
```

![[Pasted image 20260614162611.png]]

---
##### Step 1 — Append Padding Bits

Goal:
```text
Length ≡ 448 (mod 512)
```
Reason:
- Need room for the final 64-bit length field.

**Padding Rule**
- Append:
```text
1
```
- followed by enough:
```text
0's
```
- until length becomes:
```text
448 mod 512
```

**Example**
- Suppose:
```text
Message Length = 1000 bits
```
- Add:
```text
1
+
Required 0's
```
- until:
```text
Length = 448 mod 512
```

---
##### Step 2 — Append Original Length

**After padding:**
- Append:
```text
64-bit representation
```
of the original message length.

**Example:**
```text
Original Length = 1000
```
- Append:
```text
64-bit binary representation of 1000
```

**Why?**
- Allows MD5 to distinguish:
```text
ABC
```
- from
```text
ABC000
```

**Result**
- Total length becomes:
```text
Multiple of 512 bits
```

---
##### Step 3 — Divide Into 512-bit Blocks

- Message becomes:
```text
Y0
Y1
Y2
...
YL-1
```
Where:
- Each block = 512 bits
- L = Number of blocks

**Each Block Contains**
```text
16 words
```
- Each word:
```text
32 bits
```
- Thus:
```text
16 × 32 = 512 bits
```

---
##### Step 4 — Initialize MD Buffer

**MD5 uses:**
```text
128-bit state
```
- divided into four:
```text
32-bit registers
```

**Initial Values

| Buffer | Initial Value |
| ------ | ------------- |
| A      | 67452301H     |
| B      | EFCDAB89H     |
| C      | 98BADCFEH     |
| D      | 10325476H     |

**Purpose**
- These store:
	- Intermediate results
	- Final digest

**Think of them as:**
```text
Running hash state
```

---
##### Step 5 — Process Each 512-bit Block

**Most important step.**
- Every block passes through:
```text
4 Rounds
```
- Each round contains:
```text
16 Operations
```
- Total:
```text
64 Operations
```

**Round 1**
- Uses function:
```text
F(B,C,D)
=
(B AND C)
OR
(NOT B AND D)
```
- Purpose:
```text
Conditional selection
```
- Operations:
```text
1 → 16
```

**Round 2**
- Uses:
```text
G(B,C,D)
=
(B AND D)
OR
(C AND NOT D)
```
- Operations:
```text
17 → 32
```

**Round 3**
- Uses:
```text
H(B,C,D)
=
B XOR C XOR D
```
- Operations:
```text
33 → 48
```

**Round 4**
- Uses:
```text
I(B,C,D)
=
C XOR (B OR NOT D)
```
- Operations:
```text
49 → 64
```

---
# Constants Used

MD5 uses:
```text
T1 ... T64
```
Derived from:
```text
T[i]
=
floor(|sin(i)| × 2³²)
```
- These constants increase randomness.

---
# Block Processing Structure

- Your diagram represents this stage.
- For each block:
```text
512-bit Block
      ↓
Round 1 → F
      ↓
Round 2 → G
      ↓
Round 3 → H
      ↓
Round 4 → I
      ↓
Updated Buffers
```

- The output buffer becomes the input state for the next block.

---
##### Step 6 — Chaining

- After processing a block:
- New values are added to previous buffer values.
```text
Old A + New A
Old B + New B
Old C + New C
Old D + New D
```
**(mod 2³²)**

- This creates:
```text
CVq+1
```
in your diagram.

---
##### Step 7 — Generate Final Digest

- After all blocks are processed:
- Concatenate:
```text
A || B || C || D
```
- Result:
```text
128-bit Message Digest
```

---
# Output Structure

| Register | Size    |
| -------- | ------- |
| A        | 32 bits |
| B        | 32 bits |
| C        | 32 bits |
| D        | 32 bits |

Total:
```text
128 bits
```

---
# Why MD5 Produces Avalanche Effect

- Even one-bit change affects:

```text
F
↓
G
↓
H
↓
I
↓
64 Operations
↓
All Buffers
```

**Result:**
Completely different digest.

---
# MD5 Features

| Feature     | Value           |
| ----------- | --------------- |
| Digest Size | 128 bits        |
| Block Size  | 512 bits        |
| Word Size   | 32 bits         |
| Buffers     | 4               |
| Rounds      | 4               |
| Operations  | 64              |
| Output      | Fixed Length    |
| Input       | Variable Length |

---
# MD5 Memory Flow

```text
Message
↓
Padding
↓
Append Length
↓
512-bit Blocks
↓
Initialize A,B,C,D
↓
Round F
↓
Round G
↓
Round H
↓
Round I
↓
Combine Buffers
↓
128-bit Digest
```

---
# Exam Memory Rule

```text
MD5
=
Padding
+
Length
+
4 Buffers
+
4 Rounds
+
64 Operations
+
128-bit Digest
```

---
