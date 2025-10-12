# `app`
- Contains file-based app navigation.
- `app/(tabs)/index.tsx`
- `app/(tabs)/explore.tsx`---> This is your addition
- `app/(tabs)/_layout.tsx` ---> Sets up tab navigator

---
# `assets`
- `adaptive-icon.png` ---> Android
- `icon.png` ---> IOS
- `splash.png` ---> Project's splash screen
- `favicon.png` ---> Browser

---
# `components`
- Contains React Native components.
- `ThemedText.tsx` ---> Text elements uses app's color scheme in light and dark modes.

---
# `constants`
- `Colors.ts` ---> List of color values throughout the app.

---
# `hooks`
- Contains **React Hooks** sharing common behavior between components.

---
# `scripts`
- Contains reset-project.js, which can be run with `npm run reset-project`. This script will move the app directory to app-example, and create a new app directory with an index.tsx file.

---
# `app.json`
- Contains configuration options for the project and is called the app config. These options change the behavior of your project while developing, building, submitting, and updating your app.

---
# `package.json`
- The package.json file contains the project's dependencies, scripts, and metadata. Anytime a new dependency is added to your project, it will be added to this file.

---
# `tsconfig.json`
- Contains the rules that TypeScript will use to enforce type safety throughout the project.

---
