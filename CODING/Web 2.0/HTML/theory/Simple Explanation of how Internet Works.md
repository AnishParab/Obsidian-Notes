---

---
#  ARPANET
- **ARPANET** (Advanced Research Projects Agency Network) was the first operational packet-switching network.
- It laid the foundation for the modern Internet.
- **Key feature**: Used **packet switching** — breaking data into small packets before transmission.

---
#  Protocol Stack and Packets
###  What is a Protocol?
- A **protocol** is a set of rules that define how data is transmitted over a network.
- Example: **SMTP** (Simple Mail Transfer Protocol) – used for sending emails.
###  Protocol Stack Diagram:

```text
+---------------------+     <-- Application Layer (HTTP, SMTP, FTP)
|  Application Layer  |
+---------------------+     <-- Transport Layer (TCP, UDP)
|  Transport Layer     |
+---------------------+     <-- Network Layer (IP, ICMP)
|  Internet Layer      |
+---------------------+     <-- Link Layer (Ethernet, Wi-Fi)
|  Link/Hardware Layer |
+---------------------+
```

###  Packet:
- A **packet** is a small unit of data sent over a network.
- Each layer adds its own **header** (and sometimes footer) to the data — this process is called **encapsulation**.

---
# How a Packet Travels Over the Internet
``` txt
Client
  ↓
Local Router
  ↓
Local ISP
  ↓
Regional Router
  ↓
Regional ISP
  ↓
National Router
  ↓
National ISP
  ↓
Destination Server
```

---
#  Networking Tools
##  Router
- **Function**: Forwards data packets between computer networks.
- **Routing Table**: Maintains a map of IP addresses and routes.

##  Other Tools:
- **Switch**: Forwards data within a LAN using MAC addresses.
- **Modem**: Converts digital data into a format suitable for a transmission medium (like coaxial cable).
- **Firewall**: Filters incoming and outgoing traffic based on rules.
- **Load Balancer**: Distributes network or application traffic across servers.
- **DNS Resolver**: Resolves domain names to IP addresses.

---
# Domain Name Resolution
``` text
Client -> www.google.com
       -> DNS Query
       -> DNS Resolver (checks cache or asks root/authoritative DNS)
       -> Gets IP address (e.g., 142.250.192.46)
       -> Sends Request to Server via ISP
```

---
#  Protocols
Here are some common Internet protocols categorized by function:
###  Email:
- **SMTP** – Sending mail
- **IMAP / POP3** – Retrieving mail
###  Web:
- **HTTP / HTTPS** – Web browsing
###  File Transfer:
- **FTP / SFTP** – File transfers
###  Network Management:
- **ICMP** – Diagnostics (used in ping)
- **SNMP** – Network device management
###  Transport:
- **TCP** – Reliable communication
- **UDP** – Fast, connectionless transmission

---
# IPv4 vs IPv6
| Feature        | IPv4                        | IPv6                                      |
| -------------- | --------------------------- | ----------------------------------------- |
| Address Length | 32 bits                     | 128 bits                                  |
| Format         | Decimal (e.g., 192.168.0.1) | Hexadecimal (e.g., 2001:0db8::1)          |
| Address Space  | ~4.3 billion addresses      | ~340 undecillion addresses                |
| Header Size    | 20 bytes                    | 40 bytes                                  |
| Security       | Optional (via IPSec)        | Built-in (IPSec mandatory)                |
| NAT Support    | Common                      | Not typically needed (huge address space) |
| Deployment     | Widely deployed             | Growing adoption                          |

----




