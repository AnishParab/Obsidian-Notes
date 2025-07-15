- Next.js has in-built support for the `"paths"` and `"baseUrl"` options of `tsconfig.json` and `jsconfig.json` files.

- Hence you can alias project directories to absolute paths.

``` tsx
// Before
import { Button } from '../../../components/button'
 
// After
import { Button } from '@/components/button'
```

---
# Configure Absolute Imports **`baseURL`**
`tsconfig.json` or `jsconfig.json`
``` json
{
  "compilerOptions": {
    "baseUrl": "src/"
  }
}
```

---
# Use **path** option to **alias** module paths
- For example, the following configuration maps `@/components/*` to `components/*`:

`tsconfig.json` or `jsconfig.json`
``` json
{
  "compilerOptions": {
    "baseUrl": "src/",
    "paths": {
      "@/styles/*": ["styles/*"],
      "@/components/*": ["components/*"]
    }
  }
}
```

---
