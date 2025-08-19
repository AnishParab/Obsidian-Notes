# ### Next.js Jargon

- **Edge-Time Framework**:  
    Next.js is designed to execute code at the **time of the request**, often leveraging **Edge Functions** or **Serverless Functions**. This means your application doesn't run continuously like in traditional server-based architectures (e.g., Express.js on a long-running Node.js server).
- **On-Demand Execution**:  
    The app logic is executed **dynamically** in response to incoming requests. Pages are rendered (either server-side or at the edge) **only when needed**, improving scalability and reducing idle server costs.
	
> This contrasts with persistent backend servers, where apps are always "on" and listening for requests.

---
# Implications of Edge-Time Execution

> **Your database will _not_ remain connected persistently.**

- Since your app runs **on-demand** (in response to each request), the **database connection must be re-established** if it's not already present.
- **Repeated connection attempts** on every request (especially under high load) can **choke the app**, exhaust the database connection pool, or hit connection limits—leading to degraded performance or downtime.

---
