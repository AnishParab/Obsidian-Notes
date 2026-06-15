# HMAC (Hash-based Message Authentication Code)

- HMAC is basically:
```text
HMAC(K,M) =
H[(K+ ⊕ opad) || H((K+ ⊕ ipad) || M)]
```

> HMAC combines a cryptographic hash function and a secret key to provide authentication and integrity.

- Defined in RFC 2104
- Most widely used MAC mechanism
- Examples:
    - HMAC-MD5
    - HMAC-SHA1
    - HMAC-SHA256

---
# Parameters

| Symbol | Meaning                     |
| ------ | --------------------------- |
| H      | Hash Function               |
| K      | Secret Key                  |
| M      | Message                     |
| b      | Block size of hash function |
| n      | Hash output size            |
| ipad   | Inner padding constant      |
| opad   | Outer padding constant      |

---
# Padding Constants

#### ipad
```text
00110110
```
Hex:
```text
36H
```
Repeated:
```text
b / 8 times to obtain a block size 'b'
```

#### opad
```text
01011100
```
Hex:
```text
5CH
```
Repeated:
```text
b / 8 times to obtain a block of size 'b'
```

---
#### Step 1 — Prepare Key K+

1. **If:**
```text
Length(K) < b
```
- append zeros on the **right** until length becomes `b`.
Example:
```text
K = 1010

K+ = 10100000
```

2. **If:**
```text
Length(K) > b
```
hash the key first.

---
#### Step 2 — Create Inner Key

Compute:
```text
S1 = K+ ⊕ ipad
```
Since both are `b` bits:
```text
Length(S1) = b
```

---
#### Step 3 — Append Message

Create:
```text
S1 || M
```
or
```text
(K+ ⊕ ipad) || M
```

Structure:

| S1     | Y0     | Y1     | ... | YL-1   |
| ------ | ------ | ------ | --- | ------ |
| b bits | b bits | b bits | ... | b bits |

Where:
- `Y0 ... YL-1` are message blocks
- `L` = number of message blocks

---
#### Step 4 — Compute Inner Hash

Apply hash function:
```text
InnerHash =
H[(K+ ⊕ ipad) || M]
```
Output size:
```text
n bits
```

Example:

| Hash Function | n   |
| ------------- | --- |
| MD5           | 128 |
| SHA-1         | 160 |
| SHA-256       | 256 |

---
#### Step 5 — Create Outer Key

Compute:
```text
S2 = K+ ⊕ opad
```
Again:
```text
Length(S2) = b
```

---
#### Step 6 — Append Inner Hash

Create:
```text
S2 || InnerHash
```
or
```text
(K+ ⊕ opad) || H[(K+ ⊕ ipad) || M]
```

---
#### Step 7 — Compute Final Hash

Apply hash again:
```text
HMAC =
H[(K+ ⊕ opad)
||
H((K+ ⊕ ipad) || M)]
```
This output is the final HMAC value.

---
# Complete Formula

```text
HMAC(K,M)
=
H[(K+ ⊕ opad)
||
H((K+ ⊕ ipad)
||
M)]
```

---
# Why Two Hash Operations?

##### Inner Hash
```text
H[(K+ ⊕ ipad) || M]
```
Mixes:
- Secret key
- Message
##### Outer Hash
```text
H[(K+ ⊕ opad) || InnerHash]
```
- Adds another security layer.
- Prevents attacks against the underlying hash function.

---
# Why Use ipad and opad?

Without them:
```text
H(K || M)
```
- would be vulnerable to several attacks.
- ipad and opad:
	- Create two different derived keys
	- Separate inner and outer hashing stages
	- Improve security

---
# Security Services

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | No        |
| Nonrepudiation  | No        |

---
# Memory Flow

```text
K
↓
Pad to b bits
↓
K+ ⊕ ipad
↓
Append Message
↓
Hash
↓
Inner Hash
↓
K+ ⊕ opad
↓
Append Inner Hash
↓
Hash Again
↓
HMAC
```

#### One-line Memory Rule
```text
Inner Hash
    → H[(K+ ⊕ ipad) || M]

Outer Hash
    → H[(K+ ⊕ opad) || InnerHash]
```
- That's the exact Stallings/NIST HMAC algorithm.

---
# Block Diagram

![[ccns_hmap.excalidraw|500]]

---
