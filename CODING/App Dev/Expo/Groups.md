# What is a Group?
- A group is created to organize similar routes or a section of the app.
- Should be named inside parenthesis, like `(group_name)`
- Each group has a **layout file**.

---
# File Structure Before
``` css
app:
	- _layout.tsx
	- index.tsx
	- details.tsx
```

---
# File Structure Now
``` css
app:
	- _layout.tsx
	- (home)
		- _layout.tsx
		- index.tsx
		- details.tsx
```

---
# `app/(home)/_layout.tsx`
``` tsx
import { Stack } from 'expo-router';

export default function HomeLayout() {
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

---
# `app/_layout.tsx`
``` tsx
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="(home)" />
    </Stack>
  );
}
```

---
