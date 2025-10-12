# Data Fetcher Component
``` jsx
import React, { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, []);
  //it willl run only on 1st render

  return (
    <div>
      {loading ? (
        <h1>Loading...</h1>
      ) : (
        <ul>
          {data.map(post => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
export default DataFetcher
```
- Since an empty dependency list is present i.e. `[]` ---> `useEffect` will run only on first render.
- When the value in the UI is changed from _loading_ to _api values_, `useEffect` will stop running and hence the component will be unmounted from **Component Life Cycle**.

---
# Logger Component
``` jsx
import React, { useState, useEffect } from 'react';

function LoggerComponent() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('Component rendered or count changed:', count);
  });
  //runs on every render

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}


export default LoggerComponent
```
- Runs on every render as count value is changed.

---
# Multi-Effect Component
``` jsx
import React, { useState, useEffect } from 'react';

function MultiEffectComponent() {
  const [count, setCount] = useState(0);
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    console.log('Count changed:', count);
  }, [count]);
  //side-effect logic will run only when count is changed

  useEffect(() => {
    const intervalId = setInterval(() => {
        console.log("SetInterval Started")
      setSeconds(prevSeconds => prevSeconds + 1);
    }, 1000);

    return () => {
        console.log("Time to Stop");
        clearInterval(intervalId);
    }
    
  }, []);
  //it will run only on first render

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <h2>Seconds: {seconds}</h2>
    </div>
  );
}
export default MultiEffectComponent
```
- For first `useEffect`, Side-Effect Logic will run everytime count is changed.
- For second `useEffect`, Side-Effect Logic will run only on first render.

---
# Resize Window Component
``` jsx
import React, { useState, useEffect } from 'react';

function ResizeComponent() {
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => setWindowWidth(window.innerWidth);
    console.log("Event Listener Added");
    window.addEventListener('resize', handleResize);

    return () => {
      console.log("Event Listener removed");
      window.removeEventListener('resize', handleResize);
    };
  }, []);
  //it willl run only on first render

  return (
    <div>
      <h1>Window width: {windowWidth}px</h1>
    </div>
  );
}
export default ResizeComponent
```
- Since an empty dependency list is present i.e. `[]` ---> `useEffect` will run only on first render.
- No matter how many times you resize the window again, `useEffect` will not run.
- `Clean-up` function will only run when the component is **unmounted** or _removed_ from App.jsx

---
# Timer Component
``` jsx
import React, { useState, useEffect } from 'react';

function TimerComponent() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
        console.log("setInterval executed");
        setSeconds(prevSeconds => prevSeconds + 1);
    }, 1000);

    return () => {
        console.log("Time to stop");
      clearInterval(intervalId);
    };
  }, []);
  //it will run only on first render

  return (
    <div>
      <h1>Seconds: {seconds}</h1>
    </div>
  );
}

export default TimerComponent
```
- Since an empty dependency list is present i.e. `[]` ---> `useEffect` will run only on first render.
- Since it contains a `Clean-up` function ---> It stops when `<TimeComponent />` is **unmounted** or _removed_ from App.jsx

---
