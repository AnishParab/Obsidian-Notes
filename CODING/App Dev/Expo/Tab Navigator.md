# What is Tab Navigation?
- A common pattern to navigate between different sections of an app.
- The **component** used is `TabLayout()`.
- To use the tab navigator, any file or directory inside the `(tabs)` directory becomes a _route_ of the **tab navigator**.

---
# File Structure
``` css
app:
	- _layout.tsx
	- (tabs)
		- _layout.tsx
		- (home)
			- index.tsx
			- details.tsx
			- _layout.tsx
		- settings.tsx
```

---
# `app/(tabs)/_layout.tsx`
``` tsx
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="(home)" />
      <Tabs.Screen name="settings" />
    </Tabs>
  );
}
```

---
# Update the route in `app/_layout.tsx`
``` tsx
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" />
    </Stack>
  );
}
```

---

