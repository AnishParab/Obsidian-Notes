# SHA-1 (Secure Hash) Algorithm

> SHA-1 is a cryptographic hash function that accepts a message of arbitrary length and produces a fixed 160-bit message digest.

- Developed by NIST and NSA
- Published as FIPS 180-1
- Produces a 160-bit hash
- Based on MD4 family concepts
- More secure than MD5 (historically)
- Now deprecated due to collision attacks


---
# Purpose of SHA-1

Input:
```text
Any length message
```
Output:
```text
160-bit digest
```
Example:
```text
HELLO
```
↓
```text
F7FF9E8B7BB2B91AF11...
```
- A tiny message change produces a completely different digest.

---
# SHA-1 Overview

```text
Message
↓
Padding
↓
Append Length
↓
512-bit Blocks
↓
Initialize A,B,C,D,E
↓
80 Steps
↓
160-bit Digest
```

![[Pasted image 20260614165309.png]]

---
##### Step 1 — Message Padding

Append:
```text
1
```
followed by enough:
```text
0's
```
until:
```text
Length ≡ 448 (mod 512)
```

---
##### Step 2 — Append Original Length

Append:
```text
64-bit representation
```
- of original message length.
Result:
```text
Total Length
=
Multiple of 512 bits
```

---
##### Step 3 — Divide Into Blocks

Message becomes:
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

---
##### Step 4 — Initialize SHA-1 Buffers

SHA-1 uses:
```text
5 registers
```
Each:
```text
32 bits
```
Total:
```text
160 bits
```

---
# Initial Values

| Register | Initial Value |
| -------- | ------------- |
| A        | 67452301H     |
| B        | EFCDAB89H     |
| C        | 98BADCFEH     |
| D        | 10325476H     |
| E        | C3D2E1F0H     |
#### Purpose
Stores:
- Intermediate hash values
- Final digest

---
##### Step 5 — Message Schedule Expansion

Most important SHA-1 concept.

**Initial Words**
- Each 512-bit block contains:
```text
16 words
```
Each:
```text
32 bits
```
So:
```text
W0 ... W15
```

**Expansion**
- SHA-1 expands:
```text
16 words
```
into:
```text
80 words
```

**Formula**
- For:
```text
t = 16 to 79
```

```text
W[t]
=
(W[t−3]
 XOR
 W[t−8]
 XOR
 W[t−14]
 XOR
 W[t−16])
<<< 1
```
Where:
```text
<<<
```
means:
```text
Left Circular Shift
```


**Why Expansion?**
Ensures:
```text
Every input bit
influences
many later operations
```
- Creates strong diffusion.

---
##### Step 6 — Processing Rounds

- The 80 steps are divided into:
```text
4 Rounds
```
Each:
```text
20 Steps
```

**Round 1**
- Steps:
```text
0 – 19
```
- Function:
```text
f(B,C,D)
=
(B AND C)
OR
((NOT B) AND D)
```
- Called:
```text
Choice Function
```
- Constant:
```text
K1
=
5A827999H
```

**Round 2**
- Steps:
```text
20 – 39
```
- Function:
```text
f(B,C,D)
=
B XOR C XOR D
```
- Constant:
```text
K2
=
6ED9EBA1H
```

**Round 3**
- Steps:
```text
40 – 59
```
- Function:
```text
f(B,C,D)
=
(B AND C)
OR
(B AND D)
OR
(C AND D)
```
- Called:
```text
Majority Function
```
- Constant:
```text
K3
=
8F1BBCDCH
```

**Round 4**
- Steps:
```text
60 – 79
```
- Function:
```text
f(B,C,D)
=
B XOR C XOR D
```
- Constant:
```text
K4
=
CA62C1D6H
```

---
# Step Operation

- For each step:
```text
TEMP
=
(A <<< 5)
+
f(B,C,D)
+
E
+
W[t]
+
K[t]
```

Then:
```text
E = D
D = C
C = B <<< 30
B = A
A = TEMP
```

This is repeated:
```text
80 times
```

- for every 512-bit block.

---
##### Step 7 — Final Round Addition

After all 80 steps:
- Add results back to previous buffers.
```text
A = A + H0
B = B + H1
C = C + H2
D = D + H3
E = E + H4
```
- (mod 2³²)

This is the:
```text
Final Round Addition
```
shown in your diagram.

---
##### Step 8 — Chaining

The new values become:
```text
Current Chaining Value
```
- for the next block.
```text
Block 1 Output
↓
Block 2 Input
↓
Block 3 Input
```
and so on.

This is called:
```text
Merkle-Damgård Chaining
```

---
##### Step 9 — Final Digest

After the last block:
- Concatenate:
```text
A || B || C || D || E
```
Result:
```text
160-bit SHA-1 Digest
```

---
# Understanding the Diagram

### Message Padding

```text
Message
↓
Padding
```

Makes length:
```text
448 mod 512
```

---
### Word Computation

```text
W0 ... W79
```

Generated.
This is unique to SHA-1.

---
### Round Initialize

Initialize:
```text
A
B
C
D
E
```

---
### Round 0–19

Uses:
```text
K1
Choice Function
```

---
### Round 20–39

Uses:
```text
K2
XOR Function
```

---
### Round 40–59

Uses:
```text
K3
Majority Function
```

---
### Round 60–79

Uses:
```text
K4
XOR Function
```

---
### Final Round Addition

Add results to previous chaining value.

---
### MPX

Decision point:
```text
More Blocks?
```

If yes:
```text
Process Next Block
```

If no:
```text
Output Digest
```

---
# SHA-1 Features

| Feature        | Value        |
| -------------- | ------------ |
| Digest Size    | 160 bits     |
| Block Size     | 512 bits     |
| Word Size      | 32 bits      |
| Registers      | 5            |
| Message Words  | 16           |
| Expanded Words | 80           |
| Rounds         | 4            |
| Steps          | 80           |
| Output         | Fixed Length |

---
# Memory Flow

```text
Message
↓
Padding
↓
Append Length
↓
512-bit Blocks
↓
Initialize A,B,C,D,E
↓
Expand 16 Words → 80 Words
↓
Round 1 (0–19)
↓
Round 2 (20–39)
↓
Round 3 (40–59)
↓
Round 4 (60–79)
↓
Final Addition
↓
A||B||C||D||E
↓
160-bit Digest
```

```text
SHA-1
=
Padding
+
Length
+
5 Registers
+
16→80 Word Expansion
+
4 Rounds
+
80 Steps
+
160-bit Digest
```

---
