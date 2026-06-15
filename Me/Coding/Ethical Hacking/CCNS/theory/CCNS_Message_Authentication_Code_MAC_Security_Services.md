# Security Services Provided

#### Authentication
- Only legitimate users know:
```text
K
```
- Therefore only they can create valid MACs.

#### Integrity
- Even one-bit modification changes the MAC.
- Example:
```text
Transfer ₹1000
```
- becomes
```text
Transfer ₹10000
```
- MAC verification fails.

#### No Confidentiality
- Message is still visible.
- Transmission:
```text
Message || MAC
```
- Anyone can read:
```text
Message
```
- MAC only proves:
	- Who sent it
	- Whether it changed

---
# Why MAC Does Not Provide Nonrepudiation

Suppose:
```text
Alice ↔ Bob
```

Both know:
```text
K
```

- Valid MAC exists.

Question:
- Who created it?

Possible answers:
- Alice
- Bob

- Both know the key.
- Impossible to prove.

Therefore:
```text
MAC ≠ Nonrepudiation
```

---
# Security Requirements of MAC

#### 1. Forgery Resistance
Given:
```text
M
MAC(K,M)
```
Attacker should not be able to generate:
```text
MAC(K,M')
```

#### 2. Collision Resistance
Different messages should not produce same MAC.
```text
MAC(K,M1)
    ≠
MAC(K,M2)
```

#### 3. Uniform Distribution
- MAC values should appear random.
- No predictable patterns.

---
