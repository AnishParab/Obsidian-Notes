# Installation
``` bash
npm install --save-dev prettier eslint-config-prettier

```

---
# `eslint.config.mjs`
``` js
    // eslint.config.mjs
    import { FlatCompat } from '@eslint/eslintrc';

    const compat = new FlatCompat({
      baseDirectory: import.meta.dirname, // Available after Node.js v20.11.0
    });

    const eslintConfig = [
      ...compat.extends(
        'next',
        'next/core-web-vitals',
        // Add other configurations as needed, e.g., 'next/typescript'
        'prettier' // Must be last to apply Prettier's formatting
      ),
      // Add custom rules or plugins here
    ];

    export default eslintConfig;
```

---
# `prettierrc.json`
``` json
    {
      "semi": true,
      "singleQuote": false,
      "tabWidth": 2,
      "trailingComma": "es5"
    }
```

---
