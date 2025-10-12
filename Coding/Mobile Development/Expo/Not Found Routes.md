# What
- Expo router provides a special file called `+not-found.tsx`
- Handles files that are 404s.
- This route matches all unmatched routes from a nested level.

---
# `+not-found.tsx`
``` tsx
import { Link, Stack } from 'expo-router';
import { View, StyleSheet } from 'react-native';

export default function NotFoundScreen() {
  return (
    <>
      <Stack.Screen options={{ title: "Oops! This screen doesn't exist." }} />
      <View style={styles.container}>
        <Link href="/">Go to home screen</Link>
      </View>
    </>
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
