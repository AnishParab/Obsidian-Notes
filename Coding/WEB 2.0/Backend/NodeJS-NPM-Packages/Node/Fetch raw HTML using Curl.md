# Fetch raw HTML
``` bash
curl https://example.com

```

---
> This fetches the raw HTML of the page and prints it in your terminal. No browser, no rendering—just raw web content.

---
# To save it in a file
``` bash
curl -o page.html https://example.com

```

---
# Following Redirects
- Many sites redirect you (e.g., from `http://` to `https://`). By default, curl doesn’t follow redirects. To force it:
``` bash
curl -L http://example.com

```

---
