# Navigation
- To navigate between routes, use built-in components like **Link component**.
- It uses the `href` prop with the route to navigate.

`app/index.tsx`
``` tsx
import { Link } from 'expo-router';
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text>Home</Text>
      <Link href="/details">View details</Link>
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
# How **Link** Works
- `Link` wraps the children in a `Text` by default.
- This can be easily customized, example :- use a different button component.
- **Refer** _[[Navigating Between Pages]]_

---
