# Hello World Example
``` js
import express from 'express';
const app = express();

app.get('/', function(req, res) {
  res.end('Hello World');
});

app.get('/contact-us', function(req, res) {
  res.end('You can contact me at my email address');
});

app.post('/tweets', (req, res) => {
  res.status(201).end('Tweet created successfully');
});

app.listen(8000, () => console.log(`Server is running on PORT 8000`));
```

- The app now runs on port 8000.

---
> By default, Express sends a status code of **200**.

---
