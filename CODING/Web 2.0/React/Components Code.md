# Project Structure
``` css
src/
├── App.jsx
├── components/
│   └── Welcome.jsx

```

---
# Creating a Functional Component
- `export default` 
>1. It lets you import the component by name anywhere.
>2. It specifies the main component in the file.

`src/components/Welcome.jsx`
``` jsx
function Welcome() {
  return <h1>Hey there! 👋</h1>;
}

export default Welcome;
```

---
# Importing a Component
`src/App.jsx`
``` jsx
import Welcome from './components/Welcome'; // No need for .jsx extension

function App() {
  return (
    <div>
      <Welcome />
    </div>
  );
}

export default App;
```

---
# Using a Component with Children
- Use self-closing syntax, if no children.
``` jsx
<ComponentName>
  <p>Child content</p>
</ComponentName>
```

---
