# Two Types of Internet Sockets

- Stream Sockets - `SOCK_STREAM` - uses *TCP* - data arrives in order
- Datagram Sockets - `SOCK_DGRAM` - Sometimes called as "connectionless sockets" - Uses *IP* - Data arrives out of order

---
- `telnet` and `ssh` use stream sockets
- `http` uses stream sockets to get pages

---
`UDP` is a good choice for it's speed but it's less reliable

---
# OSI

Application
- telnet, ftp etc

Host-to-Host Transport Layer
- TCP, UDP

Internet Layer
- IP and routing

Network Access Layer
- Ethernet, wi-fi

---
- All you have to do is stream sockets is `send()` the data out
- All you have to do for datagram sockets is encapsulate the packlet in the method of your choosing and `sendto()` it out.
- The kernel builds the Transport Layer and Internet Layer for you and the hardware does the Network Access Layer

---
