# Network Security Model

![[Pasted image 20260612183455.png]]

![[Pasted image 20260612184230.png]]

---
# Components

- **Sender/Recipient** — the communicating parties. Both must agree on the security transformation being used.

- **Message** — the original plaintext data being transmitted.

- **Security-related transformation** — the operation applied to the message before transmission, e.g. encryption, hashing, signing. Converts message → secure message.

- **Secret information** — the key or credential used by the transformation, e.g. encryption key, private key. Only known to authorized parties.

- **Secure message** — the transformed output that travels through the information channel. Unreadable or verifiable by unauthorized parties.

- **Information channel** — the medium of transmission, e.g. internet, network link. Assumed to be untrusted — opponent has access to it.

- **Opponent** — the attacker. Sits on the channel, can intercept, modify, or inject messages. This is the threat the entire model is designed to counter.

- **Trusted third party** — an entity both sender and recipient trust, e.g. Certificate Authority, key distribution center (KDC). Role: distribute secret information or arbitrate disputes. Not always present but critical in public key systems.

---
