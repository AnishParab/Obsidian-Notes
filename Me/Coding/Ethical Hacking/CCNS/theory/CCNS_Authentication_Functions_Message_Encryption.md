# Message Encryption

> Ciphertext acts as the authenticator.

- Authentication can be achieved using encryption itself.
- Receiver decrypts the ciphertext and checks whether the resulting plaintext is meaningful.
- If only legitimate users possess the required key, a valid ciphertext indirectly proves the sender's identity.

---
# 1. **Symmetric**

- Uses a shared secret key `K`.
- Same key is used for encryption and decryption.
- Only sender and receiver know `K` **(Private)**

![[message_encryption_types_cryptography_symmetric.excalidraw|500]]

**Why Authentication Exists**
- If Bob successfully decrypts the ciphertext using `K`, he knows the sender must also know `K`.
- Since only Alice and Bob possess the key, ciphertext itself serves as proof of origin.

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Partially |
| Confidentiality | Yes       |

**Limitation:**
- Bob also knows `K`.
- Bob could create a valid ciphertext himself.
- **Partial Integrity:** Therefore symmetric encryption does **not provide nonrepudiation** (cannot guarantee that a user sent a specific message or performed an action)

**Example**
- Alice and Bob share:
```text
K = Secret123
```
- Alice sends:
```text
Transfer ₹1000
```
- Encrypted ciphertext:
```text
8F91A72C...
```
- An attacker cannot read the message and cannot create a valid ciphertext without knowing `K`.

---
# 2. **Asymmetric - Type 1**

> Confidentiality without Authentication

- Encrypt using B's Public Key
- Decrypt using B's Private Key

![[message_encryoption_asymmetric.excalidraw|500]]

**Why Confidentiality Exists**
- Anyone can know Bob's public key.
- Only Bob possesses Bob's private key.
- Therefore only Bob can decrypt.

**Why Authentication Does NOT Exist**
- Anyone can use Bob's public key.

**Example:**
```text
Alice → Encrypt(PUb)
```
or
```text
Eve → Encrypt(PUb)
```
- Both produce valid ciphertexts.
- Bob can decrypt the message but cannot determine who sent it.

| Property        | Supported |
| --------------- | --------- |
| Authentication  | No        |
| Integrity       | No        |
| Confidentiality | Yes       |

**Real-world Analogy**
- Bob publishes a locked mailbox.
- Anyone can drop a letter inside.
- Only Bob can open it.
- Bob knows the message is for him, but not who actually sent it.

---
# 3. **Asymmetric - Type 2**

> Authentication without Confidentiality

- Encrypt using A's Private Key
- Decrypt using A's Public Key


![[message_encryption_asymmetric_type_2.excalidraw|500]]

**Why Authentication Exists**
- Only Alice possesses `PRa`.
- If Bob successfully decrypts using `PUa`, Alice must have created the ciphertext.

**Why Confidentiality Does NOT Exist**
- Everyone knows Alice's public key.
- Anyone can perform:
```text
C → Decrypt(PUa) → M
```
- Therefore anybody can read the message.

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | No        |

**Example**
- Alice sends:
```text
Transfer ₹1000
```
- Encrypted with:
```text
PRa
```
- Bob decrypts using:
```text
PUa
```
- Bob now knows:
	- Message came from Alice
	- Message was not altered
- But everyone else can also read it.

**Mental Model**
```text
Private Key = Sign
Public Key = Verify
```
- This is the foundation of digital signatures.

---
# 4. **Dual encryption and decryption*#*

> Authentication + Confidentiality

- Sender:
```text
Encrypt(PRa)
Encrypt(PUb)
```
- Receiver:
```text
Decrypt(PRb)
Decrypt(PUa)
```

![[dual_encryption_and_decryption.excalidraw|800]]

**Why Authentication Exists**
- Only Alice possesses `PRa`.
- Successful verification proves Alice created the message.

**Why Confidentiality Exists**
- Only Bob possesses `PRb`.
- Only Bob can remove the outer encryption layer.

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | Yes       |

**Real-world Analogy**
1. Alice signs a letter with her unique signature.
2. Places it inside a locked box.
3. Locks the box using Bob's lock.
Result:
- Only Bob can open the box.
- Once opened, Bob can verify Alice's signature.

---
# Summary

| Method                        | Authentication | Confidentiality |
| ----------------------------- | -------------- | --------------- |
| Symmetric Encryption          | Yes            | Yes             |
| Asymmetric Type 1 (PUb → PRb) | No             | Yes             |
| Asymmetric Type 2 (PRa → PUa) | Yes            | No              |
| Dual Encryption               | Yes            | Yes             |

---
# Memory Rule

```text
Public Key of Receiver
    ⇒ Confidentiality

Private Key of Sender
    ⇒ Authentication

Both together
    ⇒ Authentication + Confidentiality
```

---
