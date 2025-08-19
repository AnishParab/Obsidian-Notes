# `useRouter`
- Like React-Native, you can call a function using `onPress` handler to navigate to another page.
- Use **useRouter hook** to access navigation functions.

---
# Code
``` tsx
import { useRouter } from 'expo-router';
import { Button } from 'react-native';

export default function Home() {
  const router = useRouter();

  return <Button onPress={() => router.navigate('/about')}>Go to About</Button>;
}
```

---
