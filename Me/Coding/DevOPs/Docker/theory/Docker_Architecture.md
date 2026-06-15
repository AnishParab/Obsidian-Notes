# Docker Architecture

![[Pasted image 20260517134251.png]]

---
# Key relationships to internalize:

- **Client** just sends commands — all the actual work is done by the daemon
- **Images** are pulled from the registry, **containers** are spawned from images, **volumes** persist container data
- **Networks** connect containers to each other and the outside world — bridge is the defaultb

---
