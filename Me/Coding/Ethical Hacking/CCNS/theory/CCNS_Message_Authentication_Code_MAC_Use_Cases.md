# Two Basic Uses of MAC

#### 1. Message Authentication

Purpose:
```text
Verify sender identity
```
- Receiver trusts message only if MAC verifies.

Example:
- Bank transaction request.

---
#### 2. Message Authentication with Confidentiality

- MAC can be combined with encryption.

Process:
```text
Message
   ↓
MAC
   ↓
Encryption
```

Provides:
- Authentication
- Integrity
- Confidentiality

- This is common in secure communication systems.

---
