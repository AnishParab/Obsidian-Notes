# Using public folder (for static URLs)
- **Example : If you have `public/logo.png:`**
``` jsx
export default function Header() {
  return <img src="/logo.png" alt="Logo" />;
}
```

- **or, if your app is deployed under a subpath, use:**
``` jsx
<img src={`${process.env.PUBLIC_URL}/logo.png`} alt="Logo" />

```

---