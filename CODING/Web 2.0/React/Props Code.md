# Code
`src/components/Greet.jsx`
``` jsx
function Greet(props) {
  return <h2>Hello, {props.name}!</h2>;
}

export default Greet;
```

`src/App.jsx`
``` jsx
import Greet from './components/Greet';

function App() {
  return (
    <div>
      <Greet name="Anish" />
      <Greet name="Parab" />
    </div>
  );
}

export default App;
```

---
# Props with Multiple Values
``` jsx
<Greet name="Anish" age={22} isStudent={true} />
```

``` jsx
function Greet(props) {
  return (
    <div>
      <p>Name: {props.name}</p>
      <p>Age: {props.age}</p>
      <p>Status: {props.isStudent ? "Student" : "Not a student"}</p>
    </div>
  );
}
```

---
