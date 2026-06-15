# Security Attack

- Deliberate attempt to evade security services and violate security policy

**Two Types**
- Passive Attacks
- Active Attacks

---
# Passive Attacks

- Learn or make use of information without affecting system resources
- Goal: obtain information being transmitted
- Hard to detect — sender and receiver are unaware
- Emphasis on **prevention** (encryption) over detection

#### Types
- **Release of message contents**
	- Intercepting and reading the actual payload of a communication.
	- Works when data is unencrypted.
	- e.g. reading a plaintext email, capturing an HTTP request with credentials.
- **Traffic Analysis** 
	- Even when content is encrypted, metadata leaks information:
	- **Frequency** — how often two parties communicate reveals relationship
	- **Length** — long messages may indicate file transfers or bulk data
	- **Timing** — bursts of traffic may correlate with real-world events
	- **Pattern** — regular intervals may indicate automated/command traffic
	- Encryption hides content but not the fact that communication is happening.

---
# Active Attacks

- Modification of data stream or creation of a false stream
- Goal: disrupt, corrupt, or fabricate communication
- Hard to prevent due to many vulnerabilities
- Emphasis on **detection and recovery**
- Detection itself can deter future attacks

#### Types
- **Masquerade**
	- Attacker impersonates a legitimate entity to gain unauthorized access.
	- e.g. fake login page, spoofed IP address, forged email sender.
	- Often combined with other attacks — masquerade first, then replay or modify.
- **Replay**
	- Attacker captures a valid transmission and retransmits it later.
	- The content is legitimate — the attack is in the repetition.
	- e.g. capturing an auth token and replaying it to authenticate without credentials. Countered by timestamps and session tokens.
- **Modification of messages**
	- Legitimate message is intercepted and altered before reaching destination.
	- e.g. changing "transfer $100 to Alice" to "transfer $10000 to Attacker".
	- Countered by message authentication codes (MACs).
- **Denial of Service**
	- Overwhelms a resource so legitimate users can't access it.
	- Two angles:
		- **Volume** — flood with traffic, e.g. UDP/TCP flood
		- **Exploitation** — abuse protocol behavior, e.g. SYN flood exploits TCP handshake, server holds half-open connections until resources exhaust
	- DDoS = distributed DoS, same goal but traffic comes from many sources (botnet), much harder to block.

---
# Passive vs Active

|                  | Passive                | Active                          |
| ---------------- | ---------------------- | ------------------------------- |
| Goal             | Obtain information     | Disrupt / falsify               |
| Effect on system | None                   | Yes                             |
| Detection        | Hard                   | Easier                          |
| Prevention       | Easier (encryption)    | Hard                            |
| Approach         | Prevent over detect    | Detect and recover              |
| Risk             | Confidentiality breach | Integrity / availability breach |

---
