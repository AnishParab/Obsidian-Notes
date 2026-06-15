# Plain Hash Function

```text
H(M) = h
```

> The hash value `h` acts as the authenticator.

- A hash function converts a message of arbitrary length into a fixed-length value called a hash, digest, or hash code.
- The hash uniquely represents the message.
- Even a tiny change in the message produces a completely different hash.
##### Working
- Sender:
```text
M → H(M) → h
```
- Transmits:
```text
M || h
```
- Receiver:
```text
M → H(M) → h'
```
- Compares:
```text
h == h'
```
- If equal:
	- Message unchanged
- If not equal:
	- Message modified

![[ccns_hash_function_only.excalidraw|700]]

#### **Integrity**
- Hash depends on every bit of the message.
- Example:
```text
Transfer ₹1000
```
- might generate:
```text
A1B2C3D4
```
- Changing one digit:
```text
Transfer ₹10000
```
- may generate:
```text
9F7A8C12
```
- Receiver immediately detects modification.

#### **No Authentication**
- Hash function uses:
```text
H(M)
```
- There is no secret key.
- Anyone can generate:
```text
H(M)
```
- including attackers.
Example:
- Eve changes:
```text
Transfer ₹1000
```
- to
```text
Transfer ₹10000
```
- Then simply computes:
```text
H(Transfer ₹10000)
```
- and sends the new hash.
- Receiver cannot detect that Eve created it.

#### **No Confidentiality**
- Message is transmitted directly.
- Example:
```text
Transfer ₹1000 || A1B2C3D4
```
- Everyone can read:
```text
Transfer ₹1000
```
- Hash only detects changes.
- It does not hide information.

| Property        | Supported |
| --------------- | --------- |
| Integrity       | Yes       |
| Authentication  | No        |
| Confidentiality | No        |
#### Limitation of Plain Hashing
- Because no secret key is involved:
```text
Anyone can compute H(M)
```
- Therefore plain hashing alone is insufficient for secure authentication.
- This is why digital signatures and MACs exist.

---
# Encryption on Hash Function Only

> Hash is encrypted using sender's private key.

### Working
- Generate hash:
```text
h = H(M)
```
- Encrypt hash:
```text
S = E(PRa, h)
```
- Transmit:
```text
M || S
```
- Receiver computes:
```text
h' = H(M)
```
- Receiver decrypts:
```text
h = D(PUa, S)
```
- Compare:
```text
h == h'
```

![[ccns_hash_function_authenticator.excalidraw|500]]

#### **Authentication**
- Only Alice possesses:
```text
PRa
```
- If Bob successfully recovers the correct hash using:
```text
PUa
```
- then Alice must have created the encrypted hash.
- Therefore:
	- Sender authentication achieved.

#### **Integrity**
- Hash is computed from the original message.
- If message changes:
```text
H(M) ≠ H(M')
```
- Comparison fails.
- Modification is detected.

#### **No Confidentiality**
- The message itself is never encrypted.
- Transmission:
```text
M || E(PRa, H(M))
```
- Everyone can read:
```text
M
```
- Only the hash is protected.

> This is essentially the basic idea behind a: Digital Signature

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | No        |

---
# Encrypting Both Message and Hash

> Signature provides authentication. Encryption provides confidentiality.

##### Working
- Generate hash:
```text
h = H(M)
```
- Create signature:
```text
S = E(PRa, h)
```
- Encrypt message:
```text
C = E(K2, M)
```
- Transmit:
```text
C || S
```
- Receiver decrypts message:
```text
M = D(K2, C)
```
- Generate fresh hash:
```text
h' = H(M)
```
- Recover original hash:
```text
h = D(PUa, S)
```
- Compare:
```text
h == h'
```

![[ccns_hash_authentic_type_2.excalidraw|1000]]

#### **Authentication**
- Only Alice possesses:
```text
PRa
```
- Valid signature proves message originated from Alice.

#### **Integrity**
- Hash comparison verifies:
```text
Message received
=
Message signed
```
- Any modification causes mismatch.

#### **Confidentiality**
- Message is encrypted.
- Only parties possessing:
```text
K2
```
- can recover the plaintext.
- An attacker sees only ciphertext.

##### Why This Is Stronger
- Previous method:
```text
M || Signature
```
- Everyone could read the message.
- Current method:
```text
Encrypted Message || Signature
```
- Only authorized users can read the message while still verifying authenticity.

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | Yes       |

##### Relationship to Digital Signatures
- This structure is the foundation of modern secure communication:
```text
Hash
    → Integrity

Private Key Encryption of Hash
    → Authentication

Message Encryption
    → Confidentiality
```
- Combining all three gives:
```text
Authentication
+ Integrity
+ Confidentiality
```

---
# Summary

| Technique                     | Authentication | Integrity | Confidentiality |
| ----------------------------- | -------------- | --------- | --------------- |
| Hash Only                     | No             | Yes       | No              |
| MAC                           | Yes            | Yes       | No              |
| Encrypted Hash (Signature)    | Yes            | Yes       | No              |
| Encrypted Message + Signature | Yes            | Yes       | Yes             |

```text
Hash
    → Detects changes

Hash + Private Key
    → Proves sender

Hash + Private Key + Encryption
    → Proves sender + Hides message
```

---
