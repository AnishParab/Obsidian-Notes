# Websockets
- **Definition**: WebSockets establish a **persistent, full-duplex communication channel** over a single TCP connection between client (e.g., browser) and server.
- **Key Features**:
    - **Persistent Connection**: Unlike `HTTP`, the connection remains open after initial handshake.
    - **Full-Duplex**: Both client and server can send messages independently at any time.
    - **Low Latency**: Eliminates the overhead of repeated HTTP requests (polling).
    - **Protocol**: Starts as an HTTP(S) handshake, then upgrades to the WebSocket protocol.
- **Use Cases**:
	- **Real-Time Chat Applications**: Chat applications, live sports updates, real-time gaming, and any application requiring instant updates can benefit from WebSockets.
	- **Live Feeds**: Financial tickers, news feeds, and social media updates are examples where WebSockets can be used to push live data to users.
	- **Interactive Services**: Collaborative editing tools, live customer support chat, and interactive webinars can use WebSockets to enhance user interaction.

---
# Example
![[websockets.excalidraw|700]]

---
# Example
> **LeetCode** uses **Polling** instead of **WebSockets**.

---
> Never have a websocket connection for severless.

---
