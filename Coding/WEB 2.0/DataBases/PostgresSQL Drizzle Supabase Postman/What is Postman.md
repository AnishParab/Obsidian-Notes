# What is Postman?
- API testing & collaboration tool.
- Lets you **send HTTP requests** and inspect responses (headers, body, status codes).
- Useful for debugging, automation, and documenting APIs.

---
# Core Features
- **Collections**: Group of saved API requests (organized by project/module).
- **Environments**: Store variables (e.g. `{{base_url}}`, `{{auth_token}}`) for dev/staging/prod.
- **Requests**: Each request defines:
    - Method: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
    - URL: Can use variables (`{{base_url}}/users`)
    - Headers: `Content-Type`, `Authorization`, etc.
    - Body: Raw JSON, form-data, x-www-form-urlencoded, GraphQL, etc.

---