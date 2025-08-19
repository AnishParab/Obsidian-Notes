# What is ESLint?
 - It is a static code analysis tool for JS and TS.
 
**ESLint is useful for the following reasons.**
- It enforces coding standards and style.
- Catches bugs early.
- Improves code quality and readability.
- Works well in teams to keep everyone's code consistent.

---
# ESLint in NextJS
- Built-in ESLint.
- Automatically installs the necessary packages and configures the proper settings when you create a new project with `create-next-app`.
- To manually add ESLint to an existing project, add `next lint` as a script to `package.json`.

`package.json`
``` json
{
  "scripts": {
    "lint": "next lint"
  }
}
```
- Then run `npm run lint` and you will be guided through the installation and configuration process.

---
# `next lint`
- You can now run `next lint` command every time you want to run ESLint to catch errors. 

---
