# Manual Installation
``` bash
npm i next@latest react@latest react-dom@latest
```

---
## `package.json`
``` json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
```
#### Scripts

- `next dev` ---> Starts development server.
- `next build` ---> Builds the application for production.
- `next start` ---> Starts the production server.
- `next lint` ---> Runs ESLint.

---
## Create `app` directory
- **NOTE** ---> Both _layout_ and _page_ match the `/` **route**.

---
#### Layout File
- This file contains the root layout.
##### `app/layout.tsx`
``` tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

**OR**

##### `app/layout.jsx`
``` jsx
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

---
#### Page File
- This is the Home Page of the app.
##### `app/page.tsx`
``` tsx
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```

**OR**

##### `app/page.js`
``` js
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```


---
## Public (Optional)
- To store static assets such as images, fonts, etc.

##### `app/page.js`
``` js
import Image from 'next/image'
 
export default function Page() {
  return <Image src="/profile.png" alt="Profile" width={100} height={100} />
}
```

**OR**

##### `app/page.tsx`
``` tsx
import Image from 'next/image'
 
export default function Page() {
  return <Image src="/profile.png" alt="Profile" width={100} height={100} />
}
```

---
