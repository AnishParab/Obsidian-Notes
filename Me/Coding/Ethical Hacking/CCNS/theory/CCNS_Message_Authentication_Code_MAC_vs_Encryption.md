# Why Use MAC Instead of Encryption?

#### Reason 1: Confidentiality Not Required

- Sometimes message secrecy is unnecessary.

Example:
```text
Temperature = 35°C
```

Need:
- Authenticity
- Integrity

Don't need:
- Confidentiality

- MAC is sufficient.

---
#### Reason 2: Faster Than Encryption

- Computing MAC is generally cheaper than encrypting large messages.

Useful for:
- High-speed networks
- Large files

---
#### Reason 3: Verify Before Processing

- Receiver can verify authenticity immediately.
- Reject forged messages early.

---
#### Reason 4: Broadcast Communication

- One message sent to many receivers.
- Authentication is needed.
- Encryption may not be feasible.

---
