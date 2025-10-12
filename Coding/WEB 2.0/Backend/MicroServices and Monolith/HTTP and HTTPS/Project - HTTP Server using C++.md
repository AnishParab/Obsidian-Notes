# High Level Design
- This server will use a `TCP/IP` socket registered to an `IP` address on the computer.
- It will also have a specific `port` through which the socket will listen for incoming network connections.
- Network connections that come into our server will be stored on a **Queue** of network threads.

---
