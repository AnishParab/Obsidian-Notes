#  Key Differences: `GET` vs `POST`

| GET                          | POST                           |
| ---------------------------- | ------------------------------ |
| Data in URL (query string)   | Data in request **body**       |
| Not secure (in logs/history) | More secure for sensitive data |
| Used to **retrieve**         | Used to **submit**             |

---
# Basic POST Request
``` html
<!DOCTYPE html>
<html>
<head>
  <title>AJAX POST Example</title>
</head>
<body>
  <h2>Send Message</h2>
  <input id="username" placeholder="Your name">
  <input id="message" placeholder="Your message">
  <button onclick="sendData()">Send</button>

  <div id="status"></div>

  <script>
    function sendData() {
      const xhr = new XMLHttpRequest();
      const url = "/api"; // we'll simulate this for now

      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          document.getElementById("status").innerText = xhr.responseText;
        }
      };

      const name = document.getElementById("username").value;
      const msg = document.getElementById("message").value;
      const data = `username=${encodeURIComponent(name)}&message=${encodeURIComponent(msg)}`;

      xhr.send(data);
    }
  </script>
</body>
</html>
```

---
# Server Side
``` bash
# python3 post_server.py
```

``` python
# post_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode('utf-8')
        print("Received POST data:", body)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"POST received successfully!")

server = HTTPServer(('localhost', 8000), Handler)
print("Listening on http://localhost:8000")
server.serve_forever()
```

Change js url to:
``` js
const url = "http://localhost:8000";
```

---
