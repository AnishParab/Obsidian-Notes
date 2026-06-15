# Query Parameters

- Appended to the URL after `?`, used to filter/sort/paginate — never for sensitive data.
```bash
# single param
curl "http://localhost:3000/books?sort=asc"

# multiple params
curl "http://localhost:3000/books?sort=asc&limit=10&page=2"
```

- Always quote the URL in curl — `&` is a shell operator, unquoted it backgrounds the process.
```bash
# this breaks — shell interprets & as background job
curl http://localhost:3000/books?sort=asc&limit=10

# this works
curl "http://localhost:3000/books?sort=asc&limit=10"
```

- URL encoding — if param values have spaces or special chars:
```bash
# manual
curl "http://localhost:3000/books?title=the%20great%20gatsby"

# let curl encode it
curl -G http://localhost:3000/books \
  --data-urlencode "title=the great gatsby" \
  --data-urlencode "author=f scott fitzgerald"
```

`-G` moves `-d`/`--data-urlencode` values into the query string instead of the body.

---
