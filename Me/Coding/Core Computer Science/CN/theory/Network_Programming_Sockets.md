# Sockets

- Everything in UNIX is a file
- When UNIX programs do any sort of I/O, they do it by reading and writing to a file descriptor.
- A file descriptor is simply an integer associated with an open file.
- It can be a network connection, a FIFO, a pipe, a terminal, a real on-the-disk file or just anything else.

- You make a call to the `socket()` system routine 
- `send()` and `recv()` offer a much greater control over your data transmission, it offers a much greater control than just `read()` and `write()`

- There are many types of sockets
	- DARPA Internet adderesses (Internet sockets)
	- path names on a local node (Unix Sockets)
	- CCITT X.25 addresses

---
