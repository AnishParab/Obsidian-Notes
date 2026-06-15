# Message Authentication Code (MAC)

> Fixed-length code generated using a message and a secret key. The MAC acts as the authenticator.

- MAC is generated using:
```text
MAC = F(K, M)
```
Where:
- `K` = shared secret key
- `M` = message
- `F` = authentication function

![[ccns_mac_authenticator.excalidraw|600]]

##### Working
- The receiver does **not trust the received MAC**.
- The receiver generates a new MAC using:
```text
MAC' = F(K, M)
```
- and compares:
```text
MAC == MAC'
```
- If equal:
	- Message is authentic
	- Message was not modified
- If not equal:
	- Message was altered
	- Wrong sender
	- Transmission error

##### **Authentication**
- Only sender and receiver know `K`.
- Example:
```text
K = Secret123
```
- Alice computes:
```text
MAC = F(K,M)
```
- and sends:
```text
M || MAC
```
- Eve intercepts the message.
- If Eve modifies:
```text
Transfer ₹1000
```
- to
```text
Transfer ₹10000
```
- she must generate a new valid MAC.
- Impossible without knowing `K`.
- Therefore:
- Sender authentication is achieved.

##### **Integrity**
- MAC depends on every bit of:
```text
Message + Key
```
- Even a one-bit change causes a completely different MAC.
- Example:
```text
Message:
HELLO
```
- might generate:
```text
A7F2C9
```
- Changing one letter:
```text
HELLo
```
- may generate:
```text
91BD54
```
- Receiver immediately detects modification.
- Therefore:
	- Message integrity is achieved.

##### **No Confidentiality**
- Message is transmitted in plaintext.
- Example:
```text
Transfer ₹5000
```
- with
```text
MAC = A7F2C9
```
- Sent as:
```text
Transfer ₹5000 || A7F2C9
```
- Anyone can read:
```text
Transfer ₹5000
```
- The MAC only proves:
	- who sent it
	- whether it changed
	- It does **not hide** the contents.
- Therefore:

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | No        |
##### Why Use MAC Instead of Encryption
- Sometimes secrecy is unnecessary.
- Example:
```text
Temperature = 35°C
```
- Nobody cares if others read it.
- But receiver wants assurance that:
	- message came from legitimate sensor
	- value was not modified
- Encrypting the entire message wastes computation.
- A MAC is sufficient.

---
# Authentication Tied to Plaintext

> MAC is generated from plaintext before encryption.

##### Working
- Generate MAC:
```text
MAC = F(K1,M)
```
- Append MAC:
```text
M || MAC
```
- Encrypt entire block:
```text
E(K2, [M || MAC])
```
- Transmit ciphertext.
- Receiver decrypts.
- Receiver recomputes MAC and verifies.

![[ccns_mac_with_encryption.excalidraw|1000]]

##### What Receiver Verifies
- Receiver checks:
```text
Received MAC
```
- against
```text
Generated MAC
```
- If equal:
	- Message authentic
	- Message unchanged

##### **Confidentiality**
- Entire message and MAC are encrypted.
- Attacker sees only ciphertext.
- Cannot determine:
	- Message contents
	- MAC value

##### **Authentication**
- After decryption:
	- Receiver verifies MAC using secret key.
	- Only legitimate sender could have generated correct MAC.

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | Yes       |
##### Why This Is Preferred
- Stallings explicitly prefers this approach.
- Reason:
	- The MAC protects the original plaintext.
	- Any modification becomes visible immediately after decryption.
	- Security is tied directly to the actual message.

---
# Authentication Tied to Ciphertext

> Message is encrypted first. MAC is generated from ciphertext.

##### Working
- Encrypt plaintext:
```text
C = E(K1,M)
```
- Generate MAC on ciphertext:
```text
MAC = F(K2,C)
```
- Transmit:
```text
C || MAC
```
- Receiver verifies MAC.
- Receiver decrypts ciphertext.

![[ccns_mac_with_encryption_type_2.excalidraw|1000]]

##### **Authentication**
- MAC still uses secret key.
- Receiver verifies:
```text
MAC == F(K2,C)
```
- Any ciphertext modification is detected.

##### **Confidentiality**
- Message remains encrypted.
- Attacker sees only ciphertext.

##### Important Difference
- Authentication is now protecting:
```text
Ciphertext
```
- instead of
```text
Plaintext
```

##### Advantage
- Receiver can verify authenticity **before decryption**.
- Useful when:
	- decryption is expensive
	- server receives huge amounts of traffic
- Reject forged messages early.

##### Limitation
- This is generally considered weaker than plaintext authentication.
- Reason:
	- Authentication is attached to encrypted data rather than the original message itself.
	- Stallings notes that plaintext authentication is usually preferred.

| Property        | Supported |
| --------------- | --------- |
| Authentication  | Yes       |
| Integrity       | Yes       |
| Confidentiality | Yes       |

---
# Comparison

|Feature|Plaintext Authentication|Ciphertext Authentication|
|---|---|---|
|MAC Computed On|Plaintext|Ciphertext|
|Encryption Order|After MAC|Before MAC|
|Authentication Protects|Original Message|Ciphertext|
|Verify Before Decryption|No|Yes|
|Preferred by Stallings|Yes|Less Preferred|

---
# Summary

```text
Hash
    = Integrity

MAC
    = Integrity + Authentication

Encryption
    = Confidentiality

Encryption + MAC
    = Integrity + Authentication + Confidentiality
```

---
