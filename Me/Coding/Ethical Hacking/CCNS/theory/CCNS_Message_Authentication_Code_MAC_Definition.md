# MAC (Message Authentication Code)

#### **NOTE:**
```text
Hash
    → Anyone can generate

MAC
    → Only key holders can generate
```

---
# Definition

- A MAC is a fixed-length authentication tag generated using:

```text
MAC = F(K,M)
```
Where:
- `K` = shared secret key
- `M` = message
- `F` = MAC algorithm

- The generated MAC is attached to the message.
- Receiver recomputes the MAC and compares.

---
# Why Do We Need MAC?

#### **Plain hash:**
```text
M → H(M)
```
- Problem:
- Anyone can compute:
```text
H(M)
```
- including attackers.
- No sender authentication.

#### **MAC:**
```text
M + Secret Key
        ↓
      MAC
```
- Now only users possessing the secret key can generate a valid MAC.
- Authentication becomes possible.

---
# Working of MAC

**Refer this:**
[[CCNS_Authentication_Functions_MAC]]

Sender:
```text
MAC = F(K,M)
```

Transmits:
```text
M || MAC
```

Receiver:
```text
MAC' = F(K,M)
```

Compare:
```text
MAC == MAC'
```

If equal:
- Sender authenticated
- Message unchanged

If unequal:
- Forgery
- Modification
- Wrong key

---
