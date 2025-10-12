# Synchronous (Strong Coupling)
- **HTTP (REST / GraphQL)**
    - Client sends a request → waits for a response.
    - Tight coupling: both client and server must be available at the same time.
    - Examples: API calls, form submissions.
- **WebSockets (Debatable)**
    - Provides **full-duplex (two-way) persistent connections**.
    - Feels synchronous because messages are delivered instantly once connected.
    - However, can also support asynchronous event-driven communication.

---
# Asynchronous (Weak Coupling)
- **Message Queues (MQ)**
    - Messages stored temporarily in a queue (e.g., RabbitMQ, SQS, Kafka).
    - Sender doesn’t wait for receiver.
    - Useful for background jobs, task distribution.
- **Publish/Subscribe (Pub/Sub)**
    - Publishers emit events → Subscribers receive them without direct awareness of each other.
    - Decouples producers from consumers.
    - Examples: Kafka, Redis Pub/Sub, Google Pub/Sub.
- **Server-Sent Events (SSE)**
    - Unidirectional: server → client over HTTP.
    - Good for real-time updates like stock prices, live scores.
- **WebSockets (Again, Debatable)**
    - Can also be **asynchronous** if used in event-driven style.
    - Example: chat apps where messages are pushed without explicit request/response.

---
# **Rule of Thumb:**
> **Synchronous = blocking / request-response / tight coupling.**
 **Asynchronous = non-blocking / event-driven / loose coupling.**

---

