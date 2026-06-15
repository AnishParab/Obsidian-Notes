> MAC and Hash Codes are also called as *message digest*

---
# Authentication Functions

### 1. Message Encryption

> Ciphertext itself acts as an authenticator

**Use symmetric encryption.**
```text
M → Encrypt(K) → C
```

**Receiver decrypts:**
```text
C → Decrypt(K) → M
```

**Provides:**
- Authentication
- Integrity
- Confidentiality

**Limitation:**
- Encryption is expensive when confidentiality is not required.

---
### 2. Message Authentication Code (MAC)

> Fixed Length Code (MAC) produced by Authentication Function acts as the authenticator

**Uses:**
- Message M
- Secret Key K

**Produces:**
```text
MAC = F(K,M)    # {K, M} -> {key, message}
```
**Append and Send:**
```text
M || MAC        # Fixed length code (authenticator) [Appended]
```
- Receiver recomputes MAC and compares.

**Provides:**
- Authentication
- Integrity

**Does NOT provide:**
- Confidentiality
- We will have some authentication function and we apply them on the plaintext along with the key which produces a fixed length code called MAC

---
### 3. Hash Function

> Fixed Length Code (hash code) produced by Hash Function acts as the authenticator

**Uses only message.**
```text
H = Hash(M)
```

**Send:**
```text
M || H
```
- Receiver recomputes hash.

**Provides:**
- Integrity

**Does NOT provide:**
- Authentication
- Because anyone can generate the same hash.

---
# Comparison

| Feature             | Encryption | MAC | Hash     |
| ------------------- | ---------- | --- | -------- |
| Integrity           | Yes        | Yes | Yes      |
| Authentication      | Yes        | Yes | No       |
| Confidentiality     | Yes        | No  | No       |
| Secret Key Required | Yes        | Yes | No       |
| Fast                | No         | Yes | Very Yes |

| Mechanism         | Proves Sender? |
| ----------------- | -------------- |
| Hash Function     | No             |
| MAC               | Yes            |
| Digital Signature | Yes            |
| Encryption        | Sometimes      |

---
