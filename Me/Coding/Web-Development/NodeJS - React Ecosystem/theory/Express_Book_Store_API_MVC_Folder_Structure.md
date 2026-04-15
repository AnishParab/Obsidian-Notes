# MVC Pattern

``` bash
project-root/
│
├── index.js                 # Process entry (server start)
├── app.js                   # Express app configuration
│
├── routes/
│   └── books.routes.js      # HTTP route definitions
│
├── controllers/
│   └── books.controller.js  # Request handlers
│
├── middleware/
│   ├── error.middleware.js
│   └── validate.middleware.js
│
├── models/
│   └── books.store.js       # In-memory data store abstraction
│
├── config/
│   └── server.config.js
│
└── package.json
```

---
