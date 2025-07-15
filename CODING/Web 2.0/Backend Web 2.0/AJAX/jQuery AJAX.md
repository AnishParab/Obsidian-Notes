#  Why Use jQuery for AJAX?
- You can make **GET, POST, and full AJAX** requests in a single line.
- Handles cross-browser differences.
- Useful for quickly prototyping or working with older codebases.

---
#  Main jQuery AJAX Methods

| Method     | Use Case                                |
| ---------- | --------------------------------------- |
| `$.get()`  | GET request (fetch data)                |
| `$.post()` | POST request (send data)                |
| `$.ajax()` | Full control (any method, extra config) |

---
#  Add jQuery to Your Project
Just add this to your `<head>`:
```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

---
#  `$.get()` — Fetch XML (or any data)

```html
<!DOCTYPE html>
<html>
<head>
  <title>jQuery GET</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <h3>Click to fetch XML</h3>
  <button id="fetch">Fetch</button>
  <pre id="output"></pre>

  <script>
    $('#fetch').click(function () {
      $.get('data.xml', function (response) {
        $('#output').text(new XMLSerializer().serializeToString(response));
      });
    });
  </script>
</body>
</html>
```

> 🔁 This fetches `data.xml` and prints the raw XML as text.

---
# `$.post()` — Send Data

Assuming you're running a local test server (like the Python one from earlier):

```html
<!DOCTYPE html>
<html>
<head>
  <title>jQuery POST</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <input id="name" placeholder="Name">
  <button id="send">Send</button>
  <div id="response"></div>

  <script>
    $('#send').click(function () {
      const name = $('#name').val();

      $.post('http://localhost:8000', { username: name }, function (data) {
        $('#response').text(data);
      });
    });
  </script>
</body>
</html>
```

> 💡 jQuery handles encoding `username=name` for you.

---

# `$.ajax()` — Full Custom Control

```js
$.ajax({
  url: 'http://localhost:8000',
  type: 'POST',
  data: {
    username: 'anish',
    message: 'Yo!'
  },
  success: function (response) {
    console.log("Server says:", response);
  },
  error: function (xhr) {
    console.error("Error:", xhr.status);
  }
});
```

---
# Summary

| Method              | Description                 |
| ------------------- | --------------------------- |
| `$.get(url)`        | Simplified GET request      |
| `$.post(url, data)` | Send POST request           |
| `$.ajax({})`        | Fully customized AJAX calls |

---

