# Digital Signature Standard (DSS)

> DSS is a NIST standard for generating and verifying digital signatures.

- Published by NIST
- Defined in FIPS 186
- Uses the Digital Signature Algorithm (DSA)
- Provides:
    - Authentication
    - Integrity
    - Nonrepudiation
- Does NOT provide confidentiality

---
# Why DSS?

- Digital signatures require a standardized method.

DSS specifies:
- Key generation
- Signature generation
- Signature verification

---
# Security Services

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | No        |
| Nonrepudiation  | Yes       |

---
# DSS Public Parameters
Known to everyone.
#### p
Large prime number.
```text
512 – 1024 bits
```
### q
Prime divisor of:
```text
(p − 1)
```
Typically:
```text
160 bits
```
### g
Generator value.
Computed from:
```text
g = h^((p−1)/q) mod p
```

---
# Private Key

```text
x
```

Chosen randomly.
```text
0 < x < q
```
Only known to signer.

---
# Public Key

```text
y = g^x mod p
```
Published publicly.

---
# Parameters Summary

| Parameter | Type        |
| --------- | ----------- |
| p         | Public      |
| q         | Public      |
| g         | Public      |
| y         | Public Key  |
| x         | Private Key |

---
# Signature Generation

Input:
```text
Message M
Private Key x
```
#### Step 1
Generate message hash.
```text
H(M)
```
#### Step 2
Choose random number.
```text
k
```
where:
```text
0 < k < q
```
Important:
```text
k must be secret
k must be unique
```
#### Step 3
Compute:
```text
r = (g^k mod p) mod q
```
#### Step 4
Compute:
```text
s = k⁻¹(H(M)+xr) mod q
```
#### Step 5
Signature becomes:
```text
(r,s)
```
Transmit:
```text
M || (r,s)
```

---
# Signature Verification

Input:
```text
Message M
Signature (r,s)
Public Key y
```
#### Step 1
Verify:
```text
0 < r < q
0 < s < q
```
#### Step 2
Compute:
```text
w = s⁻¹ mod q
```
#### Step 3
Compute:
```text
u1 = H(M)w mod q
```
#### Step 4
Compute:
```text
u2 = rw mod q
```
#### Step 5
Compute:
```text
v =
((g^u1 × y^u2)
mod p)
mod q
```
#### Step 6
Compare:
```text
v == r
```
If true:
```text
Signature Valid
```
Otherwise:
```text
Signature Invalid
```

---
# Why Authentication Exists

Only signer knows:
```text
x
```
(private key)
Therefore only signer can generate:
```text
(r,s)
```

---
# Why Integrity Exists

Verification uses:
```text
H(M)
```
Any message modification changes hash.
Verification fails.

---
# Why Nonrepudiation Exists

Only signer possesses:
```text
x
```
Valid signature proves signer created it.
Sender cannot deny signing.

---
# Importance of Random k

Most important DSS exam point.
If attacker discovers:
```text
k
```
or
```text
same k reused
```
then:
```text
Private Key x
```
can be recovered.
This completely breaks DSS.

---
# DSS vs RSA Signatures

| Feature          | DSS (DSA) | RSA    |
| ---------------- | --------- | ------ |
| Signature Only   | Yes       | No     |
| Encryption       | No        | Yes    |
| Authentication   | Yes       | Yes    |
| Integrity        | Yes       | Yes    |
| Nonrepudiation   | Yes       | Yes    |
| Speed of Signing | Faster    | Slower |
| Verification     | Slower    | Faster |

---
# Memory Flow

```text
Choose k
↓
Hash Message
↓
Compute r
↓
Compute s
↓
Signature (r,s)
↓
Send
↓
Verify using Public Key
↓
Check v = r
```

```text
Public:
p,q,g,y

Private:
x

Signature:
(r,s)

Verification:
v = r
```

---
