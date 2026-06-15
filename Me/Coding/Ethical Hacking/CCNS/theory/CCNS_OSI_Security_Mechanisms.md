# Security Mechanism

- A process or device designed to detect, prevent, or recover from a security attack
- Implements security services defined by security policies
- No single mechanism supports all services

---
# Types
#### Specific Security Mechanisms
- Incorporated into specific protocol layers of the OSI model
- **Encipherment**
	- Transforms data into unreadable form using an algorithm + key
	- Key required to encrypt and/or decrypt
	- Basis for confidentiality and supports other mechanisms
- **Digital Signature**
	- Data appended to a message to prove origin and integrity
	- Sender encrypts a hash of the message with their private key
	- Receiver verifies using sender's public key
	- Provides authentication and non-repudiation
- **Access Control**
	- Enforces access rights to resources
	- Uses identity, role, or clearance level to allow/deny
	- e.g. ACLs, RBAC, passwords
- **Data Integrity**
	- Mechanisms to detect unauthorized modification
	- Sender appends a check value (e.g. MAC, hash) to message
	- Receiver recomputes and compares
	- Detects alteration in transit
- **Authentication Exchange**
	- Confirms identity through information exchange
	- e.g. challenge-response, passwords, cryptographic tokens
	- Used in peer entity authentication
- **Traffic Padding**
	- Inserts dummy data into traffic stream
	- Prevents traffic analysis by obscuring frequency, length, and pattern
	- e.g. sending fixed-size packets at constant intervals
- **Routing Control**
	- Selects specific routes for data transmission
	- Avoids compromised or untrusted nodes
	- Can dynamically reroute if a breach is detected
- **Notarization**
	- Trusted third party assures properties of data exchange
	- e.g. SSL certificates issued by a Certificate Authority (CA)
	- Provides integrity, origin, time, and destination assurance

#### Pervasive Security Mechanisms
- Not tied to any specific OSI layer
- Applied across the entire system
- **Trusted Functionality**
	- Ensures components behave according to security policy
	- Basis for other security mechanisms
- **Security Label**
	- Marking bound to a resource indicating its sensitivity level
	- e.g. Confidential, Top Secret, Public
- **Event Detection**
	- Detects security-relevant events
	- e.g. failed login attempts, unauthorized access, intrusion detection
- **Security Audit Trail**
	- Logs and records security-relevant events for review
	- Used for forensic analysis and accountability
- **Security Recovery**
	- Handles requests from mechanisms and takes recovery action
	- e.g. immediate action (block), temporary action (session termination), long-term action (blacklist)

---
