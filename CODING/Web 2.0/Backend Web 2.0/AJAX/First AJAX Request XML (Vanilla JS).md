#  JSON vs XML in AJAX

| Feature      | JSON                   | XML                         |
| ------------ | ---------------------- | --------------------------- |
| Native in JS | ✅ Yes (`JSON.parse()`) | ❌ Needs manual parsing      |
| Lightweight  | ✅ Smaller              | ❌ Verbose                   |
| Readable     | ✅ Simple syntax        | 😐 Nested and tag-heavy     |
| Parsing      | `JSON.parse()`         | `DOMParser`, `.responseXML` |
| Used today   | ✅ Almost always        | ⚠️ Rare, legacy only        |

---
# We have XML API that returns this
``` xml
<user>
	<name>Anish Parab</name>
	<email>anish@gmail.com</email>
</user>
```

---
# How to handle in JS
``` js
document.getElementById("loadData").addEventListener("click", () => {
	const xhr = new XMlHttpRequest;
	xhr.open("GET", "your/api/name.xml", true);

	xhr.onload = () => {
		if(xhr.readyState === 4 && xhr.status === 200){
			const xmlDoc = xhr.responseXML;

			const name = xmlDoc.getElementByTagName("name")[0].textContent;
			const email = xmlDoc.getElementByTagName("email")[0].textContent;

			const output = `
				<h3>XML User Info</h3>
				<ul>
					<li><strong>Name:</strong>${name}</li>
					<li><strong>Email:</strong>${email}</li>
				</ul>
			`;

			document.getElementById("result").innerHTML = output;
		} else {
			console.log("Error Fetching Data");
		}
	}

	xhr.send();
});
```

---
