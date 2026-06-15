# Digital Signature

> A digital signature is created by encrypting the message hash using the sender's private key.

---
# Why Do We Need Digital Signatures?

Suppose Alice and Bob share:
```text
K
```
and use:
```text
MAC(K,M)
```
Bob receives:
```text
Message + Valid MAC
```

Question:
```text
Can Bob prove Alice sent it?
```
- No.
Because:
```text
Alice knows K
Bob knows K
```
- Bob could have generated the MAC himself.
- This is why MAC cannot provide:
```text
Nonrepudiation
```

---
# The Problem Digital Signatures Solve

Digital Signatures provide:

| Property        | Meaning                    |
| --------------- | -------------------------- |
| Authentication  | Verify sender identity     |
| Integrity       | Detect modification        |
| Nonrepudiation  | Sender cannot deny sending |
| Confidentiality | Not provided               |

---
# Core Idea

- Generate a fingerprint of the message:
```text
h = H(M)
```
- Sign the fingerprint:
```text
S = E(PRa,h)
```
- Transmit:
```text
M || S
```

![[ccns_didital_signature_basic.excalidraw|700]]

**Why Sign the Hash Instead of the Message?**
- Message:
```text
500 MB
```
- Hash:
```text
160 bits
```
or
```text
256 bits
```
- Much smaller.
- Therefore:
```text
Hash
↓
Sign Hash
```
- instead of:
```text
Sign Entire Message
```

**Signature Generation**
- Input:
```text
Message M
Private Key PRa
```
- Generate hash:
```text
h = H(M)
```
- Encrypt hash:
```text
S = E(PRa,h)
```
- Transmit:
```text
M || S
```

**Signature Verification**
- Input:
```text
M || S
```
- Generate fresh hash:
```text
h1 = H(M)
```
- Recover signed hash:
```text
h2 = D(PUa,S)
```
- Compare:
```text
h1 == h2
```
- If equal:
```text
Valid Signature
```
- Otherwise:
```text
Invalid Signature
```

**Authentication**
- Only Alice possesses:
```text
PRa
```
- Therefore only Alice can generate:
```text
S = E(PRa,h)
```
- Successful verification proves:
```text
Message came from Alice
```

**Integrity**
- Hash depends on every bit of the message.
- Example:
```text
Transfer ₹1000
```
↓
```text
Transfer ₹10000
```
- Hash changes.
- Verification fails.

**Non-Repudiation**
- Most important property.
MAC:
```text
Alice knows K
Bob knows K
```
- No proof.
Digital Signature:
```text
Only Alice knows PRa
```
- Valid signature proves:
```text
Alice signed it
```
- Alice cannot later deny sending it.

**No Confidentiality**
- Transmission:
```text
Message || Signature
```
- The message itself is not encrypted.
- Anyone can read:
```text
Message
```
- Only the signature is protected.

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | No        |
| Nonrepudiation  | Yes       |

---
# Why Message and Signature Are Sent Separately

Physical world:
```text
Document
+
Signature
```

Digital world:
```text
Message
+
Digital Signature
```

- The signature proves ownership of the message.
- It is not a replacement for the message.

---
# Requirements of a Digital Signature

A digital signature must:
- Depend on the message
- Use information unique to the sender
- Prevent forgery
- Prevent denial
- Be easy to generate
- Be easy to verify

---
# Algorithms Required

## Key Generation Algorithm
Generates:
```text
Private Key
+
Public Key
```
Example:
```text
(PRa, PUa)
```

## Signing Algorithm
Input:
```text
Message
Private Key
```
Output:
```text
Digital Signature
```

## Verification Algorithm
Input:
```text
Message
Signature
Public Key
```
Output:
```text
Valid / Invalid
```

---
# Comparison with MAC

| Feature         | MAC        | Digital Signature  |
| --------------- | ---------- | ------------------ |
| Authentication  | Yes        | Yes                |
| Integrity       | Yes        | Yes                |
| Confidentiality | No         | No                 |
| Nonrepudiation  | No         | Yes                |
| Key Type        | Shared Key | Public/Private Key |

---
# Memory Rule

```text
Hash
    → Integrity

MAC
    → Integrity + Authentication

Digital Signature
    → Integrity + Authentication + Nonrepudiation
```

---
