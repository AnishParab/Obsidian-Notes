# T1 Architecture (Single-Tier)
- All components (UI, application logic, and database) reside on **one machine**.
- Used in **personal or small-scale** applications.

🔸 *Example:*  
> MS Access on a local machine

---
# T2 Architecture (Two-Tier)
- Divided into:
  - **Client** (UI + application logic)
  - **Database Server**

- Client sends queries directly to the DB server using **query language** (like SQL).

*Example:*  
> Java application using JDBC to query PostgreSQL

**Diagram:**  
`Client App ↔️ DB Server`  
*(as per: ![[dbms_2_tier_architecture.excalidraw]])*

---
# T3 Architecture (Three-Tier)
- Components:
  1. **Client Tier** – UI (Frontend only)
  2. **Application Tier** – Business logic layer (App Server)
  3. **Database Tier** – Stores and manages data

- Client does **not** interact with the DB directly.

*Example:*  
> Web browser (Client) → Node.js server (App Tier) → MySQL (DB)

**Diagram:**  
`Client ↔ App Server ↔ DB Server`  
*(as per: ![[t3_architecture_dbms.excalidraw|500]])*

---
### Advantages of T3:
- **Scalability** – Can handle more users
- **Data Integrity** – Logic centralized in app server
- **Security** – DB is not exposed directly to clients

---
