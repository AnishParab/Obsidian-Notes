# T3 Architecture Advantages

- App is partitioned into 3 logical components.
- Client machine is just a frontend and does not contain any direct DB calls.
- T3 Architectures are best for **WWW** applications.
- Advantages
	- **Scalability** due to distributed application servers.
	- **Data integrity**, App server acts as a middle layer between client and DB, which minimize the chances of data corruption.
	- **Security**, client can't directly access DB, hence it is more secure.

---
