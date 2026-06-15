# Message Authentication

**Message authentication verifies:**
- Message came from claimed sender *(authentication)*
- Message was not modified during transmission *(integrity)*
- It does not necessarily provide confidentiality *(confidentiality)*


> An **authenticator** *(produced by authentication functions)* must be there to authenticate the message.

---
# Security & Authentication Requirements

#### Authentication Requirements:

| Attack                | Meaning                        |
| --------------------- | ------------------------------ |
| Masquerade            | Fake sender identity           |
| Content Modification  | Message contents changed       |
| Sequence Modification | Insert/delete/reorder messages |
| Timing Modification   | Delay messages                 |
| Replay Attack         | Reuse old valid message        |

#### Security Goals
- **Authentication** $\implies$ Who actually sent the message?
- **Integrity** $\implies$ Was the message changed?
- **Confidentiality** $\implies$ Can someone else read the message?

---
