# My Understanding and Notes in Brief

- It only allows **Serapration of Concerns** of 
	- Routing
	- Business Logic
	- Rendering
- Rendering is required anyway and hence it **does not** make the code slower ore faster, it just modularizes the code.
- It still renders inside the request lifecycle and is not a background process.
- **Pug** is _synchronous_ by default, and hence CPU blocking.

**Hence**
- Using _Pug_ encourages Server-Side rendering (SSR) and Monolithic View Layer.
> Modern architectures like _React.js_ and _Next.js_ shifts rendering to client or hybrid SSR
> _Pug_ becomes less useful in API-only backends.

---
# With Pug (Template Engine)

### Advantages

- **Separation of concerns**
    - HTML structure kept out of route logic.
- **Dynamic rendering**
    - Easy variable injection, conditionals, loops.
- **Layout reuse**
    - `extends` / `block` reduce duplication.
- **Cleaner routes**
    - Routes focus on data, not markup.

---
### Disadvantages

- **Extra abstraction**
    - Another layer to debug (template compilation).
- **Non-standard syntax**
    - Indentation errors cause subtle bugs.
- **SSR coupling**
    - Ties backend to HTML rendering.
- **Not frontend-friendly**
    - Poor fit with modern SPA workflows.

---
# Without Pug (Plain HTML)

### Advantages

- **Zero abstraction**
    - What you send is what the browser receives.
- **Simpler debugging**
    - No compile step.
- **API-friendly**
    - Ideal for JSON responses and microservices.
- **Tool-agnostic**
    - Easy migration to frontend frameworks.

---
### Disadvantages

- **HTML duplication**
    - No layout inheritance.
- **Messy routes**
    - Markup mixed with server logic.
- **Poor scalability for SSR**
    - Complex pages become unmaintainable.

---
# Engineering Conclusion

```text
Pug → Useful for legacy SSR and small server-rendered apps
No Pug → Preferred for APIs and modern frontend-driven systems
```

For debugging legacy Express apps, understanding Pug is sufficient; using it in new systems is usually unnecessary.

---
