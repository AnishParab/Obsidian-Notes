# What are Middlewares ?
- **Middleware** is a function that sits between the incoming request and the final request handler. It has access to the **request (req)**, the **response (res)**, and the function to pass control to the next middleware (**next()**).

![[Middleware.excalidraw|500]]

---
# Middlewares can do following things
- Read, modify, or log details from the **request**.
- Send a **response** and terminate the request–response cycle.
- Call `next()` to forward the request to the next middleware in the stack.
- Control the flow of the application by deciding whether to stop or continue.
- Be chained together — you can have **any number** of middlewares.
- Always execute **in sequence**, in the order they are added to the stack.

---
# Middlewares in Stack
![[MiddlewaresInStack.excalidraw|500]]

---
