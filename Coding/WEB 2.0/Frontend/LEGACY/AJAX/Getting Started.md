# Introduction
- Asynchronous Javascript and XML.
- It is a technique and not a language used in web development.
- Send/Receive data from a server asynchronously without refreshing the entire page.
- Makes the website faster and more dynamic.
- It’s a technique for making **asynchronous HTTP requests** from the browser to a server **without refreshing the page**.

---
# Why?
Before AJAX, anytime you interacted with a website (like submitting a form), the **entire page had to reload**. AJAX allows just a small part of the page to update, giving a smoother, faster, and more dynamic user experience.

---
# Traditional vs AJAX Example:
##  Traditional Request:
- Click a link → Server sends back full HTML → Page reloads.
##  AJAX:
- Click a link → JS sends request → Receives just data → Updates _part_ of the page.

---
# Flow
1. JS triggers an AJAX call (via XMLHttpRequest or Fetch).
2. AJAX sends HTTP request (GET, POST, etc.) to the server.
3. Server processes it and sends back response data.
4. JS takes that data and updates the DOM (partial DOM updation).

---










