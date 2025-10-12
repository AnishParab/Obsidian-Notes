# Structure

| File Name      | Extensions        | Purpose                      |
| -------------- | ----------------- | ---------------------------- |
| `layout`       | .js / .jsx / .tsx | Layout                       |
| `page`         | .js / .jsx / .tsx | Page                         |
| `loading`      | .js / .jsx / .tsx | Loading UI                   |
| `not-found`    | .js / .jsx / .tsx | Not found UI                 |
| `error`        | .js / .jsx / .tsx | Error UI                     |
| `global-error` | .js / .jsx / .tsx | Global error UI              |
| `route`        | .js / .ts         | API endpoint                 |
| `template`     | .js / .jsx / .tsx | Re-rendered layout           |
| `default`      | .js / .jsx / .tsx | Parallel route fallback page |

---
# Nested Routes

| Folder Structure     | Purpose                |
|---------------------|------------------------|
| `folder`            | Route segment          |
| `folder/folder`     | Nested route segment   |

---
# Dynamic Routes

| Folder / File Name    | Purpose                          |
|----------------------|----------------------------------|
| `[folder]`           | Dynamic route segment            |
| `[...folder]`        | Catch-all route segment          |
| `[[...folder]]`     | Optional catch-all route segment |

---
# Route Groups and Private Folders

| Folder Name       | Purpose                                                        |
|------------------|----------------------------------------------------------------|
| `(folder)`       | Group routes without affecting the URL (routing)                |
| `_folder`        | Opt folder and all child segments out of routing (ignored)     |

---
# Parallel and Intercepted Routes

| Folder Name         | Purpose                                        |
|--------------------|-----------------------------------------------|
| `@folder`          | Named slot                                    |
| `(.)folder`       | Intercept from same level                      |
| `(..)folder`      | Intercept from one level above                  |
| `(..)(..)folder`  | Intercept from two levels above                 |
| `(...)folder`     | Intercept from root                             |

---
