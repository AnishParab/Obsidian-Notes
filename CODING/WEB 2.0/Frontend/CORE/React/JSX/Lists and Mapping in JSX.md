``` jsx
const langs = ['Rust', 'Go', 'Python'];

function App() {
  return (
    <ul>
      {langs.map((lang, i) => <li key={i}>{lang}</li>)}
    </ul>
  );
}
```

---
# For more info...
[[Rendering Lists]]

---
