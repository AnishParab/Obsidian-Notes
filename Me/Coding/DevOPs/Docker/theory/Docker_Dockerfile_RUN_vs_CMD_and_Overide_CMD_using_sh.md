# `RUN` v/s `CMD`

- Both are Dockerfile instructions but run at completely different phases

|               | `RUN`                        | `CMD`                            |
| ------------- | ---------------------------- | -------------------------------- |
| Phase         | Build time                   | Container runtime                |
| Level         | Image                        | Container                        |
| Creates layer | Yes                          | No                               |
| Use case      | Install deps, compile, setup | Start the app process            |
| Frequency     | Runs once during build       | Runs every time container starts |

- `RUN npm install` → bakes `node_modules` into the image layer
- `CMD ["npm", "run", "dev"]` → starts the dev server *when the container runs*
- Only one `CMD` is effective per Dockerfile — last one wins

**Override `CMD` using `sh`**
- `CMD` can be overridden at runtime: `docker run vite-test:2 sh`

---
