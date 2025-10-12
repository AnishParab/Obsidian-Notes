# Fetch Data from Server and Display it without reloading the page
We will fetch some JSON placeholder data from this public API:
`https://jsonplaceholder.typicode.com/posts/1`

This API returns JSON like:
``` json
{
  "userId": 1,
  "id": 1,
  "title": "Sample Title",
  "body": "Sample body content here."
}
```

---
# HTML Boilerplate
``` html
<!DOCTYPE html>
<html>
<head>
  <title>AJAX Example</title>
</head>
<body>
  <h2>AJAX with XMLHttpRequest</h2>
  <button id="loadData">Load Post</button>
  <div id="result"></div>

  <script src="ajax.js"></script>
</body>
</html>
```

---
# Javascript `ajax.js`
``` js
document.getElementById("loadData").addEventListener("click", () => {
	const xhr = new XMLHttpRequest();
	xhr.open("GET", "https://jsonplaceholder.typicode.com/posts/1", true);

	xhr.onload = () => {
		if(xhr.status === 200){
			const data = JSON.parse(xhr.responseText);
			const output = `
				<h3>${data.title}</h3>
				<p>${data.body}</p>
			`;
			document.getElementById("result").innerHTML = output;
		} else {
			console.log("Error Fetching Data");
		}
	};

	xhr.onerror = () => {
		console.log("Request failed");
	};

	xhr.send();
});
```

---










