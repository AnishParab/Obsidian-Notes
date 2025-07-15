---

---
# Expo Router
- It is a routing framework for **React Native** and **web-applications**.
- It provides **File-Based Routing**.
- It provides both **expo router navigation** and **react-native navigation**.

---
# `app` directory
- **Create your Routes here**.
- Any file you add to this directory becomes a route inside the native app.

---
# `app/index.tsx`, (It matches `/` route)
- This sets the **initial route**.
- It matches the `/` route.
``` tsx
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text>Home</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
```

---
# Also, `app/settings/index.tsx`
- This file matches `/settings` route.

---
# `app/_layout` file
- Defines shared **UI elements**, that persists between routes.

---
## Root Layout
- Traditionally, React Native Files are structured with a single root component ---> Defined as `App.js` or `index.js`.
- Similarly, the single root component for Expo is ---> `_layout.tsx` inside the **app** directory.

---
## Basic Code
- The following code exports a _default React component_ called **RootLayout**:

`app/_layout.tsx`
``` tsx
import { Stack } from 'expo-router';

export default function RootLayout() {
  return <Stack />;
}
```

---





