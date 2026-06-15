# Security Service

- Processing or communication service that provides protection to system resources
- Implements security policies via security mechanisms

---
# Types

#### Authentication
- Verifying identity of communicating entities
- **Peer Entity** — confirms identity during a session, e.g. TLS handshake
- **Data Origin** — confirms source of a message, no replay protection, e.g. email sender verification

#### Access Control
- Prevents unauthorized use of resources
- Controls who can access what and under what conditions
- e.g. file permissions, firewall rules, RBAC

#### Data Confidentiality
- Protects data from unauthorized disclosure
- **Connection confidentiality** — protects all data on a connection
- **Selective field confidentiality** — encrypts specific fields, e.g. password field only
- **Traffic flow confidentiality** — hides frequency, length, source, destination

#### Data Integrity
- Ensures data is not altered in transit
- **Connection integrity with recovery** — detects modification and recovers
- **Connection integrity without recovery** — detects and alerts only
- **Selective field integrity** — protects specific fields in a message
- **Connectionless integrity** — detects modification of individual messages, e.g. MAC on a packet

#### Non-repudiation
- Prevents denial of sending or receiving a message
- **Origin** — proof sender sent the message, e.g. digital signature
- **Destination** — proof receiver received the message, e.g. signed delivery receipt

---
