# `-w` Flag

`-w` has more variables beyond `%{http_code}`:
``` bash
-w "%{http_code}"              # extract specific response info
```

```bash
-w "%{http_code} %{time_total} %{size_download}"
```

> Useful for scripting and performance checks.

---
