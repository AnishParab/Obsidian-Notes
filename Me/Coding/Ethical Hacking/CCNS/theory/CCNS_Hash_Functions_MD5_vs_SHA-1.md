# SHA-1 vs MD5

## Overview

- Both are cryptographic hash functions.
- Both accept variable-length input.
- Both process data in 512-bit blocks.
- Both generate fixed-length message digests.
- Both use the Merkle-Damgård iterative structure.
- Both are considered cryptographically broken today for collision resistance.

---
# Comparison Table

| Feature              | MD5               | SHA-1                   |
| -------------------- | ----------------- | ----------------------- |
| Full Form            | Message Digest 5  | Secure Hash Algorithm 1 |
| Developed By         | Ronald Rivest     | NSA / NIST              |
| Standard             | RFC 1321          | FIPS 180-1              |
| Digest Size          | 128 bits          | 160 bits                |
| Block Size           | 512 bits          | 512 bits                |
| Word Size            | 32 bits           | 32 bits                 |
| Registers            | 4 (A,B,C,D)       | 5 (A,B,C,D,E)           |
| Steps Per Block      | 64                | 80                      |
| Rounds               | 4 × 16            | 4 × 20                  |
| Message Expansion    | No                | Yes (16 → 80 words)     |
| Byte Order           | Little Endian     | Big Endian              |
| Output Length        | 32 Hex Characters | 40 Hex Characters       |
| Speed                | Faster            | Slower                  |
| Security             | Lower             | Higher (historically)   |
| Collision Resistance | Weaker            | Stronger                |
| Current Status       | Broken            | Broken                  |
| Replacement          | SHA-2             | SHA-2                   |

---
# Digest Size Difference

MD5:
```text
128-bit digest
```

SHA-1:
```text
160-bit digest
```

Extra:
```text
160 - 128 = 32 bits
```
This increases collision resistance.

---
# Buffer Difference

### MD5
Uses:
```text
A
B
C
D
```
Total:
```text
4 × 32 = 128 bits
```

### SHA-1
Uses:
```text
A
B
C
D
E
```
Total:
```text
5 × 32 = 160 bits
```

---
# Processing Difference

### MD5
```text
4 Rounds
16 Operations each
```
Total:
```text
64 Operations
```

### SHA-1
```text
4 Rounds
20 Operations each
```
Total:
```text
80 Operations
```

More operations means:
- More mixing
- Better diffusion
- Higher computational cost

---
# Word Expansion Difference

### MD5
Processes:
```text
16 words
```
directly.
- No expansion.

### SHA-1
Expands:
```text
16 words
```
into:
```text
80 words
```
using:
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
Advantage:
```text
More diffusion
More avalanche effect
```

---
# Byte Ordering Difference

### MD5
Uses:
```text
Little Endian
```
Least significant byte stored first.

### SHA-1
Uses:
```text
Big Endian
```
Most significant byte stored first.

---
# Security Difference

### MD5
- Collision attacks practical.
- Two different files can be generated with identical digest.

### SHA-1
Historically stronger than MD5 because:
- Larger digest
- More rounds
- More operations
- Word expansion

However:
```text
SHA-1 is also broken today
```
- and should not be used for modern security systems.

---
# Why SHA-1 Was Considered Better

```text
Larger Digest
+
More Registers
+
More Operations
+
Word Expansion
=
Stronger Collision Resistance
```

---
# Memory Rule

```text
MD5
=
128 bits
4 Buffers
64 Steps

SHA-1
=
160 bits
5 Buffers
80 Steps
Word Expansion
```

### Fast Recall Table

| MD5          | SHA-1           |
| ------------ | --------------- |
| 128          | 160             |
| 4 Buffers    | 5 Buffers       |
| 64 Steps     | 80 Steps        |
| No Expansion | 16→80 Expansion |
| Faster       | Slower          |
| Weaker       | Stronger        |

---
