# Saving Images in `src/assets`
- This is how you import and use the image in a component:
``` jsx
import React from 'react';
import Logo from '../assets/logo.png';

export default function Header() {
  return <img src={Logo} alt="Logo" />;
}
```
**Explanation:**
- The bundler (e.g., Vite/Webpack) processes the image.
- Optimizes, hashes, copies to the `dist/` folder.
- `Logo` is a URL string that the bundler replaces at build time.

---
