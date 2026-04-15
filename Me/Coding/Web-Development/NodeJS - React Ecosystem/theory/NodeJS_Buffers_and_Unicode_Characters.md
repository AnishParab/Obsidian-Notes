# Unicode Characters
#### Unicode

- Universal character standard assigning a **code point** to each character.
- Independent of storage or encoding.
#### UTF-8

- Variable-length encoding (1–4 bytes).
- Backward compatible with ASCII.
- Memory efficient for English-heavy text.
- Default encoding for web and Node.js.
#### UTF-16

- Variable-length encoding (2 or 4 bytes).
- Uses **code units** instead of direct code points.
- Common in JavaScript internal string representation.

---
# Buffers in Node.js

- A buffer is a temporary storage area for binary data.
- Node.js does not support direct binary manipulation (like C/C++), so buffers help handle raw data efficiently.
- Used mostly when dealing with file streams, network data, and binary protocols.

---
# Why do we need Buffers ?

- JavaScript strings are UTF-16 encoded, making direct binary data handling inefficient.
- Buffers store binary data outside V8's heap.
- Useful when working with:
	- File System (fs module)
	- Networking (TCP, UDP, WebSockets)
	- Streams (Handling chunks of data)

---
