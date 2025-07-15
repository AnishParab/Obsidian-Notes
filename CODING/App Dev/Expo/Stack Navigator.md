# What is a Stack Navigator?
- It is a pattern to navigate between different routes in an app.
- It allows transitioning between screens and managing the navigation history.

---
# Example
- You create a new file `app/details.tsx`
``` tsx
import { View, Text, StyleSheet } from 'react-native';

export default function DetailsScreen() {
  return (
    <View style={styles.container}>
      <Text>Details</Text>
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

But, this needs you to update **Root Layout component** and **import Stack**.

`app/_layout.tsx`
``` tsx
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack
      screenOptions={{
        headerStyle: {
          backgroundColor: '#f4511e',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}>
      <Stack.Screen name="index" />
      <Stack.Screen name="details" />
    </Stack>
  );
}
```

- `<Stack.Screen name={route_name} />` component in the layout file allows defining routes in a stack.

---








