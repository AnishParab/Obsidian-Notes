# Use-Case
- Configure application.
- Manage dependencies.
- Run middleware.
- Integrate monitoring tools.
- Define Environment Variables.

---
# Structure
|                                                                                                |                                         |
| ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| **Next.js**                                                                                    |                                         |
| [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js)            | Configuration file for Next.js          |
| [`package.json`](https://nextjs.org/docs/app/getting-started/installation#manual-installation) | Project dependencies and scripts        |
| [`instrumentation.ts`](https://nextjs.org/docs/app/guides/instrumentation)                     | OpenTelemetry and Instrumentation file  |
| [`middleware.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/middleware)       | Next.js request middleware              |
| [`.env`](https://nextjs.org/docs/app/guides/environment-variables)                             | Environment variables                   |
| [`.env.local`](https://nextjs.org/docs/app/guides/environment-variables)                       | Local environment variables             |
| [`.env.production`](https://nextjs.org/docs/app/guides/environment-variables)                  | Production environment variables        |
| [`.env.development`](https://nextjs.org/docs/app/guides/environment-variables)                 | Development environment variables       |
| [`.eslintrc.json`](https://nextjs.org/docs/app/api-reference/config/eslint)                    | Configuration file for ESLint           |
| `.gitignore`                                                                                   | Git files and folders to ignore         |
| `next-env.d.ts`                                                                                | TypeScript declaration file for Next.js |
| `tsconfig.json`                                                                                | Configuration file for TypeScript       |
| `jsconfig.json`                                                                                | Configuration file for JavaScript       |

---
