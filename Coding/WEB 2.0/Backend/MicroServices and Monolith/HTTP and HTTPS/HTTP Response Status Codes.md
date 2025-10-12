# What ?
- Indicates the outcome of a specific HTTP request.

---
# Responses are Grouped in Five Classes
1. **Informational (100–199)**
    - The request was received; the process is continuing.
    - Example: `100 Continue`
2. **Successful (200–299)**
    - The request was successfully received, understood, and accepted.
    - Example: `200 OK`, `201 Created`
3. **Redirection (300–399)**
    - Further action must be taken to complete the request (like redirecting to another URL).
    - Example: `301 Moved Permanently`, `302 Found`
4. **Client Errors (400–499)**
    - The request contains bad syntax or cannot be fulfilled.
    - Example: `400 Bad Request`, `401 Unauthorized`, `404 Not Found`
5. **Server Errors (500–599)**
    - The server failed to fulfill a valid request.
    - Example: `500 Internal Server Error`, `503 Service Unavailable`

---
# A neat mental trick:
- If it starts with **2**, all is well.
- If it starts with **4**, you (the client) messed up.
- If it starts with **5**, the server messed up.

---
