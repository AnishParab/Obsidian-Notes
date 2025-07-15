# Analogy
Just like a function that return JSX (UI).

---
# Component Definition and Working
- It is a piece of UI that has its own logic and appearance.
- React components are JS functions that return **Markup**.

>**NOTE** ---> React Components always start with a    capital letter.

---
# Example Code for Component and it's Nesting

1. **Example** ---> `MyButton.jsx`
``` jsx
function MyButton() {
  return (
    <button>I'm a button</button>
  );
}
```
Now that you have declared `MyButton`, you can **nest it into another component.**

2. **Example** ---> `MyApp.jsx`
``` jsx
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

3. **Final Code:**
``` jsx
function MyButton() {
  return (
    <button>I'm a button</button>
  );
}

export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

---
# Two Types
### Functional Components (Modern Way)
``` jsx
function Welcome() {
  return <h1>Hello from Functional Component!</h1>;
}

// OR using arrow function
const Welcome = () => <h1>Hello from Functional Component!</h1>;

```

### Class Components (Legacy Code)
- ES6 class that extends `React.Component`.
- Uses a `render()` method to return JSX.

``` jsx
import React, { Component } from 'react';

class Welcome extends Component {
  render() {
    return <h1>Hello from Class Component!</h1>;
  }
}

```

---

