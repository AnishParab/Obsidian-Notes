# What is an API
- It basically allows different systems to communicate with each other.

---
# API Authentication
- So that only authorized clients can access these API's.
- Process of verifying the identity of a client or user trying to access an API.

- Ensure Security.
- Control Access (Different Clients have different permissions).
- Monitor Usage.
- Apply Rate Limiting (So that API isn't overwhelmed by too many requests from a single source).

---
# Several Ways to Authenticate API Requests
- Method you choose depends on your security requirements and complexity of your system.

## HTTP Basic Authentication
- Simplest
- Client sends a **username and password** in the **HTTP Header** encoded in **base64**.
- Not secure, since credentials are sent with every request.
- These credentials are not encoded or encrypted by default.
- Insecure, unless used in conjunction with **HTTPS**.

## API Key Authentication 
- Client sends a unique **API Key** to **API Server**.
- Issued by **API Provider** to the client.
- Simple, but offers limited control over who can use the API.

---
